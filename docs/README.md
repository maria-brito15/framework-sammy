# Documentação do Sammy

Esta pasta é a documentação de referência do framework. Use este índice como **roteador**: escolha o assunto e abra somente os documentos necessários. O manual extenso foi dividido por responsabilidade para facilitar navegação, manutenção e evolução.

## Comece por aqui

| Quero... | Leia |
|---|---|
| Entender o que é Sammy, como ativá-lo e o fluxo geral | [Visão e princípios](01-visao-geral/visao-e-principios.md) |
| Entender como Sammy avalia porte, rigor e granularidade | [Triagem adaptativa](01-visao-geral/triagem-adaptativa.md) |
| Entender permissões, gates, retomada e reprocessamento | [Autonomia e execução](01-visao-geral/autonomia-e-execucao.md) |
| Consultar estrutura do projeto e comandos | [Estrutura e comandos](01-visao-geral/estrutura-e-comandos.md) |
| Entender histórias, épicos, funcionalidades e sprints | [Backlog e planejamento](02-planejamento/backlog-e-planejamento.md) |
| Entender o ciclo SDD por funcionalidade | [Especificação e alinhamento](03-sdd/especificacao-e-alinhamento.md) |
| Criar ou alterar agentes e Skills | [Agentes, Skills e contexto](04-claude-code/agentes-skills-contexto.md) |
| Configurar GitHub Projects e automações | [GitHub e automações](05-integracoes/github-e-automacoes.md) |
| Instalar, validar ou evoluir o framework | [Implantação e validação](06-operacao/implantacao-validacao-evolucao.md) |
| Encontrar um template | [Catálogo de modelos](#catalogo-de-modelos) |
| Entender o roteamento de modelos e custo de tokens | [Gerenciamento de modelos](07-modelos/gerenciamento-de-modelos.md) |
| Consultar fontes e referências | [Referências e síntese](08-referencia/referencias-e-sintese.md) |

## Mapa da documentação

### 01. Visão geral e operação
- [Visão e princípios](01-visao-geral/visao-e-principios.md) — identidade, ativação, princípios e arquitetura.
- [Triagem adaptativa](01-visao-geral/triagem-adaptativa.md) — porte, rigor, autonomia, granularidade e decisões.
- [Autonomia e execução](01-visao-geral/autonomia-e-execucao.md) — gates, manifesto, reprocessamento e qualidade.
- [Estrutura e comandos](01-visao-geral/estrutura-e-comandos.md) — organização, idioma e comandos.

### 02. Planejamento de produto e engenharia
- [Backlog e planejamento](02-planejamento/backlog-e-planejamento.md) — histórias, épicos, funcionalidades, refinamento, DoR/DoD e sprints.

### 03. Spec-Driven Development
- [Especificação e alinhamento](03-sdd/especificacao-e-alinhamento.md) — requisitos, desenho técnico, tarefas, revisão e alinhamento entre níveis.

### 04. Claude Code
- [Agentes, Skills e contexto](04-claude-code/agentes-skills-contexto.md) — Sammy, especialistas, Skills, contratos e contexto permanente.

### 05. Integrações
- [GitHub e automações](05-integracoes/github-e-automacoes.md) — Issues, Projects, labels, sincronização, hooks e automações.

### 06. Operação e evolução
- [Implantação, validação e evolução](06-operacao/implantacao-validacao-evolucao.md) — instalação, roadmap, pilotos e critérios de sucesso.

## Catálogo de modelos

Os templates copiáveis ficam em `modelos/`; o catálogo central de metadados está em [`../modelos/catalogo.json`](../modelos/catalogo.json). Sammy seleciona somente os modelos aplicáveis ao trabalho.

| Tipo | Referência |
|---|---|
| Diagnóstico, arquitetura, equipes, fases e rastreabilidade | [Modelos de planejamento](07-modelos/planejamento.md) |
| Triagem, avaliação, estratégia e calibração | [Modelos de triagem adaptativa](07-modelos/triagem-adaptativa.md) |
| Requisitos, desenho, tarefas e revisão | [Modelos de especificações](07-modelos/especificacoes.md) |
| Agentes, Skills e regras | [Modelos de agentes, Skills e regras](07-modelos/agentes-skills-e-regras.md) |
| Pesquisa, defeitos, mudanças e débito técnico | [Modelos de engenharia](07-modelos/pesquisa-defeitos-e-mudancas.md) |
| Estados, aprovações, exceções e automação | [Modelos operacionais](07-modelos/estados-aprovacoes-e-automacao.md) |
| Política e roteamento de modelos | [Gerenciamento de modelos](07-modelos/gerenciamento-de-modelos.md) |

## Configurações e implementação

- [`configuracao/configuracao-do-workflow.json`](../configuracao/configuracao-do-workflow.json) — comportamento geral.
- [`configuracao/politica-de-modelos.yaml`](../configuracao/politica-de-modelos.yaml) — custo, esforço e roteamento.
- [`configuracao/catalogo-de-modelos.json`](../configuracao/catalogo-de-modelos.json) — aliases e modelos disponíveis.
- [`configuracao/integracao-github.json`](../configuracao/integracao-github.json) — integração GitHub.
- [`.claude/agents/`](../.claude/agents/) — agentes.
- [`.claude/skills/`](../.claude/skills/) — procedimentos reutilizáveis.
- [`.claude/rules/`](../.claude/rules/) — regras compartilhadas.
- [`scripts/`](../scripts/) — automações determinísticas.
- [`schemas/`](../schemas/) — contratos de dados.

## Como manter a documentação

1. Atualize a página temática correspondente; evite concentrar novas explicações no README raiz.
2. Atualize este índice ao criar, mover ou renomear páginas.
3. Mantenha templates copiáveis em `modelos/`; esta documentação explica quando usá-los.
4. Mantenha políticas executáveis em `configuracao/` e schemas em `schemas/`.
5. Registre decisões transversais na página temática principal e adicione links cruzados.
6. O README raiz deve permanecer curto e funcionar como porta de entrada para este índice.
