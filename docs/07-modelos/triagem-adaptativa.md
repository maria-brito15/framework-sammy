<!-- Conteúdo reorganizado do Manual de Uso do Sammy. Trecho de origem: linhas 4956–5231. -->

> **Nesta página:** Contratos, esquemas, estratégias, casos de avaliação e calibração do motor adaptativo.

[← Voltar ao índice da documentação](../README.md)

---

## Decisões aprovadas
- DEC-xxx — ...

## Apêndice F — Triagem adaptativa e avaliação de execução

Este apêndice transforma a política descrita na Parte I em artefatos de implementação e em um procedimento de calibração. O objetivo é permitir que o comportamento adaptativo de Sammy seja testado, auditado e evoluído sem depender apenas de instruções em linguagem natural.

### F.1 Contrato do motor de triagem

O motor recebe um contexto estruturado e devolve uma classificação explicável. Sammy é responsável pela interpretação das evidências; scripts aplicam regras determinísticas e validam a estrutura.

**Entradas mínimas:**

- descrição da solicitação;
- tipo de trabalho identificado;
- estado do repositório;
- fontes/documentos e hashes;
- evidências para as sete dimensões de risco;
- sinais usados para estimar porte;
- políticas globais do projeto;
- condições críticas identificadas;
- modo de autonomia configurado.

**Saídas mínimas:**

- porte do projeto e confiança da avaliação;
- pontuação e justificativa por dimensão;
- condições críticas e desconhecidos;
- rigor-base do projeto;
- rigor local da unidade;
- autonomia permitida;
- granularidade escolhida;
- templates, agentes, validações e gates selecionados;
- perguntas bloqueadoras e premissas reversíveis;
- eventos que devem disparar reavaliação.

### F.2 Modelo de dados da triagem

Arquivo: `schemas/triagem.schema.json` (a implementar).

O schema deve validar tipos, enums, faixas numéricas e campos obrigatórios. Exemplo de payload:

```json
{
  "versao": 1,
  "id": "TRI-001",
  "escopo": "projeto",
  "tipo_trabalho": "projeto_novo",
  "porte": {
    "valor": "medio",
    "confianca": "media",
    "evidencias": ["Dois domínios relacionados", "Três integrações identificadas"]
  },
  "rigor": {
    "valor": "padrao",
    "pontuacao": 7,
    "maximo": 14,
    "dimensoes": [
      {"id": "dominio", "nota": 1, "evidencia": "Regras moderadas", "justificativa": "Fluxos relacionados"},
      {"id": "dados_seguranca", "nota": 1, "evidencia": "Dados pessoais comuns", "justificativa": "Permissões usuais"},
      {"id": "integracoes", "nota": 1, "evidencia": "Duas APIs externas", "justificativa": "Sem efeito financeiro direto"},
      {"id": "incerteza", "nota": 1, "evidencia": "Duas regras pendentes", "justificativa": "Não bloqueiam o diagnóstico"},
      {"id": "complexidade_tecnica", "nota": 1, "evidencia": "Frontend e API", "justificativa": "Arquitetura conhecida"},
      {"id": "organizacao", "nota": 1, "evidencia": "Duas frentes", "justificativa": "Coordenação moderada"},
      {"id": "impacto_falha", "nota": 1, "evidencia": "Indisponibilidade limitada", "justificativa": "Recuperação simples"}
    ],
    "condicoes_criticas": [],
    "desconhecidos": []
  },
  "autonomia": "controlada",
  "granularidade": "projeto",
  "politicas_globais_aplicaveis": ["idioma_pt_br", "rastreabilidade", "aprovacoes_humanas"],
  "decisoes_pendentes": [],
  "reavaliar_quando": ["fonte_alterada", "escopo_alterado", "nova_integracao"]
}
```

O exemplo contém valores fictícios para demonstrar a estrutura. Não deve ser usado como avaliação real sem evidências do projeto.

### F.3 Modelo da estratégia de execução por unidade

Arquivo: `schemas/estrategia-de-execucao.schema.json` (a implementar).

Cada unidade recebe uma estratégia que pode divergir do perfil-base do projeto:

```json
{
  "versao": 1,
  "execucao_id": "EXEC-001",
  "projeto": {
    "porte": "grande",
    "rigor_base": "rigoroso",
    "autonomia": "controlada"
  },
  "unidade": {
    "id": "FUNC-021",
    "tipo": "funcionalidade",
    "rigor_local": "leve",
    "granularidade_local": "historia_tarefa"
  },
  "controles_globais": [
    "convencoes_de_codigo",
    "rastreabilidade",
    "autenticacao_existente",
    "testes_de_regressao_pertinentes"
  ],
  "controles_locais": [
    "validacao_visual",
    "teste_do_componente_afetado"
  ],
  "templates": ["descricao_mudanca", "criterios_de_aceitacao"],
  "agentes": [],
  "validacoes": ["lint_afetado", "teste_especifico"],
  "gates": ["revisao_da_mudanca"],
  "justificativa": "Mudança isolada, sem alteração de regras, dados ou permissões."
}
```

