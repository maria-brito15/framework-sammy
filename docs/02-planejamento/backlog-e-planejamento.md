<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 1541–2708. -->

> **Nesta página:** Planejamento de produto e engenharia, histórias, épicos, funcionalidades, refinamento, sprints e gates.

[← Voltar ao índice da documentação](../README.md)

---

## Parte II — Planejamento de produto e engenharia

Esta parte explica como os documentos de entrada se transformam em planejamento, como o backlog é organizado e como o trabalho passa por especificação, aprovação, auditoria e preparação para implementação. A ordem conceitual é do entendimento do problema até unidades de entrega verificáveis.

### Conteúdo esperado dos documentos de planejamento

#### `plano/diagnostico.md`

Documento intermediário que registra o entendimento das fontes originais.

Seções recomendadas:

1. Resumo do projeto.
2. Objetivos identificados.
3. Atores e perfis de usuário.
4. Requisitos funcionais encontrados.
5. Requisitos não funcionais encontrados.
6. Regras de negócio encontradas.
7. Entidades e relacionamentos do modelo de dados.
8. Restrições e integrações mencionadas.
9. Correspondências entre requisitos e dados.
10. Contradições entre fontes.
11. Informações ausentes.
12. Questões em aberto.
13. Referências às fontes originais.
14. Premissas que precisam de confirmação.

Cada afirmação factual relevante deve ter uma referência à fonte, preferencialmente arquivo, página e seção. O agente deve distinguir claramente:

- **Fato da fonte:** informação explicitamente presente no documento.
- **Inferência:** interpretação razoável baseada nas fontes.
- **Proposta:** recomendação criada durante o planejamento.
- **Questão em aberto:** informação insuficiente para decidir.

#### `plano/arquitetura.md`

Seções recomendadas:

1. Resumo executivo da arquitetura.
2. Objetivos e restrições arquiteturais.
3. Requisitos arquiteturalmente relevantes.
4. Domínios e responsabilidades.
5. Componentes, módulos e fronteiras.
6. Fluxos principais e comunicação.
7. Arquitetura de dados e relação com o modelo fornecido.
8. Integrações externas.
9. Segurança, autenticação e autorização.
10. Requisitos não funcionais e estratégias de atendimento.
11. Implantação e infraestrutura, quando houver informação suficiente.
12. Observabilidade e operação.
13. Decisões arquiteturais (`DEC-xxx`).
14. Alternativas consideradas e justificativas.
15. Riscos técnicos e mitigação.
16. Mapeamento de requisitos para decisões e componentes.
17. Questões em aberto.

As tecnologias existentes nos documentos ou no repositório devem ser tratadas como restrições ou decisões existentes, conforme a evidência. Sugestões de tecnologias novas devem ser explicitamente rotuladas como propostas, com justificativa e alternativas.

#### `plano/equipes.md`

Seções recomendadas:

1. Premissas de organização.
2. Equipes ou frentes de trabalho propostas.
3. Responsabilidades de cada equipe.
4. Competências necessárias.
5. Entregáveis por equipe.
6. Dependências entre equipes.
7. Matriz RACI ou equivalente.
8. Responsabilidades de aprovação.
9. Necessidades de contratação ou alocação, quando identificadas.
10. Questões em aberto.

Possíveis frentes, a confirmar conforme o projeto:

- Produto e requisitos.
- Arquitetura e dados.
- Desenvolvimento de servidor.
- Desenvolvimento de interface.
- Qualidade e testes.
- Plataforma e infraestrutura.
- Segurança, quando necessário.

Não inventar quantidade de pessoas, nomes, disponibilidade ou senioridade. O documento deve descrever a capacidade necessária e indicar o que ainda depende de informação.

#### `plano/fases.md`

Seções recomendadas:

1. Estratégia de entrega.
2. Critérios de priorização.
3. Fases propostas.
4. Objetivos e entregáveis de cada fase.
5. Funcionalidades incluídas.
6. Dependências entre fases e funcionalidades.
7. Equipes envolvidas.
8. Critérios de entrada e saída.
9. Riscos e bloqueios.
10. Caminho crítico, quando puder ser identificado.
11. Marcos de validação.
12. Datas e durações, somente quando houver dados suficientes.

Uma fase não deve ser definida apenas pelo volume de funcionalidades. Deve considerar pré-requisitos técnicos, valor de negócio, riscos, integrações e dependências.

#### `plano/tarefas/historias-de-usuario.md`

Modelo por história:

```markdown
## HIST-001 — [Título]

**Origem:** REQ-001
**Prioridade:** Alta
**Ator/persona:** [Ator]
**Estado:** Rascunho

### História

Como [ator], quero [capacidade], para [benefício].

### Critérios de aceitação — resumo

- CA-001: [resultado observável principal].
- CA-002: [resultado alternativo ou exceção relevante].

**Especificação detalhada:** [caminho de `criterios-de-aceitacao.md`, quando existir].

> Regra de fonte única: quando a história tiver uma especificação própria, os cenários completos ficam em `criterios-de-aceitacao.md`; este backlog mantém apenas um resumo e o link. Para histórias pequenas sem especificação própria, os critérios completos podem permanecer aqui.

### Regras de negócio

- ...

### Restrições e exceções

- ...

### Dependências

- ...

### Questões em aberto

- ...
```

Critérios de aceitação devem ser observáveis e verificáveis. Evitar termos vagos como “rápido”, “simples”, “seguro” ou “intuitivo” sem uma definição verificável.

#### `plano/tarefas/epicos.md`

Modelo por épico:

```markdown
## EP-001 — [Título]

**Objetivo de negócio:** ...
**Valor esperado:** ...
**Prioridade:** Alta
**Fase proposta:** Fase 1
**Estado:** Rascunho

### Contexto

...

### Histórias relacionadas

- HIST-001
- HIST-002

### Funcionalidades previstas

- FUNC-001
- FUNC-002

### Critérios de conclusão do épico

- ...

### Dependências e riscos

- ...
```

