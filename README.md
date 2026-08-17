# FenderBrain

Kyle's "second brain" concept — how to think about, triage, and route
what gets captured into the **Second Brain** Notion database — and
FenderCouncil's sixth integrating repo.

## What lives here

This repo holds no code and no build. What it holds:

- `second-brain/taxonomy.md` — what the live Notion database's schema
  actually means: `Type`, `Status`, `Source`, `Tags`, `Confidence`,
  and how they relate to the other five Fender household repos' own
  domains.
- `second-brain/capture.md` — how a Claude Code session should
  actually capture a new item, now that Kyle interfaces with Second
  Brain through Claude Code rather than Telegram/n8n.
- `second-brain/triage.md` — how a captured item should move from
  `Inbox` to `Done`/`Archive`, and what a low or missing `Confidence`
  score should trigger.
- `second-brain/open-questions.md` — the gaps the founding council
  session found and hasn't resolved yet (access review, retention
  policy, Confidence calibration) — kept current, not archived.
- `actions.json` — this repo's near-term action export for the
  cross-repo Chief of Staff routine (built in `FenderOS`). Hand-
  maintained/conversationally populated during a live session, never
  by a standing script against Notion — see `CLAUDE.md`'s Action
  Section.
- `.claude/agents/` — the six FenderCouncil voices (five core voices
  plus `council-triage-lead`), copied verbatim from `FenderCouncil`'s
  `council/agents/`.
- `.claude/skills/council/SKILL.md` — a working copy of the council
  process, scoped to FenderBrain.

## The actual system of record

The **Second Brain** Notion database
(`https://www.notion.so/2ee6736317068086be5be579adcc98d0`) is where
capture actually happens — FenderBrain documents how to use it well;
it doesn't replace the database itself. The capture *path* is
changing: historically a Telegram → n8n → Notion pipeline this repo
never owned, going forward Kyle interfaces with it through Claude Code
directly (`second-brain/capture.md`). This repo still doesn't own or
modify the n8n workflow — retiring it is Kyle's own operational call.

## Why this repo exists this way

An on-demand FenderCouncil session (2026-08-10) decided FenderBrain
should launch documentation-only and claim a Council domain seat
(`council-triage-lead`) immediately, while explicitly deferring any
automation code as a separate future decision — the founding session
weighed a pure documentation repo, an active automation codebase that
would extend or replace the existing n8n pipeline, and this hybrid,
and every voice that touched the automation option rejected it. Full
record: the **Fender Household — Council Decisions** / **Council
Positions** Notion databases (see
`FenderCouncil/council/decision-log-format.md`) hold the session; this
repo is one of its outcomes.

## Council

See `CLAUDE.md`'s "Decision Council" section for when to run one.
`FenderCouncil` is the canonical source for the process, roster, and
this repo's own domain seat (`council/domains/second-brain.md`).
