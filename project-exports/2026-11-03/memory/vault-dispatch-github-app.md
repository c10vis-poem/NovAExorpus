---
name: vault-dispatch-github-app
description: VAULT_DISPATCH_TOKEN PAT being replaced by a GitHub App (NovAExorpus tools/vault-app/setup.sh); 6 draft PRs opened 2026-10-25
metadata:
  type: project
  modified: 2026-10-25T20:30:27.091Z
---
The master-files workflow in NovAExorpus was retired 2026-10-20 (commit 85526f4). The PAT secret `VAULT_DISPATCH_TOKEN` was then used only by `notify-vault.yml` in NovAExopia, Hyperion-XI, CloviX-AEyre, AEthX-AEsc, NovusAExenti (dispatch `base-repo-updated` to NovAExorpus, which has no receiver yet).

2026-10-25: draft PRs replace it with a private GitHub App: NovAExorpus#59 (`tools/vault-app/setup.sh` + manifest_server.py), and NovAExopia#14, Hyperion-XI#10, CloviX-AEyre#11, AEthX-AEsc#15, NovusAExenti#10 (workflow uses `actions/create-github-app-token@v1` with `vars.VAULT_APP_ID` / `secrets.VAULT_APP_PRIVATE_KEY`, skips with a notice until set). User must run `bash tools/vault-app/setup.sh --drop-pat` in Termux (3 taps: local button, Create GitHub App, Install on NovAExorpus). Key stored in `~/.config/vault-app/` on the phone.

**Why:** user is cost-sensitive and wants no manual token renewal ever.
**How to apply:** the future pointer-index receiver in NovAExorpus should mint a token from the same app to open PRs (GITHUB_TOKEN PRs don't trigger CI).
