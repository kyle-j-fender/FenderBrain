# CLAUDE.md — FenderBrain

This repo is documentation only — no build, no app, no generated
output, the same pattern `FenderCouncil` itself uses. It defines
Kyle's "second brain" concept: how to think about, triage, and route
what gets captured into the **Second Brain** Notion database
(`https://www.notion.so/2ee6736317068086be5be579adcc98d0`), which
remains the actual system of record. There's nothing here to run —
capture itself happens through an existing Telegram → n8n → Notion
pipeline this repo does not own or modify.

This scope was set by an on-demand FenderCouncil session on
2026-08-10, logged to the shared **Fender Household — Council
Decisions** / **Council Positions** Notion databases. FenderBrain is
now FenderCouncil's sixth integrating repo: it carries a
`.claude/agents/` copy of all six council voices (the five core voices
plus its own `council-triage-lead` domain seat) and a
`.claude/skills/council/SKILL.md`.

Kyle's stated direction, the same day: he interfaces with Second Brain
through Claude Code going forward, replacing the Telegram bot → n8n
pipeline as the capture path. See `second-brain/capture.md` for
exactly how a Claude Code session should capture an item — this is
conversational tool use in a live session, not the automation-code
option the founding session deferred (see the next section for that
line).

## What this repo is for

One thing right now: write down the second-brain concept honestly —
what the Notion database actually holds, how items should be tagged
and triaged, and which of the household's other five repos a given
captured item actually belongs to — without touching the live capture
pipeline.

## Rules

- **No automation code without a separate council decision.** The
  founding session explicitly deferred any script, pipeline, or
  integration that would read from or write to the Second Brain
  database programmatically. Extending or replacing the n8n workflow
  is its own future decision, not something that grows organically out
  of a documentation change here. This does **not** cover a live
  Claude Code session using Notion's tools turn by turn in a
  human-directed conversation (`second-brain/capture.md`) — that's the
  documented, intended interaction model, not the deferred option. The
  line is unattended writes: a scheduled job, webhook, or standing
  script that writes without a conversation happening right then still
  needs its own council session first.
- **Ground everything in the real Notion schema, not generic
  second-brain/PKM advice.** `second-brain/taxonomy.md` should read
  like it actually knows the `Type`/`Status`/`Tags`/`Confidence`
  fields, not like a generic "how to build a second brain" article. If
  a section could be copy-pasted into any other PKM system unchanged,
  it isn't doing its job — the same standard FenderCouncil holds its
  own domain seats to.
- **This repo doesn't decide anything for the other five repos.** When
  a captured item's tags cross into another domain (Finance, Ministry,
  Career, Work/pm_oraclecmms), FenderBrain's job is to say so and hand
  off — the decision itself belongs to that repo's own rules and
  council seat.
- **Keep `second-brain/open-questions.md` honest and current.** It
  tracks the gaps the founding council session found (no documented
  n8n/Telegram access review, no PII retention policy, an uncalibrated
  `Confidence` field). Update it in place as those get resolved
  instead of letting the taxonomy quietly imply they're fine.
- **Sync discipline.** `.claude/agents/` and
  `.claude/skills/council/SKILL.md` here should track FenderCouncil's
  own `council/agents/` and `council/domains/second-brain.md` — flag
  drift in either direction rather than letting the copies disagree.

## Decision Council

Run an on-demand council session ("run the council," "council this")
for any decision about this repo, any time. Proactively suggest one
(say so plainly, then offer — don't run unasked, don't silently skip
it either) when a decision matches `council/domains/second-brain.md`'s
automatic triggers in FenderCouncil: a change to what the n8n
automation can read/write in Notion, any plan to have FenderBrain
write back into the database programmatically, or a captured item's
tags crossing into another domain's own automatic-trigger territory.
See `.claude/skills/council/SKILL.md` for exactly how to run it —
dispatches `council-steward`, `council-realist`, `council-advocate`,
`council-guardian`, `council-sentinel`, and `council-triage-lead`.

## Common tasks

**Update the taxonomy** — edit `second-brain/taxonomy.md` to match
changes in the real Notion schema (a new `Type` option, a new `Tags`
value, a redefinition of what `Confidence` means). Check whether
`council/domains/second-brain.md` in FenderCouncil needs the same
update.

**Resolve an open question** — when Kyle actually reviews the
n8n/Telegram access model or defines a PII retention policy, update
`second-brain/open-questions.md` in place and note the resolution
date, rather than deleting the entry silently.

**Decide whether FenderBrain should own automation code** — this is
explicitly not a documentation change. Run a council session first;
see this repo's own founding session for the shape that decision
should take.
