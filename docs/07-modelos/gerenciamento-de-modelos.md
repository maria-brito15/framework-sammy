<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 7097–7365. -->

> **Nesta página:** Política configurável de modelos, roteamento por tarefa, esforço, contexto, custos e testes.

[← Voltar ao índice da documentação](../README.md)

---

## Apêndice G — Gerenciamento adaptativo de modelos, esforço e contexto

Este apêndice contém os arquivos de referência para implementar a política descrita na Parte I. Os nomes de campos de configuração permanecem na forma exigida pelo Claude Code; as instruções e descrições são escritas em português.

### G.1 Arquivo de política de modelos

Arquivo: `plano/controle/politica-de-modelos.yaml`

```yaml
versao: 1
modo: equilibrado # economico | equilibrado | qualidade-prioritaria

modelos_permitidos:
  - haiku
  - sonnet
  - opus
  - fable # opcional; somente se disponível para a conta/provedor

modelo_sammy:
  estrategia: modelo-da-sessao
  recomendacao_inicial: sonnet
  permitir_troca_automatica_da_sessao: false

roteamento:
  operacao_deterministica:
    executor: script
    modelo: nenhum

  triagem_simples:
    modelo: haiku
    esforco: low
    max_turns: 4

  analise_padrao:
    modelo: sonnet
    esforco: medium
    max_turns: 10

  arquitetura_critica:
    modelo: opus
    esforco: high
    max_turns: 16

  investigacao_excepcional:
    modelo: fable
    esforco: padrao-do-modelo
    max_turns: 20
    habilitado: false

limites:
  max_subagentes_simultaneos: 3
  permitir_delegacao_em_cascata: false
  exigir_motivo_para_promocao: true
  tentativas_antes_de_promover_modelo: 2
  preservar_gates_humanos: true

regras:
  - id: MOD-001
    quando: "a tarefa pode ser resolvida por parsing, comparação, cálculo ou validação determinística"
    acao: usar_script
  - id: MOD-002
    quando: "a tarefa é curta, delimitada e de baixo risco"
    acao: usar_haiku_com_baixo_esforco
  - id: MOD-003
    quando: "a tarefa exige análise ou implementação comum"
    acao: usar_sonnet_com_esforco_padrao
  - id: MOD-004
    quando: "a tarefa envolve arquitetura complexa, segurança ou dados críticos"
    acao: usar_opus_com_esforco_elevado
  - id: MOD-005
    quando: "o modelo falhou por falta de contexto, arquivo ou permissão"
    acao: corrigir_contexto_ou_permissao_antes_de_promover_modelo
  - id: MOD-006
    quando: "o modelo recebeu contexto adequado e esforço suficiente, mas não atingiu a qualidade exigida"
    acao: promover_modelo_na_proxima_chamada_e_registrar_motivo
```

O arquivo é uma política de referência e deve ser validado por schema antes de ser usado. O script de política deve recusar aliases não permitidos, campos desconhecidos em propriedades críticas e níveis de esforço indisponíveis quando a compatibilidade puder ser verificada.

### G.2 Exemplo de subagente econômico

Arquivo: `.claude/agents/analista-de-arquivos.md`

```markdown
---
name: analista-de-arquivos
description: Faz triagem simples de arquivos já identificados, classifica conteúdo e devolve resumos curtos com referências.
model: haiku
effort: low
maxTurns: 4
tools:
  - Read
  - Grep
  - Glob
---

# Analista de arquivos

Você executa somente a análise delimitada solicitada por Sammy.

- Leia apenas os arquivos e trechos indicados.
- Não examine o repositório inteiro por iniciativa própria.
- Não altere arquivos.
- Não invente informações ausentes.
- Devolva uma síntese curta, caminhos consultados, evidências e dúvidas.
- Se o trabalho exigir julgamento arquitetural ou de negócio, sinalize a limitação e devolva a Sammy; não tente resolver ampliando o escopo.
```

### G.3 Exemplo de subagente de raciocínio complexo

Arquivo: `.claude/agents/arquiteto.md`

```markdown
---
name: arquiteto
description: Avalia arquitetura, limites de domínio, dependências, trade-offs e impactos técnicos de mudanças relevantes.
model: opus
effort: high
maxTurns: 16
tools:
  - Read
  - Grep
  - Glob
  - Bash
---

# Arquiteto de software

Analise somente o escopo delegado por Sammy.

- Utilize os requisitos e decisões aprovados como fontes prioritárias.
- Diferencie fatos, inferências, alternativas e recomendações.
- Registre trade-offs e consequências.
- Não implemente código.
- Não aprove o próprio desenho.
- Se uma decisão depender de regra de negócio não documentada, devolva a dúvida a Sammy.
- Entregue uma síntese executiva, decisões propostas, evidências e riscos.
```

O exemplo pressupõe que a conta e o provedor disponibilizem esses aliases e níveis de esforço. Ajustar a matriz à disponibilidade real antes de instalar.

### G.4 Contrato de decisão por chamada de agente

Antes de invocar um subagente, Sammy monta um registro semelhante a este:

```json
{
  "id_chamada": "CHAMADA-0042",
  "papel": "analista-de-dados",
  "objetivo": "avaliar impacto da entidade Pagamento",
  "modelo_solicitado": "sonnet",
  "esforco_solicitado": "medium",
  "motivo": "análise de domínio e persistência de complexidade intermediária",
  "fontes": [
    "documentos/entrada/modelo-de-dados.pdf",
    "planejamento/arquitetura.md"
  ],
  "escopo": {
    "permitir_edicao": false,
    "max_turns": 8,
    "formato_retorno": "sintese-com-evidencias"
  },
  "resultado": {
    "estado": "pendente",
    "modelo_efetivo": null,
    "esforco_efetivo": null,
    "precisou_promover": false,
    "motivo_promocao": null
  }
}
```

