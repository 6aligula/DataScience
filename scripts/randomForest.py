from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Cargar los conjuntos de datos
accidents_df = pd.read_csv('/mnt/data/accident.CSV', encoding='latin1')
drugs_df = pd.read_csv('/mnt/data/drugs.csv', encoding='latin1')

# Visualizar las primeras filas para entender su estructura y contenido
accidents_preview = accidents_df.head()
drugs_preview = drugs_df.head()

(accidents_preview, drugs_preview)


# Seleccionar variables relevantes del primer conjunto de datos
accidents_selected = accidents_df[['ST_CASE', 'FATALS', 'DRUNK_DR', 'MAN_COLL', 'DAY_WEEK', 'LGT_COND', 'WEATHER']]

# Seleccionar variables relevantes del segundo conjunto de datos
# Nota: ST_CASE ya está incluido, así que solo necesitamos añadir DRUGRES
drugs_selected = drugs_df[['ST_CASE', 'DRUGRES']]

# Integrar los datos
# Aquí optaremos por una agregación de los resultados de las pruebas de drogas por caso, 
# ya que un accidente puede tener múltiples personas involucradas y por lo tanto múltiples registros en 'drugs.csv'
drugs_aggregated = drugs_selected.groupby('ST_CASE')['DRUGRES'].apply(list).reset_index()

# Unir los dos conjuntos de datos seleccionados
data_merged = pd.merge(accidents_selected, drugs_aggregated, on='ST_CASE', how='left')

# Visualizar las primeras filas del conjunto de datos integrado
data_merged.head()


# # Preparar el conjunto de datos para el modelado
# # Codificar las variables categóricas usando Label Encoder
# encoder = LabelEncoder()
# data_for_model = data_merged.copy()
# data_for_model['DRUGRES_CAT'] = encoder.fit_transform(data_for_model['DRUGRES_CAT'])
# data_for_model['LGT_COND_CAT'] = encoder.fit_transform(data_for_model['LGT_COND_CAT'])
# data_for_model['WEATHER_CAT'] = encoder.fit_transform(data_for_model['WEATHER_CAT'])

# # Definir la variable objetivo y las características
# X = data_for_model[['DRUNK_DR', 'MAN_COLL', 'DAY_WEEK', 'DRUGRES_CAT', 'LGT_COND_CAT', 'WEATHER_CAT']]
# y = data_for_model['FATALS'] > 1  # Clasificar como 1 si hay más de una fatalidad, 0 de lo contrario

# # Dividir el conjunto de datos en entrenamiento y prueba
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Construir y entrenar el modelo de Bosque Aleatorio
# rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_classifier.fit(X_train, y_train)

# # Predecir y evaluar el modelo
# y_pred = rf_classifier.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)

# # Importancia de las características
# feature_importances = rf_classifier.feature_importances_

# (accuracy, dict(zip(X.columns, feature_importances)))


# # Ajustar la función de clasificación con las nuevas indicaciones proporcionadas
# def clasificar_resultados_drugres_v3(lista_resultados):
#     # Convertir lista_resultados a una lista si no lo es (manejar NaN y otros casos no iterables)
#     if not isinstance(lista_resultados, list):
#         return "Desconocido"
    
#     # Clasificación basada en los nuevos criterios proporcionados
#     positivos = any(100 <= x <= 996 or x == 998 for x in lista_resultados)
#     desconocidos = any(x in [95, 997, 999] for x in lista_resultados)
    
#     if positivos:
#         return "Positivo"
#     elif desconocidos:
#         return "Desconocido"
#     else:
#         return "Negativo o No Probado"

# # Aplicar la función ajustada con las nuevas indicaciones al conjunto de datos
# data_merged['DRUGRES_CAT'] = data_merged['DRUGRES'].apply(clasificar_resultados_drugres_v3)

# # Visualizar las primeras filas para verificar la transformación con las nuevas indicaciones
# data_merged[['ST_CASE', 'DRUGRES', 'DRUGRES_CAT']].head()

