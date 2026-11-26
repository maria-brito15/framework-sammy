<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 2959–3453. -->

> **Nesta página:** Agente principal, subagentes, Skills, contratos, contexto permanente e CLAUDE.md.

[← Voltar ao índice da documentação](../README.md)

---

## Parte III — Claude Code: agentes, skills e contexto

Esta parte define como o Claude Code executa o processo sob coordenação de Sammy. A pessoa conversa com Sammy e, quando necessário, utiliza comandos explícitos. Sammy aciona as Skills adequadas, delega agentes especializados e consulta o contexto persistente. Os modelos completos ficam no Apêndice C.

### Sammy — agente principal da sessão

Sammy deve ser configurado como o agente principal do Claude Code, não como um subagente que precisa ser chamado por outro agente. A sessão principal assume a identidade, as instruções e as responsabilidades de Sammy; ele utiliza a ferramenta de delegação do Claude Code para acionar os subagentes especialistas.

**Configuração preferencial:** definir `"agent": "sammy"` em `.claude/settings.json`. Também é possível iniciar uma sessão específica com `claude --agent sammy`. O argumento da linha de comando prevalece sobre a configuração do projeto para aquela sessão.

Sammy é responsável por:

1. Receber toda solicitação e manter a comunicação com a pessoa em português brasileiro.
2. Interpretar o pedido e decidir se é uma conversa, uma ação pontual ou um workflow completo.
3. Consultar estado, manifesto, hashes, fontes e documentos aprovados antes de agir.
4. Selecionar Skills, templates e especialistas de acordo com a tarefa e o perfil do projeto.
5. Preparar instruções delimitadas para os subagentes, incluindo contexto, arquivos permitidos, restrições e formato esperado de retorno.
6. Delegar em paralelo somente atividades independentes e consolidar os resultados antes de editar artefatos compartilhados.
7. Resolver divergências mecânicas por validação e apresentar divergências semânticas como decisões pendentes.
8. Conduzir gates de aprovação sem aprovar artefatos em nome da pessoa.
9. Solicitar autorização antes de operações externas, destrutivas ou que alterem dados remotos.
10. Apresentar um resumo único e manter o estado pronto para retomada.

Sammy não deve delegar a comunicação de decisões ao especialista. Os subagentes devolvem resultados a Sammy; Sammy apresenta à pessoa as perguntas, opções e impactos consolidados.

### Subagentes especializados

Cada subagente deve ter uma missão clara, instruções em português e limites de atuação. Os especialistas não são pontos de contato independentes; trabalham sob coordenação de Sammy e devolvem a ele seus resultados.

| Agente | Responsabilidade | Limite principal |
|---|---|---|
| `analista-de-documentos` | Extrair e interpretar requisitos, objetivos, atores, regras e restrições dos documentos. | Não inventar informações nem decidir arquitetura. |
| `analista-de-dados` | Interpretar entidades, atributos, relacionamentos, cardinalidades e restrições do modelo de dados. | Não alterar o modelo original nem presumir regras não documentadas. |
| `analista-de-repositorio` | Inspecionar código, estrutura, dependências, testes, migrações e convenções de um projeto existente. | Não tratar o comportamento legado como requisito aprovado nem modificar código durante o diagnóstico. |
| `analista-de-produto` | Transformar necessidades e requisitos em histórias de usuário e critérios de aceitação. | Não tomar decisões de implementação. |
| `arquiteto-de-software` | Propor arquitetura, componentes, fronteiras, integrações e decisões técnicas. | Não implementar código. |
| `planejador-de-entregas` | Propor organização de equipes, responsabilidades, fases e dependências. | Não inventar nomes, disponibilidade ou capacidade de pessoas. |
| `especialista-em-backlog` | Agrupar histórias em épicos e decompor épicos em funcionalidades entregáveis. | Não perder rastreabilidade nem duplicar escopo sem justificativa. |
| `consolidador-de-especificacoes` | Comparar especificações da entrega, implementação e documentação global; propor consolidação de decisões reutilizáveis. | Não alterar código nem aprovar mudanças globais; não copiar detalhes locais sem valor futuro. |
| `auditor-de-planejamento` | Revisar coerência, cobertura, rastreabilidade, contradições e lacunas. | Não aprovar nem corrigir silenciosamente o artefato auditado. |
| `publicador-do-github` | Criar e atualizar Issues, labels, relações e itens do GitHub Projects. | Não publicar rascunhos nem alterar o estado de aprovação. |
| `implementador` | Implementar uma tarefa aprovada, incluindo testes. | Deve parar diante de ambiguidade ou conflito com a especificação. |
| `revisor` | Verificar a implementação contra os artefatos aprovados e produzir evidências. | Não adicionar requisitos nem revisar com base apenas em preferências pessoais. |

