---
title: "Case: Building Security From Scratch — When There Are No Baselines"
description: "A new CISO at a 500-person SaaS company discovers there's no documentation of security principles, risk management processes, or control baselines. She has 72 hours to create a foundational briefing for the entire engineering department."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

Velocity Analytics is a Series C SaaS company (founded 2019, ~$15M ARR) that provides real-time business intelligence dashboards for mid-market retailers. The company has 480 employees: 180 in engineering, 120 in sales/success, 80 in operations/finance, and 100 across other functions. In February 2026, the CEO, Rachel Morgan, hired a new Chief Information Security Officer, Dr. Amara Okonkwo, with a mandate to "build the security program from scratch."

Amara's first week was spent reviewing existing security documentation. What she found was alarming in its absence: there was no documented security policy, no defined security principles, no risk management process, no control baselines. Engineering team members had developed their own approaches to security—some teams were cautious about credentials in code, others had passwords in plaintext in configuration files. The company had implemented AWS security groups inconsistently. Some databases had encryption at rest enabled; others didn't. There was no centralized security team—security issues were handled ad-hoc by various engineers who happened to care about security.

In her initial all-hands address, Rachel asked Amara, "When can you give the engineering team a comprehensive security briefing?" Amara responded, "Two weeks to do it right." Rachel said, "You have 72 hours."

Amara's first decision was to understand what security even meant in the context of Velocity Analytics. She scheduled conversations with 15 key stakeholders: the VP of Engineering, product managers, ops leads, data engineers. Her questions were simple:

- "What does security mean to you?"
- "What are your biggest security concerns?"
- "What are your biggest security challenges?"
- "What would make your job easier from a security perspective?"

From these conversations, Amara learned:

- **Engineers viewed security as a compliance checkbox**, not as a core responsibility. "Security holds us back" was a common refrain.
- **The VP of Engineering was terrified of data breaches** because a competitor had suffered a breach two years prior that damaged customer trust.
- **Product managers had no visibility into security risks in their products**. New features were shipped without security review.
- **Operations staff were handling credentials manually** (passwords in emails, SSH keys in shared drives), and they knew it was wrong but didn't know what the right process was.
- **Nobody could articulate what "defense in depth" meant or how it applied to Velocity's systems**.

Amara realized that before she could build security controls, she needed to establish a common language and shared understanding of foundational security concepts.

She built a 2-hour engineering briefing covering:

**Part 1: Why Security Matters (30 minutes)**

- The [[cia-triad]]: Confidentiality, Integrity, Availability. How each one matters for Velocity's business.
  - Confidentiality: Customer data breaches destroy trust and violate contracts
  - Integrity: Falsified business intelligence dashboards make customers' decisions wrong
  - Availability: Down dashboards mean lost revenue and angry customers
- Real examples from Velocity's business:
  - If customer data was breached, Velocity would lose the customer (cost: $X)
  - If dashboards showed wrong numbers, customers would make bad business decisions (cost: lawsuit)
  - If dashboards were down for a day, retail customers would lose sales (cost: negative NPS, churn)

**Part 2: The Principle of Least Privilege (20 minutes)**

- Every engineer, every service, every database access should be limited to the minimum required for their job
- Real examples:
  - A junior data engineer shouldn't have access to production database admin functions
  - A Lambda function should only have permissions to read from one S3 bucket, not all buckets
  - A third-party integration shouldn't have access to customer PII, only aggregated data

**Part 3: Defense in Depth (20 minutes)**

- Security isn't one big wall; it's multiple layers. Each layer might fail, but if designed right, an attacker has to breach multiple independent layers.
- Real examples at Velocity:
  - Layer 1 (perimeter): VPN with MFA to access internal systems
  - Layer 2 (network): Network segments so databases aren't accessible from web servers
  - Layer 3 (identity): IAM roles limit what services can do
  - Layer 4 (application): CORS policies, authentication checks, input validation
  - Layer 5 (data): Encryption at rest and in transit
  - If an attacker breaches the perimeter, the other layers still protect data

**Part 4: Authentication vs. Authorization (15 minutes)**

