---
title: "Case: The Unpatched Water System — Critical Embedded Systems with No Patch Path"
description: "A regional water utility discovers that seven SCADA controllers run 2019 firmware with a known RCE vulnerability. The vendor won't patch for six months, the systems cannot go offline, and the network lacks segmentation. Physical safety hangs in the balance."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

Sierra Valley Water Utility serves 340,000 residents across three counties in Northern California. Their core infrastructure includes seven Siemens S7-1200 programmable logic controllers (PLCs) that manage chlorine dosing, water pressure regulation, and contamination detection across 147 miles of distribution pipeline. On a Tuesday morning in March, after a routine vulnerability scan, Security Manager Carlos Mendez discovered something that made his stomach drop: all seven controllers were running firmware version 4.2.1, released in June 2019.

The CVE database flagged this version with **CVE-2024-1847**, a remote code execution vulnerability affecting water utility SCADA systems. The description was chilling: "An unauthenticated attacker on the same network segment can execute arbitrary commands with the privileges of the SCADA system." The CVSS score was 9.8 (critical). And there were already proof-of-concept exploits published.

Carlos immediately called Marcus Webb, the Operations Director for the water system. Marcus's first response was predictable: "We can't patch. This facility treats water 24/7 with zero tolerance for downtime. One hour of lost pressure regulation and neighborhoods don't have water for showers and toilets. A mistake in the patch process and we're hauling emergency water trucks to 340,000 people."

Carlos pulled up the vendor's patch timeline. Siemens had released version 4.3.2 addressing the CVE in January 2024, but the water utility's existing service contract didn't include updates for this product line. Purchasing a new support contract and arranging for a certified Siemens technician to travel to the site, validate the firmware update, and perform the upgrade would take **six to eight months** according to the vendor's sales team.

This left them with a terrible choice: run systems with a known critical vulnerability, or take a multi-month detour to obtain a patch that might take weeks to fully deploy and validate across all seven controllers.

Carlos convened an emergency incident review with Marcus, CISO Linda Torres, and the plant's chief engineer, Dr. Anil Sharma. They spent two hours understanding the actual attack surface. The [[network-segmentation]] was basically non-existent—the SCADA controllers were on the same Ethernet segment as the administrative workstations used by plant supervisors. There was no [[air-gap|air-gapping]], no firewall between the SCADA network and the administrative network, and no network intrusion detection. The legacy design from 2012 had assumed "we're a utility, nobody's interested in attacking us."

Dr. Sharma explained the vulnerability mechanism: An attacker who could reach the network segment could send specially crafted packets to the PLC port (102/TCP), triggering a buffer overflow that allowed command execution. Once inside the PLC, they could modify the logic—for example, disable the chlorine feed-back monitoring and run overdose levels, or open relief valves to depressurize the entire system.

Linda Torres realized this was now a physical safety issue, not just an IT security issue. She involved their legal team and contacted the California Public Utilities Commission (CPUC). The CPUC's response was clear: utilities are required to manage known critical vulnerabilities. If the water utility had a compromise that resulted in contamination or safety issues due to negligence about a *known* unpatched system, the utility would be liable.

Over the next two weeks, Carlos and his team executed a multi-layered mitigation strategy since they couldn't patch immediately:

**1. [[Network-segmentation]] implementation** (Priority 1, completed in 3 days):
- Installed a Fortinet FortiGate firewall between the SCADA network and the administrative network
- Implemented access control lists (ACLs) that allowed only specific management workstations to reach the PLC
- Created a separate "jump server" (an isolated Windows box with direct SCADA access) that could only be accessed via SSH from two specific office workstations
- Disabled all other network paths to the PLC

**2. Enhanced monitoring and logging** (Priority 1, completed in 5 days):
- Deployed network intrusion detection (Snort) on the SCADA segment to detect CVE-2024-1847 exploitation attempts
- Configured packet capture for all traffic to the PLC
- Implemented application-level logging on the jump server to track every command sent to the PLC
- Set up real-time alerting for any suspicious network patterns

