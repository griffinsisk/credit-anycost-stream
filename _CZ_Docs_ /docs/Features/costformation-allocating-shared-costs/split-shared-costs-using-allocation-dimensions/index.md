---
title: Split Shared Costs Using Telemetry
category: features
createdAt: '2022-01-11T20:54:28.872Z'
hidden: false
slug: split-shared-costs-using-allocation-dimensions
updatedAt: '2022-02-08T15:42:08.322Z'
---
This guide explains how to split shared costs using telemetry data using Explicit Allocation Dimensions in CostFormation. Terminology is explained throughout the guide.

# Problem to solve

For the purpose of this exercise, we will assume we are working for a SaaS business that thinks of itself as a collection of Products, A, B, and C. Thus, from a cost of goods sold (COGS) perspective, this business must understand the cost of each Product.

<Image align="center" alt="RDS storage cost allocation" src="https://files.readme.io/284a42d4c8cf018ae6fecc57ce1588b3e460bcedcf0ed5dee9d26b4570c6289a-RDS-storage-costs-alloc-Screen_Shot_2022-02-03.png" />

The challenge we face is that our business has some RDS storage costs in a database, and these costs should be allocated among the Pproducts based on how much storage each Product uses. We will solve this problem by using Telemetry Streams to allocate those RDS storage costs to Products and improve the accuracy of our cost reporting from a COGS perspective.

# Steps to a solution

For a look at the complete CloudFormation and telemetry records, see [Reviewing our Work](doc:reviewing-our-work) now.  The remaining pages in this section explain what to do in detail.

<br />
