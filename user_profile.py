from database import supabase


def get_user_profile(user_id):
    res = supabase.table("user_profiles").select("*").eq("user_id", user_id).execute()
    if res.data:
        return res.data[0]
    return None


def update_user_profile(user_id, amount, location):
    profile = get_user_profile(user_id)

    if not profile:
        supabase.table("user_profiles").insert({
            "user_id": user_id,
            "avg_amount": amount,
            "last_location": location,
            "transaction_count": 1
        }).execute()
    else:
        new_count = profile["transaction_count"] + 1
        new_avg = (profile["avg_amount"] * profile["transaction_count"] + amount) / new_count

        supabase.table("user_profiles").update({
            "avg_amount": new_avg,
            "last_location": location,
            "transaction_count": new_count
        }).eq("user_id", user_id).execute()