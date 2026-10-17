"""Regressões contra promoção implícita dos onze deltas do T07."""
import copy,csv,json,sys
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import validar_trilha_t07_dec019 as checker
class TestT07Trilha(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.route=json.loads((ROOT/"modulos/T07/M03_TRILHA_PREPARATORIA_DEC019_Q.json").read_text())
        cls.queue=json.loads((ROOT/"governanca/19_FILA_QUESTOES_DELIBERAVEIS.json").read_text())
        with (ROOT/"central/03_T07_GATE_C1_11_EFEITOS_20261015.csv").open(encoding="utf-8-sig",newline="") as f:
            cls.rows=list(csv.DictReader(f))
    def reject(self,update):
        a,b,c=copy.deepcopy(self.route),copy.deepcopy(self.rows),copy.deepcopy(self.queue)
        update(a,b,c)
        with self.assertRaises(ValueError):checker.check(a,b,c)
    def test_universo_original(self):
        self.assertEqual(checker.check(self.route,self.rows,self.queue)["c1_q"],11)
    def test_fonte_sha_alterado(self):
        self.reject(lambda a,b,c:a.update(fonte_commit="0"*40))
    def test_c1_faltante(self):
        self.reject(lambda a,b,c:a["unidades_c1"].pop())
    def test_c1_duplicado(self):
        self.reject(lambda a,b,c:a["unidades_c1"][0].update(id_origem=a["unidades_c1"][1]["id_origem"]))
    def test_c0j_ficticio(self):
        self.reject(lambda a,b,c:a["unidades_c1"][0].update(estado="C0-J"))
    def test_revo_externa(self):
        self.reject(lambda a,b,c:a.update(revogacoes="Lei 9.784 revogada"))
    def test_veiculo_prematuro(self):
        self.reject(lambda a,b,c:a.update(veiculo="LC_APROVADA"))
    def test_dec016_pendente(self):
        self.reject(lambda a,b,c:c.update(dec016="APROVADA"))
    def test_delta_art69_preservado(self):
        self.reject(lambda a,b,c:next(x for x in b if x["id_origem"]=="P19-69-C").update(texto_origem="A norma geral prevalece"))
    def test_riscos_iguais(self):
        self.reject(lambda a,b,c:b[0].update(classe_risco="BAIXO"))
    def test_questao_sem_aprovacao(self):
        self.reject(lambda a,b,c:c["questoes"][4]["decisao"].update(estado="CONFIRMADA"))
    def test_pai_sem_promocao(self):
        self.reject(lambda a,b,c:c["questoes"][2].update(maturidade="APTO_A_DELIBERAR"))
if __name__=="__main__":unittest.main()
