# notebooklm-py authentication — how it works, why this device is blocked, and the real unblock path

Scope: `/data/data/com.termux/files/home/repos/notebooklm-py` (the operator's own fork,
`github.com/c10vis-poem/notebooklm-py`, source at `src/notebooklm/`) plus the runtime
state dir `~/.notebooklm/`. Device: proot Debian under Termux on Android aarch64,
X display at 672x156, Python reported as 3.13+.

**No cookie/token values are reproduced anywhere in this document — field names and
file structure only, per the incident constraint on this project.**

---

## 1. Bottom line

**The interactive Playwright login (`notebooklm login`) is not the path to pursue on
this device.** Google's own automation-signal-fusion detection blocks fresh sign-in
in an automation-launched Chromium — this is a documented, acknowledged limitation in
the project's own troubleshooting docs and code comments, not a bug this client can
fix by tweaking Playwright flags. Independently, the 672x156 X display is too small to
show Playwright's default ~1280x720 browser window, so even a successful un-blocked
attempt would likely render a broken/clipped login form. Both problems point away from
"make Playwright work here."

**The real unblock is the master-token headless auth path**
(`notebooklm login --master-token`), which needs **zero browser automation on this
device**: a human completes Google sign-in once in a genuinely real browser (the
phone's own Chrome is fine — it is not automation-controlled), the resulting
single-use `oauth_token` cookie is pasted into the CLI with `--oauth-token`, and from
then on the client mints fresh session cookies via Google's Android device-auth API
(`gpsoauth`), never touching a browser again. This sidesteps the X11/Chromium
automation-detection problem entirely because no browser automation happens in the
constrained environment at all.

**Two blockers stand between this device and that path today:**

1. **`gpsoauth` (the `[headless]` extra) is not installed.** It is pure Python, no
   native build — should install cleanly on Python 3.13+.
2. **The master-token feature (and the simpler manual `auth import-cookies` command)
   do not exist in notebooklm-py 0.7.3** — the version stated as "in play." Both
   shipped in 0.8.0 (see §3). The local checkout at `~/repos/notebooklm-py` is
   already on `0.8.0a3`, clean, tracking upstream `main`, and has both features. The
   practical fix is to run the CLI from that checkout (or `pip install` from it)
   instead of the PyPI 0.7.3 release.

**On the cookie route (`[cookies]` / rookiepy):** genuinely closed right now, not a
wheel-availability inconvenience with an easy fix. Confirmed against rookiepy's own
GitHub: [issue #53](https://github.com/thewh1teagle/rookie/issues/53) ("Installing for
python 3.13") is open, and the fix,
[PR #108](https://github.com/thewh1teagle/rookie/pull/108) ("support Python 3.13+,
replace eyre with anyhow"), is filed but **not merged**. rookiepy's latest PyPI
release (0.5.6) ships wheels only up to `cp312` for every platform, including
`manylinux_2_17_aarch64` — there is no `cp313`/`cp314` wheel anywhere, so `pip install`
falls back to a source build that fails outright (root cause per the maintainer in
that issue thread: PyO3, the Rust↔Python binding, capped at Python 3.12 until
rookiepy upgrades its PyO3 dependency). One community member reports
`PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1` lets it build from source, but this is
unverified/untested by anyone with authority in the thread — not something to rely on.

**A close second option, needing no `[headless]` install at all**, once on the
0.8.0-line checkout: `notebooklm auth import-cookies <file>` — hand-export cookies
from a real signed-in browser (e.g. via a cookie-export extension on the phone's
Chrome) and import the JSON directly. No rookiepy, no Playwright, no gpsoauth.
Simpler but doesn't self-heal on expiry the way master-token does.

---

## 2. How auth actually works (from source)

### 2.1 Three independent ways to get a session onto disk

**(a) Interactive Playwright login** — `notebooklm login`. CLI adapter:
`src/notebooklm/cli/services/playwright_login.py:428-473` (`run_playwright_login`),
delegating the actual launch/navigate/capture/persist sequence to the transport-neutral
core `src/notebooklm/_auth/browser_capture.py:462-660` (`run_browser_capture`). This is
the only mechanism that drives a real Google sign-in form.

**(b) Browser-cookie extraction via `rookiepy`** — `notebooklm login --browser-cookies
<browser>`. Reads an *already signed-in* browser's cookie database directly (no
Playwright, no sign-in flow). Conversion: `src/notebooklm/_auth/cookies.py:113-160`
(`convert_rookiepy_cookies_to_storage_state`). Gated behind the optional `[cookies]`
extra (`rookiepy>=0.1.0,<1`, `pyproject.toml:45`), deliberately excluded from the
`all` extras bundle (`pyproject.toml:89-91`) specifically because of the Python 3.13+
build failure.

**(c) Master-token headless mint** — `notebooklm login --master-token`. No browser at
runtime at all. `src/notebooklm/_auth/master_token.py` implements the whole flow:
`exchange_master_token` (lines 102-118) turns a single-use `oauth_token` into a durable
`aas_et/` master token via `gpsoauth.exchange_token`; `mint_cookies` (lines 121-214)
uses `gpsoauth.perform_oauth` (impersonating the Chromecast Android app,
`_MASTER_APP`/`_MASTER_SIG` at lines 42-43) to get a bearer token, then walks
`OAuthLogin?issueuberauth=1 → uberauth → MergeSession` against
`accounts.google.com` to mint a full `SID`/`APISID`/`SAPISID`/`__Secure-1PSID` cookie
jar (lines 159-201), and best-effort mints `__Secure-1PSIDTS` via the same
`RotateCookies` POST the keepalive path uses (lines 178-198). This is documented and
justified in `docs/adr/0023-master-token-headless-auth.md`.

A fourth, dependency-free route also exists:

**(d) Manual cookie-JSON import** — `notebooklm auth import-cookies <path>`,
implemented in `src/notebooklm/cli/_cookie_import.py`. Accepts either a bare JSON list
of cookie objects (the shape common cookie-export browser extensions produce — fields
normalized at `_normalize_imported_cookie`, `_cookie_import.py:70-97`, e.g.
`expirationDate` → `expires`) or a full Playwright `storage_state` object
(`{"cookies": [...], "origins": [...]}`). It filters through the same domain allowlist
as the Playwright/rookiepy paths, validates the required-cookie set, and atomically
writes `storage_state.json`, backing up any pre-existing file to `<name>.bak` first
(`_cookie_import.py:130-146`). CLI wiring: `src/notebooklm/cli/session_cmd.py:689-759`.
No Playwright, no rookiepy — a hand-obtained cookie export is enough.

### 2.2 Google-account cookies vs. the durable master token — two different secrets

The everyday secret is the **Google session cookie jar** (`storage_state.json`) —
short-lived, rotated, revocable by a password change. The master-token path adds a
**second, much more sensitive secret**: the durable `aas_et/` token in
`master_token.json`, which survives password changes and is described in the code and
docs as "full-account, durable, infostealer-grade" (`master_token.py:19-21`,
ADR-0023 Consequences). The project's own security guidance is to use a
**dedicated/throwaway Google account** for this path, never the operator's primary
account.

### 2.3 The `~/.notebooklm/profiles/` store — structure only, no values

Layout (`src/notebooklm/paths.py:1-65`, docstring + `__all__`):

```
~/.notebooklm/
├── config.json                       # {"default_profile": "<name>"} (paths.py:147-188)
├── .migration.lock                   # empty sentinel; legacy→profile migration marker
└── profiles/
    └── <profile-name>/                # e.g. "default"
        ├── storage_state.json         # Playwright cookie/session state (see below)
        ├── master_token.json          # durable master-token record (mode 0600)
        ├── context.json                # selected notebook/conversation, NOT auth
        └── browser_profile/            # Chromium persistent-context user-data-dir
```

Path resolution precedence: explicit `profile=` arg → `NOTEBOOKLM_PROFILE` env var →
`config.json`'s `default_profile` → `"default"` (`paths.py:191-215`,
`resolve_profile`). Legacy (pre-profile) installs fall back to the home-root files if
the profile-scoped path doesn't exist yet (`paths.py:253-273`, `_legacy_fallback`).

**`storage_state.json` schema** (Playwright's native format; produced/consumed at
`src/notebooklm/_auth/cookies.py:113-160`, `:502-513` `_cookie_to_storage_state`,
`:516-548` `_storage_entry_to_cookie`):

```json
{
  "cookies": [
    {
      "name": "...", "value": "...", "domain": "...", "path": "/",
      "expires": -1, "httpOnly": false, "secure": true, "sameSite": "None"
    }
  ],
  "origins": [],
  "notebooklm": {
    "version": 1,
    "account": {"authuser": 0, "email": "..."}
  }
}
```

The trailing `notebooklm` key is an account-identity namespace this client adds on top
of Playwright's own `{cookies, origins}` shape (`_auth/master_token.py:217-231`
`storage_state_from_jar`; also written by `_auth/account.py`'s
`write_account_metadata`, referenced from `auth.py:207-220`).

