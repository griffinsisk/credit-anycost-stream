---
title: Connecting to Oracle Cloud
deprecated: false
hidden: false
metadata:
  robots: index
---
<Callout icon="ℹ️">
  The Oracle Cloud Connector is in open beta. If you would like to use the connector, contact your FinOps Account Manager or Customer Success representative.
</Callout>

# Prerequisites for the OCI Connection

To establish a proper connection for Oracle Cloud Infrastructure (OCI), you must have the following:

1. Root tenant access
2. Ability to generate an API key
3. Copy and paste tenant information and the contents of the _private_ key.

# Steps in creating the connection

## Step 1

In Oracle Cloud, make sure your account has proper access, and navigate to **Billing & Cost Management** in the top left menu:

<Image align="center" alt="Billing and cost management screen" border={true} src="https://files.readme.io/5940fdf507c40225e43d8127f46225bc6eea43277ec41a42981bb282d9b43414-oracle-cloud-billing-and-cost-management.png" className="border" />

Then click **Cost and Usage Reports**. The screen should display a list like the following:

<Image align="center" alt="Cost and Usage Reports" border={true} src="https://files.readme.io/a2b5f57b28ada6641259097e0efc5334b62ae9277caca8a97e666b4cea3d2961-oracle-cloud-billing-cost-and-usage-reports.png" className="border" />

If you are seeing errors, messages around policies, and so on, then you likely do not have proper root access.

## Step 2

Go to your user profile and select the **Tokens and keys** tab:

<Image align="center" alt="API keys" border={true} src="https://files.readme.io/eb37aa4478f8402211acbe69f8de6aa2837d08fa74122609ce7c7ae74ebd7d7f-oracle-cloud-user-profile.png" className="border" />

1. Click **Add API key**.
2. Download your private key.
3. Click **Add**.
4. (Optional) Copy the configuration file preview. This is the information you need to provide in the CloudZero Oracle Cloud connection.

The configuration file snippet preview should look like this:

<Image align="center" alt="Configuration file preview" border={true} src="https://files.readme.io/f9c62143837264a349cf80f864eb5a14058bcc148c3e03a049007439da399579-oracle-cloud-config-file-preview.png" className="border" />

You will need the following information from the configuration file preview:

| Cloud Zero field    | Configuration field |
| :------------------ | :------------------ |
| User OCID           | user                |
| API Key Fingerprint | fingerprint         |
| Region              | region              |
| Tenancy OCID        | tenancy             |

## Step 3

Copy and paste all the information from your configuration preview into the CloudZero connection screen:

<Image align="center" alt="CloudZero connection screen" border={true} src="https://files.readme.io/9d6e4f2eeafab5e00f9f7d481266c986accf428f31222e18bb9a4dd6bbd5762d-oracle-cloud-connection-screen.png" className="border" />

Finally, locate the private key that you downloaded on your machine. Copy and paste just the private key into the **Private Key** field in the connection screen.

## Step 4

Click **Continue**. After a short verification, the connection will be created.
