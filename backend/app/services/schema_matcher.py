from rapidfuzz import fuzz, process

CANONICAL = {
    "order_id": ["orderid","oid","order_no","id"],
    "customer": ["customer_name","client","buyer"],
    "amount":   ["price","total","usd_amount"],
    "currency": ["currency","curr","$"],
    "order_date": ["date","order_dt","timestamp"]
}

def infer_columns(df):
    return [c.strip().lower().replace(" ", "_").replace("-", "_") for c in df.columns]

def best_map_to_canonical(cols, threshold=70):
    mapping = {}
    for canon, aliases in CANONICAL.items():
        choice, score, _ = process.extractOne(
            canon, cols + [a.lower() for a in aliases], scorer=fuzz.WRatio
        )
        if score >= threshold:
            mapping[canon] = choice
    return mapping
