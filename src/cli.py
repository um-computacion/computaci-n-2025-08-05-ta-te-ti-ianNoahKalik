from src.tateti import Tateti
from src.tablero import Tablero
from src.excepciones import Exceptions, CasillaFueradeRango, PosOcupadaExceptions  
from src.jugador import Jugador

def main():
    print("Bienvenidos")  
    nombre1 = input("Ingrese el nombre del jugador 1 (ficha X): ")
    nombre2 = input("Ingrese el nombre del jugador 2 (ficha O): ")
    jugador1 = Jugador(nombre1.strip(), "X")  
    jugador2 = Jugador(nombre2.strip(), "O")  
    juego = Tateti(jugador1, jugador2)
    while True:
        print("Tablero:")
        print(juego.tablero.mostrar_tablero())
        print(f"Turno de {juego.turno.nombre} | ficha: {juego.turno.ficha}")  
        try:
            fila = int(input("Ingrese fila (0 a 2): ")) 
            columna = int(input("Ingrese columna (0 a 2): "))

            juego.ocupar_una_de_las_casillas(fila, columna)  
            print("Ficha colocada.")  

            ganador = juego.turno.nombre
            if juego.hay_ganador(juego.turno.ficha):
                print(juego.tablero.mostrar_tablero())  
                print(f"El ganador es: {ganador}")
                break
            elif juego.tablero.esta_lleno():
                print(juego.tablero.mostrar_tablero())
                print("El juego ha terminado en empate.")
                break
           
            juego.cambiar_turno()
        except CasillaFueradeRango:
            print("Casilla fuera de rango. Elija entre 0 y 2.")
        except PosOcupadaExceptions:
            print("Casilla ocupada. Elija otra.")
        except Exceptions as e:
            print(f"Error: {e}")
            continue

if __name__ == '__main__':
    main()