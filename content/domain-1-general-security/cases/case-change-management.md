---
title: "Case: The Black Friday Outage — When Change Management Fails at Scale"
description: "A logistics company's network infrastructure goes down for four hours on Black Friday after an unauthorized firewall rule change bypasses the change advisory board entirely. The $2.3M in lost revenue forces a reckoning on emergency procedures."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

Logistics Dynamics is a $450M per year logistics and fulfillment platform based in Memphis that handles shipping coordination for 15,000+ retail and e-commerce customers. The company's core business happens on a handful of peak days: Black Friday, Cyber Monday, and the December holiday season. On Black Friday 2025 (November 28), the company was processing approximately 18,000 shipment requests per minute through their real-time logistics API.

At 10:47 AM CST on Black Friday, a catastrophic network outage crashed the entire logistics API. Customers couldn't submit shipments. Orders sat in queues. The company's SLA guarantees promised 99.9% uptime; they were now failing spectacularly. For four hours, from 10:47 AM to 2:54 PM, the API was completely unavailable.

The immediate post-incident review uncovered the root cause: an undocumented firewall rule change. At 10:32 AM, a network engineer named David Torres had logged into the Cisco ASA firewall and added a rule to drop traffic on port 443 (HTTPS, used by all API traffic) from a specific source IP. David's intention was to block what he believed was a DDoS attack—he'd observed unusual traffic patterns in his monitoring dashboard. He made the change without following any change management procedure, without alerting the [[change-advisory-board-cab]], and without notifying the incident response team that he was making infrastructure changes.

The problem: the source IP David had blocked was actually a legitimate AWS CloudFront distribution that Logistics Dynamics uses for CDN-accelerated API traffic. By dropping traffic on port 443 from that IP, David had inadvertently blocked all traffic from CloudFront to the internal API servers. The unusual traffic pattern he'd observed was normal Black Friday traffic, not a DDoS attack. The ASA firewall logs later showed that David's rule had dropped 98% of the incoming API traffic for 4 hours straight.

The CEO, Rachel Hernandez, was in the war room when IT director Tom Chen pulled up the firewall configuration logs. Rachel asked one question: "Who authorized this change?" Tom scrolled through the logs. "It appears David Torres made it at 10:32 AM." Rachel's next question: "Where's the change request?"

Tom pulled up the change management system (a ServiceNow instance that logged all infrastructure changes). There were zero change requests for any firewall rules on Black Friday. David's change was completely undocumented and unapproved.

Rachel's face turned red. "That change would have been rejected if it had gone through the [[change-advisory-board-cab]]. Find David right now."

David was found immediately. When asked why he hadn't filed a change request, his answer was: "I thought it was an emergency DDoS attack. I needed to act immediately. I didn't have time to file a ticket and wait for CAB approval."

This answer, while understandable, exposed a critical gap in the company's emergency change procedures. The [[change-advisory-board-cab]] process required approval, which typically took 4-8 hours. For a genuine emergency (a real DDoS attack, for example), waiting 4-8 hours would be unacceptable. But the company had never defined what "emergency change" meant or what procedures should be followed for true emergencies.

Rachel called for a complete post-incident review, which extended over two weeks. The findings were damning:

1. **No emergency change procedure existed**: The change management policy didn't account for genuine emergencies. It was all-or-nothing: either follow the 4-8 hour approval process, or bypass it entirely.

2. **No role-based change authorizations**: Anyone with firewall credentials could make changes. There was no segregation between read-only monitoring access and change-making access.

3. **Firewall changes weren't replicated to a test environment**: Changes should have been tested against a simulated attack pattern before being deployed to production.

4. **No real-time alerting for firewall rule changes**: The security team found out about the change only after the outage. There should have been immediate alerts when production firewall rules were modified.

5. **DDoS detection was poorly configured**: David's observation of "unusual traffic" wasn't actually based on automated DDoS detection—it was his subjective interpretation of his monitoring dashboard.

6. **No runbook for responding to DDoS**: If it had been a real attack, the proper response (engaging the DDoS mitigation provider, scaling CDN capacity, enabling rate limiting) was never documented.

The incident cost Logistics Dynamics approximately $2.3M in lost revenue during the 4-hour outage. More damaging was the reputational cost: customers found out their shipments couldn't be processed, and 47 of them proactively reached out to competitors for alternative logistics providers.

Rachel mandated a complete redesign of change management within 30 days.

The remediation included:

**Week 1-2: Define emergency change procedures**

