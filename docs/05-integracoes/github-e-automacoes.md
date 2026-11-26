<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 3454–3970. -->

> **Nesta página:** GitHub Issues, Projects, sincronização idempotente, integrações, hooks e automações.

[← Voltar ao índice da documentação](../README.md)

---

### GitHub Issues e GitHub Projects

A integração com GitHub transforma o backlog aprovado em itens acompanháveis, sem substituir os documentos versionados no repositório.

#### Fonte de verdade

- Git contém os documentos completos e aprovados.
- GitHub Issues representa os itens de trabalho que precisam de acompanhamento.
- GitHub Projects representa o estado e a organização visual do trabalho.
- O arquivo `plano/integracao-github/mapeamento.json` relaciona identificadores locais com Issues e itens do Project.

O Project é uma visão operacional; não deve conter a única cópia dos requisitos ou critérios de aceitação.

#### Nome do Project

**Gestão de Engenharia**

Descrição sugerida:

> Acompanhamento do planejamento, especificação, implementação e revisão das entregas do projeto. Os documentos versionados no repositório são a referência para requisitos, decisões e critérios de aceitação.

#### Hierarquia de Issues

Padrão inicial:

```text
Issue do épico: [EP-001] Gestão de usuários
  ├── Issue da funcionalidade: [FUNC-001] Cadastro de usuários
  ├── Issue da funcionalidade: [FUNC-002] Autenticação
  └── Issue da funcionalidade: [FUNC-003] Recuperação de acesso
```

Histórias de usuário permanecem, por padrão, nos arquivos Markdown e nas descrições das funcionalidades relacionadas. Só devem virar Issues individuais quando houver uma razão operacional para acompanhá-las separadamente.

A relação pai-filho de Issues depende dos recursos e permissões disponíveis no repositório/organização. Se não estiver disponível, o sincronizador deve preservar a relação por links e identificadores no corpo das Issues, sem fingir que a hierarquia nativa foi criada.

#### Labels

Labels recomendadas:

**Tipo**

```text
tipo:epico
tipo:funcionalidade
tipo:historia
```

**Área**

```text
area:produto
area:arquitetura
area:servidor
area:interface
area:dados
area:infraestrutura
area:qualidade
area:seguranca
```

**Prioridade**

```text
prioridade:critica
prioridade:alta
prioridade:media
prioridade:baixa
```

**Gestão SDD**

```text
sdd:gerenciado
sdd:aguardando-aprovacao
sdd:aprovado
sdd:bloqueado
```

As labels devem ser criadas apenas se ainda não existirem. O sincronizador não deve remover labels que tenham sido adicionadas manualmente sem antes apresentar o impacto.

#### Campos personalizados do Project

| Campo | Tipo | Opções ou exemplo |
|---|---|---|
| Situação | Seleção única | Backlog, Em análise, Em aprovação, Aprovado, Em desenvolvimento, Em revisão, Concluído, Bloqueado |
| Prioridade | Seleção única | Crítica, Alta, Média, Baixa |
| Tipo | Seleção única | Épico, Funcionalidade, História |
| Fase | Seleção única | Fase 1, Fase 2, Fase 3... |
| Equipe | Seleção única | Produto, Arquitetura, Servidor, Interface, Dados, Qualidade, Infraestrutura |
| Estimativa (horas) | Número | 8 |
| Especificação | Texto ou URL | Caminho ou link do documento |

Não duplicar campos que já existam como propriedades nativas de Issues ou Projects sem uma necessidade clara. Antes de criar campos, o script deve listar os campos existentes e verificar os limites e as permissões atuais do Project.

#### Visualizações

Criar as seguintes visualizações:

1. **Backlog — Tabela:** todos os épicos e funcionalidades, com tipo, prioridade, fase, equipe, estimativa e especificação.
2. **Fluxo SDD — Quadro:** agrupado pelo campo Situação, para visualizar o estado das entregas.
3. **Roadmap — Linha do tempo:** organizado por fase e datas, quando houver datas aprovadas.
4. **Fila de aprovação — Tabela ou quadro:** itens aguardando aprovação de requisitos, desenho, tarefas ou planejamento.
5. **Bloqueios — Tabela:** itens bloqueados, dependências pendentes e responsáveis, quando definidos.

