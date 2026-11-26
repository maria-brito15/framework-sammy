---
name: publicar-no-github
description: "Prepara publicação do backlog aprovado no GitHub Issues e Projects com sincronização idempotente."
disable-model-invocation: true
---

# Publicar no GitHub

1. Confirme backlog aprovado, configuração e destino.
2. Execute somente o planejador `scripts/planejar_sincronizacao_github.py` em modo de simulação.
3. Apresente operações que seriam criadas/atualizadas.
4. Não executar chamadas remotas até receber autorização explícita para o destino e escopo exatos.
5. A primeira versão deste pacote não implementa mutações remotas; informe essa limitação.
