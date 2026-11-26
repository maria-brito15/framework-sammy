<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 509–979. -->

> **Nesta página:** Triagem inteligente, porte, rigor, autonomia, granularidade, confiança, seleção de agentes e reavaliação.

[← Voltar ao índice da documentação](../README.md)

---

### Triagem inteligente: escolher e adaptar a execução automaticamente

A triagem é um mecanismo operacional, não uma classificação decorativa. Seu resultado determina quais etapas serão executadas, quais agentes serão chamados, quais templates serão carregados, que verificações serão realizadas e em quais pontos Sammy deve pedir aprovação.

A avaliação acontece em camadas. Sammy não precisa conhecer o projeto inteiro para começar a trabalhar, mas também não pode transformar desconhecimento em falsa certeza.

#### Quando a triagem acontece

| Momento | Objetivo | Resultado |
|---|---|---|
| **Triagem inicial** | Identificar o tipo de solicitação, o estado do repositório e riscos evidentes antes de iniciar trabalho caro | Classificação provisória e primeira estratégia |
| **Triagem após ingestão** | Reavaliar com requisitos, modelo de dados, documentação e código disponíveis | Perfil-base do projeto e plano de execução aprovado para rascunhos |
| **Triagem local** | Avaliar a funcionalidade, história, bug, migração ou tarefa específica | Rigor e granularidade locais |
| **Reavaliação por evento** | Reagir a uma mudança que altere escopo, risco, dependência ou evidência | Ajuste seletivo da estratégia e invalidação do que foi afetado |

A triagem inicial deve ser rápida. A avaliação completa ocorre depois da leitura das fontes. Sammy deve registrar o que é provisório e atualizar a estratégia quando surgirem evidências melhores.

#### Dimensões de avaliação de risco e complexidade

Sammy atribui nota de 0 a 2 às sete dimensões abaixo. Cada nota deve ter evidência e justificativa. `DESCONHECIDO` é um estado permitido e não equivale a zero.

| Dimensão | 0 — Baixa | 1 — Moderada | 2 — Alta |
|---|---|---|---|
| Complexidade de domínio | Poucas regras e fluxos | Vários fluxos relacionados | Estados complexos ou múltiplos domínios |
| Dados e segurança | Dados pouco sensíveis | Dados pessoais ou permissões usuais | Dados sensíveis/financeiros ou controles críticos |
| Integrações | Nenhuma ou simples | Algumas integrações | Integrações externas críticas, assíncronas ou numerosas |
| Incerteza | Fontes claras e coerentes | Lacunas limitadas | Contradições, mudanças frequentes ou escopo pouco definido |
| Complexidade técnica | Solução conhecida e simples | Múltiplas camadas ou tecnologias | Concorrência, distribuição, migração ou alta disponibilidade |
| Escala organizacional | Uma pessoa ou equipe pequena | Mais de uma frente | Múltiplas equipes, fornecedores ou aprovações |
| Impacto de falha | Baixo e reversível | Interrupção ou retrabalho | Perda de dados, prejuízo, exposição ou indisponibilidade crítica |

A soma possível é de 0 a 14. A pontuação serve para selecionar a profundidade do processo; não representa probabilidade matemática de incidente.

Os limites 0–4, 5–9 e 10–14 são **valores iniciais de calibração**. Devem ser testados nos casos do Apêndice F e ajustados com evidências do piloto. Não são padrões universais nem substituem políticas de segurança, arquitetura ou conformidade do projeto.

#### Avaliação do porte

O porte é calculado separadamente da pontuação de rigor. Sammy avalia pelo menos:

- quantidade e independência dos domínios de negócio;
- amplitude dos fluxos e capacidades do produto;
- quantidade e acoplamento dos componentes/sistemas;
- quantidade e criticidade das integrações;
- dependências entre equipes e áreas;
- necessidade de coordenação de entregas e implantação.

Classificação:

| Porte | Regra prática | Consequência para o planejamento |
|---|---|---|
| Pequeno | Um domínio delimitado, poucas integrações e coordenação simples | Artefatos enxutos; uma equipe ou responsável; fases simples |
| Médio | Vários módulos relacionados, integrações ou frentes de trabalho | Arquitetura e backlog estruturados; dependências e responsabilidades explícitas |
| Grande | Múltiplos domínios/sistemas/equipes com dependências cruzadas | Planejamento por domínios, contratos, integração, governança e implantação coordenada |

Não classificar porte pelo número de páginas, requisitos ou histórias isoladamente. Reavaliar depois da decomposição se o escopo real contradisser a estimativa inicial.