O modelo efetivo deve ser registrado somente após confirmação pela execução/telemetria disponível. O valor solicitado não prova que o provedor executou exatamente aquela versão do modelo.

### G.5 Contrato do resultado de um subagente

```markdown
# Resultado da análise

- Identificador da chamada:
- Especialista:
- Modelo/alias efetivo, se disponível:
- Esforço efetivo, se disponível:
- Estado: concluído | parcial | bloqueado | falha

## Conclusão
[Resposta objetiva ao objetivo delegado.]

## Evidências
- [Caminho/arquivo, seção ou linha relevante]

## Incertezas e limitações
- [Somente o que não pôde ser determinado.]

## Recomendação
[Próxima ação, se houver.]

## Próxima etapa sugerida
[Retorno a Sammy; não executar além do escopo.]
```

### G.6 Processo de promoção de modelo

1. Identificar a falha ou insuficiência do resultado.
2. Verificar se o agente recebeu as fontes corretas e contexto suficiente.
3. Verificar se as ferramentas e permissões necessárias estavam disponíveis.
4. Verificar se o agente executou as verificações solicitadas e respeitou `maxTurns`.
5. Se faltou contexto, ferramenta ou execução, corrigir isso e repetir sem trocar o modelo.
6. Se o trabalho foi executado corretamente, mas a qualidade ficou abaixo do critério por limite de capacidade, aumentar o esforço ou promover o modelo — uma variável por vez.
7. Repetir a tarefa com o mesmo contrato e registrar a diferença de resultado.
8. Se a segunda tentativa continuar insuficiente, Sammy deve interromper e apresentar o limite, sem escalar indefinidamente.

A promoção automática não pode transformar uma tarefa insegura em tarefa autorizada. Modelos mais capazes não recebem permissões adicionais.

### G.7 Controles de contexto

Checklist para Sammy antes de cada delegação:

- [ ] O objetivo está delimitado em uma frase?
- [ ] Foram enviados somente arquivos e trechos necessários?
- [ ] O subagente recebeu as decisões globais relevantes?
- [ ] Foram excluídos logs, pastas geradas e arquivos irrelevantes?
- [ ] O formato e o tamanho esperado do retorno foram definidos?
- [ ] O subagente precisa realmente de ferramentas de escrita ou `Bash`?
- [ ] A análise pode ser feita por script em vez de modelo?
- [ ] Existe outra chamada em andamento que já responde à mesma pergunta?
- [ ] O limite de turnos é proporcional à tarefa?

O conteúdo global de `CLAUDE.md` deve permanecer curto. Procedimentos extensos e referências especializadas devem ficar em Skills e arquivos carregados sob demanda, evitando enviar instruções repetidas em toda interação.

### G.8 Plano de testes do roteador de modelos

| Caso de avaliação | Resultado esperado |
|---|---|
| Calcular hashes de PDFs | Script; nenhuma chamada de modelo |
| Validar IDs e links entre Markdown | Script; modelo não necessário |
| Classificar uma lista pequena de arquivos | Haiku, esforço baixo ou médio |
| Gerar histórias a partir de requisitos claros | Sonnet, esforço padrão |
| Comparar duas alternativas arquiteturais | Opus, esforço alto |
| Revisar migração que afeta dados críticos | Opus e auditoria/testes independentes |
| Agente falha porque não recebeu o modelo de dados | Corrigir contexto, sem promover modelo |
| Agente executa tudo, mas não resolve contradição complexa | Promover a próxima chamada e registrar justificativa |
| Repositório contém milhares de linhas de logs | Delegar exploração isolada, resumir evidências; não despejar logs no contexto de Sammy |
| Muitos especialistas poderiam ser acionados | Limitar concorrência e chamar apenas os necessários |

Critérios de aceitação do gerenciamento de modelos:

- Nenhuma tarefa puramente determinística deve chamar um modelo sem justificativa.
- Toda chamada de subagente deve ter um objetivo e uma rota de modelo/esforço justificáveis.
- Promoções de modelo devem registrar motivo e resultado comparável.
- Sammy não deve trocar o modelo principal repetidamente para rotear subtarefas.
- Subagentes não devem delegar em cascata por padrão.
- O sistema deve respeitar a lista de modelos permitidos e limites do provedor.
- A redução de custo não pode reduzir a cobertura de requisitos, os controles críticos, a verificação ou os gates humanos.
- O framework deve conseguir operar mesmo quando um dos aliases recomendados não estiver disponível.

### G.9 Referências técnicas específicas

- [Claude Code — Model configuration](https://code.claude.com/docs/en/model-config) — aliases, seleção do modelo da sessão, esforço, fallback e configurações.
- [Claude Code — Subagents](https://code.claude.com/docs/en/sub-agents) — seleção de modelo e esforço por subagente, inclusive por invocação.
- [Claude Code — Skills](https://code.claude.com/docs/en/skills) — carregamento sob demanda, organização de instruções e custo de contexto.
- [Claude Academy — Choosing the right effort level in Claude Code](https://academy.claude.com/tutorials/choosing-the-right-effort-level-in-claude-code) — como distinguir necessidade de maior esforço de necessidade de um modelo mais capaz.
- [Anthropic — Choosing a Claude model and effort level in Claude Code](https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code) — recomendações práticas de seleção e calibração.


## Referências

As referências foram separadas entre fundamentos metodológicos, práticas de backlog e documentação das ferramentas. As recomendações do livro-base são distinguíveis das adaptações propostas para este framework.
