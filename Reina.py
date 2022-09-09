class Reina:
    def __init__(self, n):
        self.n = n
    
    #Metodo que crea el tablero como una lista de listas
    def tablero(self):
        tablero = []
        for i in range(self.n):
            fila = []
            for m in range(self.n):
                fila.append(" ")
            tablero.append(fila)
        return tablero

    #Metodo para el posicionamiento de las reinas
    #De esta manera elaboraremos un algoritmo que nos de una solucion para n
    def mov_caballo(self):
        #En esta funcion se define el posicionamiento como el movimiento de los caballos del ajedrez


if __name__ == "__main__":

    n = int(input("Introduzca un numero: "))
    hola = Reina(n)
    print(hola.tablero())