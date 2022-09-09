# RETO_INICIAL

Colaboradores
· Gonzalo Martínez, Rubén Nogueras, Germán Llorente, Carlos Puigserver, Alex Muñoz, Pelayo Huertas, Miguiel González

El trabajo se divide en dos partes principales, ambas relacionadas con el ajedrez: el cálculo de los movimientos de un caballo en un teclado de móvil y el problema de las n-torres.

# El problema de las n-torres

El problema de las n-torres se trata de buscar una forma de colocar n torres en un tablero de dimensiones n x n sin que estas tengan la posibilidad de comerse unas a otras. Para plantear dicho problema, suponemos que n puede tratarse de cualquier número natural mayor o igual que 4.

Una parte muy importante de este problema es entender el movimiento de la reina. La pieza en cuestión es la más versátil dentro del ajedrez, siendo capaz de desplazarse sin limitación de casillas de forma horizontal, vertical, derecha, izquierda y diagonal.

![tablero-marron-notacion (1)](https://user-images.githubusercontent.com/91720991/189424786-e39c9a33-f8ba-4b27-8933-4fae6e1c7806.png)

Queremos crear un algoritmo que nos ayude a colocar cada una de las reinas en una posición libre de las demas. Para ello, primero colocamos las reinas a la izquierda del tablero.


