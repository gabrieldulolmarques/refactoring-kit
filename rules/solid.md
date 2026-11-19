# SOLID

Critério para julgar qualquer mudança de design, antes e depois de refatorar. Fonte: Martin (2002),
caps. 8–12; o SRP segue a versão revista de Martin (2017), cap. 7. Esta rule diz o que checar; o
como está nas skills `fowler-refactoring` e `kerievsky-refactoring-to-patterns`.

## Os princípios

**SRP: Princípio da Responsabilidade Única.** Um módulo deve responder a um único ator, isto é, a um
grupo de pessoas que pede o mesmo tipo de mudança (Martin, 2017, cap. 7). Na formulação de 2002, uma
classe deve ter um só motivo para mudar (Martin, 2002, cap. 8). Quando duas responsabilidades
dividem a mesma classe, uma mudança pedida por um ator pode quebrar o que o outro usa.

**OCP: Princípio Aberto-Fechado.** Classes, módulos e funções devem estar abertos para extensão e
fechados para modificação (Martin, 2002, cap. 9): um comportamento novo entra com código novo, sem
editar o que já funciona. O sinal de violação é a rigidez: uma mudança que se espalha em cascata por
módulos dependentes. O caminho é isolar o que varia atrás de uma abstração.

**LSP: Princípio da Substituição de Liskov.** Um subtipo deve poder substituir seu tipo base sem
que quem o usa perceba (Martin, 2002, cap. 10). A herança vale pelo comportamento, não pela
estrutura: uma subclasse que exige checagem de tipo, ignora um método ou lança exceção onde a base
não lança quebra o contrato, e o código cliente passa a depender das subclasses concretas.

**ISP: Princípio da Segregação de Interfaces.** Um cliente não deve ser obrigado a depender de
métodos que não usa (Martin, 2002, cap. 12). Uma interface grande acopla todos os seus clientes: a
mudança pedida por um deles obriga os outros a recompilar ou a se adaptar. O caminho é dar a cada
tipo de cliente a interface de que ele precisa.

**DIP: Princípio da Inversão de Dependência.** Módulos de alto nível não devem depender de módulos
de baixo nível; os dois devem depender de abstrações. E as abstrações não devem depender de
detalhes; os detalhes é que dependem delas (Martin, 2002, cap. 11). A regra de negócio define a
interface de que precisa, e a infraestrutura (rede, motor, arquivos) a implementa.

## Cheques

| Princípio | Cheque | Sinal de violação | Caminho |
|---|---|---|---|
| SRP | A classe responde a um só ator? | Pedidos de áreas diferentes mexem no mesmo arquivo; Divergent Change | `F:extract-class`, `F:split-phase`, `F:move-function` |
| OCP | Um caso novo entra sem editar o código existente? | `switch`/`if` sobre tipo que cresce a cada caso; Repeated Switches | `F:replace-conditional-with-polymorphism`, `K:replace-conditional-logic-with-strategy`, `K:replace-state-altering-conditionals-with-state` |
| LSP | Qualquer subclasse funciona onde a base é esperada? | Checagem de tipo antes de usar; override vazio ou que lança exceção; Refused Bequest | `F:replace-subclass-with-delegate`, `F:replace-superclass-with-delegate`, `F:push-down-method` |
| ISP | Cada cliente depende só do que usa? | Interface grande com métodos que alguns implementadores deixam vazios | Separar a interface por cliente; `F:extract-class`, `K:unify-interfaces-with-adapter` |
| DIP | A regra de alto nível depende de abstração? | Domínio chamando direto API, rede, arquivos ou engine; `new` de classe concreta | `K:extract-adapter`, `K:encapsulate-classes-with-factory`, `K:move-creation-knowledge-to-factory` |

`F:` é uma refatoração da skill `fowler-refactoring`; `K:`, da skill
`kerievsky-refactoring-to-patterns`.

## Regras

- Ao propor ou justificar uma mudança por um princípio, cite-o no plano e no commit (`SOLID:OCP`).
- Princípio não é meta: só refatore quando a violação causar um custo real (mudança frequente,
  bug, extensão difícil). Código estável que viola um princípio pode ficar.
- Se o caminho levar a um padrão, leia antes o padrão do GoF na skill `gof-design-patterns`.
