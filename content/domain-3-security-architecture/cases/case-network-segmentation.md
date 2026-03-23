---
title: "Case: The PCI Compliance Segmentation Sprint — 1,200 Stores, 60 Days"
description: "A retail chain with 1,200 stores discovers their entire network is flat. POS systems, back-office workstations, and guest Wi-Fi share the same subnet. PCI assessors flag it as critical. The organization has 60 days to segment all stores without impacting operations."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

RetailCorp operates 1,200 stores across the United States selling apparel and home goods. Each store has:

- 8-12 POS (point-of-sale) registers that process payment cards
- 3-4 back-office workstations for inventory, staffing, and scheduling
- 2-3 employee laptops that use Wi-Fi
- A guest Wi-Fi network for customer browsing
- A single Internet connection with a basic firewall and no internal segmentation

All devices on a store's network are on the same subnet (e.g., 192.168.1.0/24). The wireless networks (employee and guest) are separate VLANs, but they're not segmented from the wired POS network. Everything can talk to everything.

In March 2024, RetailCorp underwent a PCI DSS compliance audit. The assessor's report identified a critical finding:

> "The payment processing environment is not properly [[network-segmentation|segmented]] from non-processing systems. POS devices that handle cardholder data share network segments with non-processing devices including workstations, printers, and Wi-Fi networks. This violates PCI DSS Requirement 1.2.1, which requires that all systems which are not specifically dedicated to processing, storing or transmitting cardholder data must be segmented from those that are."

The finding came with a timeline: Remediate within 60 days or lose PCI compliance certification.

PCI DSS compliance is non-negotiable for payment processors. Losing it would mean:
- Credit card processors would block the company from accepting cards
- Payment processing would halt entirely
- All 1,200 stores would go dark

The deadline was May 31, 2024. That's 60 days.

Chief Information Security Officer Jennifer Martinez called an emergency meeting with retail operations, IT, and finance. The scope of work was massive:

- **1,200 physical locations** to reconfigure
- **12,000+ devices** to segment
- **Network changes** to deploy to every store
- **Staff training** so store managers understood what changed
- **Validation** that POS systems still worked after changes
- **Minimal disruption** since stores had to remain operational

Jennifer's team designed a [[network-segmentation|segmentation]] architecture:

**Zone 1: POS Processing Zone**
- POS registers, payment terminals, and the store's card reader device
- Dedicated network segment (VLAN) with no default-allow policies
- [[jumpbox-jump-server|Restricted access]]: only specifically authorized back-office workstations can access POS devices
- No direct internet access—all payment data flows through a secure payment gateway

**Zone 2: Back-Office Workstations**
- Inventory, scheduling, and staff management systems
- Separate VLAN from POS
- Limited internet access (only to corporate systems)
- [[east-west-traffic-control|Cannot directly access]] POS devices

**Zone 3: Employee Wi-Fi**
- Employee personal laptops and phones
- Isolated VLAN
- Unrestricted internet access
- [[east-west-traffic-control|Cannot access]] POS or back-office zones

**Zone 4: Guest Wi-Fi**
- Customer Wi-Fi for in-store browsing
- Separate VLAN
- Complete isolation from all other zones
- Bandwidth-limited

The architecture required changes to each store's network equipment:

1. **Network switch upgrade**: Basic unmanaged switches were replaced with managed switches supporting [[virtual-local-area-network|VLANs]]
2. **Firewall upgrade**: Basic NAT firewalls were replaced with stateful firewalls supporting [[access-control-lists|ACL-based]] rules between VLANs
3. **Access point separation**: Guest Wi-Fi access points were configured as separate VLANs, not just SSIDs on the same network

The challenge was coordination and validation. Jennifer couldn't send IT staff to 1,200 stores to reconfigure network equipment. Instead, she executed a phased, remote-friendly approach:

**Phase 1: Equipment Procurement and Pre-Configuration (Week 1-2)**
- Pre-configured all 1,200 switch and firewall replacements at a central warehouse
- Created a "turnkey" package that store IT could plug in with minimal configuration
- Shipped kits to all stores

**Phase 2: Store Staff Rollout (Week 3-4)**
- Provided step-by-step documentation with photos for store IT staff to follow
- Conducted video training calls with each store's IT contact
- Made available a dedicated support hotline for questions

**Phase 3: Validation (Week 5-6)**
- Remote connectivity tests to ensure each store's network was properly segmented
- POS system tests to confirm payment processing still worked
- Wi-Fi testing to validate that guest Wi-Fi was properly isolated

