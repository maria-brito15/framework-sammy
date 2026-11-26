<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 6280–7096. -->

> **Nesta página:** Estados, aprovações, exceções, Skills operacionais, manifesto e configuração de automação.

[← Voltar ao índice da documentação](../README.md)

---

### Templates de estado, aprovação e skills operacionais

#### Modelo de `plano/.status`

O arquivo deve conter um único estado global atual. Exemplo de início de projeto:

```text
projeto:inicializado
documentos:recebidos
diagnostico:rascunho
planejamento:bloqueado
backlog:bloqueado
github:nao-publicado
```

Depois que a análise for concluída, o arquivo é atualizado para:

```text
projeto:inicializado
documentos:analisados
diagnostico:em-revisao
planejamento:bloqueado
backlog:bloqueado
github:nao-publicado
```

Após aprovação humana do diagnóstico:

```text
projeto:inicializado
documentos:analisados
diagnostico:aprovado
planejamento:rascunho
backlog:bloqueado
github:nao-publicado
```

Os estados acima são exemplos de transições. O validador deve definir uma máquina de estados permitida, impedir combinações contraditórias e rejeitar valores desconhecidos. Não permitir que o agente avance um estado porque “o documento parece completo”.

#### Modelo de `.status` por funcionalidade

Arquivo: `.ia/especificacoes/FUNC-001-nome/.status`

```text
funcionalidade:identificada
requisitos:rascunho
desenho:bloqueado
tarefas:bloqueadas
implementacao:bloqueada
revisao:bloqueada
```

Depois da aprovação humana dos requisitos:

```text
funcionalidade:identificada
requisitos:aprovados
desenho:rascunho
tarefas:bloqueadas
implementacao:bloqueada
revisao:bloqueada
```

Depois da aprovação humana do desenho:

```text
funcionalidade:identificada
requisitos:aprovados
desenho:aprovado
tarefas:rascunho
implementacao:bloqueada
revisao:bloqueada
```

Depois da aprovação humana das tarefas:

```text
funcionalidade:identificada
requisitos:aprovados
desenho:aprovado
tarefas:aprovadas
implementacao:pronta
revisao:bloqueada
```

O arquivo pode representar vários campos de estado, mas o parser deve validar o conjunto completo como uma única configuração coerente. Exemplo: `implementacao:pronta` é inválido se `tarefas:aprovadas` não estiver presente.

#### Histórico de aprovações

Arquivo sugerido: `plano/historico-aprovacoes.md`

```markdown
# Histórico de aprovações

## APR-001 — Aprovação do diagnóstico

- **Etapa:** Diagnóstico
- **Artefatos:** `plano/diagnostico.md`
- **Versão/commit revisado:** [hash]
- **Decisor:** [nome ou papel]
- **Data:** [data e horário]
- **Decisão:** Aprovado | Reprovado | Aprovado com ressalvas
- **Ressalvas:** ...
- **Pendências aceitas:** ...

## APR-002 — Aprovação do planejamento

- **Etapa:** Planejamento
- **Artefatos:** `plano/arquitetura.md`, `plano/equipes.md`, `plano/fases.md`
- **Versão/commit revisado:** [hash]
- **Decisor:** [nome ou papel]
- **Data:** [data e horário]
- **Decisão:** ...
- **Ressalvas:** ...
```

Não registrar aprovação apenas em texto de conversa. A ação deve estar ligada à versão exata dos documentos que foi revisada. A identidade e a forma de registro devem respeitar a política do repositório e da organização.

#### Registro de exceção de gate

Exceções não devem ser usadas para contornar o processo informalmente. Em uma emergência, registrar:

```markdown
## EXC-001 — [Nome da exceção]

**Gate afetado:** ...
**Solicitante:** ...
**Pessoa que autorizou:** ...
**Data:** ...

### Motivo da exceção
...

### Risco aceito
...

### Escopo permitido
[O que pode avançar apesar da exceção?]

### O que continua proibido
...

### Ação de regularização
- Responsável:
- Prazo:
- Evidência esperada:

### Encerramento da exceção
- Data:
- Resultado:
- Referência do registro:
```

#### Skill completa: `/analisar-documentos`

