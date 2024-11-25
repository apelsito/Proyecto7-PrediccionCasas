# Análisis y Modelado: Predicción de Precios de Casas 🏠

# Descripción del Proyecto 💡

Este proyecto tiene como objetivo desarrollar un modelo predictivo capaz de estimar el precio de propiedades inmobiliarias en Madrid, utilizando un conjunto de datos real con 40 columnas. Estas columnas incluyen información clave sobre las propiedades, como su tamaño, ubicación, número de habitaciones, tipo de propiedad y más. 

El propósito principal es ofrecer una herramienta útil para agentes inmobiliarios, compradores y vendedores, que permita tomar decisiones más informadas basadas en datos.

## 🎯 Objetivo
1. **Carga y Exploración de Datos**:
   - Identificar patrones en los datos.
   - Detectar valores atípicos y posibles inconsistencias.

2. **Preprocesamiento**:
   - Limpieza y preparación de datos.
   - Codificación de variables categóricas.
   - Escalado de variables numéricas.
   - Gestión de valores nulos y outliers.

3. **Modelado**:
   - Entrenamiento de múltiples modelos de Machine Learning.
   - Evaluación de su desempeño utilizando métricas como RMSE y R².

4. **Visualización**:
   - Mostrar gráficamente la importancia de las variables.
   - Analizar los errores y predicciones del modelo.

5. **Optimización**:
   - Ajustar hiperparámetros para maximizar la precisión del modelo.

## Estructura del Proyecto 🗂️

