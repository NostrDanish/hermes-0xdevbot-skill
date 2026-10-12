# Cheap yes/no triage (JEV pattern)

Use a small, cheap "judge" model for decisions only (is this light? does it ask
for a secret? is it a jailbreak? is this draft ready?). Never use it to write
answers or fetch numbers. One batched call per message returns probabilities.

- Key from env (`TYPESAFE_API_KEY`); endpoint only the official API host. Beware
  look-alike sites asking you to paste your key.
- Thresholds: `light >= 0.6` and `secret < 0.3` and `override < 0.3` → answer;
  anything else → escalate. Errors/timeouts → escalate.
- Keep a regression file of labelled cases (light, heavy, secret ask, jailbreak,
  look-alike tag) and re-run it after every change; all must pass.
- Typical cost ~$0.00003 and ~0.2 s per call (measured Oct 2026; re-measure).

See `scripts/jev_triage.py` for a minimal client. Adapt the request shape to the
provider's current docs before use.
