---
title: Getting Started with AnyCost Bucket
category: features
createdAt: '2022-08-03'
hidden: false
slug: anycost-bucket-getting-started
updatedAt: ''
---
An AnyCost Bucket Adaptor automates the flow of cost data into CloudZero by allowing you to upload data from any cost source to an Amazon S3 bucket.

To set up an AnyCost Bucket connection, complete the following steps:

1. [Create an S3 bucket to store cost data.](#step-1-create-an-s3-bucket-to-store-data)
2. [Register the connection in the CloudZero UI.](#step-2-register-the-connection-in-the-ui)
3. [Write the code that powers the Adaptor.](#step-3-write-code-to-create-a-custom-adaptor)
4. [Upload your cost data to S3.](#step-4-upload-cost-data-to-s3)

<Callout icon="ℹ️" theme="info">
  All of CloudZero's AWS permissions are read-only.

  AnyCost Bucket Adaptors write their cost data to an S3 bucket, and CloudZero requires the following permissions to read from that specific bucket:

  * `s3:Get*`
  * `s3:List*`

  If your AnyCost Bucket Adaptor writes to an S3 bucket in any region where STS is not active by default (such as `ap-east-1` or `eu-south-1`), ensure you activate those regions following the [Managing AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) guide._
</Callout>

## Prerequisites

* Ensure you have the necessary permissions to create a new connection in CloudZero.
* Ensure you have an existing [AWS Connection](/docs/connections-aws-automated) for the AWS account where your AnyCost Bucket Adaptor will store billing data.

## Step 1: Create an S3 bucket to store data

First, create an Amazon S3 bucket in your AWS account. Your AnyCost Bucket Adaptor will write Common Bill Format `.csv.gz` files to this bucket. To learn how to create a bucket, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

You will need the bucket name for the **Bucket Name** field in [Step 2](#step-2-register-the-connection-in-the-ui).

Inside the bucket, create a folder for the cost data and give it a meaningful name. For example, if the cost source is Sumo Logic, you could name the folder `sumo-logic-cost-data`. The folder can be nested inside other folders, if needed (for example, `cloudzero/sumo-logic-cost-data`).

You will need the folder path for the **Bucket Path** field in [Step 2](#step-2-register-the-connection-in-the-ui).

Note that creating a folder is **required**. AnyCost data cannot be stored at the root of the bucket (path `/`).

## Step 2: Register the Connection in the UI

Next, you must register your AnyCost Adaptor as a Billing Connection in the CloudZero UI.

In CloudZero, navigate to [Settings](https://app.cloudzero.com/organization/connections) by selecting the **gear icon** in the top navigation bar.

Select the **Add Connection** button.

Next, select the **AnyCost Bucket** tile and select **Get started**.

In **Add a New Custom Connection** page, fill out the following fields:

1. **Connection Metadata**

   * **Cloud Provider**: The description that will appear in the Cloud Provider Dimension and throughout the UI alongside AWS, Snowflake, Azure, GCP, and so on. For example, if you wrote an Adaptor for a service called Simple Cloud, you would enter `Simple Cloud` in this field.

   * **Connection Name**: The name of this particular connection to the Cloud Provider. The connection name is typically used to distinguish between accounts, environments, and/or instances of the AnyCost adaptors. It cannot contain spaces, periods, or special characters (except for hyphens and underscores).

     For example, if you are sending cost data from the Simple Cloud service for both your production and dev environments, the connection name might be `simple-cloud-prod`.

   * **Expected Data Delivery Frequency**: _Optional_: How often your AnyCost Adaptor is expected to deliver data to the S3 bucket, in hours. Enter a whole number only. Providing this information helps CloudZero determine the health of your connection.

2. **S3 Bucket Information**

   * **AWS Connection**: The existing [AWS Connection](/docs/connections-aws-automated) with the S3 bucket that the AnyCost Adaptor will write Common Bill Format files into.
   * **Bucket Name**: The name of the bucket you created in [Step 1](#step-1-create-an-s3-bucket-to-store-data).
   * **Bucket Path**: The path to the folder you created in [Step 1](#step-1-create-an-s3-bucket-to-store-data). Do not include leading or trailing slashes in the path. For example, use `my/file/path` instead of `/my/file/path/`.
   * **Generate IAM Policy**: Select this button to generate an IAM policy definition using the name of your S3 bucket. You must attach this policy to the CloudZero resource owner IAM role (named similar to `cloudzero-connected-account-live-ResourceOwner-Role-<RANDOM ID>`) to grant access to the billing data in your bucket. To learn how to attach a policy, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions_create-policies.html).

Select **Save**.

Once created, your AnyCost Bucket connection appears in the **Billing Connections** table of the [Cloud Integrations](https://app.cloudzero.com/organization/connections) page.

<Image alt="Billing Connections" border={false} src="https://downloads.cloudzero.com/documentation/resources/billing-connections.png" />

<Callout icon="ℹ️" theme="info">
  If you want to change the bucket used for an AnyCost Bucket Connection, you must create a new connection and pause (not delete) the old connection. This keeps the historical data and allows you to change the bucket used for the AnyCost Bucket data.
</Callout>

## Step 3: Write Code to Create a Custom Adaptor

After you create the connection in the CloudZero UI, you must write the code to create the AnyCost Adaptor. For instructions, see [Creating AnyCost Custom Adaptors](/docs/anycost-custom-adaptors).

## Step 4: Upload Cost Data to S3

Finally, upload cost data files to the S3 bucket. For details, see [Configuring AnyCost Bucket File Drops](/docs/anycost-cbf-drop-specs).

CloudZero then connects to the S3 bucket, retrieves the cost data, validates it, and processes it.

When CloudZero has processed the first ingest of data, the **Status** changes from **Pending Data** to **Healthy**. This can take several hours.

If CloudZero can no longer connect to the bucket or if your AnyCost Bucket Adaptor is not writing data correctly, the **Status** is updated with details about the error.

Note that it can take up to a day to synchronize new accounts before you see cost data in the [Explorer](/docs/explorer).
