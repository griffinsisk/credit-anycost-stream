---
title: Recommendations for AWS
category: features
createdAt: '2024-06-24T13:00:00.000Z'
hidden: false
metadata:
  title: 'AWS Recommendations'
slug: aws-recommendations
---
<Callout icon="ℹ️" theme="info">
  **Source for Recommendations:** Spend data in the CloudZero platform.

  **Frequency:** Checked once per day. If the Recommendation is marked as **Ignored**, it will still be updated, but notifications will no longer be sent for any updates.
</Callout>

CloudZero provides the following Recommendations for AWS:

## Artificial Intelligence

### SageMaker

* [AWS Savings Plans Purchase Recommendations for Amazon SageMaker AI](/docs/aws-savings-plans-purchase-of-amazon-sagemaker-ai): Identifies AWS Savings Plans purchase opportunities for Amazon SageMaker. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).

## Compute

### EC2

* [Amazon EC2 Instance Consolidation for Microsoft SQL Server](/docs/amazon-ec2-instances-consolidation-for-microsoft-sql-server): Identifies opportunities to consolidate Microsoft SQL Server licenses on Amazon EC2 instances.
* [Amazon EC2 Instance Over-Provisioned for Microsoft SQL Server](/docs/amazon-ec2-instances-over-provisioned-for-microsoft-sql-server): Identifies EC2 instances running Microsoft SQL Server that have more vCPUs than needed.
* [Amazon EC2 Instances Stopped](/docs/amazon-ec2-instances-stopped): Identifies Amazon EC2 instances that are currently stopped and may be candidates for termination.
* [Amazon EC2 Migrate to Graviton](/docs/amazon-ec2-migrate-to-graviton): Identifies EC2 instances that can be migrated to Graviton-based instances for cost optimization. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon EC2 Reserved Instance Lease Expiration](/docs/amazon-ec2-reserved-instances-lease-expiration): Identifies Amazon EC2 Reserved Instances that are approaching their lease expiration date.
* [Amazon EC2 Reserved Instance Optimization](/docs/amazon-ec2-reserved-instance-optimization): Identifies EC2 Reserved Instance optimization opportunities.
* [Amazon EC2 Rightsize Instances](/docs/amazon-ec2-rightsize-instances): Identifies EC2 instances that should be rightsized to optimize cost and performance. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon EC2 Stop Instances](/docs/amazon-ec2-stop-instances): Identifies EC2 instances that should be stopped to reduce costs. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon EC2 Upgrade Instances](/docs/amazon-ec2-upgrade-instances): Identifies EC2 instances that should be upgraded to newer generation instances for cost optimization. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Delete EBS Snapshot Older Than 180 Days](/docs/active-ec2-snapshots-older-than-90-days): Identifies EC2 snapshots that are older than 90 days and are still actively incurring costs.
* [EC2 Cross-Region Data Transfer](/docs/excessive-ec2-cross-region-data-transfer): Identifies AWS accounts where EC2 cross-region data transfer costs exceed 10% of total EC2 data transfer costs.
* [EC2/ELB Internet Traffic Bypassing CloudFront](/docs/excessive-ec2-elb-internet-traffic-bypassing-cloudfront): Identifies AWS accounts using CloudFront CDN but with significant direct internet egress from EC2/ELB.
* [Older Generation Instances](/docs/older-generation-instances-detected): Detects that the total real cost spend for the identified Amazon EC2, RDS, and ElastiCache older generation instances is at least $500.

### ECR

* [Configure ECR Repository Lifecycle Policy to Reduce Storage Costs](/docs/amazon-ecr-repository-without-lifecycle-policy): Identifies Amazon ECR repositories that do not have lifecycle policies configured.

### ECS/Fargate

* [AWS Fargate Cost Optimization Delete Recommendations for Amazon ECS](/docs/aws-fargate-service-deletion-for-amazon-ecs): Identifies unused or idle AWS Fargate services that should be deleted.
* [AWS Fargate Cost Optimization Recommendations for Amazon ECS](/docs/aws-fargate-rightsizing-for-amazon-ecs): Identifies AWS Fargate services with over-provisioned CPU or memory allocations. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).

### EKS

* [EKS Extended Support Charges](/docs/eks-clusters-incurring-extended-support-charges): Identifies Amazon EKS clusters incurring extended support charges for using Kubernetes versions that have reached end-of-standard-support.

### Lambda

