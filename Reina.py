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


    def comprobacion(self):



    def movimiento(self):
        for i in range(self.n):
            for j in range(self.n):
                self.tablero[i][j] == "X"
                self.comprobacion()            

    def resultado(self):
        resultado = []
        for i in range(self.n):
            for j in range(self.n):
                if self.tablero[i][j] == "X":
                    resultado.append(self.tablero().index("X"))
                else:
                    pass
        return resultado



if __name__ == "__main__":

    n = int(input("Introduzca un numero: "))
    hola = Reina(n)
    print(hola.tablero())