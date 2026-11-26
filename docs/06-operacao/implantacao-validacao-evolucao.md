<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 3971–4376. -->

> **Nesta página:** Instalação, desenvolvimento do framework, projetos-piloto, critérios de sucesso e decisões arquiteturais.

[← Voltar ao índice da documentação](../README.md)

---

## Parte V — Implantação, validação e evolução

A última parte do corpo principal explica como construir o framework em incrementos, como avaliá-lo com projetos-piloto e como medir se a automação realmente reduziu trabalho sem enfraquecer a qualidade.

### Instalar e testar Sammy em um repositório-laboratório

A primeira validação deve ocorrer em um repositório de teste, separado do repositório do framework e de qualquer produto importante. Isso permite ajustar prompts, permissões, Skills e scripts sem colocar código ou documentos reais em risco.

#### Separar framework e projeto de teste

Recomenda-se manter dois repositórios:

| Repositório | Conteúdo |
|---|---|
| `framework-sdd` | Sammy, subagentes, Skills, regras, templates, scripts, configurações e avaliações do framework. |
| `projeto-laboratorio` | Documentos fictícios ou sanitizados, código de teste, planejamento gerado, estados e resultados dos pilotos. |

Durante a primeira versão, o caminho mais simples é copiar para `projeto-laboratorio` os componentes necessários de `framework-sdd`: `.claude/`, `CLAUDE.md`, `modelos/`, `scripts/` e `configuracao-do-workflow.json`. Depois de estabilizar o framework, essa distribuição pode ser empacotada como plugin do Claude Code ou automatizada por um instalador versionado.

#### Inicialização

1. Criar um repositório vazio chamado `projeto-laboratorio`.
2. Copiar os componentes do framework para a raiz do projeto.
3. Criar `documentos/entrada/` e adicionar `requisitos.pdf` e `modelo-de-dados.pdf` de teste.
4. Verificar se `.claude/agents/sammy.md`, as Skills e os templates estão presentes.
5. Confirmar que `.claude/settings.json` contém `"agent": "sammy"`.
6. Iniciar Claude Code na raiz do repositório. Alternativamente, executar `claude --agent sammy` para selecionar Sammy explicitamente naquela sessão.
7. Executar `/hora-de-trabalhar`. Não é necessário fornecer uma instrução inicial: Sammy reconhece o estado e escolhe a próxima atividade.
8. Confirmar que a Skill de ativação aparece no menu `/` e que seu frontmatter contém `disable-model-invocation: true`.

Primeira ativação:

```text
/hora-de-trabalhar
```

Com Sammy configurado como agente principal, esse comando é suficiente para iniciar o reconhecimento do projeto. Em um repositório-laboratório, mantenha GitHub e operações de escrita remota desabilitados. Sammy deve identificar os documentos, preparar os rascunhos e solicitar decisões apenas quando necessário, sem implementar código ou publicar nada remotamente sem autorização.

#### Casos mínimos de teste

| Caso | Preparação | Comportamento esperado de Sammy |
|---|---|---|
| Projeto novo e completo | Requisitos e modelo de dados coerentes | Delegar análises, consolidar diagnóstico, gerar planejamento e backlog e apresentar gates. |
| Requisitos vagos | Remover regras ou critérios de aceitação de propósito | Identificar ambiguidades, continuar partes independentes e perguntar somente o que altera decisões relevantes. |
| Modelo de dados inconsistente | Criar relacionamento contraditório ou entidade sem origem clara | Apontar a divergência com referência à fonte, sem inventar correção. |
| Projeto existente | Adicionar código, testes e migrações ao laboratório | Acionar analista de repositório e distinguir estado atual da intenção documentada. |
| Alteração incremental | Modificar apenas um requisito ou entidade | Detectar os hashes alterados e reprocessar somente os artefatos dependentes. |
| Reexecução idempotente | Executar novamente sem alterar entradas | Não duplicar arquivos, IDs, Issues ou relações. |
| GitHub sem autorização | Configurar destino, mas não conceder autorização de publicação | Preparar `--dry-run` e aguardar autorização antes de qualquer efeito remoto. |

#### Critérios para considerar Sammy pronto para uso

