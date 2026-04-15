SELECT
    company,
    COUNT(*) AS job_count
FROM {{ ref('stg_jobs') }}
GROUP BY company
ORDER BY job_count DESC