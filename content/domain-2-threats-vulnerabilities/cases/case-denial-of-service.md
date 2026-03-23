---
title: "Case: New Year's Eve DDoS — When Upstream Capacity Fails"
description: "A 400 Gbps DDoS attack hits at 11:15 PM on New Year's Eve targeting a major online ticketing platform. The on-call SRE discovers the upstream DDoS provider's scrubbing center is at capacity and can't absorb the traffic."
draft: false
date: 2026-03-21
tags:
  - domain/2
  - type/case
---

## The Scenario

TicketGenius is the largest online ticket marketplace in North America, processing approximately 5 million ticket transactions annually. On New Year's Eve 2025, at 11:15 PM EST, exactly 4 hours and 45 minutes before midnight, a massive [[denial-of-service|DDoS]] attack struck. The attack source was a botnet of approximately 50,000 compromised IoT devices and servers sending 400 Gbps of traffic (gigabits per second) toward TicketGenius's web infrastructure.

The attack was volumetric—not trying to exploit specific vulnerabilities but simply overwhelming the network with sheer volume. A typical DDoS of 100 Gbps is severe; 400 Gbps is catastrophic.

The on-call Site Reliability Engineer, Marcus Chen, received alerts at 11:16 PM. His immediate actions were:
1. Engage the DDoS mitigation provider (Cloudflare) to scrub the malicious traffic
2. Alert the incident commander
3. Monitor whether traffic was being successfully filtered

Cloudflare reported back at 11:23 PM: "We're seeing the attack. Our scrubbing center in the US East region is at capacity. We can absorb 300 Gbps; you're at 400 Gbps. Some traffic is getting through."

The problem was immediately clear: TicketGenius had subscribed to Cloudflare's standard DDoS protection, which covered attacks up to 300 Gbps. This attack exceeded that. The upstream provider had a tier above that (enterprise tier, capable of absorbing 1 Tbps attacks), but TicketGenius wasn't subscribed to it—the cost was three times higher, and nobody had thought the risk warranted the expense.

Marcus made a critical decision: activate the emergency bypass. TicketGenius had a secondary CDN (Amazon CloudFront) that they maintained for backup purposes. Marcus immediately:
1. Updated DNS records to point to CloudFront instead of Cloudflare
2. Deployed rate limiting rules to CloudFront to block obvious botnet traffic
3. Enabled CAPTCHA challenges to ensure requests were from humans, not bots

CloudFront reported a different situation: they had multiple scrubbing centers and the ability to distribute load across them. They could absorb the 400 Gbps. Traffic started flowing through CloudFront at 11:34 PM (18 minutes after the attack started).

But the attack wasn't over. The botnet continued attacking. At 11:47 PM, a second wave arrived—this time, 600 Gbps of traffic. The attackers had added more botnets. CloudFront's capacity was exceeded. The website became unavailable to legitimate users.

At midnight EST (the busiest time for a ticketing platform on New Year's Eve), TicketGenius's website was down. Concert tickets, comedy shows, sporting events—none of them could be purchased. Estimated revenue loss: $3.2M in ticket sales during those peak 45 minutes.

The attack lasted for 14 hours, peaking at 1.2 Tbps at around 2 AM EST (February 1). The attacker appeared to be using a sophisticated botnet that had massive capacity. By 1:30 PM on February 1, the attack ceased as suddenly as it had begun.

The forensic investigation later revealed:
- The botnet included approximately 200,000 IoT devices and servers
- Attack traffic originated from 150 countries
- The attack had a cost to the attacker of approximately $0 (using a rented botnet that had likely already been compromised for other malicious purposes)
- The attack to TicketGenius cost approximately $8.7M (lost ticket revenue, infrastructure costs, incident response, credit monitoring for potentially compromised data)

## What Went Right

- **DNS failover to secondary CDN was fast**: Switching to CloudFront took 18 minutes, during which some service was restored
- **Rate limiting and CAPTCHA helped reduce attack surface**: While not complete protection, these mechanisms prevented some of the botnet traffic
- **The attack didn't result in data breach**: DDoS attacks disrupt availability but don't exfiltrate data (unless combined with other attacks)
- **Incident response team was mobilized quickly**: Within minutes, the incident commander had escalated to executives and the DDoS provider

## What Could Go Wrong

- **Insufficient DDoS protection tier**: TicketGenius had the standard tier (300 Gbps capacity) but faced a 400+ Gbps attack
- **No pre-arranged backup CDN capacity**: The backup CDN also became overwhelmed when traffic increased to 600 Gbps
- **DNS failover took 18 minutes**: In a mature disaster recovery plan, failover should be seconds, not minutes
- **No anycast network or multi-CDN setup from the start**: A truly robust setup would have traffic distributed across multiple CDN providers from the beginning
- **Rate limiting was reactive, not preemptive**: Rate limiting rules were added during the attack, not pre-configured before the attack occurred
- **No attack pattern database for botnet identification**: Traffic could have been filtered more aggressively if the botnet signatures were known in advance

## Key Takeaways

- **[[Amplification-attack|Volumetric DDoS attacks]] require upstream mitigation**: No individual website can absorb 400+ Gbps. The mitigation must happen at the CDN or ISP level, before traffic reaches your servers.
- **DDoS protection tiers matter**: A standard tier sufficient for 300 Gbps attacks is insufficient for targeted, well-funded attackers. Consider your value as a target and pay for protection that covers likely attack sizes.
- **Failover to secondary providers should be automatic or near-automatic**: 18 minutes is a long time to be unavailable. Implement health checks and automatic DNS failover to backup CDN providers.
- **Rate limiting is a defense layer, not a complete solution**: Rate limiting can reduce botnet traffic but won't stop a massive DDoS attack. It's one layer in [[defense-in-depth]].
- **[[Botnet|Botnets]] are rented services for attackers**: An attacker doesn't need to own a botnet. They can rent compromised IoT devices and servers for a few hundred dollars. Defend accordingly.
- **New Year's Eve is peak targeting time**: High-value events and holidays attract DDoS attackers. Ensure mitigation capacity during these windows.
- **Cost-benefit analysis of DDoS protection is complex**: The $3.2M enterprise tier DDoS protection looked expensive at $9M per year until an attack cost $8.7M in a few hours.

## Related Cases

- [[case-network-monitoring]] — Detecting unusual traffic patterns that signal DDoS attacks
- [[case-resilience-and-redundancy]] — Building redundant infrastructure and failover mechanisms
- [[case-disaster-recovery]] — Planning for rapid recovery when primary systems become unavailable
