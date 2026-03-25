from model import predict_fraud
from user_profile import get_user_profile


def check_rules(amount, location, device, profile):
    reasons = []

    if amount > 50000:
        reasons.append("high_amount")

    if device.lower() == "new":
        reasons.append("new_device")

    if profile:
        if abs(amount - profile["avg_amount"]) > 20000:
            reasons.append("amount_anomaly")

        if location != profile["last_location"]:
            reasons.append("location_change")

    return reasons


def calculate_risk(score, reasons):
    base = 0.5 * (1 - score)  # ML score inverted
    rule_score = len(reasons) / 4

    risk_score = base + rule_score

    if risk_score > 0.7:
        level = "HIGH"
    elif risk_score > 0.4:
        level = "MEDIUM"
    else:
        level = "LOW"

    return risk_score, level


def detect_fraud(user_id, amount, location, device):
    profile = get_user_profile(user_id)

    reasons = check_rules(amount, location, device, profile)

    device_flag = 1 if device == "old" else 0
    features = [amount, device_flag]

    score, ml_flag = predict_fraud(features)

    risk_score, risk_level = calculate_risk(score, reasons)

    fraud = risk_level == "HIGH"

    return fraud, score, reasons, risk_score, risk_level