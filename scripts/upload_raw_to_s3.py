from pathlib import Path
import boto3


BUCKET_NAME = "job-market-insights-data"


def upload_latest_raw_file() -> None:
    raw_dir = Path("data/raw")
    files = list(raw_dir.glob("*.json"))

    if not files:
        print("No raw files found")
        return

    latest_file = sorted(files)[-1]

    s3 = boto3.client("s3")
    s3.upload_file(str(latest_file), BUCKET_NAME, latest_file.name)

    print(
      f"Uploaded {latest_file.name} "
      f"to s3://{BUCKET_NAME}/{latest_file.name}"
    )


if __name__ == "__main__":
    upload_latest_raw_file()
