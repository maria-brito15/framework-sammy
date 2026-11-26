#!/usr/bin/env python3
"""Calcula faixa de risco a partir de uma avaliação contextual já fundamentada."""
from __future__ import annotations
import argparse, json
from pathlib import Path

DIMENSOES=["complexidade_dominio","dados_seguranca","integracoes","incerteza","complexidade_tecnica","escala_organizacional","impacto_falha"]
CRITICAS={"pagamentos","dados_sensiveis","autenticacao_critica","migracao_destrutiva","integridade_financeira","concorrencia_critica","regulacao","indisponibilidade_critica"}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("entrada", help="JSON contendo notas e evidências propostas pelo agente")
    p.add_argument("--saida", required=True)
    args=p.parse_args()
    source=Path(args.entrada); data=json.loads(source.read_text(encoding="utf-8"))
    dims=data.get("dimensoes",{})
    missing=[d for d in DIMENSOES if d not in dims]
    if missing: raise SystemExit("Dimensões ausentes: "+", ".join(missing))
    known=0; unknown=0
    for key in DIMENSOES:
        v=dims[key]
        if v == "DESCONHECIDO": unknown += 1
        elif isinstance(v,int) and not isinstance(v,bool) and 0 <= v <= 2: known += v
        else: raise SystemExit(f"Nota inválida em {key}: use 0, 1, 2 ou DESCONHECIDO")
    min_score=known
    max_score=known + unknown*2
    critical=set(data.get("condicoes_criticas",[])) & CRITICAS
    if critical or min_score >= 10:
        rigor="rigoroso"
    elif unknown == 0 and max_score <= 4:
        rigor="leve"
    elif unknown == 0 and min_score <= 9:
        rigor="padrao"
    elif max_score <= 4 and unknown == 0:
        rigor="leve"
    else:
        rigor="padrao"
    provisoria = unknown > 0 or not data.get("evidencias_suficientes",False)
    if rigor == "leve" and provisoria: rigor="padrao"
    result={
      "versao":1,
      "tipo_trabalho":data.get("tipo_trabalho","desconhecido"),
      "porte_projeto":data.get("porte_projeto","desconhecido"),
      "rigor_projeto":rigor,
      "autonomia":data.get("autonomia","controlada"),
      "granularidade":data.get("granularidade","funcionalidade"),
      "pontuacao_conhecida":known,
      "pontuacao_minima":min_score,
      "pontuacao_maxima":max_score,
      "dimensoes_desconhecidas":unknown,
      "condicoes_criticas_detectadas":sorted(critical),
      "classificacao_provisoria":provisoria,
      "observacoes":data.get("observacoes",[]),
      "evidencias":data.get("evidencias",[])
    }
    out=Path(args.saida); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Triagem calculada: rigor={rigor}, faixa={min_score}-{max_score}, desconhecidas={unknown}.")
    return 0
if __name__ == "__main__": raise SystemExit(main())
