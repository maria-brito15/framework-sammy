#!/usr/bin/env python3
"""Gera manifesto SHA-256 das fontes sem alterar os arquivos de entrada."""
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""): h.update(chunk)
    return h.hexdigest()

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raiz", default=".")
    parser.add_argument("--entrada", default="documentos/entrada")
    parser.add_argument("--saida", default="planejamento/controle/manifesto-fontes.json")
    args=parser.parse_args()
    root=Path(args.raiz).resolve(); source=root/args.entrada; output=root/args.saida
    if not source.exists():
        print(f"Diretório de entrada não existe: {source}")
        return 2
    files=[]
    for p in sorted(source.rglob("*")):
        if p.is_file() and p.name.lower() not in {"leia-me.md"}:
            files.append({"caminho":p.relative_to(root).as_posix(),"tamanho_bytes":p.stat().st_size,"sha256":sha256(p)})
    payload={"versao":1,"gerado_em":datetime.now(timezone.utc).isoformat(),"raiz":root.name,"quantidade_fontes":len(files),"fontes":files}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    try:
        display_path = output.relative_to(root)
    except ValueError:
        display_path = output
    print(f"Manifesto gravado: {display_path} ({len(files)} fonte(s)).")
    return 0
if __name__ == "__main__": raise SystemExit(main())
