---
title: Upgrade Elasticsearch to Avoid Extended Support Charges
category: features
createdAt: '2025-12-03T00:00:00.000Z'
hidden: false
slug: elasticsearch-extended-support-charges
updatedAt: '2025-12-03T00:00:00.000Z'
---

## Overview
AWS charges additional Extended Support fees for Elasticsearch domains running end-of-life (EOL) versions. These charges can add 50-100% to your regular Elasticsearch costs and increase over time.

## Why This Matters
- **High cost**: Extended support can double your Elasticsearch bill
- **Escalating fees**: Charges increase the longer you stay on old versions
- **Security risk**: EOL versions no longer receive security patches
- **Performance**: Newer versions offer better performance and features

## Common EOL Versions with Extended Support
- Elasticsearch 6.x (all versions)
- Elasticsearch 7.0 - 7.9 (early 7.x versions)

## Recommendation
Upgrade to the latest supported Elasticsearch version (7.10 or later, or migrate to OpenSearch).

## Implementation Steps

### Option 1: In-Place Upgrade (Recommended)
1. **Review compatibility**: Check application compatibility with target version
2. **Backup domain**: Create manual snapshot before upgrade
3. **Upgrade domain**: Use AWS Console or CLI to perform rolling upgrade
4. **Test thoroughly**: Validate all queries and integrations work
5. **Monitor performance**: Watch cluster health and query latency

### Option 2: Blue/Green Deployment
1. Create new domain with target version
2. Reindex data from old domain
3. Update application endpoints
4. Monitor and validate
5. Delete old domain

### Option 3: Migrate to OpenSearch
Consider migrating to OpenSearch (AWS's open-source fork) for long-term support and latest features.

## Cost Impact
Eliminates 100% of extended support charges immediately upon upgrade. For a typical domain, this can save $500-$5,000/month depending on cluster size.

## Additional Benefits
- Latest security patches
- Improved performance and efficiency
- Access to new features
- Better AWS support
- Lower operational risk
