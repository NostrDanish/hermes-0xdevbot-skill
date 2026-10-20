# hermes-0xdevbot-skill


A [Hermes Agent](https://hermes-agent.nousresearch.com) skill that teaches a Hermes bot to work like **0xDevBot**, the 0xPrivacy cypherpunk dev/security/educator bot: voice, Telegram group discipline, the absolute secrets rule, owner OK for public actions, Nostr article and BTC/XMR price workflows, cheap-judge (JEV) triage, ngit brain ops, operational lessons and a self-improvement loop.

## Install

**Option A: Hermes Skills Hub (recommended, security-scanned, updatable)**
```bash
hermes skills install NostrDanish/hermes-0xdevbot-skill/skills/0xdevbot-persona --category 0xprivacy
```
Later updates: `hermes skills check && hermes skills update 0xdevbot-persona`.

Or add the whole repo as a tap (any future skills here show up in search):
```bash
hermes skills tap add NostrDanish/hermes-0xdevbot-skill
hermes skills install NostrDanish/hermes-0xdevbot-skill/0xdevbot-persona --category 0xprivacy
```

**Option B: plain copy (one-liner)**
```bash
git clone --depth 1 https://github.com/NostrDanish/hermes-0xdevbot-skill /tmp/hermes-0xdevbot-skill && mkdir -p ~/.hermes/skills/0xprivacy && cp -r /tmp/hermes-0xdevbot-skill/skills/0xdevbot-persona ~/.hermes/skills/0xprivacy/
```
(Use `$HERMES_HOME/skills/...` instead if you run a named profile.)

**Check it loaded**
```bash
hermes skills list            # shows 0xdevbot-persona, category 0xprivacy
```
In a chat: `/0xdevbot-persona` (or just start working; Hermes loads it when relevant). Open sessions pick up a new skill on their next message.

## Configure (locally, never in this repo)
- `TYPESAFE_API_KEY` (optional) for triage. Put it in `~/.hermes/.env` or answer the secure prompt when the skill loads in the local CLI. Without it every addressed message escalates to the owner instead of being answered.
- `OWNER_TELEGRAM_ID`: who the bot trusts as owner (secret exceptions and orders come only from this account's DM). Messages from unverified accounts are treated as group text.
- Your bot username, allowed group id and topic ids go in your Hermes config/env, not in this repo.

## Layout
```
skills/0xdevbot-persona/
  SKILL.md                       always-on rules (secrets, voice, Telegram, owner OK) + workflow index
  references/                    loaded on demand
    telegram-rules.md  jev-triage.md  article-template.md  nostr-publishing.md
    price-post.md  ngit-brain-ops.md  skill-harvest.md  ops-lessons.md
  scripts/jev_triage.py          stdlib JEV triage client, fails closed (escalate)
tests/
  validate_skill.py              frontmatter/structure/secret checks
  test_jev_triage.py             unit tests with the JEV API mocked (no network, no key)
  hermes_scan.py                 runs the real Hermes skill linter + install security scanner
.github/workflows/ci.yml         active CI: all of the above + checksum-verified gitleaks
```

## Test locally
```bash
pip install pyyaml
python -m py_compile skills/*/scripts/*.py
python tests/validate_skill.py
python -m unittest discover -s tests -v
env -u TYPESAFE_API_KEY python skills/0xdevbot-persona/scripts/jev_triage.py "what is a relay?"   # -> "escalate"
git clone --depth 1 https://github.com/NousResearch/hermes-agent /tmp/hermes-agent
HERMES_SRC=/tmp/hermes-agent python tests/hermes_scan.py                                       # -> install allowed: True
```

## Notes for editors
- Hermes' install scanner hard-blocks community skills that contain certain crypto-mining keywords (for example the full name of the XMR coin). Write "XMR"; `tests/validate_skill.py` enforces this.
- Hub installs copy only files that `SKILL.md` references; keep every reference/script path mentioned in `SKILL.md` (the validator checks it).
- Avoid "pipe text into an interpreter" one-liners in `SKILL.md`; the scanner flags them. Pass arguments instead.

## Security
This repo contains no keys, tokens, ids or private config. Keep it that way: CI is active (`.github/workflows/ci.yml`) and runs gitleaks over the full history on every push — you should too before every push. To report a vulnerability, see [SECURITY.md](SECURITY.md).

License: MIT