#### Processo de sincronização

```text
Backlog aprovado
       |
       v
Executar sincronizador em modo de simulação
       |
       v
Mostrar plano de criação e atualização
       |
       v
Autorização humana
       |
       v
Verificar autenticação e permissões
       |
       v
Criar labels ausentes
       |
       v
Criar Issues dos épicos
       |
       v
Criar Issues das funcionalidades
       |
       v
Associar funcionalidades aos épicos
       |
       v
Adicionar Issues ao GitHub Project
       |
       v
Preencher campos personalizados
       |
       v
Salvar IDs e URLs no mapeamento local
       |
       v
Consultar GitHub e validar resultados
       |
       v
Marcar sincronização como concluída
```

#### Segurança e confiabilidade

O sincronizador deve:

- Ter opção `--dry-run` para simular as alterações.
- Ser idempotente: executar novamente não cria Issues duplicadas.
- Usar os identificadores `EP-xxx` e `FUNC-xxx` para localizar itens existentes.
- Manter um mapeamento de IDs, números e URLs retornados pelo GitHub.
- Não armazenar tokens ou credenciais no repositório.
- Verificar permissões antes de iniciar alterações.
- Solicitar o escopo de autorização necessário do GitHub CLI.
- Registrar erros parciais e permitir retomada segura.
- Detectar alterações feitas manualmente no GitHub.
- Não sobrescrever conflitos silenciosamente.
- Só informar sincronização completa após uma consulta de confirmação.

Exemplos de comandos do GitHub CLI (ajustar conforme repositório e versão instalados):

```bash
# Verificar autenticação
gh auth status

# Criar uma Issue de funcionalidade e adicioná-la ao Project
gh issue create \
  --title "[FUNC-001] Cadastro de usuários" \
  --body-file "temporarios/FUNC-001.md" \
  --label "tipo:funcionalidade" \
  --label "area:servidor" \
  --label "prioridade:alta" \
  --project "Gestão de Engenharia" \
  --type "Feature" \
  --parent 100

# Adicionar ao Project uma Issue que já existe
gh project item-add 3 \
  --owner ORGANIZACAO \
  --url "https://github.com/ORGANIZACAO/REPOSITORIO/issues/123"

# Criar um campo de seleção única
gh project field-create 3 \
  --owner ORGANIZACAO \
  --name "Prioridade" \
  --data-type SINGLE_SELECT \
  --single-select-options "Crítica,Alta,Média,Baixa"
```

Os números `3` e `100`, a organização, o repositório, o título do Project e os tipos de Issue são exemplos ilustrativos. O sincronizador deve descobrir ou receber os valores reais, nunca assumir esses exemplos como configuração.

A criação de Issues com `--project` e `--parent`, a adição posterior via `gh project item-add` e a criação de campos via `gh project field-create` são operações documentadas no GitHub CLI. A edição de campos de itens do Project deve usar `gh project item-edit` ou a API correspondente.

#### Sincronização dos gates com o Project

O Git permanece como fonte canônica do estado aprovado. Depois que uma mudança de `.status` for aprovada e integrada à branch principal, uma automação pode:

1. Identificar qual `.status` foi alterado.
2. Resolver a funcionalidade ou etapa pelo caminho do arquivo.
3. Consultar o mapeamento local para localizar a Issue.
4. Atualizar o campo Situação no Project.
5. Registrar o resultado da sincronização.

Uma alteração manual no campo Situação do Project não deve aprovar automaticamente um documento. O board reflete a aprovação; não a concede.
### Templates de integração com GitHub

#### Arquivo de configuração local `plano/integracao-github/configuracao.json`

