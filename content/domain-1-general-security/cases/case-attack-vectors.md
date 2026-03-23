---
title: "Case: The Exposed Jenkins Server — Attack Surfaces Gone Unmanaged"
description: "A red team penetration test at a regional bank uncovers 23 undocumented internet-facing services, including an abandoned Jenkins CI/CD server with default admin credentials. The CISO realizes the attack surface inventory has drifted catastrophically."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

First Trust Bank operates 127 branches across the Midwest, with approximately 2,300 employees and a core banking platform running on a mix of legacy mainframe systems and modern cloud infrastructure. In January 2026, the Chief Information Security Officer, Patricia Wong, commissioned a third-party red team to conduct a comprehensive penetration test. The engagement scope was intentionally aggressive: "Assume you're an external attacker trying to compromise our systems. Tell us everything you find."

On January 15, Patricia's team handed over the [[attack-surface-management|attack surface]] inventory they had documented: 47 internet-facing systems. This included web applications, VPN endpoints, email gateways, and administrative portals. The red team was given a budget of 120 hours and a six-week timeline.

Four weeks later, the red team's lead penetrator, Michael Torres, requested an urgent call with Patricia. He opened the meeting with a simple statement: "We found 23 systems that aren't on your inventory." The discovery went like this: While performing reconnaissance on First Trust's IP address ranges (123.45.0.0/16), Michael's team used Shodan queries combined with passive DNS records and SSL certificate transparency logs. They identified every TLS certificate ever issued for First Trust's domains. Cross-referencing these with active IP scanning revealed services that had never appeared in the official asset inventory.

The most critical discovery was a Jenkins CI/CD server running on jenkins.firsttrust-internal.com, which had a public DNS record pointing to 123.45.34.178. This server was used by the software development team for automated testing and build processes. It had been commissioned in 2018 to support a now-abandoned mobile banking app project. When the project was killed, the server was abandoned but never decommissioned. It still had default Jenkins credentials: username "admin" with password "admin." Within 60 seconds of connecting, Michael gained access to Jenkins's job history, which included build logs containing database connection strings, AWS access keys stored in plaintext, and source code repositories of internal tools.

The implications were staggering: from Jenkins, Michael could trigger arbitrary build jobs, which meant he could execute code on the build server's filesystem. That server was running on a shared Amazon EC2 instance that also hosted the application deployment pipeline. By modifying a build job, Michael could inject arbitrary code into the next release of First Trust's customer-facing banking application.

Patricia's hands were shaking as she listened. She immediately called for an emergency war room. By 3 PM that day, the Jenkins server was yanked offline. A forensic team began examining the logs to determine if the server had been compromised by actual attackers before Michael's discovery. The audit logs showed no evidence of unauthorized access, but there was no way to be certain—the server had minimal auditing enabled, and forensic artifacts from several months prior had already been purged.

The discovery of Jenkins prompted deeper investigation. Michael's team methodically worked through the 23 undocumented services. Among them were:

1. An old staging environment for a third-party vendor that had gone dormant but was still accessible
2. A legacy authentication server (LDAP) that was supposed to be decommissioned in 2022 but was still responding to queries
3. Three development databases accessible directly from the internet with credentials in DNS TXT records (a hack from a previous admin)
4. A backup Splunk instance serving as a cold storage repository, accessible with a shared password in a wiki
5. Five administrative dashboards for network monitoring tools, all behind HTTP basic authentication with weak credentials
6. An unpatched WebLogic server hosting internal documentation that was vulnerable to CVE-2021-2109 (a three-year-old RCE vulnerability)

Patricia's chief architect, David Chen, realized that the asset inventory process had completely broken down. The bank had never implemented formal [[attack-surface-management|asset management]]. When teams spun up servers, they submitted a ticket, but when they decommissioned services, they just stopped paying for them. DNS records lingered. SSL certificates renewed automatically. IP addresses remained allocated to projects that no longer existed.

The red team's assessment became a wake-up call. Patricia commissioned an immediate audit using automated tools: Shodan queries, SSL certificate transparency scanning, WHOIS lookups, passive DNS historical records, and reverse IP lookups. The results were even worse than the manual findings—the automated tools identified 47 additional services that Michael's small team had no time to fully investigate. These included WordPress instances hosting team wikis, abandoned Jira servers, old Confluence instances, and exposed Kubernetes API servers.

