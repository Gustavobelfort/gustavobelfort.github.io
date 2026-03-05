---
title: "Migrating to Crossplane v2: Compositions, XRDs, and What Actually Changed"
date: 2025-02-28
category: "infra"
summary: "Crossplane v2 introduced breaking changes to composition schemas and XRD definitions. Hands-on migration guide with working YAML examples and before/after comparisons."
readtime: "15 MIN READ"
tags: ["crossplane", "kubernetes", "iac"]
---

Crossplane v2 dropped with a set of breaking changes that caught many teams off guard. Here's what actually changed, what you need to update, and how to migrate without downtime.

## What Changed in v2

The biggest changes are in Composition and XRD schemas. The `compositeTypeRef` field moved, patch types were renamed, and the `resources` array now requires explicit `name` fields.

## Migration Steps

1. Update your provider versions first
2. Migrate XRD schemas to the new format
3. Update Composition resources with explicit names
4. Test in a non-production cluster
5. Apply to production with Argo Rollouts for safety

## Before & After Examples

The migration is mostly mechanical — schema field moves and renames. But the devil is in the details, especially around patch transforms and connection details.

## Lessons Learned

- Always read the full changelog, not just the highlights
- Crossplane's migration tooling is still maturing — manual review is essential
- Having GitOps made rollback trivial when issues surfaced
