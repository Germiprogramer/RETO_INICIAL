# RETO_INICIAL

Colaboradores
· Gonzalo Martínez, Rubén Nogueras, Germán Llorente, Carlos Puigserver, Alex Muñoz, Pelayo Huertas, Miguel González

El link al repositorio es el siguiente: https://github.com/Germiprogramer/RETO_INICIAL.git

El trabajo se divide en dos partes principales, ambas relacionadas con el ajedrez: el cálculo de los movimientos de un caballo en un teclado de móvil y el problema de las n-torres.

# El problema de los caballos

Este problema trata de mover un caballo de ajedrez por un tablero determinado y calcular de cuantas formas se puede mover el caballo dependiendo del número de movimientos que pudiera hacer.

Para los casos de 1 y 2 movimientos creamos un programa en python que es el siguiente:
```
list_1 = [6,8]
list_2 = [7,9]
list_3 = [4,8]
list_4 = [3,9,0]
list_6 = [1,7,0]
list_7 = [2,6]
list_8 = [1,3]
list_9 = [2,4]
list_0 = [4,6]
dicc = [list_0, list_1, list_2, list_3, list_4, list_6, list_7, list_8, list_9]
def movimientos(n):
    p = 0
    for i in range(len(dicc)):
        k = i
        if n == 1:
                p = p + len(dicc[i])
        elif n == 2:
            for j in range(len(dicc[i])):
                m = 0
                while m < n-1:
                    if dicc[k][j] == 1:
                        k = 1
                    elif dicc[k][j] == 2:
                        k = 2
                    elif dicc[k][j] == 3:
                        k = 3
                    elif dicc[k][j] == 4:
                        k = 4
                    elif dicc[k][j] == 6:
                        k = 5
                    elif dicc[k][j] == 7:
                        k = 6
                    elif dicc[k][j] == 8:
                        k = 7
                    elif dicc[k][j] == 9:
                        k = 8
                    elif dicc[k][j] == 0:
                        k = 0
                    m = m+1
                if m == n-1:
                    p = p + len(dicc[k])
                    k = i                    
    print(p)
        
movimientos(3)
```

Para más de 2 movimientos la forma que se nos ha ocurrido para resolverlo es, al igual que en el de 2, creando una lista de los movimientos que se puedene hacer desde cada numero, "m", y posteriormente creando una lista que vaya guardando la sucesión de numeros, "s", y de esta forma, al ser el tamaño de la lista igual al numero de movimientos sumariamos uno al contador de movimientos, "c", y eliminaríamos el ultimo valor de "s". Después veríamos cual es el siguiente numero en la lista "m"  del último valor de "s", y así sucesivamente hasta que ya se hayan usado todos los elementos de la lista de ese valor, y pasaríamos al anterior. Esto en resumidas cuentas es utilizar el algoritmo "backtracking", que consiste en ir siguiendo un camino, y al llegar al final, ya sea porque no se puede seguir, o en este caso, porque hemos realizado todos los movimientos, retroceder un paso y seguir.

# El problema de las n-torres

El problema de las n-torres se trata de buscar una forma de colocar n torres en un tablero de dimensiones n x n sin que estas tengan la posibilidad de comerse unas a otras. Para plantear dicho problema, suponemos que n puede tratarse de cualquier número natural mayor o igual que 4.

Una parte muy importante de este problema es entender el movimiento de la reina. La pieza en cuestión es la más versátil dentro del ajedrez, siendo capaz de desplazarse sin limitación de casillas de forma horizontal, vertical, derecha, izquierda y diagonal.

![tablero-marron-notacion (1)](https://user-images.githubusercontent.com/91720991/189424786-e39c9a33-f8ba-4b27-8933-4fae6e1c7806.png)

Queremos crear un algoritmo que nos ayude a colocar cada una de las reinas en una posición libre de las demas. Para ello, primero colocamos las reinas a la izquierda del tablero.

![Screenshot_20220909-204850_Gallery](https://user-images.githubusercontent.com/91720991/189433627-66e70b4c-4f5b-40ee-85a9-67556473f127.jpg)


La idea sería crear una función que coloque cada una de las reinas en una posición libre. Estala empezaremos aplicando en la torre de la segunda fila, ignorando las torres de filas menores dado que todavía no habrían sido añadidas. 

![Screenshot_20220909-204845_Gallery](https://user-images.githubusercontent.com/91720991/189433656-b758cd1f-f156-4651-b4a9-3367972e0278.jpg)


Así, se añadirá una torre por fila, moviendo una de las superiores si no se puede añadir más, hasta que haya 8 torres.

El código elaborado es el siguiente:

![Screenshot_20220909-204844_Gallery](https://user-images.githubusercontent.com/91720991/189433675-82099c46-f9ec-4084-92a6-f04cafb2b23f.jpg)



La imagen superior es un ejemplo de como quedaría en un tablero 8x8, pero la función calcularía las posiciones teniendo como variable las dimensiones del tablero.


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

    n = int(input("Introduzca la dimension (n) del tablero: "))
    solucion = Reina(n)
    print(solucion.resultado())

