---
title: "Case: The Silent Alterations — When Integrity Fails in Healthcare"
description: "A ransomware variant silently modifies patient lab results instead of encrypting them. The integrity breach goes undetected for 72 hours at a hospital system. By the time discovery happens, 847 patients have received potentially incorrect medical guidance based on falsified data."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

Metropolitan Hospital System is a 12-hospital network in the Upper Midwest serving approximately 1.2 million patients per year. The system's Lab Information System (LIS) maintains critical patient lab results: blood work, urinalysis, drug screens, pathology reports. On a Wednesday morning in February 2026, a pathology resident named Dr. Patel was reviewing lab results for one of his patients when something seemed off. A hemoglobin level from Tuesday's blood work showed 7.8 g/dL—dangerously low, suggesting severe anemia. The patient hadn't reported any symptoms. Dr. Patel called the lab to confirm the result.

The lab technician, Rachel Kim, checked the system. "That's strange," she said. "The sample came in at 12.4 g/dL, which is normal. Something's wrong with the system record."

Rachel pulled up the lab result audit trail. The record showed: sample collected at 08:34 AM, initial result 12.4 g/dL, then at 11:47 PM—13 hours later—the result had been modified to 7.8 g/dL by a user account called "maintenance_service."

Rachel flagged this to her supervisor, who immediately contacted the hospital's Chief Information Security Officer, Marcus Johnson. By 2:45 PM, Marcus was running a forensic investigation. He quickly discovered that the "maintenance_service" account had no legitimate business purpose. The account had been used to modify 847 lab results across the system—blood work, urinalysis, pathology reports, drug screens—all with seemingly random alterations. A hemoglobin level of 14.2 had been changed to 8.1. A glucose reading of 110 had been changed to 245. A creatinine level had been altered in ways that didn't make medical sense.

The scariest discovery: 203 of these altered results had already been reviewed by clinicians and acted upon. Patients had received medical advice based on false data. One elderly patient with an artificially elevated potassium level had been prescribed medication to lower it, medication that could have been dangerous if his potassium was actually normal.

Marcus's first action was to shut down the LIS system and alert the hospital's Incident Command Center. This was a medical emergency. The second action was to determine the scope: how many records were affected, which ones had been acted upon, and which patients might be in danger.

As the investigation unfolded, Marcus discovered that this wasn't a typical ransomware attack. The attacker hadn't encrypted the LIS database—that would have been immediately obvious to hospital staff. Instead, they had deployed a sophisticated piece of malware that silently modified lab results while leaving the [[availability]] of the system completely intact. The hospital's backup systems had also been compromised: the attacker had modified the backup copies of the database to include the same false results. If the hospital had tried to restore from backup, they would have restored the corrupted data.

The attack violated all three pillars of the [[cia-triad]]:

**Confidentiality**: The attacker had accessed patient health information (lab results). This was a HIPAA violation affecting 847 patients.

**Integrity**: The attacker had modified patient lab results, fundamentally compromising the trustworthiness of the data. Medical staff couldn't be certain which results were accurate and which were falsified.

**Availability**: The system was technically available (it responded to queries), but the data was unreliable. For medical purposes, unreliable data is as bad as no data—it's more dangerous, actually, because clinicians might act on it thinking it's accurate.

The [[dad-triad]] (an inverse perspective on CIA) was also relevant here:

**Disclosure** had occurred (patient records were visible to the attacker).

**Alteration** had occurred (results were systematically modified).

**Denial** of availability was prevented by the attacker's choice not to encrypt—they wanted the data to be used, just incorrectly.

Marcus convened the hospital's crisis team. The questions were immediately urgent:

