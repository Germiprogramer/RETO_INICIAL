#Creamos la clase tablero que creara el tbalero nxn
class Reina:
    def __init__(self, n):
        self.n = n
    
    def tablero(self):
        tablero = []
        for i in range(n):
            fila = []
            for m in range(n):
                fila.append(" ")
            tablero.append(fila)
        return tablero


if __name__ == "__main__":
    n = int(input("Introduzca un numero: "))
    hola = Reina(n)
    print(hola.tablero())