---
name: hora-de-trabalhar
description: "Ativa Sammy explicitamente. Sammy reconhece o repositório, consulta estado e manifesto, avalia contexto e inicia a próxima atividade segura sem exigir briefing inicial."
disable-model-invocation: true
---

# Sammy, hora de trabalhar

Execute o protocolo de ativação descrito em `.claude/agents/sammy.md` e no `MANUAL-DE-USO-DO-SAMMY.md`.

1. Identifique a raiz do repositório e leia `CLAUDE.md`.
2. Consulte `configuracao/configuracao-do-workflow.json` e a política de modelos configurada.
3. Verifique branch, alterações locais, documentos, estados, manifesto, aprovações, pendências e integrações.
4. Identifique se este é o repositório do framework ou um projeto consumidor.
5. Faça triagem inicial proporcional; não confunda ausência de informação com baixo risco.
6. Escolha a próxima ação segura e os especialistas realmente necessários.
7. Continue atividades independentes; agrupe perguntas que exijam decisão humana.
8. Não publique nem execute operação remota sem autorização.
9. Atualize registros de execução e apresente um resumo objetivo.
