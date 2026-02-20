---
title: Common Sources of Unit Cost Telemetry Data
category: features
hidden: false
slug: collecting-unit-cost-telemetry
---
Understanding the activity of your users and systems is what drives CloudZero's ability to transform your cloud spend into unit cost metrics. With even a basic understanding of customer activity within your application, CloudZero can quickly calculate things like cost-per-customer.

When thinking about the sources of telemetry to collect, it is important to think in broad strokes first. Unlike as needed by monitoring tools, the telemetry you send CloudZero does not need to be perfect for you to gain valuable insights. Start simple, and later as your accuracy needs increase, add additional telemetry streams. Telemetry streams can have overlapping coverage and are additive, with each one increasing the accuracy of the output.

Often you can reuse existing application data sources or you can choose to directly instrument your applications to create new sources of data. For example, existing application or load balancer metrics can be good sources of data that represent how often users are accessing your services.

You can use virtually any data source you can obtain the metrics from for Unit Cost as long as you can convert the data source into the required JSON format. Some sources of data may cost more than others depending on the external tool or platform storing the data. These costs can include the cost to store it, cost to retrieve and query it, cost to export from the tool, and cost to convert the data to the required JSON format.

The following considerations apply in specific circumstances.

* **Application and System Metrics:** Metric data types found in tools such as Grafana, Prometheus, and CloudWatch Metrics may provide the usage data you need to understand how many active daily users you had in a time frame. When possible, try to use your metric-formatted data as it may typically incur lower costs to query and run from your observability tool than more unstructured data like logs.

* **Application and System Logs:** Logs are verbose and may typically include the data you need to aggregate for Unit Cost. You may have web server logs for each user login. Depending on the observability tool you use to track these logs, you can simply run a query to obtain the total unique active daily users on a daily basis. :information_source: Due to the unstructured and verbose nature of logging, it is possible that using this data may incur slightly higher charges than metric data to process before transmitting to CloudZero.

* **Database Query:** A simple database query may provide the metric you need if it is not in a native observability tool or format. This can be something like a query for the total amount of transactions a user ran in a day, for new records created, or for any other aggregation that may be obtained through the database query.

* **Marketing and Sales Systems:** Systems used by marketing and sales teams may provide valuable metrics needed for Unit Cost. Check with your marketing and sales teams if they are collecting data such as site visits, sales, and so on.

* **Security:** Security teams usually have an abundance of important data needed for Unit Cost. Due to the sensitivity and potential compliance requirements of data a security team may own, you may not be able to use this data.
