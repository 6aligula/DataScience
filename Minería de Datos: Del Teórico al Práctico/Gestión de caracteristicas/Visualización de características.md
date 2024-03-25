El cuarteto de Anscombe es un conjunto clásico de datos que ilustra la importancia de la visualización en el análisis de datos. Aunque cada grupo tiene las mismas propiedades estadísticas, cuando se visualizan gráficamente, muestran patrones muy diferentes. Este ejemplo demuestra que el análisis estadístico por sí solo puede ser engañoso sin el acompañamiento de la visualización de los datos, que puede revelar relaciones y características no aparentes solo con los números.

El cuarteto nos enseña que debemos mirar más allá de las estadísticas básicas para comprender verdaderamente los datos. Los patrones en los datos (lineal, parabólico, relación con valores extremos) solo son evidentes cuando los visualizamos. Estas diferencias pueden tener implicaciones significativas en la toma de decisiones basada en el análisis de datos. En términos de ingeniería de software, esto se alinea con la necesidad de hacer que el código sea no solo funcional sino también legible y comprensible para humanos. Así como visualizamos los datos para entenderlos mejor, escribimos código que otros pueden leer y comprender fácilmente.

El consejo de J.A. Baker subraya un punto esencial: a veces, lo más difícil es ver lo que está directamente frente a nosotros. Las visualizaciones son herramientas poderosas porque nos ayudan a ver lo que de otro modo podríamos pasar por alto, aunque no sean una panacea y deban ser complementadas con otras técnicas de análisis para obtener una comprensión completa de los datos. Esto es comparable a la revisión de código en la programación, donde otros pueden identificar problemas o mejoras que el autor original no vio, resaltando la importancia de las perspectivas frescas y de múltiples ojos en cualquier forma de análisis.

![[Pasted image 20240319124724.png]]


![[Pasted image 20240319124751.png]]

## Ecplicación
Claro, vamos paso a paso.

El cuarteto de Anscombe consiste en cuatro conjuntos de datos distintos que, cuando se analizan estadísticamente, presentan muchas propiedades numéricas similares. En particular, tienen la misma media y varianza tanto en `x` como en `y`, el mismo coeficiente de correlación entre `x` e `y`, y las líneas de regresión lineal también son idénticas.

Sin embargo, cuando visualizas estos conjuntos de datos, como se muestra en las Figuras 2 y 3 que enviaste, revelan comportamientos muy diferentes:

1. **Caso I**: Muestra lo que parecería ser una relación lineal clásica y simple entre `x` e `y`. Los puntos de datos parecen estar distribuidos uniformemente alrededor de la línea de regresión.

2. **Caso II**: Exhibe una relación curva (parabólica). Aunque los puntos no se alinean en una recta, si calculamos la línea de regresión lineal resultante utilizando métodos estadísticos básicos, obtenemos la misma ecuación que para el primer conjunto. Esto es engañoso, ya que la relación real entre las variables no es lineal.

3. **Caso III**: También muestra una relación lineal entre `x` e `y`, pero hay un valor atípico (outlier) que influye significativamente en la línea de regresión. Si se elimina este punto, la relación entre `x` e `y` podría ser muy diferente.

4. **Caso IV**: Presenta un caso aún más extremo en el que todos los puntos de `x` tienen el mismo valor, excepto uno. A pesar de esto, la correlación sigue siendo alta debido al punto de datos extremo que alinea todos los puntos a lo largo de la línea de regresión. Sin ese punto, no habría correlación aparente.

El mensaje central de este ejemplo es que las estadísticas descriptivas no son suficientes para capturar la verdadera naturaleza de los datos. La visualización es una herramienta crítica porque nos permite ver la estructura y las anomalías en los datos que no se capturan en un simple análisis numérico. En programación, esto se asemeja a realizar pruebas y revisiones del código para asegurarse de que realmente se comporta como se espera, en lugar de confiar solo en una revisión superficial. El cuarteto de Anscombe es una lección visual sobre por qué siempre debemos inspeccionar nuestros datos (y nuestro código) más de cerca, en busca de detalles que podrían pasarse por alto si nos basamos únicamente en resúmenes numéricos o estadísticos.

```python
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


```
