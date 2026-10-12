# Nostr publishing workflow
1. Draft (research-to-draft): collect sources, test hands-on, fill the template.
2. Pre-publish check (code): regex block for secrets (nsec1, 64-hex near key/secret, bot tokens, NWC, API-key prefixes, age identities); warn on internal paths/ids; check template sections. Optional judge score 0–3 (advisory only).
3. Send the draft + check result to the owner. **Wait for explicit OK.**
4. Check your ledger for a duplicate `d` tag; abort if present.
5. Sign kind 30023 with the key from env (never print it); publish to a few public relays.
6. Verify the event on at least one relay; build ONE canonical share link (njump + naddr with a single relay hint) and reuse it everywhere.
7. Mirror title + summary + link to the news topic; record ids in the ledger.
