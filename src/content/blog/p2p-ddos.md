---
title: "OVH Anti-DDoS False Positives on Validator P2P Traffic: Diagnosis & Fix"
date: 2025-02-03
category: "blockchain"
summary: "When OVH's VAC anti-DDoS started flagging legitimate Chainflip P2P gossip as attacks. Walk-through of the investigation, packet captures, and the mitigation that saved validator uptime."
readtime: "9 MIN READ"
tags: ["ovh", "ddos", "p2p", "networking"]
---

After migrating our 25-node Chainflip validator fleet to OVH, we hit an unexpected wall: OVH's VAC anti-DDoS infrastructure started treating our legitimate P2P traffic as attack traffic.

## The Symptoms

Validators would intermittently lose connectivity. Peers reported our nodes as unreachable. Monitoring showed packet loss spikes correlating with OVH's automated DDoS mitigation kicks.

## Investigation

Packet captures revealed that Chainflip's gossip protocol generates high volumes of small UDP packets — a pattern that closely resembles a UDP flood attack from the perspective of automated detection systems.

## The Fix

After extensive back-and-forth with OVH support (5 days), we got our IP ranges added to a VAC whitelist, exempting them from automatic mitigation. We also adjusted our P2P configuration to use slightly larger packet sizes where possible.

## Takeaways

- Always test P2P workloads against your provider's DDoS mitigation before going live
- Document your traffic patterns so you can explain them to support teams
- Budget time for provider support response — especially for niche use cases
