---
name: kerievsky-refactoring-to-patterns
description: "Refatorações para padrões de Joshua Kerievsky (Refactoring to Patterns): 12 code smells e 27 refatorações que levam o código até um padrão de projeto, rumo a ele ou para longe dele (Strategy, State, Command, Observer, Composite, Factory, Template Method...), cada uma com mecânica, exemplo em C# e verificação. Use quando condicionais ou switches não param de crescer, quando a criação de objetos está espalhada ou quando uma refatoração de Kerievsky for citada. Usa a skill fowler-refactoring para os passos menores e a gof-design-patterns para descrever o padrão de destino, quando ele for do GoF."
---

# Refatoração para padrões: Kerievsky

Kerievsky (2004), cap. 4 (smells) e cap. 6-11 (refatorações para padrões). Cada refatoração é
uma sequência de refatorações menores, muitas delas de Fowler, da skill `fowler-refactoring`, que
fica instalada ao lado desta (os links apontam para `../fowler-refactoring/`). Os padrões de destino do GoF
estão na skill `gof-design-patterns` (Gamma et al., 1995), também instalada ao lado desta (os links
apontam para `../gof-design-patterns/`).

Fluxo: **smell -> refatoração -> seu arquivo em `references/`.**

1. Nomeie o smell. Use o índice rápido abaixo, ou os sintomas em
   [references/smells.md](references/smells.md).
2. Escolha uma refatoração para esse smell e abra o arquivo dela nas tabelas mais adiante. Só
   recorra a uma refatoração para padrão quando o smell pedir, e pare assim que o smell sumir:
   ir *rumo a* um padrão muitas vezes basta. Antes, leia o padrão na skill
   `gof-design-patterns`, se ele for do GoF (os cinco padrões da tabela no fim não são; o arquivo da
   própria refatoração os descreve).
3. Antes de alterar qualquer coisa, confira a rede de segurança em
   [discipline.md de Fowler](../fowler-refactoring/references/discipline.md): testes passando,
   passos pequenos, um commit após cada refatoração verde. Leia também
   [references/discipline.md](references/discipline.md): quando um padrão compensa e quando parar.
4. Siga a mecânica um passo de cada vez. Quando um passo citar uma refatoração de Fowler, abra o
   arquivo dela pelo link. Compile e execute os testes após cada passo; se algo falhar, desfaça
   o passo.

Se o pedido nomear uma refatoração, pule para o passo 3 e abra o arquivo dela diretamente. Se
nomear um padrão de projeto, ou perguntar qual padrão serve para um problema de design, use a skill
`gof-design-patterns`.

## Índice rápido de smells

| Smell | Refatorações |
|---|---|
| Código Duplicado (Duplicated Code) | `form-template-method`, `chain-constructors` |
| Função Longa (Long Function; Kerievsky: Método Longo) | `compose-method`, `move-accumulation-to-collecting-parameter` |
| Obsessão por Primitivos (Primitive Obsession) | `replace-type-code-with-class`, `replace-state-altering-conditionals-with-state` |
| Switches Repetidos (Repeated Switches; Kerievsky: Instruções Switch) | `replace-conditional-dispatcher-with-command`, `move-accumulation-to-visitor` |
| Elemento Ocioso (Lazy Element; Kerievsky: Classe Preguiçosa) | `inline-singleton` |
| Classe Grande (Large Class) | `replace-conditional-dispatcher-with-command`, `replace-state-altering-conditionals-with-state` |
| Classes Alternativas com Interfaces Diferentes (Alternative Classes with Different Interfaces) | `unify-interfaces-with-adapter` |
| Complexidade Condicional (Conditional Complexity) | `replace-conditional-logic-with-strategy`, `replace-state-altering-conditionals-with-state`, `move-embellishment-to-decorator`, `introduce-null-object` |
| Exposição Indecente (Indecent Exposure) | `encapsulate-classes-with-factory` |
| Solução Espalhada (Solution Sprawl) | `move-creation-knowledge-to-factory` |
| Explosão Combinatória (Combinatorial Explosion) | `replace-implicit-language-with-interpreter` |
| Solução Destoante (Oddball Solution) | `substitute-algorithm` (de Fowler), `unify-interfaces-with-adapter` |

São os 12 smells de Kerievsky. Sete correspondem a um smell de Fowler; onde o nome dele é
outro, está entre parênteses. Os demais smells de Fowler estão na skill `fowler-refactoring`.
O `smells.md` lista todas as opções. Cada slug é um arquivo de referência; as tabelas abaixo dão o caminho.

## Arquivos de referência

