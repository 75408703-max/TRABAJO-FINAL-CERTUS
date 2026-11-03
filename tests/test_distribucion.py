import unittest
from datetime import date
from turnos import SistemaTurnos


class TestDistribucion(unittest.TestCase):

    def test_distribucion_equilibrada(self):
        sistema = SistemaTurnos(capacidad_por_turno=2)
        dia = date(2026, 11, 3)

        for i in range(20):
            sistema.asignar(f"EST{i:03}", dia)

        ocupacion = sistema.ocupacion(dia)

        for numero in range(1, 11):
            self.assertEqual(ocupacion[numero], 2)


if __name__ == "__main__":
    unittest.main()
