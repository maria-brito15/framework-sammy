# Framework Sammy

Framework de orquestração de engenharia com Spec-Driven Development (SDD) para Claude Code.

- **Agente principal:** Sammy
- **Ativação explícita:** `/hora-de-trabalhar`
- **Idioma operacional:** português brasileiro
- **Branch de desenvolvimento sugerida:** `feat/desenvolvimento-framework-sammy`

## O que é

Sammy é o ponto único de contato com a pessoa usuária. Ao ser ativado, reconhece o repositório, investiga documentos e estado, identifica o próximo trabalho seguro, escolhe especialistas e Skills, aplica a estratégia adaptativa e apresenta resultados ou decisões necessárias.

Este repositório contém a implementação em evolução: agente principal, subagentes, Skills, regras, configurações, templates, scripts, schemas, testes e automações.

## Comece

1. Leia [visão e princípios](docs/01-visao-geral/visao-e-principios.md).
2. Use o [índice da documentação](docs/README.md) para encontrar o assunto desejado.
3. Siga [implantação, validação e evolução](docs/06-operacao/implantacao-validacao-evolucao.md).
4. Para contribuir, consulte [CONTRIBUTING.md](CONTRIBUTING.md).

Para desenvolver o próprio framework:

```bash
git checkout -b feat/desenvolvimento-framework-sammy
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python scripts/verificar_repositorio.py
python scripts/validar_modelos.py
python -m unittest discover -s tests -v
```

Abra a raiz no Claude Code e inicie Sammy:

```bash
claude --agent sammy
```

Depois, invoque `/hora-de-trabalhar`.

## Rotas rápidas

| Necessidade | Destino |
|---|---|
| Como usar e ativar Sammy | [Visão e princípios](docs/01-visao-geral/visao-e-principios.md) |
| Como Sammy escolhe rigor e estratégia | [Triagem adaptativa](docs/01-visao-geral/triagem-adaptativa.md) |
| Como funciona o backlog | [Planejamento](docs/02-planejamento/backlog-e-planejamento.md) |
| Como funciona o SDD | [Especificações](docs/03-sdd/especificacao-e-alinhamento.md) |
| Como configurar agentes e Skills | [Claude Code](docs/04-claude-code/agentes-skills-contexto.md) |
| Como controlar modelos e tokens | [Gerenciamento de modelos](docs/07-modelos/gerenciamento-de-modelos.md) |
| Como integrar GitHub | [GitHub e automações](docs/05-integracoes/github-e-automacoes.md) |
| Onde encontrar templates | [Catálogo de modelos](docs/README.md#catalogo-de-modelos) |

## Estado atual

Esta é uma base inicial em desenvolvimento, não uma implementação completa de todas as capacidades descritas. A delegação e a geração de artefatos dependem do Claude Code e das instruções dos agentes/Skills. A integração mutável com GitHub permanece desabilitada por padrão; os gates de aprovação continuam humanos. Consulte [implantação e evolução](docs/06-operacao/implantacao-validacao-evolucao.md) para limites e próximos incrementos.

## Validações locais

```bash
python scripts/verificar_repositorio.py
python scripts/validar_planejamento.py --raiz .
python scripts/validar_modelos.py
python -m unittest discover -s tests -v
```

## Licença

Nenhuma licença de distribuição foi escolhida neste pacote. Defina a licença antes de tornar o repositório público.
