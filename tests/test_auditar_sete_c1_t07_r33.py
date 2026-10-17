"""Regressões R33 contra alargamento tácito do âmbito do T07."""
import copy
import json
import sys
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import auditar_sete_c1_t07_r33 as gate

class R33T07(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=json.loads(gate.PATHS["map"].read_text())
        cls.s=gate.rows(gate.PATHS["source"])
        cls.t=gate.rows(gate.PATHS["triage"])
        cls.c=gate.rows(gate.PATHS["cases"])
        cls.view=gate.PATHS["view"].read_text()
        cls.q=json.loads(gate.PATHS["queue"].read_text())
        cls.route=json.loads(gate.PATHS["route"].read_text())
    def check(self,parts):
        return gate.check(*parts)
    def reject(self,mutate):
        parts=copy.deepcopy([self.m,self.s,self.t,self.c,self.view,self.q,self.route])
        mutate(parts)
        with self.assertRaises(ValueError):
            self.check(parts)
    def test_baseline(self):
        self.assertEqual(self.check([self.m,self.s,self.t,self.c,self.view,self.q,self.route]),
            {"c1_em_analise":7,"escopo_aptas":3,"pontuacao_aguarda":3,
             "coordenada_aguarda":1,"c1_q_total":11,"homologacoes_novas":0})
    def test_sete_sem_uma_unidade(self):
        self.reject(lambda a:a[0]["sete"].pop())
    def test_competencia_estadual_nao_pode_ser_inferida(self):
        self.reject(lambda a:a[1][0].update(texto_previa="Inclui estados e municípios"))
    def test_poderes_outros_escopo_nao_expandido(self):
        self.reject(lambda a:next(x for x in a[1] if x["id_origem"]=="P13-01-P1").update(texto_previa="Aplica-se aos juízes em função jurisdicional"))
    def test_definicoes_nao_podem_ser_universais(self):
        self.reject(lambda a:next(x for x in a[0]["sete"] if x["id_origem"]=="P13-01-P2").update(classe_juridica="C0-J"))
    def test_mudar_conceito_nao_e_tipografia(self):
        self.reject(lambda a:next(x for x in a[1] if x["id_origem"]=="P13-01-P2-I").update(texto_previa="órgão: unidade autônoma"))
    def test_tipografia_nao_e_c0j(self):
        self.reject(lambda a:next(x for x in a[0]["sete"] if x["id_origem"]=="P13-01-P2-II").update(classe_juridica="C0-J"))
    def test_autoridade_nao_perde_poder_de_decisao(self):
        self.reject(lambda a:next(x for x in a[1] if x["id_origem"]=="P13-01-P2-III").update(texto_previa="autoridade: qualquer pessoa"))
    def test_sem_revisao_independente(self):
        self.reject(lambda a:next(x for x in a[0]["sete"] if x["id_origem"]=="C18-49-A-P1").update(necessita_revisao_independente=False))
    def test_decisao_coordenada_nao_apaga_responsabilidade(self):
        self.reject(lambda a:a.__setitem__(4,a[4].replace("não exclui a responsabilidade originária","afasta a responsabilidade originária")))
    def test_coordenada_nao_admite_sancao_por_atalho(self):
        self.reject(lambda a:a.__setitem__(4,a[4].replace("**II –** relacionados ao poder sancionador; ou","**II –** inclusive sanções; ou")))
    def test_coordenada_nao_admite_autoridades_poderes_distintos(self):
        self.reject(lambda a:a.__setitem__(4,a[4].replace("**III –** em que estejam envolvidas autoridades de Poderes distintos.","**III –** em todos os Poderes.")))
    def test_questao_submetida_nao_e_aprovada(self):
        self.reject(lambda a:next(x for x in a[5]["questoes"] if x["id"]=="QD-2026-006")["decisao"].update(estado="CONFIRMADA"))
    def test_questao_mae_continua_em_estudo(self):
        self.reject(lambda a:next(x for x in a[5]["questoes"] if x["id"]=="QD-2026-003").update(maturidade="APTO_A_DELIBERAR"))
    def test_nao_pode_decidir_dec016(self):
        self.reject(lambda a:a[0].update(dec016="APROVADA"))
    def test_corpus_nao_pode_esconder_dec020(self):
        self.reject(lambda a:a[6]["decisao_preparatoria"].update(id="DEC-016"))
if __name__=="__main__":unittest.main()
