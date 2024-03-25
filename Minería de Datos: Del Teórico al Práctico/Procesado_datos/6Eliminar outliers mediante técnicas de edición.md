La idea de eliminar outliers mediante técnicas de edición es como filtrar los errores antes de que arruinen el resultado de una tarea importante. Imagina que estás pintando una imagen con una plantilla; si hay manchas fuera de los bordes esperados, no querrías que formaran parte de la imagen final. De manera similar, en la minería de datos, queremos asegurarnos de que las anomalías no desvíen nuestros modelos de sus verdaderas predicciones.

Las muestras que no se ajustan al patrón general, conocidas como outliers, pueden ser errores de captura de datos, errores humanos al ingresar información, o incluso problemas con los sensores que recogen los datos. Es crucial detectar y eliminar estos outliers porque pueden llevar a conclusiones incorrectas.

Tomemos por ejemplo un conjunto de datos donde cada punto representa una medida en un estudio. La mayoría de los puntos podrían agruparse juntos siguiendo un patrón, pero puede haber uno o dos que estén alejados del grupo. Estos puntos pueden distorsionar la interpretación de los datos, como en el caso de una regresión lineal donde la línea intenta ajustarse a todos los puntos, incluidos los outliers, lo que resulta en una predicción inexacta.

La técnica de edición de Wilson, que mencionaste, es como revisar cada punto individualmente para ver si encaja con el patrón general. Para cada muestra, temporalmente la eliminamos del conjunto de datos y construimos un modelo sin ella. Luego, usamos ese modelo para predecir la clase de la muestra eliminada. Si la predicción coincide con su clase real, la muestra probablemente es legítima y la devolvemos al conjunto. Si no coincide, es probable que la muestra sea un outlier y la descartamos permanentemente.

En tus ejemplos, los puntos que son significativamente diferentes de los demás son identificados y eliminados para que el modelo que creamos (como la línea de regresión) refleje de manera más precisa la relación real entre los datos. Al eliminar estos puntos atípicos, nos aseguramos de que el modelo esté influenciado únicamente por los datos representativos, mejorando así su calidad y precisión.
![[Pasted image 20240323134759.png]]



![[Pasted image 20240323134810.png]]
