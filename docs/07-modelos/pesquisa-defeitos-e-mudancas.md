<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 6116–6279. -->

> **Nesta página:** Templates para pesquisa técnica, defeitos, mudanças de escopo e débito técnico.

[← Voltar ao índice da documentação](../README.md)

---

## Apêndice D — Modelos de pesquisa, defeitos e mudanças

Nem todo item do backlog representa uma funcionalidade nova. Os modelos seguintes tratam de incerteza técnica, defeitos, alterações de escopo e débito técnico sem forçar esses casos a caber no formato de história de usuário.

### Templates adicionais para pesquisa, bugs, mudanças e débito técnico

#### Pesquisa técnica / spike

```markdown
## PESQ-001 — [Pergunta técnica]

**Motivo:** [Qual incerteza impede decisão ou estimativa?]
**Hipótese:** ...
**Escopo da pesquisa:** ...
**Fora de escopo:** ...
**Timebox proposto:** [validar com responsável]

### Questões a responder
- ...

### Experimentos
- ...

### Evidências coletadas
- ...

### Resultado
- ...

### Recomendação
- ...

### Decisões que podem ser tomadas após a pesquisa
- ...

### Limitações
- ...
```

Pesquisa não deve se transformar em implementação de produção sem uma especificação e uma decisão posteriores.

#### Correção de defeito

```markdown
## BUG-001 — [Comportamento incorreto]

**Severidade:** Crítica | Alta | Média | Baixa
**Ambiente/versão:** ...
**Origem:** ...

### Comportamento observado
...

### Comportamento esperado
...

### Passos para reproduzir
1. ...

### Impacto
- Usuários afetados:
- Dados afetados:
- Segurança/financeiro/operação:

### Evidências
- Logs:
- Capturas:
- IDs correlacionáveis sem dados sensíveis:

### Hipótese de causa
[Marcar como hipótese até confirmação.]

### Critério de correção
- [ ] ...

### Regressão a verificar
- ...
```

Correções pequenas e isoladas podem seguir processo leve. Defeitos que envolvam perda de dados, permissões, dinheiro ou segurança exigem análise mais rigorosa e revisão de impacto.

#### Solicitação de mudança de escopo

```markdown
## MUD-001 — [Título da mudança]

**Solicitante:** ...
**Data:** ...
**Status:** Proposta | Em análise | Aprovada | Rejeitada

### Necessidade e justificativa
...

### Artefatos afetados
- Requisitos:
- Histórias:
- Épicos:
- Funcionalidades:
- Arquitetura/dados:
- Fases/sprints:

### Impacto
- Valor:
- Prazo/capacidade:
- Custo/esforço:
- Risco:
- Segurança/operação:

### Alternativas
1. ...
2. ...

### Recomendação
...

### Decisão humana
...
```

#### Débito técnico

```markdown
## DEBITO-001 — [Problema técnico]

**Categoria:** Arquitetura | Segurança | Testes | Manutenibilidade | Performance | Infraestrutura
**Localização:** [módulo/arquivo/componente]
**Estado:** Identificado | Priorizado | Planejado | Em correção | Resolvido

### Problema atual
...

### Impacto
- Frequência:
- Efeito na entrega:
- Risco para dados/segurança/operação:

### Evidência
- ...

### Solução proposta
...

### Esforço e risco da correção
...

### Prioridade recomendada
[Justificar com impacto, frequência, risco e esforço; não usar fórmula como verdade absoluta.]

### Critérios de resolução
- [ ] ...

### Métrica antes/depois
- Antes:
- Meta:
```

Débito técnico deve ficar visível no backlog, ser reavaliado e competir por prioridade com novas funcionalidades. Não classificar toda preferência de refatoração como dívida prioritária.

---

## Apêndice E — Estados, aprovações e configuração da automação

Este apêndice reúne os arquivos operacionais necessários para o motor de orquestração: estados globais e por funcionalidade, histórico de aprovações, exceções controladas, skills operacionais, configuração, catálogo de modelos, manifesto de execução e resumo consolidado para revisão.