Épicos devem representar capacidades ou resultados relevantes, não agrupamentos arbitrários de tarefas técnicas.

#### `plano/tarefas/funcionalidades.md`

Modelo por funcionalidade:

```markdown
## FUNC-001 — [Título]

**Épico:** EP-001
**Prioridade:** Alta
**Fase proposta:** Fase 1
**Equipe responsável:** Desenvolvimento de servidor
**Estado:** Rascunho

### Objetivo

...

### Histórias relacionadas

- HIST-001

### Requisitos de origem

- REQ-001

### Requisitos funcionais relacionados

- RF-001

### Requisitos não funcionais relacionados

- RNF-001

### Entidades envolvidas

- ...

### Escopo

- ...

### Fora do escopo

- ...

### Dependências

- FUNC-002

### Critérios de aceitação

- ...

### Riscos e dúvidas

- ...
```

Uma funcionalidade deve ter escopo coerente, valor identificável, critérios de aceitação e tamanho adequado para possuir uma especificação e um ciclo de implementação próprios.

#### `plano/rastreabilidade.md`

Deve reunir tabelas de ligação entre:

- Fontes originais e requisitos extraídos.
- Requisitos e histórias.
- Histórias e épicos.
- Épicos e funcionalidades.
- Funcionalidades e decisões arquiteturais.
- Funcionalidades e fases/equipes.
- Funcionalidades e especificações individuais.
- Requisitos e critérios de verificação.

Exemplo:

| Requisito de origem | História | Épico | Funcionalidade | Fase |
|---|---|---|---|---|
| REQ-001 | HIST-001, HIST-002 | EP-001 | FUNC-001 | Fase 1 |
| REQ-002 | HIST-003 | EP-001 | FUNC-002 | Fase 1 |
| REQ-003 | HIST-004 | EP-002 | FUNC-003 | Fase 2 |

A tabela é um índice de rastreabilidade, não uma segunda fonte de verdade. Os documentos específicos permanecem como referência completa.
### Hierarquia do backlog

A ordem de geração dos documentos é:

```text
Requisitos e diagnóstico
          |
          v
Histórias de usuário
          |
          v
Agrupamento em épicos
          |
          v
Decomposição em funcionalidades
```

A estrutura conceitual do backlog é:

```text
EP-001 — Épico
  ├── FUNC-001 — Funcionalidade
  ├── FUNC-002 — Funcionalidade
  └── FUNC-003 — Funcionalidade

HIST-001 — História de usuário
HIST-002 — História de usuário
HIST-003 — História de usuário

As funcionalidades se relacionam com as histórias que atendem.
A relação pode ser muitos-para-muitos, quando justificada.
```

Para evitar confusão:

- O épico agrupa funcionalidades relacionadas a uma capacidade de negócio.
- A funcionalidade representa uma capacidade entregável que terá especificação própria.
- A história representa uma necessidade ou resultado desejado pelo usuário.
- A tarefa representa trabalho técnico necessário para implementar uma funcionalidade.
- Uma história não deve ser automaticamente tratada como tarefa.
- Uma funcionalidade pode atender várias histórias.
- Uma história pode exigir mais de uma funcionalidade.
### Modelo de dados do backlog e regras de decomposição

#### Vocabulário e hierarquia recomendada

Este framework mantém três perspectivas relacionadas, mas diferentes:

- **História de usuário (`HIST-xxx`):** necessidade, objetivo ou resultado observável do ponto de vista de um ator.
- **Épico (`EP-xxx`):** capacidade ou objetivo de negócio amplo que agrupa trabalho relacionado.
- **Funcionalidade (`FUNC-xxx`):** recorte de produto delimitado, implementável e especificável no ciclo SDD.

A **ordem de geração dos arquivos** continua sendo `historias-de-usuario.md` → `epicos.md` → `funcionalidades.md`, porque o agente primeiro extrai necessidades, depois identifica agrupamentos de valor e, por fim, define recortes de entrega.

A **relação conceitual** a registrar será:

```text
ÉPICO
 ├── FUNCIONALIDADE A ── atende HIST-001 e HIST-002
 ├── FUNCIONALIDADE B ── atende HIST-002 e HIST-003
 └── FUNCIONALIDADE C ── atende HIST-004
```

Uma história pode ser atendida por mais de uma funcionalidade, e uma funcionalidade pode atender mais de uma história. Isso deve ser justificado no mapeamento. A relação não é obrigatoriamente uma árvore perfeita.

**Atenção à prática do mercado:** alguns métodos tratam épicos como agrupamentos de histórias diretamente, sem uma camada intermediária de funcionalidades. O GitScrum, por exemplo, apresenta técnicas de decomposição de épicos diretamente em histórias. Portanto, `FUNC` é uma camada adotada por este framework porque cada funcionalidade terá especificação SDD própria; ela não deve ser criada quando apenas duplicar uma história.

#### Quando usar a camada de funcionalidade

| Situação | Recomendação |
|---|---|
| Projeto pequeno com poucas histórias | Manter o arquivo `funcionalidades.md`, mas permitir relação 1:1 ou marcar a camada como não necessária, com justificativa |
| Projeto médio com várias histórias relacionadas | Usar funcionalidades como recortes de produto especificáveis e entregáveis |
| Produto grande com vários domínios | Agrupar funcionalidades por domínio e épico; manter dependências entre domínios explícitas |
| Épico composto por histórias que já são entregáveis independentes | Não inventar um nível intermediário; uma funcionalidade pode corresponder a uma história ou ser dispensada |
| Item puramente técnico sem usuário direto | Registrar como trabalho técnico habilitador, débito técnico, pesquisa ou tarefa de engenharia; não forçar uma história artificial |

#### Técnicas de decomposição de épicos

O especialista em backlog deve escolher a técnica que melhor representa o domínio. Não aplicar a mesma técnica a todos os épicos.

