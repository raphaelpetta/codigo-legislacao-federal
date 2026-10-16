#!/usr/bin/env python3
"""Gate adversarial de 11 C1 potenciais do T07. Nunca certifica C0-J.

Fonte obrigatória: checkout separado do PR #45 no commit fixado pelo manifesto.
A matriz e os casos controlam mudança de referente, especialidade e remissões.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ID_C1 = {
    'P13-01-C': 'LPA-SEQ4-001-C',
    'P13-01-P1': 'LPA-SEQ4-001-P1',
    'P13-01-P2': 'LPA-SEQ4-001-P2',
    'P13-01-P2-I': 'LPA-SEQ4-001-P2-I',
    'P13-01-P2-II': 'LPA-SEQ4-001-P2-II',
    'P13-01-P2-III': 'LPA-SEQ4-001-P2-III',
    'P19-69-C': 'LPA-SEQ4-077-C',
    'EXP17-36-C': 'LPA-SEQ4-036-C',
    'C18-49-A-P1': 'LPA-SEQ4-050-P1',
    'C18-49-B-C': 'LPA-SEQ4-051-C',
    'C18-49-D-C': 'LPA-SEQ4-052-C',
}
RISCOS = {'CRITICO': 5, 'ALTO': 3, 'BAIXO': 3}
PONTUACAO = {'P13-01-P2-I', 'P13-01-P2-II', 'P13-01-P2-III'}
REMISSOES = {
    'EXP17-36-C': ('37', 'LPA-SEQ4-037-C'),
    'C18-49-B-C': ('9', 'LPA-SEQ4-009-C'),
    'C18-49-D-C': ('26', 'LPA-SEQ4-026-C'),
}


def demand(test: bool, why: str) -> None:
    if not test:
        raise ValueError(why)


def git_blob(path: Path) -> str:
    body = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()


def records(path: Path) -> list[dict[str, str]]:
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, strict=True))


def safe(root: Path, rel: str) -> Path:
    p = Path(rel)
    demand(not p.is_absolute() and '..' not in p.parts, f'Caminho inseguro: {rel}')
    result = (root / p).resolve()
    demand(result.is_relative_to(root.resolve()), f'Fora do checkout: {rel}')
    return result


def audit(setorial: Path) -> dict[str, int]:
    m = json.loads((ROOT / 'produto/fontes/T07_M03_v4.json').read_text(encoding='utf-8'))
    demand(m['setorial_commit'] == '2a4d1eefa864f44435aec70ed0cc55a96b718b64',
           'Commit da fonte do T07 alterado sem reauditoria')
    demand(m['dec016'] == 'PENDENTE' and m['estado_juridico'] == 'Q_SEM_C0_J'
           and m['aprovacao_material'] == 'NAO', 'Classificação jurídica promovida')
    src = safe(setorial, m['concordancia_relativa'])
    texto = safe(setorial, m['texto_relativo'])
    demand(git_blob(src) == m['concordancia_blob_sha'], 'SHA da matriz setorial mudou')
    demand(git_blob(texto) == m['texto_blob_sha'], 'SHA do texto setorial mudou')
    origin = records(src)
    demand(len(origin) == m['contagens_esperadas']['fontes'] == 215, 'Total de fontes diferente')
    demand(len({x['id_fonte'] for x in origin}) == 215, 'Origem repetida')
    demand(all(x['status_juridico'] == 'Q_SEM_C0_J'
               and x['situacao'] == 'NAO_APROVADO_NAO_PROMULGADO' for x in origin),
           'Fonte alterou estado jurídico ou aprovação')
    by_id = {r['id_fonte']: r for r in origin}
    classes = Counter(r['categoria_preliminar'] for r in origin)
    demand(classes == {'C0_T_APENAS': 203, 'C1_POTENCIAL_Q': 11, 'HISTORICO': 1},
           f'Classificações de origem alteradas: {dict(classes)}')
    c1 = {r['id_fonte'] for r in origin if r['categoria_preliminar'] == 'C1_POTENCIAL_Q'}
    demand(c1 == set(ID_C1), f'C1 não permitidos/faltantes: {c1 ^ set(ID_C1)}')
    for r in origin:
        if r['categoria_preliminar'] == 'C0_T_APENAS':
            demand(r['texto_fonte_arquivado'] == r['texto_destino_experimental'],
                   f'Delta não declarado em C0-T: {r["id_fonte"]}')
    historical = by_id['C19-70-C']
    demand(historical['destino_experimental'] == 'HIST-LEI9784-ART70'
           and historical['categoria_preliminar'] == 'HISTORICO',
           'Vigência original do art70 erroneamente reeditada')
    table = records(ROOT / 'central/03_T07_GATE_C1_11_EFEITOS_20261015.csv')
    demand(len(table) == 11 and {r['id_origem'] for r in table} == set(ID_C1),
           'Matriz auditável das 11 C1 incompleta')
    demand(Counter(r['classe_risco'] for r in table) == RISCOS, 'Risco R3 reclassificado')
    for c in table:
        ident = c['id_origem']
        r = by_id[ident]
        demand(c['sha_setorial'] == m['setorial_commit'] and c['estado_juridico'] == 'Q_SEM_C0_J'
               and c['classe_local'] == 'C1_POTENCIAL_Q'
               and c['status'] == 'GATE_ABERTO', f'Gate C1 fechado sem prova: {ident}')
        demand(c['texto_origem'] == r['texto_fonte_arquivado'] and
               c['texto_previa'] == r['texto_destino_experimental'] and
               r['destino_experimental'] == ID_C1[ident],
               f'Concordância C1 divergente: {ident}')
        a, b = c['texto_origem'], c['texto_previa']
        if ident in PONTUACAO:
            demand(a.replace(' - ', ': ', 1) == b, f'Delta de pontuação não isolado: {ident}')
        elif ident == 'P13-01-C':
            demand(a.replace('Esta Lei', 'Este Livro', 1) == b, 'Ampliação do âmbito além de referente')
        else:
            demand(a.replace('desta Lei', 'deste Livro', 1) == b and 'desta Lei' in a,
                   f'Delta de referente inesperado: {ident}')
    for ident, (num, target) in REMISSOES.items():
        original_ref = num + ('º' if num == '9' else '')
        demand(f'art. {original_ref} desta Lei' in by_id[ident]['texto_fonte_arquivado']
               and f'art. {original_ref} deste Livro' in by_id[ident]['texto_destino_experimental'],
               f'Remissão source->Livro quebrada: {ident}')
        demand(any(x['destino_experimental'] == target and
                   x['categoria_preliminar'] == 'C0_T_APENAS' for x in origin),
               f'Remissão perdeu destino ancorado {target}')
    for suffix in ('I', 'II', 'III'):
        ident = 'C18-49-A-P6-' + suffix
        demand(ident in by_id and by_id[ident]['categoria_preliminar'] == 'C0_T_APENAS',
               f'Exclusão da decisão coordenada ausente: {ident}')
    demand(all(x['destino_experimental'].startswith('HIST-')
               for x in origin if x['categoria_preliminar'] == 'HISTORICO'),
           'Dispositivo histórico restaurado')
    cases = records(ROOT / 'central/06_T07_DOZE_CASOS_ADVERSARIAIS_REMISSOES_E_ESPECIALIDADE.csv')
    demand(len(cases) == 12 and {r['id_teste'] for r in cases}
           == {f'T07-E{x:02d}' for x in range(1, 13)}, '12 contraprovas incompletas')
    demand(all(c['id_c1_fonte'] in ID_C1 and c['resultado'] == 'Q' and
               c['id_destino_c1'] == ID_C1[c['id_c1_fonte']] for c in cases),
           'Contraprova promoveu decisão, perdeu origem ou destino')
    for critical in ('P13-01-C', 'P13-01-P1', 'P19-69-C', 'EXP17-36-C', 'C18-49-D-C'):
        demand(any(c['id_c1_fonte'] == critical for c in cases),
               f'Risco crítico sem caso adversarial: {critical}')
    # Check da vista gerada é separado: gerar_produto_experimental.py --check.
    return {'fontes': 215, 'positivas': 214, 'historicas': 1,
            'c0_t_locais': 203, 'c1_potenciais_q': 11, 'casos': 12,
            'remissoes_ancoradas': len(REMISSOES), 'exclusoes_decisao_coordenada': 3}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--setorial-root', required=True, type=Path)
    a = parser.parse_args()
    try:
        print('GATE T07 PASSOU (NÃO C0-J): ' + json.dumps(audit(a.setorial_root),
                                                          ensure_ascii=False, sort_keys=True))
    except (ValueError, OSError, KeyError, csv.Error, UnicodeError) as e:
        parser.exit(1, f'FALHA GATE T07 C1: {e}\n')


if __name__ == '__main__':
    main()
