---
name: council
description: Run an LLM Council decision session for FenderBrain — dispatches the five core voices plus council-triage-lead in parallel to argue out a decision before it's made. Use for any FenderBrain decision, on demand ("run the council," "council this") or when it crosses one of the automatic triggers below.
---

# Council (FenderBrain)

This is FenderBrain's working copy of the Fender household's shared
LLM Council process. `FenderCouncil` is the canonical source — if this
file and `FenderCouncil/council/process.md` /
`council/domains/second-brain.md` ever disagree, treat FenderCouncil
as correct and flag this file as stale.

## When to run

- **On-demand, any time:** "run the council," "get a council opinion,"
  "council this."
- **Automatically, proactively suggested** (say so plainly, then offer
  — don't run unasked, don't silently skip it either) when a decision
  matches any of `council/domains/second-brain.md`'s triggers in
  FenderCouncil:
  - A change to what the n8n automation is allowed to read or write in
    the Notion workspace.
  - Any plan to have FenderBrain, or any other tool, write back into
    the Second Brain database programmatically rather than just read
    from it — this is the automation-code line the founding council
    session (2026-08-10) deliberately deferred.
  - A captured item's `Tags` crossing into another domain's own
    automatic-trigger territory (Finance, Ministry, Career, Work).

## How to run it

1. **Frame** the decision: one sentence, the real options (not a false
   binary), reversibility, and decision authority (Kyle alone, for
   anything scoped to this repo's own capture/triage concept — see
   `CLAUDE.md`). Do the framing gut-check yourself first (first
   principles / outsider view) — see `FenderCouncil/council/
   process.md`'s "Framing gut-check."
2. **Round 1 — independent positions.** Dispatch six parallel `Agent`
   tool calls, in the foreground (step 3 needs every result), one
   message, `subagent_type` values `council-steward`,
   `council-realist`, `council-advocate`, `council-guardian`,
   `council-sentinel`, `council-triage-lead`. Give each only the
   frame. Record each voice's recommendation, confidence, and
   evidence verbatim.
3. **Round 2 — cross-examination.** Dispatch the same six again, one
   message, this time with the frame plus every round-1 position.
   Each returns its single sharpest objection to the position it
   disagrees with most, or "pass."
4. **Synthesis.** You are the chair, not a seventh voice — weigh the
   positions against the decision's reversibility and who actually
   holds authority to decide, and give a recommendation, a confidence
   level, and what would change it.
5. **Present.** Four parts, always in this order: the frame restated
   plainly, round 1 as individual turns (voice, question, confidence,
   evidence), round 2 as `Voice → Voice` objections including passes,
   the chair's synthesis set visually apart from the voice turns.
   Build it from `FenderCouncil/council/presentation-template.html`
   where the environment can render a styled artifact; otherwise the
   same four-part structure in plain markdown.
6. **Log it** to Notion — there is no per-repo log file. One page in
   **Fender Household — Council Decisions** (`Repo` = `FenderBrain`),
   plus one row per voice dispatched in **Council Positions**, related
   back to that page. See `FenderCouncil/council/
   decision-log-format.md` for the exact schema and field mapping.

## Calibrating effort to stakes

For something small — a low-stakes on-demand call — it's fine to skip
the `Agent` dispatch and reason through all six voices directly in the
current conversation instead, per `FenderCouncil/council/process.md`'s
"Calibrating effort to stakes." Still all six voices, still logged —
just without spinning up separate agents for something that doesn't
need that level of independence.