- A sessão inicia como Sammy por configuração ou argumento `--agent`.
- A pessoa consegue ativar Sammy com `/hora-de-trabalhar` sem escrever um briefing inicial.
- A ativação faz Sammy reconhecer o estado do projeto antes de escolher o procedimento.
- Se não houver contexto ou trabalho pendente, Sammy pergunta somente depois da inspeção inicial.
- A pessoa consegue conversar naturalmente depois da ativação sem conhecer os nomes dos especialistas.
- Sammy seleciona subagentes com justificativa e não os aciona indiscriminadamente.
- Os subagentes devolvem resultados estruturados e Sammy os consolida.
- Nenhum subagente aprova artefatos nem conversa diretamente com a pessoa como ponto independente.
- O agente respeita os estados e gates em todas as tentativas de continuação.
- O reprocessamento não duplica artefatos nem repete operações externas concluídas.
- A publicação fica desativada até haver autorização explícita.

#### Comandos úteis para verificar a instalação

```bash
# Iniciar o Claude Code usando Sammy explicitamente
claude --agent sammy

# Dentro do Claude Code, verificar os agentes disponíveis
/agents

# Chamar Sammy: ele reconhece o repositório e decide o próximo trabalho
/hora-de-trabalhar

# Retomar explicitamente uma execução interrompida, se necessário
/continuar-projeto
```

A documentação do Claude Code informa que agentes de projeto são descobertos em `.claude/agents/`; o agente padrão da conversa pode ser definido pela propriedade `agent` em `settings.json`, e `--agent` pode selecionar um agente para uma sessão específica. Conferir sempre a documentação correspondente à versão instalada.

### Estratégia de implementação do framework

A implementação deve ocorrer em incrementos, priorizando primeiro o motor de estado, a configuração e Sammy como agente principal. Não começar criando um grande número de agentes desconectados. A arquitetura de automação inteligente e sua ordem de implementação são detalhadas nas partes sobre orquestração, execução incremental e implantação do framework.

#### Etapa 1 — Estrutura e governança

- Criar pastas.
- Criar `CLAUDE.md`.
- Criar regras de idioma, aprovação, rastreabilidade e integridade das fontes.
- Criar os formatos de estado.
- Criar templates dos documentos.

**Critério de conclusão:** Claude respeita o idioma, identifica a etapa correta e não avança gates.

#### Etapa 2 — Ingestão e diagnóstico

- Implementar extração de PDF.
- Identificar documentos digitalizados ou parcialmente extraíveis.
- Criar agentes analistas.
- Criar `/analisar-documentos`.
- Criar validação de referências às fontes.

**Critério de conclusão:** o diagnóstico separa fatos, inferências, propostas e dúvidas, com referências às fontes.

#### Etapa 3 — Planejamento

- Implementar agente de arquitetura.
- Implementar planejamento de equipes e fases.
- Criar `/planejar-projeto`.
- Criar auditoria do planejamento.

**Critério de conclusão:** os três documentos são coerentes com o diagnóstico e aguardam aprovação humana.

#### Etapa 4 — Backlog

- Implementar criação de histórias.
- Implementar agrupamento em épicos.
- Implementar decomposição em funcionalidades.
- Criar rastreabilidade automatizada.
- Criar `/montar-backlog` e `/validar-planejamento`.

**Critério de conclusão:** cada requisito, história, épico e funcionalidade possui relações verificáveis e o backlog aguarda aprovação humana.

#### Etapa 5 — GitHub Projects

- Configurar autenticação e permissões.
- Criar ou localizar o Project.
- Definir labels e campos.
- Implementar sincronizador idempotente.
- Criar modo de simulação.
- Criar mapeamento local.

**Critério de conclusão:** o sincronizador publica o backlog aprovado sem duplicações e valida o resultado no GitHub.

#### Etapa 6 — SDD por funcionalidade

- Criar `/especificar-funcionalidade`.
- Criar `/planejar-tarefas`.
- Criar gates por funcionalidade.
- Criar `/executar-tarefa`.
- Criar `/revisar-entrega` com evidências.

**Critério de conclusão:** uma funcionalidade pode percorrer requisitos, desenho, tarefas, implementação e revisão sem avançar gates indevidamente.

#### Etapa 7 — Sincronização contínua

- Criar GitHub Actions.
- Sincronizar estados aprovados com o Project.
- Detectar conflitos entre documentos e alterações manuais nas Issues.
- Criar visão consolidada de progresso.