#### Contrato de delegação de Sammy

Sammy não deve enviar prompts vagos como “analise o projeto”. Cada delegação deve ser um pacote de trabalho delimitado, com o mínimo de contexto necessário e uma saída previsível.

**Informações enviadas ao subagente:**

| Campo | Conteúdo |
|---|---|
| Objetivo | Pergunta ou resultado específico que deve ser produzido. |
| Contexto | Resumo do projeto e decisões relevantes já aprovadas. |
| Fontes | Caminhos exatos dos arquivos que devem ser consultados. |
| Estado | Gate e versão dos artefatos que podem ser usados. |
| Escopo | O que analisar ou produzir e o que está fora do trabalho. |
| Escrita permitida | Arquivos que o subagente pode criar ou modificar. |
| Restrições | Suposições proibidas, limites de ferramenta e ações não autorizadas. |
| Formato de retorno | Estrutura exigida para que Sammy possa consolidar o resultado. |

**Resposta esperada do subagente:**

- Resultado e conclusão.
- Evidências e referências às fontes.
- Arquivos criados ou modificados.
- Suposições, lacunas e divergências.
- Validações executadas e respectivos resultados.
- Decisões que dependem da pessoa usuária.
- Próxima etapa recomendada.

Sammy deve recusar ou refazer uma delegação cujo resultado não informe fontes, limitações ou arquivos alterados quando esses dados forem relevantes para a tarefa.

#### Restrições de ferramentas por agente

As ferramentas disponíveis devem ser limitadas conforme a responsabilidade:

- **Sammy:** precisa manter acesso à ferramenta de delegação `Agent` e às Skills necessárias, além das ferramentas de leitura, escrita e execução permitidas pelo projeto. Restringir operações sensíveis por permissões e gates; não remover a capacidade de delegação do agente principal.
- **Analistas de documentos e dados:** leitura de arquivos; sem escrita nos documentos originais.
- **Analista de repositório:** leitura do código e das configurações; sem escrita durante inspeção e diagnóstico, salvo tarefa delimitada de modernização aprovada.
- **Analista de produto:** leitura de fontes aprovadas e escrita apenas nos arquivos de histórias, quando invocado pela Skill correspondente.
- **Arquiteto:** leitura dos documentos aprovados e escrita nos artefatos de arquitetura; sem ferramentas de implementação de código.
- **Planejador de entregas:** leitura do diagnóstico e arquitetura; escrita nos documentos de equipes e fases.
- **Especialista em backlog:** leitura dos artefatos aprovados e escrita nos arquivos de backlog.
- **Consolidador de especificações:** leitura das especificações aprovadas, diff/código revisado e contexto global; escrita apenas em uma proposta de consolidação, sem aplicar alterações globais aprovadas automaticamente.
- **Auditor:** leitura dos documentos e execução de validadores; não altera artefatos auditados.
- **Publicador do GitHub:** acesso ao `gh` e aos scripts de sincronização; não altera documentos-fonte nem gates.
- **Implementador:** acesso ao código e aos testes, condicionado a `tarefas:aprovadas`.
- **Revisor:** leitura do código e execução de testes/verificações; escrita apenas no relatório de revisão, quando autorizado.

