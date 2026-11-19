# refactoring-skill

Dois catálogos de refatoração e um catálogo de padrões de projeto empacotados como
[Agent Skills](https://agentskills.io) para agentes de código: o *Refactoring* de Martin Fowler (2ª ed.,
2018), o *Refactoring to Patterns* de Joshua Kerievsky (2004) e os 23 padrões do *Design Patterns* de
Gamma et al. (GoF, 1995). São três skills, uma por livro, para que se saiba de qual catálogo veio cada coisa
aplicada: `fowler-refactoring` relaciona 24 code smells às 66 refatorações que os corrigem,
`kerievsky-refactoring-to-patterns` relaciona 12 code smells às 27 refatorações para padrões, e
`gof-design-patterns` é a consulta aos 23 padrões, ligando os padrões às refatorações que levam a eles, quando há. Uma quarta, `refactoring`, é a porta de entrada: `/refactoring <alvo>` conduz o fluxo completo e encaminha para as outras três.
Todo arquivo de refatoração e de padrão tem um exemplo em C# 9.

**Site:** <https://gabrieldulolmarques.github.io/refactoring-skill/> (inglês e português).

**Vai usar?** Se estas skills ajudarem você em um projeto, um artigo ou uma postagem, por favor mencione:
coloque o link deste repositório e dê o crédito a Gabriel R. Marques
([gabrieldulolmarques](https://github.com/gabrieldulolmarques) no GitHub). Também gostaria de saber como
foi, então fique à vontade para abrir uma issue.

## Como as peças se encaixam

![Fluxo do princípio violado ao padrão de projeto: SOLID, smell, refatoração de Fowler, refatoração para padrão de Kerievsky e padrão do GoF](docs/flow.svg)

O desenho é editável: abra [`docs/flow.excalidraw`](docs/flow.excalidraw) em [excalidraw.com](https://excalidraw.com).

## Estrutura

```
.claude-plugin/plugin.json # transforma o pacote em um plugin do Claude Code
.codex-plugin/plugin.json # o mesmo para o Codex
.agents/plugins/marketplace.json # marketplace local, para `codex plugin marketplace add`
codex/agents/ # os dois subagentes em TOML, para o Codex (os de agents/ são do Claude Code)
LICENSE # CC BY 4.0
NOTICE # crédito a Fowler, Kerievsky, aos autores do GoF e à Addison-Wesley; o que a licença cobre
CATALOG.md # a especificação: 66 + 27 refatorações, 29 smells, 23 padrões, formato dos arquivos, nível de C#
agents/
├── refactoring-analyst.md # somente leitura: encontra smells e devolve um plano curto
└── refactoring-implementer.md # aplica uma refatoração, testando após cada passo
rules/
├── solid.md # SOLID como critério de design, com o caminho para as refatorações das duas skills
└── source-ids.md # IDs F:, K:, GoF: e SOLID: nos commits e planos, para rastrear a fonte de cada mudança
skills/refactoring/
└── SKILL.md # porta de entrada: /refactoring <alvo> diagnostica, escolhe a skill e aplica passo a passo
skills/fowler-refactoring/
├── SKILL.md # fluxo smell → refatoração → arquivo, índice dos 24 smells, tabelas das 66
└── references/ # smells.md, discipline.md, uma pasta por capítulo
skills/kerievsky-refactoring-to-patterns/
├── SKILL.md # fluxo smell → refatoração → arquivo, índice dos 12 smells, tabelas das 27
└── references/ # smells.md, discipline.md, uma pasta por capítulo
skills/gof-design-patterns/
├── SKILL.md # consulta: os 23 padrões e as refatorações que levam a cada um
└── references/ # catalog.md, principles.md, uma pasta por categoria
```

Só a descrição de cada skill fica no contexto do agente. O corpo é carregado quando a skill é
usada, e o arquivo de cada refatoração só quando o agente o abre. As refatorações de Kerievsky
apontam para as de Fowler que usam como passos, então instale as skills lado a lado.

## Agentes

Dois subagentes que usam as três skills:

- `refactoring-analyst` lê o código indicado na chamada, nomeia os smells e devolve um plano
  curto: onde, qual smell, qual refatoração, se há testes cobrindo e o risco. Nunca
  edita.
- `refactoring-implementer` aplica um item desse plano (ou uma refatoração nomeada), seguindo
  a mecânica com um build e uma execução dos testes após cada passo.

Revise o plano antes de entregar um item ao implementador. Os comandos de build e de teste
vêm da chamada ou das instruções do próprio projeto, não deste pacote.

## Como usar

- **Qualquer cliente de Agent Skills** (Claude Code, Codex, OpenCode): crie um link de cada pasta
  de `skills/` (`refactoring`, `fowler-refactoring`, `kerievsky-refactoring-to-patterns` e `gof-design-patterns`) na pasta de skills do
  projeto (no Windows, uma junção: `New-Item -ItemType Junction`).
- **Plugin do Claude Code**: `claude --plugin-dir <caminho-deste-repositório>`. As skills e os agentes
  ficam então com o prefixo `refactoring-kit:<name>`; o comando de entrada é `/refactoring-kit:refactoring`.

- **Plugin do Codex**: `codex plugin marketplace add <caminho-ou-owner/repo>` e instale o `refactoring-kit`
  pelo diretório de plugins do app. Traz as quatro skills; o roteador só roda quando chamado
  (`$refactoring <alvo>`).
- **Subagentes do Codex**: o Codex não lê os `agents/*.md` do Claude Code. Copie `codex/agents/*.toml`
  para `.codex/agents/` do projeto (ou `~/.codex/agents/`). O Codex não deixa um subagente ter
  sandbox próprio: o `refactoring_analyst` recebe a instrução de não editar, mas o sandbox é o da
  sessão.
- **Rules** (`rules/solid.md` e `rules/source-ids.md`): copie para a pasta de rules do projeto (no
  Claude Code, `.claude/rules/`) ou cite-as no `AGENTS.md`. Rules não fazem parte do formato Agent
  Skills nem de um plugin, então nenhuma das duas vias acima as instala.

Use uma só via por projeto, ou o Claude Code verá as skills duas vezes.

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

A licença cobre apenas o conteúdo próprio deste pacote, não os livros (veja [NOTICE](NOTICE)).
A motivação e a mecânica nas skills são parafraseadas, com o capítulo citado;
nada é copiado dos livros, de refactoring.com nem de industriallogic.com. Os nomes das refatorações, os nomes
antigos e as inversas vêm dos cabeçalhos de seção do livro e da edição web do livro para as cinco
refatorações só da web. Os exemplos em C# são originais.
