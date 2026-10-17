"""Testes adversariais: maturidade não aprova normas ou DEC-016."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import validar_fila_deliberacao as gate

class GateFila(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=json.loads((ROOT/"governanca/19_FILA_QUESTOES_DELIBERAVEIS.json").read_text(encoding="utf-8"))
        cls.decisions=(ROOT/"governanca/04_REGISTRO_DE_DECISOES.md").read_text(encoding="utf-8")
    def bad(self,mutate,decisions=None):
        data=copy.deepcopy(self.source)
        mutate(data)
        with self.assertRaises(ValueError):
            gate.validate(data,self.decisions if decisions is None else decisions)
    def test_baseline(self):
        r=gate.validate(self.source,self.decisions)
        self.assertEqual(r,{"questoes":3,"submetidas":0,"confirmadas":0,"aptas":0,"fechadas":0})
    def test_dec016_nao_silenciosamente_decidida(self):
        self.bad(lambda d:d.update(dec016="APROVADA"))
    def test_registro_dec016_permanece_pendente(self):
        with self.assertRaisesRegex(ValueError,"DEC-016"):
            gate.validate(self.source,self.decisions.replace("| DEC-016 | PENDENTE |","| DEC-016 | CONFIRMADA_PELO_USUARIO |"))
    def test_dec018_nao_e_decorativa(self):
        with self.assertRaisesRegex(ValueError,"DEC-018"):
            gate.validate(self.source,self.decisions.replace("| DEC-018 | CONFIRMADA_PELO_USUARIO |","| DEC-018 | HIPOTESE_DE_TRABALHO |"))
    def test_proibir_fechamento_automatico(self):
        self.bad(lambda d:d["questoes"][0].update(fechamento="FC2_ESCOLHA_CONFIRMADA"))
    def test_apto_nao_se_declara_fc0(self):
        self.bad(lambda d:d["questoes"][1].update(maturidade="APTO_A_DELIBERAR"))
    def test_fechamento_fc1_sem_aptidao(self):
        self.bad(lambda d:d["questoes"][1].update(fechamento="FC1_APTO_A_ESCOLHA"))
    def test_escolha_nao_registrada(self):
        def change(d):
            q=d["questoes"][0]
            q["decisao"]["estado"]="CONFIRMADA"
            q["fechamento"]="FC2_ESCOLHA_CONFIRMADA"
            q["decisao"]["alternativa_escolhida"]=q["alternativas"][0]
        self.bad(change)
    def test_duplicar_id(self):
        self.bad(lambda d:d["questoes"][1].update(id=d["questoes"][0]["id"]))
    def test_apagar_melhor_objecao(self):
        self.bad(lambda d:d["questoes"][2].update(melhor_objecao=""))
    def test_reabrir_sem_motivo(self):
        self.bad(lambda d:d["questoes"][2]["decisao"].update(estado="REABERTA"))
    def test_promover_q_para_c0j(self):
        self.bad(lambda d:d["questoes"][0].update(classe_juridica="C0-J"))
    def test_sem_alternativas(self):
        self.bad(lambda d:d["questoes"][2].update(alternativas=["única decisão"]))
    def test_sem_redacao_confirmada_fc3(self):
        self.bad(lambda d:d["questoes"][1].update(fechamento="FC3_REDACAO_ESTABILIZADA"))
if __name__=="__main__":unittest.main()
