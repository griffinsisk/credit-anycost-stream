---
title: Excessive EC2/ELB Internet Traffic Bypassing CloudFront
category: features
createdAt: '2025-12-01T00:00:00.000Z'
hidden: false
slug: excessive-ec2-elb-internet-traffic-bypassing-cloudfront
updatedAt: '2025-12-01T00:00:00.000Z'
---
This recommendation identifies AWS accounts using CloudFront CDN but with significant direct internet egress from EC2/ELB. When traffic bypasses CloudFront, you pay 2-5x higher data transfer costs and miss caching, DDoS protection, and global performance benefits.

## What it identifies

- Accounts with active CloudFront distributions
- EC2/ELB direct egress >10% of CloudFront egress costs
- Minimum $1,000/month direct egress
- New services bypassing existing CDN architecture

## Cost Impact

**Savings calculation:** 50% reduction in direct egress costs through CloudFront routing, caching, and Origin Shield.

**Example:** $75k/month in direct egress = **$37,500/month savings** ($450k annually)

**Why 50% savings:**
- CloudFront caching reduces origin bandwidth 50-90%
- Origin Shield adds additional cache layer
- Reduced compute costs from fewer origin requests
- Better compression and optimization

## Why This Matters

**1. Higher data transfer costs**
- Direct is 2-5x more expensive

**2. No caching benefits**
- Every request hits origin servers
- Increased compute and database load
- Higher latency for global users

**3. Missing security & performance**
- No AWS Shield DDoS protection
- Single-region latency vs edge caching
- Increased attack surface

## Common Causes

- **New services deployed without CDN** - Microservices/APIs bypass existing CloudFront
- **"Dynamic content" misconception** - CloudFront caches API responses; even 1-second cache helps
- **Legacy architecture** - Pre-CDN infrastructure still serving traffic
- **Direct API access** - Mobile apps/integrations pointing to ALB/EC2 directly

## How to Remediate

### Step 1: Identify Sources
Use AWS Cost Explorer to find high-egress resources:
```
Service: EC2/ELB
Usage Type: DataTransfer-Out-Bytes
Group by: Resource
```

### Step 2: Add Origins to CloudFront
**Console:** CloudFront → Distributions → Origins → Create origin
- Origin domain: Your ALB DNS or EC2 endpoint
- Protocol: HTTPS only
- Enable Origin Shield for additional caching

**Terraform example:**
```hcl
origin {
  domain_name = aws_lb.app.dns_name
  origin_id   = "ALB"

  custom_origin_config {
    origin_protocol_policy = "https-only"
    origin_ssl_protocols   = ["TLSv1.2"]
  }

  origin_shield {
    enabled              = true
    origin_shield_region = "us-east-1"
  }
}

default_cache_behavior {
  target_origin_id       = "ALB"
  min_ttl     = 0
  default_ttl = 60    # Even 1 minute helps
  max_ttl     = 3600
}
```

### Step 3: Update DNS & Application Configs
Point your domain to CloudFront instead of direct ALB/EC2 endpoints.

### Step 4: Configure Caching
For dynamic content, cache based on query strings with short TTLs (30-60 seconds).

### Step 5: Monitor Results
- Check CloudFront `CacheHitRate` metric
- Verify 50-90% reduction in origin requests
- Monitor cost savings in Cost Explorer

## When Direct Egress is Acceptable

- Database replication, backups to third-party services
- VPN connections, B2B integrations with strict IP requirements
- Streaming protocols not supported by CloudFront
