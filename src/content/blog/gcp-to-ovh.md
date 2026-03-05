---
title: "How I Cut $7,500/mo in GCP Egress by Migrating 25 Validator Nodes to OVH"
date: 2025-01-14
category: "devops"
summary: "A detailed post-mortem on migrating a 25-node Chainflip validator fleet from GCP to OVH Managed Kubernetes. The full story: cost analysis, migration plan, DDoS surprises, and lessons learned."
readtime: "12 MIN READ"
tags: ["kubernetes", "gcp", "ovh", "cost-optimisation"]
---

Running blockchain validators at scale generates enormous P2P gossip traffic. For Chainflip, each of my 25 nodes was generating several terabytes per month — and on GCP, this was costing roughly `$7,500/month` almost entirely from egress fees.

## The Problem: $7,500/mo in Egress

GCP charges $0.08–$0.12/GB for egress. At ~90TB/month across 25 nodes, the math was brutal. The infrastructure itself was a fraction of that cost.

> **KEY INSIGHT**: Blockchain P2P traffic crosses regions constantly to reach other validators — making it nearly impossible to avoid egress charges on a hyperscaler.

## Architecture Before & After

The migration involved moving from GCP GKE clusters to OVH Managed Kubernetes, preserving the same ArgoCD-driven GitOps deployment pipeline.

## Migration Plan & Execution

- Phase 1: Stand up parallel OVH clusters using Crossplane compositions
- Phase 2: Deploy non-critical validators to OVH, validate performance
- Phase 3: Rolling migration of production validators with zero downtime
- Phase 4: Decommission GCP resources

## Surprise #1: OVH Anti-DDoS

OVH's VAC anti-DDoS system started nullrouting our IPs — our P2P gossip pattern looks identical to a UDP flood attack. Fix: whitelisted our IP ranges from VAC. Took 5 days of back-and-forth.

## Surprise #2: Ingress IP Mismatch

OVH's Managed Kubernetes LoadBalancer assigns a different external IP than the node IP used for P2P. Validators were invisible to the network. Solution: ConfigMap-driven external IP announcement.

## Results & Lessons Learned

Month-over-month: $7,500/mo → $890/mo. ROI is undeniable.

- Always account for anti-DDoS when migrating P2P workloads
- OVH VAC support is slow — budget time for it
- Crossplane compositions made the migration dramatically faster
