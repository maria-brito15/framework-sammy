<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 4377–4955. -->

> **Nesta página:** Templates de diagnóstico, arquitetura, equipes, fases, rastreabilidade e artefatos de planejamento.

[← Voltar ao índice da documentação](../README.md)

---

## Apêndice A — Modelos dos documentos de planejamento

Os modelos abaixo são as referências completas para os documentos em `plano/` e para o contexto permanente em `.ia/contexto/`. Sammy seleciona, por meio do catálogo, a versão adequada ao perfil de rigor e à aplicabilidade de cada seção.

### Templates dos documentos e arquivos de contexto

Todos os templates devem existir uma única vez na biblioteca central `modelos/` e ser registrados em `modelos/catalogo.json`. Skills não devem manter cópias concorrentes dos templates. A skill seleciona o modelo adequado, aplica-o no destino, preenche apenas o que estiver sustentado pelas fontes e mantém campos pendentes visíveis.

#### `CLAUDE.md`

```markdown
# [Nome do projeto]

## Agente principal
- A sessão principal utiliza Sammy, definido em `.claude/agents/sammy.md`.
- A pessoa usuária conversa diretamente com Sammy; os demais agentes são especialistas delegados.
- Sammy coordena Skills, subagentes, validações e aprovações, respeitando os limites definidos neste arquivo.

## Idioma
- Comunicar e produzir documentos em português brasileiro.
- Preservar nomes oficiais de ferramentas, protocolos e tecnologias.

## Contexto obrigatório
- Antes de decisões de produto, ler `.ia/contexto/produto.md`.
- Antes de decisões técnicas, ler `.ia/contexto/arquitetura.md` e `.ia/contexto/principios.md`.
- Antes de planejar trabalho, ler `plano/.status` e os artefatos aprovados relevantes.

## Processo
- Este projeto usa Spec-Driven Development com aprovações humanas.
- Nunca interpretar a existência de arquivo como aprovação.
- Nunca implementar antes de `tarefas:aprovadas` na especificação da funcionalidade.
- Nunca promover estados para aprovado por iniciativa própria.
- Em conflito entre documentos, parar e solicitar resolução.

## Fonte de verdade
- Documentos aprovados no Git são a referência.
- GitHub Issues e Projects refletem o estado; não substituem os documentos.

## Comandos do projeto
- `/analisar-documentos`
- `/planejar-projeto`
- `/montar-backlog`
- `/validar-planejamento`
- `/publicar-no-github`
- `/ver-progresso`

## Roteamento
- Sammy é o agente principal e ponto único de contato.
- Processos repetíveis ficam em `.claude/skills/`.
- Especialistas ficam em `.claude/agents/`.
- Regras detalhadas ficam em `.claude/rules/`.
- Contexto duradouro fica em `.ia/contexto/`.
```

Manter esse arquivo curto. Se uma orientação puder viver em uma skill, regra ou contexto especializado, apontar para ela em vez de duplicá-la.

#### `.ia/contexto/produto.md`

```markdown
# Contexto do produto

## Identificação
- Nome:
- Versão:
- Responsável pelo produto:
- Última revisão:

## Visão
[O que é o produto em linguagem simples.]

## Problema
[Qual problema real pretende resolver?]

## Usuários e atores
| Ator/persona | Necessidades | Contexto de uso |
|---|---|---|
| ... | ... | ... |

## Objetivos
- ...

## Métricas de sucesso
| Métrica | Definição | Linha de base | Meta | Fonte |
|---|---|---|---|---|
| ... | ... | Desconhecida | Pendente | ... |

## Escopo do produto
- Incluído:
- Não incluído:

## Restrições conhecidas
- ...

## Fontes e decisões
- ...
```

#### `.ia/contexto/arquitetura.md`