- **Kerievsky:** Quando usar, Mecânica, Exemplo (C#), Notas (C#) (só onde há algo próprio de
  C#), Verificação. O que um arquivo acrescenta além do livro vem marcado como **Além do livro**.
  Cada arquivo diz o padrão de destino e a direção: *até* o padrão, *rumo a* ele, ou para
  *longe* dele.

## Kerievsky: as refatorações para padrões

Cada uma é uma sequência de refatorações menores, muitas delas de Fowler, que termina em um
padrão, avança rumo a ele ou remove um. A coluna Padrão traz a direção.

### Criação (Kerievsky, cap. 6)

| Refatoração | Padrão | Quando | Arquivo |
|---|---|---|---|
| Substituir Construtores por Métodos de Criação (Replace Constructors with Creation Methods) | Creation Method (até) | vários construtores tornam difícil saber qual chamar | [replace-constructors-with-creation-methods.md](references/creation/replace-constructors-with-creation-methods.md) |
| Mover Conhecimento de Criação para Factory (Move Creation Knowledge to Factory) | Factory (até) | os dados e o código usados para criar um objeto estão espalhados por muitas classes | [move-creation-knowledge-to-factory.md](references/creation/move-creation-knowledge-to-factory.md) |
| Encapsular Classes com Factory (Encapsulate Classes with Factory) | Factory (até) | os clientes instanciam classes de um pacote que compartilham uma interface e poderiam ficar ocultas | [encapsulate-classes-with-factory.md](references/creation/encapsulate-classes-with-factory.md) |
| Introduzir Criação Polimórfica com Factory Method (Introduce Polymorphic Creation with Factory Method) | Factory Method (até) | classes irmãs repetem um método, exceto pelo objeto que ele cria | [introduce-polymorphic-creation-with-factory-method.md](references/creation/introduce-polymorphic-creation-with-factory-method.md) |
| Encapsular Composite com Builder (Encapsulate Composite with Builder) | Builder (até); Composite (longe) | montar um Composite é repetitivo, complicado ou sujeito a erros | [encapsulate-composite-with-builder.md](references/creation/encapsulate-composite-with-builder.md) |
| Internalizar Singleton (Inline Singleton) | Singleton (longe) | o código precisa de um objeto, mas não de acesso global a ele | [inline-singleton.md](references/creation/inline-singleton.md) |

### Simplificação (Kerievsky, cap. 7)

| Refatoração | Padrão | Quando | Arquivo |
|---|---|---|---|
| Compor Método (Compose Method) | Composed Method (até) | a lógica de um método é difícil de entender de relance | [compose-method.md](references/simplification/compose-method.md) |
| Substituir Lógica Condicional por Strategy (Replace Conditional Logic with Strategy) | Strategy (até, rumo a) | condicionais escolhem qual variante de um cálculo executar | [replace-conditional-logic-with-strategy.md](references/simplification/replace-conditional-logic-with-strategy.md) |
| Mover Embelezamento para Decorator (Move Embellishment to Decorator) | Decorator (até, rumo a) | o código acrescenta comportamento opcional ao trabalho principal de uma classe | [move-embellishment-to-decorator.md](references/simplification/move-embellishment-to-decorator.md) |
| Substituir Condicionais que Alteram Estado por State (Replace State-Altering Conditionals with State) | State (até, rumo a) | as condicionais que controlam as transições de estado de um objeto são complexas | [replace-state-altering-conditionals-with-state.md](references/simplification/replace-state-altering-conditionals-with-state.md) |
| Substituir Árvore Implícita por Composite (Replace Implicit Tree with Composite) | Composite (até) | uma árvore é montada implicitamente com strings ou outros primitivos | [replace-implicit-tree-with-composite.md](references/simplification/replace-implicit-tree-with-composite.md) |
| Substituir Despachante Condicional por Command (Replace Conditional Dispatcher with Command) | Command (até, rumo a) | condicionais despacham pedidos e executam suas ações | [replace-conditional-dispatcher-with-command.md](references/simplification/replace-conditional-dispatcher-with-command.md) |

### Generalização (Kerievsky, cap. 8)

| Refatoração | Padrão | Quando | Arquivo |
|---|---|---|---|
| Formar Template Method (Form Template Method) | Template Method (até) | duas subclasses fazem passos parecidos na mesma ordem | [form-template-method.md](references/generalization/form-template-method.md) |
| Extrair Composite (Extract Composite) | Composite (até) | subclasses de uma hierarquia implementam o mesmo Composite | [extract-composite.md](references/generalization/extract-composite.md) |
| Substituir Distinções Um/Muitos por Composite (Replace One/Many Distinctions with Composite) | Composite (até) | um trecho trata um único objeto e outro trata uma coleção deles | [replace-one-many-distinctions-with-composite.md](references/generalization/replace-one-many-distinctions-with-composite.md) |
| Substituir Notificações Fixas no Código por Observer (Replace Hard-Coded Notifications with Observer) | Observer (até, rumo a) | classes notificam receptores específicos em chamadas fixas no código | [replace-hard-coded-notifications-with-observer.md](references/generalization/replace-hard-coded-notifications-with-observer.md) |
| Unificar Interfaces com Adapter (Unify Interfaces with Adapter) | Adapter (até, rumo a) | os clientes usam duas classes do mesmo jeito, mas as interfaces delas diferem | [unify-interfaces-with-adapter.md](references/generalization/unify-interfaces-with-adapter.md) |
| Extrair Adapter (Extract Adapter) | Adapter (até) | uma classe adapta várias versões de um componente, biblioteca ou API | [extract-adapter.md](references/generalization/extract-adapter.md) |
| Substituir Linguagem Implícita por Interpreter (Replace Implicit Language with Interpreter) | Interpreter (até) | muitos métodos, ou combinações deles, expressam os elementos de uma linguagem implícita | [replace-implicit-language-with-interpreter.md](references/generalization/replace-implicit-language-with-interpreter.md) |

### Proteção (Kerievsky, cap. 9)

| Refatoração | Padrão | Quando | Arquivo |
|---|---|---|---|
| Substituir Código de Tipo por Classe (Replace Type Code with Class) | — | o tipo de um campo (uma string ou um int) não o protege de valores inválidos | [replace-type-code-with-class.md](references/protection/replace-type-code-with-class.md) |
| Limitar Instanciação com Singleton (Limit Instantiation with Singleton) | Singleton (até) | o código cria muitas instâncias de um objeto quando uma basta, e isso custa memória ou tempo | [limit-instantiation-with-singleton.md](references/protection/limit-instantiation-with-singleton.md) |
| Introduzir Null Object (Introduce Null Object) | Null Object (até) | a mesma verificação de campo ou variável nula se repete pelo código | [introduce-null-object.md](references/protection/introduce-null-object.md) |

### Acumulação (Kerievsky, cap. 10)

| Refatoração | Padrão | Quando | Arquivo |
|---|---|---|---|
| Mover Acumulação para Collecting Parameter (Move Accumulation to Collecting Parameter) | Collecting Parameter (até) | um método grande junta informação em uma variável local | [move-accumulation-to-collecting-parameter.md](references/accumulation/move-accumulation-to-collecting-parameter.md) |
| Mover Acumulação para Visitor (Move Accumulation to Visitor) | Visitor (até, rumo a); Iterator (longe) | um método junta informação de classes com interfaces diferentes | [move-accumulation-to-visitor.md](references/accumulation/move-accumulation-to-visitor.md) |

### Utilitários (Kerievsky, cap. 11)

| Refatoração | Padrão | Quando | Arquivo |
|---|---|---|---|
| Encadear Construtores (Chain Constructors) | — | vários construtores repetem o mesmo código | [chain-constructors.md](references/utilities/chain-constructors.md) |
| Unificar Interfaces (Unify Interfaces) | — | uma superclasse ou interface precisa da mesma interface de uma subclasse | [unify-interfaces.md](references/utilities/unify-interfaces.md) |
| Extrair Parâmetro (Extract Parameter) | — | um método ou construtor atribui a um campo um valor criado localmente | [extract-parameter.md](references/utilities/extract-parameter.md) |

## Padrões de destino

Os padrões estão na skill `gof-design-patterns`: intenção, quando compensa, participantes e exemplo
de cada um, e a tabela que liga cada padrão às refatorações que levam a ele. Kerievsky também
refatora para cinco padrões que não estão no GoF; os arquivos de referência dele os descrevem:

| Padrão | Refatorações de Kerievsky (direção) | Refatorações de Fowler (skill `fowler-refactoring`) |
|---|---|---|
| Creation Method | `replace-constructors-with-creation-methods` (até) | — |
| Factory | `move-creation-knowledge-to-factory` (até), `encapsulate-classes-with-factory` (até) | — |
| Composed Method | `compose-method` (até) | — |
| Collecting Parameter | `move-accumulation-to-collecting-parameter` (até) | — |
| Null Object | `introduce-null-object` (até) | `introduce-special-case` |

Fonte: Joshua Kerievsky, *Refactoring to Patterns*, Addison-Wesley (Pearson Education),
2004, e o catálogo online em https://www.industriallogic.com/refactoring-to-patterns/catalog/.
Parafraseado; veja o NOTICE do pacote.
