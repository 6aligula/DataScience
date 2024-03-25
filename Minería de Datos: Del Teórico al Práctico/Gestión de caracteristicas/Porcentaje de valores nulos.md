La gestión de valores nulos es un paso crucial en la preparación de datos para el análisis y la modelización. Estos son algunos enfoques comunes:

1. **Sustituir por la media**: Se utiliza en distribuciones simétricas, cuando el valor medio es una buena representación del centro de los datos.
2. **Sustituir por la mediana**: Es preferible en distribuciones sesgadas, donde los valores atípicos pueden distorsionar la media.
3. **Sustituir por valores aleatorios**: Esto puede mantener la distribución original de los datos, pero no añade información real.
4. **Sustituir por cero**: Solo es apropiado en ciertos contextos donde cero tiene un significado dentro del dominio del problema.
5. **Eliminar filas afectadas**: Es una opción si los valores nulos son pocos y se considera que su ausencia no afectará la calidad general del conjunto de datos.

En cuanto a la eliminación de características en función de su porcentaje de valores nulos, este enfoque estratégico permite:

- **Descartar características con más del 95% de valores nulos**: Se presume que estas características tienen poca o ninguna información útil debido a su alto grado de ausencia de datos.
- **No rellenar valores nulos cuando representan entre el 50% y el 95%**: Aquí se entiende que la cantidad de valores nulos es tan significativa que cualquier método de imputación podría sesgar fuertemente la característica.
- **Rellenar valores nulos si representan menos del 50%**: Esto se hace bajo la suposición de que la característica aún puede ser valiosa y que los métodos de imputación no sesgarán excesivamente la distribución de los datos.

Esta estrategia de gestión de características basada en el porcentaje de valores nulos ofrece un enfoque diferenciado que equilibra entre mantener la mayor cantidad de datos útiles y evitar introducir sesgos mediante la imputación. Como en todo en la ingeniería de datos y de software, se busca un equilibrio entre la integridad de los datos y la practicidad del enfoque, siempre con el objetivo de construir modelos robustos y fiables.