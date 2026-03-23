---
title: "Case: The Smart Factory Network — IT/OT Convergence Security Design"
description: "Designing a new smart factory network with 500 IoT sensors, real-time production control systems, and the requirement that corporate network compromise should never affect manufacturing. IT and OT teams have conflicting security requirements."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

ManuTech Industries is building a new state-of-the-art manufacturing facility in Mexico that will produce precision components for automotive suppliers. The facility integrates operational technology (OT)—robotic arms, CNC machines, pressure sensors, temperature monitors, and programmable logic controllers—with information technology (IT)—ERP systems, quality control databases, and logistics software. The two worlds need to communicate, but they have completely different security and reliability requirements.

Chief Information Security Officer Dr. James Whitmore was asked to design the network architecture. The requirements were:

1. **Production must never stop**: Even if the corporate network is completely compromised (ransomware, breach, insider threat), the manufacturing floor must continue operating safely. The [[network-zones|OT zone]] must be completely isolated from the [[network-zones|IT zone]].

2. **Real-time requirements**: Manufacturing sensors report state every 100ms. Network latency, dropped packets, or configuration errors can cause product defects or equipment damage. The OT network must be deterministic and extremely reliable.

3. **Data must flow from factory to business systems**: Quality metrics, production rates, downtime events, and inventory levels must flow from OT sensors to the IT systems for analytics, billing, and reporting. This means the [[network-zones|firewall]] must allow some outbound communication.

4. **Security is mandatory but transparent**: Factory workers don't want to see security getting in the way. They want to press a button and have the robot do what they programmed.

5. **Scale to 500+ sensors**: The sensor network will grow over time. The architecture must scale without requiring constant reconfiguration.

Dr. Whitmore designed a four-tier network architecture with [[defense-in-depth]] and [[network-segmentation|segmentation]] at each layer:

**Tier 1: The Manufacturing Floor (OT – Operational Technology)**
- 500 IoT sensors (pressure, temperature, vibration, position)
- 120 programmable logic controllers (PLCs) managing equipment
- 15 industrial robots with embedded controllers
- All devices communicate via hardened industrial protocols (Modbus, Profinet, OPC-UA) over dedicated wired networks (no Wi-Fi—too unpredictable for real-time control)
- This tier is a **closed system**: devices only communicate with each other and with the data-collection gateway. No external access. No internet. No connection to IT systems except through an [[air-gap|air-gapped]] gateway.

**Tier 2: The Manufacturing Gateway (Demilitarized Zone)**
- A single industrial data collection server (hardened Linux appliance) receives sensor data from the OT network via a one-way firewall rule
- The gateway runs only one application: a sensor data aggregator that collects metrics and logs them to a time-series database
- All network traffic to/from the gateway is inspected. Outbound traffic only goes to specific IT systems for data delivery. Inbound traffic is completely blocked—no remote access, no SSH, nothing.
- The gateway is not directly connected to the IT network; it communicates through an [[air-gap]]-style firewall where packets must pass inspection before being forwarded

**Tier 3: The Corporate IT Network**
- ERP systems (SAP, Oracle)
- Data warehouses for analytics
- Business systems (accounting, HR, supply chain)
- Development environments
- All standard IT security controls: firewalls, intrusion detection, endpoint protection, standard corporate policies

**Tier 4: External Access**
- Remote management (VPN for plant managers)
- Cloud connectivity (data feeds to corporate headquarters)
- Internet gateway
- Public-facing APIs if needed (e.g., for supplier portals)

The firewall rules enforce strict [[east-west-vs-north-south-traffic|traffic control]]:

**North-South Traffic** (data entering/leaving the facility):
- ✅ OT→Gateway (sensor data outbound): Allowed on specific ports only
- ✅ Gateway→IT (data ingestion): Allowed only to specific IT systems
- ✅ IT→External (business traffic): Standard controls
- ❌ OT→IT: Blocked completely
- ❌ External→OT: Blocked completely
- ❌ IT→OT: Blocked completely

**East-West Traffic** (lateral movement within tiers):
- Within OT: All communication allowed (sensors need to talk to each other and PLCs)
- Within IT: Segmented by function (ERP in one zone, development in another, analytics in another)
- Across tiers: Strictly filtered

The gateway implements a **protocol firewall** that understands OT protocols:

```
Industrial Protocol Firewall Rules:
- Allow Modbus READ_HOLDING_REGISTERS from sensors to PLCs
- Allow Profinet heartbeat messages (100ms interval, no larger than 256 bytes)
- Allow OPC-UA connections from gateway to sensors (authenticated, encrypted)
- Drop everything else
```

