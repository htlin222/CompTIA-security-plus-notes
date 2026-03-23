---
title: "Case: The Silent Admin Achievement — Red Team Pwns Aerospace Contractor"
description: "A red team engagement at an aerospace contractor achieves domain admin in 4.5 hours by chaining a phishing email, an unpatched print spooler vulnerability, and a Kerberoasted service account. The blue team detected nothing."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

Sterling Aerospace is a mid-size defense contractor specializing in precision guidance systems, with 800 employees and strict security requirements due to their Defense Counterintelligence and Security Agency (DCSA) facility security clearance. In March, they contracted a third-party red team firm to conduct a comprehensive penetration test under formal [[rules-of-engagement-roe]]. The engagement scope included network [[reconnaissance]], [[exploitation]], [[lateral-movement]], [[privilege-escalation]], and demonstrating persistence. The blue team (internal security) was not informed in advance—the red team's goal was to operate as close to a real attack as possible.

**Phase 1: Initial Access (0:00 - 0:47)**

The red team began with [[reconnaissance]], which in this case was entirely open-source: reviewing Sterling's public website, LinkedIn profiles, job postings, and DNS records. From the website's contact page, they identified the names and email addresses of Sterling's leadership team. The red team crafted a targeted phishing email appearing to come from the Chief Financial Officer, addressed to a finance analyst: "Hi Sarah, I need you to help coordinate a wire transfer for a supplier payment. Please review the attached invoice and let me know when you can start the process. — Tom."

The attachment was a specially crafted Word document that exploited a zero-day-equivalent vulnerability in Microsoft Word's macro execution handling. When Sarah opened the document at 9:15 AM, the macro silently executed PowerShell code that installed a Meterpreter reverse shell—a sophisticated [[exploitation]] payload that gave the red team interactive access to Sarah's workstation.

**Phase 2: Lateral Movement (0:47 - 2:30)**

With a foothold on Sarah's machine (IP: 192.168.10.45, hostname: STERLING-FIN-047), the red team immediately began [[lateral-movement]]. They harvested Sarah's cached NTLM credentials and began testing them against other systems on the network using a custom scanner.

One of the prized targets was the print server (STERLING-PRINT-01), which hadn't been patched in seven months. The red team exploited CVE-2021-1732, a critical vulnerability in the Windows Print Spooler service that allowed for arbitrary code execution with SYSTEM privileges. By sending a specially crafted print request to the print server, they gained SYSTEM-level access to the print server.

From the print server (running with SYSTEM privileges), the red team was able to enumerate the domain and identify service accounts—special accounts used by applications to authenticate to network resources. One service account stood out: `SVC_BACKUP` was used to run Sterling's backup automation system. The red team performed a [[kerberoasting]] attack: they requested a Kerberos ticket for the SVC_BACKUP service account and then used offline password cracking to recover its plaintext password (it was "Backup2023!").

**Phase 3: Domain Admin Compromise (2:30 - 4:31)**

With the SVC_BACKUP service account credentials, the red team could now authenticate to a backup server that had administrative privileges in the Active Directory domain. From that backup server, they deployed a persistence technique: they created a scheduled task that would execute a remote shell every 30 minutes, ensuring they would maintain access even if the original phishing victims changed their passwords.

Finally, at 4:31 PM (4 hours and 31 minutes after initial access), the red team executed their final attack: they used the backup server's administrative privileges to query Active Directory directly and add a newly created fake user account ("john.smith.intern") to the Domain Admins group. They then authenticated as this fake admin account and verified they had full domain administrator access across Sterling's entire Active Directory forest.

**The Blue Team's Response: Nothing**

Throughout the engagement, the blue team and their monitoring systems detected nothing. There were no alerts, no unusual activity flags, no incident tickets created. Sterling's Security Operations Center ran continuously during the red team's attack, but the alerts that were supposedly tuned to detect suspicious activity all failed to trigger:

- The EDR system had too many false positives and its alerting had been disabled by ops the previous week while they "tuned" it
- The SIEM wasn't configured to collect PowerShell execution logs or Kerberos authentication attempts
- Antivirus didn't recognize the custom Meterpreter payload because it had been polymorphically encoded
- The phishing email slipped past the email gateway's anti-phishing filters (the CFO's name was misspelled as "Tome" instead of "Tom," which the filter missed as a variation)
- The print server vulnerability wasn't in any known vulnerability scanning tools because it was patched by Microsoft but many organizations hadn't deployed the patch

When the red team presented their findings to Sterling's executive leadership, the response was shock. The security team claimed they had "mature detection capabilities," but they had detected zero out of four major attack phases.

## What Went Right

- **Comprehensive red team engagement**: Hiring an external firm with strict [[rules-of-engagement-roe]] allowed unbiased assessment without the blue team's preconceptions.
- **Testing-types included authentic threat patterns**: The red team didn't just "try random exploits"—they followed an attacker's playbook: initial compromise, lateral movement, persistence, privilege escalation.
- **Complete attack chain documentation**: The final report provided exact timestamps, attack techniques (mapped to MITRE ATT&CK), and remediation steps for each phase.

## What Could Go Wrong

- **EDR alerting disabled**: The endpoint detection system had been disabled in an attempt to "tune" false positives, eliminating the primary defense against malware execution.
- **SIEM missing critical data sources**: PowerShell execution logs and Kerberos authentication attempts are essential for detecting [[lateral-movement]] and [[privilege-escalation]] but weren't being collected.
- **Print spooler unpatched**: The seven-month gap between vulnerability disclosure and patching left Sterling vulnerable to a well-known attack vector.
- **Credential caching not disabled**: Sarah's cached NTLM credentials allowed the attacker to reuse them. Disabling credential caching would have forced new authentication.
- **Weak service account passwords**: The SVC_BACKUP password "Backup2023!" was crackable within minutes using dictionary-based password cracking.
- **No privileged access monitoring**: The backup server's administrative actions weren't being logged or monitored for unusual activity, allowing the attacker to operate freely.

## Key Takeaways

- **Red-team-vs-pen-test red teams are unbiased assessments of real-world defensive capabilities**: Penetration tests often only test known vulnerabilities. Red teams test whether defenders can actually detect and respond to attacks.
- **Exploitation success depends on unpatched vulnerabilities**: The print spooler vulnerability was disclosed seven months prior. A systematic [[vulnerability-management]] program would have eliminated this attack vector.
- **Lateral-movement detection requires logging and correlation**: PowerShell logs, Kerberos logs, and network traffic logs must all be collected and correlated to detect multi-step attacks.
- **Privilege-escalation via service account compromise indicates missing credential hygiene**: Service accounts with strong, unique passwords and periodic rotation are essential [[privileged-access-management]].
- **Rules-of-engagement-roe must be explicit and enforced**: The red team operated under agreed-upon boundaries. Clear ROE prevents unintended collateral damage and ensures the engagement reflects real-world constraints.
- **Persistence techniques must be detected and hunted**: Once an attacker achieves admin access, they typically leave persistence mechanisms. Detecting these (scheduled tasks, registry modifications, SSH keys) is critical to full remediation.

## Related Cases

- [[case-vulnerability-management]] — The unpatched print spooler was a known vulnerability; a vulnerability scanning program should have identified it before the red team exploited it.
- [[case-hardening]] — Disabling unnecessary services (like the Print Spooler if printing isn't needed) would have eliminated the attack vector.
- [[case-incident-response]] — A mature incident response program would have included hunt procedures to detect living-off-the-land attacks and persistence mechanisms.
