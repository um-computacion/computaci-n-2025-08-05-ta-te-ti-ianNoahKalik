import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_init_nombre_y_ficha(self):
        jugador = Jugador("Lucía", "X")
        self.assertEqual(jugador.nombre, "Lucía")
        self.assertEqual(jugador.ficha, "X")

    def test_init_con_ficha_o(self):
        jugador = Jugador("Tomás", "O")
        self.assertEqual(jugador.nombre, "Tomás")
        self.assertEqual(jugador.ficha, "O")

    def test_init_con_nombres_diferentes(self):
        jugador1 = Jugador("Valentina", "X")
        jugador2 = Jugador("Mateo", "O")
        self.assertEqual(jugador1.nombre, "Valentina")
        self.assertEqual(jugador2.nombre, "Mateo")
        self.assertNotEqual(jugador1.nombre, jugador2.nombre)

    def test_init_con_fichas_diferentes(self):
        jugador1 = Jugador("Luis", "X")
        jugador2 = Jugador("Luis", "O")
        self.assertEqual(jugador1.ficha, "X")
        self.assertEqual(jugador2.ficha, "O")
        self.assertNotEqual(jugador1.ficha, jugador2.ficha)

    def test_str_varios_nombres_y_fichas(self):
        casos = [
            ("Sofia", "X", "Jugador: Sofia ficha: X"),
            ("Diego", "O", "Jugador: Diego ficha: O"),
            ("Alejandro", "X", "Jugador: Alejandro ficha: X"),
            ("A", "O", "Jugador: A ficha: O"),
        ]
        for nombre, ficha, esperado in casos:
            with self.subTest(nombre=nombre, ficha=ficha):
                jugador = Jugador(nombre, ficha)
                self.assertEqual(str(jugador), esperado)

    def test_atributos_modificables(self):
        jugador = Jugador("Juan", "X")
        jugador.nombre = "Juanito"
        jugador.ficha = "O"
        self.assertEqual(jugador.nombre, "Juanito")
        self.assertEqual(jugador.ficha, "O")

    def test_igualdad_objetos_mismo_nombre_ficha(self):
        jugador1 = Jugador("Roberto", "X")
        jugador2 = Jugador("Roberto", "X")
        self.assertNotEqual(jugador1, jugador2)
        self.assertIsNot(jugador1, jugador2)

if __name__ == '__main__':
    unittest.main()