# refactoring-kit

Os catálogos de refatoração de Martin Fowler e de Joshua Kerievsky e os 23 padrões do GoF, empacotados
como [Agent Skills](https://agentskills.io) para agentes de código (Claude Code e Codex). O
pacote traz também dois subagentes, duas rules e um exemplo em C# 9 em cada arquivo de refatoração e de
padrão. O repositório se chama `refactoring-skill`; o plugin, `refactoring-kit`.

**Site:** <https://gabrieldulolmarques.github.io/refactoring-skill/> (inglês e português).

**Vai usar?** Se estas skills ajudarem você em um projeto, um artigo ou uma postagem, por favor mencione:
coloque o link deste repositório e dê o crédito a Gabriel R. Marques
([gabrieldulolmarques](https://github.com/gabrieldulolmarques) no GitHub). Também gostaria de saber como
foi, então fique à vontade para abrir uma issue.

## O que tem

Uma skill por livro, para saber de qual catálogo veio cada coisa aplicada, mais uma de entrada:

| Skill | Fonte | O que traz | ID |
|---|---|---|---|
| `refactoring` | | A porta de entrada: `/refactoring <alvo>` (no Codex, `$refactoring <alvo>`; pelo plugin, `$refactoring-kit:refactoring <alvo>`) diagnostica, escolhe a skill e aplica passo a passo | |
| `fowler-refactoring` | Fowler (2018) | 24 code smells e 66 refatorações | `F:<slug>` |
| `kerievsky-refactoring-to-patterns` | Kerievsky (2004) | 12 code smells e 27 refatorações que levam a um padrão, rumo a ele ou para longe dele | `K:<slug>` |
| `gof-design-patterns` | Gamma et al. (1995) | Consulta aos 23 padrões, cada um ligado às refatorações que levam a ele, quando há | `GoF:<padrão>` |

Cada refatoração tem quando usar, mecânica passo a passo, exemplo em C# 9 e uma lista de verificação.
Cada padrão tem intenção, quando compensa, participantes, exemplo e riscos. As fontes são citadas por
capítulo e nome da entrada, nunca por página.

## Como as peças se encaixam

![Fluxo do princípio violado ao padrão de projeto: SOLID, smell, refatoração de Fowler, refatoração para padrão de Kerievsky e padrão do GoF](docs/flow.svg)

Um princípio do SOLID violado aponta para um smell, o smell para uma refatoração de Fowler e, se
compensar, para uma refatoração de Kerievsky que termina num padrão do GoF. O desenho é editável: abra
[`docs/flow.excalidraw`](docs/flow.excalidraw) em [excalidraw.com](https://excalidraw.com).

## Agentes e rules

- `refactoring-analyst` lê o código indicado, nomeia os smells e devolve um plano curto: onde, qual
  smell, qual refatoração, se há testes cobrindo e o risco. Nunca edita.
- `refactoring-implementer` aplica um item do plano (ou uma refatoração nomeada), seguindo a mecânica
  com um build e uma execução dos testes após cada passo. Faz um commit por refatoração, com o ID da
  fonte no fim da descrição, e nunca faz push. Os comandos de build e de teste vêm da chamada ou das
  instruções do projeto, não deste pacote.
- `rules/solid.md` traz os cheques do SOLID, com o caminho de cada princípio até as refatorações.
- `rules/source-ids.md` define os IDs `F:`, `K:`, `GoF:` e `SOLID:` nos commits, planos e relatórios, por
  exemplo `♻️ refactor(billing): replace payment type switch with strategy [SOLID:OCP] [F:replace-conditional-with-polymorphism]`.
  Com eles, `git log --grep "\[F:"` conta o uso de cada fonte.

Revise o plano do analista antes de entregar um item ao implementador.

## Instalação

- **Claude Code, como plugin:** `claude --plugin-dir <caminho-deste-repositório>`. As skills e os
  agentes ganham o prefixo `refactoring-kit:`, e a entrada é `/refactoring-kit:refactoring`.
- **Codex, como plugin:** `codex plugin marketplace add <caminho-ou-owner/repo>` e depois
  `codex plugin add refactoring-kit@refactoring-kit`. O roteador só roda quando chamado, e o plugin dá um prefixo ao nome: use
  `$refactoring-kit:refactoring`. Os subagentes não vêm no plugin: copie `codex/agents/*.toml` para `.codex/agents/` do
  projeto (ou `~/.codex/agents/`). O Codex não dá sandbox próprio ao subagente: o `refactoring_analyst`
  recebe a instrução de não editar, mas usa o sandbox da sessão.
- **Qualquer cliente de Agent Skills:** crie um link de cada pasta de `skills/` na pasta de skills do
  projeto (`.agents/skills/` para o Codex, `.claude/skills/` para o Claude Code). No Windows, use uma
  junção (`New-Item -ItemType Junction`). Instale as quatro lado a lado: as refatorações de Kerievsky
  apontam para as de Fowler.
- **Rules:** copie `rules/*.md` para `.claude/rules/` ou cite-as no `AGENTS.md`. Plugins e skills não
  instalam rules.

Use uma só via por projeto, ou o Claude Code verá as skills duas vezes.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `skills/` | As quatro skills. O `SKILL.md` do `refactoring` encaminha às outras; os dos dois catálogos de refatoração levam do smell à refatoração e ao arquivo; o do GoF indexa os padrões. `references/` tem um arquivo por entrada |
| `agents/` | Os dois subagentes do Claude Code (`.md`) |
| `codex/agents/` | Os mesmos subagentes em TOML, para o Codex |
| `rules/` | `solid.md` e `source-ids.md` |
| `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/` | Manifestos dos plugins e a marketplace local do Codex |
| `docs/` | O diagrama (`flow.svg` e `flow.excalidraw`) |
| `CATALOG.md` | A especificação: as 66 + 27 refatorações, os 24 + 12 smells, os 23 padrões, o formato dos arquivos e o nível de C# |
| `LICENSE`, `NOTICE` | CC BY 4.0; crédito a Fowler, Kerievsky, aos autores do GoF e à Addison-Wesley, e o que a licença cobre |

Só a descrição de cada skill fica no contexto do agente. O corpo é carregado quando a skill é usada, e
o arquivo de cada refatoração só quando o agente o abre. Nos subagentes do Claude Code, o `SKILL.md` das três
skills de catálogo é pré-carregado.

## Licença e crédito

[CC BY 4.0](LICENSE): livre para compartilhar e adaptar para qualquer finalidade, desde que você dê crédito a este
pacote **e** aos livros em que ele se baseia:

> Martin Fowler. *Refactoring: Improving the Design of Existing Code*. 2nd ed. Boston:
> Addison-Wesley (Pearson Education), 2018. ISBN 978-0-13-475759-9.
>
> Joshua Kerievsky. *Refactoring to Patterns*. Boston: Addison-Wesley (Pearson Education),
> 2004. ISBN 978-0-321-21335-8.
>
> Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides. *Design Patterns: Elements of
> Reusable Object-Oriented Software*. Reading: Addison-Wesley, 1995. ISBN 978-0-201-63361-0.
>
> Robert C. Martin. *Agile Software Development: Principles, Patterns, and Practices*. Prentice Hall,
> 2002. ISBN 978-0-13-597444-5.
>
> Robert C. Martin. *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Pearson,
> 2017. ISBN 978-0-13-449416-6.

A licença cobre apenas o conteúdo próprio deste pacote, não os livros (veja [NOTICE](NOTICE)).
A motivação e a mecânica nas skills são parafraseadas, com o capítulo citado;
nada é copiado dos livros, de refactoring.com nem de industriallogic.com. Os nomes das refatorações, os nomes
antigos e as inversas vêm dos cabeçalhos de seção do livro e da edição web do livro para as cinco
refatorações só da web. Os exemplos em C# são originais.