**Phase 4: Compliance Audit (Week 7-8)**
- The external PCI assessor conducted spot checks at 30 stores (2.5% sample)
- Verified that the [[network-segmentation|segmentation]] was in place and functioning
- Tested [[east-west-traffic-control|lateral movement]] to confirm a device in the guest Wi-Fi zone could not access the POS zone

By May 25, all 1,200 stores had been upgraded. The PCI audit was completed on May 28. The assessor's final report showed: "Network segmentation is properly implemented and validates remediation of Requirement 1.2.1. No open findings."

PCI certification was maintained.

## The Technical Details

The network configuration was surprisingly complex despite appearing simple:

**A problematic configuration (before segmentation)**:
```
All traffic default-allow (no firewall filtering)
POS Devices: 192.168.1.10, 192.168.1.11, etc.
Back-Office: 192.168.1.50, 192.168.1.51, etc.
Employee Wi-Fi: 192.168.1.100-200
Guest Wi-Fi: 192.168.1.201-250

A compromised back-office workstation could arp-scan, find POS devices,
and attempt credit card theft attacks directly.
```

**The corrected configuration (after segmentation)**:
```
POS VLAN (VLAN 10): 10.1.1.0/24 - payment devices only
Back-Office VLAN (VLAN 20): 10.1.2.0/24 - inventory systems
Employee Wi-Fi (VLAN 30): 10.1.3.0/24 - personal devices
Guest Wi-Fi (VLAN 40): 10.1.4.0/24 - customers
Management VLAN (VLAN 99): 10.1.99.0/24 - firewall admin access only

Firewall Rules:
- VLAN 10 (POS) → Internet: ALLOW (to payment gateway only)
- VLAN 10 ← Back-Office: ALLOW (for authorized POS config)
- VLAN 10 ← Employee/Guest: BLOCK (implicit deny)
- Back-Office → Internet: ALLOW (to corporate systems only)
- Employee Wi-Fi → Internet: ALLOW (unrestricted)
- Employee Wi-Fi ↔ POS/Back-Office: BLOCK
- Guest Wi-Fi ↔ Everything: BLOCK (except internet to external sites)
```

## What Went Right

- **Deadline-driven compliance enforcement worked**: Without the PCI deadline, segmentation might never have happened.
- **Turnkey, pre-configured equipment reduced deployment complexity**: Store IT staff didn't need to be network engineers; they just plugged in the new equipment.
- **Phased validation prevented widespread failures**: Testing before full rollout caught issues with a few stores, not all 1,200.
- **Spot-check auditing confirmed remediation without auditing every store**: The assessor sampled 30 stores and verified the pattern was consistent.

## What Could Go Wrong

- **Misconfigured firewall rules could have blocked legitimate POS operations**: If the firewall was too aggressive, POS devices might not have been able to reach the payment gateway, breaking checkout.
- **VLAN misconfiguration could have allowed guest Wi-Fi to access POS**: If VLAN tagging was misconfigured, the isolation would have failed silently.
- **Lack of coordination with store staff could have caused failures**: If stores didn't follow the deployment instructions correctly, the [[network-segmentation|segmentation]] wouldn't function properly.
- **PCI assessor could have rejected the segmentation design**: If the architecture didn't properly isolate cardholder data environments, the audit would have failed.

## Key Takeaways

- **[[Virtual-local-area-network|VLANs]] alone are not sufficient isolation**: You need both [[virtual-local-area-network|VLAN]] tagging AND firewall rules that enforce [[east-west-traffic-control|traffic control]] between VLANs.
- **Segmentation must be validated, not assumed**: Test that devices in one segment cannot reach devices in another segment, even though they're on the same switch.
- **[[Jumpbox-jump-server|Restricted access]] to sensitive zones is better than default-allow**: Instead of "anyone on the office network can access POS devices," implement "only back-office workstations 192.168.1.50-51 can reach POS devices on ports 22,80,443."
- **Physical location-based segmentation is viable**: 1,200 identical stores with identical network designs is much easier than designing unique segmentation for each location.
- **Pre-configuration and turnkey equipment reduces deployment risk**: If you must deploy network changes to many locations, pre-stage everything so field staff just needs to plug in new equipment, not reconfigure it.
- **Compliance deadlines are effective drivers**: PCI's 60-day remediation deadline forced RetailCorp to act. Without it, security might have remained an unfunded initiative.

## Related Cases

- [[case-firewalls]] — Firewall rules that enforce segmentation
- [[case-east-west-traffic-control]] — Monitoring and preventing lateral movement
- [[case-zero-trust]] — More sophisticated segmentation models that verify every access

