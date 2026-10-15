"""Testes isolados da fila operacional CF/CLF, sem acesso a rede ou GitHub Actions."""
from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("controle_operacional", ROOT / "scripts/controle_operacional.py")
assert spec is not None and spec.loader is not None
ops = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ops)


class FilaOperacionalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.queue_original = ops.QUEUE
        ops.QUEUE = Path(self.temp.name) / "fila.csv"
        self.module = "M07" if ops.CF else "T07.M03"
        self.other_module = "M08" if ops.CF else "T24.M01"
        self.allowed = {"M07", "M08"} if ops.CF else {"T07", "T24"}

    def tearDown(self) -> None:
        ops.QUEUE = self.queue_original
        self.temp.cleanup()

    def item(self, number: int, **overrides: str) -> dict[str, str]:
        value = {key: "" for key in ops.FIELDS}
        value.update({
            "id": f"{ops.PROJECT}-TEST-{number:03}",
            "modulo": self.module,
            "recorte": "Revisar fonte de teste",
            "estado": "PRONTA",
            "prioridade": "P1",
            "criterio_aceite": "Entregar demonstracao documental",
        })
        value.update(overrides)
        return value

    def save(self, *items: dict[str, str]) -> None:
        with ops.QUEUE.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=ops.FIELDS, lineterminator="\n")
            writer.writeheader()
            writer.writerows(items)

    def active(self, number: int, **overrides: str) -> dict[str, str]:
        future = datetime.now(timezone.utc) + timedelta(hours=2)
        return self.item(
            number, estado="EM_EXECUCAO", responsavel="execucao-teste",
            branch="test/escopo", base_sha="a" * 40,
            reserva_ate=future.isoformat().replace("+00:00", "Z"), **overrides
        )

    def test_fila_pronta_valida(self) -> None:
        self.save(self.item(1), self.item(2, modulo=self.other_module))
        self.assertEqual(ops.check_queue(self.allowed), [])

    def test_duas_reservas_no_mesmo_recorte_sao_rejeitadas(self) -> None:
        self.save(self.active(1), self.active(2))
        with self.assertRaisesRegex(ValueError, "Duas reservas ativas"):
            ops.check_queue(self.allowed)

    def test_reservas_de_recortes_diferentes_sao_validas(self) -> None:
        self.save(self.active(1), self.active(2, recorte="Outro recorte independente"))
        self.assertEqual(ops.check_queue(self.allowed), [])

    def test_reserva_maior_que_24_horas_e_rejeitada(self) -> None:
        distant = (datetime.now(timezone.utc) + timedelta(hours=25)).isoformat()
        self.save(self.active(1, reserva_ate=distant))
        with self.assertRaisesRegex(ValueError, "24h"):
            ops.check_queue(self.allowed)

    def test_reserva_expirada_nao_e_concluida_automaticamente(self) -> None:
        expired = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        self.save(self.active(1, reserva_ate=expired))
        warnings = ops.check_queue(self.allowed)
        self.assertEqual(len(warnings), 1)
        self.assertIn("EXPIRADA", warnings[0])

    def test_bloqueio_sem_evidencia_e_rejeitado(self) -> None:
        self.save(self.item(1, estado="BLOQUEADA"))
        with self.assertRaisesRegex(ValueError, "Bloqueio sem evidencia"):
            ops.check_queue(self.allowed)

    def test_bloqueio_documentado_e_aceito(self) -> None:
        self.save(self.item(1, estado="BLOQUEADA", ultima_entrega="incidente Actions #123"))
        self.assertEqual(ops.check_queue(self.allowed), [])

    def test_fila_real_do_checkout_e_valida(self) -> None:
        ops.QUEUE = self.queue_original
        if ops.CF:
            allowed = {f"M{i:02d}" for i in range(15)}
        else:
            allowed = {f"T{i:02d}" for i in range(1, 49)}
        self.assertEqual(ops.check_queue(allowed), [])


if __name__ == "__main__":
    unittest.main()