Arquivo: `.claude/skills/analisar-documentos/SKILL.md`

```markdown
---
name: analisar-documentos
description: Analisa documentos de requisitos, modelos de dados, diagramas e materiais de projeto. Use quando a pessoa solicitar a análise dos arquivos de entrada ou a criação/atualização do diagnóstico do projeto.
argument-hint: "[caminho opcional dos documentos]"
---

# Analisar documentos do projeto

## Objetivo
Gerar ou atualizar `plano/diagnostico.md` usando os documentos fornecidos como fontes primárias.

## Argumentos
- `$ARGUMENTS`: caminho de um ou mais documentos. Se vazio, usar `documentos/entrada/`.

## Pré-condições
- Confirmar que os arquivos de entrada existem e podem ser lidos.
- Ler `plano/.status`.
- Não sobrescrever diagnóstico aprovado sem solicitar revisão da mudança.

## Procedimento
1. Listar os documentos recebidos e identificar formato, páginas e limitações de leitura.
2. Extrair o conteúdo preservando referência ao arquivo e à página/seção.
3. Acionar `analista-de-documentos` para requisitos, atores, regras e restrições.
4. Acionar `analista-de-dados` para entidades, atributos, relacionamentos, chaves, cardinalidades e restrições.
5. Cruzar requisitos e modelo de dados sem presumir que cada entidade representa uma funcionalidade.
6. Classificar cada afirmação relevante como FATO, INFERÊNCIA, PROPOSTA ou QUESTÃO EM ABERTO.
7. Registrar requisitos, regras, restrições, lacunas e contradições com origem.
8. Se uma página estiver ilegível, declarar exatamente a limitação.
9. Criar `plano/diagnostico.md` usando o template oficial.
10. Executar a validação estrutural e solicitar auditoria semântica.
11. Atualizar o estado para `diagnostico:em-revisao`.
12. Apresentar um resumo e aguardar revisão humana.

## Restrições
- Não inventar regras de negócio, personas, tecnologias ou metas não presentes nas fontes.
- Não corrigir silenciosamente os documentos originais.
- Não escolher entre fontes contraditórias sem decisão humana.
- Não aprovar o diagnóstico.
- Não iniciar arquitetura antes da aprovação do diagnóstico.

## Critérios de conclusão
- [ ] Fontes inventariadas
- [ ] Referências de origem registradas
- [ ] Fatos e inferências separados
- [ ] Lacunas e contradições registradas
- [ ] Validação estrutural executada
- [ ] Diagnóstico salvo em revisão

## Resposta
Informar arquivos analisados, páginas com limitações, principais achados, dúvidas bloqueadoras e próxima etapa segura.
```

#### Skill completa: `/planejar-projeto`

Arquivo: `.claude/skills/planejar-projeto/SKILL.md`

```markdown
---
name: planejar-projeto
description: Cria ou atualiza a arquitetura, a organização de equipes e as fases de entrega com base em diagnóstico aprovado. Use quando a pessoa solicitar o planejamento geral de produto e engenharia.
argument-hint: "[escopo ou observação opcional]"
---

# Planejar projeto

## Objetivo
Produzir `plano/arquitetura.md`, `plano/equipes.md` e `plano/fases.md`.

## Pré-condições
- `plano/.status` deve indicar `diagnostico:aprovado`.
- Os documentos originais devem estar disponíveis para conferência.
- Ler os arquivos de contexto existentes.

## Procedimento
1. Ler diagnóstico, contexto do produto, princípios e arquitetura vigente.
2. Acionar `arquiteto-de-software` para elaborar a proposta arquitetural.
3. Solicitar mapeamento de requisitos arquiteturais para componentes e decisões.
4. Acionar `planejador-de-entregas` para propor frentes, competências, responsabilidades e fases.
5. Definir dependências entre domínios, componentes, equipes e entregas.
6. Distinguir decisões já tomadas de propostas ainda não aprovadas.
7. Não inventar stack, equipe disponível, pessoas, datas ou orçamento.
8. Gerar os três documentos usando seus templates.
9. Atualizar `plano/rastreabilidade.md` com os vínculos aplicáveis.
10. Acionar `auditor-de-planejamento` em contexto independente.
11. Corrigir apenas problemas estruturais que não alterem decisões humanas; devolver decisões pendentes para revisão.
12. Salvar os documentos como rascunho e definir `planejamento:em-revisao`.
13. Apresentar alternativas, trade-offs, riscos e questões que precisam de decisão.

## Restrições
- Não implementar código.
- Não aprovar os documentos.
- Não converter fases em sprints sem dados de cadência e capacidade.
- Não escolher arquitetura distribuída ou microserviços sem justificativa baseada em requisitos.
- Não esconder riscos ou questões abertas.

## Critérios de conclusão
- [ ] Arquitetura criada
- [ ] Equipes propostas sem inventar disponibilidade
- [ ] Fases com dependências e critérios de saída
- [ ] Mapeamento de requisitos incluído
- [ ] Auditoria executada
- [ ] Documentos salvos em revisão

## Resposta
Apresentar visão geral, decisões propostas, alternativas, fases, riscos, pendências e próxima etapa segura.
```