By day 35 of the engagement, the red team had identified 70 unique internet-facing services. Of these, 47 were documented and owned by specific teams, 15 were "legacy and probably decommed but we're not sure," and 8 were complete mysteries with no owner identified.

Patricia made a critical decision: she would halt the red team penetration testing and pivot to pure discovery and inventory. Michael's team spent the remaining 40 hours documenting every service: its IP address, hostname, SSL certificate, port numbers, running software, observed vulnerabilities, and estimated exposure level. Each finding was accompanied by questions: "Who owns this?" "Why is it internet-facing?" "When will it be decomissioned?"

## What Went Right

- **Third-party red team brought external perspective**: Internal security teams often miss infrastructure they've become accustomed to. An outside perspective identified blind spots.
- **Shodan and passive reconnaissance techniques are effective**: Michael's team didn't need to exploit anything—passive information gathering (DNS lookups, SSL cert scanning, port scanning) revealed most of the attack surface.
- **Rapid containment once critical systems were identified**: The Jenkins server was pulled offline within hours of discovery, preventing potential compromise.
- **Forensic examination happened quickly**: Although inconclusive, the attempt to determine if Jenkins had been previously compromised showed good incident response muscle memory.
- **Executive escalation was appropriate**: Patricia immediately understood the severity and committed resources to asset discovery and remediation.

## What Could Go Wrong

- **No formal [[attack-surface-management]] process**: The bank had no system to ensure that every internet-facing service was documented, approved, and periodically reviewed.
- **Lack of [[defense-in-depth]]**: Default credentials on Jenkins meant a single compromised credential gave complete access. There was no WAF, IP filtering, or additional authentication required.
- **Abandoned infrastructure lingered indefinitely**: The Jenkins server had been unused for three years but was never formally decommissioned. DNS records and certificates renewed automatically, making it a "zombie" service.
- **No egress filtering or network segmentation**: Even if Jenkins had been compromised, the attacker could pivot to internal systems without any network boundaries.
- **Minimal logging and auditing on critical systems**: Jenkins had no meaningful logs, no MFA, and no session recording. An attacker could have used it for weeks undetected.
- **Inventory management was manual and unreliable**: Relying on teams to self-report assets they'd created led to drift. Many teams forgot about services they'd stood up years earlier.
- **No periodic security scanning of IP ranges**: A basic quarterly scan of the bank's IP ranges using Shodan and passive DNS would have caught this drift immediately.

## Key Takeaways

- **[[Attack-surface-management]] must be automated and continuous**: Do not rely on teams to report their own infrastructure. Automatically scan your IP ranges, domain names, and certificate transparency logs. Compare results weekly against the official inventory.
- **Default credentials are critical vulnerabilities**: Any service accessible from the internet must require strong authentication AND preferably MFA. Default credentials ("admin/admin") on CI/CD systems are disaster-level findings.
- **Internet-facing services require explicit approval**: Every service that has a public IP or DNS record should have documented business justification, an assigned owner, and a planned decommissioning date.
- **Decommissioning must be enforced at the infrastructure level**: Don't rely on teams to remove DNS records and shut down servers. Use infrastructure-as-code to manage lifecycle: if a server isn't in the approved inventory, it should be automatically terminated.
- **Assume passive reconnaissance will be thorough**: Attackers use Shodan, SSL transparency logs, and reverse IP lookups constantly. Treat passive discovery results as seriously as active scanning results.
- **[[Human-vectors]] in infrastructure management create huge risks**: Storing credentials in DNS TXT records, wiki pages, and build logs is a common pattern that needs to be detected and eliminated.
- **Periodic red teaming and asset discovery are essential**: Commission external teams every 12-18 months to perform comprehensive reconnaissance and identify drift.

## Related Cases

- [[case-social-engineering]] — How initial access is often gained through phishing the humans managing infrastructure
- [[case-vulnerability-management]] — Assessing and remediating all 70 discovered services requires a formal vulnerability management process
- [[case-defense-in-depth]] — How multiple security boundaries would have prevented Jenkins from being exploitable even if discovered
- [[case-threat-actors]] — Understanding how real attackers systematically enumerate attack surfaces exactly as Michael's red team did
