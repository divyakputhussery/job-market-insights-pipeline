import os

import pandas as pd
import psycopg2
import streamlit as st


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "jobs_db")
DB_USER = os.getenv("DB_USER", "divyakp")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df


st.title("Job Market Insights Dashboard")

total_jobs = run_query(
    "SELECT COUNT(*) AS total_jobs FROM public.stg_jobs"
)
st.metric("Total Jobs", int(total_jobs["total_jobs"][0]))

top_companies = run_query(
    """
    SELECT company, job_count
    FROM public.company_job_counts
    LIMIT 10
    """
)

st.subheader("Top Companies")
st.bar_chart(
    top_companies.set_index("company")["job_count"]
)

top_locations = run_query(
    """
    SELECT location, COUNT(*) AS job_count
    FROM public.stg_jobs
    GROUP BY location
    ORDER BY job_count DESC
    LIMIT 10
    """
)

st.subheader("Top Locations")
st.bar_chart(
    top_locations.set_index("location")["job_count"]
)

work_types = run_query(
    """
    SELECT work_type, COUNT(*) AS job_count
    FROM public.stg_jobs
    GROUP BY work_type
    ORDER BY job_count DESC
    """
)

st.subheader("Work Type Breakdown")
st.bar_chart(
    work_types.set_index("work_type")["job_count"]
)