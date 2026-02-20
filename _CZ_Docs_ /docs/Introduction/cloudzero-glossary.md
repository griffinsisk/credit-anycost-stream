---
title: CloudZero Glossary
deprecated: false
hidden: false
metadata:
  robots: index
---
# A

**Adaptor**
Code that runs in your own environments to translate a single vendor's cost data into the Common Bill Format and transfer the data to CloudZero on an automated schedule. To ingest data into CloudZero, you must create an Adaptor. See also **Common Bill Format**. For details, see [Adaptors](https://docs.cloudzero.com/docs/anycost#adaptors).

**Analytics**
CloudZero’s automated delivery of cloud cost intelligence. See also **Dashboards**. For details, see [Analytics](https://docs.cloudzero.com/docs/analytics).

**Anomalies**
See **Anomaly Detection**.

**Anomaly Detection**
CloudZero’s capability to use your cloud billing data to detect and flag abnormal spend events down to an hourly granularity. To view a list of Anomalies, use the Anomalies link in the CloudZero main navigation. For details, see [Anomaly Detection](https://docs.cloudzero.com/docs/anomaly-detection).

**AnyCost**
The CloudZero framework for ingesting cost data from any source and automating the processing of that data. See also **Adaptor**, **Billing Connection**, and **Common Bill Format**. For details, see the  [AnyCost](https://docs.cloudzero.com/docs/anycost) documentation.

# B

**Bill**
See **Common Bill Format**.

**Billing Connection**
The means by which CloudZero brings Billing, Resource, and other types of data from Cost Sources into CloudZero. For details, see [Connections](https://docs.cloudzero.com/docs/connections).

**Budget**
A budget in CloudZero enables you to track spend against important business metrics and optionally notify the right people when something goes off track. Each budget is linked to a  View, which determines the spend tracked by the Budget and the teams notified.  See also **View**. For details, see [Budgets](https://docs.cloudzero.com/docs/budgets).

# C

**Charge**
A single line item of cloud cost or a collection of cloud costs, the dollar amount that the cloud provider billed for a given thing at a given time. All Dimensions begin with a charge. For details, see [Dimensions](https://docs.cloudzero.com/docs/dimensions) and the [CostFormation Definition Language guide](https://docs.cloudzero.com/docs/costformation-definition-language-guide).

**Cloud cost intelligence**
Cost data that is automatically organized for analysis to help engineering connect technical decisions to business results. For details, see [What is Cloud Cost Intelligence?](https://www.cloudzero.com/blog/cloud-cost-intelligence-definition/)

**Cloud Financial Management (CFM)**
The process of identifying, measuring, monitoring, and [optimizing cloud costs](https://www.cloudzero.com/blog/cloud-cost-optimization), also known as Cloud Cost Management or Cloud Cost Optimization. For details see the [Cloud Spend for Finance guide](https://www.cloudzero.com/guide/cloud-spend-for-finance-guide/).

**Common Bill Format**
A standard data model to ingest cost data from any source. For details, see the [Common Bill Format (CBF)](https://docs.cloudzero.com/docs/anycost-common-bill-format-cbf) documentation.

**Connection**
See **Billing Connection**.

**Cost Allocation**
The technique of splitting cost among systems using Allocation Dimensions, a type of Custom Dimension. All allocation is based on real cost. There are Rules Allocation Dimensions and Telemetry Allocation Dimensions. For details, see [CostFormation: Allocating Shared Costs](https://docs.cloudzero.com/docs/costformation-allocating-shared-costs).

**CostFormation**
CloudZero CostFormation enables you to use features of the CloudZero platform to view your cloud costs in the context of your business and engineering needs. Using the CostFormation Definition Language, you can define Custom Dimensions. For details, see the [Cost Formation Definition Language](https://docs.cloudzero.com/docs/cost-formation-definition-language) documentation.

**Custom Dimension**
A Dimension created with custom logic specific to your organization that allows you to view your cloud costs in the context of your business or engineering needs. Custom Definitions consist of rules and conditions that are used to assign your cloud charges to different Elements based on billing line item data as well as other sources, like resource tags. See also **Dimension**. For details, see the [CostFormation Definition Language guide](https://docs.cloudzero.com/docs/costformation-definition-language-guide).

# D

**Dashboard**
A collection of one or more saved queries enabled by Analytics and displayed as visualization or text tiles together on one page. Dashboards can be standard (created by CloudZero) or custom (created by the user). See also **Analytics**. For details, see [Introduction to Dashboards](https://docs.cloudzero.com/docs/analytics#introduction-to-dashboards).

**Dimension**
A way of viewing your cloud costs broken down into different groups or Elements. Using Dimensions allows you to understand the costs of operating cloud software in ways that matter to your business. See also **Custom Dimension**. For details, see [Dimensions](https://docs.cloudzero.com/docs/dimensions).

# E

**Element**
A group of related charges within a Dimension. For details, see the [CostFormation Definition Language guide](https://docs.cloudzero.com/docs/costformation-definition-language-guide).

**Engineering Event**
Activities in your engineering systems, such as source control, CI/CD, configuration management, and so on. CloudZero allows you to correlate these activities with your cloud costs. For details, see [Engineering Events](https://docs.cloudzero.com/docs/engineering-activity-correlation).

**Explorer**
A visualization of your bill. Using the CloudZero Explorer, you can view and examine your cloud bill by filtering and grouping your charges based on different Dimensions. For details, see the [Explorer](https://docs.cloudzero.com/docs/explorer) documentation.

# F

**FinOps**
Abbreviation for Cloud Financial Operations. For details see [What is FinOps?](https://www.cloudzero.com/blog/finops/).

# I

**Insights**
User-generated observations on cost trends or optimizations in your environment. For details, see [Insights](https://docs.cloudzero.com/docs/optimize#insights).

# O

Optimize
The CloudZero Optimize feature continually analyzes your environment and automatically generates Recommendations that will help your organization save money and avoid costs. For details, see the [Optimize](https://docs.cloudzero.com/docs/optimize) documentation.

# T

**Telemetry**
Cloud usage data to help you ensure your business is maximizing profit when delivering cloud-based services. You can upload this data in a CVS file or by API. For details, see the [telemetry documentation](https://docs.cloudzero.com/docs/csv-import-telemetry).

# U

**Unit cost**
Breakdown to show the total cost for a particular business metric, for example, per API call, cost per user, cost per transaction. For details, see [Unit Cost Analytics](https://docs.cloudzero.com/docs/unit-cost-analytics).

**Unit Cost Analytics**
CloudZero functionality that calculates total cost per business metric based on telemetry data. For details, see the [Unit Cost Analytics](https://docs.cloudzero.com/docs/unit-cost-analytics) documentation.

# V

**View**
Views provide targeted cost visibility to individual teams, helping to decentralize cost management in the engineering organization. Each View includes a Principal Dimension to group costs by, at least one Filter to filter costs by, and a Slack or email (or both) notification channel. For details, see [Views](https://docs.cloudzero.com/docs/views).
