Los valores ausentes en un conjunto de datos son como los espacios vacíos en un rompecabezas. Sabes que hay una pieza correcta para cada espacio, pero no tienes la pieza a mano. En el mundo de los datos, esto sucede cuando faltan valores en tus registros, y hay diferentes maneras de manejarlo:

1. **Ignorar el atributo:** Si casi todas las piezas de una sección del rompecabezas faltan, quizás decidas que esa parte del rompecabezas no es crucial y la dejas fuera. En los datos, si muchos valores de un atributo faltan, podrías decidir no usar ese atributo en tu modelo.

2. **Llenar los espacios vacíos:** Si solo faltan unas pocas piezas, podrías tratar de adivinar cómo se ve esa parte del rompecabezas y dibujarla tú mismo. En términos de datos, esto significa asignar valores a los que faltan, basándote en lo que sabes sobre los valores presentes. Por ejemplo, podrías llenar un valor ausente con el promedio de todos los valores conocidos para ese atributo.

3. **Descartar la muestra:** Si una sola pieza del rompecabezas está casi completamente ausente, es probable que la descartes por completo. Del mismo modo, si un registro en tu conjunto de datos tiene muchos valores ausentes, es posible que decidas no usar ese registro en absoluto.

La imputación es el proceso de llenar esos espacios vacíos en tus datos. Hay muchas maneras de hacerlo:

- **Valor fijo:** Puedes asignar un valor estándar, como 0 o el mínimo, a todos los valores ausentes. Pero como en el ejemplo del salario y los kilómetros que has mencionado, esto no siempre tiene sentido.
  
- **Promedios:** Una opción común es llenar los valores ausentes con el promedio (la media) de todos los valores conocidos para ese atributo.
  
- **Regresión:** O puedes ser más sofisticado y usar un modelo de regresión que prediga el valor ausente basándose en la relación entre ese atributo y otros.

Usando el conjunto de datos que proporcionaste como ejemplo, podríamos calcular la media del salario y los kilómetros y usar esos valores para llenar los espacios en blanco. O podríamos construir un modelo de regresión que use las edades, salarios, ventas y kilómetros de los comerciales que tienen datos completos para predecir los valores faltantes para los comerciales 3 y 5.

El mejor método depende del contexto de tus datos y tus objetivos. En la práctica, probarías varios métodos y elegirías el que mejor funcione para tu situación específica.
![[Pasted image 20240323140524.png]]