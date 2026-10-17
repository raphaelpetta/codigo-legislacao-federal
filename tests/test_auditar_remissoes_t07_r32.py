"""Contraprovas R32: ligação entre artigos não equivale a homologação jurídica."""
import copy
import csv
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import auditar_remissoes_t07_r32 as audit

class R32RemissoesT07(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.map=json.loads(audit.MAPA.read_text(encoding="utf-8"))
        cls.source=audit.readcsv(audit.MATRIX)
        cls.triage=audit.readcsv(audit.TRIAGE)
        cls.cases=audit.readcsv(audit.CASES)
        cls.view=audit.VIEW.read_text(encoding="utf-8")
        cls.queue=json.loads(audit.QUEUE.read_text(encoding="utf-8"))
        cls.route=json.loads(audit.TRILHA.read_text(encoding="utf-8"))
    def no(self,mutate):
        a,b,c,d=copy.deepcopy(self.map),copy.deepcopy(self.source),copy.deepcopy(self.triage),copy.deepcopy(self.queue)
        e,f=copy.deepcopy(self.route),self.view
        inputs=[a,b,c,d,e,f]
        mutate(inputs)
        with self.assertRaises(ValueError):
            audit.check(inputs[0],inputs[1],inputs[2],self.cases,inputs[5],inputs[3],inputs[4])
    def test_baseline(self):
        r=audit.check(self.map,self.source,self.triage,self.cases,self.view,self.queue,self.route)
        self.assertEqual(r,{"vinculos_documentais":3,"c1_preservados_q":11,
                            "outras_c1_em_pesquisa":7,"aprovacoes_normativas":0,
                            "dec016":"PENDENTE"})
    def test_trinca_incompleta(self):
        self.no(lambda v:v[0]["remissoes"].pop())
    def test_remissao_troca_alvo_36(self):
        self.no(lambda v:v[0]["remissoes"][0].update(alvo_lei="26"))
    def test_remissao_troca_id_destino_49b(self):
        self.no(lambda v:v[0]["remissoes"][1].update(id_artigo_experimental_alvo="LPA-SEQ4-026"))
    def test_remissao_troca_id_destino_fonte_49d(self):
        self.no(lambda v:v[0]["remissoes"][2].update(destino_unidade_fonte="EXP15-9-C"))
    def test_escopo_nao_prova_c0j(self):
        self.no(lambda v:v[0]["remissoes"][0].update(classe_juridica="C0-J"))
    def test_falsa_auditoria_independente(self):
        self.no(lambda v:v[2][0].update(estado_auditoria_juridica="HOMOLOGADA"))
    def test_remissao_sem_protecao_de_direitos(self):
        self.no(lambda v:v[0]["remissoes"][2].update(protecao=""))
    def test_terceiro_cenario_removido(self):
        self.no(lambda v:v[0]["remissoes"][0].update(cenario_ids=[]))
    def test_apagar_alvo_da_previa(self):
        self.no(lambda v:v.__setitem__(5,v[5].replace("**Art. LPA-SEQ4-037.**","**Art. LPA-SEQ4-999.**")))
    def test_origem_t07_nao_homologada(self):
        self.no(lambda v:v[4].update(estado_juridico="C0-J"))
    def test_nenhuma_das_sete_pode_sumir(self):
        self.no(lambda v:v[0]["outros_c1_ainda_sem_fecho"].pop())
    def test_dec020_nao_dec016(self):
        self.no(lambda v:v[0].update(dec016="APROVADA"))
    def test_dec020_nao_homologa_art69(self):
        self.no(lambda v:v[0]["art69_ja_deliberado"].update(classe_juridica="C0-J"))
    def test_questao_mae_ainda_pesquisa(self):
        self.no(lambda v:v[3]["questoes"][2].update(maturidade="APTO_A_DELIBERAR"))
    def test_futura_numeracao_nao_pode_ser_inferida(self):
        self.no(lambda v:v[0].update(condicao="EQUIVALENCIA_JURIDICA_COMPROVADA"))
if __name__=="__main__": unittest.main()
