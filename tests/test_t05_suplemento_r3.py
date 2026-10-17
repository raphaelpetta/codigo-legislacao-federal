"""Mutação adversarial do suplemento T05.M06. Não avalia legalidade DOU."""
from __future__ import annotations
import copy
import csv
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import validar_t05_suplemento_r3 as audit

class RegressoT05(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.meta=json.loads((ROOT/"produto/fontes/T05_M06_9709_23_v1.json").read_text(encoding="utf-8"))
        cls.rows=audit.csvrows(ROOT/cls.meta["source_path"])

    def mutate(self,func):
        rows=copy.deepcopy(self.rows);meta=copy.deepcopy(self.meta)
        func(rows,meta)
        with self.assertRaises(ValueError):
            audit.verify(rows,meta)

    def test_material_original(self):
        self.assertEqual(audit.verify(self.rows,self.meta)["unidades_q"],23)

    def test_sem_uma_origem(self):
        self.mutate(lambda rows,meta: rows.pop())

    def test_troca_compõem_para_compõe(self):
        self.mutate(lambda rows,meta: next(r for r in rows if r["artigo"]=="3").update(
            texto_destino_documental=next(r for r in rows if r["artigo"]=="3")["texto_destino_documental"].replace("compõem","compõe")))

    def test_correcao_silenciosa_art8(self):
        self.mutate(lambda rows,meta: next(r for r in rows if r["artigo"]=="8" and r["unidade"]=="IV").update(
            texto_destino_documental=next(r for r in rows if r["artigo"]=="8" and r["unidade"]=="IV")["texto_destino_documental"].replace("a às frentes","e às frentes")))

    def test_15_nao_e_vigencia_futura(self):
        self.mutate(lambda rows,meta: next(r for r in rows if r["artigo"]=="15").update(texto_fonte_camara_html="O CLF entra em vigor hoje."))

    def test_origem_em_commit_que_nao_tem_blob(self):
        self.mutate(lambda rows,meta: meta.update(source_commit="13027681729f3cbe7f77fe5e08be521fa27bd4b2"))

    def test_sem_dou_autenticado_nao_promover(self):
        self.mutate(lambda rows,meta: meta.update(evidencia_independente="DOU_AUTENTICADO"))

    def test_nao_homologar_c0_j(self):
        self.mutate(lambda rows,meta: meta.update(status_juridico="C0_J_HOMOLOGADO"))

    def test_nao_excluir_requisito_iniciativa(self):
        self.mutate(lambda rows,meta: next(r for r in rows if r["artigo"]=="13" and r["unidade"]=="C").update(
           texto_fonte_camara_html="Assinatura livre em apenas um Estado."))

if __name__=="__main__":
    unittest.main()
