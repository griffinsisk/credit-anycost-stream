---
title: Split Shared Costs Using Rules
category: features
createdAt: '2022-02-01T16:29:31.329Z'
hidden: false
slug: split-shared-costs-proportionally
updatedAt: '2022-02-28T14:57:14.018Z'
---
This guide explains how to split shared costs using a Rules Allocation Dimension.

# Problem to solve

For the purposes of this exercise, we will assume we are working for a SaaS business that sells three distinct products. This business needs to understand the cost of each product to better understand their cost of goods sold (COGS).

<Image align="center" src="https://files.readme.io/7647faac678f0bf42635986daea989c66f7f304147b14f603fa40deb791ad05e-split-shared-costs-walkthrough.png" />

The challenge is that our business has a RDS cluster that is used by all three products. In this example, we will use a Rules Allocation Dimension to allocate those RDS costs to Products and improve the accuracy of our cost reporting, without any engineering work or additional data.

In concrete terms, we want to allocate the RDS Database to each product relative to that product's cost.

<Image align="center" src="https://files.readme.io/b4e647c51420df646a7772ff409d66dfba74980511a0267de2a77e103fe5fd5c-split-shared-costs-rules-walkthrough.png" />

<Callout icon="ℹ️" theme="info">
  For the purposes of this exercise, we will assume we have already created a Dimension called `SingleTenantProduct` that describes the spend of Product A, Product B, and Product C.

  Setting the View as the default Dimension allows you to easily select it in your analysis.
</Callout>

# What we will build

To see the complete CloudFormation, look at the page [Reviewing our Rules-Based Proportional Split](doc:reviewing-our-proportional-split) now.  The next steps will go over the parts of this in detail.
