from src.tablero import Tablero
from src.jugador import Jugador

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = jugador1
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self, fila, columna):
        self.tablero.poner_la_ficha(fila, columna, self.turno.ficha)

    def cambiar_turno(self):
        self.turno = self.jugador2 if self.turno == self.jugador1 else self.jugador1

    def hay_ganador(self, ficha):
        # Verificar filas
        for fila in self.tablero.obtener_contenedor():
            if all(casilla == ficha for casilla in fila):
                return True

        # Verificar columnas
        for col in range(3):
            if all(self.tablero.obtener_contenedor()[fila][col] == ficha for fila in range(3)):
                return True

        # Verificar diagonal principal
        if all(self.tablero.obtener_contenedor()[i][i] == ficha for i in range(3)):
            return True

        # Verificar diagonal secundaria
        if all(self.tablero.obtener_contenedor()[i][2 - i] == ficha for i in range(3)):
            return True

        return False