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
