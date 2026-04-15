from pathlib import Path
import boto3


BUCKET_NAME = "job-market-insights-data"


def upload_latest_processed_file():
    processed_dir = Path("data/processed")
    files = list(processed_dir.glob("*.json"))

    if not files:
        print("No processed files found")
        return

    latest_file = sorted(files)[-1]

    s3 = boto3.client("s3")
    s3_key = f"processed/{latest_file.name}"

    s3.upload_file(str(latest_file), BUCKET_NAME, s3_key)

    print(
      f"Uploaded {latest_file.name} "
      f"to s3://{BUCKET_NAME}/{s3_key}"
    )


if __name__ == "__main__":
    upload_latest_processed_file()
