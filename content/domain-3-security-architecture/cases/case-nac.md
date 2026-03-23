---
title: "Case: The Enrollment Catastrophe — NAC Locks Out 4,000 Students"
description: "A university implements 802.1X Network Access Control for the first time on day one of the spring semester. 4,000 students cannot connect to the network because their BYOD devices fail basic security posture checks. The help desk is overwhelmed with 600 tickets by noon."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

Pacific State University has 35,000 students, and the vast majority bring personal devices to campus: laptops, tablets, phones, and IoT gadgets. The campus Wi-Fi network had been open for years—no authentication, no device checks, just connect and go. The IT Director, Dr. Lisa Chen, and Chief Information Security Officer Marcus Thompson recognized this was a security liability. Students' devices could harbor malware, could be compromised, or could be stolen and used to attack the network.

In January 2024, they decided to implement **802.1X Network Access Control** and mandatory device compliance checking. The plan was sound in principle:

1. Require all students to authenticate with their university credentials
2. Scan devices for antivirus software, firewall, OS patch level
3. Only allow devices meeting the compliance baseline to connect
4. Non-compliant devices would be quarantined to a separate network for remediation

The IT team implemented the NAC system during the winter break using a Cisco Identity Service Engine (ISE) platform. They configured policies:

- **Required on all devices**: Antivirus software installed and up-to-date
- **Firewall enabled** on Windows/Mac systems
- **Recent OS patches** (within the last 90 days for security updates)
- **Device encryption** enabled on laptops

The system was tested with a small sample of students during the break. Those tests passed. NAC was enabled campus-wide on the night before spring semester began, January 15, 2024.

On the morning of January 15, 4,000 students showed up on campus wanting to connect to the Wi-Fi. The [[8021x|802.1X]] authentication portal appeared. Students entered their university credentials. The system scanned their devices. And then: **Network Access Denied**.

The failure messages were cryptic:

- "Device does not meet security requirements"
- "Antivirus software not detected"
- "Device encryption not enabled"
- "Operating system is unsupported"

Students tried again. Same error. They went to the IT help desk. By 10 AM, 300 students were waiting in the help desk queue. By noon, 600. The help desk had 12 staff members to process complaints; they could handle maybe 100 per hour. The queue grew exponentially.

Dr. Chen walked to the help desk around 11 AM to assess the situation. It was chaos. Students were frustrated. One student needed to submit a grad school application that day. Another had an online exam starting in 30 minutes. A group of international students didn't have antivirus software because they couldn't afford the commercial licenses in their home countries.

The root problems became apparent:

**Problem 1: Legacy Windows 7 devices**:
- Many older campus computers still ran Windows 7, which had been unsupported by Microsoft since 2020
- The NAC policy refused to allow unsupported OS versions
- But some graduate students had been using the same laptop for 5+ years

**Problem 2: Antivirus detection issues**:
- The NAC system looked for specific antivirus vendors (Norton, McAfee, Kaspersky, Bitdefender)
- Students with open-source antivirus (ClamAV, Snort) or lightweight solutions (Windows Defender) were rejected
- Windows Defender wasn't being detected properly because the ISE wasn't checking the right registry keys

**Problem 3: Encryption enabled but not recognized**:
- Some Mac students had FileVault enabled, but the system wasn't detecting it properly
- Linux systems don't have standard encryption detection, so all Linux devices were rejected

**Problem 4: No guest network for non-compliant devices**:
- The NAC system was blocking devices entirely instead of quarantining them to a guest network where students could access the remediation portal
- Students couldn't even access instructions on how to become compliant because they had no network access

**Problem 5: No advance warning or training**:
- Students weren't informed that NAC was being deployed
- No documentation on how to prepare their devices
- No tutorial on which antivirus software was compatible

By 1 PM, Dr. Chen made an emergency decision: disable NAC enforcement across the campus. The system would continue to *monitor* device compliance (logging violations for analysis) but wouldn't *block* non-compliant devices.

The queue at the help desk began to clear. Within 30 minutes, all 4,000 students who had been denied could reconnect.

But the damage was done. The help desk fielded 600+ support tickets that day. Social media exploded with complaints: "Pacific State's IT is blocking students from studying," "The university doesn't care about student productivity," "I paid tuition and can't even use the network."

The administrative backlash was swift. The Faculty Senate demanded a meeting. Student government called for the IT Director's resignation. The provost questioned whether security was worth the operational disruption.

Dr. Chen and Marcus spent the next week reassessing the rollout. What went wrong?

**Key Mistakes:**

