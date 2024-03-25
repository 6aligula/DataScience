La imagen muestra el concepto de "Feature hashing", también conocido como "Hashing de características". Te lo voy a explicar con una metáfora sencilla:

Imagina que tienes un armario con solo 4 perchas (Hash 1, Hash 2, Hash 3 y Hash 4) y un montón de abrigos de diferentes colores y estilos. Quieres organizar los abrigos de tal manera que puedas encontrarlos fácilmente, pero solo tienes esas 4 perchas para colgarlos. Así que decides un sistema en el que basas la decisión de en qué percha colgar cada abrigo en alguna característica del abrigo, como su color o estilo. Esto significa que abrigos diferentes podrían acabar colgados en la misma percha si coinciden en esa característica.

En el mundo de los datos, "Feature hashing" funciona de manera similar. Tienes un montón de datos (en este caso, productos) y una función de hashing que es como una regla que decide en qué percha (valor de hash) colgarás cada producto. No importa cuántos productos nuevos lleguen (como tu hipotético Producto 5), los organizas siempre en las mismas 4 categorías usando tu función de hashing.

Esto es útil porque no importa si tienes 10 productos o 10,000, siempre terminarán organizados en uno de los 4 valores de hash disponibles. Esto hace que la gestión de datos sea más eficiente y no necesitas reajustar tu sistema cada vez que llega un nuevo producto. Es especialmente útil para categorías con muchas opciones posibles, como tipos de productos en un sitio de comercio electrónico.

El problema potencial, como se menciona, son las colisiones. Siguiendo con la metáfora, si dos abrigos muy diferentes terminan en la misma percha, podrías confundirte y pensar que son más similares entre sí de lo que realmente son. En el hashing de características, esto significa que dos productos distintos podrían ser asignados al mismo valor de hash, lo que podría causar confusión en el modelo que usa esa información para aprender.


![[Pasted image 20240321100447.png]]

Ejemplo:
```python
from sklearn.feature_extraction import FeatureHasher

# Supongamos que tenemos una lista de frutas con sus respectivas cantidades
fruits = [
    {'fruit': 'apple', 'quantity': 10},
    {'fruit': 'pear', 'quantity': 20},
    {'fruit': 'banana', 'quantity': 5},
    {'fruit': 'orange', 'quantity': 8},
    {'fruit': 'lemon', 'quantity': 3}
]

# Creamos un FeatureHasher con 6 características (buckets)
# La cantidad de características es un parámetro que nosotros definimos.
# Seleccionar más características puede reducir la posibilidad de colisiones
hasher = FeatureHasher(n_features=6, input_type='dict')

# Aplicamos feature hashing a nuestra lista de frutas
fruits_hashed = hasher.transform(fruits)

# Convertimos el resultado a una matriz densa y la imprimimos
fruits_hashed.toarray()
```

salida del script:
```zsh
(anscombe_env) caligula@Vinicios-MacBook-Pro scripts % python featureHashing.py
[[  0.   0.   0.   0.   1. -10.]
 [  1.   0.   0.   0.   0. -20.]
 [  0.   0.   0.  -1.   0.  -5.]
 [  1.   0.   0.   0.   0.  -8.]]
 ```

## Después de añadir una fila mas:
```python
fruits = [
    {'fruit': 'apple', 'quantity': 10},
    {'fruit': 'pear', 'quantity': 20},
    {'fruit': 'banana', 'quantity': 5},
    {'fruit': 'orange', 'quantity': 8},
    {'fruit': 'lemon', 'quantity': 3}
]
```
Salida después de añadir la nueva fruta
```python
scripts % python featureHashing.py
[[  0.   0.   0.   0.   1. -10.]
 [  1.   0.   0.   0.   0. -20.]
 [  0.   0.   0.  -1.   0.  -5.]
 [  1.   0.   0.   0.   0.  -8.]
 [  0.   0.  -1.   0.   0.  -3.]]
 ```
 Como se puede apreciar la ultima fila tiene una representación vectorial diferente.