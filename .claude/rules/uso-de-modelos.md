# Modelos, esforço e contexto

- Consulte `configuracao/politica-de-modelos.yaml` antes de delegar.
- Prefira scripts para operações determinísticas.
- Use o menor contexto suficiente e limite os retornos dos subagentes.
- Selecione modelo e esforço por chamada de subagente quando suportado.
- Corrija contexto/ferramentas antes de promover modelo.
- Nunca use modelo barato para substituir controle obrigatório, teste, revisão ou aprovação.
- Não tente trocar o modelo da sessão principal automaticamente a cada tarefa.