| Técnica | Usar quando | Exemplo ilustrativo |
|---|---|---|
| Por etapas do fluxo | O valor ocorre ao longo de um processo | Carrinho → endereço → pagamento → confirmação |
| Por tipo de usuário | Personas ou permissões mudam o comportamento | Cliente, operador, administrador |
| Por regra de negócio | Regras têm comportamentos independentes | Desconto percentual, fixo, cumulativo |
| Por operação de dados | CRUD é o principal recorte real de valor | Criar, consultar, atualizar, excluir |
| Por caminho principal e exceções | O sucesso e as falhas possuem tratamentos relevantes | Pagamento aprovado, recusado, timeout, duplicado |
| Por plataforma/canal | O comportamento muda substancialmente por ambiente | Web, iOS, Android, tablet |
| Por variação de dados | Diferentes conjuntos de dados geram capacidade distinta | Relatório de um projeto, múltiplos projetos, período customizado |
| Por interface de integração | Há superfícies e contratos diferentes | Configuração de integração, API, webhook, importação em lote |
| Por nível de acesso | Ações dependem de papéis ou escopos | Visualizar, editar, aprovar, administrar |
| Por estágio de maturidade | Uma capacidade pode evoluir progressivamente | MVP manual, automação parcial, automação completa |

#### Fatiamento vertical versus horizontal

Preferir histórias ou funcionalidades que atravessem as camadas necessárias para entregar um resultado verificável ao usuário. Evitar organizar o backlog como sequências sem valor isolado, por exemplo:

**Decomposição horizontal a evitar como backlog de produto:**
- criar tabelas;
- construir API;
- construir tela;
- adicionar validação.

Esses itens podem ser tarefas técnicas internas de uma fatia vertical, mas não são necessariamente histórias de usuário independentes.

**Fatiamento vertical preferível:**
- permitir cadastro por e-mail, incluindo formulário, validação, API, persistência e retorno observável;
- depois acrescentar confirmação de e-mail;
- depois permitir recuperação de acesso.

A ordem pode ter dependências técnicas, mas cada recorte deve oferecer um incremento demonstrável e verificável sempre que possível.

#### Critérios INVEST para histórias

Cada história deve ser avaliada quanto a:

- **Independente:** pode ser desenvolvida e demonstrada sem dependências desnecessárias?
- **Negociável:** descreve necessidade e resultado, sem prescrever prematuramente a implementação?
- **Valiosa:** entrega benefício claro para usuário ou negócio?
- **Estimável:** há informação suficiente para o time estimar?
- **Pequena:** cabe em um ciclo de entrega adequado ao time?
- **Testável:** existe critério objetivo para verificar conclusão?

O agente deve registrar `APROVADA`, `PRECISA DE REFINAMENTO` ou `NÃO É HISTÓRIA` para cada item. A estimativa final deve ser validada pela equipe; o agente não deve fingir consenso do time.

#### Critérios para dividir ou combinar histórias

**Dividir quando:**
- há múltiplos atores com objetivos diferentes;
- existem muitas regras independentes;
- o item não cabe no ciclo de entrega;
- não é possível estimar com confiança;
- os critérios de aceitação acumulam muitos fluxos independentes;
- existe um caminho principal e exceções que podem ser entregues progressivamente;
- a história depende de uma sequência longa de “e depois”.

**Combinar quando:**
- os itens isolados não produzem valor ou não podem ser verificados;
- os itens são etapas técnicas inseparáveis de uma mesma capacidade;
- a separação cria dependências artificiais ou overhead sem benefício.

Não combinar apenas para reduzir a quantidade de linhas no backlog.

#### Diferenciar história, funcionalidade, tarefa, pesquisa e débito técnico

| Tipo | Pergunta respondida | Exemplo |
|---|---|---|
| História | Qual resultado um usuário precisa? | Como cliente, quero recuperar meu acesso |
| Funcionalidade | Qual capacidade de produto será especificada e entregue? | Recuperação de acesso |
| Tarefa | Qual trabalho verificável precisa ser feito? | Implementar endpoint de solicitação de recuperação |
| Pesquisa técnica | Qual incerteza precisa ser investigada? | Avaliar limites do provedor de e-mail |
| Débito técnico | Qual problema interno aumenta custo, risco ou atrito? | Remover duplicação crítica no serviço de autenticação |
| Correção de defeito | Qual comportamento existente está incorreto? | Corrigir cálculo do total em pedidos com desconto |
### Práticas de escrita, refinamento e planejamento do backlog

#### Modelo de história com INVEST e critérios verificáveis

Histórias devem conter papel/ator, objetivo e benefício. Critérios de aceitação devem expressar resultados observáveis e cobrir caminho principal, validações, permissões e exceções relevantes.

Formato recomendado:

```markdown
## HIST-001 — [Título orientado ao resultado]

**Estado:** Rascunho | Em refinamento | Pronta | Em andamento | Concluída
**Prioridade:** Crítica | Alta | Média | Baixa
**Ator/persona:** [Quem recebe o valor]
**Origem:** REQ-001
**Épico:** EP-001
**Funcionalidades relacionadas:** FUNC-001
**Estimativa:** Não estimada | [estimativa validada pelo time]
**Tamanho:** PP | P | M | G | GG (provisório, se necessário)

### História
Como [ator], quero [objetivo/capacidade], para [benefício/valor].

### Contexto
[Contexto necessário para entender a necessidade.]

### Critérios de aceitação — resumo
- CA-001: [resultado observável principal].
- CA-002: [resultado alternativo ou exceção relevante].

**Especificação detalhada:** [caminho para `criterios-de-aceitacao.md` ou indicar que os cenários completos permanecem neste documento].

> Se existir `criterios-de-aceitacao.md` na pasta da história, esse arquivo é a fonte canônica dos cenários detalhados. Não copiar o mesmo Gherkin para o backlog, requisitos da funcionalidade e especificação da história. Os outros artefatos devem referenciar os IDs CA correspondentes.

### Regras de negócio
- RN-001: ...

### Permissões e restrições
- ...

### Dados envolvidos
- Entidades: ...
- Campos relevantes: ...

### Dependências
- Bloqueia: ...
- Bloqueada por: ...

### Fora de escopo
- ...

### Questões em aberto
- DUV-001: ...

### Avaliação INVEST
- [ ] Independente
- [ ] Negociável
- [ ] Valiosa
- [ ] Estimável
- [ ] Pequena
- [ ] Testável

**Resultado do refinamento:** Aprovada | Precisa de refinamento | Não é história
**Observações do refinamento:** ...
```

