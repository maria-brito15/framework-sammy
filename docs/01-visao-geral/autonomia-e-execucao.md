<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 980–1234. -->

> **Nesta página:** Política de autonomia, aprovações, manifesto, reprocessamento, qualidade, autocorreção e exemplos.

[← Voltar ao índice da documentação](../README.md)

---

### Política de autonomia e intervenções humanas

O framework deve automatizar a maior parte do trabalho operacional, mas distinguir geração, decisão e efeitos externos.

#### Matriz de autonomia

| Ação | Automática por padrão? | Condição |
|---|---|---|
| Inventariar arquivos e calcular hashes | Sim | Leitura local |
| Extrair texto, tabelas e metadados de PDFs | Sim | Sem sobrescrever fontes |
| Analisar requisitos e dados | Sim | Resultados identificados como rascunho |
| Criar e preencher templates | Sim | Arquivos de rascunho ou não aprovados |
| Gerar arquitetura e backlog preliminares | Sim | Propostas claramente marcadas |
| Validar IDs, links, schemas e dependências | Sim | Scripts determinísticos |
| Corrigir formatação e referências mecânicas | Sim | Sem alterar significado |
| Corrigir duplicações ou agrupamentos semânticos | Propor; pode corrigir rascunho | Registrar o motivo e preservar diff |
| Escolher regra de negócio ausente | Não | Decisão humana |
| Escolher entre fontes contraditórias | Não | Responsável do domínio decide |
| Aprovar arquitetura, escopo ou requisitos | Não | Gate humano explícito |
| Criar Issues após backlog aprovado | Sim, se houver autorização prévia | Política de publicação habilitada |
| Criar ou modificar Project/labels/campos | Sim, se houver autorização prévia | Descobrir recursos existentes antes |
| Atribuir pessoas e estimativas comprometidas | Não | Exige equipe e capacidade reais |
| Excluir Issues, arquivar itens ou remover labels manuais | Não | Confirmação específica |
| Executar migrações ou deploy em ambiente real | Não por padrão | Autorização e política própria de implantação |

#### Aprovação por pacote, não por arquivo

Para evitar excesso de interrupções, o agente deve agrupar a revisão por decisão:

- **Pacote de diagnóstico:** fontes, interpretação, lacunas e conflitos.
- **Pacote de planejamento:** arquitetura, equipes, fases, premissas e riscos.
- **Pacote de backlog:** histórias, épicos, funcionalidades, prioridade preliminar e dependências.

A pessoa revisa o pacote e comenta os pontos relevantes. Não precisa aprovar cada arquivo individualmente quando fazem parte da mesma decisão. As aprovações continuam ligadas aos hashes dos artefatos exatos que foram revisados.

#### Perguntas inteligentes

O agente não deve perguntar tudo o que está ausente. Deve classificar cada dúvida:

- **Bloqueadora:** a resposta altera escopo, regra de negócio, segurança, arquitetura, modelo de dados ou compromisso relevante. Interromper e perguntar.
- **Importante, mas não bloqueadora:** registrar uma recomendação e uma alternativa; continuar o trabalho que não depende dela.
- **Baixo impacto:** usar um padrão documentado e reversível, registrar como premissa e permitir alteração posterior.
- **Não aplicável:** omitir a seção ou registrar justificativa sucinta.

Quando houver várias perguntas bloqueadoras, apresentar uma lista agrupada com contexto, alternativas e impacto, em vez de fazer perguntas repetitivas em várias rodadas. Não oferecer dezenas de escolhas técnicas sem explicar a consequência de cada uma.

#### Autorizações persistentes

A pessoa pode autorizar uma classe de operações uma única vez, por exemplo: “Após backlog aprovado, publicar automaticamente Issues e adicioná-las ao Project configurado”. Essa autorização deve ser registrada em configuração versionada, com escopo explícito.

Uma autorização persistente não pode abranger ações destrutivas não previstas, como apagar Issues, excluir campos, remover labels manuais ou alterar permissões da organização.
### Motor de execução incremental e prevenção de retrabalho

O framework deve saber o que já fez, o que mudou e o que realmente precisa ser recalculado. Reexecutar tudo a cada comando desperdiça tokens, tempo e aumenta o risco de alterações desnecessárias.

#### Manifesto da execução

Criar:

```text
plano/
└── controle/
    ├── execucao.json
    ├── grafo-dependencias.json
    ├── triagem.md
    ├── politica-de-modelos.yaml
    ├── modelo-de-execucao.json
    ├── decisoes-pendentes.md
    ├── relatorio-da-ultima-execucao.md
    └── cache/
        ├── extracao-requisitos.json
        ├── extracao-modelo-de-dados.json
        └── analises-intermediarias/
```

