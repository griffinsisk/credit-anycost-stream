---
title: Connecting to Confluent Cloud
deprecated: false
hidden: false
metadata:
  robots: index
---
# How the Confluent Cloud Connection Works

After you configure the Confluent Cloud connection in CloudZero, you can view Confluent cost and usage data alongside other Cost Sources in the Explorer.

To set up a Confluent Cloud connection, complete the following steps:

1. [Create a service account in Confluent.](#step-1-create-confluent-service-account)
2. [Create an API key for the service account.](#step-2-create-api-key)
3. [Configure the connector in CloudZero.](#step-3-create-confluent-cloud-connection-in-cloudzero)

# Prerequisites for the Confluent Cloud Connection

* OrganizationAdmin or higher level access for the Confluent Organization you want to connect
* Ability to create a Confluent service account with BillingAdmin access
* Ability to generate an API key for the Confluent service account

# Step 1: Create Confluent Service Account

1. Log in to Confluent Cloud and navigate to the **Accounts and access** page from the top right menu:

   <Image align="left" alt="The &#x22;Accounts and access&#x22; link is shown in the top right menu in Confluent." border={true} width="33% " src="https://files.readme.io/189fe01c4ff7fbc01d59ca373843d6e61355588e4561c6cd1fb4dcdad454c362-confluent-navigate-to-accounts-and-access.png" className="border" />
2. In the **Accounts** tab, select **Service accounts** and click **Add service account**:

   <Image align="center" alt="Select the &#x22;Service accounts&#x22; button and then &#x22;Add service account.&#x22;" border={true} src="https://files.readme.io/d0d433aa67afae7dc7be8820673fec9148dbfd7121950717c88af65eac1fe226-confluent-add-service-account.png" className="border" />
3. Enter a name and description for the service account and click **Next**:

   <Image align="left" alt="Enter a name and description in the form for creating a service account." border={true} width="75% " src="https://files.readme.io/8012bc14216d37207178d84411f1f52342a4f575228cb7c37be748084d7570b2-confluent-add-service-account-form.png" className="border" />
4. Select the top level Organization in the left sidebar, then click **Add role assignment**:

   <Image align="center" border={true} src="https://files.readme.io/058b2f6f399643c1f9bee643478596c0fe1ed6d4cb0145e2cb8ba1e37862d378-confluent-add-role-assignment-2.png" className="border" />
5. Select the **BillingAdmin** role from the role list and click **Add**.
6. Confirm that **BillingAdmin** appears in the **Roles assigned** section, then click **Next**:

   <Image align="left" alt="The &#x22;Roles assigned&#x22; section should display the BillingAdmin role." border={true} width="50% " src="https://files.readme.io/855c20831f6ae7336d8cc9ace431dde0c770d72cb7b3d8999f6ea628b5ae0128-confluent-confirm-assigned-role-selection.png" className="border" />
7. Review the service account information, then click **Create service account**:

   <Image align="center" alt="Review the service account information in Confluent before clicking the &#x22;Create service account&#x22; button." border={true} src="https://files.readme.io/28737623c191fbae283e682c4c98825182036036584c244a3b11f24582bc95f4-confluent-review-service-account.png" className="border" />

# Step 2: Create API Key

1. In Confluent Cloud, navigate to the **API Keys** page from the top right menu.
2. Click the **Add API key** button.
3. Select **Service account** as the account for the API key.
4. In the **Existing account** section, choose the service account you created in the previous step, then click **Next**:

   <Image align="center" alt="Select the service account you created in an earlier step." border={true} width="% " src="https://files.readme.io/491939365d5cc7299851e597475bc844651e3c026e95a2752441594ce142c940-confluent-select-existing-service-account.png" className="border" />
5. Select the **Cloud resource management** resource scope and click **Next**.
6. Optionally, enter a name and description for your API key, then click **Create API key**:

   <Image align="left" border={true} width="75% " src="https://files.readme.io/52204d60a3c4824f5a89ed43010750d6db58133f94f449f98aef8b767887f291-confluent-create-api-key.png" className="border" />
7. You’ll see your new API key and secret. **Copy and save both the API key and secret immediately. You won't be able to view the secret again after closing this dialog.**

   <Image align="center" alt="Confluent displays the API key and secret you created for the service account." border={true} width="100% " src="https://files.readme.io/c1125d72ac78d5a9dbc62fb8740235cb824f75f85d55581abbb0f1aa90bceb50-confluent-copy-api-key-and-secret.png" className="border" />

# Step 3: Create Confluent Cloud Connection in CloudZero

1. Log in to CloudZero and navigate to <Anchor label="**Settings > Cloud Integrations**" target="_blank" href="https://app.cloudzero.com/organization/connections">**Settings > Cloud Integrations**</Anchor>.
2. Click **Add Connection** and select **Confluent**.
3. Paste the Confluent service account API key and secret into the **Confluent API Key** and **Confluent API Secret** fields:

   <Image align="center" border={false} src="https://files.readme.io/a2600445bcad065c3fd279376f1762d25b6719feb0c34077fc52fd5a907e5417-confluent-connection-setup.png" />
4. Click **Continue**.

CloudZero will validate your credentials and begin importing Confluent cost data. Once connected, view your Confluent costs in the <Anchor label="Explorer" target="_blank" href="https://app.cloudzero.com/explorer">Explorer</Anchor> alongside your other cloud costs.
