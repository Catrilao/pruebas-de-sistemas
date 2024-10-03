import unittest
from unittest.mock import patch

from src import distance_client


class TestCliente(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.latitud_valida = 50
        cls.latitud_no_valida = -91
        cls.longitud_valida = 60
        cls.longitud_no_valida = -181
        cls.unidad_km = "km"
        cls.unidad_nm = "nm"
        cls.unidad_invalida = "invalid"
        cls.res_distancia_invalida = -1.0
        cls.metodo = "geodesic"

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.latitud_valida
        del cls.latitud_no_valida
        del cls.longitud_valida
        del cls.longitud_no_valida
        del cls.unidad_km
        del cls.unidad_nm
        del cls.unidad_invalida
        del cls.res_distancia_invalida

    def test_latitud_no_valida(cls):
        with patch("builtins.print") as mocked_print:
            distance_client.main(
                source=(cls.latitud_no_valida, cls.longitud_valida),
                destination=(cls.latitud_valida, cls.longitud_valida),
                unit=cls.unidad_km,
            )

            mocked_print.assert_any_call("Distance:", cls.res_distancia_invalida)
            mocked_print.assert_any_call("Distance unit:", cls.unidad_invalida)

        # verificar que la respuesta coincide con km
        def test_respuesta_en_km(cls):
            with patch("builtins.print") as mocked_print:
                distance_client.main(
                    source=(cls.latitud_valida, cls.longitud_valida),
                    destination=(cls.latitud_valida + 10, cls.longitud_valida + 10),
                    unit=cls.unidad_km,
                )
                # Verificar que la respuesta contiene la unidad "km"
                mocked_print.assert_any_call("Distance unit:", cls.unidad_km)

        # verificar que la respuesta coincide con nm
        def test_respuesta_en_nm(cls):
            with patch("builtins.print") as mocked_print:
                distance_client.main(
                    source=(cls.latitud_valida, cls.longitud_valida),
                    destination=(cls.latitud_valida + 10, cls.longitud_valida + 10),
                    unit=cls.unidad_nm,
                )
                # Verificar que la respuesta contiene la unidad "nm"
                mocked_print.assert_any_call("Distance unit:", cls.unidad_nm)

        # verificar que la respuesta sea km cuando  esté en blanco
        def test_respuesta_predeterminada_km(cls):
            with patch("builtins.print") as mocked_print:
                distance_client.main(
                    source=(cls.latitud_valida, cls.longitud_valida),
                    destination=(cls.latitud_valida + 10, cls.longitud_valida + 10),
                    unit="",  # No se especifica la unidad
                )
                mocked_print.assert_any_call("Distance unit:", cls.unidad_km)


if __name__ == "__main__":
    unittest.main()
