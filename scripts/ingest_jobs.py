import os
import json
from datetime import datetime, timezone

import requests


APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")
COUNTRY = "au"
PAGE = 1
WHAT = "software engineer"
WHERE = "sydney"


def fetch_jobs() -> dict:
    if not APP_ID or not APP_KEY:
        raise ValueError("Missing ADZUNA_APP_ID or ADZUNA_APP_KEY.")

    url = (
        f"https://api.adzuna.com/v1/api/jobs/"
        f"{COUNTRY}/search/{PAGE}"
    )
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": WHAT,
        "where": WHERE,
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def save_raw_data(data: dict) -> str:
    os.makedirs("data/raw", exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    filepath = f"data/raw/jobs_{timestamp}.json"

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return filepath


def main() -> None:
    data = fetch_jobs()
    filepath = save_raw_data(data)
    print(f"Saved raw data to {filepath}")


if __name__ == "__main__":
    main()

