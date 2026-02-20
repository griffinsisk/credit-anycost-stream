CloudZero Pipeline Project Discussion
Goal: Automate monthly redistribution of AWS credits for Kiteworks into CloudZero.
Pipeline Overview:

AWS credits (monthly) are dropped into an S3 bucket.
AWS Lambda triggers on file upload.
Lambda parses credits by account ID, not name.
Parsed data is sent to CloudZero via API.
CloudZero uses credits for Kiteworks’ monthly accounting.
Key Points:

Monthly file format must be consistent.
API call robustness is critical.
Ensure alignment with account usage.
Validate allocations in CloudZero dashboards.
Anticipate potential structural changes in credits.
Next Steps:

Upload CloudZero API docs to the project.
Build and run a prototype.
Confirm process with Kiteworks team.