Minimum required cookie *names* for the client to accept a session:
`{"SID", "__Secure-1PSIDTS"}` (`_auth/cookie_policy.py:38`, `MINIMUM_REQUIRED_COOKIES`),
plus one of two "secondary binding" pairs — `OSID` alone, or both `APISID` and
`SAPISID` (`_auth/cookie_policy.py:71-86`, `_has_valid_secondary_binding`) — or the
client logs a warning that the session is fragile.

**`master_token.json` schema** (`_auth/master_token.py:273-306`,
`read_master_token`/`write_master_token`):

```json
{
  "version": 1,
  "email": "...",
  "android_id": "...",
  "master_token": "..."
}
```

Written at file mode `0600` via a hidden `.master_token.json.tmp` + atomic rename
(`master_token.py:301-305`). `android_id` is a random 64-bit hex value generated once
per install (`generate_android_id`, `master_token.py:95-99`) and must be reused across
re-mints — changing it can re-trip Google's new-device risk signal.

**`NOTEBOOKLM_AUTH_JSON`** is a fourth on-disk-free option: set it to the full
`storage_state.json` contents and the loader (`_auth/cookies.py:262-320`,
`_load_storage_state`) uses it in place of any file, taking precedence over the
profile path. `save_cookies_to_storage` is a deliberate no-op when this env var is set
(`_auth/storage.py:369-379`) — there is nothing to write back to.

