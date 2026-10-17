# Shared brain repo over ngit (git on Nostr)
- Layout: `kb/`, `rules/`, `style/`, `skills/`, `scripts/`, `private/*.age`.
- The repo is public: assume every committed byte is world-readable.
- Sensitive operational data (ledgers, logs, user facts) only as age ciphertext to public recipients; identities never in the repo.
- `.gitignore`: `secrets/`, `*.key`, `.env*`, runtime state.
- Before every commit: gitleaks + custom regex (nsec1, 64-hex near key, bot tokens, NWC, API-key prefixes, JWT-like, AGE-SECRET-KEY). Also scan history. Any hit → abort and report.
- Push with a temporary remote signer (e.g. `nak bunker`) that reads the key from an env var; never `--sec` on the command line, never let the git tool store the key. After the push: stop the signer, shred its log and the cached `credentials.json`, reset it to `{}`.
- Verify with `git ls-remote` on each GRASP server (plain https URL). "incorrect old value" from one server can be harmless if it already shows the new tip.
- Pushing is a public action: owner OK first.
