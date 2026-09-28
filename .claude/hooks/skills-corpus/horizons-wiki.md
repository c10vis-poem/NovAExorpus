---
name: horizons-wiki
description: "Horizons Android app — architecture, UI, NPU routing, and on-device AI backend. Use when working on the Horizons Kotlin/Compose app, its HomeGrid UI, theme system, font resources, NPU/HTP integration, or the loopback bridge to Termux."
---

# Horizons Wiki

## What Horizons Is

Horizons is an Android app (Kotlin, Jetpack Compose, WebView hybrid) that serves as the **frontend and NPU gateway** for an on-device AI stack running on Snapdragon 8 Elite. It owns the app-context vendor libraries that Termux cannot reach, and exposes them over HTTP on loopback.

## Architecture — Loopback Bridge

| Port | Owner | Service |
|------|-------|---------|
| 8080 | **Horizons** (app) | `ort_engine` — GENIE-compiled NPU contexts |
| 8081 | **Termux** | `llamad` → llama-server — Gemma 4 12B Q4_0 |
| 8091 | **Horizons** (app) | Media pipeline — Moonshine STT / Kokoro TTS |
| 8765 | **Termux** | `aesopd` WebSocket bridge |

**Port discipline is non-negotiable.** Collisions are silent and fatal.

Termux **cannot** reach the Hexagon DSP. See `termux-helper` skill Part 2.

## Future: Kotlin-Accessible llama.cpp

Next mission: Horizons hosts a lightweight Kotlin-accessible llama.cpp that Termux agents call into, hitting HTP backend through the app's vendor lib access. Turns Horizons into a true backend router.

## UI — HomeGrid (v5, complete)

Commit `984b061` on `claude/homegrid-v5-tuned` (PR #31).

### Layout
- TILE_INSET = 42.dp, TOP_LIFT = 28.dp, HUB_LIFT = 28.dp
- LOGO_DP = 56.dp (renders at 42dp via 0.75 multiplier), SLOGAN_DP = 16.dp
- ROUTER plate offset: `crystalSize * 0.97f + 40.dp`

### Typography — Static Font Instances

Variable fonts with `fontVariationSettings` through XML resources are unreliable in Compose. Static instances with baked-in weight values are the solution.

| Font | Weight | Use |
|------|--------|-----|
| Orbitron ExtraBold 800 | `orbitron_extrabold_static.ttf` | Wordmark, "(Next-Gen Certified)" |
| Google Sans Code Normal 400 | `google_sans_code_regular_static.ttf` | Strapline "*Pioneer_Tech," |

**Orbitron has no U+00D8 (Ø) glyph.** Always use plain O.

Type sizes use dp (not sp) to avoid device font-scale clipping.

### Colors (inline, not from theme)

| Tile | Color |
|------|-------|
| Chat | #4FE9A6 |
| Horizons | #40C4FF |
| Settings | #FF5577 |
| Terminal | #00FF41 |
| Archives | #E8A838 |

### Starfield
- BgStar data class with 4 depth tiers
- Cross-glint on tier 3 stars
- Subtle twinkle: brightness 0.94–1.00, 7.6s cycle
- Telemetry clusters encircle twinkling stars

## Known Issues

- **Startup crash (~10s):** Breadcrumb.kt full-file read on FGS deadline path. Fix pushed, not confirmed on device.
- **Theme colors stale:** HorizonsTheme.kt doesn't match V5 inline palette.

## Branches

| Branch | Purpose |
|--------|---------|
| `claude/homegrid-v5-tuned` | Active development, PR #31 |
| `claude/homegrid-v5-SNAPSHOT-good-1837dc2` | Pre-tuning snapshot |

## Credit

Mer0vin8ian Production — Cl0vis/Claude collab.