"""Regressoes do gate indice/manifesto em checkout minimo sintetico.

Nao substituem a execucao no checkout integral nem a auditoria de DOU.
"""
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validar_corpus_ativo.py"


class GateIndiceManifesto(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "scripts").mkdir()
        shutil.copy2(SCRIPT, self.root / "scripts/validar_corpus_ativo.py")
        (self.root / "produto/fontes").mkdir(parents=True)
        (self.root / "produto/vistas").mkdir(parents=True)
        (self.root / "modulos/T01").mkdir(parents=True)
        source = self.root / "modulos/T01/espelho.csv"
        with source.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["origem", "texto"])
            w.writerow(["art1", "texto"])
        raw = source.read_bytes()
        digest = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        self.manifest = {
            "source_path": "modulos/T01/espelho.csv",
            "source_blob_sha": digest,
            "view_path": "produto/vistas/T01.md",
            "count_expected": 1,
            "articles_expected": 1,
            "status_juridico": "Q_SEM_C0_J",
            "dec016": "PENDENTE",
            "material_approved": False,
        }
        self.book = {
            "id": "CLF-TEST-T01", "titulo": "T01", "modulo": "T01.M01",
            "estado": "INTEGRADO_EXPERIMENTAL_PARCIAL_Q",
            "vista": "produto/vistas/T01.md",
            "manifesto": "produto/fontes/T01.json",
            "artigos": 1, "registros_documentais": 1,
        }
        view = "**Art. 1.** Texto de teste\n"
        (self.root / "produto/vistas/T01.md").write_text(view, encoding="utf-8")
        code = ("# Corpus sintetico\n\n"
                + f"## T01 — T01.M01 [{self.book['id']}; {self.book['estado']}]\n\n"
                + view.rstrip() + "\n")
        (self.root / "produto/CODIGO_DE_TRABALHO.md").write_text(code, encoding="utf-8")

    def run_gate(self):
        (self.root / "produto/fontes/T01.json").write_text(json.dumps(self.manifest), encoding="utf-8")
        (self.root / "produto/fontes/indice_livros.json").write_text(
            json.dumps({"livros": [self.book]}), encoding="utf-8")
        return subprocess.run([sys.executable, str(self.root / "scripts/validar_corpus_ativo.py")],
                              capture_output=True, text=True)

    def test_fixture_coerente(self):
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 manifestos", result.stdout)

    def test_indice_nao_pode_inflar_registros(self):
        self.book["registros_documentais"] = 99
        result = self.run_gate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("denominador indice/manifesto divergente", result.stderr)

    def test_manifesto_nao_pode_divergir_nos_artigos(self):
        self.manifest["articles_expected"] = 2
        result = self.run_gate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("artigos indice/manifesto divergentes", result.stderr)

    def test_vista_declarada_e_obrigatoria(self):
        self.manifest.pop("view_path")
        result = self.run_gate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("vista divergente", result.stderr)


if __name__ == "__main__":
    unittest.main()