### 2.4 Playwright launch options (interactive login)

`_auth/browser_capture.py:511-525`:

```python
launch_kwargs = {
    "user_data_dir": str(browser_profile),
    "headless": headless,
    "args": [
        "--disable-blink-features=AutomationControlled",
        "--password-store=basic",
    ],
    "ignore_default_args": ["--enable-automation"],
}
if browser in CHANNEL_BROWSERS:      # "chrome" / "msedge" (browser_capture.py:113-116)
    launch_kwargs["channel"] = browser
context = p.chromium.launch_persistent_context(**launch_kwargs)
```

This is the **only** de-automation applied: dropping the `--enable-automation` info
bar and the `AutomationControlled` Blink feature flag (so `navigator.webdriver` reads
false). No stealth library, no fingerprint patching. This is a deliberate,
documented choice — `docs/auth-cookie-lifecycle.md:830-843` ("A3 · Ruled-out
experiments") records that `undetected-chromedriver`/`selenium-stealth` and
`puppeteer-extra-plugin-stealth`/`playwright-stealth` were investigated and rejected:
*"WebDriver stealth loses to Google's signal-fusion model; login has been repeatedly
broken across Chrome bumps"* and stealth patches *"work for resumed sessions, fail for
fresh `accounts.google.com` sign-in."*

**No `viewport` or `no_viewport` argument is passed anywhere in `launch_kwargs`,** and
a repo-wide search of `src/notebooklm/` for `viewport`, `window-size`/`window_size`,
and `no-sandbox` turns up nothing outside this one unrelated HTML `<meta>` tag hit —
there is no CLI flag, env var, or config knob to override the browser window size.
Per Playwright's own docs (`playwright.dev/python/docs/api/class-browsertype`, the
`launch_persistent_context` `viewport` parameter): *"Sets a consistent viewport for
each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed
viewport."* Because `no_viewport` isn't passed either, Playwright enforces a fixed
~1280x720 logical viewport regardless of the OS window; separately, the actual
Chromium **window** Playwright opens still has to be placed somewhere by the X window
manager, and a 672x156 physical display cannot show a 1280x720 window without clipping
or letterboxing it.

