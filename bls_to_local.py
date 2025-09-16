# bls_to_local.py
import os
import json
import requests
from datetime import datetime

# ---------------- CONFIG ----------------
BLS_API_KEY = "a2365561af674b4db7f3dc2b6837560a"
SERIES = ["CUSR0000SAF11"]   # replace/add series IDs
LOCAL_RAW_DIR = "./raw_files/"  # folder on your Mac to save JSON
# ----------------------------------------

# Fetch BLS data
def fetch_bls(series_ids, startyear, endyear):
    headers = {"Content-type": "application/json"}
    payload = {
        "seriesid": series_ids,
        "startyear": str(startyear),
        "endyear": str(endyear),
        "registrationkey": BLS_API_KEY
    }
    r = requests.post("https://api.bls.gov/publicAPI/v2/timeseries/data/",
                      json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()

# Format BLS API response into newline-delimited JSON
def format_records(api_json):
    out = []
    for s in api_json["Results"]["series"]:
        sid = s["seriesID"]
        for item in s["data"]:
            rec = {
                "seriesID": sid,
                "year": item.get("year"),
                "period": item.get("period"),
                "periodName": item.get("periodName"),
                "value": float(item.get("value")) if item.get("value") not in (None,"") else None
            }
            out.append(rec)
    return out

# Save records locally
def save_locally(records):
    os.makedirs(LOCAL_RAW_DIR, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = os.path.join(LOCAL_RAW_DIR, f"bls_{ts}.json")
    with open(filename, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
    print("Saved locally:", filename)
    return filename

# ---------------- MAIN ----------------
if __name__ == "__main__":
    now = datetime.utcnow()
    data = fetch_bls(SERIES, now.year-3, now.year)  # last 3 years
    records = format_records(data)
    save_locally(records)