#### Critérios de aceitação: regras de qualidade

**Bom critério:** define cenário, ação e resultado esperado, com dados ou limites concretos quando disponíveis.

**Critério insuficiente:** “O sistema deve funcionar corretamente”, “a tela deve ser intuitiva” ou “a API deve ser rápida”.

Quando houver requisito quantitativo, utilizar valor, unidade, população, condição e método de medição. Se a fonte não trouxer o valor, registrar a decisão pendente em vez de inventar o limite.

Para regras de sistema que precisam orientar implementação, o agente pode utilizar EARS nos requisitos funcionais da especificação. Gherkin/Dado-Quando-Então é adequado para cenários de aceitação. Os dois formatos podem coexistir, pois cumprem funções distintas.

#### Modelo de épico

```markdown
## EP-001 — [Nome da capacidade]

**Estado:** Rascunho | Em refinamento | Aprovado | Em andamento | Concluído
**Prioridade:** Crítica | Alta | Média | Baixa
**Fase proposta:** Fase 1
**Domínio:** [Domínio de negócio]
**Responsável de produto:** A definir

### Problema ou oportunidade
[Qual necessidade ampla está sendo tratada?]

### Resultado esperado
[Qual mudança de comportamento, capacidade ou resultado de negócio deve ocorrer?]

### Valor para o usuário/negócio
[Por que vale entregar esse conjunto?]

### Indicadores de sucesso
- Indicador: [nome]
- Medição atual: [valor ou desconhecido]
- Meta: [valor ou pendente de decisão]

### Histórias relacionadas
- HIST-001 — [título]
- HIST-002 — [título]

### Funcionalidades relacionadas
- FUNC-001 — [título]
- FUNC-002 — [título]

### Estratégia de decomposição
[Fluxo, persona, regra, operação, caminho/exceção, plataforma, variação de dados ou interface.]

### Fora de escopo
- ...

### Dependências
- ...

### Riscos e dúvidas
- ...

### Critérios de conclusão do épico
- [ ] ...
```

#### Modelo de funcionalidade

```markdown
## FUNC-001 — [Nome orientado à capacidade]

**Estado:** Rascunho | Em refinamento | Pronta para especificação | Em desenvolvimento | Concluída
**Épico principal:** EP-001
**Prioridade:** Crítica | Alta | Média | Baixa
**Fase proposta:** Fase 1
**Equipe/frente:** [Equipe ou A definir]
**Domínio:** [Domínio]
**Estimativa:** Não estimada | [faixa validada]

### Objetivo
[Qual capacidade delimitada será entregue?]

### Valor entregue
[Qual resultado observável será possível após a entrega?]

### Histórias atendidas
- HIST-001
- HIST-002

### Requisitos de origem
- REQ-001
- RF-001
- RNF-001

### Escopo incluído
- ...

### Fora do escopo
- ...

### Fluxos e cenários
- Caminho principal: ...
- Alternativas: ...
- Exceções: ...

### Dados e integrações
- Entidades: ...
- Sistemas externos: ...

### Dependências
- FUNC-002

### Critérios de aceitação da funcionalidade
- ...

### Condições para iniciar a especificação
- [ ] Requisitos e valor compreendidos
- [ ] Questões bloqueadoras resolvidas
- [ ] Dependências identificadas

### Riscos e questões em aberto
- ...
```

#### Modelo de sessão de refinamento

```markdown
# Sessão de refinamento — [Data]

**Participantes:** [nomes/papéis fornecidos]
**Facilitador:** [responsável]
**Itens avaliados:** [IDs]

## Preparação
- [ ] Itens selecionados previamente
- [ ] Prioridade preliminar definida
- [ ] Contexto e valor preparados
- [ ] Dúvidas reunidas
- [ ] Dados, protótipos e contratos disponíveis quando necessários

## Registro por item
### HIST-001 — [Título]
**O que significa?** ...
**Quem é o usuário?** ...
**Qual valor entrega?** ...
**Critérios de aceitação adicionados/alterados:** ...
**Casos de borda:** ...
**Dependências:** ...
**Riscos técnicos:** ...
**Estimativa da equipe:** ...
**Decisão:** Pronta | Refinar depois | Dividir | Combinar | Descartar
**Responsável pela próxima ação:** ...

## Encaminhamentos
- [ ] Atualizar história
- [ ] Atualizar critérios
- [ ] Obter decisão de negócio
- [ ] Realizar pesquisa técnica
- [ ] Reestimar após divisão

## Resultado
- Itens prontos:
- Itens em refinamento:
- Itens removidos/obsoletos:
- Decisões pendentes:
```

#### Modelo de backlog saudável por horizonte

Manter três níveis de detalhe:

| Horizonte | Conteúdo | Detalhamento esperado |
|---|---|---|
| Próximas entregas (aprox. 2–3 sprints, quando a equipe usa sprints) | Itens candidatos a execução | Critérios detalhados, estimativa revisada pela equipe, dependências e Definition of Ready |
| Próximo horizonte | Itens prováveis | Descrição, valor, prioridade preliminar, tamanho aproximado e questões a resolver |
| Futuro/ideias | Oportunidades não comprometidas | Título, hipótese, origem e motivo para manter no estacionamento; não exigir estimativa detalhada |

Não detalhar todo o backlog antecipadamente. Reavaliar relevância e remover itens obsoletos regularmente.

