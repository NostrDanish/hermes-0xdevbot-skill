# hermes-0xdevbot-skill

A [Hermes Agent](https://hermes-agent.nousresearch.com) skill that teaches a Hermes bot to behave like **0xDevBot**, the 0xPrivacy cypherpunk dev/security/educator bot: voice, Telegram group discipline, secrets rule, owner-OK for public actions, Nostr article + price workflows, cheap-judge triage, ngit brain ops and a self-improvement loop.

## Install
```bash
git clone <this-repo-url> /tmp/hermes-0xdevbot-skill
mkdir -p ~/.hermes/skills/0xprivacy
cp -r /tmp/hermes-0xdevbot-skill/0xprivacy/0xdevbot-persona ~/.hermes/skills/0xprivacy/
```
Or via the Skills Hub from a GitHub URL if your Hermes version supports it. Then restart Hermes (or start a new session) and check it appears in the skill list.

## Configure (locally, never in this repo)
- `TYPESAFE_API_KEY` (optional) for triage; without it, the bot escalates instead of answering.
- Your bot username, owner user id, allowed group id and topic ids in Hermes config/env.

## Layout
```
0xprivacy/0xdevbot-persona/
  SKILL.md
  references/{telegram-rules,jev-triage,article-template,nostr-publishing,price-post,ngit-brain-ops,skill-harvest}.md
  scripts/jev_triage.py
```

## Security
This repo contains no keys, tokens, ids or private config. Keep it that way: run gitleaks before every commit.

License: MIT
