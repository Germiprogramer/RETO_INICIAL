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
    

hola = Tablero(5)