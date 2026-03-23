---
title: "Case: The Coffee Shop Demonstration — SSL Stripping Over Public Wi-Fi"
description: "An ethical hacker demonstrates SSL stripping and man-in-the-middle attacks over coffee shop Wi-Fi, capturing an employee's Slack and email credentials. The CISO's entire remote work policy is overhauled by Monday."
draft: false
date: 2026-03-21
tags:
  - domain/2
  - type/case
---

## The Scenario

Velocity Consulting, a global firm with 800 employees, had implemented remote work policies during 2024 but had never conducted a security assessment of the actual threats employees faced in unsecured networks. In February 2026, the Chief Information Security Officer, Marcus Lewis, hired a red team from a boutique security firm to conduct a week-long assessment of remote work vulnerabilities. The red team's charter was simple: demonstrate realistic attacks that employees faced and quantify the risk.

On Monday, February 24, 2026, at 9:47 AM, red team member Alex Chen set up a laptop at a Starbucks near Velocity's largest office in San Francisco's Financial District. The Starbucks had open Wi-Fi with no WPA2 encryption (customers asked for the password, which was "starbucks2024"—the same for all locations, unchanged for 6 months). Alex configured a Linux laptop to act as a rogue access point using hostapd and dnsmasq, creating a network named "Starbucks-Guest-WiFi" that mirrored the legitimate network's SSID. When employees connected to what they thought was the real network, they were actually connecting to Alex's interceptor.

At 10:15 AM, Sarah Wong, a senior consultant at Velocity, walked into the same Starbucks. She sat down at a table, opened her MacBook, and connected to "Starbucks-Guest-WiFi" (without verifying which one was legitimate). She opened her web browser and navigated to `slack.com`. Under normal circumstances, Slack's website would redirect her browser to `https://slack.com` (secure). But Alex's interceptor was configured to perform [[ssltls-stripping]]—a technique that removes the secure "s" in "https" and presents the user with an unencrypted "http://" connection.

The browser address bar showed `http://slack.com` (missing the "s"). Most users don't notice this difference. Sarah entered her username and password:

```
Username: sarah.wong@velocity-consulting.com
Password: SlackPass2024#VelocityConsult
```

The credentials were transmitted in plaintext HTTP over the Wi-Fi network, directly visible to anyone with a packet sniffer. Alex captured the traffic using Wireshark, a packet analysis tool. Within seconds, Alex had Sarah's credentials, her workspace name, and an authenticated session token. The entire capture took 90 seconds from initial connection to credential theft.

At 10:17 AM, Alex used Sarah's credentials to log into Slack via the web interface from another coffee shop. Alex then read all of Sarah's Slack conversations, including: (1) sensitive client discussions about a $120M acquisition negotiation, (2) internal project details about new product launches scheduled for Q2, (3) HR discussions about organizational restructuring plans. This information, if leaked, could be worth millions to competitors or sophisticated threat actors.

At 2:00 PM that same day, Alex scheduled a meeting with Marcus Lewis (the CISO) and demonstrated the attack live in a conference room. Marcus watched Alex connect to a test network, capture credentials, and read messages, all within 5 minutes. The implications were clear: Velocity's remote work policy was fundamentally broken.

By 4:30 PM, Marcus had convened the security and IT leadership teams. By 6:00 PM that evening, a comprehensive remediation plan was drafted. By 9:00 AM the following morning (Tuesday), the policy was rolled out to all 800 employees.

## What Went Right

- **Proactive red team engagement revealed actual threats**: Rather than relying on theoretical risk assessments, hiring a red team to demonstrate attacks on real employees in real environments provided concrete evidence of vulnerability. This converted abstract risk into visceral understanding.

- **Rapid policy update and deployment**: Once the threat was demonstrated, leadership approved and deployed a comprehensive new policy within 18 hours. This speed was possible because the team had pre-planned remediation options and could implement immediately.

- **Multi-layered response beyond just VPN**: Rather than just requiring a VPN (which would have solved the immediate problem but been inconvenient), the team implemented [[encryption]], [[https-spoofing]] defenses, corporate proxies, and device verification. This created defense-in-depth.

