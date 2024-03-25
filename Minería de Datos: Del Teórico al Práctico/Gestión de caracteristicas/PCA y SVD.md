Imagina que tienes una mesa llena de diversos objetos repartidos al azar: bolígrafos, libros, tazas de café, etc. Si te piden que describas cómo están organizados estos objetos desde donde estás parado, podrías empezar señalando dónde hay más concentración de objetos o qué tipo de objetos son más comunes. Pero si te subes a una escalera y miras la mesa desde arriba, podrías notar patrones que no eras capaz de ver desde el suelo, como que los bolígrafos tienden a agruparse cerca de los cuadernos.

PCA (Análisis de Componentes Principales) y SVD (Descomposición de Valores Singulares) son como subirte a esa escalera para ver tus datos desde una nueva perspectiva. Te permiten encontrar nuevas formas de organizar la información (componentes principales) que quizás no eras capaz de ver antes. Estas nuevas formas están mejor alineadas con cómo están distribuidos realmente tus datos. En lugar de mirar los datos en términos de sus características originales (como el color o tamaño de los objetos), PCA y SVD te muestran los datos en términos de sus patrones más fundamentales o importantes.

Por ejemplo, en vez de describir cada objeto por su color, tamaño y peso, podrías descubrir que lo más importante para agruparlos es cuánto se usan (muchos bolígrafos cerca de cuadernos podrían indicar una zona de estudio) y su tamaño (objetos grandes como libros y tazas en un lado, objetos pequeños como bolígrafos en otro). Estos serían tus nuevos componentes principales.

Sin embargo, hay un desafío: aunque estas nuevas perspectivas (componentes principales) te dan una manera mucho más eficiente de entender y clasificar tus datos (porque capturan lo más importante sobre cómo están organizados), puede ser difícil explicar qué representa exactamente cada uno de estos nuevos componentes en términos del mundo real. Es como si supieras que desde tu escalera ves mejor la mesa, pero no siempre puedes explicar fácilmente por qué ciertos objetos tienden a estar juntos, solo sabes que este nuevo punto de vista te da una mejor visión general.

Estas técnicas reorganizan y condensan la información contenida en el conjunto de datos original de una manera más eficiente.

Para ponerlo en términos más claros, imagina que tienes un conjunto de datos multidimensional representado en un espacio de muchas dimensiones. Lo que PCA y SVD hacen es:

1. **Identificar las direcciones (o dimensiones) más importantes** en ese espacio, donde "importancia" se mide por la cantidad de variabilidad o dispersión de los datos a lo largo de esas direcciones.
    
2. **Proyectar los datos originales** a estas nuevas direcciones. Esto significa que estamos calculando cómo se verían los datos si solo miráramos las sombras que proyectan cuando la luz brilla a lo largo de estas direcciones de "mayor importancia".
    
3. **Seleccionar las principales direcciones** (componentes principales en PCA, y vectores singulares en SVD) que capturan la mayor parte de la variabilidad. Al hacerlo, podemos reducir el número de dimensiones necesarias para representar nuestros datos sin perder mucha información.

Tanto el Análisis de Componentes Principales (PCA) como la Descomposición de Valores Singulares (SVD) son técnicas de reducción de dimensionalidad muy utilizadas en estadística y aprendizaje automático. Ambas metodologías transforman el conjunto original de datos a un nuevo espacio de características, pero lo hacen de manera que las nuevas características (o componentes) sean independientes unas de otras. Esta independencia se refiere a que los componentes principales capturan distintas porciones de la varianza (información) de los datos, sin solaparse entre ellos.

### PCA (Análisis de Componentes Principales)

- **Objetivo**: Identificar las "direcciones" (componentes principales) a lo largo de las cuales los datos varían más.
- **Cómo funciona**: PCA busca direcciones en el espacio de datos donde hay mayor variabilidad. Los primeros componentes principales capturan la mayor parte de la variabilidad en los datos, y cada componente subsiguiente tiene la máxima varianza posible bajo la restricción de que sea ortogonal a los componentes anteriores.
- **Uso**: Reducción de dimensionalidad, visualización de datos, filtrado de ruido, y muchas otras aplicaciones en ciencia de datos y aprendizaje automático.

### SVD (Descomposición de Valores Singulares)

- **Objetivo**: Descomponer una matriz en tres matrices constituyentes, revelando las propiedades algebraicas de la matriz original.
- **Cómo funciona**: Dada una matriz \(A\), SVD la descompone en tres matrices \(U\), \(\Sigma\), y \(V^*\) tal que \(A = U\Sigma V^*\). Las columnas de \(U\) y \(V\) son vectores ortogonales, y \(\Sigma\) es una matriz diagonal con los valores singulares.
- **Uso**: Similar a PCA, se usa para reducción de dimensionalidad, además de ser una técnica fundamental en el procesamiento de señales, sistemas de recomendación, y más.

Ambas técnicas son poderosas para simplificar los conjuntos de datos al reducir el número de variables a considerar, identificando las más informativas. Al hacer esto, se puede mejorar significativamente la eficiencia de los algoritmos de aprendizaje automático, especialmente en conjuntos de datos de alta dimensionalidad.

**Incorporación de Componentes Principales en el Conjunto de Datos Original**

Al aplicar PCA, se suele seleccionar un número de componentes principales que, juntos, explican una gran parte de la variabilidad total de los datos (por ejemplo, más del 90%). Estos componentes seleccionados se pueden usar como nuevas características para entrenar modelos de clasificación o regresión, con la ventaja de trabajar en un espacio de dimensionalidad reducida.

**Interpretabilidad**

Uno de los principales desafíos de usar PCA o SVD es la interpretabilidad de los componentes resultantes. Dado que los componentes principales son combinaciones lineales de las características originales, puede ser difícil atribuir un significado concreto a cada componente. Esto contrasta con el trabajo en el espacio de características original, donde cada variable puede tener un significado específico y comprensible. A pesar de esta complejidad, las ganancias en términos de simplificación de los datos, mejoramiento del rendimiento de los modelos, y la capacidad de identificar estructuras subyacentes en los datos hacen que estas técnicas sean herramientas valiosas en el análisis de datos. ejemplo : [[Ejemplo de PCA y SVD]]