```markdown
# Contexto arquitetural aprovado

## Estado
- Situação: Rascunho | Aprovado
- Referência: `plano/arquitetura.md`
- Commit de aprovação:

## Visão
[Resumo da arquitetura vigente.]

## Domínios e componentes
| Domínio/componente | Responsabilidade | Interfaces | Dependências |
|---|---|---|---|
| ... | ... | ... | ... |

## Tecnologias aprovadas
| Tecnologia | Uso | Versão/restrição | Justificativa | Fonte/DEC |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Restrições e princípios
- ...

## Decisões vigentes
- DEC-001: ...

## Pendências
- ...
```

#### `.ia/contexto/equipe.md`

```markdown
# Contexto da equipe

## Estrutura confirmada
| Equipe/frente | Responsável | Integrantes | Competências | Disponibilidade |
|---|---|---|---|---|
| ... | A definir | A definir | ... | Desconhecida |

## Papéis de decisão
| Decisão | Responsável por propor | Responsável por aprovar |
|---|---|---|
| Requisitos | ... | ... |
| Arquitetura | ... | ... |
| Prioridade | ... | ... |
| Liberação | ... | ... |

## Capacidade e restrições
- ...

## Observações
- Não preencher nomes ou disponibilidade por suposição.
```

#### `.ia/contexto/convencoes.md`

```markdown
# Convenções do projeto

## Idioma e documentação
- Idioma:
- Padrão de nomes:

## Código
- Organização de módulos:
- Nomenclatura:
- Tratamento de erros:
- Logs:

## APIs e integrações
- Versionamento:
- Formato de resposta:
- Autenticação/autorização:
- Timeouts e retries:

## Dados
- Convenção de tabelas e campos:
- Migrações:
- Transações:
- Auditoria e retenção:

## Testes
- Ferramentas:
- Tipos de teste:
- Comandos:

## Git e revisão
- Branches:
- Commits:
- Pull requests:
- Revisores:

## Regras de mudança
- Quando é obrigatório atualizar a especificação:
- Quando uma mudança pode usar processo leve:
```

#### `.ia/contexto/principios.md`

```markdown
# Princípios e restrições não negociáveis

## Princípios arquiteturais
- PR-001: [Regra expressa de forma verificável]
  - Motivo:
  - Consequência:
  - Exceções permitidas:

## Segurança
- ...

## Integridade de dados
- ...

## Qualidade e operação
- ...

## Limites de escopo
- ...

## Como alterar estes princípios
[Processo de proposta, revisão, aprovação e atualização de decisões afetadas.]
```

#### `plano/diagnostico.md`

```markdown
# Diagnóstico dos documentos de entrada

**Projeto:** [nome]
**Versão do diagnóstico:** [número]
**Estado:** Rascunho
**Fontes analisadas:** [lista]
**Data da análise:** [data]

## 1. Resumo executivo
...

## 2. Inventário das fontes
| Fonte | Tipo | Páginas/seções | Legibilidade | Limitações |
|---|---|---|---|---|
| ... | PDF | ... | Boa/Parcial/Ruim | ... |

## 3. Objetivos e problema
...

## 4. Atores e perfis
...

## 5. Requisitos identificados
| ID | Descrição fiel à fonte | Categoria | Prioridade encontrada | Origem |
|---|---|---|---|---|
| REQ-001 | ... | Funcional | Não informada | arquivo, página, seção |

## 6. Regras de negócio
...

## 7. Modelo de dados
| Entidade | Atributos relevantes | Relacionamentos | Restrições | Origem |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 8. Cruzamento requisito-dados
| Requisito | Entidades/atributos relacionados | Correspondência | Observação |
|---|---|---|---|
| ... | ... | Direta/Parcial/Ausente | ... |

## 9. Requisitos não funcionais e restrições
...

## 10. Contradições e lacunas
| ID | Tipo | Fontes envolvidas | Descrição | Impacto | Decisão necessária |
|---|---|---|---|---|---|
| DUV-001 | Contradição | ... | ... | ... | ... |

## 11. Fatos, inferências e propostas
- Fatos:
- Inferências:
- Propostas ainda não aprovadas:

## 12. Questões para a pessoa responsável
- DUV-001: ...

## 13. Limitações da análise
...

## 14. Recomendação de próximo passo
...
```

