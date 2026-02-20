---
title: Connecting to an Azure CSP Account
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-azure-csp
updatedAt: '2021-11-30T17:29:59.987Z'
---
To connect CloudZero to an Azure subscription acquired through a [**Cloud Solution Provider (CSP)**](https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0145p) agreement, you must enable the CloudZero multi-tenant service principal in your tenant and grant it read-only permissions to Azure's APIs.

# CSP Subscription Permissions

For CSP subscriptions, the CloudZero service principal requires the [Billing Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/management-and-governance#billing-reader) role, which grants **read-only** permission to view usage and billing data for a single subscription and any Marketplace purchases directly associated with it.

Note that the CSP agreement type does not enable the collection of invoice data, such as taxes and fees. Additionally, Marketplace purchases that are not directly tied to the subscription cannot be collected.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's Azure permissions are read-only.

  CloudZero has no access to read data except where explicitly authorized. For example, the Billing Reader role grants CloudZero permission to read usage and billing data for a specific subscription, but not to query resource configurations.
</Callout>

You need to create the CloudZero service principal only once per tenant. However, if you have multiple subscriptions obtained through a CSP agreement, you must create a separate CloudZero connection for each subscription you plan to connect. You must also assign the service principal roles that grant access to each subscription.

# Connect an Azure CSP Subscription

## Prerequisites

* In CloudZero, you must have the necessary permissions to create a new connection.
* In Azure, you must have the Owner role on the subscription you plan to connect so you can assign permissions to the service principal.

To connect an Azure CSP subscription to CloudZero, complete the following steps:

1. [Retrieve IDs from Azure.](#step-1-retrieve-ids-from-azure)
2. [Configure the connection in CloudZero.](#step-2-configure-the-connection-in-cloudzero)
3. [Authorize the CloudZero service principal in Azure.](#step-3-authorize-cloudzero-service-principal-in-azure)
4. [Grant the service principal access to the Azure Billing API.](#step-4-grant-access-to-the-azure-billing-api)
5. [View the Azure connection details in CloudZero.](#step-5-view-the-azure-connection-in-cloudzero)

## Step 1: Retrieve IDs from Azure

First, you must retrieve your tenant ID and subscription ID from Azure.

**To locate the tenant ID:**

1. Log in to the Azure Portal and navigate to [Microsoft Entra ID](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) (formerly Azure Active Directory).
2. Copy the **Tenant ID** for use in [the next step](#step-2-configure-the-connection-in-cloudzero).

<Image align="center" alt="Copy your Tenant ID in the Azure Portal" border={true} width="500px" src="https://downloads.cloudzero.com/documentation/resources/connect-azure-tenant-id.png" className="border" />

**To locate the subscription ID:**

1. Navigate to [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV2) and select the subscription you plan to connect.
2. In the **Overview**, copy the **Subscription ID** for use in [the next step](#step-2-configure-the-connection-in-cloudzero).

<Image align="center" alt="Example of a Subscription ID in the Azure Portal" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/connect-azure-subscription-id.png" className="border" />

## Step 2: Configure the Connection in CloudZero

1. In CloudZero, navigate to **[Settings](https://app.cloudzero.com/settings/overview)** and from the left navigation, select **Cloud Integrations**.
2. Click the **Add Connection** button.
3. Enter a **Connection Name**. This is the name you will see alongside the Azure subscription ID in the CloudZero UI. It cannot contain spaces, periods, or special characters (except for hyphens and underscores).
4. Select **Cloud Solution Provider** from the **Azure Agreement Type** drop-down menu.
5. Paste the tenant ID you copied in [Step 1](#step-1-retrieve-ids-from-azure) into the **Tenant ID** field.
6. Paste the subscription ID you copied in [Step 1](#step-1-retrieve-ids-from-azure) into the **Billing Account ID** field.
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

The CloudZero service principal requires read permissions to access Azure's Cost Management & Billing APIs. This allows CloudZero to generate usage reports and retrieve other billing-related information.

You must have the ownership role on the selected subscription to assign reader permissions to the CloudZero service principal.

1. In the Azure Portal, navigate to [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV2) and select the subscription you have connected to CloudZero.

2. Select **Access control (IAM)**.

3. Select **Add > Add role assignment**.

4. On the **Role** tab, search for and select the **Billing reader** role.

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

The following image shows an example [Azure MCA connection](/docs/connections-azure-mca), but your CSP connection will look similar:

<Image align="center" alt="An example Azure Connection Details page in CloudZero" border={true} src="https://downloads.cloudzero.com/documentation/resources/connect-azure-connection-details.png" className="border" />

After CloudZero has processed the first ingest of billing and/or usage data, the **Status** changes from **Pending Data** to **Healthy**. This can take several hours.

If CloudZero can no longer use the role you assigned it, the **Status** is updated with details about why CloudZero cannot connect.

Note that it can take up to a day to synchronize new accounts before you see cost data in the [Explorer](/docs/explorer).

<Callout icon="ℹ️" theme="info">
  USD is the only supported currency.

  Reach out to your CloudZero representative if your Azure cost is billed in a different currency.
</Callout>