```json
{
  "proprietario": "ORGANIZACAO_OU_USUARIO",
  "repositorio": "NOME_DO_REPOSITORIO",
  "projeto": {
    "numero": null,
    "nome": "Gestão de Engenharia"
  },
  "fonte_canonica": "git",
  "publicar_historias_como_issues": false,
  "criar_hierarquia_pai_filho": true,
  "modo_padrao": "simulacao",
  "campos": {
    "situacao": "Situação",
    "prioridade": "Prioridade",
    "tipo": "Tipo",
    "fase": "Fase",
    "equipe": "Equipe",
    "estimativa": "Estimativa (horas)",
    "especificacao": "Especificação"
  }
}
```

`numero: null` significa que o Project ainda deve ser localizado ou configurado. Não assumir que o projeto de número `3` ou qualquer outro exemplo existe.

#### Mapeamento `plano/integracao-github/mapeamento.json`

```json
{
  "versao": 1,
  "repositorio": "ORGANIZACAO/REPOSITORIO",
  "project_id": null,
  "atualizado_em": null,
  "itens": {
    "EP-001": {
      "tipo": "epico",
      "issue_number": null,
      "issue_node_id": null,
      "issue_url": null,
      "project_item_id": null,
      "hash_fonte": null,
      "ultima_sincronizacao": null
    },
    "FUNC-001": {
      "tipo": "funcionalidade",
      "epico": "EP-001",
      "issue_number": null,
      "issue_node_id": null,
      "issue_url": null,
      "project_item_id": null,
      "hash_fonte": null,
      "ultima_sincronizacao": null
    }
  }
}
```

O sincronizador deve gravar os identificadores reais retornados pelo GitHub. O exemplo não contém IDs reais.

#### Corpo de Issue de épico

```markdown
# EP-001 — [Nome do épico]

## Objetivo
[Problema/oportunidade e resultado esperado.]

## Valor de negócio
...

## Histórias relacionadas
- HIST-001 — [link para documento]

## Funcionalidades filhas
- FUNC-001 — [link para Issue/documento]

## Indicadores de sucesso
- ...

## Dependências e riscos
- ...

## Fonte canônica
`plano/tarefas/epicos.md` — seção EP-001

## Rastreabilidade
- Requisitos: REQ-001
- Fase: Fase 1
```

#### Corpo de Issue de funcionalidade

```markdown
# FUNC-001 — [Nome da funcionalidade]

## Objetivo
...

## Valor entregue
...

## Critérios de aceitação
- [ ] ...
- [ ] ...

## Histórias atendidas
- HIST-001

## Requisitos de origem
- REQ-001

## Épico
- EP-001

## Fase e equipe
- Fase: Fase 1
- Equipe: A definir

## Dependências
- ...

## Especificação
` .ia/especificacoes/FUNC-001-nome/ `

## Fonte canônica
`plano/tarefas/funcionalidades.md` — seção FUNC-001
```

#### Política de sincronização

- `--dry-run` é o modo padrão até a primeira publicação bem-sucedida.
- A publicação exige uma confirmação humana clara após exibir o plano de alterações.
- O identificador local é a chave idempotente; título não é suficiente.
- O script deve atualizar itens existentes quando o mapeamento for confiável, mas nunca sobrescrever alterações remotas divergentes sem apresentar diff.
- Se houver conflito entre o Git e o GitHub, interromper o item e registrar `conflito:pendente-de-resolucao`.
- A sincronização de estado do Project deve refletir aprovação já gravada no Git; nunca concedê-la.
- Falhas parciais devem ser retomáveis sem recriar itens já publicados.
### Sincronização inteligente e idempotente com GitHub

A sincronização deve funcionar como reconciliação de estado, não como criação cega de Issues.

#### Estratégia de reconciliação

Para cada `EP-xxx`, `FUNC-xxx` ou outro item gerenciado:

