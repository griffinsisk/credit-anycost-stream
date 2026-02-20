---
title: SSO with SAML
deprecated: false
hidden: false
metadata:
  robots: index
---
CloudZero supports Single Sign-on (SSO) using SAML 2.0. This enables users to log in to CloudZero from an IdP configured to use SAML-based authentication without needing to enter a CloudZero username and password.

CloudZero uses Just in Time provisioning. As long as a user is granted access to CloudZero in your IdP, the user will be provisioned with an account in CloudZero when they first log in.

To set up a new SSO integration for CloudZero using SAML, follow the steps on this page.

# Open the SAML SSO setup page

1. Navigate to **Settings** > **SSO** **Integrations**.
2. On the SSO integrations page click **Create New Integration**.
3. Select SAML from the list of options provided.

The Connect SAML to CloudZero screen opens.

<Image align="center" alt="Connect SAML to CloudZero" className="border" border={true} src="https://files.readme.io/fde1b664dec114964efd0747783c8d29dc55aba3abb7e4bbc12f09ef3c6fc471-Connecting-to-CloudZero-via-SAML.png" />

This screen contains several important pieces of information:

* **Single Sign on URL**: The Assertion Consumer Service (ACS) URL, the endpoint where your Identity Provider (IdP) will send the SAML response after authentication.
* **Audience URI (SP Entity ID)**: The Service Provider Entity ID, a unique identifier for CloudZero as the SAML service provider.
* **Email Domain**: Specifies the allowed email domain(s) for users authenticating through this SAML connection.
* **Sign In URL**: Login URL of your Identity Provider, where CloudZero will redirect users to authenticate.
* **Certificate Upload**: Upload the X.509 certificate from your IdP. This is used to validate the digital signature on the SAML assertions. It ensures that the SAML responses are genuine and come from your configured IdP.
* **Attribute Mapping**: Indicates whether your IdP is configured to include an email attribute in the SAML assertion payload. CloudZero uses the email attribute to associate the SAML-authenticated user with an internal CloudZero user record. If this is not properly mapped, SSO will fail or result in user misidentification.

# Configure CloudZero as a SAML application in your IdP

1. Copy the Single Sign-on URL and the Audience URI.
2. Setup the CloudZero application in your IdP. You can refer to the documentation for common IdPs for [Okta](https://help.okta.com/oie/en-us/content/topics/apps/apps_app_integration_wizard_saml.htm) and [Entra](https://learn.microsoft.com/en-us/power-pages/security/authentication/saml2-settings-azure-ad#create-an-app-registration-in-azure).
3. Ensure that you copy and enter the entire `Audience URI (SP Entity ID)` string from CloudZero.
4. Ensure that you download an X.509 certificate from your IdP (`.pem` or `.cert` file) prior to proceeding.
5. Working with your IdP, ensure that you have a SAML attribute titled `email` (for example, `<saml:Attribute Name="email" ...>`) that is mapped to the CloudZero application.

# Complete configuration in CloudZero

1. Return to the **Settings** > **SSO Integrations** > **Connect SAML to CloudZero** screen.
2. Enter your company’s email domain into the **Email Domain** field.
3. Copy the SAML Sign-On URL provided by your IdP and paste it into the **Sign In URL** field.
4. Upload the signing certificate file provided by your IdP by clicking the **Upload File** button next to the **Certificate Upload** field.
5. To confirm that you have added a mapping in your IdP to your SAML configuration such that the SAML contains a SAML AttributeStatement with the `Attribute Name = email`that is mapped to the CloudZero application, check the **Attribute Mapping checkbox**.
6. Carefully review all information entered and click **Create** **Integration**.
7. If the integration is successfully completed, you will be returned to the **Settings** > **SSO Integrations** page.
8. If the integration is unsuccessful, you will see the following error message: **Unable to create SSO integration. Please verify your configuration details and try again. If the problem persists, contact support**.

# Test your SAML configuration

The recommended steps for testing your SAML configuration are as follows:

1. After your connection is enabled, do not close or log out of your current CloudZero application session.
2. Open a private browser or incognito window, and navigate to [https://app.cloudzero.com/](https://https://app.cloudzero.com/).
3. Enter your email address. If your SSO connection is configured correctly, you will be redirected to your IdP.
4. Enter your login credentials. If you can complete the login, your configuration is correct.
