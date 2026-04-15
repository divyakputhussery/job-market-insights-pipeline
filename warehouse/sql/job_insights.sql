SELECT COUNT(*) AS total_jobs
FROM jobs;

SELECT job_id, title, company, location
FROM jobs
LIMIT 5;

SELECT company, COUNT(*) AS job_count
FROM jobs
GROUP BY company
ORDER BY job_count DESC
LIMIT 10;

SELECT location, COUNT(*) AS job_count
FROM jobs
GROUP BY location
ORDER BY job_count DESC
LIMIT 10;

SELECT work_type, COUNT(*) AS job_count
FROM jobs
GROUP BY work_type
ORDER BY job_count DESC;