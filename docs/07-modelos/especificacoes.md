<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 5232–5704. -->

> **Nesta página:** Templates de requisitos, desenho técnico, tarefas, revisão e especificações específicas por história.

[← Voltar ao índice da documentação](../README.md)

---

## Apêndice B — Modelos das especificações por funcionalidade

Cada funcionalidade aprovada no backlog pode receber uma pasta própria de especificação. Os modelos desta seção descrevem o contrato de produto, o desenho técnico, o plano de tarefas e a revisão baseada em evidências.

### Templates das especificações por funcionalidade

#### `requisitos.md` — contrato de produto

```markdown
# FUNC-001 — Requisitos: [Nome da funcionalidade]

**Estado:** Rascunho
**Épico:** EP-001
**Histórias:** HIST-001
**Versão:** 0.1

## 1. Visão geral
[Qual necessidade resolve?]

## 2. Objetivos
- ...

## 3. Fora de escopo
- ...

## 4. Atores e permissões
| Ator | Pode fazer | Não pode fazer |
|---|---|---|
| ... | ... | ... |

## 5. Histórias relacionadas
- HIST-001

## 6. Requisitos funcionais
### RF-001 — [Título]
**Prioridade:** Must | Should | Could | Won't (nesta versão)
**Origem:** REQ-001 / HIST-001
**Regra:** WHEN [evento/condição], THE SYSTEM SHALL [comportamento verificável].
**Critério de aceitação:** ...

## 7. Requisitos não funcionais
### RNF-001 — [Qualidade]
**Condição:** ...
**Meta aprovada:** ...
**Medição/verificação:** ...

## 8. Regras de negócio
- RN-001: ...

## 9. Casos e exemplos
| Entrada/condição | Resultado esperado |
|---|---|
| ... | ... |

## 10. Escopo negativo
- ...

## 11. Restrições
- ...

## 12. Questões de implementação
- DUV-001: [Pergunta] — [Aberta/Respondida]

## 13. Métricas de sucesso
- ...

## 14. Riscos
- ...

## 15. Mapeamento de origem
| RF/RNF | Fonte | História | Critério |
|---|---|---|---|
| ... | ... | ... | ... |
```

Requisitos de qualidade sem metas quantificadas devem permanecer pendentes ou ser definidos em conjunto com as pessoas responsáveis. O agente pode sugerir valores, mas deve rotulá-los como propostas.

#### `desenho-tecnico.md` — contrato técnico

```markdown
# FUNC-001 — Desenho técnico: [Nome]

**Estado:** Rascunho
**Requisitos:** Aprovados

## 1. Resumo técnico
[Descrição da solução em 2–5 frases.]

## 2. Princípios e restrições aplicáveis
- ...

## 3. Mapeamento de requisitos
| Requisito | Solução | Componente/seção | Verificação |
|---|---|---|---|
| RF-001 | ... | ... | ... |

## 4. Contexto e componentes
[Diagrama Mermaid e responsabilidades.]

## 5. Fluxos de execução
[Sequência dos fluxos principais e alternativos.]

## 6. Contratos de API/eventos
| Método/evento | Rota/tópico | Entrada | Saída | Erros | Autorização |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

## 7. Dados e persistência
- Entidades/tabelas:
- Campos:
- Relacionamentos:
- Restrições/índices:
- Transações e consistência:
- Migração e reversão:

## 8. Segurança e privacidade
- Autenticação:
- Autorização:
- Validação:
- Proteção de dados:
- Auditoria:

## 9. Erros e casos extremos
| Situação | Comportamento | Código/estado | Registro/telemetria |
|---|---|---|---|
| ... | ... | ... | ... |

## 10. Estratégia de testes
| Requisito | Tipo de teste | Cenário | Evidência esperada |
|---|---|---|---|
| ... | ... | ... | ... |

## 11. Observabilidade e operação
...

## 12. Decisões técnicas
- DEC-001: ...

## 13. Alternativas e trade-offs
...

## 14. Riscos e mitigação
...

## 15. Questões em aberto
...
```

