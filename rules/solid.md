# SOLID

A criterion for judging any design change, before and after refactoring. Source: Martin (2002),
ch. 8–12; the SRP follows Martin's revised version (2017), ch. 7. This rule says what to check; the
how is in the `fowler-refactoring` and `kerievsky-refactoring-to-patterns` skills.

## The principles

**SRP: Single Responsibility Principle.** A module should answer to a single actor, that is, to one
group of people who ask for the same kind of change (Martin, 2017, ch. 7). In the 2002 wording, a
class should have only one reason to change (Martin, 2002, ch. 8). When two responsibilities share
a class, a change one actor asks for can break what the other one uses.

**OCP: Open-Closed Principle.** Classes, modules and functions should be open for extension and
closed for modification (Martin, 2002, ch. 9): new behavior comes in as new code, without editing
what already works. The sign of a violation is rigidity: a change that cascades through dependent
modules. The way out is to isolate what varies behind an abstraction.

**LSP: Liskov Substitution Principle.** A subtype must be able to replace its base type without the
caller noticing (Martin, 2002, ch. 10). Inheritance is about behavior, not structure: a subclass
that needs a type check, ignores a method or throws where the base does not breaks the contract,
and the client code ends up depending on the concrete subclasses.

**ISP: Interface Segregation Principle.** A client should not be forced to depend on methods it
does not use (Martin, 2002, ch. 12). A large interface couples all its clients: a change one of
them asks for forces the others to recompile or adapt. The way out is to give each kind of client
the interface it needs.

**DIP: Dependency Inversion Principle.** High-level modules should not depend on low-level modules;
both should depend on abstractions. And abstractions should not depend on details; details depend
on them (Martin, 2002, ch. 11). The business rule defines the interface it needs, and the
infrastructure (network, engine, files) implements it.

## Checks

| Principle | Check | Sign of a violation | Path |
|---|---|---|---|
| SRP | Does the class answer to a single actor? | Requests from different areas touch the same file; Divergent Change | `F:extract-class`, `F:split-phase`, `F:move-function` |
| OCP | Does a new case come in without editing existing code? | A `switch`/`if` on type that grows with each case; Repeated Switches | `F:replace-conditional-with-polymorphism`, `K:replace-conditional-logic-with-strategy`, `K:replace-state-altering-conditionals-with-state` |
| LSP | Does every subclass work where the base is expected? | A type check before use; an empty override or one that throws; Refused Bequest | `F:replace-subclass-with-delegate`, `F:replace-superclass-with-delegate`, `F:push-down-method` |
| ISP | Does each client depend only on what it uses? | A large interface with methods some implementers leave empty | Split the interface per client; `F:extract-class`, `K:unify-interfaces-with-adapter` |
| DIP | Does the high-level rule depend on an abstraction? | Domain code calling an API, the network, files or the engine directly; `new` of a concrete class | `K:extract-adapter`, `K:encapsulate-classes-with-factory`, `K:move-creation-knowledge-to-factory` |

`F:` is a refactoring from the `fowler-refactoring` skill; `K:`, from the
`kerievsky-refactoring-to-patterns` skill.

## Rules

- When you propose or justify a change by a principle, cite it in the plan and in the commit
  (`SOLID:OCP`).
- A principle is not a goal: refactor only when the violation has a real cost (frequent change, a
  bug, hard extension). Stable code that violates a principle can stay.
- If the path leads to a GoF pattern, first read it in the `gof-design-patterns` skill.

## Source

MARTIN, R. C. *Agile Software Development: Principles, Patterns, and Practices*. Prentice Hall, 2002
(ch. 8–12), and *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Pearson,
2017 (ch. 7, the SRP). Paraphrased; the books' text is not reproduced.
