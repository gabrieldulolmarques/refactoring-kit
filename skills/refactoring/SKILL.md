---
name: refactoring
description: "Porta de entrada para refatorar um alvo (arquivo, pasta ou classe) do início ao fim: diagnostica com os cheques do SOLID, escolhe entre as skills fowler-refactoring, kerievsky-refactoring-to-patterns e gof-design-patterns, aplica uma refatoração por vez com build e testes e registra o ID da fonte. Use somente quando o usuário rodar /refactoring (Claude Code) ou $refactoring (Codex; pelo plugin, $refactoring-kit:refactoring), ou, no Claude Code, pedir esse fluxo completo; para uma refatoração ou um padrão específico, use direto a skill do catálogo."
---

# /refactoring <alvo> (no Codex, `$refactoring <alvo>`; pelo plugin, `$refactoring-kit:refactoring`)

O fluxo completo de refatoração. Esta skill só encaminha: o conteúdo está nas skills
`fowler-refactoring`, `kerievsky-refactoring-to-patterns` e `gof-design-patterns`, e o critério de
design, na rule `solid.md`. Se o pedido não trouxer um alvo, pergunte qual é.

1. **Diagnosticar.** Leia o alvo e nomeie os smells e os princípios do SOLID que ele viola, com
   arquivo e linhas (os cheques estão na rule `solid.md`, se estiver instalada). Se o subagente
   `refactoring-analyst` (no Codex, `refactoring_analyst`) existir, entregue o alvo a ele e use o plano que ele devolver.
2. **Escolher a fonte, uma por achado:**
   - uma refatoração simples resolve o smell: skill `fowler-refactoring`;
   - o smell pede um padrão (condicionais que escolhem variantes, notificações fixas no código,
     criação de objetos espalhada): skill `kerievsky-refactoring-to-patterns`, lendo antes o padrão
     na skill `gof-design-patterns`, quando ele for do GoF;
   - só há dúvida sobre um padrão: skill `gof-design-patterns`.
3. **Armar a rede de segurança.** Testes passando antes de começar. Se nada cobrir o código,
   escreva primeiro um teste que fixe o comportamento atual.
4. **Aplicar uma refatoração por vez**, pela mecânica do arquivo dela, com build e testes a cada
   passo. Se o subagente `refactoring-implementer` (no Codex, `refactoring_implementer`) existir, entregue cada item a ele.
5. **Registrar.** Um commit por refatoração, com o ID da refatoração
   no fim da descrição, `[F:<slug>]` ou `[K:<slug>]`, mais `[GoF:<padrão>]` e `[SOLID:<sigla>]` quando
   justificarem a mudança (a regra completa está em `rules/source-ids.md`, se instalada). Nunca faça push. Se o
   `refactoring-implementer` já commitou, esta etapa está cumprida.
6. **Conferir o resultado** com os mesmos cheques do SOLID (sem a rule, confira SRP, OCP, LSP, ISP e
   DIP pelo nome) e relatar o que mudou, os IDs usados e o
   que foi encontrado mas não tocado.

Pare assim que o smell sumir: ir *rumo a* um padrão muitas vezes basta.
