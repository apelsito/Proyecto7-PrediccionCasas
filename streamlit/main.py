import streamlit as st
import pandas as pd
import pickle

from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

import sys
sys.path.append("../")
from src.soporte_transformers import (
    load_models
)


# Configurar la página de Streamlit
st.set_page_config(
    page_title="Predicción de Precios de Casas",
    page_icon="🏠",
    layout="centered",
)

# Título y descripción
st.title("🏠 Predicción de Precios de Casas con Machine Learning")
st.write("Usa esta aplicación para predecir el precio de una casa basándote en sus características. ¡Sorpréndete con la magia de los datos! 🚀")

# Mostrar una imagen llamativa
st.image(
    "https://images.unsplash.com/photo-1568605114967-8130f3a36994",  # URL de la imagen
    caption="Tu próxima casa está aquí.",
    use_column_width=True,
)

# Cargar los modelos y transformadores entrenados
target_encoder, one_hot_encoder, robust_scaler, modelo_xgb =  load_models()