A sintaxe exata dos campos `tools`, `model` e demais propriedades deve ser validada com a versão do Claude Code instalada. As definições dos agentes devem ser mantidas como arquivos Markdown com metadados compatíveis com o formato suportado pela ferramenta. Para Sammy, não restringir a lista de ferramentas sem confirmar que a ferramenta `Agent` continua disponível; ele precisa delegar especialistas.
### Skills e seus contratos

Uma skill representa um procedimento repetível. Ela descreve quando deve ser usada, quais fontes deve ler, quais agentes deve acionar, quais arquivos pode produzir e como verificar o resultado.

#### `/iniciar-projeto`

**Objetivo:** preparar a estrutura inicial.

**Procedimento:**

1. Verificar se o diretório já contém um projeto.
2. Perguntar o nome do projeto somente se não houver informação disponível.
3. Criar as pastas previstas na estrutura de diretórios.
4. Criar `CLAUDE.md`, regras iniciais, arquivos de contexto vazios e estados iniciais.
5. Criar os modelos de documentos.
6. Não sobrescrever arquivos existentes sem autorização.
7. Apresentar um resumo da estrutura criada.

**Saída:** estrutura inicial e instruções do projeto.

#### `/analisar-documentos`

**Objetivo:** produzir um diagnóstico fundamentado nas fontes originais.

**Procedimento:**

1. Localizar todos os arquivos em `documentos/entrada/`.
2. Confirmar quais arquivos foram encontrados e quais estão ausentes.
3. Extrair texto e identificar páginas, seções, tabelas e diagramas relevantes.
4. Verificar se o PDF possui texto selecionável ou se é digitalização.
5. Se houver páginas sem texto extraível, informar a limitação e solicitar uma estratégia de leitura adequada; não inventar conteúdo.
6. Delegar a interpretação de requisitos ao `analista-de-documentos`.
7. Delegar a interpretação do modelo de dados ao `analista-de-dados`.
8. Cruzar as duas análises e identificar contradições, lacunas e suposições.
9. Registrar a origem de cada afirmação relevante: arquivo, página e seção, quando disponíveis.
10. Gerar `plano/diagnostico.md` como rascunho.
11. Definir `plano/.status` como `diagnostico:em-revisao`.
12. Apresentar as dúvidas e os pontos que exigem validação humana.

**Não pode:** gerar arquitetura definitiva, criar requisitos não presentes nas fontes ou marcar o diagnóstico como aprovado.

#### `/planejar-projeto`

**Pré-condição:** diagnóstico aprovado.

**Objetivo:** produzir o planejamento geral de engenharia.

**Procedimento:**

1. Ler `plano/.status` e confirmar `diagnostico:aprovado`.
2. Ler `plano/diagnostico.md` e `.ia/contexto/`.
3. Acionar `arquiteto-de-software` para produzir `plano/arquitetura.md`.
4. Acionar `planejador-de-entregas` para produzir `plano/equipes.md` e `plano/fases.md` com base na arquitetura e nas dependências identificadas.
5. Solicitar ao auditor a verificação cruzada dos três documentos.
6. Executar verificações de referências e identificadores.
7. Salvar os documentos como rascunho.
8. Atualizar o estado para `planejamento:em-revisao`.
9. Apresentar decisões, alternativas, riscos, premissas e perguntas em aberto.

**Não pode:** marcar o planejamento como aprovado nem inventar datas, pessoas ou capacidades disponíveis.

#### `/montar-backlog`

**Pré-condição:** planejamento aprovado.

**Objetivo:** transformar necessidades e requisitos em backlog rastreável.

**Ordem de produção:**

