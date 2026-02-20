---
title: Viewing Usage Data
category: features
hidden: false
slug: viewing-usage-data
---
The CloudZero Analytics feature provides insights into cost data. Yet, behind all cost data, there is associated usage data. For instance, if you are charged five dollars for an EC2 instance for a day, and you used it for `4.2` hours, then `4.2` hours is the usage data, and hours are the pricing unit. Incorporating this usage and pricing unit data provides additional value for analysis.

<Callout icon="ℹ️" theme="info">
  Note that the usage data discussed here is specifically from the CUR (Cost and Usage Report) and does not cover other potential metrics like memory, CPU limits, and so on.

  Because Usage Data and Invoice Date are not always the same, you may see two different dates in CloudZero for a particular cost, depending on which cost type you are using in your Dashboard. For example, your `AmazonRegistrar` charge date may not always align with your invoice.
</Callout>

# Why is usage data Important?

Costs can sometimes decrease, not because of reduced usage, but due to external factors like purchasing savings plans. While cost data can be affected by these pricing mechanisms, usage data remains unaffected, offering a clearer, more realistic insight into resource consumption.

# Access to usage data in CloudZero

Only the Analytics feature provides access to usage data.

<Callout icon="ℹ️" theme="info">
  Usage data is available only from AWS, Azure, GCP, and AnyCost (CBF).
</Callout>

When you are adding a visualization, you will see an option that says **Cost Types and Usage**. This is where you have access to usage metrics. Among them is **Usage Amount**, a metric that showcases the amount of resource consumed without indicating the cost.

<Callout icon="ℹ️" theme="info">
  Usage data requires more discernment than required by cost data to ensure the constructed visuals provide accurate insights. If you are to summarize or aggregate usage data, you must have both **Resource Type** and **Pricing Unit** selected. If these are not selected, you risk aggregating across different units, leading to potentially misleading data.
</Callout>

# How to build with usage data

1. Navigate to **Analytics**.
2. When you are adding a visualization, select the option that says **Cost Types and Usage**.
3. Select **Usage Amount**.
4. Always add a **filter** for date for optimal results.
5. To ensure accuracy, always include the **Pricing Unit** when dealing with **Usage Amount**.
6. Always keep in mind that aggregating different units (for example, hours, MB, instances) may not be meaningful. Thus, when you are summarizing or aggregating, always filter by both **Resource Type** and **Pricing Unit**.
