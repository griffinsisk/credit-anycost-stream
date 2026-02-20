---
title: Purchase Azure SQL Database Reservations
category: features
createdAt: '2024-09-16T14:49:37.000Z'
hidden: false
slug: sql-database-reservations
updatedAt: '2024-09-16T13:49:37.000Z'
---
This Recommendation is created when there is pay-as-you-go spend for Azure SQL Database or SQL Managed Instance, or both, that could be covered by a reservation for compute resources.

**Threshold**: This Recommendation is created if using a reservation on a pay-as-you-go SQL Database will save at least $500 based on a 25% savings rate. When pay-as-you-go spend results in savings of less than $500, the Recommendation will automatically be closed.

Reservations work as follows:

* A reservation is a commitment for SQL Database, a SQL Managed Instance use, or both, for a period of one or three years to get a significant discount on the compute costs.
* Existing deployments that are already running, or ones that are newly deployed automatically, that match the criteria set for the reservation will get the benefit. You do not need to assign the reservation to a specific database or managed instance.

When you are purchasing a reservation in Azure, you must specify the following:

* **Scope**: The vCore reservation's scope can cover one subscription, multiple subscriptions (shared scope), a single resource group, or a management group.
* **Region**: The Azure region that's covered by the capacity reservation.
* **Deployment Type**: The SQL resource type that you want to buy the reservation for.
* **Performance Tier**: The service tier for the databases or managed instances.
* **Term**: 1 or 3 years.
* **Quantity**: The number of vCores to reserve in the selected Azure region and Performance Tier.

Learn more about buying a reservation [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/prepare-buy-reservation?source=recommendations).

Reservations are best for workloads that have consistent resource usage across a similar deployment type.

The size of the reservation should be based on the total amount of compute used by the existing or soon-to-be-deployed database or managed instance within a specific region and using the same performance tier and hardware configuration. Learn more about how to determine the correct reservation size [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/azure-sql/database/reserved-capacity-overview?view=azuresql#determine-the-correct-size-before-purchase).

Note the following details:

* **Reservation Limitations**: Not all configurations support reservations. Learn about limitations [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/azure-sql/database/reserved-capacity-overview?view=azuresql#limitation).
* **Reservation Coverage**: A reservation applies to both primary and billable secondary compute replicas, but does not cover software, networking, or storage charges associated with the service.
* **Infrastructure Changes**: Purchasing a reservation for an existing resource does not modify its infrastructure or trigger a failover or downtime.
* **Upfront Payment**: Reservations are charged upfront  through the subscription specified.
* **Reservation Flexibility**: You can cancel, exchange, or refund reservations with certain limitations. Learn more [here](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/exchange-and-refund-azure-reservations)in the Microsoft documentation.
* **Role Requirements**: To buy a reservation, you must have the Owner role or Reservation Purchaser role on an Azure subscription.
* **Savings Calculation**: The savings multiplier used to calculate the cost impact for this Recommendation represents the savings achieved in applying a reservation to a non-Enterprise Account resource cost.

The 90-day cost graph shows the daily total spend for all SQL Databases and highlights the top five resources with the highest spend to consider optimizing.
