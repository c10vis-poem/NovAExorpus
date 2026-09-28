# horizons-ui / apk-snapshot

A point-in-time snapshot of the Horizons APK source tree as it existed in the
vault, plus the July-3rd APK documents.

## DO NOT DELETE — contains a frozen file

`src-restored/main/java/com/horizons/ui/HomeGrid.kt` is here.

`HomeGrid.kt` is **OPERATOR-FROZEN**. Per `Horizons-UI/CLAUDE.md`: no agent or
session touches it *for any reason* — not a layout tweak, not a "small" fix, not
a build-critical or CI-breaking fix — without the operator's explicit go-ahead.

**That freeze covers deletion, not only editing.** This snapshot was excised once
during the corpus migration under a general "corpus holds knowledge, repos hold
code" rule, and the frozen file went with it. It was caught by the content audit
and restored. The general rule does not override the freeze.

## Blob identity — read before assuming this is the frozen copy

| Copy | Blob |
|---|---|
| this vault snapshot | `6f50bf49118e75b5972c738131baea8edd44b1cc` |
| the frozen icebox copies named in `Horizons-UI/CLAUDE.md` | `618cf4b6` |

**These are different blobs.** This snapshot is *not* the frozen `984b061`
version. It is a separate copy of unconfirmed provenance. Do not treat it as the
canonical frozen `HomeGrid.kt`, and do not use it to restore or compare against
the frozen one without the operator confirming which is which.

Icebox branches holding `618cf4b6` (in `c10vis-poem/Horizons-UI`):
`FROZEN-correct-home-screen-984b0610`, `claude/homegrid-v5-tuned`,
`RELEASE-correct-home-screen-984b0610`.

## Contents

- `src-restored/` — 90 files, the Kotlin/resource tree as it sat in the vault
- `Copy of July 3rd Horizons APK.{pdf,docx}` + their `.md` conversions

## Status

`built-verified` as a historical artifact — it is a real snapshot of real code.
It says nothing about what currently runs. See
[`../../canon/STATE-OF-EXISTENCE.md`](../../canon/STATE-OF-EXISTENCE.md).
