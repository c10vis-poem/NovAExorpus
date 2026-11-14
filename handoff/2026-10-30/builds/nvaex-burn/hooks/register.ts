import type { EngineInterface, PluginOptions, Register } from 'claude-code'

import {
  WIND_DOWN, assess, fitting, isNagDue, jobPrompt, nagText, parseQueue, readLastNag, shouldBrake,
  statusText, weekly,
} from './burn'
import type { Job, Limit } from './burn'

// Rate limits only move with usage, so a timer keeps nags going while idle.
const RECHECK_MS = 60_000

// $.store keys (kept across sessions, so a new session doesn't repeat a nag).
const OFF = 'off'
const LAST_NAG = 'lastNag'
const DONE = 'done' // { resetsAt, ids[] }: jobs started in this weekly window
const ACTIVE = 'active' // { id, braked }: the burn job running now, if any

type Done = { resetsAt: string; ids: string[] }
type Active = { id: string; braked: boolean }

type Config = {
  queueFile: string
  webhookUrl: string
  appNotify: boolean
  minLeft: number
  brakeFive: number
  brakeWeek: number
}

function config(options: PluginOptions): Config {
  const str = (k: string) => (typeof options[k] === 'string' ? (options[k] as string) : '')
  const num = (k: string, d: number) => (typeof options[k] === 'number' ? (options[k] as number) : d)
  return {
    queueFile: str('queueFile'),
    webhookUrl: str('webhookUrl'),
    appNotify: options.appNotify !== false,
    minLeft: num('minLeftPercent', 25),
    brakeFive: num('brakeFiveHour', 90),
    brakeWeek: num('brakeWeekly', 95),
  }
}

// Off when the person said /burn off, or the shared kill-switch file exists.
async function isOff($: EngineInterface): Promise<boolean> {
  if ((await $.store.get(OFF)) === true) return true
  const home = await $.env.get('HOME')
  return home !== undefined && (await $.fs.exists(`${home}/.nvaex/off`).catch(() => false))
}

async function queuePath($: EngineInterface, c: Config): Promise<string> {
  if (c.queueFile !== '') return c.queueFile
  return `${(await $.env.get('HOME')) ?? '.'}/.nvaex/burn-queue.json`
}

async function readQueue($: EngineInterface, c: Config): Promise<Job[]> {
  const path = await queuePath($, c)
  try {
    return parseQueue(await $.fs.read(path))
  } catch {
    return [] // no queue yet: nags still tell the person what's left
  }
}

async function readDone($: EngineInterface, resetsAt: string): Promise<string[]> {
  const v = (await $.store.get(DONE)) as Done | undefined
  return v && v.resetsAt === resetsAt && Array.isArray(v.ids) ? v.ids : []
}

async function readActive($: EngineInterface): Promise<Active | undefined> {
  const v = (await $.store.get(ACTIVE)) as Active | undefined
  return v && typeof v.id === 'string' ? v : undefined
}

// Every channel is best effort: a failed one never stops the others or the session.
async function tell($: EngineInterface, c: Config, text: string): Promise<void> {
  $.ui.toast(`🔥 ${text}`)
  if (c.appNotify) await $.ui.notify(text, { title: 'nvaex-burn' }).catch(() => undefined)
  if (c.webhookUrl !== '') {
    await $.http
      .fetch(c.webhookUrl, { method: 'POST', headers: { Title: 'nvaex-burn' }, body: text })
      .catch(() => undefined)
  }
}

async function startJob($: EngineInterface, job: Job, resetsAt: string): Promise<void> {
  const done = await readDone($, resetsAt)
  await $.store.set(DONE, { resetsAt, ids: [...done, job.id] })
  await $.store.set(ACTIVE, { id: job.id, braked: false })
  void $.prompt.submit({ text: jobPrompt(job) }).catch(() => undefined)
}

let latest: readonly Limit[] = []

