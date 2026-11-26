<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 7366–7451. -->

> **Nesta página:** Referências metodológicas, documentação técnica, AgileSpec e síntese final.

[← Voltar ao índice da documentação](../README.md)

---

### Fundamentos metodológicos e documentação oficial

#### Livro-base

Fontoura, Felipe. *Spec-Driven Development: Shipping Production Software with AI Agents*. Primeira edição, 2026.

Partes utilizadas como fundamento:

- Capítulo 2, páginas 15–21: definição de SDD, pipeline e gates.
- Capítulo 3, páginas 23–31: estrutura de diretórios, contexto permanente, documentos e rastreabilidade.
- Capítulo 4, páginas 33–42: qualidade dos requisitos, escopo negativo, sintaxe EARS e questões de implementação.
- Capítulo 11, páginas 117–123: SDD com Claude Code e fluxo com gates.
- Capítulo 12, páginas 125–130: skills, subagents, verificação com evidências e riscos de automação sem gate.
- Capítulo 14, páginas 141–146: SDD em equipes, revisão de especificações e quadro de acompanhamento.
- Apêndices A e B, páginas 159–166: modelos de documentos e organização do kit SDD.

#### Documentação oficial consultada

- Claude Code — Skills: https://code.claude.com/docs/en/skills
- Claude Code — Subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code — Memory / CLAUDE.md: https://code.claude.com/docs/en/memory
- GitHub CLI — `gh issue create`: https://cli.github.com/manual/gh_issue_create
- GitHub CLI — `gh project item-add`: https://cli.github.com/manual/gh_project_item-add
- GitHub CLI — `gh project field-create`: https://cli.github.com/manual/gh_project_field-create
- GitHub CLI — `gh project item-edit`: https://cli.github.com/manual/gh_project_item-edit
- GitHub Docs — Planning and tracking with Projects: https://docs.github.com/en/issues/planning-and-tracking-with-projects
- GitHub Docs — Quickstart for Projects: https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects
### Referência complementar: AgileSpec