**Critério de conclusão:** o Project representa o estado dos artefatos e os conflitos de sincronização são identificados antes de qualquer sobrescrita.
### Plano de validação do framework com projetos-piloto

Antes de adotar a estrutura em um projeto importante, testar o workflow em pelo menos três casos diferentes.

#### Piloto A — Projeto pequeno e bem definido

**Objetivo:** verificar se o framework consegue reduzir rigor sem perder rastreabilidade.

Entradas sugeridas:
- documento de requisitos curto;
- modelo de dados simples;
- uma ou duas personas;
- poucas funcionalidades.

Resultado esperado:
- diagnóstico conciso;
- arquitetura enxuta;
- uma ou poucas fases;
- poucos épicos e histórias;
- funcionalidades sem decomposição artificial;
- publicação de teste com `--dry-run`.

Critério de sucesso: não produzir excesso de documentos ou níveis de backlog sem valor.

#### Piloto B — Projeto médio com vários módulos

**Objetivo:** verificar rastreabilidade, decomposição e dependências.

Entradas sugeridas:
- requisitos com múltiplos fluxos;
- modelo de dados com várias entidades;
- integrações e permissões;
- mais de uma frente de trabalho.

Resultado esperado:
- arquitetura com fronteiras claras;
- equipes e responsabilidades propostas;
- fases com dependências;
- histórias validadas por INVEST;
- épicos com técnica de decomposição registrada;
- funcionalidades com especificação SDD independente;
- rastreabilidade validada por script e auditor.

Critério de sucesso: nenhum requisito importante desaparece entre os artefatos e nenhuma funcionalidade duplica outra sem justificativa.

#### Piloto C — Projeto existente com documentação incompleta ou conflito

**Objetivo:** testar a honestidade do agente diante de incerteza.

Entradas sugeridas:
- requisitos incompletos;
- diagrama de dados desatualizado;
- repositório com código legado;
- divergências entre documento e implementação.

Resultado esperado:
- fatos separados de inferências;
- divergências documentadas;
- questões abertas com impacto;
- nenhuma tecnologia ou regra inventada;
- proposta de migração incremental quando necessária;
- bloqueios explícitos antes de decisões irreversíveis.

Critério de sucesso: o agente sabe dizer “não há informação suficiente” e não apresenta hipótese como decisão aprovada.

#### Registro de avaliação dos pilotos

```markdown
# Avaliação do piloto — [A/B/C]

**Projeto:** ...
**Data:** ...
**Versão do framework:** ...

## Qualidade dos documentos
- Precisão:
- Cobertura:
- Clareza:
- Rastreabilidade:

## Qualidade do backlog
- Histórias INVEST:
- Critérios verificáveis:
- Épicos coerentes:
- Fatias verticais:
- Dependências identificadas:

## Segurança do processo
- Gates respeitados:
- Aprovações não automatizadas:
- Conflitos tratados:
- Evidências produzidas:

## Operação
- Tempo de revisão humana:
- Retrabalho:
- Itens redundantes:
- Falhas de sincronização:

## Ajustes necessários
- ...

## Decisão
Adotar | Ajustar e repetir | Não adotar ainda
```
### Sequência de implementação revisada: automação primeiro, mas com segurança

A ordem de construção deve priorizar Sammy como agente principal, o motor de estado e os contratos de delegação — não criar dezenas de agentes independentes primeiro.

#### Incremento 1 — Motor de estado e configuração

- Criar configuração central do workflow.
- Criar manifesto de execução.
- Criar grafo de dependências e validação de transições.
- Criar cálculo de hashes e reprocessamento seletivo.
- Criar templates centrais com catálogo e condições de uso.

**Pronto quando:** o sistema sabe em que estado está, o que mudou, o que precisa ser feito e o que não pode fazer.

#### Incremento 2 — Sammy e a ativação `/hora-de-trabalhar`

- Criar `.claude/agents/sammy.md` e configurá-lo como agente principal.
- Criar a Skill `/hora-de-trabalhar` como comando explícito de ativação, disponível somente por invocação da pessoa (`disable-model-invocation: true`).
- Criar a Skill `/processar-projeto` como procedimento de processamento amplo, selecionado por Sammy quando apropriado.
- Implementar detecção de fontes e contexto.
- Implementar triagem automática.
- Delegar análises independentes em paralelo.
- Consolidar diagnóstico e gerar pacote de revisão.

