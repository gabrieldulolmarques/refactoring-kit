---
name: gof-design-patterns
description: "Reference catalog of the 23 GoF design patterns (Gamma et al., Design Patterns, 1995): intent, when it pays off, participants, C# example, variations, risks and related patterns (Abstract Factory, Builder, Singleton, Adapter, Decorator, Facade, Observer, State, Strategy, Visitor...), plus the book's design principles. Use when a design pattern is named, to choose a pattern for a design problem, or to check whether a pattern pays off. It does not teach refactoring: to take code to a pattern, use the kerievsky-refactoring-to-patterns skill."
---

# Design patterns: the GoF catalog

Gamma et al. (1995): the 23 design patterns (ch. 1, 3-5 and §6.1). This skill is for lookup: it
describes each pattern itself (intent, when it pays off, participants, C# example). It does not
teach refactoring. To reach a pattern from existing code, use the
`kerievsky-refactoring-to-patterns` skill; the smaller steps are in `fowler-refactoring`.

1. If the request names a pattern, open its file from the table below.
2. If it asks which pattern fits a design problem, start at
   [references/catalog.md](references/catalog.md): the 23 intents, purpose and scope, and what each
   pattern lets vary. Also read [references/principles.md](references/principles.md): program to an
   interface, favor composition, how to choose and use a pattern.
3. Check "When it pays off" and "Risks and alternatives in C#" before recommending. A pattern that
   does not pay its cost should not go in.
4. The refactoring columns say how to reach the pattern from existing code, or how to leave it.
   Apply them with the skill named.

## Reference files

Intent, When it pays off, Participants in C#, Example (C#), Variations, Risks and alternatives in
C#, Related patterns, Verification.

## The 23 design patterns

Each file describes the pattern itself. The columns on the right link the pattern to the two
refactoring catalogs: how to reach it from existing code, or how to leave it.

| Pattern | File | Kerievsky refactorings (direction; skill `kerievsky-refactoring-to-patterns`) | Fowler refactorings |
|---|---|---|---|
| Abstract Factory | [abstract-factory.md](references/creational/abstract-factory.md) | — | — |
| Builder | [builder.md](references/creational/builder.md) | `encapsulate-composite-with-builder` (to) | — |
| Factory Method | [factory-method.md](references/creational/factory-method.md) | `introduce-polymorphic-creation-with-factory-method` (to) | — |
| Prototype | [prototype.md](references/creational/prototype.md) | — | — |
| Singleton | [singleton.md](references/creational/singleton.md) | `limit-instantiation-with-singleton` (to), `inline-singleton` (away) | — |
| Adapter | [adapter.md](references/structural/adapter.md) | `extract-adapter` (to), `unify-interfaces-with-adapter` (to, towards) | — |
| Bridge | [bridge.md](references/structural/bridge.md) | — | — |
| Composite | [composite.md](references/structural/composite.md) | `replace-one-many-distinctions-with-composite` (to), `extract-composite` (to), `replace-implicit-tree-with-composite` (to), `encapsulate-composite-with-builder` (away) | — |
| Decorator | [decorator.md](references/structural/decorator.md) | `move-embellishment-to-decorator` (to, towards) | — |
| Facade | [facade.md](references/structural/facade.md) | — | — |
| Flyweight | [flyweight.md](references/structural/flyweight.md) | — | — |
| Proxy | [proxy.md](references/structural/proxy.md) | — | — |
| Chain of Responsibility | [chain-of-responsibility.md](references/behavioral/chain-of-responsibility.md) | — | — |
| Command | [command.md](references/behavioral/command.md) | `replace-conditional-dispatcher-with-command` (to, towards) | `replace-function-with-command`, `replace-command-with-function` |
| Interpreter | [interpreter.md](references/behavioral/interpreter.md) | `replace-implicit-language-with-interpreter` (to) | — |
| Iterator | [iterator.md](references/behavioral/iterator.md) | `move-accumulation-to-visitor` (away) | — |
| Mediator | [mediator.md](references/behavioral/mediator.md) | — | — |
| Memento | [memento.md](references/behavioral/memento.md) | — | — |
| Observer | [observer.md](references/behavioral/observer.md) | `replace-hard-coded-notifications-with-observer` (to, towards) | — |
| State | [state.md](references/behavioral/state.md) | `replace-state-altering-conditionals-with-state` (to, towards) | `replace-type-code-with-subclasses`, `replace-conditional-with-polymorphism`, `replace-subclass-with-delegate` |
| Strategy | [strategy.md](references/behavioral/strategy.md) | `replace-conditional-logic-with-strategy` (to, towards) | `replace-conditional-with-polymorphism`, `replace-subclass-with-delegate` |
| Template Method | [template-method.md](references/behavioral/template-method.md) | `form-template-method` (to) | — |
| Visitor | [visitor.md](references/behavioral/visitor.md) | `move-accumulation-to-visitor` (to, towards) | — |

Source: Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides, *Design Patterns: Elements of
Reusable Object-Oriented Software*, Addison-Wesley, 1995. Paraphrased; see the package NOTICE.
