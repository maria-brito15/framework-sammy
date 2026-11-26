<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 1235–1540. -->

> **Nesta página:** Estrutura de diretórios, idioma, nomenclatura e comandos de uso.

[← Voltar ao índice da documentação](../README.md)

---

### Estrutura de diretórios

A estrutura abaixo separa documentos de entrada, planejamento, contexto permanente, especificações por funcionalidade, automações e configurações nativas do Claude Code.

```text
projeto/
│
├── CLAUDE.md
├── configuracao-do-workflow.json
│
├── documentos/
│   ├── entrada/
│   │   ├── requisitos.pdf
│   │   └── modelo-de-dados.pdf
│   └── processados/
│       ├── manifesto-fontes.json
│       └── cache-extracao/
│
├── modelos/
│   ├── catalogo.json
│   ├── planejamento/
│   ├── backlog/
│   ├── especificacoes/
│   ├── gestao/
│   └── integracao/
│
├── plano/
│   ├── .status
│   ├── controle/
│   │   ├── execucao.json
│   │   ├── grafo-dependencias.json
│   │   ├── triagem.md
│   │   └── decisoes-pendentes.md
│   ├── diagnostico.md
│   ├── arquitetura.md
│   ├── equipes.md
│   ├── fases.md
│   ├── rastreabilidade.md
│   │
│   ├── tarefas/
│   │   ├── historias-de-usuario.md
│   │   ├── epicos.md
│   │   └── funcionalidades.md
│   │
│   └── integracao-github/
│       └── mapeamento.json
│
├── .ia/
│   ├── contexto/
│   │   ├── produto.md
│   │   ├── arquitetura.md
│   │   ├── dados.md                 # quando houver persistência
│   │   ├── interface.md             # quando houver interface
│   │   ├── definicao-de-concluido.md
│   │   ├── equipe.md
│   │   ├── convencoes.md
│   │   └── principios.md
│   │
│   └── especificacoes/
│       ├── FUNC-001-cadastro-de-usuarios/
│       │   ├── .status
│       │   ├── requisitos.md
│       │   ├── desenho-tecnico.md
│       │   ├── tarefas.md
│       │   ├── decisoes.md
│       │   ├── revisao.md
│       │   └── historias/
│       │       └── HIST-001/
│       │           ├── criterios-de-aceitacao.md
│       │           ├── desenho-especifico.md
│       │           ├── interface.md
│       │           └── alteracoes-de-dados.md
│       │
│       └── FUNC-002-autenticacao/
│           └── ...
│
├── .claude/
│   ├── agents/
│   │   ├── sammy.md
│   │   ├── analista-de-documentos.md
│   │   ├── analista-de-repositorio.md
│   │   ├── analista-de-dados.md
│   │   ├── analista-de-produto.md
│   │   ├── arquiteto-de-software.md
│   │   ├── planejador-de-entregas.md
│   │   ├── especialista-em-backlog.md
│   │   ├── consolidador-de-especificacoes.md
│   │   ├── auditor-de-planejamento.md
│   │   ├── publicador-do-github.md
│   │   ├── implementador.md
│   │   └── revisor.md
│   │
│   ├── skills/
│   │   ├── hora-de-trabalhar/SKILL.md
│   │   ├── processar-projeto/SKILL.md
│   │   ├── continuar-projeto/SKILL.md
│   │   ├── reprocessar-projeto/SKILL.md
│   │   ├── iniciar-projeto/SKILL.md
│   │   ├── analisar-documentos/SKILL.md
│   │   ├── planejar-projeto/SKILL.md
│   │   ├── montar-backlog/SKILL.md
│   │   ├── validar-planejamento/SKILL.md
│   │   ├── aprovar-planejamento/SKILL.md
│   │   ├── aprovar-backlog/SKILL.md
│   │   ├── publicar-no-github/SKILL.md
│   │   ├── atualizar-github/SKILL.md
│   │   ├── ver-progresso/SKILL.md
│   │   ├── especificar-funcionalidade/SKILL.md
│   │   ├── planejar-tarefas/SKILL.md
│   │   ├── aprovar-requisitos/SKILL.md
│   │   ├── aprovar-desenho/SKILL.md
│   │   ├── aprovar-tarefas/SKILL.md
│   │   ├── executar-tarefa/SKILL.md
│   │   ├── revisar-entrega/SKILL.md
│   │   └── consolidar-entrega/SKILL.md
│   │
│   ├── rules/
│   │   ├── idioma-e-comunicacao.md
│   │   ├── aprovacoes.md
│   │   ├── rastreabilidade.md
│   │   └── integridade-das-fontes.md
│   │
│   ├── hooks/
│   │   ├── verificar-estado.py
│   │   └── validar-arquivo-alterado.py
│   │
│   └── settings.json
│
├── scripts/
│   ├── orquestracao/
│   │   ├── descobrir-projeto.py
│   │   ├── calcular-hashes.py
│   │   ├── determinar-proximas-etapas.py
│   │   ├── invalidar-dependencias.py
│   │   └── registrar-execucao.py
│   │
│   └── planejamento/
│       ├── extrair-pdf.py
│       ├── validar-rastreabilidade.py
│       ├── validar-documentos.py
│       └── sincronizar-github.py
│
└── .github/
    └── workflows/
        └── sincronizar-projeto.yml
```

