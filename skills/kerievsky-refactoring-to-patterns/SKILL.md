---
name: kerievsky-refactoring-to-patterns
description: "Joshua Kerievsky's refactorings to patterns (Refactoring to Patterns): 12 code smells and 27 refactorings that take code to a design pattern, towards it or away from it (Strategy, State, Command, Observer, Composite, Factory, Template Method...), each with mechanics, a C# example and verification. Use when conditionals or switches keep growing, when object creation is scattered, or when one of Kerievsky's refactorings is named. Uses the fowler-refactoring skill for the smaller steps and the gof-design-patterns skill to describe the target pattern when it is a GoF pattern."
---

# Refactoring to patterns: Kerievsky

Kerievsky (2004), ch. 4 (smells) and ch. 6-11 (refactorings to patterns). Each refactoring is a
sequence of smaller refactorings, many of them Fowler's, from the `fowler-refactoring` skill,
installed next to this one (the links point to `../fowler-refactoring/`). The destination
patterns that come from the GoF are in the `gof-design-patterns` skill (Gamma et al., 1995), also installed next to this
one (the links point to `../gof-design-patterns/`).

Flow: **smell -> refactoring -> its file in `references/`.**

1. Name the smell. Use the quick index below, or the symptoms in
   [references/smells.md](references/smells.md).
