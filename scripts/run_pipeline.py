import subprocess
import sys


def run_step(script_path):
    command = [sys.executable, script_path]
    print(f"Running: {' '.join(command)}", flush=True)

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    print(result.stdout, end="")
    print(result.stderr, end="")

    if result.returncode != 0:
        raise Exception(f"Failed: {script_path}")


def main():
    print("Starting pipeline...", flush=True)

    run_step("scripts/ingest_jobs.py")
    run_step("scripts/transform_jobs.py")
    run_step("scripts/upload_raw_to_s3.py")
    run_step("scripts/upload_processed_to_s3.py")
    run_step("scripts/load_to_postgres.py")

    print("Pipeline completed successfully", flush=True)


if __name__ == "__main__":
    main()
