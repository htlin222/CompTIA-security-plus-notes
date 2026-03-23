---
title: "Case: The Alert Fatigue Crisis — SIEM Ingestion Explodes"
description: "Splunk license costs tripled in a year because verbose debug logging from a Kubernetes cluster is ingesting 800 GB/day. The SOC is drowning in noise while the security budget is blown."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

DataFlow Analytics deployed a Kubernetes cluster in June to run their data processing platform. The cluster was configured with the standard ELK Stack (Elasticsearch, Logstash, Kibana) for log collection, but they also fed logs into Splunk for security correlation. The Kubernetes platform logged every API call, every pod startup/shutdown, every network connection, every volume mount—everything. By default, the logging was set to "debug" level, capturing every internal operation with full details.

By July, the security team noticed that their Splunk ingestion rate had jumped from 45 GB/day to 200 GB/day. By September, it had climbed to 800 GB/day. The Splunk licensing model charges based on ingest volume: 50 GB/day = $X per month; 100 GB/day = $2X per month; 1000 GB/day = $10X per month. DataFlow's annual Splunk bill, which had been $180,000 in the previous year, was now tracking toward $540,000—three times the previous cost.

The CIO immediately demanded an investigation. It didn't take long to identify the culprit: the Kubernetes cluster was logging approximately 50,000 events per second, totaling 800 GB/day of mostly redundant, low-value logs:
- Pod startup/shutdown events with full container metadata
- Network policy enforcement logs for every single network connection
- Persistent volume operations every time a pod accessed storage
- kubelet state synchronization messages
- etcd database audit logs with full request/response bodies
- controller manager reconciliation loops

The Kubernetes logs were technically valuable for **operational debugging** if there were a problem with the cluster. But for **security monitoring**, they were mostly noise. A pod starting up is not a security event. A persistent volume being accessed is not a security event. The volume of logs was overwhelming the Splunk pipeline.

The security team faced a dilemma: they could reduce the Splunk bill by filtering out the Kubernetes logs entirely, but then they would lose visibility into the cluster for security investigations. Or they could keep ingesting all 800 GB/day, but the budget would be unsustainable.

They chose a third path: implement [[log-aggregation]] filtering. They configured the Kubernetes cluster to ship logs to the ELK Stack for operational troubleshooting, but only send security-relevant logs to Splunk. The filtering rules they implemented:
- Pod startup/shutdown: send to ELK only (operational), not Splunk
- Network policy enforcement: send to Splunk only when policy enforcement **fails** (security event), not for successful connections
- Volume access: send to ELK only (operational), not Splunk
- kubelet state sync: send to ELK only (operational), not Splunk
- **etcd audit logs**: keep ALL of these in Splunk (security-critical; database changes are security events)
- **Container image pulls**: send to Splunk (image provenance is security-relevant)
- **RBAC authorization failures**: send to Splunk (access control violations are security events)

After implementing these filters, Splunk ingestion dropped from 800 GB/day to 120 GB/day—a 85% reduction. The annual Splunk bill dropped from the projected $540,000 back down to $220,000. The SOC team, no longer drowning in noise, could actually focus on the 120 GB/day of security-relevant events.

But the incident also revealed a deeper problem: the Kubernetes cluster had no [[normalization]] of events between the different log sources. An etcd audit log had a completely different format than a network policy log, which had a different format than a kubelet log. The SIEM's [[correlation-rules]] couldn't effectively correlate events because they came in inconsistent formats.

The team implemented [[log-aggregation]] with event normalization: all Kubernetes logs were normalized to a common schema (timestamp, event_type, source_system, action, actor, resource, result). This made the [[correlation-rules]] much more effective. Rules that previously required 5-6 different event formats could now be written once and applied universally.

## What Went Right

- **Log filtering based on security relevance**: Distinguishing between operational logs (valuable for troubleshooting but not security-relevant) and security logs (critical for correlation) reduced noise while preserving visibility.
- **[[Log-aggregation]] with [[normalization]]**: Feeding all logs through a [[normalization]] process made correlation more effective and reduced the complexity of [[correlation-rules]].
- **Budget-driven analysis**: The Splunk licensing cost overrun forced a serious conversation about log value, which led to better filtering practices.
- **Preservation of operational logging**: By routing operational logs to the ELK Stack, the team maintained operational visibility for debugging Kubernetes problems without paying for Splunk ingestion.

## What Could Go Wrong

- **No baseline logging configuration**: Kubernetes defaulted to "debug" level logging. A security-focused base configuration would have started with a lower logging level and only enabled specific security-relevant events.
- **Lack of [[log-management]] governance**: Nobody reviewed the Kubernetes logging configuration against the security policy. A quarterly audit would have caught the misconfiguration quickly.
- **Poor [[log-sources]] design**: Each log source (Kubernetes, application servers, databases) should have been designed with both operational and security requirements in mind, not just operational needs.
- **No [[log-integrity]] validation**: There was no mechanism to validate that logs arriving in Splunk were actually security-relevant and not just noise that passed the filter.

## Key Takeaways

- **Distinguish operational logs from security logs**: Not all verbose operational logging is security-relevant. Implement [[log-aggregation]] filtering that routes operational logs to operational systems and security logs to the [[siem]] to reduce noise.
- **[[Normalization]] is essential for [[correlation-rules]]**: When logs from different sources (Kubernetes, applications, databases, firewalls) are normalized to a common schema, correlation is dramatically more effective. Invest in a normalization layer.
- **[[Real-time-alerting]] requires low false positive rates**: If 99% of alerts are false positives, the SOC team becomes desensitized and misses real incidents. Better filtering upstream reduces alert fatigue more effectively than post-alert correlation.
- **[[Retention-and-archival]] can be stratified by relevance**: Security-critical logs (etcd, RBAC failures) can be retained longer and ingested into expensive SIEM systems. Operational logs can be retained in cheaper storage (ELK, S3) for longer periods.
- **Document and enforce [[log-sources]] configuration**: Each system that generates logs should have documented logging requirements for both operational and security purposes. Security logs should be a deliberate configuration, not an accidental side effect.
- **Implement [[log-management]] budget controls**: Use licensing models (like Splunk's per-GB model) to create accountability for log volume. Budget overruns force conversations about value and filtering.

## Related Cases

- [[case-log-management]] — Log management includes decisions about which logs to collect, how long to retain them, and how to organize them by relevance.
- [[case-soar]] — A SOAR platform can orchestrate [[correlation-rules]] across the [[siem]] to detect multi-step attacks. If the SIEM is drowning in noise, SOAR orchestration won't help.
- [[case-incident-response]] — During incident response, having clean security logs (without operational noise) enables investigators to focus on the attack chain rather than digging through thousands of benign events.
