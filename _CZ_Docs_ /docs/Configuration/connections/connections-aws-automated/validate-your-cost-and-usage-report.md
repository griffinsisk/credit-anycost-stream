---
title: 'AWS: Validate your Cost and Usage Report'
category: getting-started
createdAt: '2020-02-13T23:52:44.710Z'
hidden: false
slug: validate-your-cost-and-usage-report
updatedAt: '2020-02-14T14:32:53.985Z'
---
When connecting to your AWS Management or Payer Account, CloudZero will attempt to connect to an existing Cost and Usage Report if it is in the correct format and granularity for CloudZero to ingest.

If there is no existing Cost and Usage Report that is suitable, the [Automated path](/docs/connections-aws-automated) will try to create one, or the [Manual path](/docs/connections-aws-manual-billing) will provide instructions on how to create one.

For a Cost and Usage Report to be valid for CloudZero, it must have the following required settings:

* Time Granularity: Hourly
* Report Versioning: Create New Report Version
* Compression: GZIP
* Include Resource IDs: ON
* Data Refresh Settings: AUTOMATIC

The following are recommended settings:

* S3 bucket name: `<your-company-name>`-billing (recommended name)
* Report path prefix: hourly-billing (recommended name)

<Callout icon="ℹ️" theme="info">
  If you create a new Cost and Usage Report, it can take up to 24 hours before AWS releases billing data to the new report. If you create a Cost and Usage Report manually, you must select **Legacy CUR export**.
</Callout>

For more information on configuring AWS Cost and Usage Reporting, see the AWS documentation for [Creating reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html).
