import asyncio
import random

async def simulate_transactions():
    while True:
        fake_txn = {
            "user_id": random.randint(1, 3),
            "amount": random.randint(100, 100000),
            "location": random.choice(["home", "office", "unknown"]),
            "device": random.choice(["old", "new"])
        }

        fraud, score, reasons, risk_score, risk_level = detect_fraud(
            fake_txn["user_id"],
            fake_txn["amount"],
            fake_txn["location"],
            fake_txn["device"]
        )

        supabase.table("transactions").insert({
            **fake_txn,
            "fraud_flag": fraud,
            "fraud_score": float(score),
            "risk_score": risk_score,
            "risk_level": risk_level
        }).execute()

        print("⚡ Simulated transaction:", fake_txn)

        await asyncio.sleep(5)  # every 5 sec


@app.on_event("startup")
async def start_simulation():
    asyncio.create_task(simulate_transactions())