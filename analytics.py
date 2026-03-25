from database import supabase
def get_stats():
    res = supabase.table("transactions").select("*").execute()
    data = res.data or []

    total = len(data)
    fraud_count = sum(1 for x in data if x.get("fraud_flag"))

    return {
        "total_transactions": total,
        "fraud_count": fraud_count,
        "fraud_rate": (fraud_count / total * 100) if total else 0
    }

def get_model_performance():
    res = supabase.table("transactions").select("*").execute()
    data = res.data or []

    y_true = []
    y_pred = []

    for row in data:
        actual = row.get("is_fraud_actual")
        pred = row.get("fraud_flag")

        if actual is not None:
            y_true.append(actual)
            y_pred.append(pred)

    if not y_true:
        return {"message": "No labeled data"}

    correct = sum(1 for i in range(len(y_true)) if y_true[i] == y_pred[i])
    accuracy = correct / len(y_true)

    return {
        "accuracy": round(accuracy, 4),
        "total_samples": len(y_true)
    }

def get_advanced_metrics():
    res = supabase.table("transactions").select("*").execute()
    data = res.data or []

    tp = fp = tn = fn = 0

    for row in data:
        actual = row.get("is_fraud_actual")
        pred = row.get("fraud_flag")

        if actual is None:
            continue

        if pred and actual:
            tp += 1
        elif pred and not actual:
            fp += 1
        elif not pred and not actual:
            tn += 1
        elif not pred and actual:
            fn += 1

    # Avoid division by zero
    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) else 0

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "accuracy": round(accuracy, 4),
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn
    }