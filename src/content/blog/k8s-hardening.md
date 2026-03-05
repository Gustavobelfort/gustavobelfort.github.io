---
title: "Kubernetes Hardening Checklist for Validator Node Operators"
date: 2025-03-10
category: "security"
summary: "Running blockchain validators on Kubernetes? Here's the security baseline I apply to every cluster: RBAC, network policies, Kyverno, secret management, and runtime threat detection."
readtime: "11 MIN READ"
tags: ["kubernetes", "security", "kyverno"]
---

Running blockchain validators on Kubernetes requires a security posture that goes beyond standard web application hardening. Validators hold keys, sign transactions, and are high-value targets.

## RBAC Lockdown

Every namespace gets its own service account with minimal permissions. No cluster-admin roles for workloads — ever.

## Network Policies

Default-deny ingress and egress on every namespace. Whitelist only the specific ports and peers each validator needs.

## Kyverno Admission Control

Policy-as-code for image verification, resource limits, label requirements, and preventing privilege escalation.

## Secret Management

HashiCorp Vault with External Secrets Operator (ESO). Validator keys never touch etcd in plain text.

## Runtime Threat Detection

Falco for anomaly detection, with custom rules for validator-specific patterns (unexpected network connections, file system changes, process spawning).

## The Checklist

- RBAC: Least-privilege service accounts
- Network: Default-deny + explicit whitelists
- Admission: Kyverno policies for image signing and resource constraints
- Secrets: Vault + ESO, no plain-text keys in etcd
- Runtime: Falco with custom validator rules
- Monitoring: Alert on any RBAC violations or policy failures
