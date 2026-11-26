---
name: validar-planejamento
description: "Executa validações estruturais determinísticas e auditoria semântica dos documentos de planejamento e backlog."
user-invocable: false
---

# Validar planejamento

1. Execute `python scripts/validar_planejamento.py --raiz .`.
2. Verifique IDs duplicados, referências quebradas, seções obrigatórias aplicáveis e dependências.
3. Acione auditor em contexto independente para semântica.
4. Separe erro bloqueador, alerta e observação.
5. Corrija apenas problemas mecânicos seguros.
6. Não altere decisões de produto ou arquitetura sem confirmação.
7. Gere relatório de validação.
