---
title: "Case: The Permission Sprawl — Authorization During SOC2 Audit"
description: "A SOC2 audit at an e-commerce platform discovers that 47% of IAM roles have excessive permissions inherited from a botched cloud migration two years prior. Compliance deadline is six weeks away."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

DynamoCart is a Series C e-commerce platform based in Seattle serving ~2 million monthly active users. The company employs 280 people across engineering, operations, customer service, finance, and executive teams. In 2024, DynamoCart migrated from a traditional on-premises data center to AWS to support rapid scaling. The migration was aggressive: 18 months compressed into 12 weeks to meet funding milestone deadlines. Security and authorization controls were deprioritized in favor of speed.

In January 2026, DynamoCart hired Deloitte to conduct a SOC2 Type II audit in preparation for enterprise customer contracts. The audit scope included evaluating access controls, authorization frameworks, and identity governance. Within the first week of audit fieldwork, the Deloitte auditor, Jennifer Chen, requested an urgent meeting with the Chief Information Security Officer, Marcus Wu. "I need to understand your AWS IAM role strategy," Jennifer said, opening her laptop to a spreadsheet. "We've identified 127 IAM roles in your AWS accounts. I need to understand the business justification for each one."

Marcus's stomach sank. He had inherited the AWS environment from the original DevOps team who had departed during the migration. There was no documentation of role design decisions. He asked his team to provide justification for each role. What they found was nightmarish:

Role "EC2-Instance-All-Access" had 89 users granted permission to it, including customer service representatives, finance staff, and contractors. Technically, this role could modify, stop, or delete any EC2 instance in the production environment. The business justification in the comments: "2024 migration—needed quick access."

Role "RDS-Full-Access" granted permission to modify, delete, and restore any AWS RDS database, including the production customer database. It was assigned to 34 users, including the entire DevOps team, all engineers, and three contractors. Nobody could articulate why customer service staff needed this role.

Role "S3-All-Buckets-Read" granted read access to 47 S3 buckets, including buckets containing customer PII, backup data, and configuration files with credentials. It was assigned to 156 users across all departments. When Jennifer asked why every employee needed to read every S3 bucket, the answer was a shrug: "It was easier to give everyone broad access during migration than to figure out specific bucket access per team."

Role "Secrets-Manager-Full-Access" granted permission to read every secret stored in AWS Secrets Manager, including database passwords, API keys, and signing certificates. It had 41 users. When Marcus asked who needed this, his team identified 12 users who clearly didn't (marketing staff, HR, administrative assistants) but had inherited the role during the migration.

The more Jennifer dug, the worse it got. She randomly selected 20 of the 127 roles and evaluated them against the principle of least privilege. Seventeen of them exceeded what the assigned users actually needed to perform their jobs.

Marcus was now facing a critical problem: Jennifer's preliminary finding was clear—"Authorization controls do not meet SOC2 requirements. The organization has not implemented the [[principle-of-least-privilege]]. Users are assigned broad permissions beyond what is required for their job functions."

Deloitte's proposed remediation scope: "Complete redesign of IAM roles with documented business justification for each role, restricted to the minimum permissions required for each job function."

Jennifer gave him six weeks to remediate, or the SOC2 audit would fail.

Marcus assembled a rapid response team. He brought in the Director of Cloud Operations (David Zhang), the security architect (Elena Torres), and a compliance manager. They worked backward from the audit deadline:

Week 1: Discovery and prioritization. Marcus ran an AWS IAM Access Analyzer against all 127 roles and generated a report of unused permissions. The analysis was shocking: 43% of assigned permissions had never been used. Roles granted "EC2:\*" (all EC2 actions) but the user only ever created instances. Roles granted write access to production databases but the user only read logs.

The team categorized roles into three groups:

- Group A (25 roles): Engineering roles that legitimately needed broad access (but still not "all EC2 actions")
- Group B (67 roles): Operational roles that should be narrowed significantly
- Group C (35 roles): Roles that could be completely eliminated and merged into existing roles

Week 2: Role redesign. For each role, the team:

1. Identified who was assigned to it
2. Interviewed those users about their actual job functions
3. Determined the minimum AWS actions required
4. Documented the business justification
5. Created a new, narrower role or retired the role entirely

For example, "EC2-Instance-All-Access" became:

- "Engineer-EC2-InstanceManagement" (create, start, stop, terminate instances in dev/staging; read in production)
- "DevOps-EC2-Production-OnCall" (emergency stop/terminate only, with mandatory MFA, logging, and approval workflow)
- "Infrastructure-Team-EC2-Management" (limited set of operations, no deletion without approval)

