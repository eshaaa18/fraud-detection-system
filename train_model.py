import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# load dataset (later replace with real CSV)
df = pd.read_csv("data.csv")

X = df[["amount"]]

model = IsolationForest(contamination=0.02)
model.fit(X)

joblib.dump(model, "model.pkl")

print("Model trained and saved")