**Browser channels available:** `"chromium"` (bundled, no channel override) or, via
`CHANNEL_BROWSERS` (`browser_capture.py:113-116`), `"chrome"` / `"msedge"` — real
system-installed Chrome/Edge driven through the same Playwright automation, not a
separate non-automated path.

**CDP-attach** (connecting Playwright to an *already-running*, human-launched Chrome
via `--remote-debugging-port`) exists in this codebase, but only in two other places,
**not** for the main `notebooklm login` flow:
- `capture_oauth_token`'s `--cdp-url` option
  (`cli/services/login/master_token.py:118-165`), used only for the master-token
  `oauth_token` capture step.
- `NOTEBOOKLM_HEADLESS_REAUTH_CDP_URL`, used only by the client's automatic **recovery**
  of an already-established session (`docs/auth-cookie-lifecycle.md:495-505`,
  "L3 — headless re-auth / CDP attach"), not initial login.

---

## 3. Why the current attempt fails

### Confirmed (primary source)

- **Google blocks the automated Chromium at sign-in.** The project's own
  troubleshooting doc states the cause plainly: `docs/troubleshooting.md:168-176`,
  *"Browser opens but login fails / Cause: Google detecting automation and blocking
  login,"* with remediation steps (clear the persistent profile, retry, solve any
  CAPTCHA, use a real mouse/keyboard). The master-token oauth-capture code has the
  same acknowledgment inline:
  `cli/services/login/master_token.py:151-156` — *"Google refuses sign-in in browsers
  that advertise automation ('This browser or app may not be secure'). Drop the
  --enable-automation banner and the AutomationControlled blink feature... This is the
  minimal de-automation, not a stealth library... if Google still blocks, use
  --cdp-url (your own Chrome) or --oauth-token."* This is the maintainer's own
  acknowledged, permanent limitation, not a misconfiguration in this fork.
