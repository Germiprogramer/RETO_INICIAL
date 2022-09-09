# RETO_INICIAL

Colaboradores
· Gonzalo Martínez, Rubén Nogueras, Germán Llorente, Carlos Puigserver, Alex Muñoz, Pelayo Huertas, Miguiel González

El trabajo se divide en dos partes principales, ambas relacionadas con el ajedrez: el cálculo de los movimientos de un caballo en un teclado de móvil y el problema de las n-torres.

# El problema de las n-torres

El problema de las n-torres se trata de buscar una forma de colocar n torres en un tablero de dimensiones n x n sin que estas tengan la posibilidad de comerse unas a otras. Para plantear dicho problema, suponemos que n puede tratarse de cualquier número natural mayor o igual que 4.

Una parte muy importante de este problema es entender el movimiento de la reina. La pieza en cuestión es la más versátil dentro del ajedrez, siendo capaz de desplazarse sin limitación de casillas de forma horizontal, vertical, derecha, izquierda y diagonal.

![tablero-marron-notacion (1)](https://user-images.githubusercontent.com/91720991/189424786-e39c9a33-f8ba-4b27-8933-4fae6e1c7806.png)

Queremos crear un algoritmo que nos ayude a colocar cada una de las reinas en una posición libre de las demas. Para ello, primero colocamos las reinas a la izquierda del tablero.

![Screenshot_20220909-204850_Gallery](https://user-images.githubusercontent.com/91720991/189425131-ea98d4d4-3c0b-43e3-9061-f09bf1e58911.jpg)

La idea sería crear una función que coloque cada una de las reinas en una posición libre. Estala empezaremos aplicando en la torre de la segunda fila, ignorando las torres de filas menores dado que todavía no habrían sido añadidas. 

![Screenshot_20220909-204845_Gallery](https://user-images.githubusercontent.com/91720991/189425152-447e9dc8-e9d2-4020-a40a-c12db6ae568a.jpg)

Así, se añadirá una torre por fila, moviendo una de las superiores si no se puede añadir más, hasta que haya 8 torres.

![Screenshot_20220909-204844_Gallery](https://user-images.githubusercontent.com/91720991/189425171-d64a6a7f-afe9-45a3-bf4f-7af591be30b1.jpg)

La imagen superior es un ejemplo de como quedaría en un tablero 8x8, pero la función calcularía las posiciones teniendo como variable las dimensiones del tablero.
