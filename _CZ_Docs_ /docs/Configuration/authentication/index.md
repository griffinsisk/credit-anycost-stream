---
title: Authentication
category: getting-started
createdAt: '2023-02-10T17:11:46.539Z'
hidden: false
slug: authentication
updatedAt: '2024-12-13T17:30:17.112Z'
---
# Use SSO to Authenticate with CloudZero

CloudZero allows you to connect your identity provider (IdP) to enable single sign-on (SSO). This enables you to log in to CloudZero from your IdP without needing to enter your CloudZero username and password.

If you have the necessary permissions, you can create one or more SSO integrations.

To view existing SSO integrations, navigate to [**Settings > SSO Integrations**](https://app.cloudzero.com/settings/sso-integrations) in the CloudZero UI.

Then, to create a new SSO integration, select the **Create Integration** button.

<Image align="center" alt="The SSO Integrations page in CloudZero" border={true} src="https://downloads.cloudzero.com/documentation/resources/sso-integrations-page.png" className="border" />

Next, select your IdP:

<Image align="center" alt="Select IdP" border={true} width="400px" src="https://files.readme.io/87097ffa3b4add13fd8bf441609327f13d258379e10567b6b730efa85485eeaf-sso-select-idp-1.png" className="border" />

See the pages for IdP-specific setup instructions:

* [Set up SSO with Okta](/docs/how-to-connect-okta)
* [Set up SSO with Microsoft Entra ID (Azure Active Directory)](/docs/how-to-connect-azure-active-directory)
* [Set up SSO with any other OpenID Connect application (including GCP)](/docs/how-to-connect-openid-connect)

CloudZero also supports setting up SSO with the following IdPs:

* OneLogin
* Ping Identity

If you are interested in using SAML with CloudZero, contact your Customer Success representative.

<Callout icon="ℹ️" theme="info">
  CloudZero can optionally allow your SSO IdP to manage your groups. See [Manage Groups with SSO](/docs/how-to-manage-groups-via-sso) for more information.
</Callout>