1. Gerar `plano/tarefas/historias-de-usuario.md`.
2. Agrupar as histórias em `plano/tarefas/epicos.md`.
3. Decompor os épicos em `plano/tarefas/funcionalidades.md`.
4. Atualizar `plano/rastreabilidade.md`.
5. Executar a auditoria de cobertura e consistência.
6. Salvar tudo como rascunho e marcar `backlog:em-revisao`.
7. Apresentar o resultado para aprovação humana.

A ordem de geração não altera a hierarquia conceitual: um épico agrupa funcionalidades; as funcionalidades entregam valor e atendem uma ou mais histórias; as histórias descrevem necessidades de usuários. Uma história pode ser atendida por mais de uma funcionalidade e uma funcionalidade pode contribuir para mais de uma história, desde que essa relação seja explícita.

#### `/validar-planejamento`

**Objetivo:** executar validação semântica e determinística.

**Verificações mínimas:**

- Todos os requisitos de origem foram classificados e considerados.
- Requisitos sem histórias estão justificados.
- Todas as histórias possuem objetivo, ator ou persona e critérios de aceitação.
- Todas as histórias estão associadas a pelo menos um épico ou possuem justificativa.
- Todos os épicos possuem objetivo e funcionalidades relacionadas.
- Todas as funcionalidades possuem escopo, critérios de aceitação e origem rastreável.
- As funcionalidades são compatíveis com a arquitetura proposta.
- As entidades do modelo de dados relevantes estão consideradas ou justificadas como fora de escopo.
- As dependências entre funcionalidades e fases não são circulares.
- As equipes propostas possuem competências compatíveis com as entregas atribuídas.
- Não há IDs duplicados, referências quebradas ou decisões contraditórias.
- Questões em aberto estão identificadas e não foram tratadas como decisões aprovadas.

**Saída:** relatório com `APROVÁVEL`, `APROVÁVEL COM RESSALVAS` ou `NÃO APROVÁVEL`, acompanhado de achados e evidências. O auditor não aprova o planejamento.

#### Skills de aprovação

As skills `/aprovar-planejamento`, `/aprovar-backlog`, `/aprovar-requisitos`, `/aprovar-desenho` e `/aprovar-tarefas` são ações explícitas da pessoa usuária.

Cada uma deve:

1. Mostrar exatamente quais documentos serão aprovados.
2. Verificar se o auditor não apontou bloqueios pendentes.
3. Verificar se as questões obrigatórias estão resolvidas.
4. Solicitar confirmação explícita quando o comando, por si só, não for inequívoco.
5. Registrar a aprovação no estado correspondente.
6. Registrar data, referência do commit e responsável, em um histórico de aprovações versionado, se esse recurso estiver habilitado.
7. Não reescrever os documentos durante o ato de aprovação.

#### `/publicar-no-github`

**Pré-condição:** backlog aprovado.

**Objetivo:** publicar os itens aprovados no repositório e no GitHub Projects.

**Procedimento:**

1. Confirmar repositório, organização ou usuário proprietário e Project de destino.
2. Verificar autenticação e permissões do GitHub CLI.
3. Executar primeiro em modo de simulação (`--dry-run`).
4. Mostrar a lista de Issues, labels, relações, campos e alterações que seriam realizadas.
5. Verificar se existe autorização persistente válida para publicar nesse repositório e nesse Project; se não existir, solicitar autorização uma única vez para o escopo apresentado.
6. Criar labels inexistentes.
7. Criar Issues de épicos.
8. Criar Issues de funcionalidades e associá-las aos respectivos épicos, quando a relação pai-filho estiver habilitada.
9. Adicionar as Issues ao GitHub Project.
10. Preencher campos personalizados.
11. Registrar os números, IDs e URLs no arquivo `plano/integracao-github/mapeamento.json`.
12. Consultar o GitHub para confirmar os resultados.
13. Registrar falhas parciais sem repetir operações já concluídas.
14. Marcar `github:sincronizado` somente após validação completa.

