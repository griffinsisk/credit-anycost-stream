---
title: Connecting to LiteLLM
deprecated: false
hidden: false
---
<Callout icon="ℹ️" theme="info">
  The LiteLLM Connector is currently in open beta. Contact your FinOps Account Manager to share feedback or request help.
</Callout>

# How the LiteLLM Connection works

CloudZero's [LiteLLM](https://www.litellm.ai/) connection allows you to export large language model (LLM) usage data from LiteLLM to CloudZero for cost tracking analysis.

After you create a connection in CloudZero and configure it in LiteLLM, you can stream LLM token, latency, and cost data into CloudZero, where you can view, track, and forecast LLM costs broken down by model, team, user, and more.

Following the next data ingestion, you will see your LiteLLM costs and usage throughout the CloudZero platform, including in the Explorer and Analytics.

# Prerequisites for the LiteLLM Connection

Before you can connect CloudZero to your LiteLLM proxy, you must have the following:

* **In CloudZero:** A role with permission to create a cloud integration.
* **In LiteLLM:**
  * An operational LiteLLM proxy deployment.
  * Administrative access to configure LiteLLM.
  * Ability to add environment variables or update LiteLLM configuration files.
  * Network access allowing LiteLLM to send usage data to CloudZero.
  * Ability to restart or reload your LiteLLM service.

<Callout icon="ℹ️" theme="info">
  Unlike other CloudZero integrations that require you to enter a provider API key into CloudZero, this is a **Provider-Linked Connection**. You must first create a LiteLLM connection inside CloudZero, then generate a Connection API Key and configure it inside your LiteLLM proxy.
</Callout>

To connect CloudZero to LiteLLM, complete the following steps:

1. [Create a LiteLLM connection inside CloudZero.](#step-1-create-litellm-connection)
2. [Generate a Connection API key.](#step-2-generate-a-connection-api-key)
3. [Configure the connection in LiteLLM.](#step-3-configure-litellm-proxy)

# Step 1: Create LiteLLM Connection

1. In CloudZero, navigate to <Anchor label="Cloud Integrations" target="_blank" href="https://app.cloudzero.com/organization/connections">Cloud Integrations</Anchor> and select **Add Connection**.

2. Select the **LiteLLM tile** and select **Get Started**:

   <Image align="center" border={true} width="80% " src="https://files.readme.io/746a426d4ec0fba8b0e57350f2c9a06308c76b1c5472d311662c5da4ae4b3557-litellm-connection-get-started.png" className="border" />

3. Enter a connection **name** and select **Save**.

Upon success, you will be redirected to <Anchor label="Cloud Integrations" target="_blank" href="https://app.cloudzero.com/organization/connections">Cloud Integrations</Anchor>, where your newly created LiteLLM Connection will be listed:

<Image align="center" border={true} src="https://files.readme.io/63b524262bfa9d9d5e90331c3d368479e70c1d0452692d3c534329a849f4a081-litellm-billing-connections-table.png" className="border" />

Next, you must generate a Connection API Key, which is required for LiteLLM to send usage data to CloudZero.

# Step 2: Generate a Connection API Key

1. On the <Anchor label="Cloud Integrations" target="_blank" href="https://app.cloudzero.com/organization/connections">Cloud Integrations</Anchor> page, click the LiteLLM connection you just created to open its configuration screen.

2. Select **Create Connection API Key**.

   <Image align="center" border={true} src="https://files.readme.io/5de9d5562efef64605e615cb1aa0b02de94872a149c2e6d0b59a673e06f575e4-litellm-connection-create-key.png" className="border" />

3. Enter a **name** for your Connection API Key and optionally add a **description**, then select **Create Connection API Key**.

4. CloudZero displays your new Connection API Key. **Copy your Connection API Key now. You will not be able to view it again.**

<Image align="center" border={true} width="75% " src="https://files.readme.io/03a0f44b9287acb0d3a3451c3e4a4bb4f054e4b4b9b9e031ab39a4f8e56bc193-litellm-connection-copy-key.png" className="border" />

Next, you must add this key to your LiteLLM configuration.

# Step 3: Configure LiteLLM Proxy

After generating your Connection API Key, you must configure your LiteLLM proxy to send data to CloudZero.

For detailed configuration instructions and examples, see the official LiteLLM guide: <Anchor label="LiteLLM CloudZero Integration Guide" target="_blank" href="https://docs.litellm.ai/docs/observability/cloudzero">LiteLLM CloudZero Integration Guide</Anchor>

# View the LiteLLM Connection in CloudZero

<Image align="center" border={true} src="https://files.readme.io/d87b6e3ddcd3ca282dd68be82e0a6bc7f0b4d60145c674d3c03633dc16aa86fc-litellm-connection-details-healthy.png" className="border" />

After you've successfully configured the LiteLLM proxy to send data to CloudZero, the LiteLLM Connection details page displays the following information:

* Status
* Connection Name
* Connection ID
* Timestamps for connection creation, ingestion, and more
* Number of most recently ingested line items

Note that the **Status** will change from **Pending Data** to **Healthy** after CloudZero has processed the first ingest of billing and/or usage data.

# Managing API Keys

You can generate additional Connection API Keys if needed. To view or manage previously generated keys in CloudZero, navigate to <Anchor label="**Settings > API Keys**" target="_blank" href="https://app.cloudzero.com/organization/api-keys">**Settings > API Keys**</Anchor>.

To learn more about API keys in CloudZero, see [API Key Scopes](/reference/authorization#api-key-scopes).
