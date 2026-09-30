# pending-corpora / transcripts

AI-assistant conversation logs. **Not canon.** Held under Rule 5 (*Pending Corpora,
Not Discard*): hallucinated specifics do not justify discarding a document, because
the operator's own turns inside it are canon-grade and the model's unorthodox
suggestions are sometimes the useful ones.

## How to read anything in here

A transcript has **two kinds of content**, and they have opposite status:

| | Status | Where it goes |
|---|---|---|
| **Operator turns** | **canon-grade** — the operator's own words | quoted verbatim, with attribution, into `canon/` |
| **Assistant prose** | **unverified** — plausible, often confidently wrong | stays here; promoted only with independent verification |

The tell is usually visible in the transcript itself: the operator correcting the
assistant. Those corrections are the highest-value lines in the file.

## Contents

### `gemini-architecture-thread-2026-08-04.{pdf,md}`
The Aug 4–5 2026 thread. **The single most load-bearing source recovered so far.**
The operator corrects the assistant's architecture document **twice**:

- *"Again, dude, everything's at 2:00, 4:00, 6:00, 8:00, 10:00, and 12:00."*
- *"You left out the monitor and the browser. And you left out the whole chat interface."*
- *"No, you just made up some of that shit. So, that 4 OS level permissions in Boost
  Layer. I don't know what that's all about."*
- *"We're not using Piper. We're using Coqui, Sherpa ONNX, Silero VAD, and Whisper base."*
- *"I'm already going to have two freaking models bouncing back and forth on the NPU."*
- *"It operates with launch demons and recovery demon, and it also has a slight time to…"*

Extracted to canon:
- `canon/horizons-ui/CLOCK-FACE.md` — the six-room layout
- `canon/aesop/PARAMETER-PACKET.md` — the four layers, daemons, zero-TTL
- `canon/STATE-OF-EXISTENCE.md` — the repo audit

**Left here as unverified:** the assistant's model-sizing figures, the Kotlin code
samples, the ASCII architecture diagrams (which it drew wrong twice before the
operator corrected it), and the APK-size guidance.

> The `.md` is a text extraction of the `.pdf`, made with the PDF's own embedded
> `ToUnicode` maps. The subset fonts mangle a few glyph pairs — some `fi`/`fl`/`ffi`
> ligature slots carry `L`/`M`/`N`/`O`, and `→` stands in for `v`. **The `.pdf` is
> the authority**; use the `.md` for grep and quoting, and check the PDF before
> relying on an exact string.

### `gemini-metaphor-drift-analysis.md`
Assistant analysis of how conversational metaphors were over-literalised into
brittle code. **The diagnosis is sound and became Rule 7** — but it is the
assistant's framing of the operator's position, not the operator's own words. The
underlying operator statements are in the thread above.

### `gemini-dynamic-params-proposal.md`
Assistant proposal for `fuse-config-schema.json`, `VoicePipelineCoordinator.kt`,
and `validate_repo_integrity.py`. **None of these were built** — see
`canon/STATE-OF-EXISTENCE.md`. Kept because the *shape* of the argument
(device-agnostic packets, no hardcoded device targets) matches canon, and the
zero-trust repo verifier is close to the mechanical check the corpus needs.

Treat every file path, class name, and "now available in your Studio panel" claim
in it as **`absent` until proven otherwise.**
