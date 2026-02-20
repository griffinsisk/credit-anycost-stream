---
title: /v2/billing/costs
excerpt: >
  This API will return cost data according to the parameters passed in.


  - Rate Limit: 60 requests/day.

  - Timeout: 30 seconds.

  - Pagination: Results are paginated in blocks of 10,000 records.
    - Using cursors for pagination doesn't affect the rate limit.
    - You have 24 hours to page through your results before you will need to rerun your query.
    - While using pagination, your results will be static as of run time.
  - This data is statically sorted as `usage_date asc`.

   NOTE: The Dimension IDs referenced within this document are the IDs by which you reference dimensions when authoring in CostFormation. You can read more about this [here](https://docs.cloudzero.com/docs/costformation-definition-language-guide#specifying-sources).

  **API Call Examples**

  For the following examples, the following updates need to be made before
  running:

  - Replace <START_DATE_HERE> with a properly formatted start date (`2023-10-26`
  or (date and time encoded) `2023-10-26T14%3A27%3A46%2B00%3A00`)

  - Replace <GRANULARITY_VALUE_HERE> with the desired granularity (`hourly`,
  `daily`,  `weekly`, `monthly`, `yearly`)


  **Real Cost Grouped by Account and Service, Filtered by Cloud Provider = AWS**

  -
  `https://api.cloudzero.com/v2/billing/costs?start_date=<START_DATE_HERE>&granularity=<GRANULARITY_VALUE_HERE>&group_by=Account&group_by=Service&filters=%7B%22CloudProvider%22%3A%20%5B%22AWS%22%5D%7D&cost_type=real_cost`


  **Real Cost Grouped by Account and Service Detail Dimension, Filtered by
  Service = AmazonS3**

  -
  `https://api.cloudzero.com/v2/billing/costs?start_date=<START_DATE_HERE>&granularity=<GRANULARITY_VALUE_HERE>&group_by=Account&group_by=CZ%3ADefined%3AServiceDetail&filters=%7B%22Service%22%3A%20%5B%22AmazonS3%22%5D%7D&cost_type=real_cost`


  **Real Cost Grouped by by Account Name and Service**

  -
  `https://api.cloudzero.com/v2/billing/costs?start_date=<START_DATE_HERE>&granularity=<GRANULARITY_VALUE_HERE>&group_by=User%3ADefined%3AAccountName&group_by=Service&cost_type=real_cost`
api:
  file: CloudZero-API-V2.yaml
  operationId: getBillingCosts
hidden: false
---