#### Regras para a estrutura

- `CLAUDE.md` é a entrada principal do Claude Code e deve permanecer curto. Ele aponta para regras, contexto e skills; não deve virar uma enciclopédia do projeto.
- `.ia/contexto/` contém informações relativamente estáveis sobre o produto, sua arquitetura, equipe, convenções e princípios.
- `plano/` contém o planejamento de produto e engenharia do projeto como um todo.
- `.ia/especificacoes/` contém as especificações individuais de funcionalidades.
- `.claude/skills/` contém processos reutilizáveis acionáveis como comandos de barra.
- `.claude/agents/sammy.md` define o agente principal da sessão. Os demais arquivos em `.claude/agents/` definem subagentes especialistas que Sammy pode acionar.
- `.claude/rules/` contém regras permanentes e transversais.
- `modelos/` é a biblioteca central de templates; cada modelo deve existir em um único lugar e ser selecionado pelo catálogo.
- `plano/controle/` guarda manifesto, grafo de dependências, triagem e decisões pendentes necessárias para retomar execuções.
- `documentos/processados/` guarda extrações e cache derivados, sem modificar os documentos originais.
- `.claude/hooks/` contém automações locais rápidas e restritas, acionadas por eventos do Claude Code.
- `scripts/` contém validações e integrações determinísticas. O que puder ser validado por código não deve depender apenas da interpretação do modelo.
- `.github/workflows/` contém automações de integração contínua, principalmente para refletir estados aprovados no GitHub Projects.

Os nomes exigidos pela ferramenta — `CLAUDE.md`, `SKILL.md`, `.claude/agents`, `.claude/skills`, `settings.json` — permanecem inalterados. O conteúdo, os comandos e os documentos produzidos devem estar em português.
### Padrão de idioma e nomenclatura

Português brasileiro é o idioma oficial da experiência e dos artefatos.

#### Regras de idioma

- Toda comunicação com a pessoa usuária deve ocorrer em português brasileiro.
- Todos os documentos do projeto devem ser redigidos em português.
- Nomes de agentes, skills, comandos, diretórios de negócio, campos, labels e mensagens devem ser em português.
- Preferir termos técnicos em português quando a tradução for clara e compreensível.
- Manter nomes oficiais de tecnologias, bibliotecas, protocolos, linguagens e convenções obrigatórias, como Java, TypeScript, PostgreSQL, REST, OAuth e `CLAUDE.md`.
- O corpo dos arquivos de configuração deve estar em português sempre que a sintaxe permitir.
- Não traduzir palavras reservadas, nomes de propriedades, esquemas ou campos exigidos por APIs externas.

#### Identificadores estáveis

Os identificadores são escritos sem acentos e não devem mudar depois de publicados.

