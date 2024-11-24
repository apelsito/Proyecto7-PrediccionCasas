# Información Sobre el Modelo 1

## 1. **Análisis Exploratorio Inicial (EDA)**
En esta etapa:
- Se exploraron las características del dataset inicial, evaluando estadísticas descriptivas y generando visualizaciones para entender la distribución de los datos.
- Se identificaron:
  - Valores atípicos.
  - Columnas con valores nulos que podrían afectar el análisis.
- Se analizaron correlaciones entre variables para encontrar patrones útiles.

---

## 2. **Gestión de Nulos**
- Se manejaron los valores nulos en las variables relevantes utilizando diferentes técnicas:
  - Para variables numéricas, se aplicaron imputaciones basadas en medias, medianas o modelos avanzados según el caso.
  - Las variables categóricas se completaron utilizando frecuencias relativas u otros métodos adaptados.
- Resultado: un dataset sin valores nulos, listo para el análisis.

---

## 3. **EDA Posterior a la Limpieza**
- Se repitió el análisis exploratorio sobre el dataset limpio.
- Validaciones clave:
  - Las imputaciones realizadas no introdujeron sesgos significativos.
  - Visualizaciones adicionales, como mapas de calor de correlaciones, ayudaron a confirmar relaciones entre variables.

---

## 4. **Codificación de Variables Categóricas**
- Las variables categóricas se transformaron en numéricas mediante:
  - **One-Hot Encoding**, generando columnas binarias para cada categoría.
- Se eliminaron las columnas originales para evitar redundancia.
- Resultado: un dataset completamente numérico, facilitando su uso en modelos de machine learning.

---

## 5. **Escalado de Variables**
- Se aplicó **RobustScaler** para escalar las variables numéricas, priorizando la preservación de los valores atípicos.
- Comparación de técnicas:
  - `MinMaxScaler`, `StandardScaler`, y otros fueron evaluados.
  - `RobustScaler` fue seleccionado debido a su manejo eficiente de outliers.
- Guardado del dataset escalado para el siguiente paso.

---

## 6. **Gestión de Outliers**
- Se identificaron valores atípicos utilizando:
  - Métodos univariados como IQR y Z-score.
  - Métodos multivariados como LOF (Local Outlier Factor) e Isolation Forest.
- Clasificación de datos en categorías según el nivel de probabilidad de ser un outlier:
  - "No es Outlier".
  - "Outlier Probable".
  - "Outlier Total".
- Estrategia:
  - Los valores categorizados como outliers se volvieron nulos.
  - Se aplicó imputación con Random Forest para rellenar los valores faltantes.
- Resultado: un dataset sin outliers extremos, preparado para el modelado.

---

## 7. **Modelado: Regresión Lineal**
- **División de datos**: Separamos el dataset en entrenamiento (70%) y prueba (30%).
- **Construcción del modelo**:
  - Regresión lineal simple para predecir precios.
  - Métricas evaluadas: R², MAE, y RMSE.
- **Visualizaciones**:
  - Gráficos de predicción vs. valores reales.
  - Residual plots para identificar errores sistemáticos.
- Conclusiones:
  - El modelo presentó limitaciones debido a la naturaleza no lineal de los datos.
  - Se observó sobreestimación en precios bajos y subestimación en precios altos.

---

## 8. **Modelado: Árboles de Decisión**
- Implementación inicial de un modelo no lineal:
  - Árbol de decisión sin ajustes.
- Evaluación:
  - Se compararon las métricas obtenidas con las de la regresión lineal.
  - Aunque el modelo capturó mejor ciertas relaciones no lineales, se observó un alto grado de overfitting.
  - Las predicciones sobre el conjunto de prueba mostraron baja generalización, indicando la necesidad de modelos más robustos.

---

## 9. **Decisión de Abandonar el Modelo**
- **Motivo principal**: El árbol de decisión presenta un sobreajuste excesivo.
  - Mientras que las métricas en el conjunto de entrenamiento son excelentes, los resultados en el conjunto de prueba son significativamente peores.
  - Este comportamiento sugiere que el modelo no puede generalizar correctamente.
- **Conclusión**: Los árboles de decisión simples no son adecuados para este problema debido a su tendencia al overfitting con datos complejos y no lineales.

---

## 10. **Próximos Pasos**
- Optimización de hiperparámetros para modelos más avanzados, como Random Forest o Gradient Boosting.
- Evaluación de métricas con validación cruzada para evitar problemas de generalización.
- Análisis de interpretabilidad para asegurar que el modelo sea útil para agentes inmobiliarios y clientes.