#### `tarefas.md` — plano de implementação

```markdown
# FUNC-001 — Tarefas: [Nome]

**Estado:** Rascunho
**Requisitos:** Aprovados
**Desenho:** Aprovado

## 1. Verificação de prontidão
- [ ] `requisitos:aprovados`
- [ ] `desenho:aprovado`
- [ ] Todos os RF Must estão cobertos
- [ ] Questões bloqueadoras resolvidas
- [ ] Dependências identificadas
- [ ] Critérios de aceitação testáveis
- [ ] Ambiente e ferramentas conhecidos

## 2. Cobertura
| Requisito | Tarefas | Evidência |
|---|---|---|
| RF-001 | TAR-001, TAR-002 | ... |

## 3. Tarefas
### TAR-001 — [Verbo + resultado]
**Tipo:** Implementação | Teste | Migração | Integração | Documentação | Pesquisa
**Requisito:** RF-001
**Prioridade:** Alta
**Estimativa:** [faixa] — validar com equipe
**Dependências:** Nenhuma | TAR-xxx
**Responsável:** A definir

**Objetivo:** ...

**Trabalho:**
- [ ] ...
- [ ] ...

**Critérios de aceitação:**
- ...

**Arquivos prováveis:**
- `caminho/arquivo.ext`

**Verificação:**
- Comando: `...`
- Resultado esperado: ...

**Riscos/notas:** ...

## 4. Ordem e dependências
[Lista ou diagrama.]

## 5. Pronto para execução?
- [ ] Sim, após aprovação humana
- [ ] Não, existem bloqueios: ...
```

#### `revisao.md` — relatório de evidências

```markdown
# Revisão — FUNC-001

**Revisor:** agente revisor em contexto independente
**Commit/diff:** [referência]
**Data:** [data]
**Estado:** Em revisão

## 1. Escopo revisado
- Requisitos:
- Desenho:
- Tarefas:
- Arquivos/diff:

## 2. Matriz de verificação
| Critério/requisito | Comando ou método | Código de saída | Resultado | Veredito |
|---|---|---:|---|---|
| RF-001 | `...` | 0 | ... | PASS/FAIL |

## 3. Achados
### ACH-001 — [Título]
**Severidade:** Bloqueadora | Alta | Média | Baixa
**Evidência:** ...
**Requisito afetado:** ...
**Impacto:** ...
**Correção recomendada:** ...

## 4. Testes executados
- ...

## 5. Verificações não executadas e limitações
- ...

## 6. Conclusão
- APROVADO | REPROVADO | APROVADO COM RESSALVAS
- Justificativa:

## 7. Pendências
- ...
```

#### Registro de perguntas e respostas

```markdown
# Dúvidas de implementação — FUNC-001

## DUV-001 — [Pergunta]
**Origem:** requisito/desenho/tarefa
**Impacto:** escopo | experiência | segurança | arquitetura | dados | prazo
**Estado:** Aberta | Respondida | Cancelada
**Alternativas:**
1. ... — impacto ...
2. ... — impacto ...

**Decisão humana:** ...
**Responsável:** ...
**Data:** ...
**Artefatos a atualizar:** ...
```

#### Checklist de mudança de requisito aprovado

```markdown
# Análise de impacto — [ID da mudança]

- [ ] Requisito original alterado identificado
- [ ] Histórias afetadas identificadas
- [ ] Épicos e funcionalidades afetados identificados
- [ ] Arquitetura/desenho afetados identificados
- [ ] Modelo de dados/migrações afetados identificados
- [ ] Tarefas e estimativas afetadas identificadas
- [ ] Testes e critérios de aceitação afetados identificados
- [ ] Issues e Project afetados identificados
- [ ] Plano de migração/reversão avaliado, se aplicável
- [ ] Aprovação humana registrada
```

---

### Templates específicos por história

