---
name: gof-design-patterns
description: "Catálogo de consulta dos 23 padrões de projeto do GoF (Gamma et al., Design Patterns, 1995): intenção, quando compensa, participantes, exemplo em C#, variações, riscos e padrões relacionados (Abstract Factory, Builder, Singleton, Adapter, Decorator, Facade, Observer, State, Strategy, Visitor...), mais os princípios de design do livro. Use quando um padrão de projeto for citado, para escolher um padrão para um problema de design ou para conferir se um padrão compensa. Não ensina a refatorar: para levar o código até um padrão, use a skill kerievsky-refactoring-to-patterns."
---

# Padrões de projeto: o catálogo do GoF

Gamma et al. (1995): os 23 padrões de projeto (cap. 1, 3-5 e §6.1). Esta skill é de consulta: descreve
cada padrão em si (intenção, quando compensa, participantes, exemplo em C#). Ela não ensina a
refatorar. Para chegar a um padrão a partir do código existente, use a skill
`kerievsky-refactoring-to-patterns`; os passos menores estão em `fowler-refactoring`.

1. Se o pedido nomear um padrão, abra o arquivo dele na tabela abaixo.
2. Se perguntar qual padrão serve para um problema de design, comece por
   [references/catalog.md](references/catalog.md): as 23 intenções, propósito e escopo, e o que cada
   padrão deixa variar. Leia também [references/principles.md](references/principles.md): programe
   para uma interface, prefira composição, como escolher e usar um padrão.
3. Confira "Quando compensa" e "Riscos e alternativas em C#" antes de recomendar. Um padrão que não
   paga o custo não deve entrar.
4. As colunas de refatorações dizem como chegar ao padrão a partir do código existente, ou como
   sair dele. Aplique-as com a skill indicada.

## Arquivos de referência

Intenção, Quando compensa, Participantes em C#, Exemplo (C#), Variações, Riscos e alternativas em
C#, Padrões relacionados, Verificação.

## Os 23 padrões de projeto

Cada arquivo descreve o padrão em si. As colunas à direita ligam o padrão aos dois catálogos de
refatoração: como chegar a ele a partir do código existente, ou como sair dele.

| Padrão | Arquivo | Refatorações de Kerievsky (direção; skill `kerievsky-refactoring-to-patterns`) | Refatorações de Fowler (skill `fowler-refactoring`) |
|---|---|---|---|
| Abstract Factory | [abstract-factory.md](references/creational/abstract-factory.md) | — | — |
| Builder | [builder.md](references/creational/builder.md) | `encapsulate-composite-with-builder` (até) | — |
| Factory Method | [factory-method.md](references/creational/factory-method.md) | `introduce-polymorphic-creation-with-factory-method` (até) | — |
| Prototype | [prototype.md](references/creational/prototype.md) | — | — |
| Singleton | [singleton.md](references/creational/singleton.md) | `limit-instantiation-with-singleton` (até), `inline-singleton` (longe) | — |
| Adapter | [adapter.md](references/structural/adapter.md) | `extract-adapter` (até), `unify-interfaces-with-adapter` (até, rumo a) | — |
| Bridge | [bridge.md](references/structural/bridge.md) | — | — |
| Composite | [composite.md](references/structural/composite.md) | `replace-one-many-distinctions-with-composite` (até), `extract-composite` (até), `replace-implicit-tree-with-composite` (até), `encapsulate-composite-with-builder` (longe) | — |
| Decorator | [decorator.md](references/structural/decorator.md) | `move-embellishment-to-decorator` (até, rumo a) | — |
| Facade | [facade.md](references/structural/facade.md) | — | — |
| Flyweight | [flyweight.md](references/structural/flyweight.md) | — | — |
| Proxy | [proxy.md](references/structural/proxy.md) | — | — |
| Chain of Responsibility | [chain-of-responsibility.md](references/behavioral/chain-of-responsibility.md) | — | — |
| Command | [command.md](references/behavioral/command.md) | `replace-conditional-dispatcher-with-command` (até, rumo a) | `replace-function-with-command`, `replace-command-with-function` |
| Interpreter | [interpreter.md](references/behavioral/interpreter.md) | `replace-implicit-language-with-interpreter` (até) | — |
| Iterator | [iterator.md](references/behavioral/iterator.md) | `move-accumulation-to-visitor` (longe) | — |
| Mediator | [mediator.md](references/behavioral/mediator.md) | — | — |
| Memento | [memento.md](references/behavioral/memento.md) | — | — |
| Observer | [observer.md](references/behavioral/observer.md) | `replace-hard-coded-notifications-with-observer` (até, rumo a) | — |
| State | [state.md](references/behavioral/state.md) | `replace-state-altering-conditionals-with-state` (até, rumo a) | `replace-type-code-with-subclasses`, `replace-conditional-with-polymorphism`, `replace-subclass-with-delegate` |
| Strategy | [strategy.md](references/behavioral/strategy.md) | `replace-conditional-logic-with-strategy` (até, rumo a) | `replace-conditional-with-polymorphism`, `replace-subclass-with-delegate` |
| Template Method | [template-method.md](references/behavioral/template-method.md) | `form-template-method` (até) | — |
| Visitor | [visitor.md](references/behavioral/visitor.md) | `move-accumulation-to-visitor` (até, rumo a) | — |

Fonte: Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides, *Design Patterns: Elements of
Reusable Object-Oriented Software*, Addison-Wesley, 1995. Parafraseado; veja o NOTICE do pacote.
