---
title: "Case: The VM Sprawl Vulnerability — 300 Unaccounted Machines During Hypervisor Patch"
description: "VM sprawl at a managed hosting provider has reached 2,400 virtual machines across 80 ESXi hosts, with 300+ VMs unaccounted for in the asset inventory. A hypervisor vulnerability advisory drops, and nobody knows the blast radius. Patching is risky without knowing what's running."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

TierOne Hosting is a managed service provider operating a VMware ESXi virtualized infrastructure hosting customer workloads. Their environment includes:

- 80 ESXi 6.7 hypervisor hosts (deployed over the past 8 years)
- 2,400 virtual machines across customer accounts
- 60+ physical locations nationwide
- Customers ranging from one-person startups to medium-sized enterprises

In January 2025, VMware released a critical security advisory: **CVE-2025-0001**, a remote code execution vulnerability in ESXi affecting all versions 6.0 through 7.0. The CVSS score was 9.1 (critical). The patch required a hypervisor reboot, which meant brief downtime for all VMs on affected hosts.

The infrastructure team, led by Operations Director Michael Chang, began planning the patch. The standard procedure would be:

1. Select a host with VMs running customer workloads
2. Notify customers of upcoming maintenance
3. Migrate all VMs from that host to unaffected hosts (using vMotion, a live migration feature)
4. Apply the patch to the host
5. Reboot the host
6. Once the host is patched, migrate VMs back to balance load

The problem: Michael's team couldn't account for 300+ virtual machines.

The CMDB (Configuration Management Database) showed 2,100 registered VMs. But when Michael's team queried the hypervisors directly, they counted 2,427 VMs. 327 VMs were missing from the inventory system.

Where did they come from?

**Investigation Results:**

- **Test environments created and forgotten**: Teams would provision VMs for testing, then abandon them. The VMs kept running, but nobody tracked them.
- **Orphaned backup VMs**: When customers migrated workloads, their old VMs were sometimes left running as "backups," but never formally handed over to the customer or decommissioned.
- **Illegal guest VMs**: A few customers had provisioned additional VMs beyond their contracted allotment, running them on the shared infrastructure without proper approval or billing.
- **Misconfigured billing systems**: 23 VMs were registered to customer accounts that had been closed 18 months ago. The VMs were still running, consuming resources, but the customer was no longer being billed.

With 327 unknown VMs, Michael couldn't confidently say which hypervisors were safe to patch. Those unknown VMs might belong to critical customer production systems. Patching a host and rebooting it without confirming all workloads could migrate would cause outages.

Michael escalated to Chief Information Officer Dr. Sarah Thompson. The decision was made: **before patching any hyperviso, we must identify and properly account for all 327 orphaned VMs**.

This triggered an emergency operational initiative:

**Phase 1: VM Identification (3 days)**
- Queried all 80 hypervisors for complete VM lists
- Compared against the CMDB to identify orphaned VMs
- Located 327 untracked VMs and began investigating ownership

**Phase 2: Contact and Assessment (1 week)**
- Contacted all customer accounts asking "do you own these VMs?"
- For VMs whose owners couldn't be identified: checked billing records, email threads, provisioning dates
- Discovered that 142 VMs belonged to customers but were never properly handed over to them
- Found 85 test VMs that should be deleted
- Found 47 VMs running on customer accounts that hadn't authorized them (unauthorized use)
- Found 23 VMs for closed customer accounts (billing orphans)
- Found 30 VMs that were completely unknown—nobody could identify them

**Phase 3: Remediation (2 weeks)**
- Contacted 142 customers: "We have VMs that appear to be yours. Confirm ownership or we'll delete them."
- Decommissioned 85 test VMs
- Shut down 47 unauthorized VMs and billed the customer accounts for the resource usage
- Decommissioned 23 billing orphans
- Created a security incident ticket for the 30 completely unidentifiable VMs (potential unauthorized access)
- Added all identified VMs to the CMDB

