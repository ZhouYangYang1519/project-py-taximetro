
import unittest
from taximetro_oop import Taximetro, Carrera, Historial


class TestTaximetro(unittest.TestCase):

    def test_estado_inicial(self):
        taxi = Taximetro()

        self.assertEqual(taxi.cuenta, 0.0)
        self.assertEqual(taxi.estado, "parado")
        self.assertFalse(taxi.viaje_activo)

    def test_calculo_importe(self):
        taxi = Taximetro()

        taxi.estado = "movimiento"
        resultado = taxi.cuenta_total(10)
        self.assertAlmostEqual(resultado, 0.50, places=2)

        taxi.estado = "parado"
        resultado = taxi.cuenta_total(5)
        self.assertAlmostEqual(resultado, 0.60, places=2)

    def test_inicio_duplicado(self):
        taxi = Taximetro()
        taxi.iniciar_carrera()

        with self.assertRaises(ValueError):
            taxi.iniciar_carrera()

    def test_estado_invalido(self):
        taxi = Taximetro()
        taxi.iniciar_carrera()

        with self.assertRaises(ValueError):
            taxi.cambiar_estado("volando")

    def test_finalizar_sin_iniciar(self):
        taxi = Taximetro()

        with self.assertRaises(ValueError):
            taxi.finalizar_carrera()

    def test_carrera(self):
        carrera = Carrera("C001", "T001", 100.0)
        carrera.finalizar(0.70, 120.0)

        self.assertEqual(carrera.id_cliente, "C001")
        self.assertEqual(carrera.id_taxista, "T001")
        self.assertEqual(carrera.duracion_segundos, 20.0)
        self.assertAlmostEqual(carrera.importe, 0.70)


if __name__ == "__main__":
    unittest.main()
