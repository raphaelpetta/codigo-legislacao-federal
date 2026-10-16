#!/usr/bin/env python3
"""Verificação adversarial do recorte CP 1–12 — documental Q, nunca C0-J."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = '3f0b56273caebfdbaba87ec4e87988da9f12c6c9'
CHECK_IDS = {f'T25-P{n:02}' for n in range(1, 11)}
TARGETS = {
    'CP-01-caput': 'Não há crime sem lei anterior',
    'CP-02-caput': 'Ninguém pode ser punido por fato',
    'CP-03-caput': 'A lei excepcional ou temporária',
    'CP-07-paragrafo_2': 'Nos casos do inciso II',
    'CP-07-paragrafo_3': 'A lei brasileira aplica-se também',
    'CP-09-caput': 'A sentença estrangeira',
    'CP-11-caput': 'Desprezam-se',
    'CP-12-caput': 'As regras gerais deste Código',
}

def fail(cond, why):
    if not cond:
        raise ValueError(why)

def blob(b):
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as h:
        return list(csv.DictReader(h, strict=True))

def run(setorial):
    meta=json.loads((ROOT/'produto/fontes/T25_CP1_12_v1.json').read_text(encoding='utf-8'))
    fail(meta['setorial_commit']==SOURCE_COMMIT, 'SHA commit setorial inesperado')
    fail(meta['status_juridico']=='Q_SEM_C0_J' and meta['material_approved'] is False and meta['dec016']=='PENDENTE',
         'Estado penal promovido')
    relative=Path(meta['source_path'])
    fail(not relative.is_absolute() and '..' not in relative.parts, 'Path externo inseguro')
    source=(setorial/relative).resolve()
    fail(source.is_relative_to(setorial.resolve()), 'Fonte fora de checkout')
    raw=source.read_bytes()
    fail(blob(raw)==meta['source_blob_sha'], 'SHA da fonte penal divergente')
    source_rows=rows(source)
    fail(len(source_rows)==39 and len({z['id_fonte'] for z in source_rows})==39, '39 origens não comprovadas')
    by_id={z['id_fonte']:z for z in source_rows}
    fail(all(z['categoria_espelho']=='C0-T' and z['equivalencia_juridica']=='Q' and
             z['tipo_ato']=='DECRETO-LEI' and z['numero_ato']=='2848' for z in source_rows),
         'Origem penal, classe ou Q alterada')
    for ident,phrase in TARGETS.items():
        fail(ident in by_id and by_id[ident]['texto_literal_sem_rotulo'].startswith(phrase),
             f'Garantia penal/remissão não preservada: {ident}')
    art12=by_id['CP-12-caput']['texto_literal_sem_rotulo']
    fail(art12=='As regras gerais deste Código aplicam-se aos fatos incriminados por lei especial, se esta não dispuser de modo diverso.',
         'Referente CP12 ou especialidade jurídica alterados')
    fail('Código da Legislação Federal' not in art12, 'CP12 ampliado ao CLF')
    cases=rows(ROOT/'central/08_T25_DEZ_GATES_ESPECIALIDADE_PENAL_20261015.csv')
    fail(len(cases)==10 and {z['id_gate'] for z in cases}==CHECK_IDS,
         '10 gates de Direito Penal incompletos')
    fail(all(z['estado'] in {'Q','Q_ESPECIALIDADE','Q_JURISPRUDENCIA','Q_INTERTEMPORAL',
                             'C1_POTENCIAL_Q','SEM_REFORMA_MATERIAL_APROVADA'}
             and z['risco_de_transposicao'] and z['invariante'] and z['prova_pendente'] for z in cases),
         'Estado indevidamente homologado ou risco sem contraprova')
    fail(next(z for z in cases if z['id_gate']=='T25-P09')['estado']=='C1_POTENCIAL_Q',
         'Art. 12 perdeu ressalva C1')
    index=json.loads((ROOT/'produto/fontes/indice_livros.json').read_text(encoding='utf-8'))
    rec=[b for b in index['livros'] if b['id']=='CLF-LIV-T25-M01-CP1-12-v1']
    fail(len(rec)==1 and rec[0]['artigos']==12 and rec[0]['registros_documentais']==39
         and rec[0]['estado'].startswith('INTEGRADO_EXPERIMENTAL'),
         'Livro T25 sem delimitação documental')
    return {'origens':39,'artigos':12,'gates':10,'remissao_art12':'CODIGO_PENAL',
            'c0_j_aprovados':0,'m_aprovadas':0}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--setorial-root',type=Path,required=True)
    a=p.parse_args()
    try:
        print('PASSOU T25 R3, NÃO C0-J: '+json.dumps(run(a.setorial_root),ensure_ascii=False,sort_keys=True))
    except (ValueError,OSError,KeyError,csv.Error) as e:
        p.exit(1,f'FALHA T25 R3: {e}\n')

if __name__=='__main__':
    main()