#### `plano/arquitetura.md`

```markdown
# Arquitetura proposta

**Versão:** 0.1
**Estado:** Rascunho
**Base:** `plano/diagnostico.md`

## 1. Resumo executivo
...

## 2. Objetivos e restrições arquiteturais
...

## 3. Requisitos arquiteturalmente significativos
| ID | Requisito | Razão de relevância | Estratégia |
|---|---|---|---|
| RNF-001 | ... | ... | ... |

## 4. Domínios e limites
| Domínio | Responsabilidade | Inclui | Não inclui | Interfaces |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 5. Visão de componentes
[Diagrama Mermaid e descrição dos componentes.]

## 6. Fluxos principais
[Diagramas de sequência/atividade quando agregarem valor.]

## 7. Dados
- Modelo conceitual:
- Persistência:
- Integridade:
- Migrações:
- Retenção e auditoria:

## 8. APIs e integrações
| Interface | Consumidor | Provedor | Contrato | Falhas/retries | Segurança |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

## 9. Segurança e privacidade
...

## 10. Requisitos não funcionais
| Requisito | Meta/limite aprovado | Estratégia | Como verificar |
|---|---|---|---|
| ... | Pendente | ... | ... |

## 11. Implantação e operação
...

## 12. Decisões arquiteturais
- DEC-001: ...

## 13. Alternativas e trade-offs
...

## 14. Mapeamento de requisitos para arquitetura
| Requisito | Componente/decisão | Seção | Cobertura |
|---|---|---|---|
| ... | ... | ... | Completa/Parcial/Pendente |

## 15. Riscos e questões em aberto
...
```

#### `plano/equipes.md`

```markdown
# Organização de equipes e responsabilidades

**Estado:** Rascunho

## 1. Premissas
...

## 2. Frentes propostas
| Equipe | Missão | Competências | Entregáveis | Dependências |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 3. Matriz RACI
| Entrega/decisão | Responsável pela execução (R) | Responsável final (A) | Consultado (C) | Informado (I) |
|---|---|---|---|---|
| Requisitos | ... | ... | ... | ... |

## 4. Matriz de competências
| Competência | Necessária? | Nível de profundidade | Equipe/frente | Situação |
|---|---|---|---|---|
| ... | Sim/Não/Pendente | ... | ... | Disponível/A contratar/A confirmar |

## 5. Interfaces entre equipes
...

## 6. Aprovações e escalonamento
...

## 7. Lacunas de capacidade
...
```

#### `plano/fases.md`

```markdown
# Fases e estratégia de entrega

**Estado:** Rascunho
**Datas:** Não comprometidas até validação de capacidade

## 1. Estratégia
...

## 2. Critérios de priorização
...

## 3. Fases
### Fase 1 — [Nome]
**Objetivo:** ...
**Valor esperado:** ...
**Entrada:** ...
**Entregáveis:** ...
**Épicos:** EP-001
**Funcionalidades:** FUNC-001, FUNC-002
**Equipes:** ...
**Dependências:** ...
**Riscos:** ...
**Critérios de saída:** ...
**Data/duração:** Pendente de capacidade validada

## 4. Dependências entre fases
[Diagrama Mermaid ou tabela.]

## 5. Marcos de validação
...

## 6. Caminho crítico (se identificável)
...

## 7. Premissas de calendário e capacidade
...
```

#### `plano/rastreabilidade.md`

