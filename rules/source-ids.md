# Source IDs

How to identify which catalog each applied refactoring, pattern or principle came from, so the use
of each source can be tracked and measured later. It applies to plans, commit messages and agent
reports.

| ID | Source | Example |
|---|---|---|
| `F:<slug>` | refactoring from the `fowler-refactoring` skill | `[F:extract-function]` |
| `K:<slug>` | refactoring from the `kerievsky-refactoring-to-patterns` skill | `[K:replace-conditional-logic-with-strategy]` |
| `GoF:<pattern>` | pattern from the `gof-design-patterns` skill (Gamma et al., 1995) | `[GoF:strategy]` |
| `SOLID:<acronym>` | principle from the `solid.md` rule | `[SOLID:OCP]` |

The slug is the reference file's name without `.md`; the GoF pattern is lowercase and hyphenated
(`abstract-factory`).

## Rules

- In a commit, the ID goes at the end of the description, in square brackets, on the same line;
  several IDs are separated by a space. The brackets do not count as description, so `SOLID:OCP` can
  be uppercase:
  `♻️ refactor(units): replace equipment switch with strategy [SOLID:OCP] [F:replace-conditional-with-polymorphism]`
- One commit per refactoring, so each commit has a single `F:` or `K:` ID. `SOLID:` and `GoF:` come
  along when they justify the change.
- A commit that applies nothing from the catalogs (docs, configuration) carries no ID.
- In plans and agent reports, the refactoring column carries the same ID.
- To count the use of a source: `git log --grep "\[F:"` (or `\[K:`, `\[GoF:`, `\[SOLID:`).