#### Skill completa: `/montar-backlog`

Arquivo: `.claude/skills/montar-backlog/SKILL.md`

```markdown
---
name: montar-backlog
description: Gera e organiza o backlog do projeto a partir de requisitos e planejamento aprovados. Cria histórias de usuário, agrupa em épicos e decompõe em funcionalidades. Use quando a pessoa solicitar a montagem ou revisão do backlog.
argument-hint: "[domínio ou parte do produto opcional]"
---

# Montar backlog

## Objetivo
Gerar `historias-de-usuario.md`, `epicos.md`, `funcionalidades.md` e atualizar `rastreabilidade.md`.

## Pré-condições
- Diagnóstico aprovado.
- Planejamento aprovado.
- Contexto do produto e arquitetura disponíveis.

## Procedimento
1. Ler requisitos, regras, atores, arquitetura, fases e restrições aprovadas.
2. Acionar `analista-de-produto` para identificar atores, objetivos, benefícios e histórias.
3. Aplicar INVEST a cada história; registrar itens que precisam de refinamento.
4. Escrever critérios de aceitação em cenários verificáveis, com Dado/Quando/Então quando apropriado.
5. Considerar fluxo principal, alternativas, erros, permissões e exceções pertinentes.
6. Acionar `especialista-em-backlog` para agrupar as histórias em épicos.
7. Para cada épico, escolher e justificar a técnica de decomposição mais adequada.
8. Decompor os épicos em funcionalidades apenas quando a camada acrescentar uma fronteira útil de produto/especificação.
9. Preferir fatias verticais de valor; manter tarefas técnicas por camada dentro do plano de implementação, não como histórias artificiais.
10. Registrar dependências, prioridade preliminar, fase proposta e equipe proposta sem inventar estimativas ou capacidade.
11. Atualizar a matriz de rastreabilidade.
12. Executar validações determinísticas.
13. Acionar `auditor-de-planejamento` em contexto independente.
14. Salvar como rascunho e definir `backlog:em-revisao`.
15. Apresentar duplicações, histórias grandes/vagas, decisões e pendências.

## Restrições
- Não criar história apenas para representar uma tabela, tela ou endpoint.
- Não usar estimativas geradas pelo agente como consenso da equipe.
- Não forçar a camada de funcionalidade se não agregar valor.
- Não publicar no GitHub nesta skill.
- Não aprovar o backlog.

## Critérios de conclusão
- [ ] Histórias derivadas das fontes
- [ ] INVEST avaliado
- [ ] Critérios verificáveis
- [ ] Épicos com valor e estratégia de decomposição
- [ ] Funcionalidades com fronteira e rastreabilidade
- [ ] Dependências identificadas
- [ ] Auditoria executada
- [ ] Backlog salvo em revisão

## Resposta
Informar quantidade de histórias, épicos e funcionalidades, itens que precisam de refinamento, cobertura de requisitos, riscos e próxima etapa segura.
```

#### Skill completa: `/consolidar-entrega`

Arquivo: `.claude/skills/consolidar-entrega/SKILL.md`