- Authentication: proving who you are (your identity)
- Authorization: proving what you're allowed to do (your permissions)
- Both must work for systems to be secure
- Real examples:
  - You authenticate to AWS (who are you?), then authorization determines which resources you can access
  - You authenticate to GitHub (you're amara@velocityanalytics.com), then authorization determines which repos you can access

**Part 5: Security Risk Assessment (15 minutes)**

- Every system has risks. Security is about identifying risks and deciding whether to accept them, mitigate them, or avoid them.
- Risk = Likelihood × Impact
- Real examples at Velocity:
  - Database unencrypted: Likelihood=medium (attackers target databases), Impact=catastrophic (all customer data). Risk=high. Decision: Must encrypt.
  - Development environment with production-like data: Likelihood=low (dev environments aren't usually targeted), Impact=moderate (if breached, production data is exposed). Risk=medium. Decision: Use anonymized test data instead.
  - Production database without automated backups: Likelihood=medium (hardware fails, malware encrypts), Impact=catastrophic (business cannot recover). Risk=high. Decision: Implement automated backups.

**Part 6: Practical Security for Engineers (20 minutes)**

- Concrete, actionable guidance:
  - Never commit credentials (passwords, API keys, SSH keys) to version control. Use environment variables or secret management systems.
  - Use MFA for all external-facing systems (GitHub, AWS, production databases)
  - Request minimum IAM permissions required for your role, not maximum possible
  - When in doubt, ask the security team. No question is dumb.
  - Report suspicious activity immediately (unusual login, permission changes, unexpected costs)

During the briefing, Amara presented a diagram showing Velocity's data flow and security risks:

1. Customer data flows through the web application
2. Data is stored in a PostgreSQL database
3. Data is transformed by batch data processing jobs
4. Data is served through dashboards

For each component, she mapped it to the [[cia-triad]]:

- Web app needs [[confidentiality]] (data in transit encrypted with TLS), [[integrity]] (data isn't modified), [[availability]] (responds quickly)
- Database needs [[confidentiality]] (encryption at rest), [[integrity]] (no unauthorized modifications), [[availability]] (backed up and recoverable)
- Batch jobs need [[confidentiality]] (no leaking data), [[integrity]] (calculations are correct), [[availability]] (run on schedule)
- Dashboards need [[confidentiality]] (user can only see their data), [[integrity]] (displays correct numbers), [[availability]] (accessible 24/7)

The briefing's impact was immediate. After the session, the VP of Engineering told Amara, "I finally understand why you're asking us to do all this security stuff. It's not theoretical—it directly protects our business."

Within a week, Amara had established a set of foundational security concepts that the entire company could reference:

1. **The [[cia-triad]]** as the framework for evaluating what needs protecting
2. **Principle-of-least-privilege** as the guideline for access control
3. **Defense-in-depth** as the architecture principle
4. **Risk-assessment** as the decision-making framework for security investments
5. **Practical guidance** for engineers on the top 5 things to avoid

These became the foundation for all future security work at Velocity.

## What Went Right

- **CEO created urgency without micromanaging**: The 72-hour deadline forced Amara to focus on essentials, not getting bogged down in details.
- **Stakeholder interviews revealed the true concerns**: Instead of assuming what security mattered, Amara asked people directly.
- **Briefing was grounded in business context**: Rather than abstract security principles, Amara connected every concept to Velocity's business (revenue impact, customer trust, product accuracy).
- **Briefing was practical and actionable**: Engineers left with specific things they could do (don't commit credentials, use MFA, request minimum permissions).
- **The [[cia-triad]] provided a common language**: Having a shared framework (Confidentiality, Integrity, Availability) made it easy for engineers to evaluate security in their own systems.

## What Could Go Wrong

- **No existing security documentation**: Velocity had built a company to $15M ARR with no documented security principles, making the task of starting from scratch daunting.
- **Security viewed as a blocker, not an enabler**: Engineers had experienced security as "slowing them down," making them skeptical of security efforts.
- **No security team existed**: All security decisions were ad-hoc, made by different people using different frameworks.
- **Inconsistent security practices**: Some teams encrypted databases; others didn't. Some used environment variables for secrets; others hardcoded them. This inconsistency meant the company's overall security posture was very weak.
- **No risk management process**: Security investments weren't driven by risk; they were driven by whoever complained loudest.
- **The brief timeframe could have resulted in a superficial presentation**: 72 hours is not much time, so the focus had to be on essentials, not comprehensive.

## Key Takeaways

- **Foundational security concepts must be established before building specific controls**: Without a shared understanding of [[cia-triad]], [[principle-of-least-privilege]], and [[defense-in-depth]], different teams will implement security inconsistently.
- **Security principles must be grounded in business context**: Explain why security matters in terms the business understands (revenue impact, customer trust, competitive advantage, legal risk).
- **A risk assessment framework helps prioritize security work**: Using Likelihood × Impact helps determine which risks to address first.
- **Practical guidance beats theoretical frameworks**: Engineers need to know "don't commit credentials" and "use MFA" more than they need to understand the formal definition of [[authentication]].
- **Security concepts should be simple enough to fit on a page**: If you can't explain it briefly, people won't remember it or apply it in their daily work.
- **One good briefing can establish baseline understanding across an entire organization**: Rather than having each team learn security separately, teaching everyone the same foundational concepts creates a shared language.

## Related Cases

- [[case-cia-triad]] — Deep dive into protecting confidentiality, integrity, and availability in real systems
- [[case-defense-in-depth]] — Understanding how to layer controls and make systems resilient to individual failures
- [[case-risk-management]] — Building a framework for assessing and prioritizing security risks across the organization
