# vault-app

A private GitHub App that replaces the `VAULT_DISPATCH_TOKEN` personal access token.
Workflows mint a fresh 1-hour token from it on every run, so there is nothing to renew.

Who uses it: `notify-vault.yml` in NovAExopia, Hyperion-XI, CloviX-AEyre, AEthX-AEsc and
NovusAExenti (dispatch `base-repo-updated` to this repo). The app also holds
`pull_requests: write`, so the future pointer-index receiver here can open PRs that trigger CI,
which PRs opened with `GITHUB_TOKEN` do not.

## Setup (once, from Termux)

```bash
bash tools/vault-app/setup.sh --drop-pat
```

Three taps in the browser: the button on the local page, **Create GitHub App**, then
**Install** on NovAExorpus. The script stores `VAULT_APP_ID` (variable) and
`VAULT_APP_PRIVATE_KEY` (secret) in all six repos, proves a dispatch works, deletes the old
PAT secret and opens the token page so you can delete the PAT itself. The key is kept in
`~/.config/vault-app/`; re-running reuses the same app.

## Using it in a workflow

```yaml
- uses: actions/create-github-app-token@v1
  id: app
  with:
    app-id: ${{ vars.VAULT_APP_ID }}
    private-key: ${{ secrets.VAULT_APP_PRIVATE_KEY }}
    owner: c10vis-poem
    repositories: NovAExorpus
- run: gh pr create ...
  env:
    GH_TOKEN: ${{ steps.app.outputs.token }}
```

The key itself does not expire. Rotate it only if it leaks: generate a new one on the app's
settings page and run `gh secret set VAULT_APP_PRIVATE_KEY` again per repo.
