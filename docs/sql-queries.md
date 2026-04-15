SELECT COUNT(*) FROM jobs;

SELECT job_id, title, company, location
FROM jobs
LIMIT 5;

SELECT job_id, COUNT(*)
FROM jobs
GROUP BY job_id
HAVING COUNT(*) > 1;

SELECT job_id, COUNT(*)
FROM jobs
GROUP BY job_id
HAVING COUNT(*) > 1;

SELECT COUNT(*) 
FROM jobs
WHERE company IS NULL;

SELECT company, COUNT(*) AS job_count
FROM jobs
GROUP BY company
ORDER BY job_count DESC
LIMIT 5;