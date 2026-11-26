import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class TestFrameworkScripts(unittest.TestCase):
    def run_script(self, script, *args):
        return subprocess.run([sys.executable,str(ROOT/script),*map(str,args)],cwd=ROOT,text=True,capture_output=True)

    def test_repo_valid(self):
        r=self.run_script(Path('scripts/verificar_repositorio.py'))
        self.assertEqual(r.returncode,0,msg=r.stdout+r.stderr)


    def test_model_policy_valid(self):
        r=self.run_script(Path('scripts/validar_modelos.py'))
        self.assertEqual(r.returncode,0,msg=r.stdout+r.stderr)

    def test_triage_critical_forces_rigorous(self):
        with tempfile.TemporaryDirectory() as td:
            src=Path(td)/'in.json'; dst=Path(td)/'out.json'
            data={"tipo_trabalho":"teste","porte_projeto":"pequeno","autonomia":"controlada","granularidade":"funcionalidade","dimensoes":{k:0 for k in ["complexidade_dominio","dados_seguranca","integracoes","incerteza","complexidade_tecnica","escala_organizacional","impacto_falha"]},"condicoes_criticas":["integridade_financeira"],"evidencias_suficientes":True}
            src.write_text(json.dumps(data),encoding='utf-8')
            r=self.run_script(Path('scripts/avaliar_triagem.py'),src,'--saida',dst)
            self.assertEqual(r.returncode,0,msg=r.stdout+r.stderr)
            self.assertEqual(json.loads(dst.read_text())['rigor_projeto'],'rigoroso')

    def test_unknown_not_zero_and_not_light(self):
        with tempfile.TemporaryDirectory() as td:
            src=Path(td)/'in.json'; dst=Path(td)/'out.json'
            keys=["complexidade_dominio","dados_seguranca","integracoes","incerteza","complexidade_tecnica","escala_organizacional","impacto_falha"]
            data={"tipo_trabalho":"teste","porte_projeto":"desconhecido","autonomia":"controlada","granularidade":"funcionalidade","dimensoes":{k:(0 if i==0 else "DESCONHECIDO") for i,k in enumerate(keys)},"condicoes_criticas":[],"evidencias_suficientes":False}
            src.write_text(json.dumps(data),encoding='utf-8')
            r=self.run_script(Path('scripts/avaliar_triagem.py'),src,'--saida',dst)
            self.assertEqual(r.returncode,0,msg=r.stdout+r.stderr)
            out=json.loads(dst.read_text())
            self.assertEqual(out['dimensoes_desconhecidas'],6)
            self.assertNotEqual(out['rigor_projeto'],'leve')

if __name__=='__main__': unittest.main()
