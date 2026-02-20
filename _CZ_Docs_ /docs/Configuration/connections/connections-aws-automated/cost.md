---
title: Cost Allocation Tagging Configuration for AWS
category: getting-started
createdAt: '2020-02-13T23:52:44.587Z'
hidden: false
slug: cost
updatedAt: '2021-09-10T16:17:46.865Z'
---
Tags are a Dimension that you can use to break your cost data down in CloudZero. Tags allow you to look at Dimensions of your cost spending that are relevant to your business. However, by default, AWS does not include tags in the billing data.

Follow these steps to include an AWS Tag in the billing data to allow the tag to be a Dimension for filtering and grouping on in the CloudZero Explorer.

1. Log in to the AWS console and navigate to [https://console.aws.amazon.com/billing/home](https://console.aws.amazon.com/billing/home).

2.  From the left navigation, select **Cost allocation tags**.

<Image align="center" alt="Cost Allocation Tags in AWS" className="border" border={true} src="https://files.readme.io/ca731cb-cost_allocation_tags_in_aws.png" />

3. Click the **Activate** button to activate **AWS-Generated Cost Allocation Tags** if the feature is not already activated.

4. On the **Activate** tab, search for and select new tags to be included in your bill.

Select the tags that are most relevant to your company. Consider the following tags, which can be useful in understanding your spending. CloudZero recommends adding these tags here if they exist in your environment.

* Name
* aws:createdby
* aws:autoscaling:groupname
* aws:cloudformation:logical-id
* aws:cloudformation:stack-name
* aws:ecs:clustername
* aws:ecs:servicename
* aws:elasticmapreduce:instance-group-role
* aws:elasticmapreduce:job-flow-id
* eks:cluster-name
* eks:nodegroup-name
