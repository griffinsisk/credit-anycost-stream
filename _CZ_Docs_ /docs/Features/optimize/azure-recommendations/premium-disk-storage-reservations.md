---
title: Purchase Azure Premium Disk Reservations
category: features
createdAt: '2024-09-03T12:44:28.000Z'
hidden: false
slug: premium-disk-storage-reservations
updatedAt: '2024-09-03T12:44:28.000Z'
---
This Recommendation is created when there is pay-as-you-go spend for Azure Premium Disk Storage that could be covered by a reservation for storage resources. Learn more about these reservations [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-reserved-capacity).

**Threshold**: This Recommendation is created if using a reservation on pay-as-you-go Premium Disk Storage will save at least $500 based on a 5% savings rate. When pay-as-you-go spend results in savings of less than $500, the Recommendation will automatically be closed.

Reservations work as follows:

* The SKU of a premium SSD determines the disk's size and performance.
* When determining your storage needs for a reservation, think of the total number of disks per SKU needed across your desired scope.
* A disk reservation is made per disk SKU. As a result, the reservation consumption is based on the unit of the disk SKUs instead of the provided size.

When purchasing a reservation in Azure, you must specify the following:

* **Billing Subscription**: Subscription used to pay for the Azure Disk Storage reservation.
* **Scope**: The reservation's scope can cover one subscription, multiple subscriptions (shared scope), a single resource group, or a management group.
* **Disks**: The SKU you want to create.
* **Region**: The Azure region covered by the capacity reservation.
* **Billing Frequency**: Upfront or monthly.

Learn more about buying a reservation [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-reserved-capacity#buy-a-disk-reservation)

Analyze your usage information to help determine which reservations you should purchase. Make sure to track the usage in disk SKUs instead of provisioned or used disk capacity. Learn more about determining the correct reservation size [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-reserved-capacity#determine-your-storage-needs).

The following details are important to note:

* **Disk and VM Reservations**: Examine your disk reservation along with your VM reservation. Azure highly recommends making reservations for both VM usage and disk usage for maximum savings.
* **Applicable Disks**: Reservations apply only to premium SSDs above size P30.
* **Reservation Flexibility**: You can cancel, exchange, or refund reservations with certain limitations. Learn more [in the Microsoft documentation](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/exchange-and-refund-azure-reservations).
* **Purchase Restrictions**: Azure Disk Storage reservation discounts don't apply to unmanaged disks, ultra disks, or page blob consumption. Learn more about purchase restrictions [here](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-reserved-capacity#purchase-restrictions).
* **Savings calculation**: The savings multiplier used to calculate the cost impact for this Recommendation represents the savings achieved when applying a reservation to a non-Enterprise Account resource cost.

The 90-day cost graph shows the daily total spend for all P30, P40, P50, P60, P70, and P80 Premium Disks Storage and highlights the top five resources with the highest spend to consider optimizing.