1. **Big-bang deployment instead of phased rollout**: Enabling NAC for the entire campus on day one of the semester maximized operational impact. A phased rollout (faculty first, then staff, then students) would have revealed problems before affecting 35,000 people.

2. **No grace period or remediation path**: Non-compliant devices should have been routed to a guest network where students could download compatible antivirus, enable encryption, and transition to compliance over a week or two.

3. **Overly strict policies that didn't match reality**: Requiring Windows Defender recognition when ISE wasn't properly checking for it was a bad policy. Open-source antivirus should have been acceptable.

4. **No advance communication or training**: Students had zero warning. Sending an email weeks before the rollout explaining NAC and how to prepare would have prevented 70% of the help desk tickets.

5. **Insufficient testing with real-world devices**: The test devices were all modern, corporate-standard laptops. Real-world student devices included Windows 7, old Macs, Chromebooks, Linux machines, and phones with custom ROMs.

Marcus and Dr. Chen redesigned the rollout:

**New Approach:**

1. **Phased rollout** (3 weeks):
   - Week 1: Voluntary opt-in for students who wanted early access
   - Week 2: Faculty and staff deployment
   - Week 3: Full campus enforcement

2. **Grace period** (2 weeks):
   - Devices failing compliance would route to "remediation Wi-Fi"
   - Students could access instructions, antivirus downloads, and support without being blocked
   - IT staff would help students troubleshoot encryption and antivirus installation

3. **Revised policies**:
   - Accept Windows 7 devices (but quarantine them for remediation)
   - Accept any antivirus that reports successful scans, not just vendor lists
   - Accept any disk encryption or full-disk encryption, not just specific implementations
   - Accept iOS and Android devices with basic security (passcode, automatic lock)

4. **Communication campaign**:
   - Email campaign explaining NAC 4 weeks before rollout
   - Poster campaign with "Is your device NAC-ready?" checklist
   - Office hours where IT staff helped students prepare
   - Video tutorials on enabling encryption and antivirus

5. **Metrics and monitoring**:
   - Track remediation rates by device type
   - Monitor help desk ticket patterns
   - Measure network access success rate by cohort

The revised rollout in March 2024 proceeded smoothly. By the end of the grace period, 98% of devices were compliant. The help desk received 47 tickets instead of 600. Student satisfaction was high. The NAC system successfully improved network security without operational disaster.

## What Went Right (in the Revised Approach)

- **Phased rollout caught issues early**: Faculty devices revealed antivirus detection problems before student deployment.
- **Remediation network provided graceful degradation**: Non-compliant devices could still connect but were isolated and encouraged to become compliant.
- **Communication prevented surprise and frustration**: Students who knew about NAC weeks in advance prepared their devices and had fewer compliance issues.
- **Flexible policies matched reality**: Accepting diverse antivirus software and encryption implementations instead of rigidly requiring specific vendors.

## What Could Go Wrong (from the Initial Deployment)

- **Blocking on day one of the semester was catastrophic timing**: Students needed network access to submit assignments, take exams, and access course materials on day one.
- **No guest network forced students to choose between compliance and access**: A [[guest-networking]] path would have provided remediation options without blocking.
- **Policy too strict for the environment**: University networks serve diverse devices (old, new, custom, BYOD). Policies must reflect that diversity or have a remediation path.
- **No stakeholder communication created backlash**: Security decisions that affect 35,000 people need months of advance notice, not surprise deployment.

## Key Takeaways

- **[[8021x|802.1X NAC]] should be rolled out phased, not all at once**: Start with a small cohort, validate policies, discover edge cases, then expand.
- **[[Guest-networking|Guest networks]] are essential for NAC deployments**: Non-compliant devices should be quarantined to a remediation network, not blocked outright. This reduces help desk load and provides a path to compliance.
- **NAC policies must account for device diversity**: BYOD environments include old devices, custom configurations, and non-standard software. Policies should be flexible or have exceptions.
- **Grace periods prevent operational catastrophe**: When enabling security controls that might block users, provide a grace period (1-2 weeks) to find and fix problems.
- **Communication is part of security implementation**: Stakeholders (students, faculty, staff) need to understand what's changing, why, and how to prepare. Surprise deployments create friction and undermine trust.
- **Remediation networks reduce help desk load**: Students with non-compliant devices should be able to self-service remediation (download antivirus, enable encryption) on a guest network rather than going to the help desk.

## Related Cases

- [[case-network-segmentation]] — How NAC enforcement relates to network zoning and isolation
- [[case-endpoint-security]] — Device posture checking and antivirus requirements
- [[case-zero-trust]] — NAC as part of a zero-trust network architecture

