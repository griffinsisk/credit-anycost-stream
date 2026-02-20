---
title: 'Connecting to OpenAI '
deprecated: false
hidden: false
metadata:
  robots: index
---
# How the OpenAI Connection works

The OpenAI connection uses a read-only Admin API Key to gather cost and usage data for your organization. In CloudZero, you can view, track, and forecast your OpenAI costs, broken down by project, model, operation, and more.

At the time of the next data ingestion, you will see your OpenAI costs and usage throughout the CloudZero platform, including in Explorer and Analytics.

# Prerequisites for the OpenAI Connector

You must create a read-only Admin API Key.

<Callout icon="ℹ️" theme="info">
  Only Organization Owners have the authority to create and use Admin API keys.
  To create an Admin API Key, follow these steps:
</Callout>

1. Navigate to [Admin Keys](https://platform.openai.com/settings/organization/admin-keys) in OpenAI, then select **+ Create new Admin Key**.
2. Provide a name for the `Admin Key`, for example, `CloudZero Integration`.
3. Set the permissions to **Restricted** and grant **Read** access to the Management API and Usage API scopes.
4. Select **Create Admin Key**.
5. Copy the generated key immediately and store it securely.
   You will not be able to see the key again.

# Create a Connection

1. In CloudZero, navigate to [Cloud Integrations](https://app.cloudzero.com/organization/connections) and select **Add Connection**.
2. Select the **OpenAI tile** and select **Get Started.**
3. Enter a connection **name**.
4. Enter the **Admin Key** you created earlier.
5. Select **Connect.**
6. You will be redirected to Cloud Integrations; verify that your newly created connection is listed.
