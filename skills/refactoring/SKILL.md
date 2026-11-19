---
name: refactoring
description: "Entry point to refactor a target (file, folder or class) end to end: diagnoses with the SOLID checks, chooses among the fowler-refactoring, kerievsky-refactoring-to-patterns and gof-design-patterns skills, applies one refactoring at a time with build and tests, and records the source ID. Use only when the user runs /refactoring (Claude Code) or $refactoring (Codex), or asks for this full flow; for one specific refactoring or pattern, use the catalog skill directly."
---

# /refactoring <target> (in Codex, `$refactoring <target>`)

The full refactoring flow. This skill only routes: the content is in the `fowler-refactoring`,
`kerievsky-refactoring-to-patterns` and `gof-design-patterns` skills, and the design criterion is in
the `solid.md` rule. If the request has no target, ask for one.

1. **Diagnose.** Read the target and name the smells and the SOLID principles it violates, with file
   and lines (the checks are in the `solid.md` rule, if installed). If the `refactoring-analyst` (in Codex, `refactoring_analyst`) subagent exists, hand it the target and use the plan it returns.
2. **Pick the source, one per finding:**
   - a simple refactoring removes the smell: `fowler-refactoring` skill;
   - the smell calls for a pattern (conditionals that choose variants, hard-coded notifications,
     scattered object creation): `kerievsky-refactoring-to-patterns` skill, reading the pattern in
     the `gof-design-patterns` skill first, when it is a GoF pattern;
   - there is only a question about a pattern: `gof-design-patterns` skill.
3. **Set up the safety net.** Tests passing before you start. If nothing covers the code, first
   write a test that pins the current behavior.
4. **Apply one refactoring at a time**, following its file's mechanics, with build and tests after
   each step. If the `refactoring-implementer` (in Codex, `refactoring_implementer`) subagent exists, hand it each item.
5. **Record.** One commit per refactoring, with the refactoring ID at
   the end of the description, `[F:<slug>]` or `[K:<slug>]`, plus `[GoF:<pattern>]` and
   `[SOLID:<acronym>]` when they justify the change (the full rule is in `rules/source-ids.md`, if
   installed).
6. **Check the result** with the same SOLID checks (without the rule, check SRP, OCP, LSP, ISP and
   DIP by name) and report what changed, the IDs used and what
   was found but left untouched.

Stop as soon as the smell is gone: going *towards* a pattern is often enough.
