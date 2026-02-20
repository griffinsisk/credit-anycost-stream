---
title: Updating Manual Snowflake Connection
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-snowflake-updating-manual-connection
updatedAt: '2021-11-30T17:29:59.987Z'
---
If you have configured a **non us-east-1 Snowflake billing connection with CloudZero**, you may need to reapply the Trust Relationship between the CloudZero cross-account role and your Snowflake instance. This relationship allows your Snowflake instance to drop files into the appropriate S3 bucket for CloudZero to ingest.

1. Run the following in your Snowflake instance: `DESC INTEGRATION CLOUDZERO_BILLING_DATA_S3_ACCESS;`.
2. From the output, copy the values for `STORAGE_AWS_EXTERNAL_ID` and `STORAGE_AWS_IAM_USER_ARN`. You will need these for your Trust Policy.
3. Open the IAM Role Console in the appropriate AWS Account.
4. Find the cross-account role with a trust relationship with CloudZero.
   1. You can do this by searching your Roles for `cloudzero`. Select the one with `Trusted entities` containing `Account: 061190967865`.
   2. Click on the role name hyperlink.
5. Click the **Trust Relationships** tab, and then the **Edit trust relationship** button.
6. Switch the view to JSON. You will see a single statement that includes any cross-account permissions already applied (if any).
7. Add an additional statement to the policy to allow Snowflake cross-account access by copying this [JSON object](https://cz-provision-account.s3.amazonaws.com/snowflake/trust-relationship.json) under the key Statements. Replace the `<STORAGE_AWS_IAM_USER_ARN>` and `<STORAGE_AWS_EXTERNAL_ID>` place holders with the values you copied.
