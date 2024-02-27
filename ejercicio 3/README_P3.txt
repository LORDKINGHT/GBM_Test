Cálculo de Mínimo de Saltos

Este script de Python calcula el mínimo número de saltos necesarios para alcanzar o superar una distancia específica.

Funcionalidad

El script min_jump.py contiene una función llamada min_jump(x) que toma una distancia x como entrada y calcula el mínimo número de saltos necesarios para alcanzar o superar esa distancia. La función sigue la siguiente lógica:

1. Inicializa una variable cur para rastrear la posición actual y una variable jump para rastrear el tamaño del siguiente salto.
2. Entra en un bucle while que continúa hasta que la posición actual sea mayor o igual a la distancia x.
3. En cada iteración del bucle, la posición actual se incrementa en el tamaño del salto actual (jump), y el tamaño del siguiente salto se incrementa en 1.
4. Cuando la posición actual sea mayor o igual a x, el bucle se detiene.
5. Si la posición actual es exactamente x + 1, la función devuelve el tamaño del siguiente salto (jump), de lo contrario devuelve el tamaño del salto anterior (jump - 1).

Ejecución

Para ejecutar el script:

1. Asegúrate de tener Python instalado en tu sistema.
2. Descarga el archivo min_jump.py y guárdalo en tu directorio de trabajo.
3. Abre una terminal y navega hasta el directorio donde se encuentra el archivo.
4. Ejecuta el siguiente comando:

python min_jump.py

Resultado Esperado

El script imprimirá el mínimo número de saltos necesarios para alcanzar o superar la distancia en cada caso proporcionado.

Ejemplo de Uso

El script proporciona un ejemplo de uso con la lista de casos [1, 2, 3, 4, 5]. Para cada distancia en la lista, se calcula y muestra el mínimo número de saltos necesario.