`execucao.json` deve registrar:

- versão do formato do manifesto;
- versão do framework;
- identificador e horário da execução;
- modo de operação;
- hashes dos arquivos de entrada;
- hash dos templates e configurações relevantes;
- etapas concluídas e seus artefatos;
- agentes e scripts acionados;
- resultados da validação;
- aprovações associadas aos hashes exatos;
- estado da integração GitHub;
- erros e operações que podem ser retomadas.

#### Hashes e reprocessamento seletivo

O script deve calcular hashes dos arquivos de entrada e artefatos. Se um PDF não mudou, não é necessário extrair e analisar novamente seu conteúdo integral. Se o modelo de dados mudou, reprocessar a análise de dados e os artefatos dependentes; não refazer automaticamente o diagnóstico de produto inteiro sem necessidade.

Exemplo de dependências:

| Mudança | Etapas que podem exigir reprocessamento |
|---|---|
| `requisitos.pdf` | Extração de requisitos, diagnóstico, histórias, épicos, funcionalidades, rastreabilidade e specs afetadas |
| `modelo-de-dados.pdf` | Extração do modelo, diagnóstico de dados, arquitetura, funcionalidades e specs que usam as entidades afetadas |
| `plano/arquitetura.md` | Funcionalidades e desenhos técnicos dependentes, decisões e auditoria arquitetural |
| Uma história | Épicos relacionados, funcionalidades relacionadas e rastreabilidade |
| Uma funcionalidade | Especificação, tarefas, Issue correspondente e dependências afetadas |
| Template de Issue | Próximas publicações ou atualizações, sem regenerar requisitos |

A invalidação deve ser seletiva. Uma mudança em um documento não deve apagar todos os artefatos ou aprovações do projeto.

#### Aprovação vinculada à versão

Uma aprovação deve guardar o hash dos arquivos aprovados. Se um artefato aprovado for alterado, a aprovação daquela versão deixa de ser válida. O motor determina quais aprovações dependentes precisam ser reabertas.

Exemplo:

```json
{
  "artefato": "plano/arquitetura.md",
  "estado": "aprovado",
  "hash_aprovado": "sha256:...",
  "aprovador": "responsavel-do-projeto",
  "aprovado_em": "2026-11-26T18:00:00-03:00",
  "commit": "abc123",
  "dependencias": ["plano/diagnostico.md"]
}
```

Esse registro é ilustrativo. O formato definitivo deve ser validado por schema e não deve armazenar dados pessoais desnecessários.

#### Retomada segura

`/continuar-projeto` deve:

1. Ler o manifesto e o estado.
2. Identificar a execução interrompida.
3. Verificar se as fontes ou artefatos mudaram desde a última etapa.
4. Identificar operações completadas, parcialmente concluídas e pendentes.
5. Retomar a primeira etapa segura, sem duplicar operações.
6. Não repetir publicação remota já confirmada.
7. Informar somente bloqueios que realmente impedem o avanço.
### Ciclo automático de qualidade e autocorreção

A auditoria não deve simplesmente listar problemas e exigir que a pessoa corrija manualmente todos os detalhes. O framework deve corrigir automaticamente o que for seguro, e escalar decisões semânticas.

#### Ciclo de qualidade

```text
Gerar artefatos em rascunho
        ↓
Validar estrutura com scripts
        ↓
Auditar conteúdo com agente independente
        ↓
Classificar achados
        ↓
+----------------------+----------------------+
| Falha mecânica       | Decisão semântica    |
|                      |                      |
| Corrigir em rascunho | Registrar e perguntar|
+----------------------+----------------------+
        ↓
Revalidar dependências afetadas
        ↓
Relatório consolidado
```

#### Classificação dos achados

| Tipo | Exemplo | Tratamento |
|---|---|---|
| Erro estrutural | ID duplicado, seção obrigatória ausente | Corrigir automaticamente e validar novamente |
| Erro de referência | História aponta para épico inexistente | Corrigir se a relação for inequívoca; caso contrário, registrar dúvida |
| Inconsistência mecânica | Label sem configuração ou campo inválido | Ajustar configuração local ou apontar incompatibilidade |
| Lacuna de cobertura | Requisito sem história relacionada | Propor história e justificar, sem aprovar automaticamente |
| Contradição de negócio | Dois documentos definem comportamentos diferentes | Bloquear e solicitar decisão |
| Decisão arquitetural ausente | Não há definição de consistência ou integração | Apresentar opções e consequências |
| História muito grande | Muitos fluxos independentes | Sugerir divisões verticais e explicar valor de cada parte |
| Critério de aceite vago | “Deve ser rápido” | Sugerir tornar mensurável; não inventar meta numérica |
| Estimativa sem evidência | Agente atribui pontos sem dados da equipe | Remover estimativa comprometida e marcar não estimada |