#### Definição de Pronto (DoR)

DoR define quando um item pode entrar no planejamento de uma sprint ou ciclo de execução. Deve ser adaptada pela equipe.

```markdown
# Definição de Pronto — DoR

Um item só pode ser selecionado para a sprint quando os critérios aplicáveis forem atendidos.

## Clareza
- [ ] Descrição compreensível
- [ ] Usuário/valor ou justificativa técnica identificados
- [ ] Critérios de aceitação específicos e verificáveis
- [ ] Dúvidas bloqueadoras resolvidas

## Tamanho e estimativa
- [ ] Escopo cabe no ciclo de entrega
- [ ] Estimativa foi discutida/validada pela equipe
- [ ] Itens grandes foram divididos

## Dependências
- [ ] Dependências internas identificadas
- [ ] Dependências externas identificadas e planejadas
- [ ] Pré-requisitos disponíveis ou agendados

## Recursos e insumos
- [ ] Protótipos ou especificações disponíveis, se necessários
- [ ] Contratos de API e dados compreendidos, se necessários
- [ ] Ambientes e dados de teste disponíveis, quando necessários
- [ ] Competências necessárias disponíveis ou plano de apoio definido

## Testabilidade
- [ ] Cenários principais definidos
- [ ] Exceções relevantes consideradas
- [ ] Evidência de conclusão identificável

**Exceções autorizadas:** [registrar motivo, pessoa que autorizou, risco e plano para resolver]
```

#### Definição de Concluído (DoD)

DoD não substitui os critérios de aceitação da história. Os critérios definem o que aquela história deve fazer; DoD define o padrão de qualidade comum aplicado ao trabalho.

```markdown
# Definição de Concluído — DoD

## Qualidade do código
- [ ] Implementação atende à especificação aprovada
- [ ] Padrões do projeto respeitados
- [ ] Sem código temporário ou depuração esquecida

## Testes e verificação
- [ ] Testes unitários pertinentes executados
- [ ] Testes de integração pertinentes executados
- [ ] Critérios de aceitação verificados
- [ ] Lint, análise estática e build executados quando aplicáveis

## Revisão e integração
- [ ] Revisão de código concluída
- [ ] Alterações integradas conforme fluxo da equipe
- [ ] Sem conflitos conhecidos com requisitos aprovados

## Documentação e operação
- [ ] Documentação atualizada quando necessário
- [ ] Logs, métricas e alertas incluídos quando necessários
- [ ] Migrações e plano de reversão avaliados quando aplicáveis

## Segurança e acessibilidade
- [ ] Controles de segurança pertinentes verificados
- [ ] Dados sensíveis tratados conforme políticas do projeto
- [ ] Acessibilidade verificada quando aplicável

## Evidências
- [ ] Comandos, resultados e limitações registrados
- [ ] Pendências explicitamente documentadas

## Consolidação das especificações
- [ ] Decisões duradouras foram avaliadas para consolidação.
- [ ] O contexto global foi atualizado ou foi registrado que nenhuma atualização era necessária.
- [ ] Divergências entre código e especificação foram resolvidas ou registradas como pendências impeditivas.

**Aprovação da DoD:** [equipe/papel]
**Versão:** [número]
**Exceções autorizadas:** [registro]
```

Começar com uma DoD curta e aplicável; expandir conforme o risco e a maturidade da equipe. Exceções emergenciais devem deixar registro do que foi adiado e criar ação de acompanhamento.

#### Modelo de planejamento de sprint

Só usar quando a equipe realmente adota sprints e fornece dados de capacidade.

```markdown
# Sprint [Número] — [Nome]

**Período:** [início] a [fim]
**Duração:** [dias úteis]
**Equipe:** [equipe]
**Responsável de produto:** [nome/papel]
**Facilitador:** [nome/papel]

## Objetivo da sprint
[Resultado que orienta a seleção do trabalho.]

## Capacidade
- Pessoas disponíveis:
- Dias úteis por pessoa:
- Férias/ausências:
- Feriados:
- Treinamentos e compromissos:
- Reuniões e suporte estimados:
- Capacidade líquida:
- Buffer para imprevistos:
- Velocidade histórica usada (se existir):
- Capacidade final acordada:

## Itens selecionados
| ID | Título | Prioridade | Estimativa validada | Dependências | Responsável inicial |
|---|---|---|---:|---|---|
| HIST-001 | ... | Alta | ... | ... | ... |

## Riscos e dependências
- ...

## Compromissos e exclusões
- Incluído:
- Não incluído:
- Condições para renegociar escopo:

## Critérios de sucesso
- [ ] Objetivo alcançado
- [ ] Itens que atendem à DoD concluídos
- [ ] Demonstração/validação realizada
```

**Regra:** capacidade deve usar histórico real quando existir. Em equipe nova, utilizar estimativa inicial conservadora e recalibrar após ciclos. Não converter automaticamente horas ideais em pontos de história. Manter buffer acordado; a referência GitScrum apresenta 10–15% como exemplo de margem no planejamento, não como lei universal.
### Avaliação de casos de backlog e escolha da técnica

O agente `especialista-em-backlog` deve aplicar a matriz abaixo antes de decompor cada épico. A técnica escolhida e a justificativa devem constar no próprio épico.

