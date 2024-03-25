Exactamente, este texto es una continuación del concepto anterior y te muestra un ejemplo práctico con un conjunto de medios de transporte urbano. Aquí te lo explico de manera simple:

Imagina que tienes una lista de medios de transporte urbano: moto, bicicleta, patinete, monociclo y segway. Quieres organizar estos medios en tu computadora de manera que pueda entenderlos fácilmente. Para hacerlo, puedes codificarlos, es decir, representarlos, de tres maneras diferentes:

1. **Decimal**: Es la forma más directa. Simplemente asignas un número único a cada medio de transporte, empezando por 0. Así, moto sería 0, bicicleta 1, y así sucesivamente. Esta es una manera sencilla, pero como mencionamos antes, puede llevar a confusiones ya que la computadora podría interpretar estos números como una jerarquía o como valores que se pueden sumar, restar, etc.

2. **Binario**: Esta codificación usa números en sistema binario (compuestos solo por ceros y unos) para representar cada medio de transporte. Aquí, cada número binario es único para cada medio de transporte. Por ejemplo, moto sería 000, bicicleta 001, etc. Esto es un poco más complejo que los números decimales, pero ayuda a que la computadora maneje la información de manera más eficiente en algunos casos.

3. **One-hot**: Este método es bastante diferente. En lugar de asignar un solo número a cada medio de transporte, creas un vector (una fila de números) para cada uno. La longitud de este vector es igual al número total de medios de transporte. En cada vector, pones un 1 en la posición que corresponde al medio de transporte y 0s en todas las demás. Por ejemplo, para la moto, que es el primer elemento, tendrías un 1 al principio y luego solo 0s. Esta codificación es muy útil porque evita cualquier malentendido sobre la jerarquía o la relación numérica entre los medios de transporte; cada uno es simplemente diferente, sin ser más o menos que los demás.

Las codificaciones binaria y one-hot son especialmente útiles para algoritmos complejos, como las redes neuronales, porque ayudan a estas máquinas a "entender" los datos de una manera que evita confusiones sobre la importancia relativa de cada categoría.

![[Screenshot 2024-03-21 at 11.49.28.png]]