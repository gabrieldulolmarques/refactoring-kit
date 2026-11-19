# refactoring-skill

Two refactoring catalogs and a design patterns catalog packaged as [Agent Skills](https://agentskills.io)
for coding agents: Martin Fowler's *Refactoring* (2nd ed., 2018), Joshua Kerievsky's *Refactoring to
Patterns* (2004) and the 23 patterns of Gamma et al.'s *Design Patterns* (GoF, 1995). There are three
skills, one per book, so you can tell which catalog each applied thing came from:
`fowler-refactoring` maps 24 code smells to the 66 refactorings that fix them,
`kerievsky-refactoring-to-patterns` maps 12 code smells to the 27 refactorings to patterns, and
`gof-design-patterns` is the lookup for the 23 patterns, linking each pattern to the refactorings that reach it. A fourth one, `refactoring`, is the entry point: `/refactoring <target>` drives the whole flow and routes to the other three. Every refactoring and pattern file has a C# 9 example.

**Site:** <https://gabrieldulolmarques.github.io/refactoring-skill/> (English and Portuguese).

**Using it?** If these skills help you in a project, a paper or a post, please mention it: link
this repository and credit Gabriel R. Marques ([gabrieldulolmarques](https://github.com/gabrieldulolmarques)
on GitHub). I'd also like to hear how it went, so feel free to open an issue.

## Layout

```
.claude-plugin/plugin.json # makes the package a Claude Code plugin
LICENSE # CC BY 4.0
NOTICE # credit to Fowler, Kerievsky, the GoF authors and Addison-Wesley; what the license covers
CATALOG.md # the spec: 66 + 27 refactorings, 29 smells, 23 patterns, file format, C# level
agents/
├── refactoring-analyst.md # read-only: finds smells and returns a short plan
└── refactoring-implementer.md # applies one refactoring, testing after each step
rules/
├── solid.md # SOLID as a design criterion, with the path to both skills' refactorings
└── source-ids.md # F:, K:, GoF: and SOLID: IDs in commits and plans, to track the source of each change
skills/refactoring/
└── SKILL.md # entry point: /refactoring <target> diagnoses, picks the skill and applies step by step
skills/fowler-refactoring/
├── SKILL.md # flow smell → refactoring → file, index of the 24 smells, tables of the 66
└── references/ # smells.md, discipline.md, a folder per chapter
skills/kerievsky-refactoring-to-patterns/
├── SKILL.md # flow smell → refactoring → file, index of the 12 smells, tables of the 27
└── references/ # smells.md, discipline.md, a folder per chapter
skills/gof-design-patterns/
├── SKILL.md # lookup: the 23 patterns and the refactorings that reach each one
└── references/ # catalog.md, principles.md, a folder per category
```

Only each skill's description stays in the agent's context. The body loads when the skill is
used, and each refactoring's file only when the agent opens it. Kerievsky's refactorings link to
the Fowler refactorings they use as steps, so install the skills side by side.

## Agents

Two subagents that use all three skills:

- `refactoring-analyst` reads the code it is pointed at, names the smells and returns a short
  plan: where, which smell, which refactoring, whether tests cover it, and the risk. It never
  edits.
- `refactoring-implementer` applies one item of that plan (or a named refactoring), following
  the mechanics with a build and a test run after each step.

Review the plan before handing an item to the implementer. The build and test commands come
from the call or from the project's own instructions, not from this package.

## Using it

- **Any Agent Skills client** (Claude Code, Codex, OpenCode): link each folder
  in `skills/` (`refactoring`, `fowler-refactoring`, `kerievsky-refactoring-to-patterns` and `gof-design-patterns`) into the project's skills folder (on Windows, a junction:
  `New-Item -ItemType Junction`).
- **Claude Code plugin**: `claude --plugin-dir <path-to-this-repo>`. The skills and agents are
  then namespaced as `refactoring-kit:<name>`; the entry command is `/refactoring-kit:refactoring`.

- **Rules** (`rules/solid.md` and `rules/source-ids.md`): copy them into the project's rules folder
  (in Claude Code, `.claude/rules/`) or reference them from `AGENTS.md`. Rules are not part of the
  Agent Skills format or of a plugin, so neither route above installs them.

Use one route per project, or Claude Code sees the skills twice.

## License and credit

[CC BY 4.0](LICENSE): free to share and adapt for any purpose, as long as you credit this
package **and** the books it is based on:

> Martin Fowler. *Refactoring: Improving the Design of Existing Code*. 2nd ed. Boston:
> Addison-Wesley (Pearson Education), 2018. ISBN 978-0-13-475759-9.
>
> Joshua Kerievsky. *Refactoring to Patterns*. Boston: Addison-Wesley (Pearson Education),
> 2004. ISBN 978-0-321-21335-8.
>
> Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides. *Design Patterns: Elements of
> Reusable Object-Oriented Software*. Reading: Addison-Wesley, 1995. ISBN 978-0-201-63361-0.

The license covers only this package's own content, not the books (see [NOTICE](NOTICE)).
The motivation and mechanics in the skills are paraphrased, with the chapter cited;
nothing is copied from the books, refactoring.com or industriallogic.com. Refactoring names, former
names and inverses come from the book's section headers, and from the book's web edition for the five web-only
refactorings. The C# examples are original.
