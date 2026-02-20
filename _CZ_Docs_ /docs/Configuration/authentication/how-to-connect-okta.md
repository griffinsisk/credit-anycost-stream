---
title: SSO with Okta
category: getting-started
createdAt: '2023-03-02T17:17:39.701Z'
hidden: false
slug: how-to-connect-okta
updatedAt: '2024-12-13T14:49:24.924Z'
---
CloudZero supports single-sign on (SSO) for Okta. This enables users to seamlessly log in to CloudZero from an Okta tile, without needing to enter a CloudZero username and password.

To set up a new SSO integration for CloudZero using Okta, complete the following steps:

1. [Create a new Okta application.](#step-1-create-a-new-okta-application)
2. [Configure the Okta SSO Integration in CloudZero.](#step-2-configure-the-okta-sso-integration-in-cloudzero)
3. [Complete the configuration in Okta.](#step-3-complete-the-configuration-in-okta)

# Step 1: Create a new Okta application

1. Log in to [Okta](https://www.okta.com) and navigate to **Admin Console** > **Applications** > **Applications**.

2. Select **Create App Integration**.

3. Select **OIDC - OpenID Connect** as the **Sign-in method**.

4. Select **Single-Page Application**.

5. Click **Next**.

6. Enter a name in the **App integration name** field, such as `CloudZero`.

7. Optionally, upload a logo to the **Logo** field. [Download the CloudZero logo here.](https://downloads.cloudzero.com/documentation/resources/cloudzero-sso-logo.png)

8. In the **Grant type** field, select **Advanced**, and then check the box for **Implicit (hybrid)**.

9. In the **Sign-in redirect URIs** field, enter `https://auth.cloudzero.com/login/callback`

10. Click **Save** to create the app integration, then select **Edit** to configure additional options.

11. In the **General** tab, ensure the **Proof Key for Code Exchange (PKCE)** box is checked in the **Client Credentials** section.

12. Copy the **Client ID**.

13. Keep the Okta settings page open so you can finish configuring it in a later step.

<Image align="center" alt="Confirm the PKCE box is checked in Okta" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/okta-sso-copy-client-credentials.png" />

# Step 2: Configure the Okta SSO Integration in CloudZero

1. Log in to CloudZero and navigate to [**Settings** > **SSO Integrations**](https://app.cloudzero.com/settings/sso-integrations).

2. Click the **Create New Integration** button:

   <Image align="center" alt="Click the Create New Integration button on the SSO Integrations page" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-integrations-page-create-new-integration.png" />

3. On the **Select Your Identity Provider** page, select **Okta**:

   <Image align="center" alt="Select Okta to set up an SSO integration in CloudZero" className="border" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/sso-select-idp-okta-1.png" />

4. CloudZero displays the **Connect Okta to CloudZero** form:

   <Image align="center" alt="The Connect Okta to CloudZero form" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connect-okta.png" />

5. The **IdP Callback URL** field displays the callback URL. Because you entered this URL into your Okta application's **Sign-in redirect URIs** field in a previous step, you can proceed to the next field.

6. Enter the **Email Domain**. Users with an email address from this domain will be forwarded to your Okta integration to log in to CloudZero.

7. Enter the **Issuer**. This is your OIDC Discovery Endpoint (for example, `https://example.okta.com/.well-known/openid-configuration`). See [Okta's documentation](https://developer.okta.com/docs/reference/api/oidc/#well-known-openid-configuration) for more information.

8. Paste the client ID you copied from Okta into the **Client ID** field.

9. Select **Create Integration**.
   CloudZero creates the SSO integration and reloads the page to display the integration details.

   <Image align="center" alt="Your new Okta integration's details page" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-okta-integration-details.png" />

10. Select the **Open Test Window** button to open a new browser tab to test the integration by logging in to your IdP:

    <Image align="center" alt="Select the Open Test Window button to test your SSO integration" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connection-details-open-test-window.png" />

11. In the new tab, authorize CloudZero's request to connect to your account.

12. When the test is successful, the tab closes, and the integration details page in CloudZero displays a modal with the message **Connection test successful!**.  Select **Close** to close the modal.

13. In the **SSO Connection Status and Controls** section, check the **Enable log-ins with my SSO** box.

14. Optionally, check the **Enable SSO for Groups** box to allow your IdP to manage your groups. See [Manage Groups with SSO](/docs/how-to-manage-groups-via-sso) for more information.

    <Image align="center" alt="Check the necessary boxes before activating your SSO integration" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connection-status-and-controls.png" />

15. Select **Enable**.

    <Callout icon="⚠️" theme="warn">
      Selecting **Enable** will immediately activate the SSO integration. If you need to disable this integration, email the team at [support@cloudzero.com](mailto:support@cloudzero.com).
    </Callout>

16. Scroll back up to the **General Configuration** section and copy the **Bookmark URL**. It will follow this format: `https://app.cloudzero.com?connection=<your-connection-name>`

    <Image align="center" alt="Copy the Bookmark URL from the CloudZero UI" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-application-bookmark-url-2.png" />

# Step 3: Complete the Configuration in Okta

1. **In Okta**, return to the application settings page and paste the bookmark URL you copied into the **Initiate login URI** field, which is in the **LOGIN** section of the **General** tab.

   <Image align="center" alt="Paste the Bookmark URL into the Initiate login URI field" className="border" border={true} width="500px" src="https://downloads.cloudzero.com/documentation/resources/okta-initiate-login-uri.png" />

2. Select **Save** in Okta.

Users can now log in to CloudZero by selecting the applicable tile in their Okta dashboard.
