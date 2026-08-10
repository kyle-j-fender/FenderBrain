# Open Questions

Gaps the FenderCouncil founding session (2026-08-10) found in the
Second Brain system and didn't resolve — kept here, current, until
they are. Don't let `taxonomy.md` or `triage.md` quietly assume these
are fine; they aren't answered yet.

## No documented access/data-handling review

Nobody has written down who has access to the Second Brain Notion
workspace, what OAuth/API scopes the n8n automation holds against it,
what the Telegram bot's own access model is, or what retention/deletion
policy applies to captured data. This matters because the database
already co-mingles three different sensitivity levels in one place:
Kyle's employer's internal work details (Chick-fil-A, Oracle
Maintenance Management access), his personal financial data (tax
return items, account balances feeding automation), and third parties'
personal data (named individuals' prayer requests). Kyle's move to
capture via Claude Code (`capture.md`, same day) adds a second access
path on top of the original one — a Claude Code session's own Notion
connector access — rather than replacing it as a review target; both
need to be in scope once this review happens.

**Status:** unresolved as of 2026-08-10. Flagged by the council's
Sentinel seat.

## Confidence field is uncalibrated

The `Confidence` score (0–1) has no written definition anywhere: not
what model produces it, what a given number means, what threshold
should trigger a human review, or who's responsible for reviewing
low-confidence items. Real sample data shows scores from 0 to 0.9
across different `Type`s with no visible pattern.

**Status:** unresolved as of 2026-08-10. Flagged by the council's
Realist seat.

## No routing contract with the other five repos

Second Brain already captures items that belong, by tag, to
FenderFinance, youngadults.whc, FenderCareer, and pm_oraclecmms's
worlds — but nothing anywhere defines how (or whether) an item
actually gets handed from Second Brain to those repos' own decision
processes once triaged. `council/domains/second-brain.md`'s automatic
triggers (in FenderCouncil) are a first pass at this, but there's no
mechanism yet beyond "a human notices."

**Status:** unresolved as of 2026-08-10. Flagged by the council's
Advocate seat.

## How to resolve one of these

Update this file in place when Kyle actually does the review or makes
the call — note the resolution and date, don't just delete the
section. If resolving one changes what `council/domains/
second-brain.md` says in FenderCouncil, flag that repo for a matching
update per this repo's own `CLAUDE.md` sync-discipline rule.