#### Condições críticas que elevam o rigor

Uma condição crítica eleva o rigor local para, no mínimo, rigoroso, independentemente da pontuação:

- pagamentos, saldos, cobrança ou movimentação financeira;
- autenticação, autorização ou isolamento entre clientes/organizações;
- dados pessoais sensíveis ou dados cuja exposição cause dano relevante;
- requisitos regulatórios ou de auditoria;
- migração, exclusão ou transformação de dados com risco de perda;
- concorrência ou idempotência em operações críticas;
- indisponibilidade com impacto operacional ou financeiro elevado;
- integrações externas que possam causar efeitos irreversíveis.

A lista é extensível e deve ser configurável por projeto. Um rótulo crítico exige identificar o controle concreto necessário; não deve gerar automaticamente todos os documentos possíveis.

#### Regra de escolha do rigor

| Pontuação / condição | Rigor selecionado | Comportamento esperado |
|---|---|---|
| 0–4, sem condição crítica e sem incerteza relevante desconhecida | Leve | Contexto afetado, critério verificável, tarefa e verificação proporcional |
| 5–9 ou incerteza que afete decisões importantes | Padrão | Requisitos, desenho proporcional, tarefas, rastreabilidade e auditoria |
| 10–14 ou qualquer condição crítica | Rigoroso | Riscos, decisões formais, cenários negativos, segurança/dados, verificação ampliada e revisão independente |

Se uma dimensão crítica estiver desconhecida e não houver evidência suficiente para descartar risco, Sammy não pode selecionar Leve. Deve selecionar Padrão provisório ou Rigoroso, conforme o impacto potencial, e registrar a pergunta ou evidência necessária para resolver a incerteza.

#### A estratégia tem quatro eixos independentes

A decisão operacional precisa registrar:

1. `porte_projeto`: pequeno, medio ou grande;
2. `rigor_projeto`: leve, padrao ou rigoroso;
3. `autonomia`: somente_rascunhos, controlada ou ampliada;
4. `granularidade`: projeto, dominio_epico, funcionalidade ou historia_tarefa.

Além disso, cada unidade de trabalho recebe `rigor_local`, `granularidade_local` e um conjunto de controles aplicáveis. O rigor do projeto orienta a governança global; não força cada alteração local a produzir a mesma quantidade de documentos. Uma pequena alteração visual em um sistema financeiro pode receber rigor local Leve, desde que não toque dados, segurança ou outros controles críticos. A política global de autenticação, rastreabilidade e revisão continua valendo quando aplicável.

**Regra de composição:** aplicar a união dos controles globais relevantes com os controles selecionados para a unidade local. Não usar uma média que permita que o rigor local remova uma proteção global obrigatória.

#### Como cada nível altera a execução

| Aspecto | Leve | Padrão | Rigoroso |
|---|---|---|---|
| Análise | Examinar o contexto diretamente afetado | Analisar requisitos, dados e dependências | Analisar também ameaças, falhas, impactos e recuperação |
| Documentação | Descrição curta e critérios | História/requisitos e desenho proporcional | Especificação detalhada, riscos e decisões rastreáveis |
| Agentes | Sammy pode resolver sem subagente; chamar especialista só se necessário | Especialistas relevantes + auditor | Especialistas de domínio/dados/segurança + auditor independente |
| Decomposição | Uma ou poucas tarefas verificáveis | Tarefas pequenas, dependências explícitas | Tarefas menores com controles e evidências por risco |
| Validação | Testes focados e lint/build pertinente | Critérios, testes e rastreabilidade | Testes negativos, segurança, integridade, recuperação e revisão independente |
| Aprovação | Revisão proporcional; gate se alterar decisão aprovada | Gates de requisitos, desenho e tarefas conforme aplicável | Gates explícitos e responsáveis especializados quando necessário |
| Evidência | Resultado do teste pertinente | Comandos, resultados e cobertura de critérios | Evidências ampliadas, limitações e riscos residuais |

Os exemplos definem o comportamento mínimo, não uma lista fixa de agentes. Sammy deve evitar chamar agentes só para preencher um organograma.

#### Autonomia é uma política separada

| Modo | Operações locais | Operações remotas |
|---|---|---|
| Somente rascunhos | Leitura e criação de rascunhos em arquivos autorizados | Bloqueadas |
| Controlada | Edição local segura, scripts de validação e testes | Exigem autorização específica ou persistente |
| Ampliada | Execução de tarefas já aprovadas, dentro do escopo | Permitidas somente para ações, destino e limites previamente autorizados |

