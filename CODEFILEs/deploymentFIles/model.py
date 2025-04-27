# model.py
from pycaret.classification import load_model, predict_model
import pandas as pd

# Load model only once
model = load_model('./svm classifier')  # no .pkl in load_model, just name

def predict_message(message: str) -> str:
    data = pd.DataFrame({"description": message},index=[0])
    prediction = predict_model(model, data=data)
    label = prediction[0]
    return label
