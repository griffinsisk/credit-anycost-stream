---
title: Purchase Azure Redis Cache Reservations
category: features
createdAt: '2024-09-06T16:48:35.000Z'
hidden: false
slug: redis-cache-reservations
updatedAt: '2024-09-11T13:49:37.000Z'
---
This Recommendation is created when there is pay-as-you-go spend for Azure Cache for Redis that could be covered by a reservation for compute resources. Learn more about these reservations [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-reserved-pricing).

**Threshold**: This Recommendation is created if using a reservation on pay-as-you-go Redis Cache will save at least $500 based on a 25% savings rate. When pay-as-you-go spend results in savings of less than $500, the Recommendation will automatically be closed.

Reservations work as follows:

* The size of the reservation should be based on the total amount of memory used by the existing or soon-to-be-deployed cache within a specific region, and using the same service tier.
* Premium and Enterprise Caches have two nodes by default, while Enterprise Flash has three nodes.
* Reservations are sold in increments of nodes. Use the [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/) to calculate the number of nodes needed based on the number of hours to cover with a reservation.

When you are purchasing a reservation in Azure, you must specify the following:

* **Subscription**: Subscription used to pay for the Azure Cache for Redis reservation.
* **Scope**: The reservation's scope can cover one subscription, multiple subscriptions (shared scope), a single resource group, or a management group.
* **Region**: The Azure region that is covered by the capacity reservation.
* *_Pricing Tier_: The service tier for the instances.
* **Term**: 1 or 3 years.
* *_Quantity_: The number of nodes to reserve in the selected Azure region and Pricing Tier.

Learn more about buying a reservation [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-reserved-pricing#buy-azure-cache-for-redis-reservations).

Analyze your usage information to help determine which reservations you should purchase. Learn more about how to determine the correct reservation size [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-reserved-pricing#determine-the-right-cache-size-before-purchase).

Note the following details:

* **Applicable Tiers**: Reservations are only available for Premium, Enterprise, and Enterprise Flash Redis Cache tiers.
* **Reservation Flexibility**: You can cancel, exchange, or refund reservations with certain limitations. Learn more [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/exchange-and-refund-azure-reservations).
* **Role Requirements**: To buy a reservation, you must have the Owner role or Reservation Purchaser role on an Azure subscription.
* **Savings Calculation**: The savings multiplier used to calculate the cost impact for this Recommendation represents the savings achieved in applying a reservation to a non-Enterprise Account resource cost.

The 90-day cost graph shows the daily total spend for all instances with a Premium, Enterprise, or Enterprise Flash Redis Cache tier and highlights the top five resources with the highest spend to consider optimizing.
