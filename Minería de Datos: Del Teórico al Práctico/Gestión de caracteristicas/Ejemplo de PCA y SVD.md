```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.utils.extmath import randomized_svd
import matplotlib.pyplot as plt

# Generar datos sintéticos
np.random.seed(0) # Para reproducibilidad
X = np.dot(np.random.rand(2, 2), np.random.randn(2, 200)).T

# Aplicar PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Aplicar SVD
U, Sigma, VT = randomized_svd(X, n_components=2)

# Transformar los datos usando SVD para comparar con PCA
X_svd = np.dot(U, np.diag(Sigma))

# Visualizar los datos originales
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(X[:, 0], X[:, 1], alpha=0.7)
plt.title('Datos Originales')
plt.axis('equal')

# Visualizar los datos transformados con PCA
plt.subplot(1, 3, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7)
plt.title('Trasformación PCA')
plt.axis('equal')

# Visualizar los datos transformados con SVD
plt.subplot(1, 3, 3)
plt.scatter(X_svd[:, 0], X_svd[:, 1], alpha=0.7)
plt.title('Transformación SVD')
plt.axis('equal')

plt.show()

```
resultado:
![[Pasted image 20240319145359.png]]
Explicación:
Este código realiza lo siguiente:

1. **Generación de datos sintéticos**: Creamos un conjunto de datos de 200 puntos en 2D que tienen una cierta correlación lineal.
2. **Aplicación de PCA**: Usamos PCA para identificar las direcciones de máxima varianza y transformamos los datos a este nuevo espacio.
3. **Aplicación de SVD**: Descomponemos la matriz de datos original utilizando SVD y transformamos los datos basándonos en esta descomposición.
4. **Visualización**: Mostramos los datos originales, los datos transformados con PCA y con SVD, para comparar cómo cada método afecta la distribución de los datos.

Ambos, PCA y SVD, revelarán patrones similares en los datos transformados, destacando las direcciones de máxima varianza. La principal diferencia conceptual entre ellos es que SVD es una técnica más general que puede aplicarse a cualquier matriz, mientras que PCA está específicamente diseñado para analizar la varianza en un conjunto de datos.

### Segundo ejemplo de demostración:
```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.utils.extmath import randomized_svd
import matplotlib.pyplot as plt

# Vamos a generar un conjunto de datos más complejo que ilustre mejor la capacidad de PCA y SVD.

np.random.seed(0) # Para reproducibilidad

# Generamos datos sintéticos con una relación más compleja

# X1 son valores entre 0 y 10 con un tamaño de 50

X1 = np.random.uniform(0, 10, 50)

# X2 es una función cuadrática de X1 más algo de ruido

X2 = 0.5 * (X1 ** 2) - 2 * X1 + np.random.normal(0, 2, 50)

# Combinamos X1 y X2 en una única matriz de datos

X = np.vstack((X1, X2)).T

# Aplicar PCA

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

# Aplicar SVD

U, Sigma, VT = randomized_svd(X, n_components=2)

# Transformar los datos usando SVD para comparar con PCA

X_svd = np.dot(U, np.diag(Sigma))

# Visualizar los datos originales y transformados

plt.figure(figsize=(18, 6))

# Visualizar los datos originales

plt.subplot(1, 3, 1)
plt.scatter(X[:, 0], X[:, 1], alpha=0.7)
plt.title('Datos Originales')
plt.xlabel('X1')
plt.ylabel('X2')
plt.axis('equal')

# Visualizar los datos transformados con PCA

plt.subplot(1, 3, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7)
plt.title('Transformación PCA')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.axis('equal')

# Visualizar los datos transformados con SVD

plt.subplot(1, 3, 3)
plt.scatter(X_svd[:, 0], X_svd[:, 1], alpha=0.7)
plt.title('Transformación SVD')
plt.xlabel('Singular Value 1')
plt.ylabel('Singular Value 2')
plt.axis('equal')

# Mostrar los gráficos

plt.show()

# Imprimir los datos para inspeccionar
print("Original", X)
print("Después de PCA", X_pca)
print("Después de SVD", X_svd)
```

![[Pasted image 20240320134344.png]]
En la imagen que compartiste, podemos ver tres gráficos:

1. **Datos Originales**: El gráfico de la izquierda muestra tus datos en su espacio original, con la relación entre las variables `X1` y `X2`.

2. **Transformación PCA**: El gráfico central muestra los datos después de aplicar PCA. Notarás que el primer componente principal (Componente Principal 1) está alineado con la dirección de máxima varianza de los datos, y el segundo componente principal (Componente Principal 2) es ortogonal al primero.

3. **Transformación SVD**: El gráfico de la derecha muestra los datos después de aplicar SVD. Similar a PCA, el primer valor singular (Singular Value 1) representa la dirección de máxima varianza, y el segundo valor singular (Singular Value 2) es ortogonal al primero.

Ambas transformaciones, PCA y SVD, tienen el efecto de rotar los datos para alinearlos con las direcciones de mayor variabilidad. La primera dimensión captura la mayor parte de la variabilidad, y las dimensiones subsiguientes capturan la variabilidad restante de manera decreciente.

Lo que estos gráficos ilustran es la reducción de la dimensionalidad, donde los datos originales de mayor dimensionalidad se proyectan en un espacio de menor dimensionalidad con el intento de preservar la mayor cantidad de información posible (en este caso, la variabilidad de los datos). Si los datos originales tienen una estructura lineal fuerte, como parece ser el caso según el gráfico, las técnicas de reducción de dimensionalidad pueden hacer un trabajo excelente al capturar esta estructura y simplificar la representación de los datos sin perder características importantes. Esto se refleja en los datos transformados que muestran un claro patrón o tendencia incluso en el espacio de menor dimensionalidad.