```bash
Proyecto7-PrediccionCasas/
├── datos/                      # Archivos de datos CSV y PKL para el proyecto.
│   ├── lista_opciones/         # Lista de opciones para los menús de streamlit.
│   ├── modelos-encoders/       # Lista de PKLs de los modelos y encoders ya entrenados.
│
├── jupyter_notebooks/          # Notebooks de Jupyter con los modelos probados.
│   ├── Modelo X/               # Carpeta del modelo
│   │   ├── 00_Sobre_El_Modelo.md
│   │   ├── 01_eda_inicial.ipynb
│   │   ├── 02_gestion_nulos.ipynb
│   │   ├── 03_eda_sin_nulos.ipynb
│   │   ├── 04_encoding.ipynb
│   │   ├── 05_feature_scaling.ipynb
│   │   ├── 06_gestion_outliers.ipynb
│   │   ├── 07_regresion_lineal.ipynb
│   │   ├── 08_decision_tree.ipynb
│   │   ├── 09_gradient_boosting.ipynb
│   │   ├── 10_XGBoost.ipynb
│ 
├── src/                        # Archivos .py para funciones auxiliares del proyecto.
│
├── streamlit/                  # Web para realizar predicciones de forma rápida y bonita
│    ├── main.py                # Configuración Web
│    ├── prueba_modelo.ipynb 
│
└── README.md                   # Descripción del proyecto, instrucciones de instalación y uso.
```
# Instalación y Requisitos 🛠️

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.x** 🐍
- **Jupyter Notebook** 📓 para ejecutar y visualizar los análisis de datos
- **Bibliotecas de Python**:
    - [pandas](https://pandas.pydata.org/docs/) para manipulación y análisis de datos 🧹
    - [numpy](https://numpy.org/doc/stable/) para cálculos numéricos y manejo de matrices 🔢
    - [matplotlib](https://matplotlib.org/stable/index.html) para crear gráficos básicos 📊
    - [seaborn](https://seaborn.pydata.org/) para visualizaciones estadísticas avanzadas 📈
    - [tqdm](https://tqdm.github.io/) para mostrar barras de progreso en procesos largos ⏳
    - [xgboost](https://xgboost.readthedocs.io/) para la implementación de modelos basados en Gradient Boosting 🌟
    - [scikit-learn](https://scikit-learn.org/stable/) para modelado predictivo y preprocesamiento, incluyendo:
        - `LinearRegression`, `DecisionTreeRegressor`, `RandomForestRegressor`, `GradientBoostingRegressor`, y `XGBRegressor` para tareas de regresión
        - `train_test_split`, `GridSearchCV`, `KFold`, `LeaveOneOut` y `cross_val_score` para partición de datos y validación de modelos
        - `StandardScaler` para el escalado de variables
        - Métricas como `r2_score`, `mean_squared_error`, `mean_absolute_error` para evaluar los modelos
    - [pickle](https://docs.python.org/3/library/pickle.html) para serializar y cargar modelos y objetos 🛠️

## Configuración Adicional

- Configura `pd.options.display.float_format` para un formato más claro en los valores flotantes.
- Añade rutas personalizadas al sistema usando `sys.path.append` para facilitar el acceso a los módulos personalizados del proyecto.

## Instalación 🛠️

1. Clona este repositorio para visualizarlo en vscode:
```bash
git clone https://github.com/apelsito/Proyecto7-PrediccionCasas.git
cd Proyecto7-PrediccionCasas
```
# Resumen del Proyecto: Predicción de Precios de Casas 🏠

## Fase 1: Análisis Exploratorio Inicial (EDA) 🔍

### Pasos:
1. **Carga de Librerías y Configuración**:
   - Importación de librerías para análisis (pandas, numpy) y visualización (matplotlib, seaborn).
   - Configuración para visualizar más columnas en los DataFrames.

2. **Exploración de Datos**:
   - Carga inicial del dataset.
   - Exploración de estadísticas descriptivas para identificar variables relevantes y anomalías.

3. **Visualización Inicial**:
   - Gráficos de distribución y correlaciones para observar relaciones entre variables y patrones.

### Observaciones 📌
- Se detectaron algunas columnas con posibles valores atípicos.
- Algunas variables tenían nombres poco descriptivos, lo que requerirá limpieza futura.

---

## Fase 2: Gestión de Valores Nulos 🧹

### Pasos:
1. **Identificación de Valores Nulos**:
   - Revisión de las columnas con valores nulos y su porcentaje sobre el total.
   
2. **Imputación de Nulos**:
   - Uso de estrategias avanzadas como `SimpleImputer`, `IterativeImputer` y `KNNImputer`.
   - Validación de las imputaciones comparando estadísticas antes y después.

### Observaciones 📌
- Las columnas `price`, `size`, y `rooms` fueron tratadas con imputaciones adecuadas basadas en distribuciones observadas.
- Algunas imputaciones requerirán validación adicional en la siguiente fase.

---

## Fase 3: EDA Sin Valores Nulos 🔍

### Pasos:
1. **Reanálisis de las Variables**:
   - Exploración de estadísticas descriptivas post-imputación.
   
2. **Visualización**:
   - Gráficos para observar cómo se ajustaron las distribuciones tras el manejo de nulos.

### Observaciones 📌
- La imputación de nulos corrigió varios valores extremos, mejorando las distribuciones de las variables.

---

## Fase 4: Codificación de Variables (Encoding) 🧮

### Pasos:
1. **Identificación de Variables Categóricas**:
   - Clasificación de las columnas categóricas según el tipo de codificación requerida (OneHot, Target, Ordinal).

2. **Aplicación de Codificaciones**:
   - Uso de `OneHotEncoder` para variables con muchas categorías.
   - Aplicación de `TargetEncoder` para las que presentaban relación con la variable respuesta.

### Observaciones 📌
- La codificación de variables categóricas aumentó la dimensionalidad, pero mejorará el modelado.

---

## Fase 5: Escalado de Características (Feature Scaling) 📏

### Pasos:
1. **Selección de Variables Numéricas**:
   - Filtrado de columnas numéricas para el escalado.

2. **Aplicación de Escaladores**:
   - Uso de `StandardScaler`, `MinMaxScaler` y `RobustScaler` según las características de los datos.

### Observaciones 📌
- El escalado uniformizó los valores, facilitando el entrenamiento de modelos de regresión.

---

## Fase 6: Gestión de Outliers 🚫

### Pasos:
1. **Identificación de Outliers**:
   - Uso de métodos como IQR y Z-Score para detectar valores atípicos.

2. **Tratamiento de Outliers**:
   - Imputación o eliminación según su impacto en las distribuciones y relaciones.

### Observaciones 📌
- La eliminación de outliers mejoró significativamente la calidad del dataset.

---

## Fase 7: Regresión Lineal 📈

### Pasos:
1. **Entrenamiento del Modelo**:
   - División del dataset en conjuntos de entrenamiento y prueba.
   - Ajuste de un modelo de regresión lineal.

2. **Evaluación del Modelo**:
   - Métricas como R², MAE, y RMSE para validar la precisión del modelo.

### Observaciones 📌
- El modelo tuvo un desempeño básico, indicando que las relaciones lineales no capturan toda la complejidad de los datos.

---

## Fase 8: Árboles de Decisión 🌳

### Pasos:
1. **Entrenamiento del Modelo**:
   - Ajuste de un modelo de Árbol de Decisión para capturar relaciones no lineales.

2. **Evaluación del Modelo**:
   - Métricas similares a la regresión lineal, con mejoras significativas en el ajuste.

### Observaciones 📌
- El Árbol de Decisión mostró mayor precisión en comparación con la regresión lineal, pero aún con limitaciones en datos complejos.

---

## Fase 9: Gradient Boosting 🚀

### Pasos:
1. **Implementación de Gradient Boosting**:
   - Uso de `GradientBoostingRegressor` para mejorar la capacidad predictiva del modelo.

2. **Tuning de Hiperparámetros**:
   - Ajuste de hiperparámetros usando `GridSearchCV`.

### Observaciones 📌
- Gradient Boosting superó significativamente a los modelos previos, mostrando menor error de predicción.

---

## Fase 10: XGBoost 🌟

### Pasos:
1. **Entrenamiento de XGBoost**:
   - Uso de `XGBRegressor` para aprovechar la capacidad de manejo de datos complejos y gran volumen.

2. **Optimización del Modelo**:
   - Ajuste de parámetros como `learning_rate`, `max_depth` y `n_estimators`.

### Observaciones 📌
- XGBoost fue el modelo más efectivo, con el mejor desempeño en términos de R² y RMSE.

---
# 📊 Análisis de las Gráficas 📊
## 1. 📈 Evolución Anual del Precio Promedio por Servicio (2019-2022)

![Evolución Anual del Precio Promedio por Servicio](src/01_graficas/01_EvolucionAnualPorServicio.png)

### Observaciones:
- **Agua**💧: El precio promedio del agua se mantuvo estable entre 2019 y 2021 (1.57€ a 1.65€), con un aumento notable en 2022 a 1.80€. Este incremento, aunque moderado en comparación con otros servicios, impacta el coste de vida dado su carácter esencial.
- **Combustible**⛽: Después de una bajada notoria en 2020 (1.22€) por la caída de la demanda durante la pandemia, los precios se dispararon en 2021 y 2022, alcanzando 1.87€ en 2022. La recuperación económica y la alta demanda global impulsaron estos aumentos, exacerbados por las restricciones en la oferta y las tensiones internacionales en el sector energético.

---

## 2. 📉 Variación Mensual del Precio Promedio por Servicio (2019-2022)

![Variación Mensual del Precio Promedio por Servicio](src/01_graficas/03_VariaciónMensualPrecioPorServicio.png)

### Observaciones:
- **Agua**💧: Mantiene una estabilidad considerable en su precio mensual hasta 2022. Este servicio esencial experimenta un aumento en el último año, probablemente relacionado con la inflación en el coste de mantenimiento y distribución.
- **Combustibles**⛽: Muestran una gran variabilidad mensual, con aumentos significativos hacia finales de 2021 y 2022, vinculados con problemas de suministro y el encarecimiento de las materias primas como el petróleo.

---

## 3. ⚡ Variación Mensual del Precio Promedio de Luz y Gas (2019-2022)

![Variación Mensual del Precio Promedio de Luz y Gas](src/01_graficas/04_VariaciónMensualPrecioPorServicio.png)

### Observaciones:
- **Luz**💡: Observamos un incremento sostenido en 2021, alcanzando máximos históricos a finales de ese año, y se estabiliza en niveles altos en 2022. Las causas incluyen la creciente demanda de gas natural (utilizado en muchas plantas de generación de electricidad) y el aumento de precios de los derechos de emisión de CO₂ en la Unión Europea, que afectaron el coste de generación.
- **Gas**🔥: Los precios del gas se mantienen relativamente estables hasta principios de 2021, cuando comienzan a escalar significativamente, llegando a un máximo en octubre de 2022. Esta subida está directamente vinculada a la dependencia europea del gas natural ruso y a las interrupciones de suministro derivadas del conflicto en Ucrania y las sanciones impuestas.

---

## 4. 💡 Evolución Mensual del Precio de la Luz

![Evolución Mensual del Precio de la Luz](src/01_graficas/05_EvolucionMensualPrecioLuz.png)

### Observaciones:
- La electricidad ha experimentado una volatilidad extrema, sobre todo a partir de 2021. Los precios subieron rápidamente debido a varios factores, entre ellos:
  - **Aumento de la demanda de gas natural**: Al ser el gas una fuente primaria para la generación de electricidad en Europa, el aumento en sus precios encarece directamente la electricidad.
  - **Mercado de CO₂**🌍: El sistema de comercio de emisiones de la UE incrementa el coste de emisión de gases contaminantes, lo cual encarece la generación de electricidad en plantas tradicionales.
  - **Limitaciones de infraestructura**: La dependencia de fuentes renovables intermitentes como la energía eólica o solar, que no siempre pueden suplir la demanda, obliga a recurrir a plantas de energía más caras.

---

## 5. 🔥 Evolución Mensual del Precio del Gas

![Evolución Mensual del Precio del Gas](src/01_graficas/06_EvolucionPreciosGas.png)

### Observaciones:
- El precio del gas se ha disparado desde mediados de 2021, alcanzando picos a mediados de 2022. Los principales factores detrás de esta subida son:
  - **Conflicto en Ucrania**: La guerra entre Rusia y Ucrania y las subsecuentes sanciones han afectado el suministro de gas a Europa, lo que generó escasez y un aumento de precios.
  - **Alta demanda post-pandemia**📈: La recuperación económica global aumentó la demanda de gas, creando un desbalance entre oferta y demanda en un momento de limitación en los recursos.
  - **Capacidad limitada de almacenamiento**: Europa no tenía suficiente capacidad de almacenamiento de gas para compensar la reducción en el suministro, lo cual exacerbó las subidas de precios.

---

## 6. ⛽ Evolución Mensual del Precio de los Combustibles (Gasolina y Diésel)

![Evolución Mensual del Precio de los Combustibles](src/01_graficas/07_EvolucionPreciosCombustible.png)

### Observaciones:
- Tanto la gasolina como el diésel muestran incrementos significativos a partir de mediados de 2021, alcanzando máximos en 2022. Estos incrementos se explican por:
  - **Subida en el precio del crudo**: El petróleo, materia prima clave, se ha encarecido debido a la menor producción y a la incertidumbre geopolítica.
  - **Crisis en la cadena de suministro**🛢️: Las dificultades logísticas globales y el aumento de los costes de transporte han impactado los precios.
  - **Política energética global**🚢: Los intentos de transición hacia energías limpias han llevado a una reducción en inversiones en petróleo, limitando la capacidad de producción frente a una alta demanda.

---

## 7. 💧 Evolución Mensual del Precio del Agua

![Evolución Mensual del Precio del Agua](src/01_graficas/08_EvolucionPrecioAgua.png)

### Observaciones:
- El precio del agua se ha mantenido estable, con un incremento modesto en 2022. A diferencia de los combustibles y la electricidad, el agua ha sido menos afectada por factores de mercado y geopolíticos, debido a su carácter local y su menor dependencia de los mercados globales.

# 📌 Conclusión

Este análisis muestra cómo los precios de productos esenciales como la luz 💡, el gas 🔥 y los combustibles ⛽ han experimentado aumentos drásticos entre 2021 y 2022, impulsados por factores como la crisis energética, el conflicto en Ucrania 🇺🇦 y la alta demanda post-COVID 📈. La electricidad y el gas, en particular, han sido afectados por la dependencia de Europa en energías importadas y por la volatilidad en el mercado de emisiones de CO₂ 🌍. 

El agua 💧, en cambio, ha mostrado una mayor estabilidad, aunque también ha tenido un leve incremento en 2022.

## 💰 Impacto en el Costo de Vida
El aumento en los precios de estos productos esenciales afecta directamente el coste de vida. Luz, gas y combustibles son bienes que no podemos dejar de consumir, y sus aumentos se reflejan en facturas más altas 🧾, lo cual reduce el poder adquisitivo y eleva el costo de vida 📉. Además, el incremento en el precio de la energía tiene un efecto en cadena, encareciendo también la producción y el transporte de bienes y servicios.

En conclusión, el encarecimiento de estos bienes plantea un desafío para la economía doméstica, sobre todo para las familias con ingresos limitados. La presión sobre los presupuestos familiares obliga a reducir el gasto en otras áreas, afectando la calidad de vida general. Esto subraya la importancia de políticas que aseguren la accesibilidad y estabilidad de estos servicios básicos 🔄, para mitigar el impacto en la población y promover una vida más sostenible y accesible.

# Próximos Pasos 🚀

Para mejorar el análisis de precios y explorar patrones más detallados en los datos obtenidos, se plantean los siguientes pasos:

1. **Ampliación del Análisis a Toda España**
   - **Cobertura Nacional**: Extender el análisis de precios de agua, electricidad, gas y combustibles a todas las comunidades autónomas de España, con el fin de identificar variaciones regionales y obtener un panorama completo del mercado nacional.
   - **Desglose Regional**: Incorporar un desglose detallado que permita comparar los precios entre diferentes regiones, resaltando áreas con costos más altos o bajos.

2. **Solicitud de Información Detallada sobre Precios del Agua**
   - **Fuentes Adicionales**: Contactar organismos que dispongan de datos más desagregados sobre precios de agua en cada comunidad o ciudad, lo que permitirá un análisis preciso.
   - **Normalización de Datos**: Implementar un proceso de limpieza y normalización de datos del agua, asegurando que las comparaciones sean consistentes y precisas entre diferentes años y fuentes.

3. **Comparación con Precios en Europa**
   - **Análisis Comparativo Internacional**: Incorporar datos de precios de servicios (agua, electricidad, gas, combustibles) de otros países europeos para comparar la evolución de precios en España con la de otros países.
   - **Identificación de Patrones Globales**: Observar si las variaciones de precios en España siguen tendencias similares en el resto de Europa, lo que puede ayudar a identificar factores externos (como conflictos geopolíticos o cambios en el mercado global) que impacten los precios.

4. **Profundización en el Análisis Temporal y Estacional**
   - **Estacionalidad y Tendencias**: Desarrollar análisis más detallados para observar patrones estacionales en los precios, especialmente en servicios con alta variabilidad, como los combustibles.
   - **Predicción de Precios**: Utilizar modelos predictivos para anticipar posibles fluctuaciones en los precios de estos servicios y brindar un panorama a futuro.

5. **Mejora de Visualizaciones y Reportes**
   - **Visualizaciones Interactivas**: Implementar gráficos interactivos que permitan a los usuarios explorar los datos por comunidad autónoma, tipo de servicio y rango de fechas.
   - **Reportes Automatizados**: Crear reportes periódicos que informen sobre cambios significativos en los precios, y detectar anomalías que puedan alertar sobre subidas o bajadas inusuales.


# Contribuciones 🤝

Las contribuciones a este proyecto son muy bienvenidas. Si tienes alguna sugerencia, mejora o corrección, no dudes en ponerte en contacto o enviar tus ideas.

Cualquier tipo de contribución, ya sea en código, documentación o feedback, será valorada. ¡Gracias por tu ayuda y colaboración!

# Autores y Agradecimientos ✍️

## Autor ✒️
**Gonzalo Ruipérez Ojea** - [@apelsito](https://github.com/apelsito) en github

## Agradecimientos ❤️
Quiero expresar mi agradecimiento a **Hackio** y su equipo por brindarme la capacidad y las herramientas necesarias para realizar este proyecto con solo una semana de formación. Su apoyo ha sido clave para lograr este trabajo.