**3. Physical controls and procedures** (Priority 2, completed in 2 weeks):
- Implemented a manual "fail-safe" procedure: if the PLC network goes down or exhibits anomalies, the system automatically switches to manual emergency operation mode with tactile pump controls
- Trained all operators on the manual failover procedure and conducted weekly drills
- Printed and laminated emergency operation procedures at every workstation

**4. Supply chain hardening** (Priority 3, ongoing):
- Verified firmware hashes for all deployed versions using SHA-256 checksums published by Siemens to ensure no supply-chain compromise
- Implemented [[hashing]] validation for any firmware updates before deployment
- Required cryptographic signing validation for all system configuration changes

**5. Aggressive patching timeline** (Priority 1, expedited):
- Carlos worked with procurement to escalate the Siemens support contract upgrade from "6-8 months" to "90 days" by agreeing to a premium service charge
- Identified that the newer firmware could be staged and tested on a lab PLC model before deploying to production

Four months after the discovery, the first PLC was patched. By month six, all seven controllers were running version 4.3.2. During that six-month window, there were no exploitation attempts—the [[network-segmentation]], monitoring, and manual controls had maintained both security and operational resilience.

## What Went Right

- **Vulnerability scan discovered the issue before exploitation**: The organization was running regular scans, which caught the CVE before attackers could find it.
- **Layered defense despite inability to patch**: Network segmentation, monitoring, manual controls, and hash validation created defense-in-depth that protected the system even with the known vulnerability.
- **Regulatory escalation worked**: Involving the CPUC prevented politics from delaying the patch process. Regulatory pressure accelerated vendor response.
- **Physical safety design allowed fallback**: The system could be operated manually, which meant even if the PLC was completely compromised, operators could maintain water safety.
- **[[Hashing]] validation for supply chain**: Verifying firmware checksums ensured that the patch itself wasn't compromised or subject to supply-chain attack.

## What Could Go Wrong

- **No [[network-segmentation]] would have been catastrophic**: If the SCADA network had remained flat with the administrative network, a compromised admin workstation could have directly controlled water treatment.
- **No monitoring would have meant silent compromise**: If intrusion detection hadn't been implemented, attackers could have modified PLC logic without detection—poisoning the water supply invisibly.
- **Firmware without [[hashing]] verification risks supply chain**: If the patch hadn't been verified against published cryptographic hashes, a malicious patch could have been introduced.
- **No manual failover would have meant choosing between security and safety**: If the system couldn't be operated manually, the utility would have faced pressure to leave the vulnerability unpatched indefinitely.
- **Vendor patch unavailability could have left the system vulnerable forever**: Some embedded systems vendors never patch legacy hardware. This utility was lucky that a patch existed at all.

## Key Takeaways

- **Embedded systems require different patching strategies**: A three-year patch window is not acceptable for critical infrastructure. Contractual requirements for patch availability should be mandated before procurement.
- **[[Network-segmentation]] is mandatory for any SCADA/OT system**: Air-gaps and firewalls between administrative networks and operational technology networks should be non-negotiable architectural requirements.
- **Monitoring embedded systems requires network-level detection**: SCADA systems often can't support traditional endpoint agents. Network intrusion detection and packet analysis are the primary defensive mechanisms.
- **[[Resilience-and-redundancy]] includes manual failover capabilities**: Systems that cannot be patched or updated need to maintain safe manual operation modes. This is both a security and safety issue.
- **[[Hashing]] validation is critical for embedded system firmware**: Before deploying any firmware update, verify the cryptographic hash against the vendor's published values to ensure supply-chain integrity.
- **Budget for premium support on critical embedded systems**: The cost of expedited patching ($180K in this case) is trivial compared to the cost of a water contamination event (potential $1B+ liability) or system compromise.

## Related Cases

- [[case-network-segmentation]] — The foundational [[network-segmentation|segmentation]] strategy that protected this SCADA system
- [[case-hardening]] — System hardening principles applied to embedded systems and legacy hardware
- [[case-vulnerability-management]] — The broader context of managing vulnerabilities across heterogeneous IT/OT environments