1. Procurar o identificador no `mapeamento.json`.
2. Se houver ID remoto, confirmar que a Issue existe e buscar seu estado atual.
3. Se não houver mapeamento, procurar o identificador nas Issues do repositório antes de criar.
4. Comparar o estado desejado no documento aprovado com o estado remoto.
5. Atualizar apenas campos pertencentes ao framework.
6. Preservar comentários, labels manuais, atribuições e metadados fora do controle do framework.
7. Detectar conflitos de edição e criar um relatório, em vez de sobrescrever silenciosamente.
8. Registrar cada operação e seu resultado.

#### Propriedade dos campos

Cada campo deve ter um proprietário definido:

| Campo/dado | Fonte canônica | Política |
|---|---|---|
| Título e descrição base da Issue | Documento aprovado | Sincronizar alterações aprovadas, preservando seções manuais separadas |
| IDs de rastreabilidade | Documentos no Git | Nunca alterar automaticamente IDs existentes |
| Labels `sdd:*` | Configuração do framework | Gerenciar de forma idempotente |
| Labels manuais | GitHub | Preservar |
| Situação do fluxo SDD | Estado aprovado no Git | Atualizar GitHub a partir do Git |
| Responsável | GitHub/equipe | Não substituir sem regra explícita |
| Estimativa comprometida | Equipe | Não substituir com estimativa gerada pelo agente |
| Comentários | GitHub | Não alterar |
| Campos customizados não gerenciados | GitHub | Preservar |

#### Operação transacional por etapas

A API do GitHub não deve ser tratada como uma transação única. O sincronizador deve:

- registrar o plano de operações antes de executá-las;
- aplicar alterações em lotes pequenos;
- guardar a resposta de cada operação;
- permitir retomar sem repetir ações concluídas;
- validar o estado final via consulta;
- marcar a sincronização como parcial quando houver falha;
- nunca registrar `github:sincronizado` se qualquer operação obrigatória estiver pendente.

#### Templates de publicação

A Issue deve conter um resumo útil e uma referência ao documento completo. Não duplicar toda a especificação no corpo da Issue.

```markdown
## Objetivo
[Resumo curto da entrega]

## Valor esperado
[Benefício para usuário/negócio]

## Escopo resumido
- ...

## Critérios de aceitação resumidos
- ...

## Rastreabilidade
- Épico: EP-001
- Histórias: HIST-001, HIST-002
- Requisitos: REQ-001, RF-001
- Funcionalidade: FUNC-001

## Dependências
- Bloqueada por: ...
- Bloqueia: ...

## Documentação canônica
- Caminho: `.ia/especificacoes/FUNC-001-nome/`
- Último commit aprovado: `...`

> O documento versionado no Git é a fonte completa e canônica.
```
### Automação e integrações

**Diretriz revisada:** Skills especializadas não devem transformar o uso do framework em uma sequência manual de comandos. Sammy decide qual Skill acionar e em que ordem, com base no estado, nas dependências, nos hashes e no perfil do projeto.

#### Componentes

| Componente | Responsabilidade |
|---|---|
| Claude Code Skills | Conduzir processos repetíveis |
| Subagentes | Executar tarefas especializadas em contextos separados |
| `CLAUDE.md` e regras | Definir comportamento e apontar para o contexto |
| Scripts Python | Extrair, validar e sincronizar dados de forma determinística |
| Git | Versionar fontes, planejamento, estados e especificações |
| GitHub CLI | Criar e editar Issues e Projects |
| GitHub GraphQL API | Operações de Project que não sejam cobertas adequadamente pelo CLI |
| GitHub Actions | Refletir mudanças aprovadas e executar verificações em eventos do repositório |
| Motor de orquestração | Controlar estado, dependências, retomada e reprocessamento seletivo |
| Manifesto de execução | Registrar hashes, etapas, artefatos, aprovações e operações parciais |
| Catálogo de templates | Selecionar modelos adequados ao tipo e risco do projeto |

#### Automação por eventos

Automatizações recomendadas, sob controle da política de execução:

