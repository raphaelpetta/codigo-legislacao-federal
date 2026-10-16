"""Regressões isoladas: integridade Q não equivale a certificação jurídica."""
from __future__ import annotations

import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / 'scripts/preflight_consolidacao.py'
spec = importlib.util.spec_from_file_location('preflight_consolidacao', MODULE)
assert spec and spec.loader
pre = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pre)


class PreflightTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        source = self.root / 'modulos/T18/espelho.csv'
        source.parent.mkdir(parents=True)
        with source.open('w', encoding='utf-8', newline='') as h:
            w = csv.DictWriter(h, fieldnames=['id_origem', 'texto'])
            w.writeheader()
            w.writerow({'id_origem': 'L6404-A1', 'texto': 'texto'})
        self.view = self.root / 'produto/vistas/T18_Q.md'
        self.view.parent.mkdir(parents=True)
        self.view.write_text('**Art. 1.** texto\n', encoding='utf-8')
        (self.root / 'produto/CODIGO_DE_TRABALHO.md').write_text('**Art. 1.** texto\n', encoding='utf-8')
        self.manifest = self.root / 'produto/fontes/T18_Q.json'
        self.manifest.parent.mkdir(parents=True)
        self.meta = {
            'source_path': 'modulos/T18/espelho.csv',
            'source_blob_sha': pre.git_blob(source),
            'view_path': 'produto/vistas/T18_Q.md',
            'count_expected': 1,
            'legal_status': 'Q_SEM_C0_J',
            'material_approved': False,
            'dec016': 'PENDENTE',
        }
        self.book = {'id': 'T18-demo', 'titulo': 'T18',
                     'vista': 'produto/vistas/T18_Q.md',
                     'manifesto': 'produto/fontes/T18_Q.json',
                     'artigos': 1, 'registros_documentais': 1,
                     'estado': 'INTEGRADO_EXPERIMENTAL_PARCIAL_Q'}
        self.save()

    def tearDown(self):
        self.tmp.cleanup()

    def save(self):
        self.manifest.write_text(json.dumps(self.meta), encoding='utf-8')
        (self.root / 'produto/fontes/indice_livros.json').write_text(
            json.dumps({'schema_version': 1, 'livros': [self.book]}), encoding='utf-8')

    def test_snapshot_documental_conferido(self):
        self.assertEqual(pre.inspect(self.root)['registros_documentais'], 1)

    def test_drift_blob_interrompe(self):
        (self.root / 'modulos/T18/espelho.csv').write_text('alterado', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Blob de origem divergente'):
            pre.inspect(self.root)

    def test_promocao_c0j_interrompe(self):
        self.meta['legal_status'] = 'C0-J'
        self.save()
        with self.assertRaisesRegex(ValueError, 'Estado jurídico incompatível'):
            pre.inspect(self.root)

    def test_aprovacao_material_interrompe(self):
        self.meta['material_approved'] = True
        self.save()
        with self.assertRaisesRegex(ValueError, 'Aprovação material'):
            pre.inspect(self.root)

    def test_caminho_externo_interrompe(self):
        self.meta['source_path'] = '../fora.csv'
        self.save()
        with self.assertRaisesRegex(ValueError, 'Caminho inseguro'):
            pre.inspect(self.root)

    def test_contagem_divergente_interrompe(self):
        self.book['registros_documentais'] = 2
        self.save()
        with self.assertRaisesRegex(ValueError, 'Contagem documental divergente'):
            pre.inspect(self.root)

    def test_livro_antigo_mutado_interrompe(self):
        with tempfile.TemporaryDirectory() as another:
            base = Path(another)
            (base / 'produto/vistas').mkdir(parents=True)
            (base / 'produto/fontes').mkdir(parents=True)
            for path in (self.view, self.manifest, self.root / 'produto/fontes/indice_livros.json'):
                (base / path.relative_to(self.root)).write_bytes(path.read_bytes())
            self.view.write_text('**Art. 1.** novo\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Livro antigo alterado'):
                pre.inspect(self.root, base)

    def test_commit_pinado_sem_documentos_externos_rejeitado(self):
        self.meta.pop('source_path')
        self.meta.pop('source_blob_sha')
        self.meta['setorial_commit'] = 'a' * 40
        self.save()
        with self.assertRaisesRegex(ValueError, 'Origem ausente'):
            pre.inspect(self.root)

    def test_texto_e_concordancia_externos_com_hashs_ficam_pendentes(self):
        self.meta.pop('source_path')
        self.meta.pop('source_blob_sha')
        self.meta.update({
            'setorial_commit': 'a' * 40,
            'texto_relativo': 'integracao/texto.md',
            'texto_blob_sha': 'b' * 40,
            'concordancia_relativa': 'integracao/concordancia.csv',
            'concordancia_blob_sha': 'c' * 40,
        })
        self.save()
        outcome = pre.inspect(self.root)
        self.assertEqual(outcome['externos_pendentes'], 1)
        self.assertEqual(outcome['locais'], 0)

    def test_fonte_setorial_externa_com_sha_fica_pendente(self):
        self.meta['setorial_commit'] = 'a' * 40
        (self.root / self.meta['source_path']).unlink()
        self.save()
        outcome = pre.inspect(self.root)
        self.assertEqual(outcome['externos_pendentes'], 1)

    def test_texto_externo_sem_sha_rejeitado(self):
        self.meta.pop('source_path')
        self.meta.pop('source_blob_sha')
        self.meta.update({
            'setorial_commit': 'a' * 40,
            'texto_relativo': 'integracao/texto.md',
            'concordancia_relativa': 'integracao/concordancia.csv',
            'concordancia_blob_sha': 'c' * 40,
        })
        self.save()
        with self.assertRaisesRegex(ValueError, 'Origem ausente'):
            pre.inspect(self.root)


if __name__ == '__main__':
    unittest.main()
