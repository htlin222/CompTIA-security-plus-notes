---
title: "Case: The Acquisition Privilege Explosion — SAML Trust Misconfiguration"
description: "A SAML misconfiguration in a federated trust between a parent company and newly acquired subsidiary allows any user in the subsidiary to assume admin roles in the parent's AWS accounts. The trust was rushed through in a week."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

GlobalTech Corporation acquired FinanceCore Inc., a 600-person finance operations company, for $340 million in January. The integration timeline was aggressive: close the deal by January 15th, integrate identity systems by February 1st, merge environments by March 1st. The identity team at GlobalTech, understaffed and under pressure, decided to establish a [[federation]] trust between GlobalTech's Azure AD and FinanceCore's Okta identity provider using [[saml-security-assertion-markup-language]].

On February 1st at 3:47 PM, an Azure AD administrator named Rick Politz configured the [[service-provider-sp]] side of the SAML trust. He created a SAML application in Azure AD that accepted assertions from FinanceCore's Okta [[identity-provider-idp]]. To speed the process, he used a SAML configuration template that came with a default [[attribute-mapping]]: any Azure AD group named "Finance-Team" would be automatically mapped to users with the role "Owner" in Azure AD and AWS accounts. Rick deployed this configuration with "p=reject" for unmatched users, thinking he was being cautious.

What Rick didn't realize was that FinanceCore's Okta administrator was working from the opposite assumption. In Okta, she created a group called "Finance-Team" and added 600 users to it—literally all employees of FinanceCore, from interns to the CTO. She configured Okta to emit SAML assertions claiming that all 600 users were members of "Finance-Team." The idea was that "Finance-Team" meant "team members from the finance company," not "members of GlobalTech's finance department." There was no communication between the two teams about what the group names actually meant.

On February 2nd, the first FinanceCore user attempted to access GlobalTech's cloud resources through the SAML federation. The SAML assertion from Okta included a claim: `<Group>Finance-Team</Group>`. Azure AD saw the assertion, validated the signature (Okta's certificate was correctly configured), validated the [[trust-relationships]], and found that "Finance-Team" matched the expected group mapping. The user was granted the "Owner" role across all of GlobalTech's production Azure subscriptions and AWS accounts.

Over the next six hours, FinanceCore employees realized they had inherited admin access to:

- $1.2 billion in AWS infrastructure (EC2 instances, RDS databases, S3 buckets containing source code and financial data)
- GlobalTech's Azure subscriptions with all production Kubernetes clusters
- Office 365 tenant with access to all company email and SharePoint documents
- Splunk security logs for the entire organization
- ServiceNow IT ticketing system with customer data
- Salesforce CRM with customer contracts and pricing information

A FinanceCore engineer, initially thinking this was intentional, began exploring the infrastructure to understand the integration. He documented his findings in Slack messages to colleagues. One of those colleagues, who was already being recruited by a competitor, forwarded the access information to the competitor's security team. Within 48 hours, the competitor had extracted customer lists, pricing information, and partially deployed source code.

The breach was discovered when a GlobalTech security team member noticed unusual AWS API calls from an IP address registered in Ukraine (not where any FinanceCore employee was supposed to be). The investigation revealed the entire chain of failures.

## What Went Right

- **Anomalous access detection**: The security monitoring system flagged API calls from unexpected geographies within 48 hours, triggering the investigation before massive damage was done.
- **SAML signature validation**: Even though the trust was misconfigured, the SAML assertion signatures were correctly validated, so at least the assertion came from Okta as expected.
- **Audit logging**: Azure AD and AWS CloudTrail recorded all the actions taken by the privileged FinanceCore accounts, providing a complete forensic record of what was accessed.

## What Could Go Wrong

- **No human review of SAML attribute mappings**: The [[attribute-mapping]] between Okta's "Finance-Team" group and Azure AD's "Owner" role should have required a human review document that clarified what each group meant semantically.
- **No communication between identity teams**: The GlobalTech and FinanceCore identity administrators never talked to each other about group naming conventions, group membership, or what roles would be assigned.
- **Overly permissive role assignment**: Assigning the "Owner" role across all production subscriptions to anyone in "Finance-Team" was dramatically overprivileged. The role should have been limited to a specific resource group or set of resources.
- **No [[cross-certification]] review**: Before enabling SAML federation, a security review should have examined the trust chain, verified the certificate, and validated the [[attribute-mapping]].
- **Missing scope constraints**: The SAML configuration should have included [[transitive-trust]] limitations: "These assertions are only valid for the Finance-Team project resources, not for the entire AWS account."
- **No test federation first**: The trust was deployed to production immediately without a test run in a staging environment with a subset of users and a limited set of resources.

## Key Takeaways

- **Attribute-mapping requires explicit semantic documentation**: Document not just "what is mapped to what," but "what does this group actually represent" and "who should be in this group." Get sign-off from both the identity provider and service provider teams.
- **Federation trust escalations require least-privilege role assignment**: If federation trusts are used, the roles assigned via federated claims should be highly restricted—"Developer" role in a specific project, not "Owner" role across the organization.
- **Cross-certification processes must validate trust chains**: Before enabling any federated trust, conduct a security architecture review that examines: (1) certificate validity, (2) attribute claims, (3) role mappings, (4) scope constraints, and (5) revocation procedures.
- **Test federation in staging with production-like scale**: Stand up a test federation with a subset of users and a limited resource group. Verify that access is exactly as intended before production deployment.
- **Transitive-trust must be carefully limited**: Federation often creates transitive trust relationships (if A trusts B, and B trusts C, then C can impersonate A). Validate that the transitive trust doesn't exceed your intended scope.
- **Group membership must be explicitly managed**: Never assume that a group name means the same thing in two different systems. Explicitly define and manage group membership on both sides of the federation.

## Related Cases

- [[case-sso]] — SSO systems often implement federation internally; the same trust and attribute mapping risks apply.
- [[case-identity-management]] — [[identity-governance]] and [[provisioning-and-deprovisioning]] processes are critical to preventing orphaned access during acquisitions and integrations.
- [[case-mfa]] — Even with MFA, if the identity provider is compromised or misconfigured, the MFA serves only to authenticate the wrong entity.
