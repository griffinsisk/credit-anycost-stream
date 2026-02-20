---
title: Unit Cost Analytics
category: features
hidden: false
slug: unit-cost-analytics
---
Unit Cost Analytics, also known as Unit Economics, can provide the total cost of a specified metric for the business. This metric can be something like the cost per API call, cost per user, cost per transaction, or any other useful data point for understanding the efficiency and effectiveness of a system.

# Unit cost example

For example, Company A may know the total cost of their system is **$10,000** on day one, and **$7,500** on day two. Without any additional information, they might then conclude that day one was the costliest day for their business.

However, Company A also has a `cost per user` metric that indicates that their cost per user was $1.75 on day one, and $2.25 on day two. This indicates that the cost to run the business was actually higher on the day with the lowest spend.

In this way, unit metrics helped Company A understand that their system was running less efficiently when the total cost was deceptively low.

# Understanding unit cost

Multi-tenant systems provide many cost, architecture, and operational benefits. However, these same benefits come at the expense of granularity. With these more complicated system architectures, it becomes more difficult to break down the costs across data points such as daily active users or events.

This breakdown into unit costs can provide crucial insights into a system's performance and utilization. With access to this information, an organization can empower their teams to more successfully manage and optimize their systems, and in so doing, take control of their related cloud costs.

Organizations that have command over their unit costs have a better command over their gross margins, because these organizations know that a steady or decreasing unit metric trend, even while costs increase, is an indicator of healthy growth.

<Image align="center" alt="Unit cost decresasing over time with usage increase" className="border" border={true} src="https://files.readme.io/90e81dc-CleanShot_2020-09-17_at_17.21.072x.png" />

# Unit Cost Analytics implementation

Unit Costs are calculated as the **spend divided by the metric**. You will need the following to calculate it:

* **Spend that will drive unit cost** This will be the numerator used to calculate unit cost. Will it be all spend data or a subset? Is it just production data? Is it only data for a certain product?
* **Metric to divide the spend by** This is the denominator used to calculate the unit cost. This data is oftentimes found in an observability tool or database query, and typically it is not a dataset found in your cloud provider’s bill.

This metric could be something like total active users per day, total API calls per day, and so on. Provide a metric at a time granularity of at least daily. Hourly will provide the best ability to understand Unit Cost at the lowest level.

The metrics will be transmitted to CloudZero through an API.

Follow these steps to implement Unit Cost Analytics.

1. Identify the spend you wish to break down.
   Create a View that highlights the spend you wish to break down using one or more filters.

<Image align="center" alt="Explorer View" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/Unit_Metrics_Step_1.png" />

2. Identify a source for your unit cost data stream.
   Filter your whole organization’s spend specifically to the spend driving your Unit Cost. Take note of the metadata (Dimensions, tags, and so on) used in the filter, if any.

3. Format your Unit Cost Data Stream.
   An example unit cost data stream is shown in the diagram that follows. The unit cost data stream must be in a specific JSON format before you transmit the stream to the CloudZero API. The data must include a `datetime`, the filters indicating what the spend you want to break down, and the metric value, for example, total active daily users. You do not need to convert the value. For more information on the JSON format, see the [Unit Metric API documentation](/reference/unit-metric-telemetry-api-1#/).

<Image align="center" alt="Unit metric stream for daily API calls by feature" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/Unit_Metrics_Step_2.jpg" />

4. Send the data to the CloudZero API.
   When your data is prepared, you will send it to CloudZero using the Unit Metric API. For details, see the [Unit Metric API documentation](/reference/unit-metric-telemetry-api-1#/).

5. Review your Unit Cost Report.
   After the next ingest of your CloudZero billing data, the metric will be available in the CloudZero Analytics feature as a measure.

   <Image align="center" alt="Example of unit metrics measure" className="border" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/Unit_Metric_Step_4.png" />

   <Callout icon="ℹ️" theme="info">
     The name of the measure will be derived from the name of the associated Unit Metric stream (that is,  the value you selected for `{metric_name}` in the Unit Metric API path.

     When CloudZero begins to receive data, your stream will appear on the CloudZero [Telemetry Streams page](https://app.cloudzero.com/telemetry) with a **Type** of **Metric**.
   </Callout>

6. Automate the transmission of Unit Cost data.
   When you have confirmed the data, it is recommended that you automate the retrieval, formatting, and transmission of it to CloudZero. This can be done with something like a Lambda function that runs hourly or a scheduled query in your observability tool that transmits to CloudZero in the required JSON format.