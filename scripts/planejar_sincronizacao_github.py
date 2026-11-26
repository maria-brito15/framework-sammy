#!/usr/bin/env python3
"""Gera um plano local de sincronização; não chama APIs nem altera o GitHub."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--config",default="configuracao/integracao-github.json"); p.add_argument("--saida",default="planejamento/controle/plano-github.json"); args=p.parse_args()
    cfg=json.loads(Path(args.config).read_text(encoding="utf-8"))
    if not cfg.get("habilitada",False):
        print("Integração GitHub desabilitada na configuração. Nenhuma operação foi preparada.")
        return 0
    payload={"modo":"dry-run","destino":{"repositorio":cfg.get("repositorio"),"projeto":cfg.get("projeto")},"operacoes":[],"observacao":"Planejador inicial: leia o backlog aprovado e complete a integração antes de executar operações remotas."}
    out=Path(args.saida); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Plano de simulação gravado em {out}. Nenhuma chamada remota foi feita.")
    return 0
if __name__ == "__main__": raise SystemExit(main())
