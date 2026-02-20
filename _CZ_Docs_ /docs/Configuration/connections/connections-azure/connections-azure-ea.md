---
title: Connecting to an Azure EA Account
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-azure-ea
updatedAt: '2024-08-15T17:29:59.987Z'
---
To connect CloudZero to an Azure [**Enterprise Agreement (EA)**](https://www.microsoft.com/en-us/licensing/licensing-programs/enterprise) account, you must enable the CloudZero multi-tenant service principal in your tenant and grant it read-only permissions to Azure's APIs.

# EA Account Permissions

For EA accounts, the CloudZero service principal requires the [EnrollmentReader](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/assign-roles-azure-service-principals#permissions-that-can-be-assigned-to-the-service-principal) role, which grants the following **read-only** permissions:

* View usage and billing data for all accounts, subscriptions, and Marketplace purchases managed through the billing account
* View discounts applied through the EA agreement
* View the Azure Prepayment balance associated with the enrollment

Note that the EA account type does not enable the collection of invoice data, such as taxes and fees.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's Azure permissions are read-only.

  CloudZero has no access to read data except where explicitly authorized. For example, the EnrollmentReader role grants CloudZero permission to read usage and billing data for accounts and subscriptions, but not to query resource configurations.
</Callout>

# Connect an Azure EA Account

## Prerequisites

* In CloudZero, you must have the necessary permissions to create a new connection.
* In Azure, you must have the [Billing Account Owner](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes#enterprise-agreement-scopes) role on the billing account you plan to connect so you can assign permissions to the service principal.

To connect an Azure EA account to CloudZero, complete the following steps:

1. [Retrieve IDs from Azure.](#step-1-retrieve-ids-from-azure)
2. [Configure the connection in CloudZero.](#step-2-configure-the-connection-in-cloudzero)
3. [Authorize the CloudZero service principal in Azure.](#step-3-authorize-cloudzero-service-principal-in-azure)
4. [Grant the service principal access to the Azure Billing API.](#step-4-grant-access-to-the-azure-billing-api)
5. [View the Azure connection details in CloudZero.](#step-5-view-the-azure-connection-in-cloudzero)

## Step 1: Retrieve IDs from Azure

First, you must retrieve your tenant ID and billing account ID from Azure.

**To locate the tenant ID:**

1. Log in to the Azure Portal and navigate to [Microsoft Entra ID](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) (formerly Azure Active Directory).
2. Copy the **Tenant ID** for use in [a later step](#step-2-configure-the-connection-in-cloudzero).

**To locate the billing account ID:**

1. Navigate to [Cost Management + Billing](https://portal.azure.com/#view/Microsoft_Azure_GTM/ModernBillingMenuBlade/~/BillingAccounts) and select the billing account you plan to connect.
2. In the left menu, under **Settings**, select **Properties**.
3. Copy the 8-digit **Billing Account ID** for use in [a later step](#step-2-configure-the-connection-in-cloudzero).

## Step 2: Configure the Connection in CloudZero

1. In CloudZero, navigate to **[Settings](https://app.cloudzero.com/settings/overview)** and from the left navigation, select **Cloud Integrations**.
2. Enter a **Connection Name**. This is the name you will see alongside the Azure billing account ID in the CloudZero UI. It cannot contain spaces, periods, or special characters (except for hyphens and underscores).
3. Select **Enterprise Agreement** from the **Azure Agreement Type** drop-down menu.
4. Paste the tenant ID you copied in [an earlier step](#step-1-retrieve-ids-from-azure) into the **Tenant ID** field.
5. Paste the billing account ID you copied in [an earlier step](#step-1-retrieve-ids-from-azure) into the **Billing Account ID** field.
6. Select **Continue**.

## Step 3: Authorize CloudZero Service Principal in Azure

If you have not connected the selected tenant to CloudZero before, CloudZero redirects you to Azure and asks you for permission to create the **CloudZeroPlatform** [service principal](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser#service-principal-object) in your tenant.

If you have already granted CloudZero this consent, proceed to [Step 4: Grant Access to the Azure Billing API](#step-4-grant-access-to-the-azure-billing-api).

1. In Azure, check the **Consent on behalf of your organization** box.
2. Select **Accept**.

<Image align="center" alt="Azure Permission Dialog" border={false} src="https://files.readme.io/daad5a9-azure-security-prompt-cz.png" />

Azure starts the process of creating the service principal in your tenant and redirects you to CloudZero.

<Callout icon="ℹ️" theme="info">
  Note that it can take an hour or more for Azure to complete creating the service principal.
</Callout>

<Callout icon="✅" theme="okay">
  In some cases, approving the CloudZeroPlatform application through Azure’s Admin Consent Requests results in the following message: `Consent for CloudZeroPlatform was cancelled by user`.

  To resolve this issue, have a user with the Global Administrator role (PIM-enabled) perform [step 2](#step-2-configure-the-connection-in-cloudzero) and [step 3](#step-3-authorize-cloudzero-service-principal-in-azure).
</Callout>

## Step 4: Grant Access to the Azure Billing API

<Callout icon="ℹ️" theme="info">
  A faster method is to use the [PowerShell script](https://github.com/Cloudzero/provision-account/blob/develop/azure/cz_azure_billing_permissions_setup.ps1) to grant the CloudZero service principal access to the Azure Billing API.

  After running the script, proceed to [Step 5](#step-5-view-the-azure-connection-in-cloudzero).
</Callout>

The CloudZero service principal requires read permissions to access Azure's Cost Management & Billing APIs. This allows CloudZero to generate usage reports and retrieve other billing-related information, including discounts and balances.

You must have the billing account owner role on the selected billing account to assign reader permissions to the CloudZero service principal.

Because the [EnrollmentReader](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/assign-roles-azure-service-principals#permissions-that-can-be-assigned-to-the-service-principal) role isn't shown in the Azure Portal, you must use Azure's REST API to assign it to the service principal, as explained in the following steps.

1. In the Azure Portal, navigate to [Enterprise applications](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AppAppsPreview).

2. Select the **CloudZeroPlatform** application.

3. On the **Overview** page, in the **Properties** section, copy the **Object ID** for use in a later step.

<Image align="left" alt="Copy the CloudZeroPlatform Object ID in Azure" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/connect-azure-spn-object-id.png" className="border" />

4. Navigate to the [Role Assignments - Put](https://learn.microsoft.com/en-us/rest/api/billing/role-assignments/put?view=rest-billing-2019-10-01-preview\&tabs=HTTP#code-try-0) article in Azure's documentation. This interactive article allows you to send requests to Azure's REST API.

5. Select the **Try it** button.

<Image align="left" alt="Select the Try It button in the Azure documentation" border={false} width="500px" src="https://downloads.cloudzero.com/documentation/resources/connect-azure-rest-api-try-it.png" />

6. Use your account credentials to sign in to the tenant with the enrollment access that you want to assign. You are redirected to the REST API **Try it** form.

7. In the **Parameters** section, enter the following parameters:

   * `billingAccountName`: Use the 8-digit billing account ID you copied in [Step 1](#step-1-retrieve-ids-from-azure).
   * `billingRoleAssignmentName`: Generate a GUID using the [Online GUID/UUID Generator](https://guidgenerator.com/) and enter it in this field.
   * `api-version`: Use the `2019-10-01-preview` version.

8. Copy the following request body and paste it into the **Body** section, replacing these parameters:

   * `{YOUR-OBJECT-ID}`: Use the CloudZeroPlatform object ID you copied earlier in this step.
   * `{YOUR-TENANT-ID}`: Use the tenant ID you copied in [Step 1](#step-1-retrieve-ids-from-azure).
   * `{YOUR-BILLING-ACCOUNT-ID}`: Use the 8-digit billing account ID you copied in [Step 1](#step-1-retrieve-ids-from-azure). This is the same `billingAccountName` you entered in the **Parameters** section.

   ```json
   {
     "properties": {
       "principalId": "{YOUR-OBJECT-ID}",
       "principalTenantId": "{YOUR-TENANT-ID}",
       "roleDefinitionId": "/providers/Microsoft.Billing/billingAccounts/{YOUR-BILLING-ACCOUNT-ID}/billingRoleDefinitions/24f8edb6-1668-4659-b5e2-40bb5f3a7d7e"
     }
   }
   ```

   Note that `24f8edb6-1668-4659-b5e2-40bb5f3a7d7e` is the billing role definition ID for the [EnrollmentReader](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/assign-roles-azure-service-principals#permissions-that-can-be-assigned-to-the-service-principal) role.

9. Ensure that the **Request Preview** shows the following URL, with `{billingAccountName}` and `{billingRoleAssignmentName}` set to your own values: `https://management.azure.com/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName}?api-version=2019-10-01-preview`

<Image align="left" alt="Example REST API request using the interactive Azure documentation" border={true} width="500px" src="https://downloads.cloudzero.com/documentation/resources/connect-azure-rest-api-try-it-example.png" className="border" />

10. Select **Run**. You should see a `200 OK` response, which indicates that the role was successfully added to the service principal.

If you receive an error, see Azure's [troubleshooting](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/assign-roles-azure-service-principals#troubleshoot) documentation.

## Step 5: View the Azure Connection in CloudZero

1. In CloudZero, navigate to [Settings](https://app.cloudzero.com/organization/connections) by selecting the **gear icon** in the top navigation bar.

2. Select the newly created Azure connection in the **Billing Connections** table.

<Image alt="An example Azure connection in the Billing Connections table in CloudZero" border={false} src="https://downloads.cloudzero.com/documentation/resources/connect-azure-billing-connections.png" />

On the **Azure Connection Details** page, you can find the following information:

* Status
* Connection Name
* Connection ID
* Tenant ID
* Billing Account ID
* Agreement Type
* Timestamps for connection creation, ingestion, and more

The following image shows an example [Azure MCA connection](/docs/connections-azure-mca), but your EA connection will look similar:

<Image align="center" alt="An example Azure Connection Details page in CloudZero" border={true} src="https://downloads.cloudzero.com/documentation/resources/connect-azure-connection-details.png" className="border" />

After CloudZero has processed the first ingest of billing and/or usage data, the **Status** changes from **Pending Data** to **Healthy**. This can take several hours.

If CloudZero can no longer use the role you assigned it, the **Status** is updated with details about why CloudZero cannot connect.

Note that it can take up to a day to synchronize new accounts before you see cost data in the [Explorer](/docs/explorer).

<Callout icon="ℹ️" theme="info">
  USD is the only supported currency.

  Reach out to your CloudZero representative if your Azure cost is billed in a different currency.
</Callout>