- **Security awareness training was data-driven**: With video evidence of the attack, training materials were far more compelling than theoretical discussions of [[ssl-stripping]]. Employees could see their own credentials being captured and understand the stakes.

## What Could Go Wrong

- **No [[https-spoofing|HTTP Strict Transport Security (HSTS)]] enforcement**: HSTS headers tell browsers "always use HTTPS on this domain" and are cached locally. When configured correctly (with preloading), HSTS makes [[ssltls-stripping]] attacks impossible because the browser will reject any non-HTTPS connection. Slack did have HSTS headers set, but many internal web applications didn't.

- **Employees can't distinguish between real and rogue access points**: Sarah connected to "Starbucks-Guest-WiFi" without verifying which one was legitimate. Many users don't know how to check network authenticity. Proper SSID verification and certificate pinning (browsers checking that certificates come from trusted CAs) would have protected against MITM attacks.

- **No mandatory VPN for remote workers**: Prior to this incident, Velocity's remote work policy "recommended" VPNs but didn't mandate them. Many employees used public Wi-Fi directly for convenience. A mandatory VPN policy with enforcement (device access revoked if VPN is disconnected) would have prevented this attack entirely.

- **No [[ssltls-interception-ssl-proxy|corporate proxy or SSL inspection]]**: Velocity had no corporate gateway that inspected all outbound traffic. If all traffic had been routed through a corporate proxy with SSL/TLS termination and inspection, the stolen credentials would have been visible to the security team for immediate alert and incident response.

- **No device posture checking**: There was no verification that employee devices were "healthy" (running current OS patches, endpoint security active, VPN connected) before accessing company resources. A device that can't prove it's on the VPN or has updated security software shouldn't be allowed to access Slack or email.

## Key Takeaways

- **[[ssltls-stripping]] removes HTTPS encryption if not defended**: Attackers can intercept traffic on unsecured networks and downgrade HTTPS to HTTP, capturing credentials. [[https-spoofing|HSTS (HTTP Strict Transport Security)]] headers, certificate pinning, and [[encryption]] are essential defenses.

- **Public Wi-Fi is inherently untrusted**: Assume that all traffic on public Wi-Fi is visible to network-adjacent attackers. Mandatory VPN is the only reliable defense for remote workers.

- **[[man-in-the-middle]] attacks don't require sophisticated tools**: Alex Chen used standard tools available to any security researcher: hostapd (Linux Wi-Fi access point), dnsmasq (DNS server), and Wireshark (packet capture). No custom malware or zero-day exploits were needed. Any technically competent attacker can execute these attacks.

- **Credential theft on unsecured networks is immediate**: From initial connection to complete credential compromise: 90 seconds. From credential theft to authenticated access: 2 minutes. From initial attack to reading sensitive business data: 3 minutes. Once credentials are captured, the attacker has the time advantage.

- **[[vpn|VPN]] adoption requires both policy and enforcement**: Recommending VPN is insufficient; it must be mandatory with technical enforcement (endpoint agent checking VPN status before allowing resource access, network access control blocking non-VPN traffic, etc.).

## Related Cases

- **[[case-encryption]]** — Understanding [[ssltls-stripping]], [[https-spoofing]], and how cryptographic protections prevent credential theft; learning about [[encryption]] as a defense against on-path attacks.

- **[[case-network-attacks]]** — ARP spoofing, DNS spoofing, and other network-layer attacks that enable [[man-in-the-middle]] conditions; understanding [[arp-spoofingpoisoning]] as a complementary attack to SSL stripping.

- **[[case-wireless-attacks]]** — Rogue access points, [[evil-twin]] networks, and Wi-Fi eavesdropping; understanding how attackers create the conditions for on-path attacks in the first place.

- **[[case-vpn]]** — Designing VPN infrastructure for remote workers; understanding [[encryption]], [[authentication]], and [[defenses]] against [[relay-attacks]] and [[session-hijacking]] in VPN contexts.
