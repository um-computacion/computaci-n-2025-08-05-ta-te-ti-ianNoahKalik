from unittest.mock import patch
import unittest
from src import cli

class TestCLI(unittest.TestCase):

    @patch('builtins.input')
    @patch('builtins.print')
    def test_juego_con_ganador(self, mock_print, mock_input):
        mock_input.side_effect = ["Ana", "Luis", "0", "0", "1", "0", "1", "1", "2", "0", "2", "2"]
        cli.main()
        mock_print.assert_any_call("El ganador es: Ana")

    @patch('builtins.input')
    @patch('builtins.print')
    def test_juego_empate(self, mock_print, mock_input):
        mock_input.side_effect = ["Ana", "Luis", "0", "0", "0", "1", "0", "2", "1", "1", "1", "0", "1", "2", "2", "1", "2", "0", "2", "2"]
        cli.main()
        mock_print.assert_any_call("El juego ha terminado en empate.")

    @patch('builtins.input')
    @patch('builtins.print')
    def test_casilla_fuera_de_rango(self, mock_print, mock_input):
        mock_input.side_effect = ["Ana", "Luis", "5", "0", KeyboardInterrupt]
        with self.assertRaises(KeyboardInterrupt):
            cli.main()
        mock_print.assert_any_call("Casilla fuera de rango. Elija entre 0 y 2.")

    @patch('builtins.input')
    @patch('builtins.print')
    def test_posicion_ocupada(self, mock_print, mock_input):
        mock_input.side_effect = ["Ana", "Luis", "0", "0", "0", "0", KeyboardInterrupt]
        with self.assertRaises(KeyboardInterrupt):
            cli.main()
        mock_print.assert_any_call("Casilla ocupada. Elija otra.")

if __name__ == '__main__':
    unittest.main()