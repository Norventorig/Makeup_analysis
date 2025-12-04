from pathlib import Path
from model.model_handler.model_handler import ModelHandler
from tensorflow.keras.models import load_model
import pickle

PROJECT_ROOT = Path(__file__).resolve().parents[1]
utils_path = PROJECT_ROOT / "model" / "utils"

model = load_model(utils_path / "model.keras")
with open(utils_path / 'config.pkl', 'rb') as f:
    labels = pickle.load(f)

model_handler = ModelHandler(labels=labels, model=model)
