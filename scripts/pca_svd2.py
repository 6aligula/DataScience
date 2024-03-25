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
