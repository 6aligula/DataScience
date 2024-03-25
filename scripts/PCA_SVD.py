import numpy as np
from sklearn.decomposition import PCA
from sklearn.utils.extmath import randomized_svd
import matplotlib.pyplot as plt

# Generar datos sintéticos
np.random.seed(0) # Para reproducibilidad
X = np.dot(np.random.rand(2, 2), np.random.randn(2, 50)).T
print(f"Original", X)

# Aplicar PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(f"Despues de PCA", X_pca)

# Aplicar SVD
U, Sigma, VT = randomized_svd(X, n_components=2)

# Transformar los datos usando SVD para comparar con PCA
X_svd = np.dot(U, np.diag(Sigma))
print(f"Despues de SVD", X_svd)

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
