import unittest
from src.tablero import Tablero
from src.excepciones import PosOcupadaExceptions, CasillaFueradeRango

class TestTablero(unittest.TestCase):

    def test_init(self):
        tablero = Tablero()
        contenedor_inicial = tablero.obtener_contenedor()
        self.assertEqual(len(contenedor_inicial), 3)
        self.assertEqual(contenedor_inicial[0], ["", "", ""])

    def test_poner_ficha_valida(self):
        tablero = Tablero()
        tablero.poner_la_ficha(1, 1, "O")
        self.assertEqual(tablero.obtener_contenedor()[1][1], "O")

    def test_poner_ficha_fuera_de_rango(self):
        tablero = Tablero()
        casos = [(-1, 0), (3, 0), (0, -1), (0, 3)]
        for fila, col in casos:
            with self.subTest(fila=fila, col=col):
                with self.assertRaises(CasillaFueradeRango):
                    tablero.poner_la_ficha(fila, col, "X")

    def test_poner_ficha_posicion_ocupada(self):
        tablero = Tablero()
        tablero.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaExceptions):
            tablero.poner_la_ficha(0, 0, "O")

    def test_esta_lleno_false(self):
        tablero = Tablero()
        self.assertFalse(tablero.esta_lleno())

    def test_esta_lleno_true(self):
        tablero_lleno = Tablero()
        for fila in range(3):
            for col in range(3):
                tablero_lleno.poner_la_ficha(fila, col, "X")
        self.assertTrue(tablero_lleno.esta_lleno())

if __name__ == '__main__':
    unittest.main()