```markdown
---
name: consolidar-entrega
description: Compara uma entrega revisada com as especificações globais e propõe atualizações de decisões duradouras. Use após a revisão de uma história ou funcionalidade, antes de marcá-la como concluída.
argument-hint: "[HIST-xxx ou FUNC-xxx]"
---

# Consolidar entrega

## Pré-condições
- A implementação da unidade foi concluída.
- A revisão independente está aprovada.
- Os critérios de aceitação e evidências estão disponíveis.
- A Definição de Concluído foi consultada.

## Procedimento
1. Ler a especificação aprovada, o diff/commit e o relatório de revisão.
2. Ler os arquivos globais relacionados em `.ia/contexto/`.
3. Acionar `consolidador-de-especificacoes` em contexto separado.
4. Classificar cada decisão como local, reutilizável, provisória ou pendente.
5. Gerar proposta de consolidação com diff e justificativa.
6. Verificar links, consistência e ausência de duplicação.
7. Apresentar a proposta a Sammy.
8. Sammy solicita aprovação humana para mudanças semânticas nos documentos globais.
9. Aplicar somente as alterações aprovadas e executar os validadores.
10. Se não houver atualização global necessária, registrar `consolidacao:sem-atualizacao` com justificativa e evidências. Se houver mudanças semânticas aprovadas pela pessoa, registrar `consolidacao:aprovada`.
11. Permitir `concluida` somente quando a Definição de Concluído estiver satisfeita e o estado de consolidação for um dos dois resultados válidos.

## Restrições
- Não alterar código.
- Não sobrescrever mudanças humanas.
- Não promover uma decisão proposta a aprovada.
- Não marcar a unidade como concluída se houver divergência bloqueadora.

## Saída
- Resultado da comparação:
- Decisões reutilizáveis:
- Arquivos globais propostos:
- Atualizações aplicadas após aprovação:
- Validações:
- Pendências:
- Estado de consolidação:
```

#### Skills com efeitos externos ou aprovação explícita

Skills que aprovam estados, publicam Issues, alteram campos remotos ou executam tarefas com efeitos importantes devem ser configuradas para invocação humana explícita, por exemplo com a opção `disable-model-invocation: true` quando suportada pela versão atual do Claude Code.

Exemplo para `/publicar-no-github`:

```yaml
---
name: publicar-no-github
description: Publica no GitHub Issues e GitHub Projects um backlog já aprovado. Use somente quando a pessoa solicitar explicitamente a publicação.
argument-hint: "[--dry-run | --publicar]"
disable-model-invocation: true
---
```

Aplicar a mesma política a `/aprovar-planejamento`, `/aprovar-backlog`, `/aprovar-requisitos`, `/aprovar-desenho`, `/aprovar-tarefas` e, conforme a política de risco do repositório, `/executar-tarefa`. A opção impede a invocação automática pelo modelo; a skill ainda deve verificar autorização, estado e pré-condições antes de realizar a ação.

#### Contrato de scripts

Todo script determinístico deve documentar:

```markdown
# [Nome do script]

## Objetivo
...

## Entradas
- Arquivos:
- Argumentos:
- Variáveis de ambiente:

## Saídas
- Arquivos modificados:
- Relatório:
- Código de saída:

## Modos
- `--dry-run`: simular sem modificar arquivos ou serviços remotos.
- `--verbose`: detalhar decisões e operações, sem expor segredos.

## Segurança
- Não imprimir tokens, senhas ou dados sensíveis.
- Não executar operações destrutivas sem confirmação.
- Não sobrescrever artefatos aprovados sem apresentar diff.

## Idempotência
[Descrever como uma segunda execução se comporta.]

## Erros
[Lista de erros esperados e códigos de saída.]

## Testes
- ...
```

**Regra final:** as skills orquestram; os agentes analisam e produzem; scripts verificam propriedades determinísticas; Git mantém histórico e fonte canônica; GitHub Projects acompanha o estado; a pessoa responsável decide e aprova.
### Templates de configuração da automação

#### Skill de ativação explícita: `/hora-de-trabalhar`

Arquivo: `.claude/skills/hora-de-trabalhar/SKILL.md`

Esta é a porta de entrada padrão para a pessoa usuária. Ela não recebe uma tarefa como argumento: sua finalidade é ativar Sammy, reconhecer o estado do projeto e permitir que ele escolha o próximo procedimento adequado.