| Prefixo | Significado | Exemplo |
|---|---|---|
| `REQ-` | Requisito de origem | `REQ-001` |
| `RF-` | Requisito funcional | `RF-001` |
| `RNF-` | Requisito não funcional | `RNF-001` |
| `HIST-` | História de usuário | `HIST-001` |
| `EP-` | Épico | `EP-001` |
| `FUNC-` | Funcionalidade | `FUNC-001` |
| `DEC-` | Decisão | `DEC-001` |
| `TAR-` | Tarefa | `TAR-001` |
| `DUV-` | Dúvida ou questão em aberto | `DUV-001` |

Os identificadores devem ser únicos no escopo definido para cada categoria. A numeração deve ser obtida dos documentos existentes ou de uma rotina determinística, nunca apenas da memória do agente.

#### Vocabulário padrão

| Termo | Uso no framework |
|---|---|
| História de usuário | Necessidade expressa do ponto de vista de um usuário ou ator |
| Épico | Agrupamento de capacidade ou objetivo amplo de negócio |
| Funcionalidade | Capacidade delimitada e entregável, especificada individualmente |
| Requisito funcional | Comportamento que o sistema deve oferecer |
| Requisito não funcional | Qualidade ou restrição mensurável do sistema |
| Desenho técnico | Descrição técnica de como uma funcionalidade será construída |
| Tarefa | Unidade de trabalho pequena, estimável e verificável |
| Gate | Ponto de aprovação explícita entre etapas |
| Contexto | Informação persistente que orienta o agente entre sessões |
### Comandos disponíveis

Os comandos são implementados como Skills do Claude Code. O nome da pasta da Skill define o comando de barra correspondente. Sammy é a interface conversacional e pode acionar essas Skills sem exigir que a pessoa conheça sua organização interna. A pessoa usuária não precisa invocar subagentes diretamente: Sammy coordena os especialistas necessários.

**Interface cotidiana:** a pessoa chama Sammy explicitamente com `/hora-de-trabalhar`. Esse é o ponto de entrada padrão e não exige argumentos. A partir daí, a pessoa conversa diretamente com Sammy. `/processar-projeto` é um procedimento de processamento amplo que Sammy seleciona quando apropriado; `/continuar-projeto` é uma opção explícita de recuperação; `/ver-progresso` consulta o estado sem iniciar o trabalho. Os demais comandos existem para manutenção, depuração ou intervenção específica.

#### Ativação e planejamento

| Comando | Função |
|---|---|
| `/hora-de-trabalhar` | **Comando principal de ativação.** Inicia Sammy sem exigir argumentos; ele reconhece o projeto, verifica o estado e decide a próxima atividade segura. |
| `/processar-projeto` | Procedimento de processamento amplo, acionado por Sammy quando um projeto novo ou uma revisão abrangente exigir planejamento de ponta a ponta. Também pode ser chamado diretamente para intervenção explícita. |
| `/continuar-projeto` | Retoma uma execução interrompida a partir do manifesto, sem repetir etapas concluídas. |
| `/reprocessar-projeto` | Reprocessa apenas artefatos e etapas impactados por mudanças em fontes, decisões ou templates. |
| `/iniciar-projeto` | Cria a estrutura de diretórios, arquivos-base, regras e templates. |
| `/analisar-documentos` | Analisa os documentos de entrada e gera `plano/diagnostico.md`. |
| `/planejar-projeto` | Gera `plano/arquitetura.md`, `plano/equipes.md` e `plano/fases.md`. |
| `/montar-backlog` | Gera histórias de usuário, épicos e funcionalidades, nessa ordem de produção. |
| `/validar-planejamento` | Executa a auditoria semântica e as validações determinísticas do planejamento. |

#### Aprovações

| Comando | Função |
|---|---|
| `/aprovar-planejamento` | Registra a aprovação humana do diagnóstico e dos documentos de planejamento. |
| `/aprovar-backlog` | Registra a aprovação humana das histórias, épicos e funcionalidades. |
| `/aprovar-requisitos` | Aprova os requisitos de uma funcionalidade específica. |
| `/aprovar-desenho` | Aprova o desenho técnico de uma funcionalidade específica. |
| `/aprovar-tarefas` | Aprova as tarefas de uma funcionalidade específica. |

