# BTC/XMR price post
- Live sources only, short timeouts, fast failover (e.g. CoinGecko → KuCoin; after a 429 go secondary-first for ~30 min).
- Deterministic sanity gate in code: hard bounds, plausible BTC/XMR ratio, >20% move vs last post needs a second source agreeing within ~3% else abort and tell owner.
- Format: `🟠 BTC: $X  |  🔵 XMR: $Y` + one line, e.g. `Price check — sovereign money, no middlemen.`
- Publish kind 1 + mirror the identical text to the prices topic only. Dedupe within ~10 min. Never invent prices.
