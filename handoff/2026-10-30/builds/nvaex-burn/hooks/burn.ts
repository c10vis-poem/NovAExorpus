// Pure parts of nvaex-burn: no `$`, so they test without an engine.
// The tier logic is adapted from burn-baby-burn (eel-brah, MIT) and the
// wake-time rounding from cache-caffeine (lperezmo, MIT).

export type Limit = { kind: string; percentUsed: number; resetsAt?: string }
export type Tier = 'smoulder' | 'blaze' | 'inferno'
export type Burn = { tier: Tier; left: number; msLeft: number; resetsAt: string }
export type Gate = 'suggest' | 'ask' | 'auto'
export type Size = 'S' | 'M' | 'L'
export type Job = { id: string; title: string; prompt: string; size: Size; gate: Gate; repo?: string }
export type LastNag = { at: number; tier: Tier }

const HOUR = 60 * 60 * 1000

// How long before the reset each tier starts, and how often it may nag.
const TIERS: { tier: Tier; within: number; every: number }[] = [
  { tier: 'inferno', within: 6 * HOUR, every: 30 * 60 * 1000 },
  { tier: 'blaze', within: 24 * HOUR, every: 2 * HOUR },
  { tier: 'smoulder', within: 72 * HOUR, every: 24 * HOUR },
]

// Roughly how much of the week each job size spends, in percentage points.
export const SIZE_COST: Record<Size, number> = { S: 5, M: 15, L: 30 }

export const WIND_DOWN =
  '[nvaex-burn] WIND DOWN: the usage limit is close. Finish the current step, commit what is done, ' +
  'write a short resume note (state, next step) beside the work, and stop. Start nothing new.'

export function weekly(limits: readonly Limit[]): Limit | undefined {
  return limits.find(l => l.kind === 'seven_day')
}

export function fiveHour(limits: readonly Limit[]): Limit | undefined {
  return limits.find(l => l.kind === 'five_hour')
}

export function assess(limit: Limit | undefined, now: number, minLeft: number): Burn | null {
  if (limit?.resetsAt === undefined) return null
  const msLeft = Date.parse(limit.resetsAt) - now
  const left = Math.round(100 - limit.percentUsed)
  if (Number.isNaN(msLeft) || msLeft <= 0 || left < minLeft) return null
  // Tightest first, so the first match is the hottest.
  const match = TIERS.find(t => msLeft <= t.within)
  return match ? { tier: match.tier, left, msLeft, resetsAt: limit.resetsAt } : null
}

export function readLastNag(value: unknown): LastNag | undefined {
  if (typeof value !== 'object' || value === null) return undefined
  const { at, tier } = value as Record<string, unknown>
  if (typeof at !== 'number' || !Number.isFinite(at)) return undefined
  if (!TIERS.some(t => t.tier === tier)) return undefined
  return { at, tier: tier as Tier }
}

// A hotter tier always nags; otherwise once per the tier's interval.
export function isNagDue(burn: Burn, now: number, last: LastNag | undefined): boolean {
  if (last === undefined || last.tier !== burn.tier) return true
  const every = TIERS.find(t => t.tier === burn.tier)?.every ?? 24 * HOUR
  return now - last.at >= every
}

// Store and file values are untrusted: a malformed job is dropped, never guessed at.
export function parseQueue(text: string): Job[] {
  let raw: unknown
  try {
    raw = JSON.parse(text)
  } catch {
    return []
  }
  const list = Array.isArray(raw) ? raw : (raw as { jobs?: unknown })?.jobs
  if (!Array.isArray(list)) return []
  const jobs: Job[] = []
  for (const item of list) {
    if (typeof item !== 'object' || item === null) continue
    const { id, title, prompt, size, gate, repo } = item as Record<string, unknown>
    if (typeof id !== 'string' || id === '' || typeof prompt !== 'string' || prompt === '') continue
    jobs.push({
      id,
      title: typeof title === 'string' && title !== '' ? title : id,
      prompt,
      size: size === 'S' || size === 'M' || size === 'L' ? size : 'M',
      gate: gate === 'ask' || gate === 'auto' ? gate : 'suggest',
      ...(typeof repo === 'string' && repo !== '' ? { repo } : {}),
    })
  }
  return jobs
}

// Jobs that fit what is left, biggest first, skipping ones already run this week.
export function fitting(jobs: readonly Job[], left: number, done: readonly string[]): Job[] {
  return jobs
    .filter(j => !done.includes(j.id) && SIZE_COST[j.size] <= left)
    .sort((a, b) => SIZE_COST[b.size] - SIZE_COST[a.size])
}

// The brake holds when either window is at or past its line.
export function shouldBrake(limits: readonly Limit[], fiveHourAt: number, weeklyAt: number): boolean {
  const five = fiveHour(limits)
  const week = weekly(limits)
  return (five !== undefined && five.percentUsed >= fiveHourAt) || (week !== undefined && week.percentUsed >= weeklyAt)
}

export function formatLeft(ms: number): string {
  const hours = Math.floor(ms / HOUR)
  const days = Math.floor(hours / 24)
  if (days > 0) return `${days}d ${hours % 24}h`
  if (hours > 0) return `${hours}h ${Math.floor((ms % HOUR) / 60000)}m`
  return `${Math.max(1, Math.floor(ms / 60000))}m`
}

const FLAMES: Record<Tier, string> = { smoulder: '🔥', blaze: '🔥🔥', inferno: '🔥🔥🔥' }

export function statusText(burn: Burn, fitCount: number): string {
  return `${FLAMES[burn.tier]} ${burn.left}% of the week left · resets in ${formatLeft(burn.msLeft)} · ${fitCount} job${fitCount === 1 ? '' : 's'} fit`
}

export function nagText(burn: Burn, fits: readonly Job[]): string {
  const head = `${burn.left}% of your weekly limit is unspent and resets in ${formatLeft(burn.msLeft)}.`
  if (fits.length === 0) return `${head} No queued job fits; add one to your burn queue.`
  const top = fits.slice(0, 3).map(j => `${j.title} (${j.size}, ${j.gate})`).join('; ')
  return `${head} Jobs that fit: ${top}. Run /burn to see them.`
}

export function jobPrompt(job: Job): string {
  const where = job.repo ? ` in ${job.repo}` : ''
  return `[nvaex-burn] Burn job "${job.title}"${where}: ${job.prompt}`
}
