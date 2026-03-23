---
title: "Case: The Forgotten Shared Password — Credential Rotation Failure"
description: "A database administrator at a credit union has been using a shared root password for three years that is also hardcoded in 14 cron jobs. He's leaving the company Friday and nobody realizes this until his resignation email."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

Metro Credit Union operates with 300 employees across 4 branches, serving 85,000 members in the Midwest. Their entire member database, transaction history, and loan portfolio runs on a PostgreSQL database server. The root account for that database—the most privileged credential—had a password: "Credit1234". The password had been created three years ago by the previous database administrator and had been passed down verbally to the current DBA, Marcus, when he was hired.

Marcus never changed it. Nobody suggested he change it. Marcus simply used "Credit1234" to log in whenever he needed to perform administrative tasks on the database.

But there was a bigger problem: that password was hardcoded in 14 different locations in the environment:
- 8 cron jobs that performed automated backups and maintenance tasks
- 3 custom applications that connected to the database for reporting
- 2 monitoring scripts that collected performance metrics
- 1 disaster recovery failover script

On Thursday at 3:47 PM, Marcus sent his resignation email to HR: "I'll be leaving Metro Credit Union effective end of business Friday. I'll transition my responsibilities to the team." Nobody in IT was copied. Nobody in IT knew that the most critical database in the organization had just entered "orphaned credential" status.

On Friday morning, the CIO received a meeting request from HR: "Exit interview and asset return for Marcus." That's when it occurred to them that Marcus was the sole person with direct knowledge of the database root password. When asked if the database had a documented root password change procedure, the security team went silent. They didn't have one.

The investigation revealed:
1. **Shared credentials**: The password was shared verbally with no documentation
2. **Hardcoded in cron jobs**: 8 automated backup and maintenance jobs would break immediately if the password were changed
3. **Undocumented [[service-account-management]]**: The 3 applications that used the database credentials were supposed to use a service account, not root, but nobody had ever implemented this
4. **No [[credential-rotation]]**: The password hadn't been rotated in three years despite being the most critical credential in the organization
5. **No [[just-in-time-jit-access]]**: Marcus had permanent access to the root account. There was no time-limited or audited credential issuance mechanism

The CIO ordered an emergency action: change the database root password immediately. But when the team tried to make the change, they realized they needed to:
1. Update all 14 hardcoded password references
2. Test the backup scripts to ensure they still worked
3. Test the custom applications to ensure they still connected
4. Coordinate with the DR team to update the failover script
5. Notify anyone who might need to manually access the database

This couldn't be done in parallel—it had to be done carefully, with each system tested before the next was updated. The process took 6 hours of database maintenance downtime, during which the credit union couldn't process transactions (all systems that needed the database were blocked).

The financial impact: The credit union processes approximately 8,000 transactions per day. With $250 average transaction value, the outage cost the credit union roughly $2 million in lost transaction processing for those 6 hours. Additionally, customers who tried to access ATMs or online banking received error messages, damaging the organization's reputation.

## What Went Right

- **The oversight was discovered before it became a security breach**: Marcus hadn't used his access maliciously, and the password change was executed (albeit with downtime) before a threat actor could exploit it.
- **The incident forced a security review**: The credit union immediately implemented a [[privileged-access-management]] system with credential vaulting and [[session-recording]].
- **Documentation was created**: The organization created a complete inventory of where the database credentials were used, enabling a systematic update process.

## What Could Go Wrong

- **No [[credential-rotation]] schedule**: The password hadn't been rotated in three years. A policy requiring quarterly rotation would have prevented the hardcoded references from persisting.
- **Shared credentials instead of [[service-account-management]]**: Each application should have had its own service account with limited privileges (e.g., read-only to specific tables), not shared root access.
- **No offboarding process for database credentials**: When an employee left, nobody verified that their privileged credentials had been rotated or their access revoked.
- **No [[break-glass-accounts]]**: There should have been an emergency admin account separate from the day-to-day DBA account, with a different password, in case Marcus's account needed to be revoked immediately.
- **No [[session-recording]]**: If database access had been recorded, the organization would have had visibility into everything Marcus did with those credentials (though this wouldn't have prevented the hardcoding problem).
- **No monitoring for privileged action patterns**: If the system had been monitoring database access, it would have detected that the database root credentials were being used from multiple servers simultaneously (the cron jobs), which is unusual for a human user.

## Key Takeaways

- **[[Credential-rotation]] must be enforced on a schedule**: The database root password should be rotated quarterly at minimum. Rotating the password forces a systematic update of all locations where it's hardcoded.
- **[[Service-account-management]] eliminates shared credentials**: Every application that needs database access should have its own service account with minimal necessary privileges. The root account should almost never be used outside of emergencies.
- **[[Just-in-time-jit-access]] prevents permanent credential exposure**: Instead of permanently holding the database root password, privileged users should request temporary access (30 minutes, 1 hour) for specific tasks. This prevents long-term credential compromise.
- **[[Password-vaulting]] enables credential rotation without downtime**: A privileged access management system can automatically rotate the database password, update all hardcoded references, and test the changes before placing them in production.
- **Offboarding procedures must include credential revocation**: When an employee leaves, all privileged credentials must be rotated immediately, not at their next scheduled rotation date.
- **[[Break-glass-accounts]] provide emergency access**: Maintain a separate, high-security root account that can be used only for emergencies, with a different password stored in a physical vault. This prevents a single employee from being a single point of failure.

## Related Cases

- [[case-identity-management]] — Identity lifecycle management must include offboarding processes that revoke all privileged credentials.
- [[case-log-management]] — All database access, especially by privileged accounts, should be logged with full [[session-recording]] to enable forensic investigation.
- [[case-hardening]] — The database server should be configured to reject logins from certain IP addresses or networks, limiting the attack surface even if root credentials are compromised.