#### `/atualizar-github`

Compara os artefatos aprovados com os itens existentes no GitHub. Deve apresentar um plano de atualização antes de alterar títulos, corpos, labels, relações ou campos. Mudanças manuais no GitHub não devem ser sobrescritas silenciosamente. Em caso de conflito, interromper e solicitar decisão.

#### `/ver-progresso`

Exibe:

- Estado atual do planejamento.
- Estado de aprovação de cada artefato.
- Quantidade de histórias, épicos, funcionalidades e tarefas.
- Funcionalidades bloqueadas ou sem dependências resolvidas.
- Issues correspondentes no GitHub.
- Próxima etapa segura do workflow.
- Pendências e decisões aguardando intervenção humana.

#### `/especificar-funcionalidade`

Recebe um identificador `FUNC-xxx`, consulta os artefatos aprovados e cria a pasta da especificação individual. Produz requisitos específicos e, após aprovação dos requisitos, o desenho técnico. Não inicia tarefas nem implementação antes dos gates correspondentes.

#### `/planejar-tarefas`

Decompõe o desenho técnico aprovado em tarefas pequenas, independentes quando possível, com dependências explícitas, estimativas, critérios de aceitação, arquivos prováveis e comandos de verificação. Como referência, o livro sugere tarefas de 2 a 4 horas para projetos médios; esse intervalo deve ser ajustado ao tamanho e à natureza do projeto.

#### `/executar-tarefa`

Recebe um identificador `TAR-xxx`, verifica o estado da funcionalidade e implementa somente aquela tarefa. Deve ler requisitos, desenho, tarefas, contexto e convenções. Se surgir ambiguidade, interrompe a execução e propõe atualização da especificação antes de continuar.

#### `/revisar-entrega`

Revisa a implementação em contexto independente, comparando o resultado com requisitos, desenho, tarefas e critérios de aceitação. Deve executar as verificações pertinentes e produzir evidências. Não cria requisitos novos.
#### `/consolidar-entrega`

**Orquestração automática:** após `/revisar-entrega` aprovar uma história ou funcionalidade, Sammy deve iniciar esta skill automaticamente, sem exigir que a pessoa memorize outro comando. O comando explícito continua disponível para repetir a verificação ou consolidar uma entrega específica.

Executa o ciclo de alinhamento após uma revisão aprovada. Consulta a especificação da unidade entregue, o código/diff, os resultados de verificação e o contexto global. O `consolidador-de-especificacoes` propõe somente mudanças que serão úteis em entregas futuras. Sammy apresenta o diff, executa validações e solicita aprovação humana para mudanças semânticas globais. A skill registra também quando nenhuma consolidação é necessária. Não modifica código nem marca a entrega como concluída antes de atender à Definição de Concluído.

### Modelo de uma skill

Exemplo de estrutura de `SKILL.md`:

```markdown
---
name: analisar-documentos
description: Analisa documentos de requisitos e modelo de dados, identifica fatos, lacunas, contradições e questões em aberto e gera o diagnóstico do projeto. Use quando for necessário iniciar a análise das fontes originais. Não use para aprovar documentos nem para implementar código.
---

# Analisar documentos

## Objetivo

Gerar `plano/diagnostico.md` com base exclusiva nas fontes disponíveis.

## Pré-condições

- Os arquivos de entrada devem estar em `documentos/entrada/`.
- Não sobrescrever diagnósticos aprovados sem autorização.

## Fontes obrigatórias

- `documentos/entrada/requisitos.pdf`
- `documentos/entrada/modelo-de-dados.pdf` ou `.md`
- Regras em `.claude/rules/`

## Procedimento

1. Conferir os arquivos existentes.
2. Extrair o conteúdo e verificar páginas sem texto extraível.
3. Acionar os agentes analistas correspondentes.
4. Cruzar requisitos e modelo de dados.
5. Classificar fatos, inferências, propostas e questões em aberto.
6. Registrar referências às fontes.
7. Gerar `plano/diagnostico.md`.
8. Executar validações disponíveis.
9. Atualizar o estado para `diagnostico:em-revisao`.
10. Apresentar o diagnóstico para revisão humana.

## Restrições

- Não inventar requisitos ou regras de negócio.
- Não transformar inferências em fatos.
- Não marcar o diagnóstico como aprovado.
- Não avançar automaticamente para a arquitetura.

## Critérios de conclusão

- Todas as fontes encontradas foram analisadas ou suas limitações foram registradas.
- As afirmações relevantes têm referências às fontes.
- Lacunas e contradições estão explícitas.
- O diagnóstico foi salvo como rascunho e está aguardando revisão.
```

