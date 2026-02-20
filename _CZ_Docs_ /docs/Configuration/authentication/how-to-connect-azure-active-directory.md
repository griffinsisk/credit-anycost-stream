---
title: SSO with Microsoft Entra ID (Azure AD)
category: getting-started
createdAt: '2023-03-02T17:17:39.701Z'
hidden: false
slug: how-to-connect-azure-active-directory
updatedAt: '2024-12-13T14:49:24.924Z'
---
CloudZero supports single-sign on (SSO) for Microsoft Entra ID (formerly Azure Active Directory). This enables Entra ID users to seamlessly log in to CloudZero without needing to enter a CloudZero username and password.

To set up a new SSO integration for CloudZero using Microsoft Entra ID, complete the following steps:

1. [Retrieve your Entra ID primary domain from Azure.](#step-1-retrieve-your-Entra-ID-primary-domain-from-azure)
2. [Create a new app registration in Azure.](#step-2-create-a-new-app-registration-in-azure)
3. [Create a client secret for the application.](#step-3-create-a-client-secret-for-the-application)
4. [Assign API permissions to the application.](#step-4-assign-api-permissions-to-the-application)
5. [Configure the Entra ID SSO Integration in CloudZero.](#step-5-configure-the-entra-id-sso-integration-in-cloudzero)

As part of these steps, you will gather the following information from Azure:

* Primary domain
* Application (client) ID
* Secret value
* Secret expiration date

# Step 1: Retrieve your Entra ID primary domain from Azure

1. Log in to the [Azure Portal](https://portal.azure.com) and navigate to [Entra ID](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview).

2. Copy the **Primary domain** from your Entra ID overview for use in [configuring the SSO integration in CloudZero](#step-5-configure-the-entra-id-sso-integration-in-cloudzero).

   <Image align="center" alt="Copy your tenant's Primary Domain from Entra ID" className="border" border={true} width="500px" src="https://downloads.cloudzero.com/documentation/resources/azure-ad-sso-primary-domain.png" />

# Step 2: Create a new app registration in Azure

1. In the Azure Portal, navigate to [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade).

2. Select **New registration**.

3. Enter a name in the **Name** field, such as `CloudZero`.

4. In the **Supported account types** section, select **Accounts in this organizational directory only (Single tenant)**.

5. In the **Redirect URI** section, select **Web** from the drop-down menu and enter the following URI: `https://auth.cloudzero.com/login/callback`

6. Select **Register**. Azure creates the app registration.

   <Image align="center" alt="Create the app registration in Azure" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/azure-ad-sso-app-registration.png" />

7. On the **Overview** page for the app you created, copy the **Application (client) ID** for use in [configuring the SSO integration in CloudZero](#step-5-configure-the-entra-id-sso-integration-in-cloudzero).

   <Image align="center" alt="Copy the application (client) ID in Azure" className="border" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/sso-azure-ad-app-id.png" />

# Step 3: Create a client secret for the application

1. In the Azure Portal, on the **Overview** page for the app registration you created, select **Manage > Certificates & secrets**.

2. Select **New client secret**.

3. Enter a description for the client secret.

4. Select an expiration date.

5. Select **Add**.

6. Copy the secret's **Value** (not the secret's ID). Note that the value cannot be displayed again after you leave the page. You will need this value for [configuring the SSO integration in CloudZero](#step-5-configure-the-entra-id-sso-integration-in-cloudzero).

   <Image align="center" alt="Copy the secret value in Azure" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-azure-ad-copy-secret-value.png" />

7. Note the secret's expiration date for use in [configuring the SSO integration in CloudZero](#step-5-configure-the-entra-id-sso-integration-in-cloudzero).

# Step 4: Assign API permissions to the application

1. In the Azure Portal, on the **Overview** page for the app registration, select **Manage > API permissions**.

2. Select **Add a permission**.

3. Select **Microsoft Graph**.

4. Select **Delegated permissions**.

5. In the **Select permissions** search field, search for and select the following permissions:

   * `Directory.Read.All`
   * `User.Read`

6. Select **Add permissions**.

   <Image align="center" alt="Add Directory.Read.All and User.Read permissions to the application" className="border" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/sso-azure-ad-api-perms.png" />

# Step 5: Configure the Entra ID SSO Integration in CloudZero

1. Log in to CloudZero and navigate to [**Settings** > **SSO Integrations**](https://app.cloudzero.com/settings/sso-integrations).

2. Click the **Create New Integration** button:

   <Image align="center" alt="Click the Create New Integration button on the SSO Integrations page" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-integrations-page-create-new-integration.png" />

3. On the **Select Your Identity Provider** page, select **Azure Active Directory**:

   <Image align="center" alt="Select Azure Active Directory to set up an SSO integration in CloudZero" className="border" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/sso-select-idp-azure-ad-1.png" />

4. When the **Connect Azure Active Directory to CloudZero** form opens, complete the fields according to the steps that follow the image:

   <Image align="center" alt="The Connect Azure Active Directory to CloudZero form" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connect-azure-ad.png" />

5. The **IdP Callback URL** field displays the callback URL. Because you entered this URL into your Microsoft Entra ID application's **Redirect URI** field in a previous step, you can proceed to the next field.

6. Enter the **Email Domain**. Users with an email address from this domain will be forwarded to your Microsoft Entra ID integration to log in to CloudZero.

7. Paste the primary domain you copied in [Step 1: Retrieve your Entra ID primary domain from Azure](#/step-1-retrieve-your-entra-id-primary-domain-from-azure) into the **Tenant URL** field. Note that this is the _domain name only_ (such as `example.com`). Do not add `https://www.` to it.

8. Paste the application (client) ID you copied in [Step 2: Create a new app registration in Azure](#/step-2-create-a-new-app-registration-in-azure) into the **Client ID** field.

9. Paste the secret value you copied in [Step 3: Create a client secret for the application](#step-3-create-a-client-secret-for-the-application) into the **Client Secret** field.

10. Enter the expiration date for the secret from [Step 3: Create a client secret for the application](#step-3-create-a-client-secret-for-the-application) into the **Secret Expiration Date** field, using the format `YYYY-mm-dd`.

11. Select **Create Integration**. CloudZero creates the SSO integration and reloads the page to display the integration details.

    <Image align="center" alt="Your new Entra ID integration's details page" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-azure-ad-integration-details.png" />

12. Click the **Open Test Window** button to open a new browser tab to test the integration by logging in to your IdP:

    <Image align="center" alt="Select the Open Test Window button to test your SSO integration" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connection-details-open-test-window.png" />

13. In the new tab, authorize CloudZero's request to connect to your account.

14. When the test is successful, the tab closes, and the integration details page in CloudZero displays a modal with the message **Connection test successful!** Select **Close** to close the modal.

15. In the **SSO Connection Status and Controls** section, check the **Enable log-ins with my SSO** box.

16. Optionally, check the **Enable SSO for Groups** box to allow your IdP to manage your groups. See [Manage Groups with SSO](/docs/how-to-manage-groups-via-sso) for more information.

    <Image align="center" alt="Check the necessary boxes before activating your SSO integration" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connection-status-and-controls.png" />

17. Select **Enable**.

    <Callout icon="⚠️" theme="warn">
      Selecting **Enable** will immediately activate the SSO integration. If you need to disable this integration, email the team at [support@cloudzero.com](mailto:support@cloudzero.com).
    </Callout>

18. Scroll back up to the **General Configuration** section and copy the **Bookmark URL**. It will follow this format: `https://app.cloudzero.com?connection=<your-connection-name>`

    <Image align="center" alt="Copy the Bookmark URL from the CloudZero UI" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-application-bookmark-url-2.png" />

19. Manually create a bookmark in your browser of choice using the Bookmark URL you copied. When you select the bookmark in your browser, you will seamlessly log in to CloudZero.

20. Share the Bookmark URL with other users in your CloudZero organization so they can create their own browser bookmarks to log in to CloudZero.
