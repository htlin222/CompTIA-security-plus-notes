---
title: "Case: The Persistent Exfiltration — NetFlow Analysis Discovers Hidden Data Drain"
description: "NetFlow analysis reveals a steady 50 Mbps data stream leaving the network every night between 2-4 AM, destined for an IP in a country with no business relationship. The traffic originates from a build server in the CI environment."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

CloudScale Technologies operates a SaaS platform for financial services companies. In late November, their security team implemented a new [[netflow-sflow-ipfix]] monitoring system to establish [[baseline-establishment]] of normal network traffic patterns across their environment. The system was configured to collect flow records from all edge routers and switches, providing visibility into what data was leaving the network.

After one week of baseline collection, the monitoring system began generating reports. One report caught the attention of the SOC analyst reviewing it: every single night between 2:04 AM and 3:47 AM, a consistent 50 Mbps data stream was leaving the network through the internet edge router, destined for an IP address (185.220.101.14) registered in Romania—a country with which CloudScale had no business relationship.

The [[netflow-sflow-ipfix]] records showed:
- Source IP: 10.88.14.22 (build server in the CI/CD environment)
- Destination IP: 185.220.101.14 (Romania)
- Destination Port: 443 (HTTPS traffic, encrypted)
- Total bytes per night: approximately 18 GB
- Duration: consistently between 2:04 AM and 3:47 AM
- Traffic had been occurring for at least 9 days (the entire monitoring window)

This meant that 9 days × 18 GB = 162 GB of data had been exfiltrated over the previous nine days. The [[bandwidth-monitoring]] showed that the traffic was significant—50 Mbps represented about 5% of the outbound internet capacity during off-peak hours, but it was consistent and automated.

The incident response team immediately launched an investigation. They identified the build server (hostname: builder-07-prod) as a critical system that was running automated builds for the company's main SaaS platform. They suspected the server had been compromised—but how? The build server was supposedly hardened, had no direct internet access, and was behind a NAT gateway. All internet traffic should have been logged and monitored.

The security team reviewed the build server's logs and firewall rules:
1. The server had direct internet access through an outbound firewall rule that had been created six months ago to allow "updates" from external package repositories.
2. The firewall rule was overly permissive: it allowed ANY outbound traffic on port 443 to ANY destination, not just to specific package repository servers.
3. The server had been compromised through a dependency injection attack: a third-party Node.js package (used for build automation) had been compromised by attackers who modified it to include a backdoor.
4. The backdoor, once executing on the build server with npm credentials installed, had installed a data harvesting bot that copied the entire source code repository (35 GB), sensitive configuration files (2.3 GB), and documentation (400 MB) and staged them for exfiltration.

When the attacker confirmed that the build server had internet access (which shouldn't have existed), they scheduled the exfiltration to occur during off-peak hours (2-4 AM) to avoid raising alerts due to unusual bandwidth usage. Each night, the bot exfiltrated a portion of the staged data to the attacker-controlled server in Romania.

The investigation escalated quickly. The stolen data included:
- Complete source code for the company's proprietary payment processing engine
- OAuth credentials for integration with three major bank partners
- Database schemas and connection strings for customer production databases
- Private cryptographic keys for TLS certificate signing

If the exfiltration had continued undetected, the attacker would have obtained the complete blueprint of the company's financial services platform, enabling them to either sell it to competitors or use it to conduct targeted attacks against CloudScale's customers.

## What Went Right

- **[[Netflow-sflow-ipfix]] monitoring detected the exfiltration**: Without [[network-monitoring]], this attack could have continued indefinitely. The consistent data flow pattern was easily recognizable once the monitoring system was in place.
- **[[Baseline-establishment]] enabled anomaly detection**: The system established a baseline of normal traffic patterns (primarily internal network traffic, some external API calls, updates). The 50 Mbps stream to Romania immediately violated the baseline.
- **Rapid containment**: Once the exfiltration was discovered, the security team immediately revoked the compromised npm credentials, isolated the build server, and invalidated all OAuth tokens that had been exposed.
- **Forensic preservation**: By examining the [[netflow-sflow-ipfix]] records, the forensics team could determine exactly when the exfiltration started and how much data had been stolen, enabling them to notify customers about the scope of the breach.

## What Could Go Wrong

- **No [[netflow-sflow-ipfix]] monitoring**: Without flow-based monitoring, the exfiltration could have continued indefinitely. [[packet-capture-pcap]] at every network tap would have consumed massive storage and processing overhead, but [[netflow-sflow-ipfix]] provides efficient visibility.
- **Overly permissive [[disable-unnecessary-services-and-ports]] outbound rules**: The firewall rule allowed "any port 443 to any destination." If it had been scoped to "port 443 to [list of specific package repository IPs]", the exfiltration wouldn't have been possible.
- **No monitoring of [[port-mirroring-span]] ports**: The attacker was sophisticated enough to exfiltrate through encrypted HTTPS (port 443) rather than obvious data transfer protocols (SFTP, FTP, raw TCP). Only [[netflow-sflow-ipfix]] provided visibility into the encrypted traffic volume.
- **No [[baseline-establishment]] for CI/CD environments**: If the team had simply accepted all traffic from the CI environment as "normal," the exfiltration wouldn't have been detected. [[baseline-establishment]] is critical for detecting anomalies.
- **Missing supply chain security controls**: The compromised npm package should have been caught by dependency scanning and integrity verification before it was deployed. This attack exploited a supply chain vulnerability.

## Key Takeaways

- **[[Netflow-sflow-ipfix]] is essential for detecting data exfiltration**: Flow-based monitoring provides efficient visibility into traffic volume and patterns without the storage overhead of full packet capture. It's the ideal tool for detecting anomalous data flows.
- **[[Baseline-establishment]] enables anomaly detection**: Collect NetFlow records for 2-4 weeks to establish normal traffic patterns. Then alert on any traffic that deviates significantly from the baseline (e.g., new external destinations, unusual volumes, unusual times).
- **Egress filtering requires allow-listing, not deny-listing**: Instead of "block known-bad traffic," use "allow only known-good destinations." Outbound rules should specify exact target IPs/hostnames, not broad port-based rules.
- **CI/CD environments need special scrutiny**: Build systems have credentials, source code, and often internet access for fetching dependencies. Monitor them aggressively for suspicious outbound traffic, unusual repository clones, and changes to build artifacts.
- **[[Bandwidth-monitoring]] can detect exfiltration speed**: If an attacker exfiltrates 18 GB per night (50 Mbps × 103 minutes), calculate the total data stolen to understand breach scope: 9 days × 18 GB = 162 GB. This helps prioritize customer notification scope.
- **Encrypted traffic volume is still observable**: Even if the attacker uses HTTPS encryption, [[netflow-sflow-ipfix]] still reveals the source, destination, port, and byte count. An attacker exfiltrating 50 Mbps to a non-whitelisted destination is detectable.

## Related Cases

- [[case-siem]] — SIEM systems can correlate NetFlow data with authentication logs to identify which user accounts were used during suspicious data transfers.
- [[case-ids-ips]] — A network-based IDS can monitor for exfiltration patterns, but it requires either unencrypted traffic or decryption at the network level.
- [[case-threat-hunting]] — Once an exfiltration is detected, [[threat-hunting]] across the environment can identify if other systems were compromised with the same backdoor or dependency injection attack.
