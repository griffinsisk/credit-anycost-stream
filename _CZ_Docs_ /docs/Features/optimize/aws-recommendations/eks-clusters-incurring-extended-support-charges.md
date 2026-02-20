---
title: EKS Clusters Incurring Extended Support Charges
category: features
createdAt: '2025-12-01T00:00:00.000Z'
hidden: false
slug: eks-clusters-incurring-extended-support-charges
updatedAt: '2025-12-01T00:00:00.000Z'
---
This recommendation identifies Amazon EKS (Elastic Kubernetes Service) clusters that are incurring extended support charges for using Kubernetes versions that have reached end-of-standard-support.

## What are EKS Extended Support Charges?

AWS charges additional fees for EKS clusters running on Kubernetes versions that have passed their standard support end date. Extended support provides:

- Security patches and bug fixes for the Kubernetes control plane
- Continued access to Amazon EKS optimized AMIs
- Technical support for the extended version

However, these charges can be significant and are avoidable by upgrading to a supported Kubernetes version.

## Cost Impact

Extended support charges typically add:
- **~$0.60/hour per cluster** (~$438/month)
- This is in addition to standard EKS cluster costs ($0.10/hour)
- Represents a **6x increase** in control plane costs

For organizations with multiple clusters, these charges can accumulate to thousands of dollars per month.

## Why This Matters

1. **Cost Optimization**: Eliminating extended support charges immediately reduces EKS costs
2. **Security**: Newer Kubernetes versions include important security improvements
3. **Features**: Access to latest Kubernetes features and improvements
4. **Performance**: Newer versions often include performance enhancements
5. **Compliance**: Running EOL software may violate security policies

## Recommended Actions

**Upgrade your EKS clusters** to a Kubernetes version that is within standard support.

### Check Current Version
```bash
aws eks describe-cluster --name <cluster-name> --query cluster.version
```

### Upgrade Process

1. **Review the upgrade path**: EKS only allows upgrading one minor version at a time (e.g., 1.21 → 1.22 → 1.23)

2. **Update control plane**:
   ```bash
   aws eks update-cluster-version --name <cluster-name> --kubernetes-version <version>
   ```

3. **Update node groups**:
   - Managed node groups: Update through AWS Console or CLI
   - Self-managed nodes: Update AMIs and roll out new nodes

4. **Update add-ons**:
   ```bash
   aws eks update-addon --cluster-name <cluster-name> --addon-name <addon> --addon-version <version>
   ```

5. **Test thoroughly** between each version upgrade

### Important Considerations

- **Application compatibility**: Test workloads with new Kubernetes API versions
- **Deprecated APIs**: Check for deprecated API usage in your manifests
- **Add-ons**: Ensure all add-ons (CNI, CoreDNS, kube-proxy) are compatible
- **Helm charts**: Verify Helm chart compatibility with target version
- **Downtime**: Plan upgrade window (control plane upgrade causes brief API disruption)

## Current Support Timeline

AWS provides 14 months of standard support for each Kubernetes version:

| Version | Release | End of Standard Support | Extended Support Until |
|---------|---------|------------------------|----------------------|
| 1.28    | Sep 2023 | Nov 2024              | Nov 2025            |
| 1.27    | May 2023 | Jul 2024              | Jul 2025            |
| 1.26    | Apr 2023 | Jun 2024              | Jun 2025            |
| 1.25    | Feb 2023 | May 2024              | May 2025            |
| 1.24    | Nov 2022 | Jan 2024              | Jan 2025            |

*Check [AWS EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html) for current support dates*

## Best Practices

1. **Stay current**: Aim to be within 2 minor versions of latest
2. **Upgrade regularly**: Don't let versions fall too far behind
3. **Test in non-prod first**: Always test upgrades in dev/staging
4. **Automate**: Use GitOps tools (ArgoCD, Flux) for consistent deployments
5. **Monitor**: Set up alerts for version EOL dates
6. **Plan ahead**: Schedule upgrades well before standard support ends

## Resources

- [EKS Kubernetes Versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)
- [EKS Cluster Upgrade Guide](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html)
- [Kubernetes Deprecation Policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/)
- [EKS Extended Support Pricing](https://aws.amazon.com/eks/pricing/)
