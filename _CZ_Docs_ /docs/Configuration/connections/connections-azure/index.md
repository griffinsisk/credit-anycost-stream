---
title: Connecting to Azure
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-azure
updatedAt: '2021-11-30T17:29:59.987Z'
---
# How the Azure Connection works

Connecting CloudZero to an Azure account shows Azure cost data alongside other Cost Sources in the Explorer and enables anomaly alerts on Azure spend.

Depending on the [Azure account type](#how-to-connect-to-supported-azure-agreement-types) and billing scope, this includes the following data:

* Daily and monthly usage data
* Billing data
* Data from invoices and balances, including taxes and discounts applied

You connect CloudZero to Azure by enabling the CloudZero multi-tenant service principal in your tenant and granting it read-only access to the Azure Cost Management and Billing APIs.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's Azure permissions are read-only.
  CloudZero has no access to read data except where explicitly authorized. For example, the Billing Reader role grants CloudZero permission to read usage and billing data for a specific subscription, but not to query resource configurations.
</Callout>

# How to connect to supported Azure agreement types

Microsoft Azure accounts can have different agreement types that affect how usage and billing data can be collected.

To get started with an Azure Connection, select your agreement type from the following list:

* [Microsoft Customer Agreement (MCA)](/docs/connections-azure-mca)
* [Enterprise Agreement (EA)](/docs/connections-azure-ea)
* [Cloud Solution Provider (CSP)](/docs/connections-azure-csp)

Accounts obtained through other agreements, such as the Microsoft Online Services Program or other MSDN-based agreements, do not support exporting usage data and cannot be connected to CloudZero.

To check which agreement type you have, follow these steps. For more details, see the [Azure documentation](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts#check-the-type-of-your-account).

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Open **Cost Management + Billing** from the search bar or the left navigation.
3. If you have access to only one billing scope, select **Properties** from the left navigation. The **Type** value on the **Properties** pane determines the type of your account.
4. If you have access to multiple billing scopes, select **Billing scopes** from the left navigation, and then check the type in the **Billing account type** column.

# How to migrate Microsoft EA to Microsoft MCA

There may be situations in which your organization moves from Microsoft Enterprise Agreement (EA) to a Microsoft Customer Agreement (MCA). To achieve a clean migration of your Connections and maintain data continuity within CloudZero, follow these steps.

1. Add the new Microsoft Customer Agreement (MCA) account as a net new Connection by following the steps on the page [Connecting to an Azure MCA Account](/docs/connections-azure-mca).
2. Navigate to **Settings** > **Cloud Integrations** and pause the existing Enterprise Agreement (EA) connection.

After you pause the EA connection, data will begin to flow in over the new MCA connection instead of the EA connection.

It is critical to pause, not delete, this Connection in order to maintain historical data in CloudZero. If the Enterprise Agreement is deleted, you will lose access to all data associated with that Connection.

If you did not pause the EA Connection earlier, it will begin to display an Error state as your account migrates over to the MCA. It is still critical to not delete the EA Connection despite this error, as doing so will cause you to lose all historical data for that Connection.
