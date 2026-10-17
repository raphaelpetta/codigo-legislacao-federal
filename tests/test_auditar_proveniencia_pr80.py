"""Regressões para diferenciar origem existente hoje de origem no commit alegado."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE/"scripts"))
import auditar_proveniencia_pr80 as audit

def git(repo, *args):
    p=subprocess.run(["git","-C",str(repo),*args],capture_output=True,text=True,check=True)
    return p.stdout.strip()

class AuditFixture(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        git(self.root,"init","-q")
        git(self.root,"config","user.email","auditoria@example.invalid")
        git(self.root,"config","user.name","Auditoria Q")
        self.src=self.root/"modulos/T01/espelho.csv"
        self.src.parent.mkdir(parents=True)
        self.view=self.root/"produto/vistas/T01_Q.md"
        self.view.parent.mkdir(parents=True)
        self.view.write_text("**Art. 1.** Teste Q\n",encoding="utf-8")
        self.man=self.root/"produto/fontes/T01_Q.json"
        self.man.parent.mkdir(parents=True)
        self.index=self.root/"produto/fontes/indice_livros.json"
        self.src.write_text("id,texto\n1,Q\n",encoding="utf-8")
        self.meta={"source_path":"modulos/T01/espelho.csv",
                   "source_blob_sha":audit.blob(self.src),
                   "view_path":"produto/vistas/T01_Q.md",
                   "legal_status":"Q_SEM_C0_J","dec016":"PENDENTE",
                   "material_approved":False}
        self.book={"id":"T01-fixture","titulo":"T01","vista":"produto/vistas/T01_Q.md",
                   "manifesto":"produto/fontes/T01_Q.json","artigos":1,
                   "estado":"INTEGRADO_EXPERIMENTAL_PARCIAL_Q"}
        self.save()
        self.commit("original")
    def tearDown(self):
        self.tmp.cleanup()
    def save(self):
        self.man.write_text(json.dumps(self.meta),encoding="utf-8")
        self.index.write_text(json.dumps({"schema_version":1,"livros":[self.book]*60},
                                          ensure_ascii=False),encoding="utf-8")
    def commit(self,message):
        git(self.root,"add",".")
        git(self.root,"commit","-qm",message)
        return git(self.root,"rev-parse","HEAD")
    def historical(self,commit=None):
        return audit.historical_blob(self.root,commit or git(self.root,"rev-parse","HEAD"),
                                     "modulos/T01/espelho.csv")

    def test_comparacao_blob_identico(self):
        self.assertEqual(self.historical(),("PRESENTE_NO_COMMIT",audit.blob(self.src)))

    def test_commit_anterior_ao_nascimento_detectado(self):
        self.src.unlink()
        earlier=self.commit("sem arquivo")
        self.src.write_text("id,texto\n1,Q\n",encoding="utf-8")
        self.commit("novo arquivo")
        self.assertEqual(self.historical(earlier)[0],"CAMINHO_NAO_EXISTIA_NO_COMMIT")

    def test_blobs_do_mesmo_caminho_podem_divergir(self):
        before=git(self.root,"rev-parse","HEAD")
        self.src.write_text("id,texto\n1,mudou\n",encoding="utf-8")
        self.commit("nova versao")
        status,sha=audit.historical_blob(self.root,before,"modulos/T01/espelho.csv")
        self.assertEqual(status,"PRESENTE_NO_COMMIT")
        self.assertNotEqual(sha,audit.blob(self.src))

    def test_metadata_fonte_url_muda_sem_trocar_texto(self):
        self.src.write_text("id,texto,fonte_primaria\n1,Texto juridico,URL_errada\n", encoding="utf-8")
        original=self.commit("url fonte incorreta")
        before=git(self.root,"rev-parse",original+":modulos/T01/espelho.csv")
        self.src.write_text("id,texto,fonte_primaria\n1,Texto juridico,URL_corrigida\n", encoding="utf-8")
        self.commit("corrigir url sem texto")
        self.assertTrue(audit.metadata_only_drift(self.root,before,self.src))
        self.src.write_text("id,texto,fonte_primaria\n1,Outro texto,URL_corrigida\n",encoding="utf-8")
        self.assertFalse(audit.metadata_only_drift(self.root,before,self.src))

    def test_commit_malformado_falha(self):
        with self.assertRaisesRegex(ValueError,"Commit declarado inválido"):
            self.historical("HEAD; rm -rf /")

    def test_caminho_relativo_escape_falha(self):
        with self.assertRaisesRegex(ValueError,"inseguro"):
            audit.safe(self.root,"../fora.csv")

    def test_hash_manipulado_nao_equivale_prova(self):
        self.assertNotEqual("0"*40,audit.blob(self.src))

    def test_conteudo_da_fonte_preserva_q(self):
        self.assertEqual(self.meta["legal_status"],"Q_SEM_C0_J")

    def test_commit_nao_resolvido_classificado(self):
        self.assertEqual(self.historical("f"*40)[0],"COMMIT_NAO_RESOLVIDO")

if __name__=="__main__":
    unittest.main()
