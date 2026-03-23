---
title: "Case: The Printer Pivot — Why Defense in Depth Matters"
description: "A red team's penetration test at a global insurance company shows an attacker pivoting from a compromised printer to the claims database in under four minutes because the network is flat and unsegmented. The CISO realizes they have zero defense in depth."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

Global Assurance Financial serves approximately 200,000 insurance customers across auto, home, and commercial lines. The company's headquarters campus in Atlanta houses 450 employees. In February 2026, the Chief Information Security Officer, Robert Chen, commissioned a red team exercise from a boutique penetration testing firm. The engagement was scoped to test network segmentation and incident response: "Assume you've compromised a device on our network. Can you reach the claims database?"

The red team lead, Sarah Martinez, began with reconnaissance. She walked around the campus and identified network infrastructure. In the main office building, she found an open network cabinet in a break room—a security failure in physical controls, but not the focus of this exercise. The team's actual attack vector was simpler: compromise an internet-facing application and pivot internally.

The red team compromised a customer-facing web form that allowed customers to request claim status. The vulnerability was a SQL injection flaw that allowed code execution on the web server. Within 4 minutes of gaining code execution, Sarah's team had:

1. **Minute 1**: Executed commands on the web server to enumerate the local network
2. **Minute 2**: Identified a printer on the same network segment (10.1.20.0/24) with a default password
3. **Minute 3**: Compromised the printer via its web interface
4. **Minute 4**: Used the printer's network access to scan the internal network and identify the claims database server (10.1.100.50)

Sarah then requested a database connection from the claims database using default credentials (a common oversight on internal systems that "nobody should be able to reach anyway"). The database responded with access granted. Sarah downloaded a complete export of the claims database containing 15 months of claim data, customer personal information, and financial records.

The entire exercise took 12 minutes from code execution to data exfiltration. Robert Chen received the red team report on Friday morning, and his reaction was shocked silence. His team had invested millions in firewalls, intrusion detection systems, and threat monitoring. And yet, a competent attacker could walk through his network like it didn't exist.

The root cause: there was no [[network-segmentation]]. All devices were on the same 10.0.0.0/8 supernet with routing allowed between segments. A compromise on the public-facing web server was only one hop away from the claims database. The printer, a device that definitely didn't need internet access, was on the same segment as the database servers.

Robert assembled his architecture team and gave them a mandate: redesign the network with complete [[defense-in-depth]].

**Layer 1: Perimeter Defense**
The existing firewall was good but only protected the edge. The team added:
- Web Application Firewall (WAF) to stop SQL injection and similar web attacks at the application layer
- API gateway with rate limiting and authentication to prevent automated attacks
- DDoS mitigation service to absorb large volumetric attacks

**Layer 2: Network Segmentation**
The team completely re-architected the network:
- Trust zone: Internet-facing servers (web, API, email) in DMZ with strict egress filtering
- Workstation zone: Employee machines on a separate segment with endpoint protection and network access control (NAC)
- Database zone: Claims, financial, and sensitive databases on completely isolated network segments
- IoT zone: Printers, cameras, HVAC systems on a separate guest-like network with no access to other systems
- Management zone: Administrative consoles on a separate network requiring MFA to access

Between each zone, a stateful firewall enforced rules. The database zone had incoming rules only for specific database clients and blocked all egress except for backup replication to isolated backup systems.

**Layer 3: Identity and Access**
The team implemented:
- Multi-factor authentication (MFA) for all remote access (VPN, RDP, SSH)
- Role-based access control (RBAC) so that compromised database admin credentials couldn't be used to access web servers
- PAM (Privileged Access Management) so that database admin credentials were never stored; instead, temporary credentials were issued from a hardware security module
- Logging of all privileged account usage

**Layer 4: Endpoint Detection and Response**
The team deployed EDR to all workstations and servers:
- Behavior-based detection would have caught the printer's network scanning activity
- Process execution monitoring would have caught the command execution on the web server
- File modifications would have alerted on the malware execution

**Layer 5: Data Protection**
The team implemented:
- Encryption at rest for all databases using keys stored in AWS KMS (separate from the systems that access them)
- Encryption in transit using TLS 1.3 for all network communication
- Data loss prevention (DLP) tools that would block attempts to exfiltrate databases through unusual channels