- **rookiepy's Python 3.13+ block is real and currently unresolved upstream**, not a
  packaging quirk local to this device. rookiepy 0.5.6 on PyPI ships wheels only up to
  `cp312` for every platform (including `manylinux_2_17_aarch64` — Linux aarch64 *is*
  otherwise supported, just not on 3.13+). GitHub
  [thewh1teagle/rookie#53](https://github.com/thewh1teagle/rookie/issues/53)
  ("Installing for python 3.13") is open; the fix,
  [PR #108](https://github.com/thewh1teagle/rookie/pull/108), is filed but unmerged.
  Root cause per the maintainer in that thread: PyO3 (the Rust↔Python bridge) caps
  supported Python at 3.12 until rookiepy bumps its PyO3 dependency. The
  notebooklm-py project's own docs concur: `docs/installation.md:78-84,136`,
  `pyproject.toml:89-91`.
- **This checkout is the operator's own fork, clean, and ahead of the "0.7.3 in
  play" version.** `git -C ~/repos/notebooklm-py remote -v` → `origin
  https://github.com/c10vis-poem/notebooklm-py.git` (fetch+push); `git status` →
  `On branch main / up to date with origin/main / nothing to commit, working tree
  clean`; `pyproject.toml:3` → `version = "0.8.0a3"`.
- **notebooklm-py 0.7.3 does not have `auth import-cookies` or
  `login --master-token`.** `CHANGELOG.md:781-809` describes 0.7.3 explicitly:
  *"Maintenance patch on the 0.7.x line. Backports fixes from `main` (cherry-picked
  ahead of the v0.8.0 breaking release)"* — and lists exactly three backported fixes
  (a markdown-upload MIME fix, an anti-abuse-redirect error message, and a Playwright
  `wait_until="commit"` fix for the "Login not detected within 5 minutes" hang).
  `auth import-cookies` (GitHub PR
  [#1626](https://github.com/teng-lin/notebooklm-py/pull/1626), merged
  2026-06-24, one day before 0.7.3's 2026-06-29 release) is **not** in that backport
  list, and master-token auth (ADR-0023) is mentioned only inside the `[0.8.0]`
  CHANGELOG section (`CHANGELOG.md:23-780` range, well before the `[0.7.3]` header at
  line 781). Both are 0.8.0-line-only features present in the local
  `~/repos/notebooklm-py` checkout.
- **No display available is the maintainers' own documented case, with the same
  answer this report gives:** `docs/troubleshooting.md:679-681`, *"No display
  available (headless server): Browser login requires a display. Authenticate on a
  machine with GUI, then copy `storage_state.json`."* Independently, a user of the
  project reported the identical sandboxed-agent situation in
  [GitHub issue #1856](https://github.com/teng-lin/notebooklm-py/issues/1856)
  ("Support for sandboxed agent environments (Claude Cowork)") and confirmed the
  working pattern is: log in once on a machine with a display, move
  `storage_state.json` over (or set `NOTEBOOKLM_AUTH_JSON`), and everything except
  `login` itself needs no browser.
- **`~/.notebooklm/profiles/default/` currently has only a leftover
  `browser_profile/` directory** (dated Jul 12) from a prior attempt — no
  `storage_state.json`, no `master_token.json`, no `config.json` exist yet
  (confirmed by directory listing; contents not inspected).

### Hypothesis (plausible, not independently confirmed)

- That the specific rejection text the operator saw was literally Google's "This
  browser or app may not be secure" screen, as opposed to some other failure — the
  task description characterizes it that way, and it matches the exact phrase
  reproduced in the project's own code comment
  (`cli/services/login/master_token.py:151`), but this report did not independently
  observe on-device logs/screenshots to confirm the exact string.
- That the degenerate 672x156 display *by itself*, with an otherwise-succeeding
  automation-tolerant sign-in, would have been sufficient to cause the failure seen —
  plausible given Playwright's fixed-viewport default and the absence of any
  `no_viewport`/window-size override in this codebase, but not separable from the
  automation-detection cause without actually running a (disallowed) login attempt.
  Both causes may well have fired simultaneously.

---

## 4. Concrete unblock procedure

**Recommended path: master-token headless auth, run from the local fork checkout.**

1. **(operator, in this environment)** Point the CLI at the local checkout instead of
   the PyPI 0.7.3 install, so `auth import-cookies` / `login --master-token` exist:
   ```
   pip install -e /data/data/com.termux/files/home/repos/notebooklm-py
   pip install "notebooklm-py[headless]"    # adds gpsoauth (pure Python)
   ```
   (`pyproject.toml:54`: `headless = ["gpsoauth>=1.1.0"]` — no native/Rust build,
   unlike rookiepy, so this should install cleanly on Python 3.13+.)

2. **(operator, in a real, non-automated browser — the phone's own Chrome is fine)**
   Sign in at **`https://accounts.google.com/EmbeddedSetup`**. Use a **dedicated /
   throwaway Google account**, not the operator's primary one — the master token this
   produces is durable and full-account-scoped
   (`_auth/master_token.py:19-21`; ADR-0023 "Consequences" section).

3. **(operator, same real browser)** After sign-in, open that browser's cookie
   inspector (e.g. Chrome DevTools → Application → Cookies →
   `accounts.google.com`, or a cookie-export extension) and copy the value of the
   **`oauth_token`** cookie. It is single-use and short-lived — capture it and move to
   the next step promptly. **Do not paste this value into any chat, log, or shared
   terminal** — only into the CLI invocation below, on-device.

4. **(operator, back in the proot Debian environment)** Run:
   ```
   notebooklm login --master-token --account <the-throwaway-email> --oauth-token <captured-value>
   ```
   This performs no browser automation at all — `exchange_master_token` +
   `mint_cookies` (`_auth/master_token.py:102-214`) are plain HTTPS/gpsoauth calls.
   It writes `~/.notebooklm/profiles/default/master_token.json` (mode 0600) and
   `storage_state.json`.

5. **Verify:**
   ```
   notebooklm auth check --test --json
   ```
   Require `"status": "ok"` **and** `"checks": {"token_fetch": true}` — a bare
   `auth check --json` only proves the file parses, not that the cookies still
   authenticate (per `docs/installation.md:110`).

6. **Ongoing use needs no further browser interaction.** Sessions self-heal: an
   expired `storage_state.json` beside a `master_token.json` triggers an automatic
   in-process re-mint (ADR-0023, layer-4 recovery). A manual re-mint is available any
   time via `notebooklm login --master-token-refresh`.

**Faster / lower-risk stopgap, if a second machine with a real display is reachable
at all** (no code/version change needed, works even on stock 0.7.3): run
`notebooklm login` once on that machine, then copy
`~/.notebooklm/profiles/default/storage_state.json` from it into this device's
`~/.notebooklm/profiles/default/storage_state.json` — or set
`NOTEBOOKLM_AUTH_JSON` to the file's contents. This is the maintainers' own
documented answer for "no display" (`docs/troubleshooting.md:679-681`,
`docs/installation.md` Persona D). Downside: this cookie session is not durable and
will eventually need to be refreshed the same way.

**Alternative to the master token, once on the 0.8.0-line checkout, no `[headless]`
extra needed:** export cookies from a real signed-in browser via a cookie-export
extension (JSON list of `{name, value, domain, path, expirationDate/expires,
httpOnly, secure, sameSite}` objects, or a full Playwright `storage_state.json`), copy
that file onto the device, then:
```
notebooklm auth import-cookies <path-to-exported-cookies.json>
```
(`cli/_cookie_import.py`, `cli/session_cmd.py:689-759`). Simpler than the master-token
path and needs no extra dependency, but the resulting session is an ordinary cookie
jar — it will eventually expire and need re-export, unlike the master-token path's
automatic re-mint.

**Before attempting the interactive Playwright flow again at all** (not recommended
as primary, but if attempted): clear the stale profile first
(`rm -rf ~/.notebooklm/profiles/default/browser_profile/` — this directory currently
holds a leftover profile from a prior failed attempt) and fix the X11 display size to
at least 1280x720, since Playwright enforces that viewport by default regardless of
outcome on the automation-detection front (`docs/troubleshooting.md:168-176`).

---

## 5. What is unverified

- **The exact text of the rejection actually seen on this device.** This report relies
  on the task's characterization ("unsupported browser" / "this browser or app may not
  be secure") and the matching string found in the project's own code comment; it was
  not independently confirmed against a device log or screenshot.
- **Whether fixing the X11 display size alone (without also solving automation
  detection) would let the existing Playwright flow succeed.** Not testable without
  running a login attempt, which was out of scope for this investigation.
- **Whether `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1` actually lets rookiepy build on
  this specific aarch64 proot Debian setup.** This is a single unverified community
  report in the upstream rookiepy issue thread, not confirmed by the rookiepy
  maintainer, and not tested here.
- **Whether `gpsoauth` truly has zero native/build dependencies on aarch64.** The
  `pyproject.toml:50-54` comment asserts "pure-Python (no native wheels)," but this
  report did not independently inspect gpsoauth's own dependency tree or attempt an
  install (installs were out of scope / disallowed for this task).
- **Whether PR #1626/#1629 (`auth import-cookies`) and ADR-0023 (master-token) shipped
  cleanly in the first 0.8.0 PyPI release**, versus still being pre-release-only at
  publish time. This report confirmed both are merged to `main` well before the
  `chore: release v0.8.0a1` commit visible in `git log`, but did not check PyPI's
  actual file listing for a stable `0.8.0` release.
- **The exact installed Python version on this device.** Per the task, "Python 3.13+"
  was already established prior to this investigation; it was not re-verified here.
- **Whether the operator has access to any second machine with a real display**,
  which would make the "copy `storage_state.json` over" stopgap in §4 immediately
  actionable rather than merely theoretical.
