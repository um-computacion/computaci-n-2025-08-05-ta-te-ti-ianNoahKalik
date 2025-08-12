class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def __str__(self):
        return f"Jugador: {self.nombre} ficha: {self.ficha}"