```markdown
# Matriz de rastreabilidade

## Fontes para requisitos
| Fonte/página | REQ | RF/RNF | Observação |
|---|---|---|---|
| ... | REQ-001 | RF-001 | ... |

## Requisitos para histórias
| REQ/RF/RNF | HIST | Cobertura | Justificativa se não houver |
|---|---|---|---|
| ... | ... | Completa/Parcial | ... |

## Histórias para épicos e funcionalidades
| HIST | EP | FUNC | Cobertura/Observação |
|---|---|---|---|
| ... | ... | ... | ... |

## Funcionalidades para arquitetura e fases
| FUNC | Domínio/componente | DEC | Fase | Equipe |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Funcionalidades para especificações e tarefas
| FUNC | Requisitos da especificação | TAR | Verificação |
|---|---|---|---|
| ... | ... | ... | ... |

## Lacunas de cobertura
- ...
```

#### Modelo de registro de decisão (`DEC-xxx`)

```markdown
# DEC-001 — [Título da decisão]

**Estado:** Proposta | Aprovada | Rejeitada | Substituída
**Data:** [data]
**Responsável pela decisão:** [papel/pessoa]
**Contexto:** [problema e restrições]

## Decisão
[O que foi escolhido?]

## Justificativa
[Por que atende melhor aos objetivos?]

## Alternativas consideradas
| Alternativa | Vantagens | Desvantagens | Motivo da rejeição/seleção |
|---|---|---|---|
| ... | ... | ... | ... |

## Consequências
- Positivas:
- Negativas:
- Riscos:

## Artefatos afetados
- ...

## Evidência e aprovação
- Referência do commit:
- Aprovação:
```

---

#### Template de `.ia/contexto/definicao-de-concluido.md`

```markdown
# Definição de Concluído

**Escopo:** [todas as histórias / funcionalidades / tipo de entrega]
**Versão:** [versão]
**Aprovado por:** [responsável]

## Comportamento e aceitação
- [ ] Todos os critérios de aceitação aplicáveis foram atendidos.
- [ ] Casos normais e casos extremos relevantes foram verificados.
- [ ] Regras de negócio e permissões foram respeitadas.

## Qualidade técnica
- [ ] Código segue as convenções do projeto.
- [ ] Testes adequados foram criados ou atualizados.
- [ ] Lint, testes e build aplicáveis foram executados.
- [ ] Não foram introduzidas regressões conhecidas.

## Segurança, dados e acessibilidade
- [ ] Controles de autenticação e autorização foram verificados quando aplicáveis.
- [ ] Dados sensíveis foram tratados conforme as regras do projeto.
- [ ] Migrações, integridade e reversibilidade foram avaliadas quando aplicáveis.
- [ ] Acessibilidade e responsividade foram verificadas quando houver interface.

## Revisão e operação
- [ ] Revisão independente aprovada.
- [ ] Logs, métricas e tratamento de falhas foram considerados quando aplicáveis.
- [ ] Documentação e contratos relevantes foram atualizados.

## Consolidação
- [ ] Decisões duradouras foram avaliadas para atualização do contexto global.
- [ ] A consolidação foi aprovada (`consolidacao:aprovada`) ou registrada como não necessária (`consolidacao:sem-atualizacao`), com evidência.

## Evidências
| Critério | Comando/método | Resultado | Evidência |
|---|---|---|---|
| ... | ... | ... | ... |
```

#### Template de `.ia/contexto/dados.md`

```markdown
# Diretrizes globais de dados

## Escopo e fontes canônicas
- Modelo conceitual/físico:
- Schema ou migrations:
- Responsável pelo domínio:

## Persistência
- Banco(s) e finalidade:
- Estratégia de transações:
- Estratégia de concorrência e idempotência:

## Integridade
- Chaves e relacionamentos:
- Restrições e invariantes:
- Exclusão, cascata e retenção:
- Auditoria e histórico:

## Ciclo de vida e proteção
- Classificação de dados:
- Dados pessoais/sensíveis:
- Retenção e descarte:
- Backup e recuperação:

## Evolução
- Convenções de migrations:
- Compatibilidade entre versões:
- Plano de reversão:
