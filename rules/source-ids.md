# IDs de fonte

Como identificar de qual catálogo veio cada refatoração, padrão ou princípio aplicado, para rastrear
o uso de cada fonte e medi-lo depois. Vale para planos, mensagens de commit e relatórios dos agentes.

| ID | Fonte | Exemplo |
|---|---|---|
| `F:<slug>` | refatoração da skill `fowler-refactoring` | `[F:extract-function]` |
| `K:<slug>` | refatoração da skill `kerievsky-refactoring-to-patterns` | `[K:replace-conditional-logic-with-strategy]` |
| `GoF:<padrão>` | padrão da skill `gof-design-patterns` (Gamma et al., 1995) | `[GoF:strategy]` |
| `SOLID:<sigla>` | princípio da rule `solid.md` | `[SOLID:OCP]` |

O slug é o nome do arquivo de referência sem `.md`; o padrão do GoF vai em minúsculas e com hífen
(`abstract-factory`).

## Regras

- No commit, o ID vai no fim da descrição, entre colchetes, na mesma linha; vários IDs ficam
  separados por espaço. Os colchetes não contam como descrição, então `SOLID:OCP` pode ter
  maiúsculas:
  `♻️ refactor(billing): replace payment type switch with strategy [SOLID:OCP] [F:replace-conditional-with-polymorphism]`
- Um commit por refatoração, então cada commit tem um só ID `F:` ou `K:`. `SOLID:` e `GoF:`
  acompanham quando justificam a mudança.
- Commit que não aplica nada dos catálogos (docs, configuração) não leva ID.
- Nos planos e nos relatórios dos agentes, a coluna da refatoração traz o mesmo ID.
- Para contar o uso de uma fonte: `git rev-list --count --grep='\[F:' HEAD` (ou `\[K:`, `\[GoF:`, `\[SOLID:`).
