---
title: AWS Savings Plans Purchase Recommendations for Amazon SageMaker AI
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: AWS_Savings_Plans_purchase_recommendations_for_Amazon_SageMaker_AI
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisite:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
</Callout>

Amazon SageMaker Savings Plans offer significant savings on SageMaker usage in exchange for a commitment to a consistent amount of usage (measured in $/hour) for a one or three year term. AWS Trusted Advisor analyzes your SageMaker usage patterns and provides recommendations for purchasing Savings Plans that could reduce your costs.

# How to remediate

1. Review the recommended Savings Plan commitment amount and term
2. Navigate to the AWS Cost Management console
3. Go to Savings Plans > Purchase Savings Plans
4. Select SageMaker Compute as the Savings Plans type
5. Enter the recommended commitment amount
6. Choose the appropriate term (1-year or 3-year)
7. Select the payment option (All Upfront, Partial Upfront, or No Upfront)
8. Review and complete the purchase

# Additional context

* Savings Plans provide flexibility to change instance families, sizes, operating systems, and regions
* Longer commitment terms (3 years) typically offer higher savings rates
* All Upfront payment provides the highest discount
* Savings Plans automatically apply to eligible usage across your AWS account
* You can stack multiple Savings Plans to match your usage patterns
