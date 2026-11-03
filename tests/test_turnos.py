"""Pruebas de regresión del sistema de turnos, solo con unittest."""
import unittest
from datetime import date
from turnos import ErrorAsignacion, SistemaTurnos, TURNOS, generar_turnos


class TestTurnos(unittest.TestCase):
    DIA = date(2026, 11, 3)

    def test_diez_franjas_entre_12_y_1430(self):
        self.assertEqual(len(generar_turnos()), 10)
        self.assertEqual(TURNOS[0].inicio.strftime("%H:%M"), "12:00")
        self.assertEqual(TURNOS[-1].fin.strftime("%H:%M"), "14:30")

    def test_asigna_primero_turno_menos_ocupado(self):
        sistema = SistemaTurnos(capacidad_por_turno=2)
        self.assertEqual(sistema.asignar("A001", self.DIA).numero, 1)
        self.assertEqual(sistema.asignar("A002", self.DIA).numero, 2)
        self.assertEqual(sistema.asignar("A003", self.DIA).numero, 3)

    def test_no_duplica_estudiante_mismo_dia(self):
        sistema = SistemaTurnos()
        sistema.asignar("A001", self.DIA)
        with self.assertRaises(ErrorAsignacion):
            sistema.asignar(" A001 ", self.DIA)

    def test_permite_mismo_estudiante_distinto_dia(self):
        sistema = SistemaTurnos()
        sistema.asignar("A001", self.DIA)
        self.assertEqual(sistema.asignar("A001", date(2026, 11, 4)).numero, 1)

    def test_rechaza_sin_cupos(self):
        sistema = SistemaTurnos(capacidad_por_turno=1)
        for i in range(10):
            sistema.asignar(f"A{i:03}", self.DIA)
        with self.assertRaisesRegex(ErrorAsignacion, "No quedan cupos"):
            sistema.asignar("A999", self.DIA)

    def test_rechaza_codigo_invalido(self):
        sistema = SistemaTurnos()
        for codigo in ["", "   ", None]:
            with self.subTest(codigo=codigo), self.assertRaises(ErrorAsignacion):
                sistema.asignar(codigo, self.DIA)

    def test_capacidad_valida(self):
        for capacidad in [0, -3, 1.1, True]:
            with self.subTest(capacidad=capacidad), self.assertRaises(ValueError):
                SistemaTurnos(capacidad)

    def test_consulta_turno(self):
        sistema = SistemaTurnos()
        self.assertIsNone(sistema.consultar_asignacion("A100", self.DIA))
        sistema.asignar("A100", self.DIA)
        self.assertEqual(sistema.consultar_asignacion("A100", self.DIA).numero, 1)

    def test_mantiene_ocupacion_separada_por_dia(self):
        sistema = SistemaTurnos()
        sistema.asignar("A100", self.DIA)
        self.assertEqual(sistema.ocupacion(self.DIA)[1], 1)
        self.assertEqual(sistema.ocupacion(date(2026, 11, 4))[1], 0)


if __name__ == "__main__":
    unittest.main()