O restante das skills deve seguir o mesmo padrão: objetivo, gatilho de uso, pré-condições, fontes, procedimento, restrições, saídas e critérios de conclusão.
### Modelo de definição de agente

Exemplo conceitual para `.claude/agents/arquiteto-de-software.md`:

```markdown
---
name: arquiteto-de-software
description: Analisa requisitos e contexto aprovados para propor arquitetura, componentes, fronteiras, integrações e decisões técnicas. Não implementa código.
---

# Arquiteto de software

## Responsabilidade

Produzir uma proposta arquitetural coerente com os requisitos e as restrições do projeto.

## Fontes

- `plano/diagnostico.md`
- `.ia/contexto/produto.md`
- `.ia/contexto/arquitetura.md`, quando existir
- `.ia/contexto/principios.md`
- `documentos/entrada/`, quando uma referência original precisar ser conferida

## Entregável

- `plano/arquitetura.md`

## Regras

- Não implementar código.
- Não inventar requisitos ou regras de negócio.
- Distinguir fatos, restrições, inferências e propostas.
- Explicar o motivo das decisões relevantes.
- Registrar alternativas e trade-offs.
- Mapear requisitos relevantes para componentes e decisões.
- Identificar riscos e questões em aberto.
- Não aprovar o próprio documento.
```

O metadado acima é uma referência de conteúdo. Antes de instalar as definições, conferir o esquema de frontmatter aceito pela versão do Claude Code utilizada e restringir as ferramentas disponíveis a cada agente.
### Contexto permanente do projeto

Os arquivos em `.ia/contexto/` guardam informações que o agente precisa consultar em várias sessões.

#### `produto.md`

- O que é o produto.
- Quem são os usuários.
- Qual problema resolve.
- Objetivos e métricas.
- O que deliberadamente não faz.

#### `arquitetura.md`

- Visão arquitetural aprovada.
- Domínios e componentes.
- Fronteiras e integrações.
- Restrições e decisões duradouras.
- Referência ao documento completo em `plano/arquitetura.md`.

#### `equipe.md`

- Equipes e responsabilidades aprovadas.
- Responsáveis conhecidos, quando fornecidos.
- Competências e formas de colaboração.
- Matriz de aprovação.

#### `convencoes.md`

- Padrões de código e nomenclatura.
- Organização de diretórios.
- Estratégia de erros.
- Estratégia de testes.
- Convenções de API, dados e segurança.
- Condições para exigir uma especificação.

#### `dados.md` (condicional)

- Estratégia de persistência aprovada.
- Regras globais de integridade e consistência.
- Convenções de migrations, versionamento e evolução do schema.
- Ciclo de vida, retenção, exclusão, anonimização e proteção dos dados.
- Regras de transação, concorrência, idempotência e auditoria, quando aplicáveis.
- Referências ao modelo de dados, schemas e migrations mantidos em suas fontes próprias.

Não reproduzir todas as tabelas e colunas neste arquivo. O objetivo é registrar decisões e convenções que devem orientar futuras funcionalidades.

#### `interface.md` (condicional)

