"""Asignación de turnos de almuerzo universitario, sin almacenamiento persistente."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta


@dataclass(frozen=True)
class Turno:
    numero: int
    inicio: time
    fin: time


def generar_turnos() -> tuple[Turno, ...]:
    """Genera diez franjas de quince minutos desde las 12:00 hasta las 14:30."""
    base = datetime.combine(date(2000, 1, 1), time(12, 0))
    return tuple(
        Turno(
            numero=i + 1,
            inicio=(base + timedelta(minutes=i * 15)).time(),
            fin=(base + timedelta(minutes=(i + 1) * 15)).time(),
        )
        for i in range(10)
    )


TURNOS = generar_turnos()


class ErrorAsignacion(ValueError):
    """Error de validación o falta de disponibilidad de turnos."""


class SistemaTurnos:
    """Asignación determinista al turno con menor ocupación, con cupos diarios."""
    def __init__(self, capacidad_por_turno: int = 30) -> None:
        if type(capacidad_por_turno) is not int or capacidad_por_turno <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo")
        self.capacidad_por_turno = capacidad_por_turno
        self._asignaciones: dict[date, dict[str, int]] = {}
        self._ocupacion: dict[date, dict[int, int]] = {}

    def asignar(self, codigo: str, dia: date | None = None) -> Turno:
        """Asigna un solo turno por estudiante y día, respetando el aforo."""
        if not isinstance(codigo, str) or not codigo.strip():
            raise ErrorAsignacion("El código de estudiante no puede estar vacío")
        if dia is None:
            dia = date.today()
        if not isinstance(dia, date) or isinstance(dia, datetime):
            raise ErrorAsignacion("La fecha debe ser de tipo date")
        codigo = codigo.strip()
        asignaciones = self._asignaciones.setdefault(dia, {})
        if codigo in asignaciones:
            raise ErrorAsignacion("El estudiante ya tiene un turno asignado hoy")
        ocupacion = self._ocupacion.setdefault(dia, {t.numero: 0 for t in TURNOS})
        disponibles = [t for t in TURNOS if ocupacion[t.numero] < self.capacidad_por_turno]
        if not disponibles:
            raise ErrorAsignacion("No quedan cupos de almuerzo para esa fecha")
        turno = min(disponibles, key=lambda t: (ocupacion[t.numero], t.numero))
        asignaciones[codigo] = turno.numero
        ocupacion[turno.numero] += 1
        return turno

    def ocupacion(self, dia: date | None = None) -> dict[int, int]:
        dia = dia or date.today()
        return dict(self._ocupacion.get(dia, {t.numero: 0 for t in TURNOS}))

    def consultar_asignacion(self, codigo: str, dia: date | None = None) -> Turno | None:
        dia = dia or date.today()
        numero = self._asignaciones.get(dia, {}).get(codigo.strip())
        return next((t for t in TURNOS if t.numero == numero), None)
