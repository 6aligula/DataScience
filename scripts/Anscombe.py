import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# Definimos los datos manualmente para el cuarteto de Anscombe
anscombe_data = {
    'I': {'x': [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
          'y': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]},
    'II': {'x': [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
           'y': [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]},
    'III': {'x': [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
            'y': [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]},
    'IV': {'x': [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0],
           'y': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]}
}

# Creamos la figura y los ejes para la visualización
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), sharex=True, sharey=True)
axes = axes.flatten()  # Convierte el arreglo 2D de ejes en un arreglo 1D para un acceso más fácil

# Recorremos cada conjunto de datos para crear las gráficas correspondientes
for i, (key, value) in enumerate(anscombe_data.items()):
    ax = axes[i]
    x = value['x']
    y = value['y']
    ax.scatter(x, y)

# Continuamos desde el código proporcionado
axes = axes.flatten()  # Convertimos la matriz 2D de ejes en una matriz 1D para un acceso más fácil

# Calculamos y trazamos las regresiones lineales
for i, (dataset, data) in enumerate(anscombe_data.items()):
    ax = axes[i]
    x = data['x']
    y = data['y']
    ax.scatter(x, y, label=f'Dataset {dataset}')

    # Ajustamos una regresión lineal a los datos
    m, b = np.polyfit(x, y, 1)
    ax.plot(x, [m*xi + b for xi in x], color='blue')
    
    # Configuramos los títulos y etiquetas
    ax.set_title(f'Dataset {dataset}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

# Ajustamos el layout
plt.tight_layout()

# Mostramos la figura
plt.show()
