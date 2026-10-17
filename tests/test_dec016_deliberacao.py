"""Regressões da escolha preparatória A: DEC-019 confirmada, DEC-016 pendente."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import validar_fila_deliberacao as gate

class QD004(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/"governanca/19_FILA_QUESTOES_DELIBERAVEIS.json").read_text(encoding="utf-8"))
        cls.registro=(ROOT/"governanca/04_REGISTRO_DE_DECISOES.md").read_text(encoding="utf-8")
    def altered(self,fn):
        doc=copy.deepcopy(self.data)
        fn(doc["questoes"][3])
        with self.assertRaises(ValueError):
            gate.validate(doc,self.registro)
    def test_decisao_especifica_nao_fecha_dec016(self):
        r=gate.validate(self.data,self.registro)
        self.assertEqual((r["questoes"],r["aptas"],r["submetidas"],r["confirmadas"],r["fechadas"]),(4,1,0,1,1))
        self.assertEqual(self.data["questoes"][0]["maturidade"],"PESQUISA_FOCAL")
    def test_dossie_existe(self):
        self.assertTrue((ROOT/self.data["questoes"][3]["ref_dossie"]).is_file())
    def test_submissao_sem_maturidade_falha(self):
        self.altered(lambda q:q.update(maturidade="PESQUISA_FOCAL"))
    def test_submissao_sem_fc1_falha(self):
        self.altered(lambda q:q.update(fechamento="FC0_ABERTO"))
    def test_submissao_sem_fonte_falha(self):
        self.altered(lambda q:q.update(evidencias_maturidade=[]))
    def test_submissao_sem_pergunta_falha(self):
        self.altered(lambda q:q.update(pergunta_deliberacao=""))
    def test_subquestao_pai_falso_falha(self):
        self.altered(lambda q:q.update(subquestao_de="QD-2026-999"))
    def test_alternativa_trocada_sem_nova_decisao_falha(self):
        self.altered(lambda q:q["decisao"].update(alternativa_escolhida=q["alternativas"][1]))
    def test_reabrir_sem_motivo_falha(self):
        self.altered(lambda q:q["decisao"].update(estado="REABERTA"))
    def test_evidencia_da_aprovacao_ausente_falha(self):
        self.altered(lambda q:q["decisao"].update(evidencia_aprovacao=None))
    def test_aprovacao_nao_fecha_veiculo_definitivo(self):
        self.assertEqual(self.data["dec016"],"PENDENTE")
        self.assertEqual(self.data["questoes"][0]["decisao"]["estado"],"NAO_SUBMETIDA")
        self.assertEqual(self.data["questoes"][3]["decisao"]["registro_decisao"],"DEC-019")
    def test_nao_ha_fc3_automatico(self):
        self.altered(lambda q:q.update(fechamento="FC3_REDACAO_ESTABILIZADA"))
    def test_nao_ha_fingimento_de_fonte_primaria(self):
        self.altered(lambda q:q["decisao"].update(tipo_evidencia="PERMALINK_CHAT_AUTENTICADO"))

if __name__=="__main__": unittest.main()
