import unittest

from src import distance_client
import helpers


class DistanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.latitud_menor_90_neg = -91
        cls.latitud_mayor_90 = 91
        cls.longitud_menor_180_neg = -181
        cls.longitud_mayor_180 = 181
        cls.latitud_valida = 50
        cls.longitud_valida = 50
        cls.unidad_km = "km"
        cls.unidad_nm = "nm"
        cls.delta = 10
        cls.print_message = False

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.latitud_menor_90_neg
        del cls.latitud_mayor_90
        del cls.longitud_menor_180_neg
        del cls.longitud_mayor_180
        del cls.latitud_valida
        del cls.longitud_valida
        del cls.unidad_km
        del cls.unidad_nm
        del cls.delta
        del cls.print_message

    def test_distance_inicio_final_iguales(self):
        coordenadas = (self.latitud_valida, self.longitud_valida)

        distance_test = distance_client.main(
            source=coordenadas,
            destination=coordenadas,
            unit=self.unidad_km,
            print_message=self.print_message,
        )

        self.assertEquals(0, distance_test["distance"])

    def test_distance_nm(self):
        begin = (self.latitud_valida, self.longitud_valida)
        end = (self.latitud_valida + 20, self.longitud_valida + 10)

        distance_pred = distance_client.main(
            source=begin,
            destination=end,
            unit=self.unidad_nm,
            print_message=self.print_message,
        )
        distance_true = helpers.distance(
            source=begin,
            destination=end,
            unit=self.unidad_nm,
        )

        self.assertAlmostEqual(
            distance_pred["Distance"], distance_true["distance"], delta=self.delta
        )

    def test_distance_km(self):
        begin = (self.latitud_valida, self.longitud_valida)
        end = (self.latitud_valida + 20, self.longitud_valida + 10)

        distance_pred = distance_client.main(
            source=begin,
            destination=end,
            unit=self.unidad_km,
            print_message=self.print_message,
        )
        distance_true = helpers.distance(
            source=begin,
            destination=end,
            unit=self.unidad_km,
        )

        self.assertAlmostEqual(
            distance_pred["Distance"], distance_true["distance"], delta=self.delta
        )

    def test_distance_sin_unidad(self):
        begin = (self.latitud_valida, self.longitud_valida)
        end = (self.latitud_valida + 20, self.longitud_valida + 10)

        distance_pred = distance_client.main(
            source=begin,
            destination=end,
            unit="",
            print_message=self.print_message,
        )
        distance_true = helpers.distance(
            source=begin,
            destination=end,
            unit="",
        )

        self.assertAlmostEqual(
            distance_pred["Distance"], distance_true["distance"], delta=self.delta
        )

        self.assertEqual(distance_pred["Distance unit"], self.unidad_km)


if __name__ == "__main__":
    unittest.main()
