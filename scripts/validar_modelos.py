#!/usr/bin/env python3
"""Valida a política editável de roteamento de modelos e níveis de esforço."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
ALLOWED_MODELS={"haiku","sonnet","opus","fable"}
ALLOWED_EFFORT={"low","medium","high","xhigh","max"}
ALLOWED_MODES={"economico","equilibrado","qualidade-prioritaria"}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--arquivo",default="configuracao/politica-de-modelos.yaml"); args=p.parse_args()
    try:
        import yaml
    except ImportError:
        print("PyYAML ausente. Instale com: pip install -e '.[dev]'"); return 2
    path=Path(args.arquivo)
    try: cfg=yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e: print(f"YAML inválido: {e}"); return 1
    errors=[]
    if not isinstance(cfg,dict): errors.append("A raiz da política deve ser um objeto YAML.")
    else:
        if cfg.get("modo") not in ALLOWED_MODES: errors.append(f"Modo inválido: {cfg.get('modo')}")
        allowed=set(cfg.get("modelos_permitidos",[]))
        if not allowed: errors.append("modelos_permitidos não pode ser vazio.")
        unknown=allowed-ALLOWED_MODELS
        if unknown: errors.append("Aliases não reconhecidos: "+", ".join(sorted(unknown)))
        for papel, route in cfg.get("roteamento_por_papel",{}).items():
            model=route.get("modelo")
            if model and model not in allowed: errors.append(f"{papel}: modelo {model} não está em modelos_permitidos")
            effort=route.get("esforco")
            if effort and effort not in ALLOWED_EFFORT: errors.append(f"{papel}: esforço inválido {effort}")
        if cfg.get("modelo_sammy",{}).get("permitir-troca-automatica",False):
            print("AVISO: política não pode trocar silenciosamente o modelo da sessão principal; prefira roteamento por chamada de subagente.")
    for e in errors: print("ERRO:",e)
    if not errors: print(f"OK: política válida no modo {cfg['modo']}.")
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