This is different from a traditional firewall that understands HTTP/TCP/UDP. The protocol firewall understands that Modbus packets larger than 256 bytes are abnormal and might indicate an attack or misconfiguration.

**Physical Segmentation**:
- The OT network runs on dedicated, isolated switches that are not connected to any other network
- The gateway has dual network interfaces: one connected to the OT switches, one connected to the IT firewall (which is just a regular firewall appliance)
- The gateway is the **only** bridge between OT and IT

**Backup and Failover**:
- OT systems have redundant controllers and can operate independently if the gateway fails
- If the gateway stops receiving sensor data, the PLCs continue operating using their last-known state
- Production stops gracefully (equipment enters safe state) if sensors can't communicate with controllers, rather than operating on stale data

**Monitoring and Analytics**:
- The gateway logs all sensor data in a time-series database
- IT systems have read-only access to the time-series data
- Analytics, reports, and dashboards are built from this read-only copy, never from the live OT network

**Incident Response**:
- If a ransomware outbreak is detected in the IT network, the firewall between IT and Gateway is automatically hardened to allow only heartbeat traffic from OT sensors
- The OT network can continue operating indefinitely on just heartbeat data
- IT systems can be shut down, wiped, and recovered without affecting manufacturing
- If an attack is detected in the OT network (e.g., malware on a PLC), that device is physically disconnected from the industrial network, and the line reverts to manual control while IT investigates

### Implementation and Testing

The architecture was implemented in Q3 2024. Before go-live, the team conducted three months of testing:

**Scenario 1: IT Network Ransomware Outbreak**
- Simulated a ransomware attack in the IT network
- Verified that OT network continued operating without degradation
- Confirmed that manufacturing output was unaffected
- Validated that the gateway could continue sending sensor data to an external IT system (corporate headquarters) via a temporary secure tunnel

**Scenario 2: Gateway Failure**
- Took the gateway offline while manufacturing was running
- Verified that OT systems detected the failure and entered safe state gracefully
- Restored the gateway
- Confirmed that OT systems resumed normal operation

**Scenario 3: Malicious Sensor Traffic**
- Injected abnormal Modbus commands into the OT network
- Verified that the protocol firewall detected them and dropped them
- Confirmed that legitimate sensor data continued flowing

All tests passed. The facility went live in October 2024.

## What Went Right

- **Complete isolation of OT from IT security threats**: A corporate data breach does not affect manufacturing operations.
- **Defense-in-depth with multiple control layers**: The [[air-gap|air-gapping]], protocol firewall, and network segmentation provide redundant protection.
- **Deterministic OT operation**: Real-time manufacturing control is not affected by network latency or firewall overhead because the OT network is completely isolated.
- **Data still flows for analytics**: Despite isolation, manufacturing data flows to IT systems for reporting and optimization.
- **Physical segmentation prevents misunderstanding**: Having a gateway device and physically separate switches makes the architecture clear and prevents misconfiguration.

## What Could Go Wrong

- **If IT and OT were on the same network**: A single malware outbreak could compromise both, stopping production entirely.
- **If bidirectional communication were allowed between IT and OT**: Attackers who compromised IT could reach down and compromise PLCs, causing safety issues or production sabotage.
- **If the gateway didn't implement protocol-level filtering**: Sophisticated attacks could use legitimate-looking OT traffic to exfiltrate data or inject commands.
- **If there was no failover mode**: If the gateway failed without graceful OT shutdown, equipment could operate on stale sensor data, causing accidents or product damage.
- **If monitoring and alerting weren't in place**: Attacks on the OT network (slow exfiltration, subtle sensor manipulation) could go undetected.

## Key Takeaways

- **Defense-in-depth is mandatory for critical infrastructure**: Manufacturing networks need multiple layers of protection—physical segmentation, firewalls, protocol filtering, monitoring.
- **OT and IT networks should be completely separated**: Different security models, different threats, different requirements. Convergence is minimal and one-directional (OT→IT only).
- **Protocol-level filtering is more effective than IP-level filtering**: Understanding OT protocols (Modbus, Profinet) allows detection of semantic attacks, not just syntactic malformed packets.
- **Failsafe design is critical for physical systems**: When communication fails, manufacturing equipment should enter a safe state, not continue operating on stale data.
- **Lateral movement must be blocked**: Restrict traffic within zones and between zones. This prevents an attacker from using a compromised sensor to attack a PLC.
- **Air-gapping is still relevant in modern networks**: Complete isolation of critical OT networks from IT systems, with a gateway that strictly controls information flow, is a proven architecture.

## Related Cases

- [[case-firewalls]] — Implementing firewalls that understand industrial protocols
- [[case-network-segmentation]] — Logical and physical segmentation strategies
- [[case-hardening]] — Securing the gateway appliance and OT devices themselves

