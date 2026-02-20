---
title: Connecting AWS Billing Data Manually from a Management or Payer Account
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-aws-manual-billing
updatedAt: '2021-11-30T17:29:59.987Z'
---
CloudZero supports a fully manual or custom provisioning process that can be facilitated using your infrastructure provisioning process of choice, for example Terraform, Shell Scripts, CLI, and so on.

# How the manual AWS Integration works

CloudZero is a Cloud Cost Management solution that requires permissions beyond the typical cost and usage data. By using metadata on how your AWS environment is operating, the services that you are using, and how they are being used, CloudZero can boost tag coverage, identify more complex anomalies, and highlight the specific resources and changes that are responsible for cost changes in your environment.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's permissions are read-only. CloudZero has no access to data except where explicitly authorized, for example the S3 bucket where your cost and usage report is stored.
</Callout>

The following summarizes the permissions that CloudZero needs:

Management Account access is need for:

* Access to the Cost and Usage, Billing, and Organizations API
* Access to the Cost and Usage S3 bucket where reports are stored
* Access to CloudWatch Metrics
* Read-only access to the list metadata service API

<Callout icon="ℹ️" theme="info">
  If you have resources in your AWS cloud in any regions for which STS is not active by default, for example, `ap-east-1` or `eu-south-1`, make sure you activate those regions following the Amazon [Managing AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) guide.
</Callout>

# Prerequisites for connecting manually from a Management or Payer Account

You must also configure the the following AWS services before connecting to CloudZero:

* Required: [AWS Organizations with consolidated billing enabled](https://aws.amazon.com/organizations/)
* Required: [Cost and Usage Report enabled within your AWS Payer account](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) (sometimes also called your AWS Management account
* Highly recommended: [Cost Allocation Tagging Configuration](/docs/cost)

In addition, CloudZero has requirements for [valid Cost & Usage Reports](/docs/validate-your-cost-and-usage-report).

# Connect an AWS Account

For most features to work, you must connect your AWS account that holds your Management Account so that CloudZero can get access to your billing data. CloudZero strong recommend that you connect your Management Account first.

CloudZero fully supports organizations with multiple Management Accounts. Follow the steps in this section to connect all your Management Accounts to get a consolidated view of your spending.

## Add an AWS Connection

<Callout icon="ℹ️" theme="info">
  You must be a CloudZero Admin to add new Integrations to the platform.
</Callout>

To open the Cloud Integrations page, navigate to the gear icon on the top navigation bar and select Cloud Integrations, or use the link to the page: [https://app.cloudzero.com/organization/connections](https://app.cloudzero.com/organization/connections)

On the Cloud Integrations page you can see all of the Integrations in your system. To connect an AWS Account, click the **Add Connection** button.

On the page that opens, click the **AWS** tile and to manually connect an AWS Management or Payer Account, click the **Manual - Billing** button from the three options for connecting accounts.

Follow the steps on the screen to enable cost and usage reports from the AWS console. As you follow these steps, note the following unique pieces of information you must gather while in the AWS console:

* Cost & Usage Report Name
* Cross-Account IAM Role ARN
* Cost & Usage S3 Bucket Name

In addition, note of the external ID listed under **Create a cross-account AIM role** in the manual connection steps. You will need this while configuring your policy in the AWS Console.

<Callout icon="ℹ️" theme="info">
  You must create an AWS cross-account access role. Refer to the information box where the system has generated all of the necessary policy details you must provide in the AWS Console.
</Callout>

In the box, enter the S3 Bucket Name where your Cost & Usage Report will be saved, as provided when you enabled cost and usage reports in the AWS console. Click the **Generate IAM Policy** button to help generate all of the necessary policy details you must provide in the AWS Console.

## Enter Cost and Usage Report details

After your policy is generated and applied to your S3 bucket, you must complete the input boxes using the information you collected from the AWS Console earlier.

1. Enter a **Connection Name**. This is the name you will see throughout the CloudZero UI, in addition to the AWS Account ID.
   The name must conform to AWS naming conventions: lowercase, dashes, without spaces or periods.
2. Enter the **Cost & Usage Report Name**.
   This is _not_ the name of your cost and usage S3 bucket, but the name of your cost and usage report configuration in AWS. [Find your CUR name](https://console.aws.amazon.com/billing/home?#/reports) on Amazon.
3. Enter the **Cross-Account IAM Role ARN**, as found in the AWS Console earlier.
4. Click **Save**.

## Confirm on the Cloud Integrations page

AWS generally takes ~5 minutes to deploy the necessary permissions to allow CloudZero to pull in the information it needs. AWS cost and usage data will typically appear in CloudZero within 24 hours of the integration being configured.

When the connection is complete, an AWS Connection appears on the CloudZero Cloud Integrations page in the **Billing Connections** table.

<Image align="center" alt="Billing Connections table" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/billing-connections.png" />

The **Health** column will be green or red and show the overall connection health. If something changes on your side and CloudZero can no longer use the role that was just granted permissions, the **Health** will change and provide details on why CloudZero cannot connect.

You can connect any other AWS Accounts you want at this point using the same process.
