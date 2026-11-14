import { expect, test } from 'claude-code/testing'

import { assess, fitting, isNagDue, parseQueue, shouldBrake } from './burn'

const H = 60 * 60 * 1000
const NOW = Date.parse('2026-10-30T00:00:00Z')
const at = (ms: number) => new Date(NOW + ms).toISOString()

test('tiers follow the time to reset and the share left', async () => {
  expect(assess({ kind: 'seven_day', percentUsed: 40, resetsAt: at(5 * H) }, NOW, 25)?.tier).toBe('inferno')
  expect(assess({ kind: 'seven_day', percentUsed: 40, resetsAt: at(20 * H) }, NOW, 25)?.tier).toBe('blaze')
  expect(assess({ kind: 'seven_day', percentUsed: 40, resetsAt: at(60 * H) }, NOW, 25)?.tier).toBe('smoulder')
  expect(assess({ kind: 'seven_day', percentUsed: 40, resetsAt: at(100 * H) }, NOW, 25)).toBe(null)
  expect(assess({ kind: 'seven_day', percentUsed: 90, resetsAt: at(5 * H) }, NOW, 25)).toBe(null)
})

test('a hotter tier nags at once, the same tier waits its interval', async () => {
  const burn = { tier: 'blaze' as const, left: 50, msLeft: 10 * H, resetsAt: at(10 * H) }
  expect(isNagDue(burn, NOW, { at: NOW - 60_000, tier: 'smoulder' })).toBe(true)
  expect(isNagDue(burn, NOW, { at: NOW - 60_000, tier: 'blaze' })).toBe(false)
  expect(isNagDue(burn, NOW, { at: NOW - 3 * H, tier: 'blaze' })).toBe(true)
})

test('the queue drops malformed jobs and fits by size, skipping done ones', async () => {
  const jobs = parseQueue(JSON.stringify({ jobs: [
    { id: 'a', prompt: 'big', size: 'L', gate: 'auto' },
    { id: 'b', prompt: 'mid', size: 'M' },
    { id: 'c', prompt: 'small', size: 'S', gate: 'ask' },
    { id: '', prompt: 'no id' },
    { id: 'd' },
  ] }))
  expect(jobs.map(j => j.id)).toEqual(['a', 'b', 'c'])
  expect(jobs[1]?.gate).toBe('suggest')
  expect(fitting(jobs, 20, []).map(j => j.id)).toEqual(['b', 'c'])
  expect(fitting(jobs, 60, ['a']).map(j => j.id)).toEqual(['b', 'c'])
  expect(parseQueue('not json')).toEqual([])
})

test('the brake holds at either line', async () => {
  expect(shouldBrake([{ kind: 'five_hour', percentUsed: 91 }], 90, 95)).toBe(true)
  expect(shouldBrake([{ kind: 'seven_day', percentUsed: 96 }], 90, 95)).toBe(true)
  expect(shouldBrake([{ kind: 'five_hour', percentUsed: 50 }, { kind: 'seven_day', percentUsed: 50 }], 90, 95)).toBe(false)
})
