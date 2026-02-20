---
title: Release Idle Elastic IP Addresses
category: features
createdAt: '2025-12-01T00:00:00.000Z'
hidden: false
slug: release-idle-elastic-ip-addresses
updatedAt: '2025-12-01T00:00:00.000Z'
---
Elastic IP addresses (EIPs) that are allocated but not associated with running resources incur hourly charges. This recommendation identifies idle EIPs that can be released to reduce costs.

## What Are Elastic IPs?

Static IPv4 addresses for AWS resources that allow you to:
- Maintain consistent public IPs across instance replacements
- Quickly remap IPs to different instances
- Mask availability zone failures

## Common Causes

1. **Terminated Instances**: EIP not released when EC2 instance deleted
2. **Testing/Development**: Allocated for testing and forgotten
3. **Infrastructure Changes**: Old IPs from decommissioned services
4. **Deleted Resources**: EIPs from removed NAT Gateways or Load Balancers

## Detection Method

Uses **AmazonVPC billing data** for idle addresses:
- Service: `AmazonVPC`
- Usage Type: `PublicIPv4:IdleAddress`
- Criteria: Idle 7+ days

## Cost Impact

| Idle EIPs | Monthly | Annual |
|-----------|---------|--------|
| 5 | $18 | $216 |
| 10 | $36 | $432 |
| 50 | $180 | $2,160 |
| 100 | $360 | $4,320 |

## Recommended Actions

### 1. Verify EIP Status

```bash
aws ec2 describe-addresses --allocation-ids eipalloc-xxxxxxxxx
```

Check output:
- `InstanceId: null` → Safe to release
- `InstanceId: i-xxxxx` → Still in use, don't release
- `NetworkInterfaceId: eni-xxxxx` → Check if ENI is attached

### 2. Check Dependencies

Before releasing, verify the EIP is NOT referenced in:
- DNS A records
- Firewall allowlist rules
- Application configurations
- Documentation

### 3. Release the EIP

**AWS Console:**
1. EC2 → Elastic IPs
2. Select unassociated EIP
3. Actions → Release Elastic IP addresses

**AWS CLI:**
```bash
aws ec2 release-address --allocation-id eipalloc-xxxxxxxxx
```

### 4. Update References

After release:
- Update DNS records (if applicable)
- Remove from firewall rules
- Update documentation

## Important Considerations

**Do NOT release if:**
- Referenced in DNS (update DNS first)
- In firewall allowlists (update rules first)
- Reserved for disaster recovery
- Actively used (verify association status)

**Recovery:** You cannot recover the same IP once released. You must allocate a new one and update all references.

## Best Practices

1. **Tag all EIPs:**
   ```bash
   aws ec2 create-tags --resources eipalloc-xxx --tags \
     Key=Name,Value="Production API" \
     Key=Owner,Value=team-name
   ```

2. **Regular audits**: Review idle EIPs monthly in all regions

3. **Automation**: Set up Lambda to alert on idle EIPs detected

4. **Use alternatives when possible:**
   - Auto-assigned public IPs (free)
   - Application Load Balancer (AWS-managed IPs)
   - CloudFront (global edge network)

## Cost Optimization

- **Multiple EIPs per instance**: First is free when associated, additional cost $3.60/month each
- **NAT Gateway vs Instance**: NAT Gateway has no EIP charges (included)
- **Load Balancers**: ALB/NLB don't require EIPs, often cheaper at scale
