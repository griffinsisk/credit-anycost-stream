---
title: Purchase Azure PostgreSQL Database Reservations
category: features
createdAt: '2024-09-07T10:32:57.000Z'
hidden: false
slug: postgresql-database-reservations
updatedAt: '2024-09-07T10:32:57.000Z'
---
This Recommendation is created when there is pay-as-you-go spend for Azure Database for PostgreSQL Single Server or Azure Database for PostgreSQL Flexible Server that could be covered by a reservation for compute resources.

**Threshold**: This Recommendation is created if using a reservation on pay-as-you-go Databases for PostgreSQL will save at least $500 based on a 25% savings rate. When pay-as-you-go spend results in savings of less than $500, the Recommendation will automatically be closed.

Reservations work as follows:

* A reservation is a commitment for PostgreSQL Single Server or Azure Database for PostgreSQL Flexible Server use for a period of one or three years to get a significant discount on the compute costs.
* Existing deployments that are already running, or ones that are newly deployed automatically, that match the criteria set for the reservation will get the benefit. You do not need to assign the reservation to a specific database or managed instance.

When you are purchasing a reservation in Azure, you must specify the following:

* **Scope**: The vCore reservation's scope can cover one subscription, multiple subscriptions (shared scope), a single resource group, or a management group.
* **Region**: The Azure region covered by the capacity reservation.
* **Deployment Type**: The Azure Database for the PostgreSQL Flexible Server resource type that you want to buy the reservation for.
* **Performance Tier**: The service tier for the PostgreSQL Flexible Server instances.
* **Term**: 1 or 3 years.
* **Quantity**: The number of vCores to reserve in the selected Azure region and Performance Tier.

Learn more about buying a reservation [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/prepare-buy-reservation?source=recommendations).

The size of reservation should be based on the total amount of compute used by the existing or soon-to-be-deployed database or managed instance within a specific region and using the same performance tier and hardware generation. Learn more about how to determine the correct reservation size [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-reserved-pricing#determining-the-right-server-size-before-purchase).

The following details are important to note:

* **PostgreSQL Single Server Retirement**: Azure Database for PostgreSQL Single Server is being retired. Azure strongly recommends upgrading to Azure Database for PostgreSQL Flexible Server.
  * New reservations will not be available for Azure Database for PostgreSQL Single Server. Your existing single server reservations remain valid, and you can still purchase reservations for Azure Database for PostgreSQL Flexible Server.
  * For more information about migrating to Azure Database for PostgreSQL Flexible Server, see [the Microsoft documentation](https://learn.microsoft.com/en-us/azure/postgresql/single-server/whats-happening-to-postgresql-single-server).
* **Reservation Flexibility**: You can cancel, exchange, or refund reservations with certain limitations. Learn more [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/exchange-and-refund-azure-reservations).
* **Role Requirements**: To buy a reservation, you must have the Owner role or Reservation Purchaser role on an Azure subscription.
* **Reservation Coverage**: A reservation applies to both primary and billable secondary compute replicas, but does not cover software, networking, or storage charges associated with the service.
* **No Impact on Existing Infrastructure**: Purchasing a reservation for an existing resource does not modify its infrastructure or trigger a failover or downtime.
* **Savings Calculation**: The savings multiplier used to calculate the cost impact for this Recommendation represents the savings achieved in applying a reservation to a non-Enterprise Account resource cost.

The 90-day cost graph shows the daily total spend for all Databases for PostgreSQL and highlights the top five resources with the highest spend to consider optimizing.