**Phase 4: VM Sprawl Prevention (Ongoing)**
- Implemented a VM lifecycle management policy:
  - VMs must be created through a request system (no direct provisioning)
  - VMs have an owner and an expiration date
  - VMs older than 90 days without recent use are flagged for review
  - Monthly audit comparing CMDB against hypervisor reality
  - Automated alerts for new VMs created outside the provisioning system

**Phase 5: Hypervisor Patching (After sprawl cleanup)**
- With the sprawl identified and remediated, Michael's team had confidence in the patch plan
- Executed phased patching of all 80 hypervisors
- Completed within two weeks without customer impact or downtime

### Impact Assessment

The VM sprawl had hidden costs:

- **Resource overconsumption**: 327 extra VMs were consuming CPU, RAM, and storage that wasn't being paid for. Estimated waste: $47,000/month
- **Unpatched systems**: The 30 unidentified VMs had been running without documented ownership or patch management. They were potential entry points for attackers
- **Compliance risk**: Some of those VMs might be handling customer data without proper security controls, incident response plans, or audit logs
- **Legal liability**: The 47 unauthorized VMs on customer accounts could have created contractual disputes if a security incident occurred

## What Went Right

- **VM sprawl was discovered before a major hypervisor vulnerability**: If the critical CVE hadn't forced an inventory audit, the sprawl would have continued indefinitely.
- **Proper [[live-migration-security|migration]] procedures prevented forced downtime**: Using vMotion to live-migrate VMs allowed patching without interrupting customer services.
- **Systematic remediation prevented data loss**: Rather than deleting unknown VMs immediately, the team investigated ownership and communicated with customers.
- **Preventive controls were implemented**: The ongoing VM lifecycle management policy will catch future sprawl before it becomes a problem.

## What Could Go Wrong

- **If the CVE advisory hadn't forced the audit**: Sprawl would have continued growing at 50-100 new untracked VMs per year.
- **If a critical infrastructure hypervisor had been patched without identifying sprawled VMs**: A forced reboot could have caused unplanned downtime for customers, potentially triggering SLA violations and refunds.
- **If 30 unidentified VMs had been compromised**: Attackers could have had persistent access to the infrastructure for months without being detected.
- **If [[snapshot-management|snapshots]] of those VMs had been retained**: Data loss, compliance violations, and storage waste would have continued indefinitely.
- **If [[hardening-the-hypervisor|hypervisor hardening]] hadn't been applied**: The untracked VMs could have been used as pivoting points for attacks against the hypervisor or other VMs.

## Key Takeaways

- **VM sprawl is the hypervisor equivalent of configuration drift**: Without systematic inventory management, VMs accumulate silently. Implement CMDB syncing with hypervisors to detect divergence.
- **VM lifecycle management must be enforced**: VMs should have owners, expiration dates, and regular review intervals. Automate deprecation warnings and decommissioning.
- **VM isolation requires understanding what's running**: You can't apply security policies to VMs you don't know exist. Inventory is foundational.
- **VM-escape and [[vm-isolation|escape attacks]] create blast radius risk**: Unknown VMs could be compromised without anyone knowing, providing a foothold for further attacks.
- **Snapshots must be cleaned up**: VM snapshots consume storage and can cause data inconsistency if older snapshots are reverted accidentally. Enforce a retention policy.
- **Resource-contention from sprawl wastes money**: Hundreds of VMs consuming resources without being billed represents financial loss. Regular inventory audits catch this waste.
- **Critical hypervisor patches should force an audit**: Security advisories are opportunities to check the health of your environment. Use patching as a checkpoint for inventory accuracy.

## Related Cases

- [[case-cloud-security]] — Similar sprawl patterns occur in cloud environments with EC2 instances or other resources
- [[case-hardening]] — Hardening the hypervisor itself to prevent [[vm-escape|VM escape attacks]]
- [[case-network-segmentation]] — Segmenting VMs by criticality and customer to contain blast radius

