---
title: Connecting to Anthropic
deprecated: false
hidden: false
metadata:
  robots: index
---
# How the Anthropic Connection works

The Anthropic connection uses an Admin API Key to gather cost and usage data for your organization. In CloudZero you can view, track, and forecast your Anthropic costs, broken down by project, model, operation, and more.

After you create your Connection, at the time of the next data ingestion, you will see your Anthropic costs and usage throughout the CloudZero platform, including in Explorer and Analytics.

# Prerequisites for Anthropic Connection

You must create an Admin Key.

<Callout icon="ℹ️" theme="info">
  Only organization members with the Admin Role have the authority to create and use Admin API keys.
</Callout>

To create an Admin Key, follow these steps:

1. Navigate to the Anthropic Console: [console.anthropic.com](https://console.anthropic.com).
2. Sign in to your Anthropic account.
3. Navigate to API Keys.
   Look for **API Keys** in the sidebar or settings menu. You may have to navigate to **API Keys** then **Admin keys**.
4. Click the button to **Create Admin Key**.
5. Name your key with a descriptive name.
6. When you have created the API key, copy it immediately and store it securely.
   You will not be able to see the key again.

# Create Anthropic Connection

1. In CloudZero, navigate to [Cloud Integrations](https://app.cloudzero.com/organization/connections) and select **Add Connection**.
2. Select the **Anthropic tile** and select **Get Started**.
3. Enter a connection **name**.
4. Enter the **Admin Key** you created earlier.
5. Enter your **Anthropic Organization ID**.
6. Select **Connect**.
   You will be redirected to Cloud Integrations, and your newly created Connection will be listed.
