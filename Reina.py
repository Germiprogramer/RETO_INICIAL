#Creamos la clase tablero que creara el tbalero nxn
class Tablero:
    def __init__(self, n):
        self.n = n
        tablero = []
        for i in range(n):
            fila = []
            for m in range(n):
                fila.append(" ")
            tablero.append(fila)
        print (tablero)
    

if __name__ == "__main__":
    n = int(input("Introduzca un numero: "))
    hola = Tablero(n)