```markdown
---
name: hora-de-trabalhar
description: Ativa explicitamente Sammy no repositório atual. Reconhece o projeto, verifica o estado, identifica trabalho pendente e inicia a próxima atividade segura. Use quando a pessoa chamar Sammy para começar ou retomar o trabalho.
disable-model-invocation: true
---

# Sammy, hora de trabalhar

## Objetivo
Ativar Sammy sem exigir que a pessoa forneça um briefing ou escolha previamente uma etapa do workflow.

## Procedimento de ativação
1. Confirmar o repositório e o diretório de trabalho atuais.
2. Ler as instruções aplicáveis: `CLAUDE.md`, regras do projeto e configuração do framework.
3. Consultar estado, manifesto, grafo, hashes, aprovações, tarefas abertas e registros de integração.
4. Identificar documentos de entrada, documentos aprovados, mudanças locais e alterações desde a última execução.
5. Verificar a branch e o estado do Git; não descartar nem sobrescrever alterações humanas.
6. Executar a triagem adaptativa quando houver trabalho a realizar ou mudança relevante de contexto.
7. Determinar se o próximo passo é iniciar um projeto, continuar, reprocessar, especificar, implementar uma tarefa aprovada, revisar, sincronizar ou apenas apresentar o estado.
8. Acionar a Skill adequada e delegar aos especialistas necessários. Não pedir à pessoa que escolha agentes ou etapas.
9. Executar atividades locais seguras e independentes, respeitando gates, permissões e limites de autonomia.
10. Agrupar dúvidas bloqueadoras e continuar tarefas que não dependam delas.
11. Atualizar manifesto e relatório da execução.
12. Apresentar uma resposta concisa com resultado, trabalho iniciado/concluído, decisões necessárias e próxima etapa segura.

## Regras
- Não exigir argumentos nem uma descrição inicial da tarefa.
- Não iniciar automaticamente uma operação remota ou destrutiva.
- Não interpretar a ativação como aprovação de requisitos, desenho, tarefas ou publicação.
- Não inventar trabalho quando não houver pendências ou intenção inferível.
- Se o repositório não estiver configurado, identificar o que falta e preparar apenas a inicialização segura.
- A execução deve ser idempotente: uma nova ativação verifica o estado e não duplica trabalho.
- A Skill é invocada pela pessoa; não deve ser disparada automaticamente pelo modelo.

## Resposta inicial
Começar com uma confirmação breve, por exemplo: “À disposição. Vou reconhecer o estado do projeto e organizar a próxima atividade.” Em seguida, executar o reconhecimento; não parar na mensagem de confirmação.

## Critérios de conclusão da ativação
- O estado do projeto foi reconhecido ou as limitações de reconhecimento foram registradas.
- A próxima atividade foi identificada e iniciada quando autorizada.
- Bloqueios e decisões humanas foram consolidados.
- O manifesto e o relatório foram atualizados quando aplicável.
```

**Observação de implementação:** `disable-model-invocation: true` mantém a ativação sob controle explícito da pessoa. O nome da pasta da Skill cria o comando `/hora-de-trabalhar`. A pessoa precisa estar em uma sessão do Claude Code com Sammy selecionado como agente principal.

#### Skill de processamento amplo, acionada por Sammy: `/processar-projeto`

Arquivo: `.claude/skills/processar-projeto/SKILL.md`