#### Limites de autocorreção

- Executar no máximo duas rodadas automáticas de correção semântica em rascunhos; depois apresentar os achados restantes.
- Correções puramente mecânicas podem ser repetidas enquanto forem idempotentes e não alterarem conteúdo aprovado.
- Não corrigir automaticamente regras de negócio, prioridades críticas, metas quantitativas, arquitetura aprovada ou decisões de segurança.
- Sempre mostrar resumo das correções automáticas e manter diff versionado.
- Se a autocorreção gerar nova inconsistência, interromper o ciclo e registrar falha.

#### Relatório de qualidade

```markdown
# Relatório de qualidade do planejamento

- Execução:
- Perfil de rigor:
- Fontes utilizadas:
- Resultado: Aprovável | Aprovável com ressalvas | Não aprovável

## Cobertura
- Requisitos com rastreabilidade:
- Requisitos sem história:
- Histórias sem épico:
- Épicos sem funcionalidade:
- Funcionalidades sem requisitos de origem:

## Validações automáticas
| Verificação | Resultado | Evidência |
|---|---|---|
| IDs únicos | PASS/FAIL | ... |
| Referências válidas | PASS/FAIL | ... |
| Dependências sem ciclos | PASS/FAIL | ... |
| Critérios verificáveis | PASS/FAIL/REVISAR | ... |

## Correções automáticas
- ...

## Decisões humanas necessárias
- ...

## Riscos aceitos ou pendentes
- ...

## Próxima etapa segura
- ...
```
### Casos de funcionamento automatizado

A cada ativação por `/hora-de-trabalhar`, Sammy deve adaptar sua execução conforme a situação encontrada.

| Caso | Comportamento automático | Quando interromper |
|---|---|---|
| Projeto novo, documentos completos | Fazer triagem, analisar fontes, gerar todos os rascunhos e auditar em sequência | Gates de diagnóstico, decisões arquiteturais e backlog |
| Projeto novo, requisitos vagos | Gerar diagnóstico parcial, listar ambiguidades e propor opções | Quando a resposta alterar escopo ou regras essenciais |
| Projeto existente com código | Inspecionar estrutura, dependências, testes, migrações e padrões antes de propor arquitetura | Se documentação e implementação divergirem materialmente |
| Projeto com modelo de dados ausente | Continuar análise de produto e marcar modelagem como pendente | Antes de aprovar arquitetura que dependa do modelo |
| PDFs contraditórios | Comparar evidências, listar conflitos e impactos | Sempre que não houver precedência documentada |
| Projeto de alto risco | Selecionar perfil rigoroso e aplicar controles extras | Decisões de segurança, integridade, compliance e operação |
| Projeto pequeno e isolado | Usar perfil leve e reduzir documentos opcionais | Somente se uma decisão relevante permanecer ambígua |
| Mudança em um requisito aprovado | Detectar dependências e reprocessar somente os artefatos afetados | Aprovação dos artefatos cuja semântica foi alterada |
| Falha parcial ao publicar Issues | Retomar usando o mapeamento e verificar o que já foi criado | Se houver conflito com edição humana ou identidade ambígua |
| GitHub indisponível | Concluir geração e validações locais; registrar sincronização pendente | Não bloquear o planejamento local por falha externa |

#### Exemplo: projeto novo com documentos completos

Uma única execução prepara diagnóstico, arquitetura, equipes, fases e backlog. O agente apresenta um pacote consolidado, não seis relatórios separados em momentos diferentes. Depois da aprovação, publica os itens no GitHub se essa autorização estiver configurada.

#### Exemplo: documentação incompleta

O sistema não bloqueia todo o trabalho porque uma informação está ausente. Ele continua as partes independentes, cria uma lista de decisões pendentes e identifica exatamente quais artefatos não podem ser concluídos sem respostas.

#### Exemplo: alteração no modelo de dados

O sistema compara o hash, detecta o arquivo alterado, reextrai apenas o modelo, encontra entidades e relações impactadas e reavalia arquitetura, funcionalidades e especificações dependentes. Histórias não relacionadas não devem ser regeneradas indiscriminadamente.

#### Exemplo: sincronização repetida

Se `/publicar-no-github` for executado novamente, o sistema identifica Issues pelo mapeamento e pelos IDs estáveis, compara os campos gerenciados e não cria duplicatas. Se alguém editou manualmente um campo controlado pelo time, o sistema mostra o conflito e preserva a alteração até haver decisão.
