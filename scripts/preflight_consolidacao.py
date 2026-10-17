#!/usr/bin/env python3
"""Porta estrutural reproduzível para o corpus experimental CLF.

Não autentica DOU, vigência, C0-J, reforma ou veículo DEC-016.
Valida somente o snapshot disponível, sem escrever derivados.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


def inside(root: Path, value: str) -> Path:
    p = Path(value)
    if p.is_absolute() or not value or '..' in p.parts or value == '.':
        raise ValueError(f"Caminho inseguro: {value}")
    target = (root / p).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"Escapa do checkout: {value}")
    return target


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def books_from(root: Path) -> list[dict]:
    index = root / 'produto/fontes/indice_livros.json'
    if not index.is_file():
        raise ValueError('Índice de Livros ausente (a main sem corpus não é candidata)')
    obj = json.loads(index.read_text(encoding='utf-8'))
    if obj.get('schema_version') != 1 or not isinstance(obj.get('livros'), list):
        raise ValueError('Esquema/array de Livros inválidos')
    return obj['livros']


def inspect(root: Path, base: Path | None = None) -> dict:
    books = books_from(root)
    if not books:
        raise ValueError('Nenhum Livro declarado')
    seen_ids, seen_views = set(), set()
    local, external, composite, articles, records = 0, 0, 0, 0, 0
    previous = {}
    if base is not None and (base / 'produto/fontes/indice_livros.json').is_file():
        for book in books_from(base):
            previous[book['id']] = (
                git_blob(inside(base, book['vista'])),
                git_blob(inside(base, book['manifesto']))
            )
    for b in books:
        ident, view_path, manifest_path = b['id'], b['vista'], b['manifesto']
        if not ident or ident in seen_ids or view_path in seen_views:
            raise ValueError(f'ID/vista repetido: {ident}')
        seen_ids.add(ident)
        seen_views.add(view_path)
        if not view_path.startswith('produto/vistas/') or not manifest_path.startswith('produto/fontes/'):
            raise ValueError(f'Posição inesperada de vista/manifesto: {ident}')
        view, manifest = inside(root, view_path), inside(root, manifest_path)
        m = json.loads(manifest.read_text(encoding='utf-8'))
        if not b.get('estado', '').startswith('INTEGRADO_EXPERIMENTAL'):
            raise ValueError(f'Estado não experimental: {ident}')
        if m.get('dec016') not in (None, 'PENDENTE'):
            raise ValueError(f'DEC-016 promovida sem decisão: {ident}')
        if m.get('material_approved') is True or m.get('aprovacao_material') == 'SIM':
            raise ValueError(f'Aprovação material alegada: {ident}')
        legal = next((m.get(k) for k in ('legal_status', 'estado_juridico', 'status_juridico') if m.get(k)), None)
        if legal != 'Q_SEM_C0_J':
            raise ValueError(f'Estado jurídico incompatível com lote Q: {ident}: {legal}')
        if m.get('view_path', m.get('vista_relativa', view_path)) != view_path:
            raise ValueError(f'Manifesto aponta outra vista: {ident}')
        nart = sum(line.startswith('**Art. ') for line in view.read_text(encoding='utf-8').splitlines())
        if nart != b['artigos']:
            raise ValueError(f'Contagem de artigos divergente: {ident}')
        expected = m.get('count_expected', (m.get('contagens_esperadas') or {}).get('fontes'))
        if expected != b['registros_documentais']:
            raise ValueError(f'Contagem documental divergente: {ident}: {expected}')
        src, sha = m.get('source_path'), m.get('source_blob_sha')
        source = inside(root, src) if src else None
        pinned = re.fullmatch(r'[0-9a-f]{40}', str(m.get('setorial_commit') or '')) is not None
        if source is not None and sha and source.is_file() and 'components' not in m:
            if not re.fullmatch(r'[0-9a-f]{40}', str(sha)) or git_blob(source) != sha:
                raise ValueError(f'Blob de origem divergente: {ident}')
            if source.suffix == '.csv':
                with source.open(encoding='utf-8-sig', newline='') as h:
                    total = sum(1 for _ in csv.DictReader(h, strict=True))
                if total != expected:
                    raise ValueError(f'Inventário com cardinalidade divergente: {ident}')
            local += 1
        elif 'components' in m:
            parts = m['components']
            if not isinstance(parts, list) or not parts:
                raise ValueError(f'Composto vazio: {ident}')
            if source is not None and source.is_file():
                if not sha or not re.fullmatch(r'[0-9a-f]{40}', str(sha)) or git_blob(source) != sha:
                    raise ValueError(f'Blob de origem divergente: {ident}')
            if any(not isinstance(c, dict) or type(c.get('count')) is not int
                   or c['count'] <= 0 for c in parts):
                raise ValueError(f'Componente sem contagem válida: {ident}')
            if sum(c['count'] for c in parts) != expected:
                raise ValueError(f'Cardinalidade composta divergente: {ident}')
            seen_parts = set()
            for part in parts:
                for path_key, blob_key in (
                    ('path', 'git_blob'),
                    ('concordance_path', 'concordance_git_blob'),
                    ('view_part_path', 'view_part_git_blob'),
                ):
                    if path_key not in part and blob_key not in part:
                        continue
                    rel, declared = part.get(path_key), part.get(blob_key)
                    if (not isinstance(rel, str) or not isinstance(declared, str)
                            or not re.fullmatch(r'[0-9a-f]{40}', declared)):
                        raise ValueError(f'Componente sem par caminho/SHA válido: {ident}/{path_key}')
                    if rel in seen_parts:
                        raise ValueError(f'Arquivo composto duplicado: {ident}/{rel}')
                    seen_parts.add(rel)
                    item = inside(root, rel)
                    if not item.is_file() or git_blob(item) != declared:
                        raise ValueError(f'Blob de componente divergente: {ident}/{rel}')
                if 'path' not in part:
                    raise ValueError(f'Componente sem arquivo principal: {ident}')
            composite += 1
        elif pinned and (
            # T25: fonte setorial identificada por caminho e SHA, mas ausente deste checkout.
            (source is not None and sha and re.fullmatch(r'[0-9a-f]{40}', str(sha))) or
            # T07: texto e concordância externos, cada qual com caminho e SHA explícitos.
            (source is None and m.get('texto_relativo') and m.get('concordancia_relativa')
             and re.fullmatch(r'[0-9a-f]{40}', str(m.get('texto_blob_sha') or ''))
             and re.fullmatch(r'[0-9a-f]{40}', str(m.get('concordancia_blob_sha') or '')))
        ):
            # Proveniência apenas declarada: checkout externo continua PENDENTE.
            external += 1
        else:
            raise ValueError(f'Origem ausente/não identificada: {ident}')
        if ident in previous and previous[ident] != (git_blob(view), git_blob(manifest)):
            raise ValueError(f'Livro antigo alterado, requer auditoria específica: {ident}')
        articles += nart
        records += expected
    code = root / 'produto/CODIGO_DE_TRABALHO.md'
    if not code.is_file() or sum(line.startswith('**Art. ') for line in code.read_text(encoding='utf-8').splitlines()) != articles:
        raise ValueError('Código derivado ausente ou contagem de artigos divergente')
    return dict(livros=len(books), titulos=len({b['titulo'] for b in books}), artigos=articles,
                registros_documentais=records, locais=local, externos_pendentes=external,
                compostos_pendentes=composite, livros_preservados=len(previous))


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path('.'))
    p.add_argument('--base', type=Path)
    args = p.parse_args()
    try:
        outcome = inspect(args.root.resolve(), args.base.resolve() if args.base else None)
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError, csv.Error) as exc:
        p.exit(1, f'FALHA PREFLIGHT Q: {exc}\n')
    print('PASSOU PREFLIGHT ESTRUTURAL (NÃO C0-J): ' + json.dumps(outcome, ensure_ascii=False, sort_keys=True))
    if outcome['externos_pendentes'] or outcome['compostos_pendentes']:
        print('PENDENTE: cotejo dos checkouts setoriais externos/compostos; sem homologação.')


if __name__ == '__main__':
    main()
