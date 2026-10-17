# Operational lessons

Rules learned the hard way. Each one stands on its own.

- **Scheduled routines can stop when the runtime runs out of usage/credits.** Symptom: every routine fails with a "no usage available" style error. Check usage first, tell the owner, and resume. Do not backfill missed price posts (prices would be stale); skipped harvest runs just run next time.
- **Dependencies can vanish after a machine restore.** A Node script failing with "Cannot find module …" usually means `node_modules` is gone. Run `npm ci` once in that workspace and retry; report a failure only if it still fails.
- **Hosted connector refuses (e.g. GitHub 403 on create/push):** fall back to the CLI that is already signed in as the same account (`gh repo create`, `git push`). Never paste, mint or copy tokens to get around it.
- **Remote signer hygiene:** start the temporary signer (e.g. `nak bunker`) with the key from an environment variable, never as a command-line flag (`--sec …` is visible in the process list and shell history). After the push: stop the signer, shred its log and the git tool's cached credentials file, reset that file to `{}`.
- **GRASP "incorrect old value" on push:** the server may already hold the new tip. Verify with `git ls-remote <plain https GRASP url>` before re-pushing.
- **Verify, don't assume:** every publish/push ends with a read-back from the public side (relay query, `git ls-remote`, CI status).
