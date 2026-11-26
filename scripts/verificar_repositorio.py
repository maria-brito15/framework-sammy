#!/usr/bin/env python3
"""Verificações locais da estrutura inicial do Framework Sammy."""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "CLAUDE.md", "MANUAL-DE-USO-DO-SAMMY.md", ".claude/settings.json",
    ".claude/agents/sammy.md", ".claude/skills/hora-de-trabalhar/SKILL.md",
    "configuracao/configuracao-do-workflow.json", "configuracao/politica-de-modelos.yaml",
    "modelos/catalogo.json", "scripts/validar_planejamento.py", "scripts/gerar_manifesto.py"
]

def main() -> int:
    errors=[]; warnings=[]
    for rel in REQUIRED:
        if not (ROOT/rel).is_file(): errors.append(f"Arquivo obrigatório ausente: {rel}")
    for rel in [".claude/settings.json", "configuracao/configuracao-do-workflow.json", "configuracao/catalogo-de-modelos.json", "configuracao/integracao-github.json", "modelos/catalogo.json", "schemas/triagem.schema.json"]:
        p=ROOT/rel
        if p.exists():
            try: json.loads(p.read_text(encoding="utf-8"))
            except Exception as e: errors.append(f"JSON inválido em {rel}: {e}")
    settings_path=ROOT/".claude/settings.json"
    if settings_path.exists():
        settings=json.loads(settings_path.read_text(encoding="utf-8"))
        if settings.get("agent") != "sammy": errors.append(".claude/settings.json deve definir agent=sammy")
    agent_path=ROOT/".claude/agents/sammy.md"
    if agent_path.exists() and "name: sammy" not in agent_path.read_text(encoding="utf-8")[:500]: errors.append("Frontmatter do agente Sammy não define name: sammy")
    skill_path=ROOT/".claude/skills/hora-de-trabalhar/SKILL.md"
    if skill_path.exists():
        content=skill_path.read_text(encoding="utf-8")[:1000]
        if "disable-model-invocation: true" not in content: errors.append("Skill de ativação deve exigir invocação explícita")
    # Verifica contratos mínimos de agentes e Skills do Claude Code.
    try:
        import yaml
        yaml_loader = yaml.safe_load
    except ImportError:
        yaml_loader = None
    for base, kind in [(ROOT/".claude/agents", "agente"), (ROOT/".claude/skills", "skill")]:
        for pth in base.rglob("*.md") if base.exists() else []:
            content=pth.read_text(encoding="utf-8")
            if not content.startswith("---\n"):
                errors.append(f"Frontmatter ausente em {pth.relative_to(ROOT)}")
                continue
            try:
                end=content.find("\n---",4)
                if end < 0: raise ValueError("fechamento --- ausente")
                raw=content[4:end]
                if yaml_loader:
                    meta=yaml_loader(raw) or {}
                    if not isinstance(meta,dict): raise ValueError("frontmatter precisa ser objeto YAML")
                    if not meta.get("name") or not meta.get("description"): raise ValueError("name e description são obrigatórios")
                    if kind == "skill" and meta.get("name") != pth.parent.name: warnings.append(f"Nome da skill difere da pasta: {pth.relative_to(ROOT)}")
                else:
                    if "name:" not in raw or "description:" not in raw: raise ValueError("name/description ausentes")
            except Exception as e:
                errors.append(f"Frontmatter inválido em {pth.relative_to(ROOT)}: {e}")
    catalog=ROOT/"modelos/catalogo.json"
    if catalog.exists():
        data=json.loads(catalog.read_text(encoding="utf-8"))
        for item in data.get("templates",[]):
            if not (ROOT/item.get("arquivo","")).is_file(): errors.append(f"Template catalogado não encontrado: {item.get('arquivo')}")
    policy=(ROOT/"configuracao/politica-de-modelos.yaml")
    if policy.exists():
        try:
            import yaml
            yaml.safe_load(policy.read_text(encoding="utf-8"))
        except ImportError:
            warnings.append("PyYAML não instalado; YAML não validado. Execute pip install -e '.[dev]'.")
        except Exception as e: errors.append(f"YAML inválido em politica-de-modelos.yaml: {e}")
    print("VERIFICAÇÃO DO FRAMEWORK SAMMY")
    for w in warnings: print(f"AVISO: {w}")
    for e in errors: print(f"ERRO: {e}")
    if not errors: print("OK: estrutura e configurações essenciais válidas.")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