| Caso encontrado | Técnica inicial | Exemplo de decomposição | Cuidado |
|---|---|---|---|
| Processo com começo, meio e fim | Etapas do fluxo | Criar solicitação → acompanhar → aprovar → concluir | Cada etapa precisa entregar valor observável, não ser apenas tela |
| Vários perfis e permissões | Tipo de usuário/nível de acesso | Cliente consulta; operador analisa; administrador configura | Não duplicar histórias se só muda a permissão sem mudar o valor |
| Muitas regras de negócio | Uma regra por recorte coerente | Desconto percentual, desconto fixo, combinação | Preservar invariantes e interações entre regras |
| CRUD predominante | Operação, mas agrupada por valor | Criar e consultar um registro utilizável antes de detalhes avançados | CRUD não deve virar história se operação isolada não tem valor |
| Fluxo com falhas relevantes | Caminho feliz e exceções | Pagamento aprovado; recusado; timeout; duplicidade; estorno | Priorizar risco e impacto; não deixar segurança para o fim |
| Várias plataformas | Plataforma/canal quando comportamento difere | Web responsiva; aplicativo móvel | Evitar duplicar histórias idênticas sem necessidade |
| Relatórios e consultas complexas | Variação de dados/filtros/escopo | Relatório simples; múltiplos projetos; intervalo customizado; exportação | Critérios de desempenho e volume precisam de limites aprovados |
| Integração externa | Interface/contrato e modo de falha | Configurar; enviar; receber webhook; reprocessar | Incluir timeout, retry, idempotência, autenticação e observabilidade conforme o caso |
| Funcionalidade técnica por camadas | Fatiamento vertical | Um fluxo ponta a ponta de valor, com tarefas em UI/API/dados | Não criar histórias que só entregam banco ou tela sem capacidade utilizável |
| Feature grande, pouco conhecida | Pesquisa e protótipo controlado antes de comprometer | Spike para provar risco; depois histórias de produto | Não apresentar estimativa como compromisso antes de reduzir incerteza |
| Migração de dados | Por conjunto/etapa e critério de reconciliação | Amostra piloto; lote inicial; sincronização; corte; reversão | Integridade e recuperação são parte do escopo, não tarefas opcionais |
| Segurança e privacidade | Requisitos transversais e cenários de abuso | Permissão por papel, isolamento de dados, auditoria | Não agrupar segurança apenas como uma feature tardia |

#### Exemplo: épico de checkout

**Técnica recomendada:** fluxo do usuário + exceções relevantes.

Possíveis histórias (exemplo):
- HIST-001: visualizar e revisar os itens do carrinho;
- HIST-002: informar endereço de entrega;
- HIST-003: selecionar forma de pagamento;
- HIST-004: confirmar pedido;
- HIST-005: receber confirmação;
- HIST-006: entender por que um pagamento foi recusado;
- HIST-007: evitar criação duplicada em reenvio/timeout, conforme regra de negócio aprovada.

Funcionalidades podem agrupar recortes implementáveis, por exemplo `FUNC-001 — Finalização de pedido` e `FUNC-002 — Tratamento e recuperação de falha de pagamento`. A decomposição real depende de integrações, regras e arquitetura confirmadas.

#### Exemplo: épico de gerenciamento de usuários

**Técnica recomendada:** ator/permissão + operações + fluxo.

Avaliar separadamente:
- cadastro e validação;
- autenticação;
- atualização de perfil;
- recuperação de acesso;
- administração e desativação de contas;
- papéis e permissões.

Não assumir que todo CRUD é uma história. Uma operação pode ser uma tarefa interna ou parte de uma história maior, dependendo do valor e da possibilidade de demonstração.

#### Exemplo: épico de relatórios

**Técnica recomendada:** variação de dados + filtros + formatos de saída.

Avaliar:
- um registro versus consolidação de múltiplos registros;
- filtros de período e dimensão;
- paginação/volume;
- exportação;
- permissões e isolamento;
- consistência e atualização dos dados.

Não definir metas de tempo de resposta sem volume e percentil aprovados. Registrar os dados necessários para uma decisão técnica.

#### Exemplo: integração com API externa

**Técnica recomendada:** fatiar por contrato e fluxo de falha.

Avaliar:
- configuração e credenciais;
- chamada de saída;
- recepção de eventos/webhooks;
- validação de assinatura/autenticidade;
- idempotência;
- timeout e retries;
- tratamento de indisponibilidade;
- reconciliação e reprocessamento;
- monitoramento e alertas.

A integração não pode ser considerada concluída apenas porque o caminho de sucesso funciona em ambiente local.
### Refinamento contínuo e planejamento de sprint

#### O refinamento é contínuo

O backlog não deve ser produzido uma vez e tratado como imutável. A skill `/montar-backlog` cria a primeira estrutura; o refinamento contínuo melhora itens próximos de execução, atualiza prioridades e remove itens que perderam sentido.

Atividades recorrentes:
- esclarecer descrição, valor e critérios;
- identificar cenários de borda;
- identificar dependências internas e externas;
- estimar com a equipe quando houver informação suficiente;
- dividir itens grandes;
- combinar itens sem valor isolado;
- remover ou arquivar itens obsoletos;
- manter alguns ciclos futuros prontos, sem detalhar todo o futuro.

O agente pode preparar uma pauta e sugerir perguntas, mas não deve representar consenso de estimativa que não ocorreu.

#### Modelo de prontidão para sprint

Uma história está pronta para ser considerada em uma sprint quando tem clareza, valor, critérios de aceitação, tamanho compatível com o ciclo, dependências identificadas e entendimento compartilhado. Se faltar informação, deve permanecer em refinamento ou virar pesquisa técnica delimitada.

#### Planejamento de capacidade

Calcular capacidade com:
1. dias úteis e duração do ciclo;
2. pessoas efetivamente disponíveis;
3. férias, feriados, treinamento e outras ausências;
4. tempo de suporte, reuniões e atividades não relacionadas diretamente à entrega;
5. histórico de entrega real, se houver;
6. margem para imprevistos acordada pela equipe.

A capacidade teórica em pessoa-dia não equivale automaticamente a pontos. Pontos são relativos à calibração da equipe. Não misturar estimativas de horas de implementação com pontos de história.

#### Tamanho da história versus tamanho da tarefa

As referências consultadas sugerem histórias idealmente com 1–3 dias de trabalho para caber em uma sprint, enquanto o livro SDD de Felipe Fontoura sugere tarefas de implementação de 2–4 horas em projetos médios. Essas referências tratam de níveis diferentes:

