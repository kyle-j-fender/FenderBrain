# Triage

How an item should move once it lands in `Inbox`, using the signals
the Notion schema already gives you — without writing any code against
the database (see `CLAUDE.md`'s rule against automation code without a
separate council decision).

## The default path

`Inbox` → someone (Kyle, or a Claude Code session working from this
repo) looks at the item → either moves it to `In progress` (it's real
and being worked), `Done` (it was resolved outside the item itself —
e.g. a `Task` that got handled directly), or `Archive` (decided not to
act on it, but keeping the record).

## When to slow down

- **`Confidence` is low or 0.** Per `taxonomy.md`, this field isn't
  calibrated yet — treat a low score as "the system isn't sure," not
  as "the system is confidently telling you this is unimportant."
  Read `Raw Command` and `Content` yourself before triaging on the
  strength of `Type`/`Tags` alone.
- **The life-domain tags cross into another repo's world.** A
  `Financial`-tagged item nearing a real dollar decision belongs to
  FenderFinance's own rules and `council-cfo` seat, not FenderBrain's.
  A `Ministry`/`Prayer`-tagged item that turns into something needing
  Pastor Tessa's sign-off belongs to youngadults.whc. FenderBrain's
  `council-triage-lead` seat exists to notice this crossing and say so
  — not to make that call itself.
- **It's tagged `Action Required` or `Urgent` and also `Now`.** These
  are the meta-tags the pipeline already uses for genuinely
  time-sensitive items — don't let them sit in `Inbox`.

## What triage is not

Not a reason to write automation. If a pattern repeats often enough
that it's tempting to script it, that's a signal for a future council
session on the automation-code option the founding session deferred —
not a reason to quietly start scripting inside this documentation-only
repo.
