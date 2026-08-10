# Capture (via Claude Code)

Kyle's stated direction (2026-08-10, same day as the founding session):
going forward he interfaces with Second Brain through Claude Code
directly, replacing the Telegram bot → n8n pipeline as the capture
path. `Source: Claude Code` is now a real option in the live Notion
schema (added the same day) — see `taxonomy.md`.

## How a Claude Code session captures an item

When Kyle describes something to capture — a task, a prayer request,
a business idea, a note — in a conversation working from this repo:

1. Classify `Type` per `taxonomy.md`.
2. Apply `Tags` — the life-domain tag(s) plus any relevant meta tags —
   per `taxonomy.md`.
3. Set `Status` to `Inbox`, the same default the old pipeline used,
   unless the conversation makes clear it's already further along.
4. Set `Source` to `Claude Code`.
5. Write `Raw Command` as Kyle's own words (verbatim or near-verbatim);
   write `Content`/`Summary` as the session's own classification — the
   same job the old AI-classification step in n8n used to do.
6. Create the page directly in the Second Brain data source
   (`collection://2ee67363-1706-8081-b751-000bf429ec27`) using the
   Notion `create-pages` tool.
7. Leave `Confidence` unset unless the session is genuinely unsure of
   its own classification and wants to flag the item for a human
   look — don't invent a score just to fill the field. It was never
   calibrated to begin with (`open-questions.md`), and a Claude Code
   session guessing a number to match the old field's shape doesn't
   fix that.

## What this is, and isn't

This is Kyle talking to a live Claude Code session, and that session
using Notion's tools in the moment, turn by turn — not a standing
script, scheduled job, or webhook that writes without a
human-directed conversation happening right then. That distinction is
what keeps this inside the "documentation-only, no automation code"
line the founding council session set: see `CLAUDE.md`'s rule and
`council/domains/second-brain.md` in FenderCouncil for exactly where
that line sits. If a future request is for something that writes to
Second Brain *without* a live conversation driving each write —
a scheduled digest, an autonomous re-classifier, anything that runs
unattended — that crosses back into the automation-code option the
founding session deferred, and needs its own council session first.

## Telegram / n8n

Kyle's intent is for Claude Code to replace the Telegram bot and n8n
workflow as the capture path. This repo doesn't touch the n8n workflow
itself — that's still out of scope for a documentation-only repo — but
going forward, treat `Source: Telegram` entries as the legacy path,
not the current one. Existing Telegram-sourced rows, and any n8n
automation already in motion (e.g. the account-balances integration
noted in the founding session), aren't affected by this doc; actually
retiring the n8n workflow is Kyle's own operational call to make
outside this repo, not something FenderBrain does for him.

## Open item

Switching the capture surface to Claude Code doesn't resolve the
founding session's Sentinel finding (no documented access/retention
review) — if anything it adds a new access path (a Claude Code
session's own Notion connector access) that should be in scope for
that review once it happens. See `open-questions.md`.