Os arquivos abaixo são criados somente quando a história for uma unidade independente de especificação ou quando o detalhe não couber claramente na especificação compartilhada da funcionalidade. Os critérios de aceitação são obrigatórios; os demais documentos são condicionais.

#### `criterios-de-aceitacao.md`

```markdown
# HIST-001 — Critérios de aceitação: [Título]

**Épico:** EP-001
**Funcionalidade:** FUNC-001 (se aplicável)
**Requisitos de origem:** REQ-001, RF-001
**Estado:** Rascunho | Em revisão | Aprovado

## Resultado esperado
[O que o usuário deve conseguir fazer ou observar.]

## Casos normais
### CA-N-001 — [Fluxo principal]
**Dado** [contexto inicial]
**Quando** [ação]
**Então** [resultado verificável]

## Casos alternativos
### CA-A-001 — [Variação válida]
**Dado** ...
**Quando** ...
**Então** ...

## Casos extremos e falhas
### CA-E-001 — [Limite, entrada inválida ou falha]
**Dado** ...
**Quando** ...
**Então** ...

## Regras de negócio
- RN-001 — ...

## Permissões e segurança
- ...

## Dados envolvidos
- Entradas:
- Saídas:
- Dados persistidos:

## Fora de escopo
- ...

## Mapeamento para verificação
| Critério | Teste ou método | Evidência esperada |
|---|---|---|
| CA-N-001 | ... | ... |
```

#### `desenho-especifico.md` (opcional)

```markdown
# HIST-001 — Desenho específico: [Título]

## Contexto
[Referência à arquitetura e ao desenho da funcionalidade.]

## Componentes e responsabilidades
- ...

## Fluxo específico
1. ...

## Contratos
- API/eventos:
- Entradas/saídas:
- Erros:

## Decisões locais
- DEC-xxx — ...

## Estratégia de testes
- Casos normais:
- Casos extremos:

## Fora de escopo e riscos
- ...
```

#### `interface.md` (opcional)

```markdown
# HIST-001 — Interface: [Título]

## Telas e estados afetados
- ...

## Fluxo do usuário
1. ...

## Componentes e interações
- ...

## Estados
- Carregando:
- Vazio:
- Sucesso:
- Erro:

## Responsividade e acessibilidade
- ...

## Referências visuais
- [Links de protótipos ou design]
```

#### `alteracoes-de-dados.md` (opcional)

```markdown
# HIST-001 — Alterações de dados: [Título]

## Objetivo
- ...

## Alterações propostas
| Entidade/tabela | Alteração | Motivo | Compatibilidade |
|---|---|---|---|
| ... | ... | ... | ... |

## Integridade e relações
- Chaves:
- Restrições:
- Cascatas:
- Unicidade:

## Migração
- Estratégia:
- Ordem:
- Backfill:
- Reversão:

## Segurança e ciclo de vida
- Classificação:
- Retenção:
- Auditoria:

## Verificação
- Testes de migration:
- Testes de integridade:
- Evidências:
```

#### Template de proposta de consolidação

```markdown
# Consolidação — HIST-001 / FUNC-001

**Revisão da implementação:** [referência]
**Especificação aprovada:** [hash/commit]
**Estado:** Proposta | Em revisão | Aprovada | Sem atualização necessária

## Resultado da comparação
- Critérios atendidos:
- Divergências encontradas:
- Limitações:

## Decisões potencialmente reutilizáveis
| Decisão | Documento global de destino | Por que será útil novamente? |
|---|---|---|
| ... | `.ia/contexto/arquitetura.md` | ... |

## Alterações propostas
| Arquivo | Trecho/tema | Alteração | Impacto |
|---|---|---|---|
| ... | ... | ... | ... |

## Conteúdo que permanece específico da história
- ...

## Resultado
- [ ] Contexto global atualizado e validado
- [ ] Nenhuma atualização global necessária
- [ ] Divergência bloqueadora pendente

## Aprovação
- Responsável:
- Data:
- Commit/hash aprovado:
```