- história: unidade de valor de produto, estimada pela equipe;
- funcionalidade: unidade de capacidade que recebe especificação SDD;
- tarefa: unidade de implementação verificável, decomposta a partir do desenho técnico.

Os números são referências iniciais, não regras universais. Ajustar conforme o time, o tipo de trabalho e o risco.

#### Antipadrões que o agente deve detectar

- histórias sem ator, valor ou critérios;
- critérios vagos ou subjetivos;
- épicos usados como listas de tarefas;
- funcionalidades que duplicam histórias sem acrescentar uma fronteira de especificação útil;
- tarefas técnicas apresentadas como histórias de usuário;
- decomposição por camadas sem entrega vertical de valor;
- estimar itens grandes demais sem dividir ou pesquisar;
- tentar detalhar todo o backlog até o mesmo nível;
- selecionar para sprint itens com dependências bloqueadoras;
- comprometer mais trabalho que a capacidade histórica permite;
- confundir `Concluído` com “código escrito” sem revisão e evidência;
- ignorar bugs, suporte, risco e débito técnico;
- manter itens obsoletos indefinidamente.
### Estados e gates de aprovação

O estado é uma fonte de verdade do processo. A existência de um documento não indica aprovação.

#### Estado geral do planejamento

O arquivo `plano/.status` contém um único estado atual por vez. Os valores previstos são:

```text
documentos:pendentes
documentos:em-analise
diagnostico:em-revisao
diagnostico:aprovado
planejamento:rascunho
planejamento:em-revisao
planejamento:aprovado
backlog:rascunho
backlog:em-revisao
backlog:aprovado
github:pendente
github:sincronizando
github:sincronizado
```

Transições inválidas devem ser recusadas. Por exemplo, não é permitido passar para `backlog:rascunho` sem `planejamento:aprovado`.

#### Estado por funcionalidade

Cada diretório de funcionalidade contém seu próprio `.status`:

```text
requisitos:rascunho
requisitos:em-revisao
requisitos:aprovados
desenho:rascunho
desenho:em-revisao
desenho:aprovado
tarefas:rascunho
tarefas:em-revisao
tarefas:aprovadas
implementacao:em-andamento
implementacao:concluida
revisao:em-andamento
revisao:aprovada
consolidacao:pendente
consolidacao:em-revisao
consolidacao:aprovada
consolidacao:sem-atualizacao
concluida
```

#### Regras dos gates

- O agente pode criar ou atualizar rascunhos.
- O agente pode executar auditorias e apresentar recomendações.
- Somente uma ação humana explícita pode registrar aprovação.
- Se o estado estiver ausente, inválido ou inconsistente, o agente deve parar.
- Nenhum desenho técnico específico pode ser aprovado antes dos requisitos correspondentes.
- Nenhuma tarefa pode ser aprovada antes do desenho técnico.
- Nenhuma implementação pode iniciar antes de `tarefas:aprovadas`.
- `implementacao:concluida` não significa que a entrega está concluída; a revisão independente ainda precisa ser aprovada.
- Depois de `revisao:aprovada`, a entrega entra em `consolidacao:pendente`.
- A consolidação deve ser verificada mesmo quando não houver atualização global a fazer.
- Se nenhuma decisão global duradoura precisar ser atualizada, Sammy registra `consolidacao:sem-atualizacao`, com justificativa e evidências; não é necessária uma aprovação semântica para uma alteração inexistente.
- Se houver atualização semântica de contexto global, ela permanece em `consolidacao:em-revisao` até aprovação humana e só então passa a `consolidacao:aprovada`.
- A entrega só pode chegar a `concluida` depois da Definição de Concluído e de um dos resultados válidos: `consolidacao:aprovada` ou `consolidacao:sem-atualizacao`, sem bloqueios pendentes.
- Uma alteração aprovada em requisitos pode exigir revisão do desenho e das tarefas dependentes.
- Não alterar silenciosamente documentos já aprovados.
- Toda mudança relevante deve ser versionada no Git.

#### Mudanças de escopo

Quando uma etapa posterior revelar uma lacuna em documento aprovado:

1. Interromper a parte afetada do trabalho.
2. Identificar quais requisitos, decisões, histórias, épicos, funcionalidades ou tarefas são impactados.
3. Propor a alteração nos documentos de origem.
4. Explicar o impacto e as alternativas.
5. Solicitar aprovação humana.
6. Atualizar os artefatos derivados somente depois da aprovação.
7. Registrar a mudança na rastreabilidade e no histórico de decisões.
### Auditoria e validação

O framework combina validações determinísticas e avaliação semântica.

#### Verificações determinísticas por script

Um ou mais scripts Python devem validar:

- Existência dos arquivos obrigatórios.
- Formato dos identificadores.
- IDs duplicados.
- Referências a IDs inexistentes.
- Funcionalidades sem épico.
- Épicos sem funcionalidades.
- Histórias sem critérios de aceitação.
- Dependências circulares.
- Estados inválidos.
- Transições de estado proibidas.
- Mapeamento local do GitHub com campos obrigatórios.
- Divergência entre identificadores dos documentos e IDs publicados.

#### Auditoria semântica

O agente `auditor-de-planejamento` verifica:

- Se os documentos realmente refletem as fontes.
- Se houve omissão ou interpretação incorreta de requisitos.
- Se a arquitetura oferece suporte às funcionalidades propostas.
- Se o modelo de dados foi interpretado corretamente.
- Se há sobreposição desnecessária entre funcionalidades.
- Se a decomposição em épicos faz sentido para o negócio.
- Se as fases respeitam as dependências técnicas e de produto.
- Se as equipes propostas cobrem as competências necessárias.
- Se os critérios de aceitação são claros e verificáveis.
- Se existem suposições indevidamente apresentadas como fatos.

#### Formato do relatório

Cada achado deve incluir:

```markdown
### ACH-001 — [Título do achado]

**Severidade:** Bloqueador | Alta | Média | Baixa
**Documento:** plano/arquitetura.md
**Referência:** estrutura de diretórios → regras para a estrutura
**Tipo:** Omissão | Contradição | Ambiguidade | Rastreabilidade

**Problema:**
Descrição objetiva.

**Evidência:**
Fonte, requisito, ID ou trecho relacionado.

**Impacto:**
Consequência para produto, arquitetura ou implementação.

**Recomendação:**
Ação proposta, sem aprovar a alteração.
```

Resultado geral:

- `APROVÁVEL`: não há bloqueios conhecidos.
- `APROVÁVEL COM RESSALVAS`: há pontos que precisam ser explicitamente aceitos ou acompanhados.
- `NÃO APROVÁVEL`: há bloqueios ou inconsistências que impedem avançar.

O auditor não substitui a leitura humana. Seu relatório é um instrumento para orientar a revisão.
### Matriz consolidada de comportamento do workflow

| Situação detectada | Ação automática permitida | Ação humana necessária | Gate que deve bloquear |
|---|---|---|---|
| Documentos completos e consistentes | Extrair, cruzar e criar diagnóstico | Revisar diagnóstico | Aprovação do diagnóstico |
| Fonte ilegível ou incompleta | Relatar páginas/trechos afetados e continuar parcialmente | Fornecer fonte legível ou confirmar limite | Diagnóstico aprovado |
| Requisitos contraditórios | Criar achado e alternativas | Escolher regra válida | Planejamento e backlog |
| Modelo de dados sem requisito relacionado | Sinalizar elemento sem justificativa | Confirmar se é legado, infraestrutura ou escopo | Arquitetura/backlog |
| Arquitetura exige tecnologia não especificada | Comparar opções e propor decisão | Aprovar escolha técnica | Aprovação da arquitetura |
| História grande ou vaga | Sugerir divisão e registrar INVEST | Validar divisão, prioridade e estimativa | Backlog pronto |
| Épico pode ser dividido por mais de uma técnica | Comparar técnicas e recomendar uma | Revisar valor e fronteiras | Backlog aprovado |
| Funcionalidade sem critério de aceitação | Sugerir critérios baseados nos requisitos ou marcar lacuna | Resolver lacuna de negócio | Requisitos aprovados |
| Item sem capacidade ou velocidade conhecida | Manter estimativa como pendente/faixa provisória | Equipe validar estimativa | Seleção para sprint |
| Dependência externa sem prazo | Registrar risco e bloqueio | Confirmar fornecedor/contrato/prazo | Fase/sprint afetada |
| Mudança após aprovação | Gerar análise de impacto | Aprovar alteração e revalidar descendentes | Gate afetado |
| GitHub diverge do Git | Mostrar diff e sugerir reconciliação | Resolver conflito | Sincronização |
| Tarefa aprovada e sem ambiguidades | Implementar uma tarefa | Revisar entrega conforme política | Revisão |
| Testes falham | Registrar evidência e investigar | Resolver decisão de especificação se houver lacuna | Conclusão da tarefa |
| Correção urgente de produção | Permitir fluxo emergencial controlado e registrar exceção | Autorizar e revisar pós-incidente | Merge/revisão conforme política emergencial |
### Critérios de qualidade por artefato

Antes de apresentar documentos para aprovação, o agente responsável deve utilizar os critérios abaixo.

#### Diagnóstico
- [ ] Cada afirmação relevante tem origem indicada.
- [ ] Fatos, inferências e propostas estão separados.
- [ ] Páginas ilegíveis ou ausentes foram declaradas.
- [ ] Contradições e lacunas foram registradas.
- [ ] O modelo de dados foi analisado sem inventar semântica.

#### Arquitetura
- [ ] Requisitos arquiteturalmente relevantes estão identificados.
- [ ] Componentes têm responsabilidades claras.
- [ ] Fronteiras e integrações estão descritas.
- [ ] Decisões têm justificativa e alternativas.
- [ ] Requisitos relevantes têm mapeamento arquitetural.
- [ ] Restrições não aprovadas estão rotuladas como propostas.

#### Equipes
- [ ] Responsabilidades não estão duplicadas sem justificativa.
- [ ] Competências são derivadas das entregas.
- [ ] Pessoas e capacidades não foram inventadas.
- [ ] Aprovações e dependências são claras.

#### Fases
- [ ] Cada fase tem objetivo e critério de saída.
- [ ] Dependências respeitam a ordem técnica e de negócio.
- [ ] Datas não foram inventadas.
- [ ] Fase não foi confundida com sprint.
- [ ] Riscos e bloqueios estão visíveis.

#### Histórias
- [ ] Ator, objetivo e benefício existem.
- [ ] Critérios são verificáveis.
- [ ] INVEST foi avaliado.
- [ ] Casos negativos relevantes foram considerados.
- [ ] Dependências e origem estão rastreáveis.

#### Épicos
- [ ] Representam objetivo/capacidade ampla de negócio.
- [ ] Agrupam histórias coerentes.
- [ ] A técnica de decomposição está justificada.
- [ ] Valor e critério de conclusão são identificáveis.

#### Funcionalidades
- [ ] Possuem fronteira e valor entregável.
- [ ] Não duplicam escopo sem justificativa.
- [ ] Estão ligadas a épicos e histórias.
- [ ] Têm requisitos de origem e critérios de aceitação.
- [ ] Podem receber uma especificação SDD própria.

#### Tarefas
- [ ] Derivam do desenho aprovado.
- [ ] São pequenas e verificáveis.
- [ ] Cobrem requisitos Must.
- [ ] Dependências são explícitas.
- [ ] Critérios e comandos de verificação existem.
- [ ] Estimativas não são apresentadas como consenso sem validação da equipe.

#### GitHub
- [ ] Cada item tem identificador local único.
- [ ] O mapeamento remoto é válido.
- [ ] A publicação foi simulada antes da execução.
- [ ] O processo é idempotente.
- [ ] Conflitos não foram sobrescritos.
- [ ] O Project reflete o estado aprovado no Git.