async function check($: EngineInterface, c: Config, limits: readonly Limit[]): Promise<void> {
  latest = limits
  if (await isOff($)) {
    $.ui.status(undefined)
    return
  }

  // The brake comes first: a running burn job is wound down before anything else.
  const active = await readActive($)
  if (active && !active.braked && shouldBrake(limits, c.brakeFive, c.brakeWeek)) {
    await $.store.set(ACTIVE, { ...active, braked: true })
    await $.session.append({ message: { type: 'user', content: [{ type: 'text', text: WIND_DOWN }] } }).catch(() => undefined)
    await tell($, c, `Winding down burn job "${active.id}": a usage limit is close.`)
  }

  const now = await $.clock.now()
  const burn = assess(weekly(limits), now, c.minLeft)
  if (burn === null) {
    $.ui.status(undefined)
    return
  }

  const done = await readDone($, burn.resetsAt)
  const fits = fitting(await readQueue($, c), burn.left, done)
  $.ui.status(statusText(burn, fits.length))

  const last = readLastNag(await $.store.get(LAST_NAG))
  if (isNagDue(burn, now, last)) {
    await $.store.set(LAST_NAG, { at: now, tier: burn.tier })
    await tell($, c, nagText(burn, fits))
  }

  // Inferno alone starts anything, only a job the person marked auto, one at a time.
  if (burn.tier === 'inferno' && (active === undefined || active.braked)) {
    const auto = fits.find(j => j.gate === 'auto')
    if (auto !== undefined && !shouldBrake(limits, c.brakeFive, c.brakeWeek)) {
      await startJob($, auto, burn.resetsAt)
      await tell($, c, `Started burn job "${auto.title}" (pre-approved: auto).`)
    }
  }
}

function safe($: EngineInterface, c: Config, limits: readonly Limit[]): Promise<void> {
  // A nag is never worth breaking the session for.
  return check($, c, limits).catch(() => undefined)
}

async function answer($: EngineInterface, c: Config, args: string): Promise<string> {
  const [verb = '', ...rest] = args.trim().split(/\s+/)
  if (verb === 'off') {
    await $.store.set(OFF, true)
    $.ui.status(undefined)
    return 'nvaex-burn is off: no nags, no starts, no brake. /burn on turns it back on.'
  }
  if (verb === 'on') {
    await $.store.delete(OFF)
    await safe($, c, latest)
    return 'nvaex-burn is on.'
  }
  if (verb === 'done') {
    await $.store.delete(ACTIVE)
    return 'Cleared the running burn job.'
  }

  const usage = await $.session.usage()
  const limit = weekly(usage.rateLimits)
  if (limit === undefined) return 'No weekly limit reading yet. Send one prompt, then try /burn again.'
  const now = await $.clock.now()
  const burn = assess(limit, now, 0)
  const resetsAt = limit.resetsAt ?? ''
  const left = Math.round(100 - limit.percentUsed)
  const jobs = await readQueue($, c)
  const fits = fitting(jobs, left, await readDone($, resetsAt))

  if (verb === 'start') {
    const id = rest.join(' ')
    const job = jobs.find(j => j.id === id)
    if (job === undefined) return `No job "${id}" in ${await queuePath($, c)}.`
    if (job.gate === 'suggest') return `"${job.title}" is marked suggest. Change its gate to ask or auto to start it from here.`
    if (shouldBrake(usage.rateLimits, c.brakeFive, c.brakeWeek)) return 'A usage limit is already at the brake line, so nothing starts.'
    await startJob($, job, resetsAt)
    return `Starting "${job.title}".`
  }

  const off = (await isOff($)) ? ' (off: /burn on to resume)' : ''
  const head = burn ? statusText(burn, fits.length) : `${left}% of the week left, outside the 72-hour window.`
  const list = fits.length
    ? fits.map(j => `- ${j.id}: ${j.title} [${j.size}, ${j.gate}]${j.repo ? ` in ${j.repo}` : ''}`).join('\n')
    : `No queued job fits. Queue file: ${await queuePath($, c)}`
  return `${head}${off}\n${list}\n/burn start <id> runs an ask or auto job now · /burn off · /burn on · /burn done`
}

export const register: Register = (on, options) => {
  const c = config(options)

  on('session.start', async ($, e, next) => {
    const started = await next(e)
    await $.command.register({ name: 'burn', description: 'Weekly usage left to burn, the jobs that fit, and the off switch' })
    // A new session never inherits a running job from a closed one.
    await $.store.delete(ACTIVE)
    await safe($, c, (await $.session.usage()).rateLimits)
    $.clock.every(RECHECK_MS, () => void safe($, c, latest))
    return started
  })

  on('session.measure', async ($, e, next) => {
    if (e.changed.includes('rateLimits')) await safe($, c, e.rateLimits)
    return next(e)
  })

  on('command.run', { command: 'burn' }, async ($, e) => ({ text: await answer($, c, e.args) }))
}
