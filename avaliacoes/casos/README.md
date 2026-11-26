# Casos de avaliação do Sammy

Use estes cenários como especificações de teste. A pessoa avaliadora deve registrar a classificação esperada e comparar com a decisão de Sammy. Os casos abaixo são descrições, não testes automáticos de julgamento semântico.

1. Projeto pequeno e bem definido — espera-se rigor leve ou padrão conforme risco.
2. Sistema financeiro de grande porte — rigor rigoroso em capacidades financeiras.
3. Correção visual isolada em sistema crítico — rigor local leve, preservando controles globais.
4. Requisitos vagos — não converter desconhecido em zero; investigar e perguntar somente decisões bloqueadoras.
5. Modelo de dados contraditório — registrar conflito e não escolher silenciosamente.
6. Repositório legado com baixa documentação — inspecionar código, testes e migrations.
7. Migração com risco de perda — elevar rigor e exigir estratégia de reversão/reconciliação.
8. Alteração incremental em um requisito — reprocessar somente descendentes afetados.
9. Reexecução sem mudanças — idempotência e nenhum item duplicado.
10. GitHub configurado sem autorização de publicação — produzir plano, não executar mutações.
11. Modelo barato retorna resultado incompleto por falta de contexto — corrigir contexto antes de promover modelo.
12. Modelo adequado usa esforço insuficiente — aumentar esforço antes de trocar família.
13. Conflito entre requisito aprovado e steering — parar e propor correção controlada.
14. Sem trabalho pendente após ativação — apresentar estado e perguntar objetivo.
15. Feature com integração de terceiros e dados sensíveis — rigor local elevado, especialistas e auditoria pertinentes.
