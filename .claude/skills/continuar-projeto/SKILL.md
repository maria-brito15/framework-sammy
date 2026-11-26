---
name: continuar-projeto
description: "Retoma uma execução existente a partir de estado, manifesto, hashes, aprovações e dependências, sem repetir trabalho válido."
user-invocable: false
---

# Continuar projeto

1. Leia configuração, estado, manifesto, hashes e aprovações.
2. Detecte entradas e saídas alteradas.
3. Invalide apenas resultados dependentes das entradas modificadas.
4. Verifique se há operações externas concluídas para evitar duplicação.
5. Calcule a próxima etapa segura do grafo.
6. Execute etapas independentes e autorizadas.
7. Pare em gates, conflitos ou autorizações ausentes.
8. Atualize manifesto e resumo.
