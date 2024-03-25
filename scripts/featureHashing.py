from sklearn.feature_extraction import FeatureHasher

# Supongamos que tenemos una lista de frutas con sus respectivas cantidades
fruits = [
    {'fruit': 'apple', 'quantity': 10},
    {'fruit': 'pear', 'quantity': 20},
    {'fruit': 'banana', 'quantity': 5},
    {'fruit': 'orange', 'quantity': 8},
    {'fruit': 'lemon', 'quantity': 3},
    {'fruit': 'apple', 'quantity': 40},
]

# Creamos un FeatureHasher con 6 características (buckets)
# La cantidad de características es un parámetro que nosotros definimos.
# Seleccionar más características puede reducir la posibilidad de colisiones
hasher = FeatureHasher(n_features=6, input_type='dict')

# Aplicamos feature hashing a nuestra lista de frutas
fruits_hashed = hasher.transform(fruits)

# Convertimos el resultado a una matriz densa y la imprimimos
print(fruits_hashed.toarray())