```markdown
---
name: processar-projeto
description: Procedimento amplo de Sammy para conduzir o planejamento SDD de ponta a ponta quando a triagem indicar que essa execução é necessária. Detecta o estado do projeto, analisa fontes, seleciona rigor e modelos, coordena especialistas, gera artefatos e valida os resultados. Não é o comando de ativação cotidiana.
argument-hint: "[--somente-diagnostico | --sem-github | --perfil leve|padrao|rigoroso]"
---

# Processar projeto

## Objetivo
Permitir que Sammy conduza todas as etapas seguras e pendentes do projeto sem exigir que a pessoa invoque cada Skill especializada. Esta Skill é um procedimento interno de processamento amplo; a porta de entrada cotidiana é `/hora-de-trabalhar`.

## Procedimento de orquestração
1. Ler `configuracao-do-workflow.json`, `plano/.status` e `plano/controle/execucao.json`, se existirem.
2. Detectar o repositório, os arquivos de entrada, a estrutura existente e as mudanças desde a última execução.
3. Executar os scripts de descoberta e cálculo de hashes.
4. Determinar se a execução é inicial, continuação ou reprocessamento parcial.
5. Fazer triagem inicial; após a ingestão, reavaliar porte, rigor-base, autonomia, granularidade e confiança com evidências.
6. Para cada unidade de trabalho relevante, avaliar rigor e granularidade locais sem remover controles globais aplicáveis.
7. Aplicar o motor de políticas, identificar condições críticas/desconhecidas e registrar `triagem.md`, `triagem.json` e `estrategia-de-execucao.json`.
8. Consultar `modelos/catalogo.json` e escolher somente templates aplicáveis aos eixos e condições avaliados.
9. Selecionar especialistas pela necessidade real da atividade, não por uma lista fixa.
10. Construir o grafo de etapas pendentes e identificar tarefas independentes.
11. Sammy delega análises independentes a subagentes, sem permitir escrita concorrente no mesmo artefato.
12. Sammy consolida os resultados recebidos dos subagentes e gera documentos em rascunho.
13. Executar validadores determinísticos após cada conjunto de artefatos relacionado.
14. Acionar o auditor independente nas etapas de planejamento e backlog.
15. Corrigir falhas mecânicas e estruturais permitidas; repetir validação dentro do limite configurado.
16. Reavaliar a estratégia somente se surgir evento que altere materialmente risco, escopo, dependência ou evidência; registrar a nova decisão.
17. Se houver decisão bloqueadora, preparar um pacote agrupado de perguntas e continuar etapas independentes.
18. Atualizar manifesto, grafo, hashes, estados, estratégia e relatório de execução.
19. Quando atingir um gate humano, apresentar um pacote consolidado com diffs, decisões, riscos, pendências e opções.
20. Aceitar aprovação em linguagem natural somente quando a resposta identificar claramente o pacote/etapa aprovado; registrar a decisão vinculada aos hashes dos artefatos.
21. Após aprovação explícita, seguir para a próxima etapa automaticamente quando possível. Publicar no GitHub apenas se o backlog estiver aprovado e existir autorização persistente válida para o destino e as operações previstas.

## Regras
- Sammy é o único responsável pela comunicação com a pessoa usuária; subagentes retornam resultados a Sammy.
- Não pedir à pessoa para executar manualmente Skills internas.
- Não repetir etapa cuja entrada e saída não mudaram e cuja validação continua válida.
- Não assumir que informação ausente é informação negativa ou risco baixo.
- Não inventar regra de negócio, disponibilidade de equipe, estimativa comprometida ou data.
- Não aprovar artefatos.
- Não efetuar ações remotas destrutivas.
- Não esconder falhas parciais; registrar o que foi concluído e o que falta.
- Se uma etapa não puder avançar, executar as demais etapas independentes.

## Resultado
Apresentar um resumo único: concluído, aguardando decisão, bloqueado, pendente de autorização, arquivos alterados e próxima etapa segura.
```

#### Skill de retomada: `/continuar-projeto`

Arquivo: `.claude/skills/continuar-projeto/SKILL.md`

```markdown
---
name: continuar-projeto
description: Retoma a execução do projeto do último ponto seguro, detectando alterações, falhas parciais, aprovações e etapas ainda pendentes.
argument-hint: "[observação opcional]"
---

# Continuar projeto

1. Ler configuração, estado e manifesto.
2. Verificar hashes e aprovações vinculadas às versões dos artefatos.
3. Detectar operações locais/remotas concluídas ou parciais.
4. Calcular a primeira etapa segura do grafo.
5. Invalidar apenas saídas cuja entrada relevante mudou.
6. Não repetir publicação já confirmada.
7. Retomar automaticamente as etapas seguras.
8. Parar somente diante de um gate humano, conflito ou autorização ausente.
9. Atualizar manifesto e relatório.
```

#### Configuração do workflow

Arquivo: `configuracao-do-workflow.json`