Nenhum modo permite Sammy aprovar documentos, inventar decisões, ignorar gates, ampliar sua própria autorização ou executar operações destrutivas não previstas.

#### Granularidade e seleção de templates

Sammy seleciona o menor nível que mantenha valor, rastreabilidade e verificação independente. Usa templates de projeto para decisões sistêmicas; de domínio/épico para capacidades relacionadas; de funcionalidade para entrega implementável; de história/tarefa para trabalho pequeno. Não cria uma história, épico ou arquitetura completa para uma correção trivial sem justificativa.

Cada template deve declarar metadados no catálogo: tipo de trabalho aplicável, portes compatíveis, rigor mínimo, condições, dependências, se é obrigatório quando aplicável e verificações associadas. O catálogo é consultado por script com schema validado. Sammy decide a aplicabilidade semântica; o script resolve caminhos, campos obrigatórios e compatibilidade mecânica.

#### Seleção dinâmica de agentes

| Situação | Especialistas normalmente necessários | Quando não chamar |
|---|---|---|
| Análise de PDFs | Analista de requisitos e analista de dados, em paralelo quando há duas fontes distintas | Se a solicitação não envolve documentos ou dados |
| Repositório existente | Analista de repositório + especialistas relevantes | Se não houver código existente para inspecionar |
| Arquitetura ou mudança estrutural | Arquiteto; analista de dados quando persistência for afetada | Mudança pontual sem impacto arquitetural |
| Histórias e épicos | Especialista de produto | Correção técnica sem comportamento de produto novo |
| Fases e equipes | Planejador | Mudança local e isolada |
| Migração ou dados críticos | Analista de dados + arquiteto + auditor; segurança quando pertinente | Alteração sem persistência ou migração |
| Publicação GitHub | Integrador GitHub + validação determinística | Se GitHub estiver desabilitado ou sem autorização |
| Implementação | Implementador, um item aprovado por vez | Antes de tarefas aprovadas |
| Revisão | Revisor em contexto independente | Não substituir validação determinística por opinião do revisor |

Sammy pode combinar papéis em projetos pequenos. A especialização existe para reduzir erros, não para multiplicar chamadas.

#### Reavaliação orientada por eventos

Sammy não deve recalcular toda a estratégia a cada mensagem. Reavalia quando ocorrer evento que possa alterar materialmente risco, escopo, dependência ou saída.

| Evento | Reavaliar | Possível impacto |
|---|---|---|
| Novo documento ou versão de fonte | Cobertura, incerteza e dependências | Reprocessar somente etapas que dependem da fonte |
| Requisito alterado | Escopo, risco, histórias e rastreabilidade | Reabrir aprovações afetadas |
| Entidade ou relação alterada | Modelo de dados, integridade e desenho técnico | Reavaliar funcionalidades que usam os dados |
| Nova integração | Complexidade, falhas e segurança | Elevar rigor local e incluir contratos/testes |
| Regra de permissão adicionada | Segurança e autorização | Aplicar controles de acesso e revisão apropriados |
| Funcionalidade maior que o previsto | Granularidade e dependências | Decompor em unidades independentes |
| Teste ou auditoria falha | Especificação, implementação e risco | Corrigir causa e repetir validação pertinente |
| Equipe ou capacidade muda | Plano de fases e sprint | Replanejar compromisso, sem alterar requisitos automaticamente |
| Incidente ou falha de produção | Impacto, risco e controles | Bloquear avanço inseguro e ampliar investigação |

#### Estabilidade da classificação: evitar oscilações

Para evitar que Sammy altere o perfil a cada pequena mudança:

- **Elevar rigor:** imediatamente quando houver evidência de condição crítica ou risco maior.
- **Manter rigor:** enquanto as evidências permanecerem na mesma faixa ou houver incerteza relevante.
- **Reduzir rigor:** somente em ponto de controle, após a condição que motivou a elevação ter sido resolvida, sem condições críticas abertas e com justificativa registrada.
- **Evitar oscilação:** uma redução de perfil exige evidência estável em duas avaliações consecutivas ou aprovação explícita de uma alteração de política. Essa regra é uma proteção operacional inicial e deve ser calibrada com os casos de avaliação.
- **Nunca rebaixar controles globais:** reduzir rigor local não remove convenções, controles de segurança ou gates já definidos para o projeto.

#### Perguntas e decisões humanas

Sammy interrompe quando a resposta altera regra de negócio, escopo, permissão, retenção de dados, decisão arquitetural relevante, aceitação de risco ou publicação externa não autorizada. Para lacunas de baixo impacto, usa um padrão documentado e reversível, identifica-o como premissa e continua as atividades independentes.