- Define what constitutes an emergency (genuine DDoS attack verified by automated detection, critical system failure, active security incident with ongoing data loss)
- Create an "emergency change" process: brief (5-minute) verbal approval from the on-call engineering director + immediate documentation post-approval
- Establish that emergency changes must include a 4-hour rollback window (if the change causes problems, it can be reversed within 4 hours)
- Require retrospective approval from CAB within 24 hours of the emergency change

**Week 2-3: Implement role-based access**

- Separate "monitor and alert" credentials from "make changes" credentials
- Require MFA for any firewall change
- Implement a change approval workflow in ServiceNow that blocks the actual change execution until approval is recorded

**Week 3-4: Add real-time alerting**

- Configure Splunk to alert the security team immediately when any firewall rules are added, modified, or deleted
- Alert includes the user who made the change, the timestamp, what rule was changed, and what the new configuration is
- Alert goes to security oncall and the change log, creating an audit trail

**Week 4+: Build testing infrastructure**

- Create a test firewall configuration that mirrors production
- All non-emergency changes must be tested in the test environment for at least 1 hour before production deployment
- DDoS attack patterns can be simulated using tools like iperf or actual traffic from a DDoS mitigation service's test platform

By December 1 (three days after the outage), the new procedures were documented and approved. By December 8, the technical controls (role-based access, MFA, automated alerting) were deployed. By December 15, the testing infrastructure was ready.

The team also discovered a silver lining: after implementing proper change management, they realized that 47% of the firewall changes over the previous year had been made without [[change-advisory-board-cab]] approval. A complete audit and re-approval process was initiated, catching several rules that had been added for "temporary workarounds" that were never removed.

## What Went Right

- **Rapid root cause analysis**: The firewall logs clearly showed David's rule change and the exact timestamp. Root cause was identified within 2 hours.
- **Post-incident review was thorough and honest**: Rachel didn't blame David; instead, she recognized that the change management process had failed to account for emergencies.
- **Executive commitment to remediation**: The CEO prioritized fixing the change management gap even though it would require investment and process changes.
- **Clear emergency change definition**: Instead of arguing about whether emergencies justified bypassing CAB, the new process defined exactly what constituted an emergency.
- **Automated controls enforce compliance**: Real-time alerting and role-based access ensure that future unauthorized changes are immediately visible and require MFA.

## What Could Go Wrong

- **No emergency change procedure existed**: The process required 4-8 hour approvals, which meant genuine emergencies had no path to quick response other than "skip the process entirely."
- **No role-based access control on firewall**: Anyone with credentials could make changes. There was no segregation between monitoring access and change-making access.
- **Changes weren't tested before deployment**: David's rule should have been tested against simulated traffic in a test environment before going to production.
- **No real-time alerting for rule changes**: The security team found out about the change only after the outage, not when it was made.
- **DDoS detection was manual and unreliable**: David's observation of "unusual traffic" was subjective interpretation, not automated detection against known patterns.
- **No incident playbook for DDoS response**: If it had been a real attack, the company had no documented procedures for escalation, customer notification, or mitigation steps.
- **Historical changes were never audited**: A complete audit revealed that 47% of previous firewall changes had bypassed the CAB process, indicating systemic non-compliance.

## Key Takeaways

- **Change-advisory-board-cab must have an emergency path**: Define what "emergency" means (genuine active incident, automated detection + manual verification), then create a streamlined approval process (verbal + 4-hour rollback window + post-approval documentation).
- **Change-management must be enforced technically, not just by process**: Use [[infrastructure-as-code]] and role-based access so that non-approved changes are technically blocked or require MFA and explicit approval.
- **All configuration changes must be logged and alerted in real-time**: Implement integration between your configuration management system and your SIEM so that changes are visible immediately.
- **Non-emergency changes must be tested before production**: Use blue-green-deployment or a mirror test environment to validate changes impact.
- **DDoS detection must be automated, not manual**: Implement tools that automatically detect attack patterns and alert the team, rather than relying on subjective interpretation of dashboards.
- **Emergency procedures require definition and testing**: If you don't define emergency change processes, people will improvise and bypass the official process—then you have no control whatsoever.
- **Post-incident reviews must be blameless and thorough**: Blaming David would have missed the systemic failure: the process didn't account for emergencies and had no enforcement mechanism.

## Related Cases

- [[case-infrastructure-as-code]] — Using code to make infrastructure changes, with automated testing and version control
- [[case-incident-response]] — Building playbooks and procedures for different incident types (DDoS, security breach, etc.)
- [[case-defense-in-depth]] — How multiple protective layers (change approval, testing, monitoring, alerting) work together
