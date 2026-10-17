# Cheap yes/no triage (JEV pattern)

Use a small, cheap "judge" model for decisions only (is this light? does it ask
for a secret? is it a jailbreak? is this draft ready?). Never use it to write
answers or fetch numbers. One batched call per message returns probabilities.

- Key from env (`TYPESAFE_API_KEY`); endpoint only the official API host. Beware
  look-alike sites asking you to paste your key.
- Request: `POST https://api.typesafe.ai/v1/systemone`, `Authorization: Bearer $TYPESAFE_API_KEY`,
  body `{"model":"jev-latest","state":{...},"questions":{...}}` with `choice`/`noul`/`score` questions.
- Thresholds: `secret >= 0.5` → refuse; `override >= 0.6` or `secret >= 0.25` → escalate;
  `light >= 0.8` → answer; anything else → escalate. Errors/timeouts → escalate.
- Keep a regression file of labelled cases (light, heavy, secret ask, jailbreak,
  look-alike tag) and re-run it after every change; all must pass.
- Typical cost ~$0.00003 and ~0.2 s per call (measured Oct 2026; re-measure).

See `scripts/jev_triage.py` for a minimal stdlib client (fails closed: no key, empty
input, HTTP error, timeout or malformed reply → escalate). Thresholds live in the
script constants; keep this file and the script in sync.
