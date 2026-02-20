---
title: SSO with OpenID Connect
category: getting-started
createdAt: '2023-03-02T17:17:39.701Z'
hidden: false
slug: how-to-connect-openid-connect
updatedAt: '2024-12-13T14:49:24.924Z'
---
CloudZero supports single-sign on (SSO) for any OpenID Connect (OIDC) application, including GCP. This enables users to seamlessly log in to CloudZero from their IdP, without needing to enter a CloudZero username and password.

To set up a new SSO integration for CloudZero using an OIDC application, complete the following steps:

1. [Create a new OIDC Application in your IdP.](#step-1-create-a-new-oidc-application-in-your-idp)
2. [Configure the OIDC SSO Integration in CloudZero.](#step-2-configure-the-oidc-sso-integration-in-cloudzero)
3. [Complete the OIDC configuration in your IdP.](#step-3-complete-the-oidc-configuration-in-your-idp)

# Step 1: Create a new OIDC Application in your IdP

1. Create a new OIDC Single-Page Application in your identity provider (IdP).

2. Select
   * **Implicit (Hybrid)**
   * **PKCE Required**
   * **Redirect URI**: `https://auth.cloudzero.com/login/callback`

3. Assign at least these **Scopes**:
   * `openid`
   * `email`
   * `profile`

4. Ensure that the `"email_verified"` attribute is set to `"true"`. Note that this is the default for many IdPs, but not for all.

5. Copy the **Client ID** your IdP generates for you.

6. Keep the OIDC application settings page open so you can finish configuring it in a later step.

# Step 2: Configure the OIDC SSO Integration in CloudZero

1. Log in to CloudZero and navigate to [**Settings** > **SSO Integrations**](https://app.cloudzero.com/settings/sso-integrations).

2. Select the **Create New Integration** button:

   <Image align="center" alt="Select the Create New Integration button on the SSO Integrations page" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-integrations-page-create-new-integration.png" />

3. On the **Select Your Identity Provider** page, select **Other**:

   <Image align="center" alt="Select Other to set up an SSO integration in CloudZero" className="border" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/sso-select-idp-oidc-1.png" />

4. When the **Connect Other to CloudZero** form opens, complete the fields according to the instructions that follow the image:

   <Image align="center" alt="The Connect Other to CloudZero form" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connect-oidc.png" />

5. The **IdP Callback URL** field displays the callback URL. Because you entered this URL into your OIDC application's **Redirect URI** field in a previous step, you can proceed to the next field.

6. Enter the **Email Domain**. Users with an email address from this domain will be forwarded to your SSO integration to log in to CloudZero.

7. Enter the **Issuer**. This is your OIDC Discovery Endpoint (for example, `https://your-idp/.well-known/openid-configuration`).

8. Paste the client ID you copied from your IdP into the **Client ID** field.

9. Select **Create Integration**. CloudZero creates the SSO Integration and reloads the page to display the integration details.

   <Image align="center" alt="Your new OIDC integration's details page" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-oidc-integration-details.png" />

10. Select the **Open Test Window** button to open a new browser tab to test the integration by logging in to your IdP:

    <Image align="center" alt="Select the Open Test Window button to test your SSO integration" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connection-details-open-test-window.png" />

11. In the new tab, authorize CloudZero's request to connect to your account.

12. When the test is successful, the tab closes, and the integration details page in CloudZero displays a modal with the message **Connection test successful!** Select **Close** to close the modal.

13. In the **SSO Connection Status and Controls** section, check the **Enable log-ins with my SSO** box.

14. Optionally, check the **Enable SSO for Groups** box to allow your IdP to manage your groups. See [Manage Groups with SSO](/docs/how-to-manage-groups-via-sso) for more information.

    <Image align="center" alt="Check the necessary boxes before activating your SSO integration" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-connection-status-and-controls.png" />

15. Select **Enable**.

    <Callout icon="⚠️" theme="warn">
      Selecting **Enable** will immediately activate the SSO integration. If you need to disable this integration, email the team at [support@cloudzero.com](mailto:support@cloudzero.com).
    </Callout>

16. Scroll back up to the **General Configuration** section and copy the **Bookmark URL**. It will follow this format: `https://app.cloudzero.com?connection=<your-connection-name>`

    <Image align="center" alt="Copy the Bookmark URL from the CloudZero UI" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-application-bookmark-url-2.png" />

## Step 3: Complete the OIDC configuration in your IdP

1. Return to your IdP's OIDC application settings and paste the bookmark URL you copied into the **Bookmark URL** field, which may also be called the **Initiate Login URL** field or the **Website URL** field, depending on your IdP.

2. Save your IdP settings.

Users can now log in to CloudZero through your IdP.