Quando houver várias dúvidas bloqueadoras, apresenta um único pacote com: pergunta, evidência, opções, impacto e recomendação. Não delega a pergunta ao subagente; o subagente devolve a dúvida a Sammy, que conversa com a pessoa usuária.

#### Procedimento operacional do motor adaptativo

1. Identificar tipo de solicitação e contexto do repositório.
2. Ler configurações, políticas globais, estados e manifesto existentes.
3. Fazer triagem inicial rápida e marcar lacunas como desconhecidas.
4. Inventariar e analisar fontes relevantes.
5. Calcular porte e pontuação preliminar com evidências.
6. Identificar condições críticas e aplicar regras de elevação.
7. Selecionar autonomia permitida, sem alterar gates humanos.
8. Definir granularidade global e local.
9. Consultar catálogo e selecionar templates aplicáveis.
10. Selecionar especialistas apenas para atividades que exijam seu conhecimento.
11. Selecionar modelo e nível de esforço por chamada, consultando `politica-de-modelos.yaml`; usar scripts quando a atividade for determinística.
12. Delimitar o contexto enviado e o formato de retorno de cada subagente.
13. Construir grafo de dependências e paralelizar somente etapas independentes.
14. Executar, validar e corrigir automaticamente falhas mecânicas dentro de limites.
15. Reavaliar quando surgir evento relevante.
16. Apresentar pacote de aprovação quando atingir gate humano.
17. Registrar decisão, evidências, hashes, perfil, rota de modelo e próxima etapa segura.

#### Responsabilidade: agente, motor de políticas e scripts

| Componente | Responsabilidade | Não deve fazer |
|---|---|---|
| Sammy | Interpretar evidências, justificar classificação, decidir o fluxo semântico e comunicar decisões | Inventar evidência ou aprovar o próprio trabalho |
| Subagentes | Produzir análises especializadas com escopo e formato definidos | Alterar estados de aprovação ou conversar diretamente com a pessoa usuária |
| Motor de políticas | Aplicar regras, faixas, precedência, controles obrigatórios e seleção de perfis | Decidir regras de negócio |
| Seletor de modelos | Escolher modelo e esforço por tipo de tarefa, com base em política e evidências | Trocar o modelo principal a cada etapa ou ignorar limites de provedor |
| Catálogo de templates | Declarar aplicabilidade, dependências, campos e verificações | Obrigar o uso de todos os modelos |
| Scripts | Calcular pontuação, validar schemas, IDs, hashes, dependências e integridade do manifesto | Fazer julgamento semântico de negócio |
| Auditor | Verificar cobertura, coerência e lacunas em contexto independente | Aprovar artefatos ou introduzir requisitos novos |

#### Gerenciamento adaptativo de modelos, esforço e contexto

Sammy deve administrar o uso dos modelos de forma proporcional à tarefa. O objetivo não é usar sempre o modelo mais barato nem sempre o mais capaz: é evitar gastar capacidade de raciocínio em atividades mecânicas e, ao mesmo tempo, não economizar justamente nas decisões em que um erro custa caro.

**Limite técnico importante:** Sammy é o agente principal de uma sessão do Claude Code, que tem um modelo ativo. A seleção de um modelo diferente para cada trabalho é feita principalmente na delegação aos subagentes, por meio do parâmetro `model` da chamada ao agente ou do campo `model` no frontmatter do subagente. Sammy não deve presumir que consegue trocar silenciosamente o modelo da própria sessão a cada etapa. A troca do modelo da sessão principal é uma operação diferente e pode causar recarga de contexto não armazenado em cache; por isso, não deve ser usada como mecanismo de roteamento de cada tarefa.

A política tem três alavancas distintas:

1. **Escolha do modelo:** define a faixa de capacidade necessária para a tarefa.
2. **Nível de esforço (`effort`):** define quanto trabalho, verificação e raciocínio o modelo deve empregar. Não substitui capacidade do modelo.
3. **Gestão de contexto:** define quais arquivos, histórico, ferramentas e resultados precisam chegar a cada agente.

A ordem recomendada é: primeiro remover trabalho que pode ser resolvido deterministicamente; depois limitar o contexto ao necessário; em seguida escolher o modelo adequado; por último ajustar o esforço. Se um modelo falhar, Sammy deve diagnosticar se faltou contexto, execução, verificação ou capacidade antes de aumentar o modelo.

##### Política inicial de roteamento

