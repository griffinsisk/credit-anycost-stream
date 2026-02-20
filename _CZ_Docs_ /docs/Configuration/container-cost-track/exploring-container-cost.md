---
title: Exploring Kubernetes Cost
category: features
createdAt: '2022-01-05T15:24:58.439Z'
hidden: false
slug: exploring-container-cost
updatedAt: '2024-11-01T15:24:58.439Z'
---
Kubernetes cost allocations will appear in CloudZero the next billing data ingestion for your cost source. After that, you can [view cost allocation data](#view-cost-allocations-in-the-explorer) in the [Explorer](https://app.cloudzero.com/explorer) and [view a list of clusters](#view-cluster-list) on the [Kubernetes Integration page](https://app.cloudzero.com/organization/k8s-integration).

# View Cost Allocations in the Explorer

You can filter and group costs by Kubernetes Dimensions in the CloudZero [Explorer](https://app.cloudzero.com/explorer). Viewing and filtering is available by namespace, cluster, workload, or label.

For example, in the following image, the **Group By** drop-down menu is set to the Kubernetes **Cluster** Dimension:

<Image align="center" alt="Costs grouped by Kubernetes cluster in the Explorer" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-group-by-k8s-cluster.png" className="border" />

To group by a different Dimension, select the **Group By** drop-down menu and choose a different Dimension.

After you have grouped by a Kubernetes Dimension, you can set a filter to further narrow the view:

1. In the Explorer, click **+ Add**.
2. Choose a Dimension from the drop-down list. Kubernetes Dimensions include **cluster**, **namespace**, **workload**, and **label keys**.
3. Choose one or more Dimension values from the drop-down list.
4. Optionally, select the `is` operator and choose a different operator (`is not`, `contains`, `does not contain`) for the filter. For example, select `is not` to show only costs that _do not match_ the selected dimension value(s).
5. Optionally, repeat the previous steps to filter by additional Dimensions.
6. Select **Apply**.

In the following example, as shown in the image, the allocated costs are filtered to show only existing clusters within the `kube-system` namespace:

<Image align="center" alt="Costs grouped by Kubernetes cluster and filtered by namespace in the Explorer" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-group-by-k8s-cluster-filtered.png" className="border" />

# View Cluster List and Details

To view a list of Kubernetes clusters connected to CloudZero, navigate to **Settings** > **Kubernetes Integration**. The [Kubernetes Integration](https://app.cloudzero.com/organization/k8s-integration) page opens, showing the following information for each cluster:

* **Cluster name**
* **Account ID**
* **Request Activity** graph
* **Last Ingest**
* **Agent Version**
* **Status** (**Connected** or **Disconnected**, or **Upgrade Required**.)

You can search cluster names or account IDs, filter the list by cluster status, or both. You can use the **Setup Instructions** button to display the Helm commands to connect a Kubernetes cluster.

Click on a cluster name to display the Cluster Details page for that cluster.

This page shows the **Kubernetes Version**, **Node Count**, **Region**, **Pod Count**, **Account ID**, and date and time of **Last Ingest Success**. A graph showing the number of files received over the last 30 days is provided.

**Agent Details** are also provided: **Agent Info**, **Kube State Metrics**, **CAdvisor**, **SSL Certificate**, **Insights Controller**, **Labels**, and **Annotations**. You can click the **Open in Explorer** button to see the cluster details in the Explorer.

<br />
