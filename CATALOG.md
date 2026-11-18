# Catalog spec

The spec the skill was written from and is checked against: one skill,
`refactoring`, with one reference file per refactoring, the smells and the discipline,
and the file format. Sections 1–4 cover Fowler's catalog; section 5 covers Kerievsky's
refactorings to patterns, added in 0.4.0; section 6 the GoF patterns and section 7 the C# level of
every example (0.5.0).

Sources: Fowler, *Refactoring*, 2nd ed. (2018), chapters 2–4 and 6–12, and the online catalog
([refactoring.com/catalog](https://refactoring.com/catalog/), checked on 2026-10-31), which
lists **66 refactorings**: the **61 from the book** plus **5 that only exist in the web
edition** (marked "(web)" after the name).

**How sources are cited:** by chapter, section and entry name, never by page. The page changes
with the edition and format (print, PDF, O'Reilly, EPUB); the chapter and the name do not. The
same pattern holds for all three sources: `Fowler (2018), ch. 6`, `Kerievsky (2004), ch. 7`,
`Gamma et al. (1995), §1.6` or `ch. 5`, always with the name of the refactoring or pattern.

The skill is generic: it teaches the refactorings, not any project's process. The examples
are plain C# 9 with current, neutral themes (section 7), and nothing refers
to a specific project, framework, engine or team workflow.

---

## 1. The skill

One skill, `refactoring`. Only its `description` stays in the agent's context; the
`SKILL.md` body loads when the skill is used, and each reference file only when the agent
opens it. The agent starts from a problem (a smell), not from a refactoring's name, so one
entry point that routes smell → refactoring → file works better than 66 competing
descriptions.

| File | Source | Content |
|---|---|---|
| `SKILL.md` | this spec | the flow smell → refactoring → file, a smell quick index and a table of the 66 refactorings (name, when, file), grouped by chapter (section 4.1) |
| `references/fowler/smells.md` | ch. 3 | the 24 smells, symptoms and suggested refactorings (section 3) |
| `references/fowler/discipline.md` | ch. 2 and 4 | tests first, small steps, commit after each green refactoring |
| `references/fowler/<chapter>/<slug>.md` (66 files) | ch. 6–12, or the web edition for the web-only ones | one refactoring each: when to use, mechanics, C# example, verification (section 4.2) |
| `references/kerievsky/<chapter>/<slug>.md` (27 files) | Kerievsky ch. 6–11 | one refactoring to a pattern each, same format plus pattern and direction (section 5) |
| `references/kerievsky/smells.md` | Kerievsky ch. 4 | the 12 smells and the refactorings to patterns they point to (section 5.2) |
| `references/kerievsky/discipline.md` | Kerievsky ch. 1-3 | when a pattern pays off, composite and test-driven refactorings, to/towards/away, design debt |
| `references/gof/catalog.md` | GoF ch. 1, 3-5 | the 23 intents, purpose and scope, causes of redesign, what each pattern lets vary, comparisons (section 6) |
| `references/gof/principles.md` | GoF ch. 1 and 6 | design principles, how to select and use a pattern (section 6) |
| `references/gof/<category>/<slug>.md` (23 files) | GoF ch. 3-5 | one pattern each: intent, when it pays off, participants, C# example, variations, risks (section 6) |

The slug is the refactoring's name in kebab-case. Example: Extract Function →
`references/fowler/first-set/extract-function.md`. The files are grouped by book (`fowler/`, `kerievsky/`) and then in one folder per chapter. Fowler's:
`first-set` (ch. 6), `encapsulation` (7), `moving-features` (8), `organizing-data` (9),
`conditional-logic` (10), `refactoring-apis` (11) and `inheritance` (12); a web-only refactoring goes
in the chapter section 2 lists it under. The refactoring.com page uses the name in camelCase
instead: `https://refactoring.com/catalog/extractFunction.html`.

```
skills/
└── refactoring/
    ├── SKILL.md
    └── references/
        ├── fowler/
        │   ├── smells.md
        │   ├── discipline.md
        │   ├── first-set/
        │   │   ├── extract-function.md
        │   │   └── ...
        │   └── ... # 7 chapter folders, 66 files
        ├── kerievsky/
        │   ├── smells.md
        │   ├── discipline.md
        │   ├── creation/
        │   └── ... # 6 chapter folders, 27 files
        └── gof/
            ├── catalog.md
            ├── principles.md
            ├── creational/
            └── ... # 3 category folders, 23 files
```

---

## 2. The 66 refactorings

Checked against the book on 2026-10-31, mechanically from the PDF's text: each of the 61 book
refactorings is in the chapter shown, the **Formerly / aka** and
**Inverse** columns are the book's own section header (`formerly:`, `aka:`, `subsumes:`,
`inverse of:`), and all 575 "Name (page)" cross-references in ch. 3–12 point to the right
refactoring. For the 5 web-only refactorings, names, aliases and mechanics come from the book's web edition (checked on 2026-11-11).

**C# note** is what the reference file must add because the book's examples are JavaScript:
only generic C# points. Where it says "—", the file has no C# notes section.

### Chapter 6: A First Set of Refactorings

| # | Refactoring | Formerly / aka | Inverse | C# note |
|---|---|---|---|---|
| 1 | Extract Function | formerly Extract Method | Inline Function | in C#, local functions are an option for helpers used in one place |
| 2 | Inline Function | formerly Inline Method | Extract Function | do not inline a `virtual`/`override` method or an interface implementation without checking the other implementations |
| 3 | Extract Variable | formerly Introduce Explaining Variable | Inline Variable | — |
| 4 | Inline Variable | formerly Inline Temp | Extract Variable | — |
| 5 | Change Function Declaration | aka Rename Function, Change Signature; formerly Rename Method, Add Parameter, Remove Parameter | — | the compiler finds direct callers, not reflection, string-based lookups or serialized names; on a public API, keep the old signature as an `[Obsolete]` forwarder during migration |
| 6 | Encapsulate Variable | formerly Encapsulate Field, Self-Encapsulate Field | — | public field → private field + property; a static field → static property |
| 7 | Rename Variable | — | — | — |
| 8 | Introduce Parameter Object | — | — | a class, `record` or `record struct` |
| 9 | Combine Functions into Class | — | — | — |
| 10 | Combine Functions into Transform | — | — | idiomatic in JavaScript; in C# it is usually a function that returns a new enriched `record` (`with` expressions), or it becomes Combine Functions into Class |
| 11 | Split Phase | — | — | the intermediate data structure is usually a `record` |

### Chapter 7: Encapsulation

| # | Refactoring | Formerly / aka | Inverse | C# note |
|---|---|---|---|---|
| 12 | Encapsulate Record | formerly Replace Record with Data Class | — | dictionary, tuple, anonymous or `dynamic` data → a class or `record` with properties |
| 13 | Encapsulate Collection | — | — | expose `IReadOnlyList<T>` / `IReadOnlyCollection<T>`, with `Add`/`Remove` methods; a read-only interface does not stop a caller from casting back, so return a copy where that matters |
| 14 | Replace Primitive with Object | formerly Replace Data Value with Object, Replace Type Code with Class | — | meaningful `string`/`int` → own type (`record`, `readonly record struct`) or `enum` |
| 15 | Replace Temp with Query | — | — | a read-only property or a method; keep expensive queries as methods |
| 16 | Extract Class | — | Inline Class | — |
| 17 | Inline Class | — | Extract Class | — |
| 18 | Hide Delegate | — | Remove Middle Man | — |
| 19 | Remove Middle Man | — | Hide Delegate | — |
| 20 | Substitute Algorithm | — | — | — |

### Chapter 8: Moving Features

| # | Refactoring | Formerly / aka | Inverse | C# note |
|---|---|---|---|---|
| 21 | Move Function | formerly Move Method | — | the target may be another class, a static class, or an extension method |
| 22 | Move Field | — | — | a field that is persisted or serialized keeps its stored name only if the mapping is updated too |
| 23 | Move Statements into Function | — | Move Statements to Callers | — |
| 24 | Move Statements to Callers | — | Move Statements into Function | — |
| 25 | Replace Inline Code with Function Call | — | — | — |
| 26 | Slide Statements | formerly Consolidate Duplicate Conditional Fragments | — | — |
| 27 | Split Loop | — | — | — |
| 28 | Replace Loop with Pipeline | — | — | LINQ; mind deferred execution (enumerate once) and allocation on hot paths |
| 29 | Remove Dead Code | — | — | code with no static callers may still be reached by reflection, dependency injection or serialization |

### Chapter 9: Organizing Data

| # | Refactoring | Formerly / aka | Inverse | C# note |
|---|---|---|---|---|
| 30 | Split Variable | formerly Remove Assignments to Parameters, Split Temp | — | no immutable locals (`const` only fits compile-time constants), so keep each new variable assigned once; renaming a parameter breaks callers that use named arguments |
| 31 | Rename Field | — | — | a serialized or persisted field keeps its wire name only with a mapping attribute (e.g. `[JsonPropertyName("oldName")]`) or a migration |
| 32 | Replace Derived Variable with Query | — | — | a computed read-only property |
| 33 | Change Reference to Value | — | Change Value to Reference | `record`, `readonly record struct` or an immutable class with value equality (`Equals`/`GetHashCode`) |
| 34 | Change Value to Reference | — | Change Reference to Value | a repository or registry that hands out the shared instance |
| 35 | Replace Magic Literal (web) | Replace Magic Number with Symbolic Constant | — | `const` for compile-time values, `static readonly` for the rest |

### Chapter 10: Simplifying Conditional Logic

| # | Refactoring | Formerly / aka | Inverse | C# note |
|---|---|---|---|---|
| 36 | Decompose Conditional | — | — | — |
| 37 | Consolidate Conditional Expression | — | — | — |
| 38 | Replace Nested Conditional with Guard Clauses | — | — | — |
| 39 | Replace Conditional with Polymorphism | — | — | a `switch` on a type code → `abstract`/`virtual` members or an interface |
| 40 | Introduce Special Case | formerly Introduce Null Object | — | with nullable reference types enabled, the special case removes `?`/null checks at the call sites |
| 41 | Introduce Assertion | — | — | `Debug.Assert` (removed from Release builds) |
| 42 | Replace Control Flag with Break (web) | Remove Control Flag | — | — |

### Chapter 11: Refactoring APIs

| # | Refactoring | Formerly / aka | Inverse | C# note |
|---|---|---|---|---|
| 43 | Separate Query from Modifier | — | — | — |
| 44 | Parameterize Function | formerly Parameterize Method | — | — |
| 45 | Remove Flag Argument | formerly Replace Parameter with Explicit Methods | — | — |
| 46 | Preserve Whole Object | — | — | — |
| 47 | Replace Parameter with Query | formerly Replace Parameter with Method | Replace Query with Parameter | — |
| 48 | Replace Query with Parameter | — | Replace Parameter with Query | useful to remove a dependency on a static or singleton and make the code testable |
| 49 | Remove Setting Method | — | — | `{ get; }` or `{ get; init; }` |
| 50 | Replace Constructor with Factory Function | formerly Replace Constructor with Factory Method | — | a static factory method; make the constructor `private` or `protected` |
| 51 | Replace Function with Command | formerly Replace Method with Method Object | Replace Command with Function | — |
| 52 | Replace Command with Function | — | Replace Function with Command | — |
| 53 | Return Modified Value (web) | — | — | — |
| 54 | Replace Error Code with Exception (web) | — | — | do not use exceptions for expected control flow |
| 55 | Replace Exception with Precheck (web) | Replace Exception with Test | — | the `TryParse`/`TryGetValue` pattern |

### Chapter 12: Dealing with Inheritance

| # | Refactoring | Formerly / aka | Inverse | C# note |
|---|---|---|---|---|
| 56 | Pull Up Method | — | Push Down Method | — |
| 57 | Pull Up Field | — | Push Down Field | — |
| 58 | Pull Up Constructor Body | — | — | `: base(...)` constructor chaining |
| 59 | Push Down Method | — | Pull Up Method | — |
| 60 | Push Down Field | — | Pull Up Field | — |
| 61 | Replace Type Code with Subclasses | subsumes Replace Type Code with State/Strategy, Extract Subclass | Remove Subclass | — |
| 62 | Remove Subclass | formerly Replace Subclass with Fields | Replace Type Code with Subclasses | — |
| 63 | Extract Superclass | — | — | an `abstract` base class, or an interface if only the signatures are shared |
| 64 | Collapse Hierarchy | — | — | — |
| 65 | Replace Subclass with Delegate | — | — | — |
| 66 | Replace Superclass with Delegate | formerly Replace Inheritance with Delegation | — | — |

---

## 3. `references/fowler/smells.md`: the 24 smells and where they lead

Summary of ch. 3: the index the agent checks before picking a refactoring. Each refactoring
named here is the file `references/fowler/<chapter>/<slug>.md`.

| Smell | Suggested refactorings |
|---|---|
| Mysterious Name | Change Function Declaration, Rename Variable, Rename Field |
| Duplicated Code | Extract Function, Slide Statements, Pull Up Method |
| Long Function | Extract Function, Replace Temp with Query, Introduce Parameter Object, Preserve Whole Object, Replace Function with Command, Decompose Conditional, Replace Conditional with Polymorphism, Split Loop |
| Long Parameter List | Replace Parameter with Query, Preserve Whole Object, Introduce Parameter Object, Remove Flag Argument, Combine Functions into Class |
| Global Data | Encapsulate Variable |
| Mutable Data | Encapsulate Variable, Split Variable, Slide Statements, Extract Function, Separate Query from Modifier, Remove Setting Method, Replace Derived Variable with Query, Combine Functions into Class, Combine Functions into Transform, Change Reference to Value |
| Divergent Change | Split Phase, Move Function, Extract Function, Extract Class |
| Shotgun Surgery | Move Function, Move Field, Combine Functions into Class, Combine Functions into Transform, Split Phase, Inline Function, Inline Class |
| Feature Envy | Move Function, Extract Function |
| Data Clumps | Extract Class, Introduce Parameter Object, Preserve Whole Object |
| Primitive Obsession | Replace Primitive with Object, Replace Type Code with Subclasses, Replace Conditional with Polymorphism, Extract Class, Introduce Parameter Object |
| Repeated Switches | Replace Conditional with Polymorphism |
| Loops | Replace Loop with Pipeline |
| Lazy Element | Inline Function, Inline Class, Collapse Hierarchy |
| Speculative Generality | Collapse Hierarchy, Inline Function, Inline Class, Change Function Declaration, Remove Dead Code |
| Temporary Field | Extract Class, Move Function, Introduce Special Case |
| Message Chains | Hide Delegate, Extract Function, Move Function |
| Middle Man | Remove Middle Man, Inline Function, Replace Superclass with Delegate, Replace Subclass with Delegate |
| Insider Trading | Move Function, Move Field, Hide Delegate, Replace Subclass with Delegate, Replace Superclass with Delegate |
| Large Class | Extract Class, Extract Superclass, Replace Type Code with Subclasses |
| Alternative Classes with Different Interfaces | Change Function Declaration, Move Function, Extract Superclass |
| Data Class | Encapsulate Record, Remove Setting Method, Move Function, Extract Function |
| Refused Bequest | Push Down Method, Push Down Field, Replace Subclass with Delegate, Replace Superclass with Delegate |
| Comments | Extract Function, Change Function Declaration, Introduce Assertion |

Checked against ch. 3 on 2026-10-31: every refactoring the chapter cites as "Name (page)" under
each smell is in its row. Data Class lists Split Phase with a caveat: the book's smell table names it, but the chapter
text mentions it as the example of an exception (an immutable result record), not as a fix.

---

## 4. How each piece becomes a file

### 4.1 `SKILL.md`

Frontmatter `name: refactoring` and a `description` (at most 1024 characters) that names
the catalog, the common symptoms and the most used refactorings, so the agent finds the skill
both by problem ("this class does too much") and by name ("do an Extract Class"). The body has
the flow (smell → refactoring → file, with the discipline before the first step), the smell
quick index, and one table per chapter with every refactoring, a one-line "when" and a link to
its file. It ends with the Source line:

```markdown
Sources: Martin Fowler, *Refactoring: Improving the Design of Existing Code*, 2nd ed., ...;
Joshua Kerievsky, *Refactoring to Patterns*, ...; Erich Gamma, Richard Helm, Ralph Johnson and
John Vlissides, *Design Patterns*, ... Paraphrased; see the package NOTICE.
```

When a reference file is added, renamed or removed, its row in the `SKILL.md` table changes
with it.

### 4.2 A refactoring's reference file

```markdown
# Extract Class

Fowler (2018), ch. 7. Formerly / aka: —. Inverse: Inline Class
([inline-class.md](inline-class.md)).

## When to use
Smells: Large Class, Divergent Change, Data Clumps. (paraphrase, a few bullets, plus when
not to use it if the book says so)

## Mechanics
1. ... (paraphrase of the book's steps, numbered, one testable step per item)

## Example
Before / after in C#, written for this package (not copied from the book).

## C# notes
- Only when section 2 has a C# note.

## Verification
- Compiles and the tests pass after every step; one commit per refactoring.
```

No frontmatter and no Source line: the credit is in `SKILL.md` and the NOTICE. A link to
another refactoring is relative: `[inline-class.md](inline-class.md)` in the same chapter folder,
`[move-function.md](../moving-features/move-function.md)` in another. For a web-only
refactoring, the citation line says "web edition only" and links the refactoring.com summary instead of the chapter.

### 4.3 What goes in each part

| Part | Comes from | Note |
|---|---|---|
| Name, formerly / aka, inverse | the book's section header (section 2); the web edition for the web-only ones | short: may be literal |
| When to use, mechanics | the book (its web edition for the web-only ones) | **paraphrase**, with the chapter; nothing copied |
| Example | written for this package in C# | current, neutral theme per chapter, C# 9 (section 7); not the book's example or domain |
| C# notes | section 2, "C# note" column | only where there is something to say |
| Verification | ch. 4 + `references/fowler/discipline.md` | the shared check, plus one or two specific to the refactoring |
| Source line | this spec (4.1) | once, at the end of `SKILL.md`; credits the author and the publisher |

Nothing in the skill names a specific project, framework, engine or team process.


---

## 5. Kerievsky's refactorings to patterns

Source: Joshua Kerievsky, *Refactoring to Patterns*, Addison-Wesley (Pearson Education), 2004,
chapters 4 and 6–11. Each refactoring is a sequence of smaller refactorings, mostly Fowler's,
that ends at a pattern (*to*), moves partway (*towards*) or removes one (*away*). The online
catalog at https://www.industriallogic.com/refactoring-to-patterns/catalog/ has only a summary
and a diagram for each; the mechanics come from the book.

### 5.1 The 27 refactorings

Checked against the book's own list of refactorings (inside front cover); **Direction** comes from its "Refactoring Directions" table. The
book's mechanics name Fowler's refactorings by their 1st-edition names; the reference files use
the 2nd-edition names (section 2) and link their files.

**C# note** is what the reference file must add because the book's examples are Java: only
generic C# points. Where it says "—", the file has no C# notes section.

#### Chapter 6: Creation (`kerievsky/creation`)

| # | Refactoring | Pattern | Direction | C# note |
|---|---|---|---|---|
| 1 | Replace Constructors with Creation Methods | Creation Method | to | optional parameters and object initializers do not name the variant; a `record` with a private constructor works the same way |
| 2 | Move Creation Knowledge to Factory | Factory | to | — |
| 3 | Encapsulate Classes with Factory | Factory | to | hide the classes with `internal` (or nested `private`) types and constructors; tests can use `InternalsVisibleTo` |
| 4 | Introduce Polymorphic Creation with Factory Method | Factory Method | to | the factory method is `protected abstract`, or `protected virtual` with a default |
| 5 | Encapsulate Composite with Builder | Builder | to (Builder); away (Composite) | — |
| 6 | Inline Singleton | Singleton | away | a `static class` counts as a Singleton here |

#### Chapter 7: Simplification (`kerievsky/simplification`)

| # | Refactoring | Pattern | Direction | C# note |
|---|---|---|---|---|
| 7 | Compose Method | Composed Method | to | expression-bodied members and local functions keep the pieces short |
| 8 | Replace Conditional Logic with Strategy | Strategy | to, towards | an interface, or an abstract class if the strategies share code; stateless strategies can be `static readonly` |
| 9 | Move Embellishment to Decorator | Decorator | to, towards | — |
| 10 | Replace State-Altering Conditionals with State | State | to, towards | shared `static readonly` state instances, nested `private sealed` subclasses; persist a stable code, not the object |
| 11 | Replace Implicit Tree with Composite | Composite | to | a `record` leaf; expose children as `IReadOnlyList<T>` |
| 12 | Replace Conditional Dispatcher with Command | Command | to, towards | a `Dictionary<string, Func<...>>` is a lighter command type for tiny handlers |

#### Chapter 8: Generalization (`kerievsky/generalization`)

| # | Refactoring | Pattern | Direction | C# note |
|---|---|---|---|---|
| 13 | Form Template Method | Template Method | to | a non-`virtual` template method is the C# `final`; `abstract` and `virtual` `protected` steps |
| 14 | Extract Composite | Composite | to | expose children as `IReadOnlyList<T>` |
| 15 | Replace One/Many Distinctions with Composite | Composite | to | a `params`/`IEnumerable<T>` overload may be enough |
| 16 | Replace Hard-Coded Notifications with Observer | Observer | to, towards | `event EventHandler<T>`; every `+=` needs its `-=` |
| 17 | Unify Interfaces with Adapter | Adapter | to, towards | — |
| 18 | Extract Adapter | Adapter | to | — |
| 19 | Replace Implicit Language with Interpreter | Interpreter | to | `Func<T, bool>` or LINQ may be enough; `Expression<Func<T, bool>>` when a provider translates the criteria |

#### Chapter 9: Protection (`kerievsky/protection`)

| # | Refactoring | Pattern | Direction | C# note |
|---|---|---|---|---|
| 20 | Replace Type Code with Class | — | — | an `enum` accepts any integer; use a sealed class with a private constructor for a closed set |
| 21 | Limit Instantiation with Singleton | Singleton | to | `static readonly` or `Lazy<T>`; a DI singleton lifetime often replaces the pattern |
| 22 | Introduce Null Object | Null Object | to | with nullable reference types the field is no longer nullable; a shared static instance |

#### Chapter 10: Accumulation (`kerievsky/accumulation`)

| # | Refactoring | Pattern | Direction | C# note |
|---|---|---|---|---|
| 23 | Move Accumulation to Collecting Parameter | Collecting Parameter | to | `StringBuilder`, or a `TextWriter` parameter |
| 24 | Move Accumulation to Visitor | Visitor | to, towards (Visitor); away (Iterator) | a `switch` expression with type patterns often suffices; a generic visitor returns values |

#### Chapter 11: Utilities (`kerievsky/utilities`)

| # | Refactoring | Pattern | Direction | C# note |
|---|---|---|---|---|
| 25 | Chain Constructors | — | — | `: this(...)`; optional parameters as an alternative; primary constructors |
| 26 | Unify Interfaces | — | — | `virtual`/`override`, not hiding; default interface methods |
| 27 | Extract Parameter | — | — | `ArgumentNullException.ThrowIfNull` |

Overlaps with Fowler's 2nd edition, kept short and pointing to the Fowler file: Compose Method
(Extract Function, Slide Statements), Replace Type Code with Class (Replace Primitive with
Object, which subsumes it) and Introduce Null Object (Introduce Special Case, its new name).

### 5.2 The 12 smells

From ch. 4 and the inside back cover, in `references/kerievsky/smells.md`. The "Fowler's smell"
column is the bridge that the quick index in `SKILL.md` uses; the two `smells.md` files do not
refer to each other.

| Smell | Fowler's smell | Refactorings |
|---|---|---|
| Duplicated Code | Duplicated Code | Form Template Method, Introduce Polymorphic Creation with Factory Method, Chain Constructors, Replace One/Many Distinctions with Composite, Extract Composite, Unify Interfaces with Adapter, Introduce Null Object |
| Long Method | Long Function | Compose Method, Move Accumulation to Collecting Parameter, Replace Conditional Dispatcher with Command, Move Accumulation to Visitor, Replace Conditional Logic with Strategy |
| Conditional Complexity | new | Replace Conditional Logic with Strategy, Move Embellishment to Decorator, Replace State-Altering Conditionals with State, Introduce Null Object |
| Primitive Obsession | Primitive Obsession | Replace Type Code with Class, Replace State-Altering Conditionals with State, Replace Conditional Logic with Strategy, Replace Implicit Tree with Composite, Replace Implicit Language with Interpreter, Move Embellishment to Decorator, Encapsulate Composite with Builder |
| Indecent Exposure | new | Encapsulate Classes with Factory |
| Solution Sprawl | new (the book calls it the twin of Shotgun Surgery) | Move Creation Knowledge to Factory |
| Alternative Classes with Different Interfaces | same | Unify Interfaces with Adapter |
| Lazy Class | Lazy Element | Inline Singleton |
| Large Class | Large Class | Replace Conditional Dispatcher with Command, Replace State-Altering Conditionals with State, Replace Implicit Language with Interpreter |
| Switch Statements | Repeated Switches | Replace Conditional Dispatcher with Command, Move Accumulation to Visitor |
| Combinatorial Explosion | new | Replace Implicit Language with Interpreter |
| Oddball Solution | new | Substitute Algorithm, Unify Interfaces with Adapter |

### 5.3 File format

Same as section 4.2, with a different citation line:

```markdown
# Replace State-Altering Conditionals with State

Kerievsky (2004), ch. 7. Pattern: State. Direction: to, towards.
```

A mechanics step that is a Fowler refactoring names it by its 2nd-edition name and links its
file; a refactoring with no 2nd-edition counterpart (such as Extract Interface) is described in
plain words and marked "(1st ed. only)". "When to use" includes the book's liabilities, so the
agent knows when the pattern is not worth it. Examples are original C#, as in section 4.3.

---

## 6. The GoF design patterns

Source: Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides, *Design Patterns: Elements of
Reusable Object-Oriented Software*, Addison-Wesley, 1995. Covered: ch. 1 (except §1.2), ch. 3-5,
the comparisons that close each of them, and §6.1. Left out: §1.2 (MVC in Smalltalk), ch. 2 (a
long case study in its own domain), §6.2-6.5 (history and community) and the appendices. The
`gof/` files are self-contained: they do not mention the refactoring catalogs, and the table at the
end of `SKILL.md` links each pattern to the refactorings that reach it.

| Pattern | Folder | Ch. |
|---|---|---|
| Abstract Factory | `creational` | 3 |
| Builder | `creational` | 3 |
| Factory Method | `creational` | 3 |
| Prototype | `creational` | 3 |
| Singleton | `creational` | 3 |
| Adapter | `structural` | 4 |
| Bridge | `structural` | 4 |
| Composite | `structural` | 4 |
| Decorator | `structural` | 4 |
| Facade | `structural` | 4 |
| Flyweight | `structural` | 4 |
| Proxy | `structural` | 4 |
| Chain of Responsibility | `behavioral` | 5 |
| Command | `behavioral` | 5 |
| Interpreter | `behavioral` | 5 |
| Iterator | `behavioral` | 5 |
| Mediator | `behavioral` | 5 |
| Memento | `behavioral` | 5 |
| Observer | `behavioral` | 5 |
| State | `behavioral` | 5 |
| Strategy | `behavioral` | 5 |
| Template Method | `behavioral` | 5 |
| Visitor | `behavioral` | 5 |


File format:

```markdown
# State

Gamma et al. (1995), ch. 5. Category: object behavioral.

## Intent
## When it pays off
## Participants in C#
## Example (C#)
## Variations
## Risks and C# alternatives
## Related patterns
## Verification
```

## 7. C# level of every example

All examples in the package are C# 9, so that they also compile in Unity, whose compiler stops at
C# 9: no `record` or `init` (they need an `IsExternalInit` shim there), no `required`, no primary
constructors, no collection expressions, no file-scoped namespaces, no `global using`, no raw
strings, no list patterns. Pattern matching, switch expressions, `new()`, nullable reference types,
delegates, events, LINQ and `async` are used freely. Every block is compiled against
`netstandard2.1` with `LangVersion` 9; a deliberately partial block starts with `// fragment`.
Examples use current, neutral themes (checkout, billing, payments, HTTP clients, an AI assistant,
IoT, feature flags, report export, cloud storage...), never the books' own examples.