Usar aliases (`haiku`, `sonnet`, `opus` e, quando disponível e justificado, `fable`) em vez de fixar versões específicas em todos os arquivos. Os aliases acompanham as versões recomendadas pelo Claude Code, mas a resolução pode variar conforme provedor, conta e disponibilidade. A configuração deve permitir que a pessoa responsável fixe versões quando houver necessidade de reprodutibilidade ou restrição organizacional.

| Tipo de trabalho | Rota inicial | Esforço inicial | Exemplos | Condição para escalar |
|---|---|---|---|---|
| Operação determinística | Não usar modelo | Não aplicável | Hashes, parsing, validação de JSON/YAML, IDs, links, cobertura estrutural, cálculo de dependências, sincronização GitHub | Só chamar modelo se houver interpretação semântica ou ambiguidade |
| Tarefa curta e delimitada | `haiku` | `low` ou `medium` | Classificar arquivos já identificados, resumir um trecho, extrair campos de um formato conhecido, gerar rótulos candidatos | Resultado incompleto, ambíguo ou inconsistência semântica |
| Análise e desenvolvimento comuns | `sonnet` | `medium` (ou padrão do modelo) | Análise de requisitos bem delimitados, histórias, decomposição de funcionalidades, implementação comum, testes e documentação técnica | Repetidas falhas com contexto suficiente e esforço adequado; tarefa exige raciocínio arquitetural mais profundo |
| Raciocínio complexo ou alto impacto | `opus` | `high` ou `xhigh`, conforme disponibilidade | Decisões arquiteturais com trade-offs, conflitos entre fontes, auditoria semântica crítica, segurança, migração e integridade de dados | Escalar para `fable` somente em trabalho excepcionalmente longo/difícil, se disponível e se o benefício justificar o custo |
| Trabalho excepcional de longa duração | `fable`, se disponível | Começar no padrão recomendado para esse modelo | Investigação extensa e tarefas agentic de longa duração que exigem planejamento e verificação persistentes | Não usar como padrão; comparar custo, qualidade e conclusão com `opus` |

Essas rotas são padrões iniciais, não regras universais. A disponibilidade dos aliases e níveis de esforço depende da versão do Claude Code, provedor, conta e modelo habilitado. Se uma rota não estiver disponível, Sammy deve usar a alternativa permitida mais próxima, registrar a substituição e não tentar contornar restrições do provedor ou da organização.

##### Regras para escolher modelo versus esforço

- Se o modelo sabe executar a tarefa, mas fez pouco trabalho, pulou verificações ou parou cedo, aumentar `effort` antes de trocar de modelo.
- Se o modelo recebeu contexto suficiente, empregou esforço adequado e ainda não consegue resolver a tarefa por limitação de capacidade, conhecimento ou raciocínio, promover para um modelo mais capaz.
- Se o resultado está excessivamente longo, redundante ou especulativo, reduzir o esforço ou restringir o contrato de saída; não trocar automaticamente para um modelo menor sem avaliar a qualidade.
- Ao trocar de família de modelo, começar novamente no esforço padrão recomendado para aquela família e ajustar a partir de evidências. O mesmo rótulo de esforço não representa necessariamente o mesmo volume de trabalho entre modelos.
- Não elevar modelo e esforço simultaneamente na primeira tentativa de correção, pois isso impede identificar qual mudança resolveu o problema.
- Em tarefas de risco crítico, o modelo mais barato não pode substituir controles obrigatórios, testes, revisão independente ou aprovação humana.

##### Roteamento por agente

O campo `model` deve ser definido por subagente conforme a natureza de seu trabalho. Sammy também pode passar um alias de modelo por chamada quando o mesmo especialista precisar de níveis diferentes de capacidade conforme a tarefa.

| Agente ou papel | Modelo padrão recomendado | Quando usar rota superior |
|---|---|---|
| Analista de repositório / exploração | `haiku` ou `sonnet` | Repositório muito grande, arquitetura pouco documentada ou dependências difíceis de inferir |
| Analista de documentos e extração semântica | `sonnet`; `haiku` para triagem mecânica de trechos | Contradições, requisitos regulatórios ou ambiguidades de domínio |
| Analista de dados | `sonnet` | Migração, integridade, concorrência ou dados críticos: `opus` |
| Especialista de produto / histórias | `sonnet` | Regras de negócio complexas ou jornadas interdependentes: `opus` |
| Arquiteto | `opus` para decisões estruturais relevantes; `sonnet` para desenho delimitado | Arquitetura de alto impacto ou trade-offs sistêmicos: `opus` com esforço elevado |
| Implementador | `sonnet` | Algoritmo complexo, concorrência, segurança ou refatoração de grande risco: `opus` |
| Revisor | `sonnet` para revisão normal | Revisão independente de mudança crítica: `opus` |
| Auditor de rastreabilidade | Script primeiro; `haiku`/`sonnet` para interpretação | Auditoria semântica crítica ou divergência entre múltiplas fontes: `opus` |
| Integrador GitHub | Scripts/CLI primeiro; modelo apenas para interpretar exceções | Não escalar para modelo caro para operações CRUD previsíveis |

