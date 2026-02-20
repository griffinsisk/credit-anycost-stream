---
title: Configure S3 Lifecycle Policy to Abort Incomplete Multipart Uploads
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_S3_Incomplete_Multipart_Upload_Abort_Configuration
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies Amazon S3 buckets that do not have lifecycle policies configured to automatically abort incomplete multipart uploads, which can lead to unnecessary storage costs.

# Overview

AWS Trusted Advisor monitors your S3 buckets and identifies those without lifecycle policies configured to abort incomplete multipart uploads. Incomplete multipart uploads continue to incur storage costs until they are explicitly aborted or automatically cleaned up by lifecycle policies.

# What it identifies

* S3 buckets without lifecycle policies for incomplete multipart upload cleanup
* Opportunities to implement lifecycle policies for multipart upload management
* Buckets that may be accumulating costs from incomplete uploads
* Recommendations for appropriate lifecycle policy configurations
* Cost optimization opportunities from AWS Trusted Advisor

# Key features

* Uses AWS Trusted Advisor's `c1cj39rr6v` check for incomplete multipart upload abort configuration
* Leverages Trusted Advisor's cost estimates and recommendations
* Provides dynamic titles with specific actions
* Covers all S3 buckets across all regions
* Bucket-level recommendations for targeted optimization

# Cost impact

Buckets without incomplete multipart upload abort policies can result in:

* Accumulation of incomplete multipart upload parts over time
* Continued storage costs for failed or abandoned uploads
* Wasted storage space from incomplete upload fragments
* Missed opportunities for cost optimization through automated cleanup

# Multipart upload lifecycle policy benefits

* **Automated cleanup**: Abort incomplete multipart uploads automatically
* **Cost control**: Eliminate storage costs from failed uploads
* **Storage optimization**: Free up storage space from abandoned uploads
* **Predictable costs**: Better control over multipart upload-related storage costs
* **Simplified management**: No manual intervention required for cleanup

# Common multipart upload lifecycle configurations

* **Immediate cleanup**: Abort incomplete multipart uploads after 1 day
* **Standard cleanup**: Abort incomplete multipart uploads after 7 days
* **Extended cleanup**: Abort incomplete multipart uploads after 30 days
* **Comprehensive policy**: Combine with other lifecycle rules for complete bucket management

# Multipart upload considerations

* **Upload timeouts**: Incomplete uploads can occur due to network issues or application failures
* **Storage costs**: Each part of an incomplete multipart upload incurs storage charges
* **Cleanup timing**: Balance between allowing retry attempts and cost control
* **Application integration**: Ensure applications handle multipart upload failures gracefully

# Recommended actions

* Review buckets without incomplete multipart upload abort policies
* Implement lifecycle policies specifically for multipart upload cleanup
* Consider application retry patterns when setting abort timing
* Monitor incomplete multipart upload accumulation
* Use lifecycle policies to automate multipart upload cleanup
* Regularly review and adjust abort policies based on usage patterns
