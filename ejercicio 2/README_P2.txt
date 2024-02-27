Formula 1

Este script de Python arroja el resultado de quien fue el ganador de cada una de las vueltas y el sistema de puntuacion.

Requisitos

1. Python 3.x
3. Importar Sys
2. Biblioteca estándar de Python

Funcionalidad

El Script recibe la cantidad de X veces que se quiera validar los resultados de uno o varios torneos, calcula posicion de cada participante para luego dependiendo de la tabla de puntajes muestra quien o quienes son los ganadores. El codigo finaliza cuando se le ingresa un 0 0.

La función realiza los siguientes pasos:

1. Convierte la palabra a minúsculas utilizando el método lower().
2. Elimina los espacios en blanco de la palabra utilizando el método replace(" ", "").
3. Compara la palabra original con su versión invertida para determinar si es un palíndromo.

Ejecución

Para ejecutar el script:

El script recibe 2 entradas, G y P, done G es el numero de premios y P la cantidad de pilotos.
Ej:
3 10 (Enter)

Posteriormente recibe por cada linea de entrada, la posicion en la que quedaron los participantes del G sub n.
Ej:
1 2 3 4 5 6 7 8 9 10 (Enter)
10 1 2 3 4 5 6 7 8 9 (Enter)
9 10 1 2 3 4 5 6 7 8 (Enter)

Posteriormente recibe a S, que significa cuantos sistemas de puntuaciones se van a utilizar y para cada sistema de puntuacion se debe sacara un ganador.
Ej:
2 (Enter)

Posteriormente se recibe la entrada K, que significa la cantidad de puntajes que se tiene para esa calificacion, aquellos que no sean incluidos se les asigna directamente 0.
Una vez se recibe K, recibimos los K sub n, que son  los puntajes para cada una de las posiciones.
Ej:
3 (Enter)
3 2 1 (Enter)
(Se recibe "Winner 3") 

3 (Enter )
5 4 2 (Enter)
(Se recibe "Winner 3") 

(Se repite el While se esperan otras 2 entradas, 0 0 para finalizar)


Resultado Esperado

El script imprimirá el ganador o ganadores de cada uno de los sistemas de puntuacion. En caso de ingresar mal un valor, saldra por un Catch diciendo "Invalid input".

Ejemplo de Uso

Se adjuntara un foto para ver como se ingresan los parametros por consola.