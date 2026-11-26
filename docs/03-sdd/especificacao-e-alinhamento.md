<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 2709–2958. -->

> **Nesta página:** Especificações por funcionalidade, tarefas, revisão e alinhamento entre especificações globais e locais.

[← Voltar ao índice da documentação](../README.md)

---

### Especificação SDD de cada funcionalidade

Depois que o backlog estiver aprovado, cada funcionalidade pode iniciar seu ciclo individual.

Exemplo de diretório:

```text
.ia/especificacoes/FUNC-001-cadastro-de-usuarios/
├── .status
├── requisitos.md
├── desenho-tecnico.md
├── tarefas.md
├── decisoes.md
└── revisao.md
```

#### `requisitos.md` — O QUE e POR QUÊ

Deve ser independente de tecnologia e conter:

- Visão geral.
- Objetivos.
- Fora de escopo.
- Histórias relacionadas.
- Requisitos funcionais em linguagem clara e, quando apropriado, sintaxe EARS.
- Requisitos não funcionais.
- Prioridades.
- Restrições.
- Regras de negócio.
- Critérios de aceitação.
- Questões e decisões pendentes.
- Métricas de sucesso.
- Riscos.

#### `desenho-tecnico.md` — COMO

Deve conter:

- Resumo técnico.
- Mapeamento de cada requisito para a solução.
- Componentes e responsabilidades.
- Fluxos e contratos de API.
- Modelo de dados e migrações relevantes.
- Segurança e autorização.
- Tratamento de erros e casos extremos.
- Estratégia de testes e verificação.
- Decisões técnicas, justificativas e alternativas.
- Riscos e mitigação.

#### `tarefas.md` — QUANTO e EM QUE ORDEM

Deve conter:

- Verificação de prontidão.
- Cobertura dos requisitos.
- Tarefas com identificadores `TAR-xxx`.
- Estimativa e prioridade.
- Dependências explícitas.
- Checklist de implementação.
- Critérios de aceitação verificáveis.
- Arquivos prováveis.
- Comandos de verificação.
- Dependências entre fases ou tarefas.

Cada tarefa deve ser pequena o suficiente para ser implementada e verificada de forma independente sempre que possível. Como referência inicial, considerar unidades de 2 a 4 horas para projetos médios, ajustando quando a natureza do trabalho justificar.

#### `revisao.md` — EVIDÊNCIA

O relatório de revisão deve registrar:

```markdown
## TAR-001 — [Título]

**Afirmação verificada:** ...
**Comando executado:** `comando de teste`
**Código de saída:** 0
**Resultado:** 3 testes executados, 3 aprovados
**Veredito:** APROVADO
**Limitações:** Nenhuma
```

Se a verificação for manual, registrar explicitamente que foi manual e quais limitações existem. Não declarar `APROVADO` sem evidência compatível com a afirmação.

### Ciclo de alinhamento entre especificações globais e específicas

