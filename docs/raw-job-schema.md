# Raw Job Schema

## Fields
- job_id
- title
- company
- location
- work_type
- category
- posted_date
- description
- source_url
- latitude
- longitude
- salary_is_predicted
- collected_at

## Mapping (Adzuna → Internal)
- id → job_id
- title → title
- company.display_name → company
- location.display_name → location
- contract_time → work_type
- category.label → category
- created → posted_date
- description → description
- redirect_url → source_url
- latitude → latitude
- longitude → longitude
- salary_is_predicted → salary_is_predicted

## Notes
- `job_id` should be treated as the unique identifier from the source
- `collected_at` will be added by the ingestion script at collection time
- salary_min and salary_max are not included yet because they were not present in this sample record
- nested Adzuna fields are flattened into simple internal field names