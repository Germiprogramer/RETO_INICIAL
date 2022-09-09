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


    #Metodo que comprueba que la solucion sea correcta
    def comprobacion(self):
        solucion = False
        #Aqui iria el codigo que verifica que la solucion sea correcta
        if solucion:
            return True
        else:
            return False


    #Metodo que nos devuelve el tablero con una solucion
    def movimiento(self):
        for i in range(self.n):
            for j in range(self.n):
                self.tablero()[i][j] == "X"
                if self.comprobacion():
                    break
                else:
                    pass          


    #Metodo que nos devuelve la solucion de las reinas
    def resultado(self):
        self.movimiento()
        resultado = []
        for i in range(self.n):
            for j in range(self.n):
                if self.tablero()[i][j] == "X":
                    #Añadimos el indice de la lista donde esta la reina en la solucion final
                    resultado.append(self.tablero().index("X"))
                else:
                    pass
        return resultado



if __name__ == "__main__":

    n = int(input("Introduzca un numero: "))
    solucion = Reina(n)
    print(solucion.resultado())