**Layer 6: Monitoring and Alerting**
The team built a comprehensive monitoring stack:
- Network flow analysis to detect unusual traffic patterns (why is the printer connecting to the database server?)
- SIEM rules to correlate authentication events, network flows, and endpoint telemetry
- Behavioral analytics to detect anomalies

By April 2026, the network redesign was 80% complete. The red team was invited back to test. This time, Sarah compromised the web server the same way. But this time:

- **She couldn't scan the internal network** because the DMZ firewall blocked outbound traffic except to specific approved systems
- **She couldn't compromise the printer** because it was on a separate network segment with no access to internal systems
- **She couldn't reach the database server** because the database was on an isolated segment with firewall rules allowing access only from approved application servers
- **When she tried to access the database from the web server using compromised database credentials**, the PAM system logged the request as "credential used from unexpected location—web server instead of admin workstation" and blocked the access

The red team concluded their report: "The network is now defensible. A single compromise is no longer catastrophic."

## What Went Right

- **Red team assessment provided clear evidence of the vulnerability**: Walking through the network in 12 minutes was more convincing than any report about flat networks. Robert immediately understood the severity.
- **Complete redesign addressed multiple layers simultaneously**: The team didn't just add one firewall and call it done. They addressed application security (WAF), network segmentation, identity controls, endpoint monitoring, and data protection together.
- **Physical security improvements prevented easy access**: Securing network cabinets and requiring badge access to server rooms prevented the kind of shoulder-surfing and direct cable access that make social engineering attacks easier.
- **Infrastructure as Code approach made the network maintainable**: All firewall rules, network segments, and security policies were documented in version control, making it easy to audit and update them.
- **The redesign was validated by rerunning the red team exercise**: The second red team exercise proved that the controls actually worked, not just theoretically.

## What Could Go Wrong

- **Flat network with no segmentation**: A single compromise on any device gives attackers access to everything. This is a critical vulnerability that violates [[defense-in-depth]] principles.
- **Default credentials on internal systems**: The database accepted default credentials because "nobody should be able to reach it." But "nobody" is an unreliable assumption.
- **Devices with no business need for network access on the same segment as sensitive systems**: The printer didn't need to be on the same segment as the database. Isolating it would have stopped lateral movement.
- **No [[network-segmentation]] enforcement**: Even if multiple network segments were drawn in diagrams, if routers allowed traffic between all segments, the segmentation was meaningless.
- **No endpoint detection on servers**: If the web server had EDR installed, the suspicious activity (network scanning, printer exploitation, database connection attempts) would have been detected and blocked.
- **No logging of database access**: Exfiltrating an entire database should have generated alerts. If the database server had no audit logging, nobody would have known the data was taken.
- **No egress filtering**: The web server could reach any internal system. With egress filtering, the web server could only reach approved databases and services.

## Key Takeaways

- **[[Defense-in-depth]] means multiple layers that each stop different attack vectors**: A single compromised system should not grant access to everything. Each layer should require different credentials, bypass different controls, or traverse different network segments.
- **Assume every layer will fail**: A firewall will fail (rule misconfiguration), MFA will fail (token compromised), EDR will fail (attacker knows how to evade it). Design systems that survive individual failures.
- **[[Network-segmentation]] is essential**: Isolate systems that don't need to communicate with each other. Printers don't need to reach databases. Web servers don't need to reach admin systems.
- **Default credentials on "internal only" systems are critical vulnerabilities**: If an attacker can reach the system, they will try defaults. Every system needs strong authentication, regardless of whether it's "internal."
- **Monitoring must detect abnormal behavior, not just policy violations**: A printer connecting to a database server is abnormal and should trigger alerts, even if firewall rules would prevent it.
- **[[Control-diversity]] is as important as control depth**: Relying only on firewalls is fragile. Combine firewalls, segmentation, identity controls, endpoint monitoring, and data protection. An attacker might bypass one layer but needs to bypass multiple independent layers.
- **Administrative control zones need special protection**: Compromise of an administrator's workstation or database admin credentials can bypass many controls. PAM, MFA, and logging are essential for protecting administrative access.

## Related Cases

- [[case-firewalls]] — Understanding firewall rules and egress filtering
- [[case-network-segmentation]] — Deep dive into designing and implementing network trust boundaries
- [[case-zero-trust]] — Taking defense-in-depth to the next level by verifying at every access
- [[case-physical-security]] — Securing network infrastructure and preventing direct cable access
