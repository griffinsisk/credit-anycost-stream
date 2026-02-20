---
title: Manage Roles with SSO
deprecated: false
hidden: false
metadata:
  robots: index
---
You can manage your CloudZero Roles by enabling your single-sign on (SSO) identity provider (IdP) to automatically assign users to existing, manually-created Roles.

After you [create one or more Roles](/docs/view-and-manage-roles#create-role) and set [up your SSO integration](/docs/authentication) in CloudZero, you can enable the **SSO for Roles** setting.

To do this, navigate to **Settings** > **SSO Integrations** > Select an **SSO Integration you have configured from the list** > Check **Enable SSO for Groups.**

If you pass in group claims using your IdP (for example, Finance team, IT team, Product team), CloudZero will look for existing Roles with a name matching the group claims passed in and then sync the appropriate users to those Roles. Any Roles without a matching name will be ignored.

To enable SSO for Roles, follow the steps for your IdP:

* [Okta](/docs/manage-roles-with-sso#manage-roles-with-okta)
* [Microsoft Entra ID (Azure AD)](/docs/manage-roles-with-sso#microsoft-entra-id-azure-ad)
* [OpenID Connect including GCP](/docs/manage-roles-with-sso#openid-connect-including-gcp)

# Manage Roles with Okta

<Callout icon="ℹ️">
  You must manually [create one or more Roles](/docs/view-and-manage-roles#create-role) in CloudZero before you can enable SSO for Roles.
</Callout>

To enable SSO for Roles using an [Okta](/docs/how-to-connect-okta) integration, follow these steps:

1. [Add a claim to the Okta Authorization Server](/docs/manage-roles-with-sso#step-1-add-claim-to-okta-authorization-server).
2. [Add a claim to the CloudZero-specific application in Okta](/docs/manage-roles-with-sso#step-2-add-claim-to-cloudzero-application-in-okta).
3. [Enable SSO for Roles in CloudZero](/docs/manage-roles-with-sso#step-3-enable-sso-for-roles-in-cloudzero).

## Step 1: Add Claim to Okta Authorization Server

1. In Okta, navigate to **Security** > **API** > **Authorization** > **Servers** and select the appropriate authorization server. This is usually the default server.
2. Select **Claims** > **Add Claim**.
3. Enter a **Name** for the Okta claim.
4. In the **Include in token type** field, select **ID Token**, and in the second drop-down selector, choose **Userinfo/id_token request**.
5. Set Value type to **Groups**.
6. In the Filter field, set the filter predicate drop-down menu to your choice of predicate, for example, **Matches regex**.
7. Set the filter value to your choice of value, for example, `.*` to match all CloudZero Roles. Ensure this matches the name of the Roles your users are in.
8. Set the Include in field to **Any scope**.
9. Click **Save**.

These Okta settings are illustrated in the Edit Claim form:

<Image align="center" alt="Edit claim form" border={true} width="500px" src="https://files.readme.io/e356271752f2239bdda8d4eb484c307a8d72e6e48b4184cbb5691a768344fbfd-01-roles-edit-claim.png" className="border" />

You should then see the claim in the claims table for your authorization server:

<Image align="center" alt="Claims table" border={true} src="https://files.readme.io/4d5c6f65dfdffff3b5bbe33d1c40929fa5c44bf22318b1c4585035982f9e8472-02-roles-add-access-claim.png" className="border" />

## Step 2: Add Claim to CloudZero application in Okta

1. In Okta, navigate to **Admin Console** > **Applications** > **Applications**.
2. Select your **CloudZero application**.
3. On the **Sign On** tab, scroll down to the **OpenID Connect ID Token** and click **Edit**.

   <Image align="center" alt="Edit OpenID Connect ID Token" border={true} width="500px" src="https://files.readme.io/e616b03842a5c894f8eb9a206091e4060311d4679b2040dde27d27e5a7344f11-03-roles-edit-connect-token.png" className="border" />
4. In the **Groups claim filter** section, set the first drop-down menu to **groups**.
5. Set the second drop-down menu to your choice of filter predicate, for example, **Matches regex**.
6. Set the **filter value** field to your choice of value, for example, `.*` to match all CloudZero Roles. In the example that follows, we want to pass all groups that **start with `app-clou`**.

   <Image align="center" alt="Choose filter value" border={true} src="https://files.readme.io/abdecd23a810de832f7464ea3762dd5a01f1ceafd25f8784e7e89c46f21ec90c-04-roles-groups-claim-filter.png" className="border" />
7. Click **Save**.

## Step 3: Enable SSO for Roles in CloudZero

1. In CloudZero, navigate to **Settings** > **SSO Integrations** and select your **Okta integration**:

   <Image align="center" alt="Connect your SSO integration" border={true} src="https://files.readme.io/c0a5b61fc7f19b88bc74ec66a7d227decdc0f207e749d98fd89192d8b312cfdc-05-roles-connect-integ.png" className="border" />
2. Scroll down to the **SSO Connection Status and Controls** section and check the **Enable SSO for Roles** (called Groups in the image) box:

   <Image align="center" alt="Enable SSO for Roles called Groups" border={true} src="https://files.readme.io/1fe712dcecd23a61c7442de20d49e9b3a2b126265f3576311acb7805cbbf42c0-06-roles-enable-sso-for-groups.png" className="border" />
3. Click **Enable**.

# Microsoft Entra ID (Azure AD)

<Callout icon="ℹ️">
  You must manually [create one or more Roles](/docs/view-and-manage-roles#create-role) in CloudZero before you can enable SSO for Roles.
</Callout>

To enable SSO for Roles using a [Microsoft Entra ID (Azure Active Directory)](https://docs.cloudzero.com/docs/how-to-connect-azure-active-directory) integration:

1. In CloudZero, navigate to **Settings** > **SSO Integrations** and select your **Microsoft Entra ID (Azure AD) integration**:

   <Image align="center" alt="Connect your SSO integration" border={true} src="https://files.readme.io/6a15d3fb0ab6e7f3a90a15dceff7047c98c03f588b0e8e0ef6c7187735e6d540-05-roles-connect-integ.png" className="border" />
2. Scroll down to the **SSO Connection Status and Controls** section and check the **Enable SSO for Roles** (called Groups in the image) box:

   <Image align="center" alt="Enable SSO for Roles called Groups" border={true} src="https://files.readme.io/03fe7236f6af3b8ec73989d7cb4e7d47cf2ab69064ca5365325df633eb6eed4d-06-roles-enable-sso-for-groups.png" className="border" />
3. Click **Enable**.

# OpenID Connect including GCP

<Callout icon="ℹ️">
  You must manually [create one or more Roles](/docs/view-and-manage-roles#create-role) in CloudZero before you can enable SSO for Roles.
</Callout>

The Roles claim is often a new scope in your OpenID Connect (OIDC) IdP. None of CloudZero's existing OIDC integrations ask for this claim.

Follow these steps to send CloudZero the Roles claim and enable your OIDC IdP to manage your existing Roles in CloudZero:

1. In CloudZero, navigate to **Settings** > **SSO Integrations** and select your **OIDC integration**.

   <Image align="center" alt="Connect your SSO integration" border={true} src="https://files.readme.io/7d76a32698429f240518024e7253f25390b3fbfc1ebe5f3f2e266c6dff9bc713-05-roles-connect-integ.png" className="border" />
2. Scroll down to the **SSO Connection Status and Controls** section and check the **Enable SSO for Roles** (called Groups in the image) box.

   <Image align="center" alt="Enable SSO for Roles called Groups" border={false} src="https://files.readme.io/ca4b69db01a51ac70b62406781b7571b10f120bfdffbed32e42960d4aaee02b0-06-roles-enable-sso-for-groups.png" />
3. Click **Enable**.