O agente principal Sammy deve permanecer em um modelo de uso geral configurado para a sessão, salvo decisão explícita da pessoa ou política do ambiente. O ganho econômico principal vem de delegar tarefas menores a subagentes mais leves e manter as tarefas difíceis em modelos mais capazes, não de alternar o modelo da conversa principal a cada etapa.

##### Redução de tokens e do contexto enviado

A troca de modelo sozinha não resolve desperdício. Sammy deve:

1. Manter `CLAUDE.md` curto, com regras essenciais e links para contexto sob demanda.
2. Carregar Skills e referências extensas somente quando a tarefa precisar delas; procedimentos longos devem ficar em Skills, não duplicados no contexto permanente.
3. Inspecionar primeiro índices, nomes e metadados; abrir somente os arquivos e trechos necessários.
4. Usar scripts para extração, parsing, hashes, comparação, cálculo, validação estrutural e sincronização.
5. Delegar buscas extensas e leitura de muitos arquivos a subagentes isolados, solicitando sínteses com evidências e caminhos — não cópias integrais do material.
6. Passar a cada subagente um pacote de contexto delimitado: objetivo, fontes, trechos relevantes, decisões aprovadas, restrições e formato de saída.
7. Pedir retornos estruturados e concisos: conclusão, evidências, incertezas, arquivos consultados, recomendação e próximos passos.
8. Não enviar novamente documentos inteiros ou decisões estáveis quando hashes e referências indicarem que nada mudou.
9. Evitar delegação em cascata. Por padrão, subagentes especialistas não devem criar outros agentes; Sammy controla o plano e o limite de concorrência.
10. Definir `maxTurns` apropriado para limitar execuções que se desviem do escopo e interromper/replanejar trabalhos que retornem resultados parciais.
11. Não chamar agentes diferentes para repetir a mesma análise sem motivo de revisão independente.
12. Não usar o modelo para responder perguntas que um comando determinístico, teste ou consulta local pode responder.

Subagentes isolam o contexto de trabalho e podem evitar que grandes logs e resultados de exploração contaminem a conversa principal. Isso não significa que sejam gratuitos: as chamadas dos subagentes também contam para os limites de uso da sessão/conta. O paralelismo deve ser usado quando reduzir o tempo ou melhorar a independência da análise, e não para aumentar artificialmente a quantidade de agentes.

##### Quando não trocar de modelo

Não trocar de modelo quando:

- O agente não recebeu o arquivo correto ou o contexto relevante.
- A instrução está incompleta ou contraditória.
- O trabalho exige uma ferramenta ou permissão que não está disponível.
- A falha é determinística e pode ser corrigida por script.
- O agente não executou os testes ou não consultou os arquivos previstos.
- A saída está incompleta apenas porque o limite de turnos foi atingido; nesse caso, retomar com estado e escopo definidos.

##### Quando trocar de modelo

Sammy pode tentar um modelo mais capaz quando registrar pelo menos uma destas evidências:

- Duas tentativas bem delimitadas falharam por limitação de raciocínio, apesar de contexto adequado.
- Existem contradições semânticas relevantes que o modelo atual não consegue reconciliar.
- A tarefa envolve impacto elevado e exige análise de alternativas que não pode ser validada por regras mecânicas.
- O resultado do modelo atual não atende aos critérios de qualidade após o esforço adequado.

A troca deve ser feita preferencialmente na próxima chamada de subagente, sem reiniciar toda a sessão principal. Sammy registra modelo/alias, esforço, motivo, tarefa, resultado e se a promoção melhorou a qualidade.

##### Transparência e orçamento

Criar `plano/controle/politica-de-modelos.yaml` para definir:

- aliases permitidos e modelo padrão por papel;
- nível de esforço padrão e limites permitidos;
- limite de subagentes simultâneos;
- limite de turnos por papel;
- tarefas que devem usar scripts em vez de modelos;
- tarefas que exigem modelo de maior capacidade;
- política de escalonamento e critérios de promoção;
- restrições do provedor e da conta;
- modo de custo (`economico`, `equilibrado` ou `qualidade-prioritaria`).

