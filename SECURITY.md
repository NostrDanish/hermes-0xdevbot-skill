# Security Policy

## Reporting a vulnerability

Report vulnerabilities or leaked secrets **via Nostr DM to the maintainer
(0xPrivacy)** — never open a public GitHub issue for secrets or vulnerabilities.

- Include what you found, where (file/commit), and how to reproduce.
- Do not paste any real secret into the report; describe its location instead.
- You will get an acknowledgement as soon as the maintainer reads the DM.

## If a secret is exposed

1. **Rotate the exposed secret immediately** — assume it is compromised the
   moment it lands in a commit, chat or log.
2. Purge it from git history afterwards; rotation comes first, cleanup second.

## CI enforcement

CI (`.github/workflows/ci.yml`) runs gitleaks over the full git history on
every push, so committed keys are caught automatically. Keep it that way:
never commit keys, tokens, ids or private config.
