import json
import os
from pathlib import Path

import psycopg2


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "jobs_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def create_table(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS jobs (
                job_id TEXT PRIMARY KEY,
                title TEXT,
                company TEXT,
                location TEXT,
                work_type TEXT,
                category TEXT,
                posted_date TIMESTAMP,
                description TEXT,
                source_url TEXT,
                latitude FLOAT,
                longitude FLOAT,
                salary_is_predicted INT,
                collected_at TIMESTAMP
            );
            """
        )
    conn.commit()


def load_data(conn, file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    with conn.cursor() as cur:
        for job in jobs:
            cur.execute(
                """
                INSERT INTO jobs (
                    job_id,
                    title,
                    company,
                    location,
                    work_type,
                    category,
                    posted_date,
                    description,
                    source_url,
                    latitude,
                    longitude,
                    salary_is_predicted,
                    collected_at
                )
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s
                )
                ON CONFLICT (job_id) DO NOTHING;
                """,
                (
                    job.get("job_id"),
                    job.get("title"),
                    job.get("company"),
                    job.get("location"),
                    job.get("work_type"),
                    job.get("category"),
                    job.get("posted_date"),
                    job.get("description"),
                    job.get("source_url"),
                    job.get("latitude"),
                    job.get("longitude"),
                    job.get("salary_is_predicted"),
                    job.get("collected_at"),
                ),
            )
    conn.commit()


def main():
    processed_dir = Path("data/processed")
    files = list(processed_dir.glob("*.json"))

    if not files:
        print("No processed files found")
        return

    latest_file = sorted(files)[-1]

    conn = get_connection()
    create_table(conn)
    load_data(conn, latest_file)
    conn.close()

    print(f"Loaded data from {latest_file} into PostgreSQL")


if __name__ == "__main__":
    main()
