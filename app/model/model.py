import pickle
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f'{BASE_DIR}/model-{__version__}.pkl', 'rb') as f:
    model = pickle.load(f)

classes = [
    'Not Fraud',
    'Fraud'
]


def get_predict(feat: list):
    prediction = model.predict([feat])
    return classes[prediction[0]]
