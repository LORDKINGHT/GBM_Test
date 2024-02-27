Configuración de Clasificación de Clientes

Este script de Python realiza la clasificación de clientes en función de su frecuencia de compra y hábitos de gasto utilizando un modelo de red neuronal implementado con Keras.

Instrucciones de Instalación:

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las siguientes dependencias utilizando pip:

Uso del Script:

1. Descarga el archivo "data_customer_classification.xlsx" que contiene los datos de clientes.
2. Coloca el archivo "data_customer_classification.xlsx" en el mismo directorio que el script.
3. Ejecuta el script Python.

Funcionalidad:

El script realiza las siguientes operaciones:

1. Carga los datos de clientes desde el archivo Excel "data_customer_classification.xlsx" utilizando la biblioteca Pandas.
2. Agrupa los datos por 'customer_id' y calcula características como la frecuencia de compras, el gasto promedio y el máximo gasto por cliente.
3. Codifica las etiquetas de clasificación ('low', 'medium', 'high') utilizando LabelEncoder de scikit-learn.
4. Divide los datos en conjuntos de entrenamiento y prueba utilizando train_test_split de scikit-learn.
5. Escala los datos utilizando StandardScaler de scikit-learn.
6. Convierte las etiquetas de salida a codificación one-hot utilizando to_categorical de Keras.
7. Construye un modelo de red neuronal secuencial utilizando Keras con capas densas.
8. Compila y entrena el modelo utilizando el optimizador 'adam' y la función de pérdida 'categorical_crossentropy'.
9. Evalúa el modelo en el conjunto de prueba y muestra la precisión obtenida.