Week 3: Implementation. Elena used AWS CDK (Infrastructure as Code) to define every role with explicit permissions. Every line of code had a comment explaining the business justification. The code required code review and approval before deployment.

The most challenging work was building a governance model. Marcus implemented:

- **Role ownership**: Each role now had a documented owner (usually a team lead) responsible for quarterly review
- **User attestation**: Every user assigned to a role received a quarterly email asking "Do you still need this role? Confirm or it will be revoked."
- **Approval workflow**: Any new role or permission change required documented business justification and approval from the role owner AND the security team
- **Automated review**: AWS Config and custom Lambda functions monitored for roles with unused permissions and alerted the team

Week 4-5: Migration. The team systematically moved every user from old roles to new, narrower roles. They prepared a communication plan:

- Week 4 notification: "Your access is changing. Here's what you'll lose, here's what you'll keep, here's why."
- Week 5 cutover: Old roles were disabled; new roles were activated. Most users didn't notice because their actual access barely changed—they'd just been granted broad permissions they didn't use.
- Post-cutover monitoring: The team watched CloudTrail logs for permission denied errors that would indicate roles were too narrow. They discovered three cases where users needed slightly more access and refined the roles.

Week 6: Audit remediation. Jennifer returned for follow-up audit work. She sampled 25 of the new roles and verified that every permission was documented with business justification. She spot-checked access reviews to confirm the quarterly user attestation process was real. She approved the remediation work.

The final stats were compelling:

- 127 IAM roles consolidated to 42
- 89 unnecessary permissions revoked from users
- 100% of remaining roles had documented business justification
- Authorization matrix now auditable and maintainable

DynamoCart passed the SOC2 Type II audit with a "green" finding on access controls.

## What Went Right

- **Auditor identified the problem systematically**: Jennifer's role-by-role examination forced the team to justify every authorization decision.
- **Clear compliance deadline created urgency**: Six weeks focused the team's priorities and prevented indefinite deferral of the problem.
- **Infrastructure as Code captured role design**: Using AWS CDK meant every permission change was version controlled, approved, and documented.
- **Post-migration discipline was applied**: The team built governance (approval workflows, quarterly attestation, role ownership) that prevented permission sprawl in the future.
- **User impact was minimized**: Most users didn't notice the change because their actual work didn't require the broad permissions they'd been granted during migration.

## What Could Go Wrong

- **12-week migration timeline forced dangerous shortcuts**: The original migration prioritized speed over security, resulting in overly broad permissions granted as a temporary workaround that became permanent.
- **No role governance during migration**: There was no process requiring business justification for role design decisions. Roles were created ad-hoc as problems arose.
- **Permission creep went unnoticed for 18 months**: Nobody reviewed authorization regularly. Users accumulated permissions from role changes, and old permissions were never revoked.
- **No [[principle-of-least-privilege]] enforcement**: The default approach was "give them everything they might need" rather than "give them the minimum they actually need."
- **IAM roles lacked documentation**: Roles had cryptic names and no comments explaining business justification. This made auditing impossible.
- **No automated compliance tooling initially**: AWS IAM Access Analyzer could have been run weekly to identify unused permissions, but it wasn't configured until the audit prompted it.
- **User education was insufficient**: Many users with overly broad access didn't understand they had that access or why they didn't need it.

## Key Takeaways

- **Authorization must be built with least privilege as the default**: Start by identifying the minimum permissions needed, not the maximum that might be helpful.
- **Every role must have documented business justification**: Use Infrastructure as Code with comments, or maintain an authorization matrix. Undocumented roles are impossible to audit and impossible to remediate.
- **Role design must happen before production**: The migration should not have gone live with temporary, overly broad permissions. It's far harder to narrow permissions after the fact than to design them correctly initially.
- **Quarterly user attestation is essential**: Users should receive periodic confirmation that they still need their assigned roles. Lack of attestation creates unlimited permission drift.
- **IAM Access Analyzer and similar tools should run continuously**: Automated detection of unused permissions identifies roles that are too broad before audit finds them.
- **Segregation of duties requires explicit role design**: Some actions (like deleting production databases) should require approval workflows and MFA, not just role assignment.
- **Principle-of-least-privilege requires effort but pays dividends**: The investment in designing 42 well-justified roles is far cheaper than managing 127 roles, investigating permission sprawl, and failing compliance audits.

## Related Cases

- [[case-access-control-models]] — Understanding role-based access control and how to design roles properly
- [[case-privileged-access-management]] — Deep dive into high-risk roles (EC2 termination, RDS deletion, Secrets access) and how to control them
- [[case-identity-management]] — Automating user lifecycle management and access review processes
