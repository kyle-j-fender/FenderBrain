# Second Brain Taxonomy

What the live **Second Brain** Notion database's schema actually
means, as of the FenderCouncil founding session (2026-08-10). This is
the real schema, not aspirational — update this file the moment the
database's schema changes; a stale taxonomy doc is worse than none.

## Type

One of `Sermon`, `Document`, `Financial`, `Prayer`, `Business Idea`,
`Task`, `Note`. This is the first, coarsest routing signal — before
`Tags` — and generally maps to which household repo eventually cares:

| Type | Usually belongs to |
|---|---|
| `Financial` | FenderFinance |
| `Prayer`, `Sermon` | youngadults.whc (ministry) |
| `Business Idea` | no current repo owner — stays in Second Brain |
| `Task`, `Note`, `Document` | depends on `Tags` — see below |

## Status

`Inbox` → `In progress` → `Done` / `Archive`. Everything lands in
`Inbox` first. `Done` and `Archive` are both terminal but distinct:
`Done` means the item was acted on, `Archive` means it was decided not
to act on it. Neither should be treated as "safe to ignore" without
that distinction — a `Business Idea` archived without a reason and a
`Business Idea` done are very different signals if this database ever
gets mined for patterns later.

## Source

`Manual`, `Email`, `Voice`, `Telegram`, `Claude Code`. Historical
capture (through 2026-08-10) is almost entirely `Telegram`, via an n8n
automation this repo does not own or modify. `Claude Code` was added
to the schema the same day, per Kyle's stated direction to interface
with Second Brain through Claude Code going forward instead of
Telegram/n8n — see `capture.md` for how a session should actually
write one of these.

## Tags

A 26-option multi-select. Two families, not formally distinguished in
the schema but distinguished here because they do different jobs:

**Life-domain tags** (map to a household repo's world): `Spiritual`,
`Prayer`, `Intercession`, `Thanksgiving`, `Finance`, `Health`,
`Personal`, `Family`, `Ministry`, `Business`, `Work`, `Idea`, and the
employer-specific `Chick-fil-A` (Kyle's current role — the same kind of
Oracle Maintenance Management work `pm_oraclecmms` documents).

**Meta/workflow tags** (about the item itself, not its domain):
`Improvement`, `Process`, `AI`, `Automation`, `Answered`, `Urgent`,
`Someday`, `Soon`, `Now`, `Planning`, `Decision`, `Reference`,
`Follow-Up`, `Action Required`.

A captured item's real domain is its life-domain tags, not its `Type`
alone — a `Task` tagged `Chick-fil-A` and a `Task` tagged `Personal`
are different repos' business even though they share a `Type`.

## Confidence

A 0–1 number, shown as a ring, set by whatever AI classification the
n8n pipeline runs. **As of 2026-08-10 this field is uncalibrated and
undocumented** — real sample data shows scores from 0 to 0.9 with no
written definition of what a given score means, what threshold should
trigger a human review, or who's supposed to do that review. Treat any
decision that leans on a specific `Confidence` value as resting on an
unverified number until that changes — see `open-questions.md`.

## DFR Link

A relation to a separate **Daily Finance Report** data source, which
itself relates back to Second Brain rows and to a `Report` data
source. This confirms downstream automation already exists beyond raw
capture — treat any change to a `Financial`-typed item as potentially
touching that downstream report, not just the row itself.

## Work items: Second Brain vs. the Work Tasks Tracker vs. pm_oraclecmms

As of an audit on 2026-08-10, three separate places can describe the
same piece of Kyle's Chick-fil-A work, and they are **not** meant to
duplicate each other. Each has one job:

| System | Job |
|---|---|
| `pm_oraclecmms` | System of record for formal Oracle CMMS Epic/User Story work — durable, versioned, documented (`registry/story-index.md`). |
| Notion **Work Tasks Tracker** (`https://www.notion.so/32e67363170680439bb6ee7adc203b74`) | System of record for day-to-day/team-visible work that doesn't rise to a formal Story — decks, QBRs, training, items tied to a 1:1. |
| **Second Brain** (`Type: Task`, tagged `Work`/`Chick-fil-A`) | Capture and triage only. Not a third system of record. |

A `Task` row here should exist for one of two reasons: (1) it's brand
new and hasn't been triaged into either of the other two systems yet
(`Status: Inbox`), or (2) it's a catch-up/cross-reference row flagged
`Follow-Up` because it's already tracked elsewhere and needs a status
check (see the 2026-08-10 audit rows). Once a `Follow-Up` row is
confirmed against its real owner (a Tasks Tracker item or a
pm_oraclecmms story), move it to `Done` here rather than letting it sit
open as a permanent duplicate — the Tasks Tracker or the story keeps
tracking the actual work, not this row.

Do not assume a title match is a confirmed link. The 2026-08-10 audit
found "Work on first iteration for asset routes" in the Tasks Tracker
almost certainly overlaps `RXT-001`/`RXT-002` in pm_oraclecmms but
could not confirm which — treat that kind of match as a prompt to ask
Kyle, not as settled fact.