A forma preferencial de aprovação é uma resposta natural e inequívoca ao pacote apresentado, por exemplo: “Aprovo o diagnóstico” ou “Aprovo o planejamento e o backlog”. Como o pacote e os artefatos exatos já estão identificados na conversa, a skill pode registrar essa decisão e retomar automaticamente o fluxo. Os comandos `/aprovar-*` permanecem como alternativas explícitas para aprovações isoladas. Um agente nunca pode aprovar o próprio trabalho nem inferir aprovação a partir de silêncio, ausência de comentários ou resultado positivo de testes.

#### GitHub e acompanhamento

| Comando | Função |
|---|---|
| `/publicar-no-github` | Publica o backlog aprovado em Issues e adiciona os itens ao GitHub Projects. |
| `/atualizar-github` | Sincroniza alterações aprovadas nos documentos com as Issues e os campos do Project. |
| `/ver-progresso` | Mostra o estado atual do projeto, gates, pendências, bloqueios e próximas etapas seguras. |

#### Especificação e desenvolvimento

| Comando | Função |
|---|---|
| `/especificar-funcionalidade` | Cria ou atualiza os requisitos e o desenho técnico de uma funcionalidade. |
| `/planejar-tarefas` | Decompõe o desenho aprovado em tarefas pequenas e verificáveis. |
| `/executar-tarefa` | Implementa uma única tarefa aprovada por vez. |
| `/revisar-entrega` | Revisa o código contra os requisitos, desenho, tarefas e evidências de execução. |
| `/consolidar-entrega` | Verifica o alinhamento entre a entrega validada e o contexto global do projeto; propõe atualizações reutilizáveis. |

#### Uso esperado — ativação explícita e operação contínua

A pessoa abre o repositório no Claude Code e chama Sammy:

```text
/hora-de-trabalhar
```

Sammy começa pelo reconhecimento do ambiente. Ele verifica o repositório, a branch, as alterações locais, os documentos de entrada, o manifesto de execução, as aprovações pendentes, as tarefas abertas e as integrações configuradas. Em seguida, realiza a triagem adaptativa e escolhe o próximo trabalho. Não exige que a pessoa descreva a atividade antes dessa investigação.

Exemplos de decisões após a ativação:

- Projeto novo com documentos: iniciar análise e planejamento.
- Projeto com execução interrompida: retomar a próxima etapa segura.
- Projeto com alterações recentes: avaliar impacto e reprocessar somente o que mudou.
- Projeto sem pendências identificadas: apresentar o estado e perguntar qual objetivo novo deve ser iniciado.
- Projeto com gate ou decisão bloqueadora: executar atividades independentes e apresentar as decisões necessárias.

Depois de uma resposta ou aprovação, Sammy continua automaticamente quando as regras permitirem. A pessoa também pode executar `/continuar-projeto` explicitamente, mas não precisa fazê-lo no fluxo normal. Para iniciar um novo ciclo em outra ocasião, basta chamar novamente `/hora-de-trabalhar`.

Para uma execução parcial, diagnóstico ou manutenção, os comandos especializados permanecem disponíveis. A pessoa não precisa utilizar o fluxo manual abaixo, salvo quando desejar controlar uma etapa individual:

```text
/iniciar-projeto
/analisar-documentos
/planejar-projeto
/montar-backlog
/validar-planejamento
/publicar-no-github
```

Depois, para cada funcionalidade:

```text
/especificar-funcionalidade FUNC-001
# Revisar e aprovar requisitos
/planejar-tarefas FUNC-001
# Revisar e aprovar desenho e tarefas
/executar-tarefa TAR-001
/revisar-entrega FUNC-001
/consolidar-entrega FUNC-001
```

Os comandos podem receber identificadores, caminhos de arquivos ou instruções adicionais. Quando faltar informação indispensável, a skill deve perguntar de forma objetiva, uma pergunta por vez.

---
