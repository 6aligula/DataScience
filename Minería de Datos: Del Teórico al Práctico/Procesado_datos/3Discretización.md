La discretización es como organizar los juguetes de una habitación en cajas según su tipo: algunos van en la caja de peluches, otros en la de coches de juguete, etc. De esta manera, en lugar de lidiar con cada juguete individualmente, solo necesitas considerar las cajas. Esto simplifica mucho la tarea de encontrar un juguete cuando lo necesitas, ya que solo tienes que elegir entre unas pocas categorías en lugar de entre todos los juguetes.

En el mundo de los datos, la discretización tiene beneficios similares:

1. **Reduce el coste computacional:** Es como tener menos tipos de juguetes para clasificar; hace que todo el proceso de análisis de datos sea más rápido y menos exigente porque hay menos valores únicos con los que trabajar.
   
2. **Acelera el aprendizaje:** Entrenar un modelo de datos es más rápido porque, al igual que es más rápido ordenar las cajas de juguetes que los juguetes individuales, es más rápido para el modelo aprender de categorías que de datos continuos.
   
3. **Ahorra espacio de almacenamiento:** Guardar información sobre las categorías (las cajas) en lugar de cada dato individual (cada juguete) requiere menos memoria.
   
4. **Reduce el tamaño del modelo resultante:** Al igual que es más manejable tener unas pocas cajas grandes que muchos juguetes pequeños esparcidos, trabajar con datos discretizados puede hacer que los modelos, como los árboles de decisión, sean más simples y compactos.
   
5. **Mejora la comprensión:** Es más fácil entender un resumen basado en categorías generales que tratar de hacer sentido de miles o millones de puntos de datos individuales.

Sin embargo, como cuando decides qué juguetes poner en qué caja, la discretización debe hacerse con cuidado para no perder información importante. Si haces las categorías demasiado amplias, podrías perder detalles cruciales, como mezclar puzzles con libros solo porque ambos se usan en una mesa. Esto podría hacer que los modelos de datos sean menos precisos o útiles, ya que pierden la capacidad de distinguir entre matices finos en los datos.

Por tanto, aunque discretizar puede hacer que el análisis de datos sea más eficiente y los modelos más fáciles de manejar y entender, es importante hacerlo de manera que preserve tanto como sea posible la utilidad y la precisión de los datos.

A continuación se describen tres métodos para discretizar.
[[Método de partición en intervalos de la misma amplitud]], [[Obtención de intervalos de discretización de igual frecuencia]], [[Método de partición basado en el algoritmo k-means]]