* [AWS Lambda Cost Optimization Recommendations for Functions](/docs/aws-lambda-functions): Identifies AWS Lambda functions that have cost optimization opportunities. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Fix Lambda Function with Excessive Error Rate](/docs/aws-lambda-functions-with-high-error-rates): Identifies AWS Lambda functions that are experiencing high error rates.
* [Fix Lambda Function with Excessive Timeouts](/docs/aws-lambda-functions-with-excessive-timeouts): Identifies AWS Lambda functions that are experiencing excessive timeouts.

### EMR Serverless

* [Migrate EMR Serverless to ARM (Graviton)](/docs/migrate-emr-serverless-to-arm-graviton): Identifies AWS accounts running EMR Serverless workloads on x86 architecture that could achieve significant cost savings by migrating to ARM-based Graviton processors.

### Multiple Services

* [AWS Savings Plans Purchase Recommendations for Compute](/docs/aws-savings-plans-purchase-for-compute): Identifies AWS Savings Plans purchase opportunities for compute resources. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).

## Databases

### Aurora

* [Amazon Aurora Delete Clusters](/docs/amazon-aurora-delete-clusters): Identifies Aurora clusters that should be deleted to reduce costs. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon Aurora Migrate to Graviton](/docs/amazon-aurora-migrate-to-graviton): Identifies Aurora clusters that can be migrated to Graviton-based instances for cost optimization. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon Aurora Rightsize Clusters](/docs/amazon-aurora-rghtsize-clusters): Identifies Aurora clusters that should be rightsized to optimize cost and performance. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon Aurora Upgrade Clusters](/docs/amazon-aurora-upgrade-clusters): Identifies Aurora clusters that should be upgraded to newer generation types for cost optimization. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).

### DynamoDB

* [Amazon DynamoDB Reserved Capacity Purchase Recommendations](/docs/amazon-dynamodb-reserved-capacity-purchase): Identifies Amazon DynamoDB reserved capacity purchase opportunities. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
* [Delete Inactive DynamoDB Tables](/docs/inactive-dynamodb-tables): Identifies DynamoDB tables that are incurring storage costs but show no usage activity.

### ElastiCache

* [Amazon ElastiCache Reserved Node Purchase Recommendations](/docs/amazon-elasticache-reserved-node-purchase): Identifies ElastiCache Reserved Node purchase opportunities. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).

### MemoryDB

* [Amazon MemoryDB Reserved Node Purchase Recommendations](/docs/amazon-memorydb-reserved-node-purchase): Identifies MemoryDB Reserved Node purchase opportunities. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).

### OpenSearch Service

* [Amazon OpenSearch Service Reserved Instance Purchase Recommendations](/docs/amazon-opensearch-service-reserved-instance-purchase): Identifies OpenSearch Service Reserved Instance purchase opportunities. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
* [Upgrade Elasticsearch to Avoid Extended Support Charges](/docs/elasticsearch-extended-support-charges): Identifies Elasticsearch clusters incurring extended support charges for using versions that have reached end-of-standard-support.
* [Upgrade OpenSearch to Avoid Extended Support Charges](/docs/opensearch-extended-support-charges): Identifies OpenSearch clusters incurring extended support charges for using versions that have reached end-of-standard-support.

### RDS

* [Amazon RDS Delete Instances](/docs/amazon-rds-delete-instances): Identifies RDS instances that should be deleted to reduce costs. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon RDS Migrate to Graviton](/docs/amazon-rds-migrate-to-graviton): Identifies RDS instances that can be migrated to Graviton-based instances for cost optimization. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon RDS Reserved Instance Purchase Recommendations](/docs/amazon-rds-reserved-instance-purchase): Identifies Amazon RDS Reserved Instance purchase opportunities. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
* [Amazon RDS Rightsize Instances](/docs/amazon-rds-rightsize-instances): Identifies RDS instances that should be rightsized to optimize cost and performance. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon RDS Storage Delete Recommendations](/docs/amazon-rds-storage-delete): Identifies Amazon RDS database instances with storage that can be deleted to reduce costs. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon RDS Storage Rightsize Recommendations](/docs/amazon-rds-storage-rightsize): Identifies Amazon RDS database instances with storage that can be rightsized to reduce costs. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon RDS Storage Upgrade Recommendations](/docs/amazon-rds-storage-upgrade): Identifies Amazon RDS database instances where storage can be upgraded to more cost-effective options. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon RDS Upgrade Instances](/docs/amazon-rds-upgrade-instances): Identifies RDS instances that should be upgraded to newer generation types for cost optimization. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [RDS Backup Retention](/docs/excessive-rds-backup-retention): Identifies Amazon RDS backups and manual snapshots retained beyond 90 days, potentially exceeding business or compliance requirements.
* [RDS Extended Support Charges](/docs/rds-clusters-incurring-extended-support-charges): Identifies Amazon RDS database instances and clusters running on outdated engine versions that incur AWS extended support charges.
* [RDS Snapshot Costs](/docs/rds-snapshot-costs-are-higher-than-expected): Created when the percentage of RDS snapshots exceeds 10% of the total RDS costs.