Esta seção adapta uma ideia central do [AgileSpec](https://github.com/mtov/AgileSpec): manter dois níveis de especificação conectados. A documentação global orienta cada entrega; as descobertas úteis de cada entrega atualizam a documentação global. O fluxo não termina quando o código passa nos testes: ele termina quando a implementação, a revisão e a documentação relevante estão alinhadas.

#### Nível 1 — Especificações do projeto

São documentos duradouros, consultados por Sammy e pelos especialistas quando uma decisão de implementação depende do contexto geral. Eles devem registrar princípios, convenções e decisões que ajudam trabalhos futuros, sem tentar descrever todos os detalhes de cada funcionalidade.

| Documento | Conteúdo | Aplicabilidade |
|---|---|---|
| `.ia/contexto/produto.md` | Visão, problema, usuários, objetivos, métricas e limites do produto | Obrigatório para produtos com escopo de negócio definido |
| `.ia/contexto/arquitetura.md` | Módulos, responsabilidades, fronteiras, integrações e restrições arquiteturais aprovadas | Obrigatório quando há decisões arquiteturais relevantes |
| `.ia/contexto/dados.md` | Convenções globais de persistência, integridade, ciclo de vida, migrações e proteção de dados | Quando o produto persiste ou integra dados |
| `.ia/contexto/interface.md` | Convenções globais de interface, navegação, acessibilidade, componentes e feedback visual | Quando existe interface de usuário |
| `.ia/contexto/definicao-de-concluido.md` | Critérios compartilhados para considerar uma entrega concluída | Obrigatório para o fluxo de implementação |
| `.ia/contexto/equipe.md` | Responsabilidades, competências, responsáveis conhecidos e aprovações | Quando há mais de uma pessoa ou equipe envolvida |
| `.ia/contexto/convencoes.md` | Padrões de código, API, erros, testes, nomenclatura e organização | Recomendado para todo repositório com código |
| `.ia/contexto/principios.md` | Invariantes, regras não negociáveis, segurança e privacidade | Recomendado; obrigatório em sistemas de risco elevado |

A lista é adaptativa. Não criar documentos vazios apenas para completar a estrutura. Quando um assunto não se aplica, registrar a justificativa no manifesto ou no diagnóstico, em vez de produzir um arquivo sem conteúdo útil.

**Não duplicar o modelo de dados inteiro em `dados.md`.** O documento global deve registrar regras e decisões duradouras de persistência. O modelo físico ou conceitual detalhado permanece na fonte apropriada — diagrama, migrations, schema ou documentação específica — e é referenciado.

**Não duplicar telas em `interface.md`.** O documento global define padrões compartilhados. Fluxos, componentes e estados visuais específicos de uma história ficam na especificação daquela história.

O backlog canônico continua sendo o conjunto de documentos versionados em `plano/tarefas/`. Caso seja útil uma visão resumida `plano/backlog.md`, ela será gerada automaticamente como índice, nunca mantida manualmente como uma segunda fonte de verdade.

#### Nível 2 — Especificações da unidade de entrega

A unidade de planejamento e a unidade de implementação não precisam ser sempre iguais:

**Fonte única dos critérios de aceitação:** `plano/tarefas/historias-de-usuario.md` é o registro canônico da identidade, origem, objetivo, prioridade, relações e estado de cada história. Quando uma história recebe uma especificação própria, seus cenários completos e verificáveis passam a ter como fonte canônica o arquivo `criterios-de-aceitacao.md` dessa história. O backlog conserva somente um resumo e o caminho do arquivo. Requisitos e desenho da funcionalidade referenciam os IDs dos critérios, sem duplicar os cenários. Para histórias pequenas sem pasta própria de especificação, os critérios completos permanecem no próprio backlog. Sammy deve aplicar essa regra automaticamente para impedir divergência entre cópias.

- `EP-xxx` organiza uma capacidade ampla de negócio.
- `FUNC-xxx` agrupa uma capacidade delimitada e pode conter várias histórias.
- `HIST-xxx` descreve um resultado observável para um usuário ou ator.
- A unidade de especificação e implementação é escolhida por Sammy conforme tamanho, dependências, risco e coesão técnica.

**Preferir especificar por funcionalidade (`FUNC`) quando:** várias histórias compartilham arquitetura, modelo de dados, APIs, integrações ou uma decisão técnica que precisa ser aprovada uma única vez.

**Preferir especificar por história (`HIST`) quando:** a história representa uma fatia vertical pequena, independente, com critérios de aceitação claros e desenho técnico limitado.

**Usar uma especificação de funcionalidade com critérios por história quando:** o grupo de histórias compartilha o desenho, mas cada história tem cenários de comportamento próprios. Essa é a opção padrão para funcionalidades médias.

Sammy não deve criar uma especificação extensa para cada história por hábito. Deve escolher a menor unidade que preserve clareza, testabilidade e rastreabilidade, registrando a decisão no manifesto.

#### Estrutura adaptativa de uma especificação

A pasta de uma funcionalidade pode conter:

```text
.ia/especificacoes/FUNC-001-cadastro-de-usuarios/
├── .status
├── requisitos.md
├── desenho-tecnico.md
├── tarefas.md
├── decisoes.md
├── revisao.md
└── historias/
    ├── HIST-001-criar-conta/
    │   ├── criterios-de-aceitacao.md
    │   ├── desenho-especifico.md       # opcional
    │   ├── interface.md                # opcional
    │   └── alteracoes-de-dados.md      # opcional
    └── HIST-002-confirmar-email/
        └── criterios-de-aceitacao.md
```

Quando a história for a própria unidade de implementação, ela pode ter uma pasta de especificação independente em `.ia/especificacoes/historias/HIST-xxx/`, sem exigir uma pasta `FUNC` artificial.

A presença de `interface.md` depende de mudanças na experiência visual. A presença de `alteracoes-de-dados.md` depende de mudanças em persistência, schema, migração ou integridade. Arquivos opcionais não devem ser criados se não houver conteúdo aplicável.

#### Critérios de aceitação: casos normais e casos extremos

Cada história implementável deve explicitar:

1. **Casos normais:** comportamento esperado no fluxo válido mais comum.
2. **Casos alternativos:** variações válidas do fluxo.
3. **Casos extremos:** limites, entradas inválidas, ausência de dados, concorrência, falhas externas e estados inesperados relevantes.
4. **Regras de negócio:** condições que precisam permanecer verdadeiras.
5. **Permissões e segurança:** quem pode realizar a operação e em quais condições.
6. **Rastreabilidade:** requisitos de origem e testes/verificações que demonstrarão o atendimento.

Os cenários devem ser concretos e verificáveis, preferencialmente no formato Dado/Quando/Então. Não exigir Gherkin em situações em que uma tabela de entradas e resultados seja mais clara.

#### Loop de alinhamento das especificações

```text
ESPECIFICAÇÕES DO PROJETO
 produto + arquitetura + dados + interface + definição de concluído
                |
                | orientam
                v
ESPECIFICAÇÃO DA FUNCIONALIDADE/HISTÓRIA
 requisitos + aceitação + desenho + mudanças específicas
                |
                v
IMPLEMENTAÇÃO E TESTES
                |
                v
REVISÃO INDEPENDENTE
                |
                v
CONSOLIDAÇÃO
 identificar decisões que serão úteis em entregas futuras
                |
                v
PROPOSTA DE ATUALIZAÇÃO DO CONTEXTO GLOBAL
                |
                v
APROVAÇÃO HUMANA QUANDO HOUVER MUDANÇA DURADOURA
                |
                v
PRÓXIMA HISTÓRIA COM CONTEXTO ATUALIZADO
```

A consolidação é executada após a revisão técnica e antes de marcar a entrega como concluída. Ela é obrigatória como verificação, mesmo quando o resultado for “nenhuma atualização global necessária”.

#### Procedimento de consolidação

A Skill `/consolidar-entrega` deve:

1. Ler a especificação aprovada da unidade entregue, o diff/commit, os resultados de teste e os documentos globais relacionados.
2. Comparar o comportamento implementado com os critérios de aceitação, o desenho e as alterações de dados/interface aprovadas.
3. Identificar decisões que devem orientar funcionalidades futuras, por exemplo: padrão de integração, convenção de persistência, regra de segurança, componente visual compartilhado ou decisão arquitetural.
4. Distinguir decisões duradouras de detalhes locais, escolhas provisórias e dívida técnica.
5. Preparar uma proposta de atualização dos documentos globais, mostrando diff e justificativa.
6. Não copiar classes, funções, schemas ou detalhes de uma tela para os documentos globais quando isso não constituir uma convenção reutilizável.
7. Não alterar código, critérios de aceitação originais ou especificações aprovadas durante a consolidação.
8. Se houver divergência entre implementação e especificação, reportá-la antes de consolidar.
9. Solicitar aprovação humana para mudanças em decisões globais ou arquitetura; atualizações meramente editoriais e sem alteração de significado podem ser automatizadas se a política do projeto permitir.
10. Registrar o resultado, incluindo a decisão explícita de que não havia nada a consolidar, se for o caso.

**Regra de conclusão:** uma história ou funcionalidade só pode receber estado `concluida` quando os critérios de aceitação forem atendidos, a revisão estiver aprovada, a Definição de Concluído estiver satisfeita e a consolidação tiver sido verificada. Se nenhuma atualização global for necessária, registrar `consolidacao:sem-atualizacao` com justificativa. Quando houver mudança global semântica, ela precisa ser aprovada; uma pendência bloqueadora impede a conclusão.

#### Requisitos não funcionais e preocupações transversais

Não obrigar todo requisito não funcional a viver em um único arquivo. Sammy deve manter cada NFR no lugar em que ele possa ser entendido e verificado:

- Como requisito transversal do produto, em `produto.md`, `arquitetura.md`, `dados.md` ou `principios.md`.
- Como condição específica de uma história, nos critérios de aceitação daquela história.
- Como regra que se aplica a toda entrega, em `definicao-de-concluido.md`.
- Como decisão de implementação de uma funcionalidade, em `desenho-tecnico.md`.

Todo NFR relevante deve ter uma forma de verificação, responsável e escopo. Não permitir que requisitos de segurança, desempenho, privacidade, acessibilidade, disponibilidade ou auditabilidade desapareçam entre documentos.

#### Arquivamento das especificações antigas

Manter as especificações de histórias enquanto forem úteis para manutenção, auditoria e rastreabilidade. Quando se tornarem obsoletas por mudança substancial do produto, Sammy pode propor arquivamento, preservando o histórico Git, os identificadores e os vínculos com Issues/commits. Não excluir automaticamente especificações que sustentem decisões ou obrigações de conformidade.

#### O que adotar e o que não adotar do AgileSpec

| Ideia da referência | Decisão neste framework | Justificativa |
|---|---|---|
| Dois níveis de especificação: projeto e história | **Adotar** | Ajuda a separar contexto duradouro de decisões locais. |
| Loop de alinhamento após cada entrega | **Adotar** | Evita que a arquitetura global envelheça enquanto histórias são implementadas. |
| Critérios separados por casos normais e extremos | **Adotar** | Melhora cobertura de comportamento e testes. |
| `views.md` e `tables.md` opcionais | **Adaptar** para `interface.md` e `alteracoes-de-dados.md` em português | Só criar quando a história realmente alterar UI ou dados. |
| Documentos globais de interface e persistência | **Adotar de forma condicional** | Convenções reutilizáveis não devem ser duplicadas em cada história. |
| Não exigir lista de tarefas detalhada | **Não adotar como padrão** | Nosso fluxo usa tarefas pequenas, dependências e evidências para execução controlada; projetos pequenos podem simplificar. |
| Tratar backlog apenas como lista de histórias | **Adaptar** | Nosso backlog mantém épicos, funcionalidades, histórias e rastreabilidade entre níveis. |
| Não incluir eventos Scrum no escopo | **Adotar como separação conceitual** | SDD e gestão ágil são complementares; sprints são opcionais e dependem de equipe/capacidade confirmadas. |
| Consolidar depois de cada história validada | **Adotar com gate** | Sammy prepara a consolidação; a aprovação humana continua obrigatória para mudanças semânticas globais. |


---
