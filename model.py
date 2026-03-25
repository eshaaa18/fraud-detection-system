import joblib

model = joblib.load("model.pkl")

def predict_fraud(features):
    score = model.decision_function([features])[0]
    pred = model.predict([features])[0]
    return score, (pred == -1)