### Redshift

* [Amazon Redshift Reserved Node Purchase Recommendations](/docs/amazon-redshift-reserved-node-purchase): Identifies Redshift Reserved Node purchase opportunities. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
* [Underutilized Amazon Redshift Clusters](/docs/underutilized-amazon-redshift-clusters): Identifies Amazon Redshift clusters that are underutilized and could benefit from optimization.

## Management Tools

### CloudTrail

* [CloudTrail Redundant Usage](/docs/redundant-cloudtrail-usage-detected): Detects whether you are being charged for CloudTrail events.

### CloudWatch

* [CloudWatch Costs Higher Than Expected](/docs/expensive-cloudwatch-logs): Detects increases in CloudWatch costs.

## Networking & Content Delivery

### Network Firewall

* [Delete Inactive AWS Network Firewall](/docs/inactive-aws-network-firewall): Identifies AWS Network Firewalls that appear to be inactive and could be deleted to reduce costs.

### Elastic IP Addresses

* [Release Idle Elastic IP Addresses](/docs/release-idle-elastic-ip-addresses): Identifies Elastic IP addresses (EIPs) that are allocated but not associated with running resources and incur hourly charges.

### Elastic Load Balancing

* [Delete Idle Load Balancer](/docs/idle-classic-load-balancers): Identifies AWS Classic Load Balancers (ELBs) that are idle and can be deleted to reduce costs.
* [Delete Inactive Gateway Load Balancer Endpoint](/docs/inactive-gateway-load-balancer-endpoints): Identifies Gateway Load Balancer endpoints that appear to be inactive and could be deleted.

### NAT Gateway

* [Inefficient AWS NAT Gateway Detected](/docs/unused-nat-gateways-detected): Detects NAT Gateways that have hourly charges without appreciable corresponding data processing charges.
* [NAT Gateway Excessive Data Transfer](/docs/managed-nat-gateway-with-excessive-data-transfer): Identifies AWS NAT Gateways where data transfer costs represent an unusually high percentage of total gateway costs.

### VPC

* [Delete Inactive VPC Interface Endpoint](/docs/inactive-vcp-interface-endpoints): Identifies VPC interface endpoints that appear to be inactive and could be deleted to reduce costs.

## Storage

### EBS

* [Amazon EBS Delete Volumes](/docs/amazon-ebs-delete-volumes): Identifies EBS volumes that should be deleted to reduce costs. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon EBS Rightsize Volumes](/docs/amazon-ebs-rightsize-volumes): Identifies EBS volumes that should be rightsized to optimize cost and performance. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Amazon EBS Upgrade Volumes](/docs/amazon-ebs-upgrade-volumes): Identifies EBS volumes that should be upgraded to newer generation types for cost optimization. **Prerequisite:** Opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
* [Unarchived Old EBS Snapshots](/docs/unarchived-old-ebs-snapshots): Identifies Amazon EBS snapshots that have been stored for an extended period in standard snapshot storage and are candidates for EBS Snapshot Archive.

### S3

* [Configure S3 Lifecycle Policy to Abort Incomplete Multipart Uploads](/docs/amazon-s3-incomplete-multipart-upload-abort-configuration): Identifies Amazon S3 buckets that do not have lifecycle policies configured to automatically abort incomplete multipart uploads.
* [Consider Intelligent-Tiering or Lifecycle Rules for S3](/docs/consider-intelligent-tiering-or-lifecycle-rules-for-s3): Created when there are S3 buckets with spend only on Standard Storage.
* [High Data Retrieval Costs for S3 Glacier Storage](/docs/high-data-retrieval-costs-for-s3-glacier-storage): Identifies data retrieval costs for an S3 bucket occurring on an S3 Glacier storage tier.
* [High Non-Standard API Requests for S3](/docs/non-standard-api-requests-for-s3-exceed-threshold): Identifies high spend on non-standard API requests to S3.
* [High Ratio of S3 API Cost to Storage Cost](/docs/high-ratio-of-s3-api-costs-to-storage-costs): Created when spend on API requests to an S3 bucket represents greater than 80% of costs for that bucket.
* [S3 Administrative Fees](/docs/high-s3-admin-fees): High as calculated by subtracting the per bucket fees threshold (10% of the total 30 day bucket cost) from the total administrative fees for the specified S3 buckets.
