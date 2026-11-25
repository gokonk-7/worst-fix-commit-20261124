# Variants tested

The judge compares entries two at a time, weighing first whether the line
is really a commit message about a fix that backfired, then how funny it
is, then how sharply it captures the specific irony of a repair that broke
more than it mended. Every candidate below is one line, at most 100
characters. The obvious families — "broke prod", "DROP TABLE", "fixed the
tests instead of the code", "works on my machine" — were discarded first:
with 461 entries in the field, the first obvious idea is the one hundreds
of other entries already submitted.

## Shortlist

| # | Candidate | Chars | Verdict |
|---|-----------|------:|---------|
| 1 | `fix: the bug is gone — so are the data, the backups, and Dave` | 61 | **KEPT** |
| 2 | `fix: silenced the alarm — the fire is much quieter now` | 54 | Runner-up |
| 3 | `fix: the bug turned out to be load-bearing — removing it took down the feature` | 78 | Runner-up |
| 4 | `fix: prod was slow, so I cached everything — including the bug, forever` | 71 | Cut |
| 5 | `fix: patched the memory leak by moving it into billing — it now charges by the megabyte` | 87 | Cut |
| 6 | `fix: bug is now in prod, cache and backups — it has tenure` | 58 | Cut |
| 7 | `fix: the error is fixed — the fix is now the error` | 50 | Cut |

## Why #1 won

- It is unmistakably a real commit message (`fix: …`) about a fix that
  backfired: the bug is gone, which is what the fix was for — but so is
  everything the fix was supposed to protect.
- The comedy is a rule of three with the third item breaking the pattern:
  data, backups… and Dave. The first two losses are technical; the third
  is a person, which is where the laugh lands.
- The irony is specific, not generic "broke prod": the fix succeeded at
  its stated job (the bug is gone) and the success itself is the disaster.
  The cure deleted more than the disease ever could.

## Why the runners-up lost

- #2 is dry and elegant, but it is a joke about hiding a symptom, and the
  "silenced the warning" family is a crowded one.
- #3 ("load-bearing bug") is the most original concept of the set, but its
  punchline — "took down the feature" — lands flatter than "and Dave".
- #4–#7 are each one clever turn with no second beat: a cached bug, a
  relocated leak, a tenured bug, a fix that became the error. Funny, but
  none of them escalates the way #1 does.
