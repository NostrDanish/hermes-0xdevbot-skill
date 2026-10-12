# Shared brain repo over ngit (git on Nostr)
- Layout: `kb/`, `rules/`, `style/`, `skills/`, `scripts/`, `private/*.age`.
- Sensitive operational data (ledgers, logs, user facts) only as age ciphertext to public recipients; identities never in the repo.
- `.gitignore`: `secrets/`, `*.key`, `.env*`, runtime state.
- Before every commit: gitleaks + custom regex (nsec1, 64-hex near key, bot tokens, NWC, API-key prefixes, JWT-like, AGE-SECRET-KEY). Also scan history. Any hit → abort.
- Push with a temporary remote signer (e.g. `nak bunker`) reading the key from env; never let the git tool store the key; kill the signer and shred its log after. Verify with `git ls-remote` on each GRASP server.
- Pushing is a public action: owner OK first.
