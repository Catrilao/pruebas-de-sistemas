import unittest

from tarea01 import geo_location


class DistanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.latitud_menor_90_neg = -91
        cls.latitud_mayor_90 = 91
        cls.longitud_menor_180_neg = -181
        cls.longitud_mayor_180 = 181
        cls.latitud_valida = 50
        cls.longitud_valida = 50
        cls.altura = 0

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.latitud_menor_90_neg
        del cls.latitud_mayor_90
        del cls.longitud_menor_180_neg
        del cls.longitud_mayor_180
        del cls.latitud_valida
        del cls.longitud_valida
        del cls.altura

    def test_latitud_menor_90_negativo(self):
        with self.assertRaises(ValueError):
            geo_location.Position(
                self.latitud_menor_90_neg, self.longitud_valida, self.altura
            )

        self.assertRaises(ValueError)

    def test_latitud_mayor_90(self):
        with self.assertRaises(ValueError):
            geo_location.Position(
                self.latitud_mayor_90, self.longitud_valida, self.altura
            )

        self.assertRaises(ValueError)

    def test_longitud_mayor_180(self):
        with self.assertRaises(ValueError):
            geo_location.Position(
                self.latitud_valida, self.longitud_mayor_180, self.altura
            )

        self.assertRaises(ValueError)

    def test_longitud_menor_180_negativo(self):
        with self.assertRaises(ValueError):
            geo_location.Position(
                self.latitud_valida, self.longitud_menor_180_neg, self.altura
            )

        self.assertRaises(ValueError)


if __name__ == "__main__":
    unittest.main()
