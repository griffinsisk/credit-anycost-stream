---
title: 'CostFormation: Allocating Shared Costs'
category: features
createdAt: '2022-01-20T18:18:50.938Z'
hidden: false
slug: costformation-allocating-shared-costs
updatedAt: '2022-02-28T14:54:33.659Z'
---
Custom Dimensions allow you to organize your cloud costs by grouping resources together in ways that make the most sense for your business. However, when a resource is shared by multiple systems, such as customers, products or tenants, it becomes necessary to split the cost across multiple systems. For example, an RDS database that is used by multiple products should not have its cost entirely assigned to only one product.

You can allocate this cost by using **Allocation Dimensions**. This is a type of Custom Dimension created using the CostFormation definition language. All allocation is based on real cost. There are **Rules Allocation Dimensions** and **Telemetry Allocation Dimensions**.

You can use **Rules Allocation Dimensions** to split shared costs across the elements of another Dimension, for example, to split the cost of a shared database among the products using the database, proportional to the relative cost for each product, or to split a system-wide operational cost evenly across a number of engineering teams. Rules Allocation Dimensions provide a way to split costs to increase your cloud cost visibility without further engineering work.

You can use **Telemetry Allocation Dimensions** to split shared costs among different target elements based on additional telemetry data provided to the CloudZero platform. Telemetry Allocation Dimensions provide for granular control over how the shared costs are split, for example, to split the cost according to a utilization metric.

To learn more about Allocation Dimensions, see the following documentation:

* [Split Shared Costs Using Rules](doc:split-shared-costs-proportionally): Split a shared cost using a proportional Rules Allocation Dimension, which allows you to split the shared cost relative to other costs in another dimension.
* [Split Shared Costs Using Telemetry](doc:split-shared-costs-using-allocation-dimensions): Split a shared cost into new elements using a telemetry stream.
* [Combining Dedicated and Shared Cost](doc:combining-dedicated-and-shared-cost): Combine the split shared cost with an existing dedicated cost.

<br />