```json
{
  "versao": 1,
  "idioma": "pt-BR",
  "modo": "autonomia-controlada",
  "agente_principal": {
    "nome": "sammy",
    "nome_exibicao": "Sammy",
    "papel": "orquestrador_de_engenharia",
    "ponto_unico_de_contato": true,
    "comando_de_inicializacao": "claude --agent sammy",
    "comando_de_ativacao": "hora-de-trabalhar",
    "comando_principal": "hora-de-trabalhar",
    "procedimento_de_processamento_amplo": "processar-projeto",
    "retomar_com": "continuar-projeto",
    "limite_de_agentes_simultaneos": 4,
    "rodadas_maximas_de_autocorrecao_semantica": 2
  },
  "triagem": {
    "habilitada": true,
    "modo": "automatico",
    "dimensoes_independentes": {
      "porte": ["pequeno", "medio", "grande"],
      "rigor": ["leve", "padrao", "rigoroso"],
      "autonomia": ["somente_rascunhos", "controlada", "ampliada"],
      "granularidade": ["projeto", "dominio_epico", "funcionalidade", "historia_tarefa"]
    },
    "pontuacao_risco": {
      "minimo": 0,
      "maximo": 14,
      "faixas": {
        "leve_maximo": 4,
        "padrao_maximo": 9,
        "rigoroso_minimo": 10
      },
      "desconhecido_nao_equivale_a_zero": true
    },
    "elevar_para_rigoroso_em_condicao_critica": true,
    "reavaliar_por_eventos": true,
    "reducao_exige_evidencia_estavel": true,
    "avaliacoes_estaveis_para_reducao": 2,
    "preservar_controles_globais": true
  },
  "fontes": {
    "diretorio": "documentos/entrada",
    "preservar_originais": true,
    "calcular_hashes": true,
    "cache_de_extracao": true
  },
  "aprovacoes": {
    "diagnostico": "humana",
    "arquitetura": "humana",
    "backlog": "humana",
    "requisitos_por_funcionalidade": "humana",
    "desenho_por_funcionalidade": "humana",
    "tarefas_por_funcionalidade": "humana"
  },
  "github": {
    "habilitado": false,
    "publicar_apos_aprovacao": false,
    "criar_project_automaticamente": false,
    "preservar_campos_manualmente_gerenciados": true,
    "modo_simulacao_por_padrao": true
  }
}
```

O arquivo contém padrões conservadores. O setup inicial pode descobrir o ambiente e propor valores, mas a habilitação de ações remotas deve ser explícita.

#### Catálogo de templates e regras de seleção

Arquivo: `modelos/catalogo.json`

```json
{
  "versao": 1,
  "templates": [
    {
      "id": "diagnostico-completo",
      "arquivo": "planejamento/diagnostico.md",
      "artefato": "diagnostico",
      "perfis": ["padrao", "rigoroso"],
      "condicoes": ["projeto_novo", "fontes_documentais"],
      "obrigatorio": true
    },
    {
      "id": "diagnostico-enxuto",
      "arquivo": "planejamento/diagnostico-enxuto.md",
      "artefato": "diagnostico",
      "perfis": ["leve"],
      "condicoes": ["escopo_pequeno", "baixo_risco"],
      "obrigatorio": true
    },
    {
      "id": "arquitetura-completa",
      "arquivo": "planejamento/arquitetura.md",
      "artefato": "arquitetura",
      "perfis": ["padrao", "rigoroso"],
      "condicoes": ["arquitetura_relevante"],
      "obrigatorio": true
    },
    {
      "id": "plano-de-riscos",
      "arquivo": "planejamento/riscos.md",
      "artefato": "riscos",
      "perfis": ["rigoroso"],
      "condicoes": ["condicao_critica", "alto_impacto_de_falha"],
      "obrigatorio": true
    },
    {
      "id": "historias-completas",
      "arquivo": "backlog/historias-de-usuario.md",
      "artefato": "historias",
      "perfis": ["padrao", "rigoroso"],
      "condicoes": ["backlog_de_produto"],
      "obrigatorio": true
    },
    {
      "id": "sprint-backlog",
      "arquivo": "gestao/planejamento-de-sprint.md",
      "artefato": "sprint",
      "perfis": ["padrao", "rigoroso"],
      "condicoes": ["equipe_confirmada", "capacidade_disponivel", "cadencia_definida"],
      "obrigatorio": false
    }
  ]
}
```

