# BTC/XMR price post
- **Preflight:** if the price script fails with a missing-module error (dependencies wiped after a restore), run `npm ci` once in its workspace and retry. Only report a failure if it still fails.
- Live sources only, short timeouts, fast failover (e.g. CoinGecko → KuCoin; after a 429 go secondary-first for ~30 min).
- One snapshot for both assets. Deterministic sanity gate in code: hard bounds (BTC $10k–$200k, XMR $50–$2k), plausible BTC/XMR ratio, >20% move vs last post needs a second source agreeing within ~3% else abort and tell owner.
- Format: `🟠 BTC: $X  |  🔵 XMR: $Y` + one line, e.g. `Price check — sovereign money, no middlemen.`
- Publish kind 1 + mirror the identical text to the prices topic only. Dedupe within ~10 min. Never invent prices; numbers come literally from the script output.
- Missed hours (outage) are skipped, never backfilled.