**Pronto quando:** a pessoa executa apenas `/hora-de-trabalhar`, Sammy reconhece o repositório e conduz autonomamente a próxima atividade segura; em projetos novos, isso inclui a descoberta até a revisão do diagnóstico.

#### Incremento 3 — Geração e auditoria do planejamento

- Produzir arquitetura, equipes, fases e backlog.
- Escolher templates conforme o perfil.
- Executar autocorreção limitada.
- Gerar revisão consolidada.
- Vincular aprovação aos hashes.

**Pronto quando:** um comando produz planejamento e backlog coerentes, com rastreabilidade e pendências explícitas.

#### Incremento 4 — Retomada e mudança incremental

- Criar `/continuar-projeto` e `/reprocessar-projeto`.
- Detectar mudanças em fontes e artefatos.
- Invalidar somente aprovações afetadas.
- Retomar operações interrompidas sem duplicação.

**Pronto quando:** o sistema pode ser usado em várias sessões sem recomeçar do zero.

#### Incremento 5 — Integração GitHub idempotente

- Descobrir repositório e Project.
- Reutilizar campos, labels e automações existentes.
- Publicar com autorização persistente e limites explícitos.
- Sincronizar estados aprovados e detectar conflitos.

**Pronto quando:** a integração pode ser executada repetidamente e preserva mudanças humanas.

#### Incremento 6 — Hooks, CI e acompanhamento

- Adicionar hooks locais rápidos e restritos.
- Adicionar validações em pull requests.
- Sincronizar estados após merge aprovado.
- Criar resumo de progresso e alertas de inconsistência.

**Pronto quando:** o projeto mantém os artefatos e o board consistentes sem depender de alguém lembrar de executar verificações simples.
### Critérios de sucesso do workflow

O framework será considerado funcional quando:

1. Receber os documentos de entrada sem exigir que os dados sejam copiados manualmente para o chat.
2. Extrair e referenciar as informações disponíveis.
3. Identificar lacunas e contradições sem preenchê-las por suposição.
4. Gerar os documentos de planejamento em português.
5. Gerar histórias, épicos e funcionalidades com identificadores estáveis.
6. Manter rastreabilidade entre fontes, requisitos e backlog.
7. Impedir avanço de etapas sem aprovação humana.
8. Criar Issues e organizá-las no GitHub Projects sem duplicações.
9. Detectar conflitos entre documentos versionados e alterações feitas manualmente no GitHub.
10. Gerar especificações individuais e tarefas verificáveis por funcionalidade.
11. Registrar evidências para declarar tarefas concluídas.
12. Permitir que o projeto continue usando os artefatos mesmo que o modelo de IA ou a ferramenta de agente sejam substituídos.
### Critérios de sucesso da automação

Além dos critérios funcionais anteriores, medir:

- Quantidade de comandos necessários para ir dos PDFs ao pacote de aprovação.
- Percentual de etapas executadas sem intervenção manual.
- Quantidade de perguntas feitas e proporção realmente bloqueadora.
- Quantidade de artefatos reprocessados sem necessidade.
- Percentual de requisitos com rastreabilidade até uma entrega verificável.
- Taxa de duplicação de Issues, que deve ser zero.
- Taxa de conflitos de sincronização detectados corretamente.
- Quantidade de aprovações vinculadas a hashes válidos.
- Tempo gasto pela pessoa revisando decisões, em vez de organizar arquivos.
- Número de problemas encontrados antes da implementação.

Metas devem ser estabelecidas depois de executar pilotos. Não declarar percentuais de automação ou ganhos de produtividade sem medição real.
### Decisões em aberto antes da implementação

As seguintes decisões precisam ser confirmadas no início da implantação do framework. O workflow pode ser criado com padrões provisórios, mas não deve inventar respostas.

