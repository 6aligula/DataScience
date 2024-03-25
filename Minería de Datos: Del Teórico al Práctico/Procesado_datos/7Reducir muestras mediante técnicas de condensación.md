![[Pasted image 20240323135511.png]]

Reducir muestras mediante técnicas de condensación es como simplificar un ramo de flores. Imagina que tienes un gran ramo y deseas conservar solo la esencia de su belleza para que quepa en un jarrón más pequeño. En lugar de tener muchas flores de la misma especie, eliges una representante de cada grupo que capte la esencia del conjunto.

En el contexto de los datos, las técnicas de condensación buscan reducir el número de muestras manteniendo intacta la información más importante. Si tienes un conjunto de datos muy grande, que es demasiado para procesar o que tarda mucho tiempo en analizarse, puedes buscar muestras similares (o puntos de datos cercanos) y reemplazar estos grupos con un punto central que los represente. Este punto central se llama centroide y es como una muestra promedio del grupo.

En problemas supervisados, es decir, aquellos en los que las muestras están etiquetadas con la clase correcta, también te asegurarías de que todas las muestras que se agrupen y se reemplacen por un centroide compartan la misma etiqueta. Esto garantiza que no estás mezclando información de diferentes clases.

La figura que mencionaste ilustra este concepto. En la imagen original, puedes ver grupos de datos distintos, cada uno de una clase diferente. Aplicando la técnica de condensación, estos grupos se simplifican a un solo punto por clase: su centroide. Es una forma muy efectiva de reducir la cantidad de datos, en este caso, aproximadamente en un 80 %, sin perder la capacidad de distinguir entre las clases. Es como pasar de un ramo grande a uno pequeño, donde cada flor restante es la más representativa de su tipo en el ramo original. 

Esta simplificación hace que los modelos sean más rápidos de construir y más fáciles de interpretar, sin una pérdida significativa de precisión. Es particularmente útil cuando las muestras adicionales no aportan información nueva y solo aumentan la carga computacional.