[mtov/AgileSpec — An Agile Workflow for AI-Assisted Software Delivery](https://github.com/mtov/AgileSpec)

Consulta realizada em 26 de novembro de 2026. O repositório propõe um workflow leve e independente de ferramenta, organizado em especificações do projeto e especificações de histórias. Seu diferencial é o *Specification Alignment Loop*: documentos globais orientam histórias; decisões úteis descobertas durante a implementação são consolidadas de volta aos documentos globais. A proposta também sugere critérios de aceitação separados em casos normais e casos extremos, arquivos opcionais de interface e alterações de dados, e consolidação antes de marcar uma história como concluída. O README informa que a proposta ainda é preliminar e sujeita a evolução; portanto, este framework reutiliza ideias, não presume que o AgileSpec seja um padrão definitivo.

Arquivos consultados:

- [README.md](https://github.com/mtov/AgileSpec/blob/main/README.md) — motivação, níveis de especificação, estrutura de pastas e fluxo de trabalho.
- [faq.md](https://github.com/mtov/AgileSpec/blob/main/faq.md) — limites declarados do fluxo, papel de sprints, Definition of Done, NFRs e relação entre specs e configuração de agentes.
- [prompts/specification.md](https://github.com/mtov/AgileSpec/blob/main/prompts/specification.md) — instrução para produzir critérios de aceitação e desenho específico sem implementar.
- [prompts/implementation.md](https://github.com/mtov/AgileSpec/blob/main/prompts/implementation.md) — implementação guiada por especificações aprovadas, cobrindo casos normais e extremos, e parada antes da consolidação.
- [prompts/consolidation.md](https://github.com/mtov/AgileSpec/blob/main/prompts/consolidation.md) — consolidação de decisões duradouras no contexto global sem copiar detalhes locais.
- [Exemplo PodLite](https://github.com/mtov/AgileSpec/tree/main/examples/podlite) — demonstra versões sucessivas com specs específicas e consolidação aprovada.
- [Licença MIT](https://github.com/mtov/AgileSpec/blob/main/LICENSE) — permite reutilização e adaptação sob as condições da licença; se trechos ou arquivos forem copiados, preservar o aviso de copyright e a licença.

**Avaliação para o nosso framework:** a contribuição mais valiosa é o ciclo de consolidação após cada entrega e a separação entre contexto global e especificação local. O framework deve adotar isso, mas manter seu próprio planejamento de produto (épicos, funcionalidades e histórias), gates SDD, tarefas explícitas e integração com GitHub. O AgileSpec não substitui essas partes; ele complementa principalmente o ciclo de entrega por história.

### Práticas complementares de backlog e Claude Code

As páginas do GitScrum são guias práticos de uma ferramenta de gestão e não normas obrigatórias de Scrum ou SDD. As recomendações abaixo foram incorporadas como heurísticas; devem ser adaptadas ao produto, ao time e ao risco.

1. [Epic Breakdown Techniques | Story Slicing](https://docs.gitscrum.com/en/best-practices/epic-breakdown-techniques) — técnicas de divisão por fluxo, persona, regra de negócio, CRUD, caminho feliz/exceções, plataforma, dados e interface; reforça fatias verticais e validação das histórias.
2. [User Story Writing | Format, INVEST, and Examples](https://docs.gitscrum.com/en/best-practices/user-story-writing) — papel, objetivo, benefício, critérios de aceitação, INVEST, Gherkin e técnicas de divisão de histórias.
3. [Backlog Grooming Best Practices | Sprint-Ready Refinement](https://docs.gitscrum.com/en/best-practices/backlog-grooming-best-practices) — refinamento contínuo, preparação, perguntas, critérios, estimativa, remoção de itens obsoletos e backlog organizado por horizonte.
4. [Sprint Backlog Creation | Right Work, Right Size](https://docs.gitscrum.com/en/best-practices/creating-effective-sprint-backlogs) — Definition of Ready, capacidade, disponibilidade, velocidade histórica, buffer e seleção de trabalho.
5. [Definition of Done | Shared Quality Standards](https://docs.gitscrum.com/en/best-practices/definition-of-done) — diferença entre critérios de aceitação e Definition of Done, checklist de qualidade e aplicação por nível.
6. [Technical Debt Prioritization | Impact-Effort Framework](https://docs.gitscrum.com/en/best-practices/technical-debt-prioritization) — avaliação de débito técnico por impacto, frequência, risco e esforço; utilizado como referência para tornar débito técnico visível no backlog.
7. [Sprint Backlog Refinement](https://docs.gitscrum.com/en/best-practices/managing-sprint-backlog-refinement) — prontidão, estimativa, tamanho de itens e refinamento antes do planejamento da sprint.

#### Referências técnicas do Claude Code

- [Claude Code — Skills](https://code.claude.com/docs/en/skills) — diretórios de skills, arquivo `SKILL.md` e invocação.
- [Claude Code — Subagents](https://code.claude.com/docs/en/sub-agents) — agentes personalizados, agente principal da sessão, delegação e restrições de ferramentas.
- [Claude Code — Settings](https://code.claude.com/docs/en/settings) — configuração JSON, agente padrão da sessão, permissões e precedência.
- [Claude Code — Model configuration](https://code.claude.com/docs/en/model-config) — aliases de modelos, seleção do modelo da sessão, níveis de esforço e fallback.
- [Claude Code — Subagents](https://code.claude.com/docs/en/sub-agents) — escolha de modelo e esforço por subagente e por chamada.
- [Claude Academy — Choosing the right effort level](https://academy.claude.com/tutorials/choosing-the-right-effort-level-in-claude-code) — ajuste de esforço e critérios para trocar de modelo.
- [Anthropic — Choosing a Claude model and effort level](https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code) — recomendações práticas de seleção e consumo.
- [Anthropic — Steering Claude Code](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) — distinção entre contexto, skills, hooks, rules e subagents.

#### Como reconciliar as referências

- O livro de Felipe Fontoura orienta o pipeline SDD, os gates, a separação de agentes e as tarefas de implementação.
- O GitScrum complementa a qualidade do backlog, a decomposição de épicos, a escrita e o refinamento de histórias, a prontidão para sprint e a definição de concluído.
- O AgileSpec complementa o ciclo por história: especificação local, implementação, revisão e consolidação das decisões reutilizáveis no contexto global.
- Este framework combina as referências sem tratar um guia comercial ou uma proposta preliminar como regra universal.
- O tamanho de 1–3 dias citado para histórias e 2–4 horas citado pelo livro para tarefas pertencem a granularidades diferentes; não devem ser comparados como estimativas do mesmo item.

## Síntese final

Este manual define Sammy como ponto único de contato e orquestrador adaptativo. Para cada solicitação, ele deve identificar o tipo de trabalho, avaliar separadamente porte, rigor, autonomia e granularidade, selecionar agentes e templates necessários, construir um plano verificável e reavaliar a estratégia diante de eventos relevantes. O motor de políticas e os scripts tornam as regras repetíveis; o roteador adaptativo seleciona modelo, esforço e contexto por tarefa; os subagentes fornecem especialização; os documentos versionados preservam contexto e decisões; os gates mantêm a responsabilidade humana onde ela é necessária.

O objetivo operacional é simples: a pessoa chama Sammy com `/hora-de-trabalhar`; Sammy reconhece o projeto, decide o que precisa acontecer e conduz o trabalho sem exigir um briefing inicial. Ele deve aplicar o processo mínimo suficiente para produzir uma entrega segura, rastreável e verificável — nem mais burocracia do que o caso exige, nem menos controle do que o risco permite.


O framework deve permitir que a pessoa abra o repositório, inicie o Claude Code com Sammy como agente principal e execute `/hora-de-trabalhar`. Não é necessário fornecer documentos por mensagem nem descrever o que deve ser feito antes da ativação: Sammy reconhece as fontes e o estado do projeto, avalia o contexto e escolhe a próxima atividade. Depois da ativação, a pessoa pode conversar naturalmente, fornecer novas instruções e responder às decisões que Sammy apresentar. Ele assume descoberta, análise, escolha do rigor, delegação, geração de artefatos, validação, autocorreção segura, retomada incremental e preparação da integração com o GitHub. A pessoa participa nos pontos que exigem decisões de produto, risco, arquitetura, capacidade, aprovação ou autorização de efeitos externos.

A automação é considerada bem-sucedida quando reduz o trabalho operacional e o retrabalho, preserva a rastreabilidade, evita duplicação de dados e mantém os artefatos aprovados coerentes com o que será implementado. Após cada entrega, Sammy também verifica se decisões descobertas precisam ser consolidadas no contexto global, para que a próxima história comece com documentação atualizada. A quantidade de arquivos, agentes ou comandos não é uma métrica de qualidade.
