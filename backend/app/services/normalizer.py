import pandas as pd

def normalize(df, colmap):
    out = pd.DataFrame()
    g = colmap.get

    if g("order_id") in df: out["order_id"] = df[g("order_id")].astype(str)
    if g("customer") in df: out["customer"] = df[g("customer")].astype(str).str.title()
    if g("amount") in df: out["amount"] = pd.to_numeric(df[g("amount")], errors="coerce")
    if g("currency") in df:
        out["currency"] = df[g("currency")].astype(str).str.upper().str.replace("$", "USD")
    if g("order_date") in df:
        out["order_date"] = pd.to_datetime(df[g("order_date")], errors="coerce", utc=True)
    return out