Em cada execução, registrar em `plano/controle/modelo-de-execucao.json` o modelo efetivamente usado por chamada de agente, esforço, motivo de seleção, duração quando disponível, status, necessidade de escalonamento e resultado. Não registrar credenciais, conteúdo secreto ou dados pessoais desnecessários. Métricas de tokens/custo só devem ser preenchidas quando forem realmente disponibilizadas pela ferramenta ou pelo provedor; não inventar estimativas apresentadas como consumo real.

O modo `economico` favorece scripts, `haiku` e menor esforço para tarefas simples; `equilibrado` usa a matriz padrão; `qualidade-prioritaria` aumenta a capacidade nas tarefas de alto risco e revisão. Nenhum modo pode remover testes, gates, validações obrigatórias ou autorizações humanas.

##### Verificação e calibração

A matriz de modelos precisa ser avaliada com o conjunto de cenários do Apêndice F. Para cada classe de tarefa, comparar qualidade, conclusão, retrabalho, quantidade de chamadas e consumo disponível. Não presumir que modelo mais barato sempre custa menos no total: uma tarefa incompleta pode exigir novas tentativas e sair mais cara. A promoção de modelo deve ser baseada em evidência, e a matriz precisa ser revista quando aliases ou versões mudarem.

#### Artefatos de decisão

Toda execução relevante deve produzir:

- `plano/controle/triagem.md`: explicação legível da avaliação, evidências e dúvidas;
- `plano/controle/triagem.json`: classificação estruturada para scripts;
- `plano/controle/estrategia-de-execucao.json`: decisão de porte, rigor, autonomia, granularidade, templates, agentes, verificações e gates;
- `plano/controle/politica-de-modelos.yaml`: aliases permitidos, roteamento por papel, níveis de esforço, limites e modos de custo;
- `plano/controle/modelo-de-execucao.json`: registro de modelo e esforço efetivamente usados por chamada, motivo e resultado;
- `plano/controle/execucao.json`: manifesto de execução, hashes, dependências, resultados e retomada.

Esses artefatos representam decisões da execução, não novas fontes de requisitos. Eles devem referenciar as fontes e versões que sustentam a classificação.

#### Modelo do relatório de triagem

Arquivo: `plano/controle/triagem.md`

```markdown
# Triagem de execução — [ID]

- Projeto:
- Solicitação:
- Data:
- Tipo de trabalho: projeto_novo | evolucao | bug | pesquisa | migracao | refatoracao | alteracao_pontual
- Estado do repositório: novo | existente | sem_repositorio
- Confiança da avaliação: alta | média | baixa

## Classificação do projeto
- Porte: pequeno | medio | grande
- Rigor-base: leve | padrao | rigoroso
- Autonomia: somente_rascunhos | controlada | ampliada
- Granularidade-base: projeto | dominio_epico | funcionalidade | historia_tarefa

## Avaliação de risco e complexidade
| Dimensão | Nota (0–2 ou DESCONHECIDO) | Evidência | Justificativa |
|---|---:|---|---|
| Complexidade de domínio | | | |
| Dados e segurança | | | |
| Integrações | | | |
| Incerteza | | | |
| Complexidade técnica | | | |
| Escala organizacional | | | |
| Impacto de falha | | | |

- Pontuação conhecida:
- Condições críticas:
- Desconhecidos relevantes:

## Estratégia para a unidade atual
- ID / unidade:
- Rigor local:
- Granularidade local:
- Controles globais aplicáveis:
- Templates selecionados:
- Agentes necessários e justificativa:
- Validações:
- Gates:

## Decisões e pendências
- Perguntas bloqueadoras:
- Premissas reversíveis:
- Riscos residuais:
- Próxima etapa segura:
```

#### Modelo estruturado de estratégia de execução

Arquivo: `plano/controle/estrategia-de-execucao.json`

```json
{
  "versao": 1,
  "execucao_id": "EXEC-001",
  "solicitacao": "Processar o planejamento inicial",
  "contexto": {
    "tipo_trabalho": "projeto_novo",
    "estado_repositorio": "novo",
    "fontes": []
  },
  "classificacao_projeto": {
    "porte": "medio",
    "rigor_base": "padrao",
    "autonomia": "controlada",
    "granularidade_base": "projeto",
    "pontuacao": 7,
    "pontuacao_maxima": 14,
    "confianca": "media",
    "condicoes_criticas": [],
    "desconhecidos": []
  },
  "unidades": [
    {
      "id": "FUNC-001",
      "rigor_local": "rigoroso",
      "granularidade_local": "funcionalidade",
      "controles_globais": ["rastreabilidade"],
      "templates": ["requisitos", "desenho-tecnico", "riscos", "tarefas"],
      "agentes": ["arquiteto", "analista-de-dados", "auditor"],
      "validacoes": ["cobertura", "seguranca", "integridade", "testes"],
      "gates": ["requisitos", "desenho", "tarefas"]
    }
  ],
  "decisoes_pendentes": [],
  "proxima_etapa": "gerar-diagnostico"
}
```

