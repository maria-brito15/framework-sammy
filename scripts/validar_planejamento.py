#!/usr/bin/env python3
"""Valida integridade estrutural básica de documentos Markdown do planejamento."""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path
ID_RE=re.compile(r"\b(?:REQ|NFR|HIST|EP|FUNC|TAR|DEC|PESQ|BUG|APR|EXC)-\d{3,}\b")
HEADING_ID=re.compile(r"^#{1,6}\s+((?:REQ|NFR|HIST|EP|FUNC|TAR|DEC|PESQ|BUG|APR|EXC)-\d{3,})\b", re.M)

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--raiz",default="."); ap.add_argument("--diretorio",default="planejamento")
    args=ap.parse_args(); root=Path(args.raiz).resolve(); folder=root/args.diretorio
    if not folder.exists():
        print(f"Diretório não encontrado: {folder}"); return 2
    files=list(folder.rglob("*.md")); occurrences={}; headings={}; errors=[]; warnings=[]
    for f in files:
        if f.name.lower() in {"leia-me.md"}: continue
        text=f.read_text(encoding="utf-8")
        for ident in HEADING_ID.findall(text):
            headings.setdefault(ident,[]).append(f.relative_to(root).as_posix())
        for ident in ID_RE.findall(text):
            occurrences.setdefault(ident,[]).append(f.relative_to(root).as_posix())
    for ident, paths in headings.items():
        if len(paths)>1: errors.append(f"ID duplicado em títulos: {ident}: {paths}")
    defined=set(headings)
    for ident, paths in occurrences.items():
        if ident not in defined:
            warnings.append(f"Referência sem título correspondente: {ident} (em {', '.join(sorted(set(paths)))})")
    print(f"Arquivos Markdown examinados: {len(files)}")
    for e in errors: print("ERRO:",e)
    for w in warnings: print("AVISO:",w)
    if not errors and not warnings: print("OK: nenhuma duplicação ou referência sem definição foi encontrada.")
    return 1 if errors else 0
if __name__ == "__main__": raise SystemExit(main())