2. Pick one refactoring for that smell and open its file from the tables further down. Reach
   for a refactoring to a pattern only when the smell calls for it, and stop as soon as the
   smell is gone: going *towards* a pattern is often enough. Before you start, read the
   pattern in the `gof-design-patterns` skill if it is a GoF pattern (the five in the table at the
   end are not; the refactoring's own file describes them).
3. Before changing anything, check the safety net in
   [Fowler's discipline.md](../fowler-refactoring/references/discipline.md): passing tests,
   small steps, a commit after each green refactoring, with the source ID
   (`[K:<slug>]`) and no push. Also read
   [references/discipline.md](references/discipline.md): when a pattern pays off, and when to stop.
4. Follow the mechanics one step at a time. When a step names one of Fowler's refactorings, open
   its file through the link. Compile and run the tests after each step; if anything fails, undo
   the step.

If the request names a refactoring, skip to step 3 and open its file directly. If it names a
design pattern, or asks which pattern fits a design problem, use the
`gof-design-patterns` skill.

## Smell quick index

| Smell | Refactorings |
|---|---|
| Duplicated Code | `form-template-method`, `chain-constructors` |
| Long Function (Kerievsky: Long Method) | `compose-method`, `move-accumulation-to-collecting-parameter` |
| Primitive Obsession | `replace-type-code-with-class`, `replace-state-altering-conditionals-with-state` |
| Repeated Switches (Kerievsky: Switch Statements) | `replace-conditional-dispatcher-with-command`, `move-accumulation-to-visitor` |
| Lazy Element (Kerievsky: Lazy Class) | `inline-singleton` |
| Large Class | `replace-conditional-dispatcher-with-command`, `replace-state-altering-conditionals-with-state` |
| Alternative Classes with Different Interfaces | `unify-interfaces-with-adapter` |
| Conditional Complexity | `replace-conditional-logic-with-strategy`, `replace-state-altering-conditionals-with-state`, `move-embellishment-to-decorator`, `introduce-null-object` |
| Indecent Exposure | `encapsulate-classes-with-factory` |
| Solution Sprawl | `move-creation-knowledge-to-factory` |
| Combinatorial Explosion | `replace-implicit-language-with-interpreter` |
| Oddball Solution | `substitute-algorithm` (Fowler's), `unify-interfaces-with-adapter` |

These are Kerievsky's 12 smells. Seven match one of Fowler's smells; where his name differs, it is
in parentheses. Fowler's other smells are in the `fowler-refactoring` skill.
`smells.md` lists every option. Each slug is a reference file; the tables below give the path.

## Reference files

- **Kerievsky:** When to use, Mechanics, Example (C#), Notes (C#) (only where there is something
  specific to C#), Verification. What a file adds beyond the book is marked **Beyond the book**.
  Each file names the target pattern and the direction: *to* the pattern, *towards* it, or
  *away* from it.

## Kerievsky: the refactorings to patterns

Each one is a sequence of smaller refactorings, many of them Fowler's, that ends at a pattern,
moves towards it, or removes one. The Pattern column gives the direction.

### Creation (Kerievsky, ch. 6)

| Refactoring | Pattern | When | File |
|---|---|---|---|
| Replace Constructors with Creation Methods | Creation Method (to) | several constructors make it hard to know which one to call | [replace-constructors-with-creation-methods.md](references/creation/replace-constructors-with-creation-methods.md) |
| Move Creation Knowledge to Factory | Factory (to) | the data and code used to create an object are spread over many classes | [move-creation-knowledge-to-factory.md](references/creation/move-creation-knowledge-to-factory.md) |
| Encapsulate Classes with Factory | Factory (to) | clients instantiate classes of one package that share an interface and could be hidden | [encapsulate-classes-with-factory.md](references/creation/encapsulate-classes-with-factory.md) |
| Introduce Polymorphic Creation with Factory Method | Factory Method (to) | sibling classes repeat a method except for the object it creates | [introduce-polymorphic-creation-with-factory-method.md](references/creation/introduce-polymorphic-creation-with-factory-method.md) |
| Encapsulate Composite with Builder | Builder (to); Composite (away) | building a Composite is repetitive, complicated or error-prone | [encapsulate-composite-with-builder.md](references/creation/encapsulate-composite-with-builder.md) |
| Inline Singleton | Singleton (away) | code needs an object but not global access to it | [inline-singleton.md](references/creation/inline-singleton.md) |

### Simplification (Kerievsky, ch. 7)

| Refactoring | Pattern | When | File |
|---|---|---|---|
| Compose Method | Composed Method (to) | a method's logic is hard to follow at a glance | [compose-method.md](references/simplification/compose-method.md) |
| Replace Conditional Logic with Strategy | Strategy (to, towards) | conditionals choose which variant of a calculation runs | [replace-conditional-logic-with-strategy.md](references/simplification/replace-conditional-logic-with-strategy.md) |
| Move Embellishment to Decorator | Decorator (to, towards) | code adds optional behavior on top of a class's core job | [move-embellishment-to-decorator.md](references/simplification/move-embellishment-to-decorator.md) |
| Replace State-Altering Conditionals with State | State (to, towards) | conditionals that control an object's state transitions are complex | [replace-state-altering-conditionals-with-state.md](references/simplification/replace-state-altering-conditionals-with-state.md) |
| Replace Implicit Tree with Composite | Composite (to) | a tree is built implicitly with strings or other primitives | [replace-implicit-tree-with-composite.md](references/simplification/replace-implicit-tree-with-composite.md) |
| Replace Conditional Dispatcher with Command | Command (to, towards) | conditionals dispatch requests and run their actions | [replace-conditional-dispatcher-with-command.md](references/simplification/replace-conditional-dispatcher-with-command.md) |

### Generalization (Kerievsky, ch. 8)

| Refactoring | Pattern | When | File |
|---|---|---|---|
| Form Template Method | Template Method (to) | two subclasses do similar steps in the same order | [form-template-method.md](references/generalization/form-template-method.md) |
| Extract Composite | Composite (to) | subclasses of a hierarchy implement the same Composite | [extract-composite.md](references/generalization/extract-composite.md) |
| Replace One/Many Distinctions with Composite | Composite (to) | one piece of code handles a single object and another handles a collection | [replace-one-many-distinctions-with-composite.md](references/generalization/replace-one-many-distinctions-with-composite.md) |
| Replace Hard-Coded Notifications with Observer | Observer (to, towards) | classes notify specific receivers in hard-coded calls | [replace-hard-coded-notifications-with-observer.md](references/generalization/replace-hard-coded-notifications-with-observer.md) |
| Unify Interfaces with Adapter | Adapter (to, towards) | clients use two classes the same way but their interfaces differ | [unify-interfaces-with-adapter.md](references/generalization/unify-interfaces-with-adapter.md) |
| Extract Adapter | Adapter (to) | one class adapts several versions of a component, library or API | [extract-adapter.md](references/generalization/extract-adapter.md) |
| Replace Implicit Language with Interpreter | Interpreter (to) | many methods or combinations of them express the elements of an implicit language | [replace-implicit-language-with-interpreter.md](references/generalization/replace-implicit-language-with-interpreter.md) |

### Protection (Kerievsky, ch. 9)

| Refactoring | Pattern | When | File |
|---|---|---|---|
| Replace Type Code with Class | — | a field's type (a string or int) does not protect it from invalid values | [replace-type-code-with-class.md](references/protection/replace-type-code-with-class.md) |
| Limit Instantiation with Singleton | Singleton (to) | code creates many instances of an object when one is enough and that costs memory or time | [limit-instantiation-with-singleton.md](references/protection/limit-instantiation-with-singleton.md) |
| Introduce Null Object | Null Object (to) | the same check for a null field or variable is repeated across the code | [introduce-null-object.md](references/protection/introduce-null-object.md) |

### Accumulation (Kerievsky, ch. 10)

| Refactoring | Pattern | When | File |
|---|---|---|---|
| Move Accumulation to Collecting Parameter | Collecting Parameter (to) | one large method gathers information into a local variable | [move-accumulation-to-collecting-parameter.md](references/accumulation/move-accumulation-to-collecting-parameter.md) |
| Move Accumulation to Visitor | Visitor (to, towards); Iterator (away) | one method gathers information from classes with different interfaces | [move-accumulation-to-visitor.md](references/accumulation/move-accumulation-to-visitor.md) |

### Utilities (Kerievsky, ch. 11)

| Refactoring | Pattern | When | File |
|---|---|---|---|
| Chain Constructors | — | several constructors repeat the same code | [chain-constructors.md](references/utilities/chain-constructors.md) |
| Unify Interfaces | — | a superclass or interface needs the same interface as a subclass | [unify-interfaces.md](references/utilities/unify-interfaces.md) |
| Extract Parameter | — | a method or constructor assigns a field to a locally created value | [extract-parameter.md](references/utilities/extract-parameter.md) |

## Destination patterns

The patterns are in the `gof-design-patterns` skill: intent, when it pays off, participants and an
example for each one, and the table linking each pattern to the refactorings that reach it.
Kerievsky also refactors to five patterns that are not in GoF; their reference files describe them:

| Pattern | Kerievsky refactorings (direction) | Fowler refactorings |
|---|---|---|
| Creation Method | `replace-constructors-with-creation-methods` (to) | — |
| Factory | `move-creation-knowledge-to-factory` (to), `encapsulate-classes-with-factory` (to) | — |
| Composed Method | `compose-method` (to) | — |
| Collecting Parameter | `move-accumulation-to-collecting-parameter` (to) | — |
| Null Object | `introduce-null-object` (to) | `introduce-special-case` |

Source: Joshua Kerievsky, *Refactoring to Patterns*, Addison-Wesley (Pearson Education),
2004, and the online catalog at https://www.industriallogic.com/refactoring-to-patterns/catalog/.
Paraphrased; see the package NOTICE.
