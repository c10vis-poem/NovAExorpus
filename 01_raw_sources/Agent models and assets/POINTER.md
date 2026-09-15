# Agent models and assets — intentionally not in git

This folder holds device-local runtime assets (compiled model weights,
SDK/runtime tarballs — e.g. hybrid_llama_qnn.pte at ~930MB, several
70-90MB compiled binaries/tarballs). These exceed GitHub's 100MB
per-file limit and are bad practice to version in git regardless
(no meaningful diffing, permanent repo bloat).

This matches the architecture's own design: model weights are meant to
be Load Only, streamed from local device storage via mmap, never
bundled into a repo/APK. Keep these device-local; do not commit them
here even if the exclusion is later removed for other reasons.