- Princípios de experiência e consistência visual.
- Padrões de navegação, layout, responsividade e acessibilidade.
- Componentes e padrões compartilhados.
- Estados globais de carregamento, vazio, sucesso e erro.
- Regras de linguagem, feedback e interação.

Não descrever cada tela. Telas e fluxos específicos ficam na especificação da funcionalidade ou história correspondente.

#### `definicao-de-concluido.md`

- Critérios mínimos de qualidade compartilhados por todas as entregas.
- Testes obrigatórios conforme tipo e risco da mudança.
- Revisão de código e segurança, quando aplicáveis.
- Atualização de documentação e contratos relevantes.
- Evidências de verificação.
- Consolidação das decisões duradouras no contexto global.

A Definição de Concluído é diferente dos critérios de aceitação: critérios de aceitação descrevem o comportamento daquela história; a Definição de Concluído descreve o padrão de qualidade que todas as entregas precisam satisfazer.

O contexto não deve contradizer uma especificação aprovada. Se houver conflito, o agente deve interromper e solicitar qual artefato precisa ser atualizado. Os documentos globais devem evoluir por consolidação incremental, não por um exercício de detalhamento exaustivo antes da primeira implementação.
### Arquivo principal `CLAUDE.md`

O `CLAUDE.md` deve funcionar como roteador e manter as instruções fundamentais visíveis em todas as sessões.

Modelo inicial:

```markdown
# Projeto — Diretrizes do Claude Code

## Agente principal
- A sessão principal utiliza Sammy, definido em `.claude/agents/sammy.md`.
- A pessoa usuária conversa diretamente com Sammy; os demais agentes são especialistas delegados.
- Sammy coordena Skills, subagentes, validações e aprovações, respeitando os limites definidos neste arquivo.
- Para iniciar um ciclo de trabalho, a pessoa executa `/hora-de-trabalhar`; Sammy reconhece o estado antes de escolher a próxima atividade.
- Não exigir briefing inicial para iniciar a inspeção do repositório.

## Idioma

- Toda comunicação e documentação deve ser em português brasileiro.
- Manter nomes oficiais de tecnologias e convenções obrigatórias.
- Comandos, agentes, skills, documentos de negócio e mensagens devem usar português.

## Estrutura

- Agente principal: `.claude/agents/sammy.md`.
- Documentos de entrada: `documentos/entrada/`.
- Planejamento: `plano/`.
- Contexto permanente: `.ia/contexto/`.
- Especificações por funcionalidade: `.ia/especificacoes/`.
- Skills: `.claude/skills/`.
- Agentes: `.claude/agents/`.

## Processo

Este projeto utiliza Spec-Driven Development com gates de aprovação humana.

1. Leia as regras aplicáveis em `.claude/rules/`.
2. Consulte `.ia/contexto/` antes de decisões de produto ou engenharia.
3. Antes de executar uma etapa, leia o `.status` correspondente.
4. Arquivo existente não significa aprovação.
5. Nunca aprove um documento produzido por você.
6. Nunca implemente antes de `tarefas:aprovadas`.
7. Trabalhe em uma tarefa por vez, salvo autorização explícita para paralelismo.
8. Pare quando encontrar ambiguidade ou conflito com uma especificação aprovada.
9. Registre evidências de verificação; não declare conclusão sem prova.
10. Não altere documentos aprovados silenciosamente.

## Fonte de verdade

- Os documentos versionados no Git são a referência do planejamento e das especificações.
- O GitHub Projects representa o acompanhamento operacional; não substitui os documentos.

## Próxima etapa

Sammy seleciona a Skill correspondente ao pedido. Consulte as instruções completas em `.claude/skills/`.

```

---

## Parte IV — GitHub e automações externas

Esta parte trata da publicação do backlog, da gestão visual e da sincronização. O Git continua sendo a fonte canônica dos documentos; GitHub Issues e Projects refletem o trabalho aprovado e seu estado operacional.
