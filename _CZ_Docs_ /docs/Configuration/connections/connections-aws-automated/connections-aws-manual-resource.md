---
title: Connecting AWS Resource Data Manually from a Member Account
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-aws-manual-resource
updatedAt: '2021-11-30T17:29:59.987Z'
---
CloudZero supports a fully manual or custom provisioning process that can be facilitated using your infrastructure provisioning process of choice, Terraform, Shell Scripts, CLI, and so on.

<Callout icon="ℹ️" theme="info">
  To get started, you must connect an AWS Management or Payer Account. Confirm that you have [followed the AWS Connection process](/docs/connections-aws-automated) before you add a Resource Connection.
</Callout>

# How the Manual AWS Connection works

CloudZero is a Cloud Cost Management solution and requires permissions beyond the typical cost and usage data. By using metadata on how your AWS environment is operating, the services that you are using, and how they are being used, CloudZero can boost tag coverage, identify more complex anomalies, and highlight the specific resources and changes that are responsible for cost changes in your environment.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's permissions are read-only. CloudZero has no access to data except where explicitly authorized.
</Callout>

The following summaries the permissions that CloudZero needs.

* Access to Resource (member) Accounts, optional but required for waste and root cause analysis
* Access to CloudWatch Metrics
* Read-only access to the list metadata service API

<Callout icon="ℹ️" theme="info">
  If you have resources in your AWS cloud in any regions for which STS is not active by default, for example, `ap-east-1` or `eu-south-1`), ensure that you activate those regions following the Amazon [Managing AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) guide.
</Callout>

# Connect AWS Account

## Add AWS Connection

<Callout icon="ℹ️" theme="info">
  You must have the necessary permissions to add new Connections to the CloudZero platform.
</Callout>

To start, open the CloudZero Integrations page by using the the gear icon on the top navigation bar and selecting **Cloud Integrations**, or by using the link to the page:  [https://app.cloudzero.com/organization/connections](https://app.cloudzero.com/organization/connections).

The Cloud Integrations page displays all of the Integrations in your system. To connect an AWS Account, click the **Add Connection** button.

On the next page, click the **AWS** tile and, to manually connect an AWS Member Account, click the **Manual - Resources** button in the three options for connecting accounts .

<Callout icon="ℹ️" theme="info">
  You must create an AWS cross-account access role. Refer to the information box where the system has generated all of the necessary policy details you must provide in the AWS Console.
</Callout>

## Connect Account with CloudZero

When your policy is generated and applied to the role, you must enter the information you collected from the AWS Console.

1. Enter a **Connection Name**. This is the name you will see throughout the CloudZero UI, in addition to the AWS Account ID. The name must conform to AWS naming conventions: lowercase, dashes, without spaces or periods.
2. Enter the **Cross-Account IAM Role ARN**.
3. Click **Save**.

## Confirm on Cloud Integrations page

AWS generally takes ~5 minutes to deploy the necessary permissions to allow CloudZero to pull in the information it needs. AWS cost and usage data will typically appear in CloudZero within 24 hours of the integration being configured.

When the connection is complete, an AWS Connection appears on the CloudZero Cloud Integrations page in the **Resource Connections** table.

<Image alt="Resource Connections table" border={false} src="https://downloads.cloudzero.com/documentation/resources/billing-resource-tables.png" />

The **Health** column will be green or red and show the overall connection health. If something changes on your side and CloudZero can no longer use the role that was just granted permissions, the **Health** will change and provide details on why CloudZero cannot connect.

You can connect any other AWS Accounts you want at this point  using the same process.
