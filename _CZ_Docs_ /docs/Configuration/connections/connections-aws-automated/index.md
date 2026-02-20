---
title: Connecting to AWS
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-aws-automated
updatedAt: '2021-11-30T17:29:59.987Z'
---
<Callout icon="✅" theme="okay">
  The policy templates the CloudZero access role will use for either a payer or a resource account connection are in this repository: [https://github.com/Cloudzero/provision-account/tree/develop/policies](https://github.com/Cloudzero/provision-account/tree/develop/policies).
</Callout>

# How the AWS Connection Works

Connecting to an AWS account will show AWS cost data alongside other Cost Sources in the Explorer, as well as enable anomaly alerts on AWS spend.

CloudZero access to your AWS accounts uses a delegated access role from the CloudZero AWS account (#061190967865) to yours, with read-only permissions designed to limit access to only those parts of the system CloudZero needs for operation.

<Callout icon="ℹ️" theme="info">
  All CloudZero access to your AWS accounts is read-only and requires the minimum permissions to access cost, usage data, and surrounding metadata to help you understand what drives spend. CloudZero has no access to data except where explicitly authorized, for example, the S3 bucket where your cost and usage report is stored.

  By using metadata on how your AWS environment is operating, the services that you are using, and how they are being used, CloudZero can boost tag coverage, identify more complex anomalies, and highlight the specific resources and changes that are responsible for cost changes in your environment.
</Callout>

The following summarizes the CloudZero Permissions:

* Management Account access is required:
  * Cost and Usage, Billing, and Organizations API
  * Cost and Usage S3 bucket where reports are stored
  * CloudWatch Metrics and read-only access to the metadata service APIs
* Resource (member) Account access is optional, required for waste and root cause analysis:
  * CloudWatch Metrics
  * Read-only access to the metadata service APIs

When you grant resource (member) level access, CloudZero can display additional key metadata usage as tags and resource-specific usage data alongside each resource in both the Explorer and Optimize features. This adds additional context and visibility for you to use while analyzing spend data in CloudZero.

<Callout icon="ℹ️" theme="info">
  If you have resources in your AWS cloud in any regions for which STS is not active by default, for example, `ap-east-1` or `eu-south-1`, ensure that you activate those regions, following the instructions in the [Managing AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) guide.
</Callout>

CloudZero uses CloudFormation to automate the provisioning process, and the CloudZero CloudFormation templates and IAM policies are open source and available for review at [https://github.com/Cloudzero/provision-account/tree/develop/policies](https://github.com/Cloudzero/provision-account/tree/develop/policies).

# Prerequisites for AWS Connection

You must configure the following AWS services before connecting to CloudZero:

* Required: [AWS Organizations with consolidated billing enabled](https://aws.amazon.com/organizations/)
* Required: [AWS Cost and Usage Report enabled within your AWS Management account ](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/)(sometimes also called your AWS Payer account)
* Highly recommended: [Cost Allocation Tagging Configuration](/docs/cost)

In addition, CloudZero has requirements for [valid Cost and Usage Reports](/docs/validate-your-cost-and-usage-report).

# Connect an AWS Account

<Callout icon="✅" theme="okay">
  CloudZero strongly recommends that you connect your AWS Management Account before connecting other AWS accounts. This allows CloudZero to retrieve your billing data.
</Callout>

You must be a CloudZero Admin to add new Connections to the platform.

CloudZero fully supports organizations with multiple Management Accounts. Connect them all to get a consolidated view of your spending.

## Add AWS Connection

1. To start, open the CloudZero Integrations page by using the the gear icon on the top navigation bar and selecting **Cloud Integrations**, or by using the link to the page:  [https://app.cloudzero.com/organization/connections](https://app.cloudzero.com/organization/connections).
2. On the Cloud Integrations page, you can see all of the Integrations in your system. To connect an AWS Account, click the **Add Connection** button.
3. On the next page, click the **AWS** tile and choose how you would like to connect your AWS Account. The options are as follows:

* **Automated- Billing**: CloudZero highly recommends this option. Deploy from the AWS Console using the CloudZero CloudFormation template to connect either a Billing Connection or a Resource Connection.
* **Automated - Resources**: Create multiple Resource Connections by connecting to each individual AWS Member Account within the AWS Organization.
* **Manual - Billing**: Create a Billing Connection by [following the manual instructions](connections-aws-manual-billing) to connect an AWS Management/Payer Account.
* **Manual - Resources**: Create a Resource Connection by [following the manual instructions](connections-aws-manual-resource) to connect an individual AWS Member Account.

The Automated method is the easiest, and the steps to use it follow.

## Connect using the AWS Console

1. Enter a **Connection Name**. This is the name you will see throughout the CloudZero UI, in addition to the AWS Account ID.
   The name must conform to AWS naming conventions: lowercase, dashes, without spaces or periods.
2. Click **Save & Connect** to launch the AWS console. You will be automatically redirected to the AWS Console.
3. Ensure that you are logged in to the correct AWS account. You can open a new tab and log in to the AWS console if necessary.

## Create Stack

Scroll to the bottom of the page, check the two boxes in the **Capabilities** section, and then click **Create stack**.
![](https://files.readme.io/ac8f05b-AWS_capbilities_screenshot.png)

## Confirm Connection

AWS generally takes ~5 minutes to deploy the necessary permissions to allow CloudZero to pull in the information it needs. AWS cost and usage data will typically appear in CloudZero within 24 hours of the integration being configured.

When the process is complete, an AWS Connection will appear on the CloudZero Cloud Integrations page. Any Management and Payer Accounts, where CloudZero retrieves Billing data, will appear at the top of the page in the **Billing Connections** table. Any Member Accounts, where CloudZero retrieves additional information about your Resources, will appear at the bottom of the page in the **AWS Resource Connections** table.

<Image align="center" alt="Billing Connections and AWS Resource Connections tables" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/billing-resource-tables.png" />

The **Health** column will be green or red and show the overall connection health. If something changes on your side and CloudZero can no longer use the role that was just granted permissions, the **Health** will change and provide details on why CloudZero cannot connect.

You can connect any other AWS Accounts you want at this point using the same process.
