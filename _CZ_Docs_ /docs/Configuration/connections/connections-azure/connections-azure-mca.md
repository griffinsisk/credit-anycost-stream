---
title: Connecting to an Azure MCA Account
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-azure-mca
updatedAt: '2024-08-14T17:29:59.987Z'
---
To connect CloudZero to an Azure [**Microsoft Customer Agreement (MCA)**](https://www.microsoft.com/en-us/licensing/how-to-buy/microsoft-customer-agreement) account, you must enable the CloudZero multi-tenant service principal in your tenant and grant it read-only permissions to Azure's APIs.

# MCA Account Billing Scopes and Permissions

Connections to MCA accounts can be made at different [billing scopes](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes#microsoft-customer-agreement-scopes). The billing scope determines the type of usage and billing data that can be collected, and which subscriptions and Azure Marketplace purchases are included in that data. Each scope requires a different read-only role.

| Scope           | Data types                       | Data source                                                                 | Role                                                                                                                                                       |
| --------------- | -------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Billing account | Usage, billing, and invoice data | Subscriptions and Marketplace purchases associated with the billing account | [Billing Account Reader role](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-mca-roles#billing-account-roles-and-tasks) |
| Billing profile | Usage, billing, and invoice data | Subscriptions and Marketplace purchases associated with the billing profile | [Billing Profile Reader role](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-mca-roles#billing-profile-roles-and-tasks) |
| Invoice section | Usage and billing data           | Subscriptions and Marketplace purchases associated with the invoice section | [Invoice Section Reader role](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-mca-roles#invoice-section-roles-and-tasks) |
| Subscription    | Usage and billing data           | The connected subscription and Marketplace purchases associated with it     | [Billing Reader role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/management-and-governance#billing-reader)           |

Note that the invoice section and subscription scopes do not enable the collection of invoice data, such as taxes and fees. In addition, Marketplace purchases not directly tied to the subscriptions in the invoice section (for the invoice section scope) or to the selected subscription (for the subscription scope) cannot be collected.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's Azure permissions are read-only.

  CloudZero has no access to read data except where explicitly authorized. For example, the Billing Account Reader role grants CloudZero permission to read usage and billing data for a billing account, but not to query resource configurations.
</Callout>

# Connect an Azure MCA Account Billing Scope

## Prerequisites

* In CloudZero, you must have the necessary permissions to create a new connection.
* In Azure, you must have the Owner role on the billing scope you plan to connect so you can assign permissions to the service principal.

To connect an Azure MCA account billing scope to CloudZero, complete the following steps:

1. [Retrieve IDs from Azure.](#step-1-retrieve-ids-from-azure)
2. [Configure the connection in CloudZero.](#step-2-configure-the-connection-in-cloudzero)
3. [Authorize the CloudZero service principal in Azure.](#step-3-authorize-cloudzero-service-principal-in-azure)
4. [Grant the service principal access to the Azure Billing API.](#step-4-grant-access-to-the-azure-billing-api)
5. [View the Azure connection details in CloudZero.](#step-5-view-the-azure-connection-in-cloudzero)

## Step 1: Retrieve IDs from Azure

First, you must retrieve your Azure tenant ID and the ID for the billing scope you intend to connect.

**To locate the tenant ID:**

1. Log in to the Azure Portal and navigate to [Microsoft Entra ID](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) (formerly Azure Active Directory).
2. Copy the **Tenant ID** for use in [the next step](#step-2-configure-the-connection-in-cloudzero).

<Image align="center" alt="Copy your Tenant ID in the Azure Portal" border={true} width="600px" src="https://downloads.cloudzero.com/documentation/resources/connect-azure-tenant-id.png" className="border" />

**To locate a billing account, billing profile, or invoice section ID:**

1. Navigate to [Cost Management + Billing](https://portal.azure.com/#view/Microsoft_Azure_GTM/ModernBillingMenuBlade/~/BillingAccounts) and select the billing scope you plan to connect.
2. In the left menu, under **Settings**, select **Properties**.
3. Copy the account, profile, or invoice section **ID** for use in [the next step](#step-2-configure-the-connection-in-cloudzero).

For example, the following image shows where to find a billing account ID:

<Image align="center" alt="Example of a Billing Account ID in the Azure Portal" border={true} src="https://files.readme.io/9e1ee0e-Screen_Shot_2022-09-09_at_10.03.34_AM.png" className="border" />

**To locate a subscription ID:**

1. Navigate to [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV2) and select the subscription you plan to connect.
2. In the **Overview**, copy the **Subscription ID** for use in [the next step](#step-2-configure-the-connection-in-cloudzero).

<Image align="center" alt="Example of a Subscription ID in the Azure Portal" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/connect-azure-subscription-id.png" className="border" />

## Step 2: Configure the Connection in CloudZero

1. In CloudZero, navigate to **[Settings](https://app.cloudzero.com/settings/overview)** and from the left navigation, select **Cloud Integrations**.
2. Click the **Add Connection** button.
3. Enter a **Connection Name**. This is the name you will see alongside the Azure billing scope ID in the CloudZero UI. It cannot contain spaces, periods, or special characters (except for hyphens and underscores).
4. Select **Microsoft Customer Agreement** from the **Azure Agreement Type** drop-down menu.
5. Paste the tenant ID you copied in [Step 1](#step-1-retrieve-ids-from-azure) into the **Tenant ID** field.
6. Paste the billing account, billing profile, invoice section, or subscription ID you copied in [Step 1](#step-1-retrieve-ids-from-azure) into the **Billing Account ID** field.
7. Select **Continue**.

## Step 3: Authorize CloudZero Service Principal in Azure

If you have not connected the selected tenant to CloudZero before, CloudZero redirects you to Azure and asks you for permission to create the **CloudZeroPlatform** [service principal](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser#service-principal-object) in your tenant.

If you have already granted CloudZero this consent, proceed to [Step 4: Grant Access to the Azure Billing API](#step-4-grant-access-to-the-azure-billing-api).

1. In Azure, check the **Consent on behalf of your organization** box.
2. Select **Accept**.

<Image align="center" alt="Azure Permission Dialog" border={true} src="https://files.readme.io/daad5a9-azure-security-prompt-cz.png" className="border" />

Azure starts the process of creating the service principal in your tenant and redirects you to CloudZero.

<Callout icon="ℹ️" theme="info">
  Note that it can take an hour or more for Azure to complete creating the service principal.
</Callout>

## Step 4: Grant Access to the Azure Billing API

<Callout icon="ℹ️" theme="info">
  A faster method is to use the [PowerShell script](https://github.com/Cloudzero/provision-account/blob/develop/azure/cz_azure_billing_permissions_setup.ps1) to grant the CloudZero service principal access to the Azure Billing API. After running the script, proceed to [Step 5](#step-5-view-the-azure-connection-in-cloudzero).
</Callout>

The CloudZero service principal requires read permissions to access Azure's Cost Management & Billing APIs. This allows CloudZero to generate usage reports, read invoices to determine the taxes assessed when possible, and retrieve other billing-related information, including discounts and balances.

You must have the ownership role on the selected billing scope to assign reader permissions to the CloudZero service principal.

1. In the Azure Portal, select the billing scope you have connected to CloudZero.

   * **Subscription scope:** Navigate to [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV2) and select the subscription.
   * **All other scopes:** Navigate to [Cost Management + Billing](https://portal.azure.com/#view/Microsoft_Azure_GTM/ModernBillingMenuBlade/~/BillingAccounts) and select the billing scope.

2. Select **Access control (IAM)**.

3. Select **Add > Add role assignment**.

4. On the **Role** tab, search for and select the required role for your billing scope:

   * **Billing account:** Billing Account Reader role
   * **Billing profile:** Billing Profile Reader role
   * **Invoice section:** Invoice Section Reader role
   * **Subscription:** Billing Reader role

   For details about the data each role reads, see [MCA Account Billing Scopes and Permissions](#mca-account-billing-scopes-and-permissions).

5. Select **Next**.

6. On the **Members** tab, select **User, group, or service principal**.

7. Click **Select members**.

8. Search for and select the **CloudZeroPlatform** service principal that was created in [Step 3](#step-3-authorize-cloudzero-service-principal-in-azure). Note that it can take an hour or more for Azure to create the service principal, so if you don't see it in the search results, wait a while and try again.

9. Select **Next**.

10. Select **Review + assign** to assign the role.

## Step 5: View the Azure Connection in CloudZero

1. In CloudZero, navigate to [Settings](https://app.cloudzero.com/organization/connections) by selecting the **gear icon** in the top navigation bar.

2. Select the newly created Azure connection in the **Billing Connections** table.

<Image align="center" alt="An example Azure connection in the Billing Connections table in CloudZero" border={true} src="https://downloads.cloudzero.com/documentation/resources/connect-azure-billing-connections.png" className="border" />

On the **Azure Connection Details** page, you can find the following information:

* Status
* Connection Name
* Connection ID
* Tenant ID
* Billing Account ID
* Agreement Type
* Timestamps for connection creation, ingestion, and more

<Image align="center" alt="An example Azure Connection Details page in CloudZero" border={true} src="https://downloads.cloudzero.com/documentation/resources/connect-azure-connection-details.png" className="border" />

After CloudZero has processed the first ingest of billing and/or usage data, the **Status** changes from **Pending Data** to **Healthy**. This can take several hours.

If CloudZero can no longer use the role you assigned it, the **Status** is updated with details about why CloudZero cannot connect.

Note that it can take up to a day to synchronize new accounts before you see cost data in the [Explorer](/docs/explorer).

<Callout icon="ℹ️" theme="info">
  USD is the only supported currency.

  Reach out to your CloudZero representative if your Azure cost is billed in a different currency.
</Callout>
