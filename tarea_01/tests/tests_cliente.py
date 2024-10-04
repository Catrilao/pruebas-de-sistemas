import unittest

from src import distance_client


class TestCliente(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.latitud_valida = 50
        cls.latitud_no_valida = -91
        cls.longitud_valida = 60
        cls.longitud_no_valida = -181
        cls.latitud_menor_90_neg = -91
        cls.latitud_mayor_90 = 91
        cls.longitud_menor_180_neg = -181
        cls.longitud_mayor_180 = 181
        cls.unidad_km = "km"
        cls.unidad_nm = "nm"
        cls.unidad_invalida = "invalid"
        cls.res_distancia_invalida = -1.0
        cls.print_message = False

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.latitud_valida
        del cls.latitud_no_valida
        del cls.longitud_valida
        del cls.longitud_no_valida
        del cls.latitud_menor_90_neg
        del cls.latitud_mayor_90
        del cls.longitud_menor_180_neg
        del cls.longitud_mayor_180
        del cls.unidad_km
        del cls.unidad_nm
        del cls.unidad_invalida
        del cls.res_distancia_invalida
        del cls.print_message

    def test_latitud_no_valida(self):
        response = distance_client.main(
            source=(self.latitud_no_valida, self.longitud_valida),
            destination=(self.latitud_valida, self.longitud_valida),
            unit=self.unidad_km,
            print_message=self.print_message,
        )

        self.assertEqual(response["Distance"], self.res_distancia_invalida)
        self.assertEqual(response["Distance unit"], self.unidad_invalida)

    # verificar que la respuesta coincide con km
    def test_respuesta_en_km(self):
        response = distance_client.main(
            source=(self.latitud_valida, self.longitud_valida),
            destination=(self.latitud_valida + 10, self.longitud_valida + 10),
            unit=self.unidad_km,
            print_message=self.print_message,
        )

        # Verificar que la respuesta contiene la unidad "km"
        self.assertEqual(response["Distance unit"], self.unidad_km)

    # verificar que la respuesta coincide con nm
    def test_respuesta_en_nm(self):
        response = distance_client.main(
            source=(self.latitud_valida, self.longitud_valida),
            destination=(self.latitud_valida + 10, self.longitud_valida + 10),
            unit=self.unidad_nm,
            print_message=self.print_message,
        )
        # Verificar que la respuesta contiene la unidad "nm"
        self.assertEqual(response["Distance unit"], self.unidad_nm)

    # verificar que la respuesta sea km cuando  esté en blanco
    def test_respuesta_predeterminada_km(self):
        response = distance_client.main(
            source=(self.latitud_valida, self.longitud_valida),
            destination=(self.latitud_valida + 10, self.longitud_valida + 10),
            unit="",  # No se especifica la unidad
            print_message=self.print_message,
        )
        self.assertEqual(response["Distance unit"], self.unidad_km)

    def test_latitud_menor_90_negativo(self):
        response = distance_client.main(
            source=(self.latitud_menor_90_neg, self.latitud_valida),
            destination=(self.latitud_valida, self.longitud_valida),
            unit=self.unidad_km,
            print_message=self.print_message,
        )

        self.assertEqual(response["Distance"], self.res_distancia_invalida)
        self.assertEqual(response["Distance unit"], self.unidad_invalida)

    def test_latitud_mayor_90(self):
        response = distance_client.main(
            source=(self.latitud_mayor_90, self.latitud_valida),
            destination=(self.latitud_valida, self.longitud_valida),
            unit=self.unidad_km,
            print_message=self.print_message,
        )
        self.assertEqual(response["Distance"], self.res_distancia_invalida)
        self.assertEqual(response["Distance unit"], self.unidad_invalida)

    def test_longitud_menor_180_neg(self):
        response = distance_client.main(
            source=(self.latitud_valida, self.longitud_menor_180_neg),
            destination=(self.latitud_valida, self.longitud_valida),
            unit=self.unidad_km,
            print_message=self.print_message,
        )

        self.assertEqual(response["Distance"], self.res_distancia_invalida)
        self.assertEqual(response["Distance unit"], self.unidad_invalida)

    def test_longitud_mayor_180(self):
        response = distance_client.main(
            source=(self.latitud_valida, self.longitud_mayor_180),
            destination=(self.latitud_valida, self.longitud_valida),
            unit=self.unidad_km,
            print_message=self.print_message,
        )

        self.assertEqual(response["Distance"], self.res_distancia_invalida)
        self.assertEqual(response["Distance unit"], self.unidad_invalida)


if __name__ == "__main__":
    unittest.main()
