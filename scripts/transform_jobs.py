import json
from datetime import datetime, timezone
from pathlib import Path


def transform_job(job: dict) -> dict:
    return {
        "job_id": job.get("id"),
        "title": job.get("title"),
        "company": job.get("company", {}).get("display_name"),
        "location": job.get("location", {}).get("display_name"),
        "work_type": job.get("contract_time"),
        "category": job.get("category", {}).get("label"),
        "posted_date": job.get("created"),
        "description": job.get("description"),
        "source_url": job.get("redirect_url"),
        "latitude": job.get("latitude"),
        "longitude": job.get("longitude"),
        "salary_is_predicted": job.get("salary_is_predicted"),
        "collected_at": datetime.now(timezone.utc).isoformat(),
    }


def process_file(input_path: Path, output_path: Path) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    jobs = data.get("results", [])
    transformed = [transform_job(job) for job in jobs]

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(transformed, f, indent=2)


def main():
    raw_dir = Path("data/raw")
    output_dir = Path("data/processed")

    files = list(raw_dir.glob("*.json"))
    if not files:
        print("No raw files found")
        return

    latest_file = sorted(files)[-1]
    output_file = output_dir / f"processed_{latest_file.name}"

    process_file(latest_file, output_file)
    print(f"Processed data saved to {output_file}")


if __name__ == "__main__":
    main()