| Decisão | Padrão proposto | Observação |
|---|---|---|
| Repositório | GitHub | Confirmar organização e repositório de destino. |
| Proprietário do Project | Organização ou usuário | Necessário para localizar ou criar o Project. |
| Nome do Project | Gestão de Engenharia | Pode ser alterado. |
| Issue hierarchy | Épico como pai de funcionalidades | Depende do suporte e das permissões do repositório. |
| Histórias como Issues | Não, por padrão | Permanecem nos documentos; criar Issues individuais quando necessário. |
| Idioma dos commits | Português | Confirmar convenção da equipe. |
| Tamanho das tarefas | 2 a 4 horas como referência | Ajustar conforme projeto e equipe. |
| Datas das fases | Não estimar sem informação | Primeiro definir sequência e dependências. |
| Política de sincronização | Git como fonte canônica | Alterações manuais no GitHub geram conflito para resolução. |
| Aprovação | Humana | Não automatizar aprovação. |
### Recomendação final revisada

A proposta deve ser implementada como um framework modular, orientado a estado e altamente automatizado, não como uma cadeia rígida que força todos os projetos a terem o mesmo volume de artefatos. Sammy é o agente principal e o ponto único de contato. A entrada padrão é o comando explícito `/hora-de-trabalhar`, que inicia o protocolo de reconhecimento e decisão da próxima atividade. `/processar-projeto` é um procedimento de processamento amplo, selecionado por Sammy quando o contexto exigir; os demais comandos são recursos de manutenção e intervenção.

A primeira versão executável deve incluir:

1. Estrutura, idioma, contexto e regras de aprovação.
2. Templates completos dos artefatos do planejamento e backlog.
3. Ingestão e diagnóstico com referências às fontes.
4. Planejamento de arquitetura, equipes e fases.
5. Histórias, épicos e funcionalidades com técnicas de decomposição e critérios de qualidade.
6. Auditoria semântica e validação determinística de rastreabilidade.
7. Integração GitHub em modo de simulação e publicação idempotente.
8. Especificação SDD por funcionalidade com requisitos, desenho, tarefas e revisão.

Só depois de validar os primeiros projetos-piloto devem ser adicionadas automações mais ambiciosas, execução paralela de múltiplos agentes e sincronização contínua por GitHub Actions.

**Princípio central atualizado:** a pessoa conversa com Sammy, e Sammy coordena o workflow. O sistema deve gerar documentação suficiente para tomar decisões e construir o produto corretamente — não documentação máxima. A qualidade está na clareza, rastreabilidade, capacidade de verificação e adequação ao risco, não na quantidade de arquivos.
### Decisões arquiteturais finais do framework

1. **Um agente principal, várias capacidades:** Sammy é a experiência padrão; ele aciona Skills e subagentes conforme a solicitação e o estado do projeto.
2. **Sammy orientado a estado:** não depende da memória da conversa para saber o que executar; consulta manifesto, hashes, aprovações e grafo de dependências.
3. **Grafo de dependências:** permite paralelismo seguro e reprocessamento seletivo.
4. **Templates centrais com seleção dinâmica:** todo artefato tem modelo, mas nem todo modelo é obrigatório em todos os projetos.
5. **Agentes especializados, não numerosos por princípio:** agentes são criados quando há responsabilidade distinta, necessidade de contexto isolado ou trabalho paralelo real.
6. **Scripts para o que é verificável por código:** IDs, schemas, hashes, links, dependências, estados e APIs não devem depender só de julgamento do LLM.
7. **Hooks para garantias determinísticas:** usar eventos para inspeções rápidas e bloqueios, não para executar o pipeline inteiro a cada edição.
8. **Correção automática limitada:** o sistema resolve problemas mecânicos e propõe alterações semânticas com transparência.
9. **Aprovações vinculadas a versões:** qualquer alteração posterior em artefato aprovado exige avaliação de impacto.
10. **Git como fonte canônica; GitHub como projeção operacional:** sincronização é idempotente e sensível a conflitos.
11. **Autonomia controlada como padrão:** máxima automação local, gates humanos nos pontos de julgamento e autorização explícita para efeitos externos.
12. **Operação incremental:** o sistema executa apenas o que mudou ou está pendente.

**Resultado esperado:** a pessoa abre o repositório, inicia ou retoma uma sessão de Sammy e executa `/hora-de-trabalhar`. Não precisa descrever previamente a tarefa: Sammy assume a descoberta, análise, classificação, escolha do workflow, delegação, geração, validação, organização e sincronização. Depois da ativação, a pessoa conversa naturalmente e participa apenas nas decisões, aprovações e autorizações necessárias.

---