Este catálogo é ilustrativo. A implementação deve criar entradas para todos os templates existentes no repositório. Para dar suporte à triagem adaptativa, cada registro de template deve poder declarar também `portes`, `tipos_de_trabalho`, `rigor_minimo`, `aplicavel_quando`, `obrigatorio_quando_aplicavel`, `dependencias` e `validacoes`. A skill seleciona modelos por todos os eixos relevantes; não cria arquivos vazios nem inclui seções sem aplicabilidade. O catálogo deve possuir schema de validação para impedir caminhos inexistentes, perfis inválidos e condições desconhecidas.

Exemplo de registro expandido:

```json
{
  "id": "plano-migracao-dados",
  "arquivo": "especificacoes/migracao/alteracoes-de-dados.md",
  "artefato": "plano_migracao",
  "portes": ["pequeno", "medio", "grande"],
  "tipos_de_trabalho": ["migracao", "modernizacao"],
  "rigor_minimo": "rigoroso",
  "aplicavel_quando": ["persistencia_alterada", "risco_integridade_dados"],
  "obrigatorio_quando_aplicavel": true,
  "dependencias": ["diagnostico", "desenho_tecnico"],
  "validacoes": ["estrategia_reversao", "reconciliacao_dados", "integridade"]
}
```

O catálogo não toma decisões semânticas sozinho. Sammy decide se a condição se aplica com base nas evidências; o mecanismo determinístico valida se o template existe, se sua configuração é válida e se suas dependências foram atendidas.

#### Manifesto de execução

Arquivo: `plano/controle/execucao.json`

```json
{
  "versao_manifesto": 1,
  "execucao_atual": null,
  "modo": "autonomia-controlada",
  "fontes": [],
  "artefatos": [],
  "etapas": [],
  "aprovacoes": [],
  "integracao_github": {
    "estado": "desabilitada",
    "ultima_sincronizacao": null,
    "operacoes_pendentes": []
  }
}
```

O script deve atualizar este arquivo com os hashes, timestamps, etapas e resultados reais. O exemplo não representa uma execução realizada.

#### Registro estruturado de etapa

```json
{
  "id": "gerar-historias",
  "estado": "concluida",
  "entradas": ["plano/diagnostico.md", "plano/arquitetura.md"],
  "hashes_entrada": {},
  "saidas": ["plano/tarefas/historias-de-usuario.md"],
  "hashes_saida": {},
  "agentes": ["analista-de-produto"],
  "validacoes": ["ids-unicos", "referencias-de-origem"],
  "inicio": null,
  "fim": null,
  "observacoes": []
}
```

#### Template de resumo para aprovação consolidada

```markdown
# Revisão consolidada do projeto

**Projeto:** [nome]
**Perfil de rigor:** [Leve/Padrão/Rigoroso]
**Execução:** [ID]
**Resultado da auditoria:** [Aprovável/Aprovável com ressalvas/Não aprovável]

## O que foi produzido
- [ ] Diagnóstico
- [ ] Arquitetura
- [ ] Equipes
- [ ] Fases
- [ ] Histórias de usuário
- [ ] Épicos
- [ ] Funcionalidades
- [ ] Rastreabilidade

## Resumo do produto e da solução
[Resumo executivo]

## Decisões que precisam de aprovação
| ID | Decisão | Alternativas | Impacto | Recomendação |
|---|---|---|---|---|
| DEC-001 | ... | ... | ... | ... |

## Questões bloqueadoras
- ...

## Premissas não bloqueadoras
- ...

## Riscos relevantes
- ...

## Validação
- Requisitos cobertos:
- Histórias:
- Épicos:
- Funcionalidades:
- Referências inválidas:
- Dependências circulares:
- Falhas pendentes:

## Alterações automáticas realizadas
- ...

## Aprovação
- [ ] Aprovar diagnóstico
- [ ] Aprovar planejamento arquitetural
- [ ] Aprovar backlog
- [ ] Aprovar publicação no GitHub, se ainda não autorizada

**Observação:** cada aprovação fica vinculada aos hashes dos artefatos revisados.
```

---
