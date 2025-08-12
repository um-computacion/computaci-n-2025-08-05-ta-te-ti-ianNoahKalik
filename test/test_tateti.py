import unittest
from src.tateti import Tateti
from src.tablero import Tablero
from src.jugador import Jugador

class TestTateti(unittest.TestCase):

    def test_init(self):
        jugador1 = Jugador("Lucía", "X")
        jugador2 = Jugador("Tomás", "O")
        juego = Tateti(jugador1, jugador2)
        self.assertEqual(juego.turno, jugador1)
        self.assertIsInstance(juego.tablero, Tablero)

    def test_ocupar_casilla(self):
        jugador1 = Jugador("Lucía", "X")
        jugador2 = Jugador("Tomás", "O")
        juego = Tateti(jugador1, jugador2)
        juego.ocupar_una_de_las_casillas(1, 1)
        self.assertEqual(juego.tablero.obtener_contenedor()[1][1], "X")

    def test_cambiar_turno_x_a_o(self):
        jugador1 = Jugador("Lucía", "X")
        jugador2 = Jugador("Tomás", "O")
        juego = Tateti(jugador1, jugador2)
        self.assertEqual(juego.turno, jugador1)
        juego.cambiar_turno()
        self.assertEqual(juego.turno, jugador2)

    def test_cambiar_turno_o_a_x(self):
        jugador1 = Jugador("Lucía", "X")
        jugador2 = Jugador("Tomás", "O")
        juego = Tateti(jugador1, jugador2)
        juego.turno = jugador2
        juego.cambiar_turno()
        self.assertEqual(juego.turno, jugador1)

    def test_hay_ganador_varios_casos(self):
        jugador1 = Jugador("Lucía", "X")
        jugador2 = Jugador("Tomás", "O")
        casos = [
            [(0, 0), (0, 1), (0, 2)],  # fila
            [(0, 0), (1, 0), (2, 0)],  # columna
            [(0, 0), (1, 1), (2, 2)],  # diagonal principal
            [(0, 2), (1, 1), (2, 0)],  # diagonal secundaria
        ]
        for posiciones in casos:
            with self.subTest(posiciones=posiciones):
                juego = Tateti(jugador1, jugador2)
                for fila, col in posiciones:
                    juego.tablero.poner_la_ficha(fila, col, "X")
                self.assertTrue(juego.hay_ganador("X"))

    def test_no_hay_ganador(self):
        jugador1 = Jugador("Lucía", "X")
        jugador2 = Jugador("Tomás", "O")
        juego = Tateti(jugador1, jugador2)
        self.assertFalse(juego.hay_ganador("X"))

if __name__ == '__main__':
    unittest.main()