- Ao integrar uma alteração aprovada de `.status`, atualizar o campo Situação no Project.
- Ao criar uma Issue com a label `sdd:gerenciado`, adicioná-la ao Project, se a regra estiver habilitada.
- Ao alterar uma especificação aprovada, executar validações de IDs e referências.
- Ao abrir um PR que modifica requisitos, desenho ou tarefas, executar o validador de rastreabilidade.
- Ao concluir uma tarefa, exigir evidência de testes ou uma justificativa explícita para verificação manual.

Nenhuma automação deve transformar um estado em aprovado apenas porque um PR foi criado, um arquivo foi salvo ou um teste passou.
### Automatização por hooks, Git e GitHub Actions

Automação por evento deve complementar a coordenação de Sammy e o ciclo iniciado por `/hora-de-trabalhar`. Ela não deve iniciar análises grandes a cada edição de arquivo.

#### Hooks locais do Claude Code

Usar hooks pequenos, rápidos e determinísticos:

| Evento | Automação | Limite |
|---|---|---|
| `SessionStart` | Ler resumo do estado, informar fontes alteradas e próxima etapa segura | Não iniciar pipeline completo silenciosamente |
| `PreToolUse` | Impedir escrita em arquivos de origem, alteração de gate ou publicação sem autorização | Não bloquear operações de leitura comuns |
| `PostToolUse` após edição | Executar verificações rápidas de Markdown, IDs ou schema nos arquivos afetados | Não rodar auditoria semântica completa em cada edição |
| `Stop` | Verificar se a tarefa declarou conclusão sem executar a validação obrigatória | Limitar escopo e evitar ciclos infinitos |

Hooks executam comandos com permissões do ambiente em que o Claude Code está rodando. Por isso, devem ser revisados, restritos a scripts do próprio repositório e não devem executar comandos arbitrários provenientes de documentos externos. Não usar `--dangerously-skip-permissions` como atalho para automatização.

#### Git hooks e CI

- `pre-commit`: verificar formatação, links locais, IDs e schemas alterados.
- `pre-push` (opcional): validar consistência do conjunto de documentos afetados.
- Pull request: executar validação de rastreabilidade, detectar mudanças em artefatos aprovados e produzir relatório.
- Merge na branch principal: atualizar estados no Project quando houver aprovação registrada e hash correspondente.
- Mudança de fonte original: sinalizar artefatos potencialmente desatualizados.

Não executar uma chamada de LLM em cada hook local. Deixar a avaliação semântica para as Skills e os agentes e a validação determinística para scripts e CI.

#### GitHub Projects

Utilizar primeiro as automações nativas do GitHub Projects e complementar com GitHub Actions/GraphQL somente quando necessário:

- Adicionar automaticamente Issues com a label `sdd:gerenciado`, se essa regra estiver configurada.
- Alterar situação para concluído quando a Issue for fechada, se essa semântica corresponder ao processo.
- Atualizar campos quando um estado aprovado for integrado ao Git.
- Arquivar itens concluídos conforme política do projeto.
- Adicionar pull requests ao Project e acompanhar revisão.

O GitHub documenta automações nativas, GraphQL e GitHub Actions para esses fluxos: [Automatizar um Project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project), [melhores práticas de Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects) e [automações nativas](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations).

#### Descoberta automática do ambiente GitHub

Antes de perguntar dados que podem ser descobertos:

1. Detectar o repositório pelo `git remote`.
2. Verificar autenticação com `gh auth status`.
3. Identificar organização/proprietário e repositório.
4. Listar Projects acessíveis e identificar se já existe um Project associado.
5. Inspecionar labels, Issue Types e campos existentes.
6. Reutilizar configurações existentes em vez de duplicá-las.
7. Perguntar apenas quando houver mais de um destino plausível ou permissão insuficiente.

A partir de junho de 2026, o GitHub CLI oferece operações para tipos de Issue, hierarquia pai/filho e dependências em versões recentes. O sincronizador deve detectar a versão instalada e os recursos disponíveis antes de escolher o caminho de execução. Referência: [GitHub Changelog — CLI para sub-issues, tipos e dependências](https://github.blog/changelog/2026-06-10-manage-sub-issues-types-and-dependencies-from-github-cli/).

---
