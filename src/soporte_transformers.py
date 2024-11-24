import pickle

# Cargar los modelos y transformadores entrenados
def load_models():
    with open('../../datos/modelos-encoders/target_encoder.pkl', 'rb') as f:
        target_encoder = pickle.load(f)
    with open('../../datos/modelos-encoders/one_hot_encoder.pkl', 'rb') as f:
        one_hot_encoder = pickle.load(f)
    with open('../../datos/modelos-encoders/robust_scaler.pkl', 'rb') as f:
        robust_scaler = pickle.load(f)    
    with open('../../datos/modelos-encoders/modelo_xgb.pkl', 'rb') as f:
        modelo = pickle.load(f)
    return target_encoder, one_hot_encoder, robust_scaler, modelo
