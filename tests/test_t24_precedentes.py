"""Regressões adversariais: não substituir interpretação judicial por lei vigente."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import sys
import unittest

BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/"scripts"))
import validar_t24_precedentes as gate


class T24PrecedentesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs=gate.documents()
        cls.original=json.loads(gate.MATRIX.read_text(encoding="utf-8"))

    def check_mutation(self,modify):
        obj=copy.deepcopy(self.original)
        modify(obj)
        with self.assertRaises(ValueError):
            gate.validate(obj,self.docs)

    def test_documentacao_fixa_passa(self):
        self.assertEqual(gate.validate(self.original,self.docs)["efeitos"],9)

    def test_sem_tema1178_proibicao_indeferimento_imediato_nao_passa(self):
        self.check_mutation(lambda d:d["cenarios"].pop(0))

    def test_tema1178_nao_pode_vincular_pessoa_juridica_automaticamente(self):
        self.check_mutation(lambda d:d["cenarios"][0].update(escopo="PESSOA_JURIDICA"))

    def test_tema1178_nao_pode_ser_convertido_em_norma_nova(self):
        self.check_mutation(lambda d:d["cenarios"][1].update(tipo="NORMA_LEGAL_PROMULGADA"))

    def test_stf1255_nao_pode_ser_declarado_julgado_no_merito(self):
        self.check_mutation(lambda d:d["cenarios"][6].update(tipo="TESE_MERITO_TRANSITADA"))

    def test_stf1255_nao_pode_abranger_todas_as_causas_automaticamente(self):
        self.check_mutation(lambda d:d["cenarios"][6].update(escopo="TODAS_AS_CAUSAS"))

    def test_sem_personalidade_gratuidade_nao_passa(self):
        self.check_mutation(lambda d:d["cenarios"].pop(3))

    def test_art82_nao_e_isencao_geral_de_custas(self):
        self.check_mutation(lambda d:d["cenarios"][7].update(efeito="ISENCAO_GERAL"))

    def test_dec016_nao_pode_ser_promovida(self):
        self.check_mutation(lambda d:d.update(dec016="APROVADA"))

    def test_sha_fonte_75_nao_pode_ser_trocado(self):
        self.check_mutation(lambda d:d.update(fonte_editorial_75_sha="0"*40))


if __name__=="__main__":
    unittest.main()
