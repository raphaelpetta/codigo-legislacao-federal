"""Regressões de proveniência dos Livros compostos Q (T24 e análogos).

Testes de integridade de artefatos, NÃO de vigência/DOU/C0-J.
"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/preflight_consolidacao.py"
spec = importlib.util.spec_from_file_location("preflight_consolidacao", SCRIPT)
assert spec and spec.loader
pre = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pre)


class ComponentesQTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.files = {
            "produto/vistas/T24_parte.md": "**Art. 1.** exemplo\n",
            "produto/concordancia/T24_parte.csv": "id,origem\n1,A\n",
            "produto/fontes/T24_segunda.csv": "id,origem\n2,B\n",
            "produto/vistas/T24_segunda.md": "**Art. 2.** exemplo\n",
            "produto/vistas/T24_composto.md": "**Art. 1.** exemplo\n**Art. 2.** exemplo\n",
            "produto/CODIGO_DE_TRABALHO.md": "**Art. 1.** exemplo\n**Art. 2.** exemplo\n",
        }
        for rel, content in self.files.items():
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        def sha(rel):
            return pre.git_blob(self.root / rel)
        self.parts = [
            {"name": "PARTE_A", "path": "produto/vistas/T24_parte.md",
             "git_blob": sha("produto/vistas/T24_parte.md"),
             "concordance_path": "produto/concordancia/T24_parte.csv",
             "concordance_git_blob": sha("produto/concordancia/T24_parte.csv"),
             "count": 1},
            {"name": "PARTE_B", "path": "produto/fontes/T24_segunda.csv",
             "git_blob": sha("produto/fontes/T24_segunda.csv"),
             "view_part_path": "produto/vistas/T24_segunda.md",
             "view_part_git_blob": sha("produto/vistas/T24_segunda.md"),
             "count": 1},
        ]
        self.manifest = {
            "source_path": "modulos/T24/origem_externa.csv",
            "view_path": "produto/vistas/T24_composto.md",
            "count_expected": 2,
            "status_juridico": "Q_SEM_C0_J",
            "material_approved": False,
            "dec016": "PENDENTE",
            "components": self.parts,
        }
        self.book = {
            "id": "T24-composite", "titulo": "T24",
            "vista": "produto/vistas/T24_composto.md",
            "manifesto": "produto/fontes/T24_manifesto.json",
            "artigos": 2, "registros_documentais": 2,
            "estado": "INTEGRADO_EXPERIMENTAL_CONTINUO_Q",
        }
        self.save()

    def tearDown(self):
        self.temp.cleanup()

    def save(self):
        (self.root / "produto/fontes/T24_manifesto.json").write_text(
            json.dumps(self.manifest), encoding="utf-8")
        (self.root / "produto/fontes/indice_livros.json").write_text(
            json.dumps({"schema_version": 1, "livros": [self.book]}), encoding="utf-8")

    def test_composto_valido_permanece_q(self):
        out = pre.inspect(self.root)
        self.assertEqual(out["compostos_pendentes"], 1)
        self.assertEqual(out["registros_documentais"], 2)

    def test_mutacao_de_conteudo_com_sha_antigo_bloqueada(self):
        (self.root / "produto/fontes/T24_segunda.csv").write_text(
            "id,origem\n2,CONTEUDO ALTERADO\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Blob de componente divergente"):
            pre.inspect(self.root)

    def test_mutacao_de_concordancia_bloqueada(self):
        (self.root / "produto/concordancia/T24_parte.csv").write_text(
            "id,origem\n1,OUTRO\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Blob de componente divergente"):
            pre.inspect(self.root)

    def test_mutacao_de_vista_parcial_bloqueada(self):
        (self.root / "produto/vistas/T24_segunda.md").write_text(
            "**Art. 2.** alterado\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Blob de componente divergente"):
            pre.inspect(self.root)

    def test_componente_sem_arquivo_bloqueado(self):
        (self.root / "produto/fontes/T24_segunda.csv").unlink()
        with self.assertRaisesRegex(ValueError, "Blob de componente divergente"):
            pre.inspect(self.root)

    def test_hash_declarado_ausente_bloqueado(self):
        self.parts[1].pop("git_blob")
        self.save()
        with self.assertRaisesRegex(ValueError, "par caminho/SHA"):
            pre.inspect(self.root)

    def test_cardinalidade_composta_divergente_bloqueada(self):
        self.parts[1]["count"] = 2
        self.save()
        with self.assertRaisesRegex(ValueError, "Cardinalidade composta"):
            pre.inspect(self.root)

    def test_contagem_invalida_bloqueada(self):
        self.parts[1]["count"] = "1"
        self.save()
        with self.assertRaisesRegex(ValueError, "contagem válida"):
            pre.inspect(self.root)

    def test_arquivo_repetido_bloqueado(self):
        self.parts[1]["path"] = self.parts[0]["path"]
        self.parts[1]["git_blob"] = self.parts[0]["git_blob"]
        self.save()
        with self.assertRaisesRegex(ValueError, "Arquivo composto duplicado"):
            pre.inspect(self.root)

    def test_travessia_de_diretorio_bloqueada(self):
        self.parts[1]["path"] = "../fora.csv"
        self.save()
        with self.assertRaisesRegex(ValueError, "Caminho inseguro"):
            pre.inspect(self.root)



    def test_fonte_local_nao_contorna_validacao_dos_componentes(self):
        source = self.root / self.manifest["source_path"]
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text("id,origem\\n1,A\\n2,B\\n", encoding="utf-8")
        self.manifest["source_blob_sha"] = pre.git_blob(source)
        self.save()
        (self.root / "produto/fontes/T24_segunda.csv").write_text(
            "id,origem\\n2,ALTERADO\\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Blob de componente divergente"):
            pre.inspect(self.root)

    def test_componente_vazio_nao_vira_origem_externa_pendente(self):
        self.manifest["components"] = []
        self.manifest["source_blob_sha"] = "a" * 40
        self.manifest["setorial_commit"] = "b" * 40
        self.save()
        with self.assertRaisesRegex(ValueError, "Composto vazio"):
            pre.inspect(self.root)

    def test_fonte_local_e_componentes_validos_sao_auditados_juntos(self):
        source = self.root / self.manifest["source_path"]
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text("id,origem\\n1,A\\n2,B\\n", encoding="utf-8")
        self.manifest["source_blob_sha"] = pre.git_blob(source)
        self.save()
        out = pre.inspect(self.root)
        self.assertEqual(out["compostos_pendentes"], 1)
        self.assertEqual(out["locais"], 0)

if __name__ == "__main__":
    unittest.main()