1. Which lab results were actually incorrect? (Answer: don't know yet; every result from the affected time period is suspect)
2. Which patients need to be contacted and advised that their results might be wrong? (Answer: at least 847)
3. Which patients already received medical treatment based on false results? (Answer: 203, but we're still investigating)
4. Which patients might be at risk if they don't get corrected results? (Answer: unknown)

The hospital's medical director, Dr. Sarah Chen, made a difficult decision: they would notify all 847 patients whose results had been modified. The notification would explain that some results might have been falsified and that they should contact their physician for re-testing. This notification would likely cause panic and might trigger thousands of phone calls to the hospital's already-overwhelmed call center.

By Thursday evening (72 hours after initial discovery), the hospital had:

1. Shut down the LIS and conducted forensics to determine exactly which modifications were made
2. Restored the database from backup tapes that had been physically isolated from the network (stored offline, not accessible to the malware)
3. Re-run all lab work from specimens that were still available in the lab (most blood samples remain viable for 1-2 weeks)
4. Began notifying patients and physicians

The forensic investigation revealed that the attacker had gained access through a vulnerable VPN appliance that had been patched in the security advisory but not yet updated due to a missed maintenance window. From the VPN, they'd moved laterally to the LIS database server and installed the data modification malware.

The hospital's backup procedures saved them from complete disaster: the backup tapes that were physically isolated still contained clean data. However, the malware had been active for 72 hours before discovery—a long window for spreading to multiple systems.

The incident highlighted a critical gap in the hospital's approach to the [[cia-triad]]: they had focused heavily on [[availability]] (keeping the hospital running, no downtime allowed) and somewhat on [[confidentiality]] (HIPAA compliance, encryption at rest). But [[integrity]] assurance was weak. There was no system that independently verified lab results, no checksums or digital signatures on data, no separation of duties (the maintenance_service account shouldn't have had the ability to modify historical results). There were no alerts when large-scale result modifications occurred.

## What Went Right

- **Lab technician noticed the anomaly**: Dr. Patel's clinical suspicion (the result didn't make sense for the patient) led him to verify with the lab. This human verification caught the attack.
- **Audit trail existed**: The LIS system logged who modified which records and when. This made the scope of the compromise determinable.
- **Offline backup existed**: The hospital's oldest backup tapes had been physically isolated from the network, preventing the malware from corrupting them. This allowed recovery of clean data.
- **Incident response was swift**: Once the anomaly was discovered, the hospital escalated immediately and shut down the compromised system within hours.
- **Forensic analysis was thorough**: The investigation determined exactly which records were modified, allowing targeted patient notification rather than system-wide panic.

## What Could Go Wrong

- **No [[integrity]] verification mechanism**: The system had no checksums, digital signatures, or independent verification of lab results. Modifications went undetected until a clinician questioned a specific result.
- **Backup systems were also compromised**: The primary and backup copies of the database were both modified. If the hospital's offline backups hadn't existed, they would have had no clean data to restore.
- **Maintenance account had excessive permissions**: A generic "maintenance_service" account had the ability to read and modify any lab result. This account should have been removed or restricted to actual maintenance operations.
- **No real-time alerting on bulk data modifications**: The system didn't alert when a single account modified 847 records in one session. A rule like "alert if any account modifies >10 records in one hour" would have caught this within minutes.
- **Backup was restored immediately without verification**: The hospital's initial impulse was to restore from backup. If they'd done so without checking offline backups first, they would have restored corrupted data.
- **No air-gapping of critical systems**: The LIS should have been on a network segment that couldn't be accessed from the general hospital network. The attacker shouldn't have been able to reach it after compromising the VPN.
- **Vulnerable VPN appliance hadn't been patched**: A known vulnerability existed; the patch was available; the hospital just hadn't scheduled the update.

## Key Takeaways

- **The [[cia-triad]] requires equal protection of all three pillars**: The hospital had focused on availability and confidentiality but neglected integrity verification. Integrity is just as critical—falsified medical data is more dangerous than unavailable data.
- **Integrity assurance requires active verification, not just trusted systems**: Implement digital signatures, checksums, or independent verification of critical data. Database log files aren't enough—you need mechanisms that would detect if someone modifies the log files too.
- **Backup systems must be isolated and verified**: Backups should be offline or in separate network segments to prevent malware from compromising both primary and backup copies. Backups should be tested regularly to ensure they can be restored cleanly.
- **Separation of duties applies to maintenance accounts**: Even "maintenance_service" accounts should have restricted permissions. A maintenance account might need to run specific commands or scripts but shouldn't have blanket database modification permissions.
- **Real-time alerting should detect bulk modifications**: Rules like "flag any account that modifies >N records in M minutes" or "alert on unusual patterns in medical data modifications" would have caught this attack within minutes instead of 72 hours.
- **Critical systems need network segmentation**: The LIS shouldn't be accessible from the general hospital network. It should be on an isolated VLAN with strict firewall rules allowing only specific, approved connections.
- **The [[dad-triad]] is sometimes more intuitive than CIA**: Understanding disclosure, alteration, and denial can sometimes make it clearer why data modification is a critical security concern.

## Related Cases

- [[case-encryption]] — Encryption in transit and at rest protects confidentiality, but not integrity if an attacker has the encryption keys
- [[case-resilience-and-redundancy]] — Designing backup and recovery systems that can withstand attacks that target both primary and backup systems
- [[case-defense-in-depth]] — How network segmentation, backup isolation, and integrity verification work together to protect all three CIA pillars