Este exemplo demonstra como um projeto de rigor-base rigoroso pode ter uma alteração local leve sem remover controles globais aplicáveis.

### F.4 Modelo de caso de avaliação da triagem

Arquivo: `avaliacoes/casos/AVAL-001.yaml`.

```yaml
id: AVAL-001
nome: alteracao-visual-isolada-em-sistema-critico
contexto:
  porte_projeto: grande
  rigor_base: rigoroso
  solicitacao: "Alterar o texto de um botão sem mudar comportamento."
  impacto_em_dados: false
  impacto_em_permissoes: false
  impacto_em_integracoes: false
resultado_esperado:
  rigor_local: leve
  granularidade_local: historia_tarefa
  controles_globais_preservados: true
  agentes_esperados: []
  validacoes_esperadas:
    - teste-ou-verificacao-do-componente
  gates_esperados:
    - revisao-proporcional
acoes_proibidas:
  - replanejar-o-projeto-inteiro
  - gerar-arquitetura-completa
  - remover-controles-globais
```

### F.5 Bateria mínima de calibração

A bateria inicial deve cobrir pelo menos:

1. projeto pequeno, baixo risco e fontes claras;
2. projeto pequeno com condição crítica;
3. produto médio com várias integrações;
4. produto grande com múltiplas equipes;
5. protótipo exploratório sem compromisso de produção;
6. alteração local leve em projeto de rigor alto;
7. funcionalidade de segurança em projeto de rigor baixo;
8. migração de dados com risco de perda;
9. requisitos contraditórios;
10. dimensão crítica desconhecida;
11. mudança de escopo depois de aprovação;
12. alteração que não afeta artefatos previamente aprovados;
13. reprocessamento sem alteração de entradas;
14. publicação remota sem autorização;
15. agente especialista indisponível ou resultado inconclusivo.

Cada caso deve especificar: entradas, evidências, classificação esperada, templates selecionados, agentes previstos, validações, gates, perguntas esperadas e ações proibidas.

### F.6 Critérios de aceitação do motor adaptativo

O motor só pode ser considerado utilizável quando:

- não atribuir nota zero a dimensão desconhecida;
- registrar justificativa e evidência para cada nota atribuída;
- identificar condições críticas independentemente da pontuação;
- separar porte, rigor, autonomia e granularidade;
- permitir rigor local diferente do rigor-base sem remover controles globais;
- selecionar somente templates existentes e aplicáveis;
- evitar acionar agentes sem contribuição necessária;
- reavaliar diante dos eventos configurados;
- preservar histórico e justificativa de alterações de estratégia;
- impedir redução silenciosa de rigor após condição crítica;
- passar pela bateria de cenários críticos sem falso nível leve;
- produzir relatório legível e dados estruturados equivalentes.

### F.7 Procedimento de calibração durante o piloto

1. Executar a bateria de casos com o motor em modo de simulação.
2. Comparar classificações e ações com os resultados esperados.
3. Analisar falsos leves, excesso de processo, perguntas desnecessárias e custo.
4. Ajustar pesos, limiares, condições críticas e catálogo de templates.
5. Reexecutar toda a bateria após cada alteração.
6. Registrar versão da política e resultados da avaliação.
7. Habilitar o modo operacional inicialmente em um repositório-laboratório.
8. Só depois considerar o uso em projetos reais.

A política não deve ser ajustada para “passar” em um único exemplo. Deve funcionar em um conjunto variado de casos, inclusive casos-limite e situações com informações incompletas.

### F.8 Registro de mudança da política adaptativa

```markdown
# Alteração da política adaptativa — POL-001

- Versão anterior:
- Versão nova:
- Responsável:
- Data:

## Motivo
...

## Evidências observadas
- Casos de avaliação afetados:
- Falsos leves ou excesso de processo:
- Custo/latência:

## Regra alterada
...

## Impacto esperado
...

## Resultados da bateria de avaliação
- Casos aprovados:
- Casos reprovados:
- Pendências conhecidas:

## Aprovação
- Decisor:
- Data:
```

## Referências
- [Links para diagramas, schemas e migrations]
```

#### Template de `.ia/contexto/interface.md`

```markdown
# Diretrizes globais de interface

## Princípios de experiência
- Público e contexto de uso:
- Princípios de consistência:

## Estrutura e navegação
- Navegação global:
- Padrões de layout:
- Responsividade:

## Componentes e linguagem visual
- Biblioteca/design system:
- Tipografia e tokens:
- Componentes compartilhados:

## Estados e feedback
- Carregamento:
- Estado vazio:
- Sucesso:
- Erro e recuperação:

## Acessibilidade
- Navegação por teclado:
- Contraste e foco:
- Semântica e leitores de tela:

## Decisões aprovadas
- DEC-xxx — ...

## Referências
- [Design system, protótipos e componentes]
```
