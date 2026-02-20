---
title: What's New At CloudZero
category: documentation
createdAt: '2025-03-14T19:39:05.304Z'
hidden: false
slug: whats-new
updatedAt: '2025-03-20T19:39:05.304Z'
---
<Image alt="What's New At CloudZero" border={false} src="https://downloads.cloudzero.com/documentation/resources/whats-new-banner.png" />

# December 2025

## Manage Recommendation Types in Optimize

The **Optimize Settings** panel **(in beta)** allows you to control which Recommendation Types are evaluated for your organization. When you disable a Recommendation Type, CloudZero stops evaluating it and hides existing Recommendations of that type. Changes take effect during the next daily analysis cycle. To access Optimize Settings, click **Settings** in the upper-right corner of the [Optimize](https://app.cloudzero.com/optimize/overview) page. For more information, see [Manage Recommendations](/docs/optimize#manage-recommendation-types).

## LiteLLM Connector (Open Beta)

CloudZero's **LiteLLM Connector** is in open beta. The LiteLLM Connector allows you to bring AI spend data from hundreds of LLMs across more than 70 providers directly into the CloudZero platform for unified cost visibility. This helps FinOps, engineering, and finance teams understand how AI spend is changing over time, where costs originate, and how usage maps to business value, all within CloudZero's existing workflows. For details, see the [LiteLLM Connector documentation](/docs/connections-litellm).

# November 2025

## CloudZero Academy launch

The CloudZero Academy is now live, powered by Thinkific. This updated learning hub provides a self-guided experience with role-based learning paths, expanded courses on core CloudZero concepts, interactive assessments, and formal certifications to validate CloudZero proficiency.

Access the CloudZero Academy directly from the <Anchor label="CloudZero platform" target="_blank" href="https://app.cloudzero.com/">CloudZero platform</Anchor> by clicking the **Help** icon in the top-right navigation bar and selecting **CloudZero Academy**.

## Multiple email addresses for Views

You can now add **multiple email addresses** to any View. It is no longer necessary to use a distribution list to reach multiple recipients. You can simply add the email addresses of users who are to receive notifications.

## See Role update details

A new **RBAC enhancement** lets you see when a Role was updated and who made the change. This information is on the list of Roles page and each Role Details page. For more information, see [View and Manage Roles](/docs/view-and-manage-roles).

# October 2025

## Beta release of RBAC

The beta release of **RBAC** (Role-based Access Control) is now available. RBAC allows customers to create and manage roles that both restrict access to data AND govern the capabilities users can take action on. For details, see the [RBAC documentation](/docs/role-based-access-control).

## RBAC enhancements

**Managing user and role assignments now requires fewer steps**. Before this improvement, if you assigned a user to four roles, it was necessary to open the role, assign the user to the role, save the changes, and then move to the next role and repeat the steps a total of four times. Now you can open the **Users** page, select the **Roles** to assign to the user, and **Save**.

You can now **view combined permissions on the Users page**. CloudZero allows for all users to be assigned to multiple roles. Each role may have different permission sets. For example, Role A may have `View-only` permissions, and Role B may have `Edit` permissions. Now, on the **Users** page, admins can view the fully combined permission set granted to a particular user based on the combination of all of that user's assigned roles. This improvement makes it easier for admins to understand exactly what a user is permitted to do in CloudZero.

For details see [View and Manage Roles](/docs/view-and-manage-roles).

## Optimize Realized Savings

Optimize now includes **Realized Savings**, allowing customers to track the total savings realized from all addressed Recommendations. Users can select the time range and group by Dimensions. For more information, see the [Optimize documentation](/docs/optimize#realized-savings).

## Activity history for Optimize Recommendations

CloudZero users can now view a complete activity history for every Optimize Recommendation. Users can see events such as when the Recommendation was created or who changed the status of the Recommendation. Comments are included inline to help facilitate team collaboration and decision making. This update makes it easier for customers to understand the lifecycle of each Recommendation, improve accountability, and stay aligned on cost optimization efforts.

## GCP currency conversion selection

By default, when you set up a GCP billing connection, the currency is converted to US dollars and the checkbox **Convert all currency to USD** is selected. You can now deselect the checkbox to leave the currency as it is currently set in GCP. This will cause mixing of currencies on the platform. For details, see the [GCP billing connection setup documentation](https://docs.cloudzero.com/docs/connections-gcp-billing#step-2-configure-your-connection).

## Common Bill Format `lineitem/cloud_provider`

`lineitem/cloud_provider` has been added to the CloudZero Common Bill Format (CBF). This new field is a string value that identifies the underlying cloud provider for each line item. The field supports values including `Anthropic`, `OpenAI`, `AWS`, `Azure`, and more, making it easier than ever to track costs across multiple cloud providers. If you use an aggregator service that consolidates billing from multiple cloud providers into a single CBF file, you can now seamlessly distinguish between providers without any manual mapping or guesswork. For more information, see the [Common Bill Format documentation](/docs/anycost-common-bill-format-cbf#lineitemcloud_provider).

## Automated Databricks pricing

Your custom Databricks pricing now applies automatically to your usage data in CloudZero. For details, see  [Automated pricing with Account Prices](/docs/connections-databricks-v2#automated-pricing-with-account-prices-databricks-private-preview) in the Databricks connection documentation.

## Enhanced job run granularity for Databricks (beta)

CloudZero now provides run-level visibility for your Databricks workloads, enabling you to track and optimize individual job executions rather than being limited to job-level analysis. You can now view, filter, and group your Databricks spend by:

* `run_name`: the specific name of each job execution
* `job_run_id`: the unique identifier for each job run

These attributes capture point-in-time execution data, giving you the granularity needed to measure the impact of configuration changes and optimizations across multiple runs of the same job.

### Benefits of run-level granularity

As you tune Databricks jobs for efficiency, adjusting cluster configurations, modifying runtime parameters, or optimizing code, you need to measure whether those changes actually reduce costs. Job-level aggregation masks this detail. Run-level granularity lets you compare the cost of individual executions before and after changes, helping you quantify the ROI of optimization efforts.

This capability also restores functionality that was previously available through the AnyCost adapter, ensuring you maintain the same analytical depth as you migrate to the native Tier 1 Databricks integration.

### How to use run-level granularity

In Explorer and Analytics, you will now see `run_name` and `job_run_id` available as Dimensions for filtering and grouping. Use these to:

* Compare costs across specific runs of the same job.
* Identify which runs consumed unexpected resources.
* Track cost trends as you optimize job configurations over time.

<Callout icon="ℹ️" theme="info">
  Unlike tags, run-level metadata is not backfilled to historical data, but reflects the actual execution context at the time each job ran.
</Callout>

# September 2025

* The **Dimension Studio** is now available, allowing users to create, update, or delete Dimension definitions directly within the CloudZero application. For details, see the [Dimension Studio documentation](/docs/dimension-studio).
* There is now an **Anthropic Connector**. For details, see the [Anthropic Connector documentation](/docs/connections-anthropic).
* An **Open AI Connector** is now available. For details, see the [Open AI Connector documentation](/docs/connecting-to-openai).
* A **ClickHouse AnyCost (tier3) adapter** is available. If you would like to use the adapter, contact your FinOps Account Manager for access.
* A **new automated Recommendation** has been added for AWS: **Inactive DynamoDB table**. For more information, see [Recommendations for AWS](/docs/aws-automated-insights).

# August 2025

* The **Optimize** feature, available on the CloudZero top navigation, continually analyzes your environment and automatically generates Recommendations that will help your organization save money and avoid costs. All of your manual and custom Insights are now on the **Insights** tab on the Optimize page. Migration is automatic. To see Anomalies, use the new **Anomalies** option in the CloudZero top navigation. For details, see the [Optimize documentation](/docs/optimize).

* **Static Rate Smoothing**: CloudZero now supports applying a static cost rate to resources using CostFormation. For more information, contact your FinOps Account Manager or your Customer Success Representative.

* **Date Filtered Group Dimensions for CostFormation**: Date Filters now allow you to specify start and stop dates for specific group Dimensions. Publishing changes to Dimensions through CostFormation applies that Dimension change to all of the data in CloudZero. CloudZero recommends specifying a timeframe when you change a Dimension to have consistent reporting that does not change all historical data. This allows you to do things like manage re-organization, where there are specific effective dates. For more information, see the [CostFormation Language Reference](/docs/cfdl-reference).

* **Usage Type** and **Operation** are now shown as default global Dimensions on the Explorer page. For more information, see the [Explorer](/docs/explorer) documentation.

# July 2025

* **The Organization Management** feature is now in GA. For details, see the [documentation](/docs/organization-management).

* **New standard Dashboards are available**, including total Cloud Spend - Summary Dashboard, Finance - Summary Dashboard, and Total Cloud Spend - New Resource Digest Dashboard. In addition, all standard dashboards have been modified to provide a cleaner and more consistent UX/UI experience.

* **AWS resource collection is now in Beta**. To use this feature, customers must have their member accounts connected to CloudZero as Resource Accounts. For details, refer to the [setup instructions](/docs/connections-aws-manual-resource). This enhanced data collection provides more robust, detailed insights across a wider variety of AWS resources, unlocking new capabilities for customers: Enhanced resource details pages with comprehensive resource information; Additional context for Optimize recommendations to more quickly triage and make better decisions; and New Optimize recommendations powered by richer data. For more information and to request access, contact your FinOps Account Manager or Customer Success Representative.

* **The CloudWatch Kubernetes Agent will no longer be available effective on November 1**. Customers must migrate to the latest version of the new CloudZero Agent for Kubernetes (V1.2.1 or Later) to receive billing data after November 15. If you need help, contact your FinOps Account Manager.

* **The Kubernetes Details Page is now available in Beta**. This feature allows customers to get details about their Kubernetes agent directly in the CloudZero platform. This includes agent version, labels, annotation configuration, and more. The goal is to improve the experience for any needed troubleshooting. For more information and to request access, contact your FinOps Account Manager or Customer Success Representative.

# June 2025

* **Kubernetes Agent 1.2.3 is now available**: This release introduces Cloud Service Provider Auto-Detection, significant Performance Optimizations for the admission controller, enhanced Istio Integration, and numerous reliability improvements. This release also simplifies deployment configuration while improving performance and compatibility with service mesh environments. For details, see the [Kubernetes Agent Releases](https://github.com/Cloudzero/cloudzero-charts/releases/tag/1.2.3).

* **Additional Standard Dashboards are now available**: These dashboards provide CloudZero users with additional information about their cloud spend, provide finance teams with a focused view into month-to-date, rolling-12-month, and anticipated upcoming cloud spend, and allow FinOps users to easily flag newly created, high-cost resources.

# May 2025

* **Add a User via the UI**: Organizers can now add a user directly from the user settings page. This is available for customers with and without SSO enabled. [Learn more.](https://docs.cloudzero.com/docs/user-management)

* **All User Roles can now switch between Organizations**: We’re thrilled to announce an upgrade to Organization Management that is going to make life a whole lot easier for our customers! Tenant switching is now available to all Primary Org users that have the Organization Management feature enabled – regardless of role. Whether you are an Organizer, Contributor, or Viewer, you can now seamlessly switch tenants. When users switch into another org, their role from the Primary Org will carry over – no need to manually reassign roles or elevate permissions.

# April 2025

* **Jira Integration**: Set up an app integration with Jira so you can create work items from Insights, allowing your team to track and resolve cloud cost issues faster. [Learn more.](https://docs.cloudzero.com/docs/jira-integration)
* **Analytics Dashboard Folders:** Organize dashboards into folders with customizable visibility settings for user groups, organization-wide access, or private use, ensuring users only see the information relevant to them. [Learn more.](https://docs.cloudzero.com/docs/edit-dashboard#managing-folders)
* **CloudZero Agent for Kubernetes v1.1.0:** Leverage an in-cluster collector application that provides end-to-end telemetry tracking, seamless API key rotation, customizable upload intervals, and simplified integration. [Learn more.](https://github.com/Cloudzero/cloudzero-charts/releases/tag/1.1.0)
* **Quick Link to Platform Status:** Quickly access CloudZero's [status page](https://status.cloudzero.com/) from the question mark drop-down menu in the top navigation of the app.

# March 2025

* **Multiple API Keys:** Create and manage API keys with finely scoped permissions for improved security, flexibility, and usage tracking. [Learn more.](https://docs.cloudzero.com/reference/authorization)
* **Insights And Anomalies By Groups:** Users in limited access groups can now view Insights and Anomalies. [Learn more.](https://docs.cloudzero.com/docs/user-groups#limited-access-permissions)
* **Filter Insights And Anomalies By Dimension:** Use dimension filters to view only the Insights and Anomalies directly associated with a custom or core dimension, such as product or provider account. [Learn more.](https://docs.cloudzero.com/docs/insights#filtering-and-sorting)

# [February 2025](https://www.cloudzero.com/blog/product-release-notes-february-2025/)

* **Kubernetes Labels And Annotations**: Enables selective ingestion of specific Kubernetes labels and annotations with granular control over metadata from various Kubernetes resources. [Learn more.](https://docs.cloudzero.com/docs/k8s-advanced-configuration-labels-and-annotations)
* **Anomaly Resource Breakdown**: Provides deeper visibility into cost anomalies by displaying specific resources contributing to cost issues, helping users quickly pinpoint and resolve unexpected spending. [Learn more.](https://docs.cloudzero.com/docs/anomaly-detection#viewing-anomalies)
* **Enhanced Proportional Allocation Flexibility**: Offers more granular time-based allocation options with the ability to allocate costs monthly and specify cost types for improved financial tracking. [Learn more](/docs/allocation-short-form-rules#allocationmethod-proportional).
* **Automatically Fill Gaps In Telemetry Streams**: Automatically populates missing timestamps in cost and usage data by using the most recent available timestamp to ensure continuous and consistent reporting. [Learn more.](https://docs.cloudzero.com/docs/csv-import-telemetry)

# [January 2025](https://www.cloudzero.com/blog/product-release-notes-january-2025/)

* **Amazon Q Developer Chat Integration**: Introduces a CloudZero plugin for Amazon Q chat that enables accessing cost insights directly in the AWS Management Console. [Learn more.](https://docs.cloudzero.com/docs/amazon-q-integration)
* **OpenAI Integration**: Allows customers to easily pull in OpenAI spend data and analyze costs by project or AI model, providing greater visibility and optimization opportunities.
* **AWS Auto Insights - S3 API Costs**: Provides alerts when API request costs exceed 80% of S3 bucket spend, recommending moving high-access data to Standard storage tier. [Learn more.](https://docs.cloudzero.com/docs/high-ratio-of-s3-api-costs-to-storage-costs)
* **AWS Auto Insights - Glacier Storage**: Highlights excessive data retrieval costs in Glacier storage, suggesting moving active data to Standard storage tier. [Learn more.](https://docs.cloudzero.com/docs/high-data-retrieval-costs-for-s3-glacier-storage?_gl=1*15i2y5z*_gcl_au*NDYzMjEzMTc2LjE3MzQ2NDI3NjA.)

# [December 2024](https://www.cloudzero.com/blog/product-release-notes-december-2024/)

* **Cost Type Access By Group**: Introduces granular data access controls allowing user groups to limit visible cost types and set default cost types. [Learn more.](https://docs.cloudzero.com/docs/user-groups#access-to-cost-types)
* **SSO Integration Enhancements**: Provides a unified view of SSO integrations with improved management and testing capabilities. [Learn more.](https://docs.cloudzero.com/docs/authentication)
* **AWS Auto Insight - IPv4 Addresses**: Identifies costs associated with AWS-provided IPv4 addresses, indicating opportunities to reduce unnecessary costs and providing suggestions for how to eliminate or optimize costs related to public IPv4 addresses in your AWS environment. [Learn more.](https://docs.cloudzero.com/docs/consider-eliminating-spend-on-ipv4-addresses)
* **AWS Auto Insight - Lifecycle Rules for S3**: Identifies when there are S3 buckets with spend only on Standard Storage, indicating that use of Intelligent-Tiering or Lifecycle policies could be applied to reduce cost. By leveraging S3 Intelligent-Tiering or S3 Lifecycle, customers can save up to 10% on storage costs. [Learn more.](https://docs.cloudzero.com/docs/consider-intelligent-tiering-or-lifecycle-rules-for-s3)

# [November 2024](https://www.cloudzero.com/blog/product-release-notes-november-2024/)

* **AWS Support Amortization**: Enables proportional spreading of AWS monthly support charges across different business units with activation by FinOps Account Manager.
* **CSV Import → API Example Template**: Automatically provides API URL and JSON template for CSV file uploads to simplify automated data ingestion for [unit cost metric telemetry streams](https://docs.cloudzero.com/docs/csv-import-telemetry#view-example-unit-cost-metric-api-payload) and [allocation telemetry streams](https://docs.cloudzero.com/docs/csv-import-telemetry#view-example-allocation-api-payload)
* **AnyCost API Public Repo Examples**: Releases a public GitHub repository with example integrations to help admins build custom cost data adaptors from various cloud providers. [Learn more.](https://github.com/Cloudzero/cloudzero-anycost-example)

# Release notes archive

[Release Notes Archive](https://www.cloudzero.com/search/release+notes/)
