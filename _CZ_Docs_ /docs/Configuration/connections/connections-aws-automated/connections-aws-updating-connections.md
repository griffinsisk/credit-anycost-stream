---
title: Updating an AWS Account Connection Stack
category: getting-started
createdAt: '2023-03-06T19:39:05.363Z'
hidden: false
slug: connections-aws-updating-connections
updatedAt: '2023-03-06T19:39:05.363Z'
---
Sometimes it is necessary to update AWS Connection Stacks. For example, AWS updated their [Billing and Cost Management Permissions](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/) in January 2023.

You are in complete control of the permissions you grant CloudZero. Neither the automated nor manual [Connections](doc:connections) can update themselves.

CloudZero maintains the [Provision Account Open Source repository](https://github.com/Cloudzero/provision-account/tree/develop/policies) so you can review all of the CloudZero permissions. In addition, CloudZero publishes useful resources, policies, and CloudFormation templates from that repository to S3 for your use. This document covers a few workflows for updating your CloudZero permissions using those resources.

# Automated Connections

If you connected to CloudZero using [Automated Connections](doc:connections-aws-automated). you can use these steps to update the `cloudzero-connected-account` CloudFormation Stack.

## Console

1. Open the AWS CloudFormation Console in the appropriate AWS Account.
2. Select the `cloudzero-connected-account` stack.
3. If you do not see the stack right away in the list, first uncheck the **View Nested** radio button to the right of the search box and then search for `cloudzero`.
4. Click **Update**.
5. Select **Replace current template**.
6. Paste `https://cz-provision-account.s3.amazonaws.com/latest/services/connected_account.yaml` into the Amazon S3 URL Text Box.
7. Click **Next** three times.
8. At the bottom of the screen, check the boxes for CAPABILITIES:
   ```
   [✅] I acknowledge that AWS CloudFormation might create IAM resources with custom names.
   [✅] I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND
   ```
9. Click **Submit**.

## CLI

<Callout icon="ℹ️">
  The AWS CLI `update-stack` command does not have an option to `keep existing Parameters`.
  The following `bash` snippet will do that for you. It requires these commands be present in your shell: [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [jq](https://stedolan.github.io/jq/download/) command.
</Callout>

```bash
aws cloudformation update-stack \
  --stack-name cloudzero-connected-account \
  --template-url https://cz-provision-account.s3.amazonaws.com/latest/services/connected_account.yaml \
  --parameters "$(aws cloudformation describe-stacks --stack-name cloudzero-connected-account | jq '.Stacks[0].Parameters')"
```

# Manual Connections

## Console

1. Open the IAM Role Console in the appropriate AWS Account.
2. Find the Cross Account Role with a trust relationship with CloudZero.
   1. You can do this by searching your Roles for `cloudzero`. Select the one with `Trusted entities` containing `Account: 061190967865`.
   2. Click on the role name hyperlink.
3. Update Inline Policy
   1. On the Permissions tab of the Role page, click on the attached **Customer inline** policy.
   2. Click on the **JSON** tab.
   3. Copy the contents of the appropriate policy, [payer](https://cz-provision-account.s3.amazonaws.com/latest/policies/master_payer.json) or [resource owner](https://cz-provision-account.s3.amazonaws.com/latest/policies/resource_owner.json), into the text editor.
   4. Click **Review policy**.
   5. Click **Save changes**.
4. Add `AWSBillingReadOnlyAccess` managed policy.
   1. On the Permissions tab of the Role page, click on the attached **Add permissions** button and from the drop-down list, select **Attach Policies**.
   2. Search for `AWSBillingReadOnlyAccess`.
   3. Check the box to the left of the policy name.
   4. Click **Add permissions**.

## CLI

<Callout icon="ℹ️">
  It takes a few commands to find and update roles and their policies.
  The following `bash` snippet will do that for you. It requires these commands be present in your shell: [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [jq](https://stedolan.github.io/jq/download/).
</Callout>

```bash
# Find roles with Trust Relationships with CloudZero
aws iam list-roles | jq -r -e '.Roles | map(select(.AssumeRolePolicyDocument.Statement[0].Principal.AWS == "arn:aws:iam::061190967865:root")) | map(.RoleName)[] | .'

# For each of the roles from the output of the previous command
aws iam list-role-policies --role-name <role-name> | jq -r -e '.PolicyNames[]'

# Now we have the list of policies to update
# For each role and policy:
aws iam put-role-policy \
  --role-name <role-name> \
  --policy-name <policy-name> \
  --policy-document "$(curl -XGET https://cz-provision-account.s3.amazonaws.com/latest/policies/resource_owner.json)"  # change resource_owner.json to master_payer.json if this is a billing account role and policy

# And we attach the AWSBillingReadOnlyAccess managed policy to your role
aws iam attach-role-policy \
  --role-name <role-name> \
  --policy-arn arn:aws:iam::aws:policy/AWSBillingReadOnlyAccess
```