Os valores são exemplos. Na implementação, o JSON deve ser validado por schema, os nomes de templates/agentes devem existir no catálogo e as decisões precisam apontar para evidências reais.

#### Casos de avaliação e comportamento esperado

| Caso | Contexto | Classificação esperada | Comportamento de Sammy |
|---|---|---|---|
| Landing page pessoal | Poucas páginas, sem dados críticos | Porte pequeno; rigor leve ou padrão | Diagnóstico curto, poucas histórias e validação visual/acessibilidade pertinente |
| CRUD acadêmico | Entidades e regras simples, poucas integrações | Porte pequeno/médio; padrão | Histórias, critérios, desenho enxuto, tarefas e testes |
| SaaS com organizações e permissões | Vários módulos e isolamento entre clientes | Porte médio/grande; rigor rigoroso nas permissões | Analisar autorização, isolamento, dados e testes negativos |
| Sistema financeiro | Saldos, pagamentos e conciliação | Porte possivelmente grande; rigor rigoroso | Tratar dinheiro, idempotência, auditoria, falhas e recuperação como controles críticos |
| Protótipo descartável | Hipóteses ainda não validadas | Porte provisório; rigor leve de exploração | Definir hipótese, experimento, limite e aprendizado; não criar backlog de produção prematuro |
| Correção de texto em sistema bancário | Mudança isolada sem alteração de lógica/dados | Rigor local leve | Verificar contexto e regressões pertinentes; preservar controles globais não relacionados |
| Migração de dados | Transformação de registros existentes | Rigor rigoroso | Exigir inventário, backup/recuperação, reconciliação, plano de reversão e validação |
| Integração externa nova | Dependência externa e falhas fora do controle do sistema | Padrão ou rigoroso conforme impacto | Definir contratos, timeouts, retentativas, idempotência e comportamento degradado |
| Repositório legado com documentos incompletos | Comportamento real pode divergir das especificações | Porte e rigor provisórios; confiança baixa | Inspecionar código/testes/migrações, separar observado de desejado e não assumir que os PDFs estão atualizados |
| Mudança de requisito aprovado | Uma regra de negócio foi alterada | Rigor herdado e reavaliado localmente | Construir grafo de impacto, invalidar só aprovações dependentes e pedir nova decisão quando a semântica mudar |

#### Critérios de avaliação do próprio mecanismo

A lógica de triagem deve ter testes automatizados com entradas e resultados esperados. Cada cenário deve armazenar contexto, evidências, classificação esperada, condições críticas, templates, agentes, validações, gates e ações proibidas.

Métricas recomendadas:

- **Adequação da classificação:** proporção de cenários em que porte e rigor correspondem ao resultado esperado.
- **Falsos leves:** casos em que Sammy selecionou rigor insuficiente diante de uma condição crítica. Essa métrica deve ter tolerância zero nos casos críticos do conjunto de avaliação.
- **Excesso de processo:** artefatos ou agentes acionados sem utilidade para o caso.
- **Cobertura de riscos:** riscos conhecidos identificados e controles pertinentes selecionados.
- **Perguntas desnecessárias:** interrupções que não alteram decisão nem reduzem risco.
- **Reprocessamento:** etapas repetidas sem mudança de entrada relevante.
- **Custo e latência:** consumo de chamadas/contexto e tempo por classe de trabalho.
- **Estabilidade:** mudanças de perfil sem evidência material ou sem justificativa.

O conjunto de avaliação deve incluir casos leves, padrão, rigorosos, desconhecidos e mudanças de escopo. Toda alteração nas regras, templates ou instruções de Sammy deve executar novamente essa bateria. A avaliação não substitui revisão humana de casos críticos.

#### Limites da automação

- A classificação é uma recomendação operacional, não uma certificação de conformidade ou segurança.
- Uma nota baixa não prova que o projeto é seguro; a qualidade da evidência importa.
- O agente não pode transformar ausência de documento em confirmação de ausência de risco.
- A autonomia nunca substitui aprovação humana de requisitos, arquitetura, riscos ou publicação quando o gate exigir essa aprovação.
- As faixas e pesos devem ser calibrados com resultados reais do piloto, e não tratados como universais.
