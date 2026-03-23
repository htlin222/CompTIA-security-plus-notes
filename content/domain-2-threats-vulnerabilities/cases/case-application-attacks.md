---
title: "Case: The SSRF to Cloud Metadata Exploit — When API Vulnerabilities Chain"
description: "A bug bounty hunter discovers a Server-Side Request Forgery (SSRF) vulnerability in an internal API gateway that chains with AWS metadata endpoints to exfiltrate IAM credentials. The company has 24 hours before responsible disclosure goes public."
draft: false
date: 2026-03-21
tags:
  - domain/2
  - type/case
---

## The Scenario

CloudPlatform is a cloud management and compliance platform serving approximately 1,500 enterprise customers. The company has a custom-built API gateway written in Python that routes requests to various backend services. On February 28, 2026, at 2:15 PM PST, the company received an email from a bug bounty researcher (HackerOne handle "SecurityRaven") with a critical vulnerability report.

The vulnerability: Server-Side Request Forgery (SSRF) in the API gateway's webhook validation endpoint. The endpoint was supposed to validate that external webhooks were coming from legitimate sources by making an HTTP request to verify the sender's identity. However, the validation function had no URL allowlist—it would make an HTTP request to any URL provided by the user.

A sophisticated attacker could exploit this by:
1. Calling the webhook validation endpoint with URL = "http://169.254.169.254/latest/meta-data/iam/security-credentials/cloudplatform-service-role"
2. The API gateway would make an HTTP request to that URL
3. That URL is the AWS metadata endpoint, which returns IAM credentials for any EC2 instance that can reach it
4. The API gateway, running on an EC2 instance in AWS, would get back the temporary AWS credentials
5. The attacker would receive the credentials in the response

With those credentials, the attacker could:
- Access all S3 buckets that the service role could access
- Modify databases
- Spin up EC2 instances
- Access customer data

The researcher included proof-of-concept code demonstrating the vulnerability. They had responsibly disclosed it and given the company 90 days before public disclosure, as per standard responsible disclosure practices. However, since the vulnerability was critical and the company's infrastructure was significantly exposed, the researcher had also notified the company's insurance carrier.

Within 30 minutes of receiving the report, CloudPlatform's CTO, Dr. Michael Hassan, was briefing the executive team. The situation was stark:

**Timeline:**
- Today (February 28): Bug bounty disclosure received
- April 29: Public disclosure will occur if not patched
- But the vulnerability was already public in various security forums and hacker communities (the researcher had likely developed this independently after seeing similar patterns, and others may have discovered it too)

**Impact:**
- The API gateway handles 100% of CloudPlatform's customer requests
- The SSRF vulnerability affects all requests to the webhook validation endpoint
- Customer data from 1,500 organizations is at risk

**Immediate Actions (Hour 1-2):**

Michael's team immediately:
1. Reviewed the code to confirm the vulnerability: yes, the webhook validation function had no URL allowlist
2. Checked logs to see if the vulnerability had been exploited: logs showed no evidence of anyone exploiting this specific endpoint, but logs only went back 7 days
3. Checked the security scanning tools: had this vulnerability been detected? No—the code scanning tools hadn't flagged it because the vulnerability wasn't about a known CVE, it was a logic flaw in CloudPlatform's custom code
4. Assessed the blast radius: the webhook endpoint was used by approximately 47 customers; the other 1,453 customers used direct API calls, not webhooks

**Remediation (Hour 3-8):**

Michael's team developed a fix:
```python
# BEFORE (vulnerable):
def validate_webhook(user_url):
    response = requests.get(user_url, timeout=5)
    return response.json()

# AFTER (fixed):
ALLOWED_DOMAINS = ['api.github.com', 'api.gitlab.com', 'api.slack.com']
def validate_webhook(user_url):
    parsed_url = urllib.parse.urlparse(user_url)
    if parsed_url.netloc not in ALLOWED_DOMAINS:
        raise ValueError("Webhook domain not in allowlist")
    response = requests.get(user_url, timeout=5)
    return response.json()
```

The fix was simple: only allow webhook validation requests to known, approved domains (GitHub, GitLab, Slack). Block everything else, including the AWS metadata endpoint and internal IP addresses.

The fix was tested immediately:
1. Confirmed that the SSRF attack no longer worked (requests to 169.254.169.254 were blocked)
2. Confirmed that legitimate webhook validation still worked (requests to api.github.com proceeded)
3. Confirmed that no other endpoints had similar vulnerabilities (code review of 12 similar validation functions)

**Deployment (Hour 8-12):**

Michael made a difficult decision: deploy the fix immediately without following the normal change management process. The risk of the vulnerability being exploited was higher than the risk of the fix causing problems. The change was deployed to production at 11:30 PM on February 28.

Deployment had minimal impact:
- No customers reported problems because the fix only made the webhook endpoint more restrictive
- 47 customers using webhook validation saw no change in behavior (they were only using allowed domains)
- The attack surface was immediately reduced

**Post-Incident Investigation (March 1-3):**

Michael's team investigated whether the vulnerability had been exploited:
1. Searched CloudTrail logs (AWS's audit logging service) for unusual access patterns: found one connection from the API gateway to the AWS metadata endpoint, occurring on March 1 at 8:15 AM (approximately 6 hours after the fix was deployed)
2. The attacker was still trying the exploit, even though it had been fixed. This meant the attacker was working based on old information or had automated tools that were retrying the endpoint
3. No evidence that the vulnerability had been exploited before the fix was deployed: the metadata endpoint showed no successful credential queries from the API gateway's IP address in the prior 7 days

**Root Cause Analysis (March 4-7):**

Why had this vulnerability existed for so long?

1. **Code review process was insufficient**: The webhook validation function was written 8 months prior. It had been code reviewed by one other engineer, who didn't catch the vulnerability.
2. **Security testing was missing**: The company had no automated [[api-attacks|API security testing]] tools. A tool like Burp Suite or OWASP ZAP would have found this immediately.
3. **Security training was minimal**: The engineer who wrote the code wasn't aware of [[server-side-request-forgery]] (SSRF) vulnerabilities or their potential impact.
4. **The metadata endpoint is a known target**: AWS documentation warns against SSRF vulnerabilities that could expose metadata. This should have been part of security training.

**Post-Incident Improvements:**

Michael implemented:
1. **Security code review checklist**: A specific checklist for security-sensitive functions (anything that makes HTTP requests, accesses databases, handles authentication). The checklist included: "Does this function access external URLs? If yes, is there a URL allowlist?"
2. **Automated API security testing**: Integration of OWASP ZAP into the CI/CD pipeline. Every API change is automatically tested for SSRF, injection attacks, broken authentication, etc.
3. **Security training for developers**: Mandatory quarterly training on [[api-attacks]], [[injection-attacks]], [[broken-authentication]], and other common [[application-layer-attacks]].
4. **Allowlist-based design for network requests**: Any function that makes HTTP requests should use an allowlist (whitelist) approach, not a blocklist (blacklist) approach.
5. **Metadata endpoint protection**: Configure security groups and IAM policies to block EC2 metadata endpoint access from services that don't need it

## What Went Right

- **Responsible disclosure process worked**: The bug bounty researcher disclosed privately before public disclosure, giving CloudPlatform time to patch
- **Fast code review and fix**: The team understood the vulnerability, developed a fix, and deployed it within 12 hours
- **Comprehensive logging**: CloudTrail logs provided evidence of attempted exploitation post-fix
- **Blast radius was limited**: Only 47 customers used the vulnerable endpoint; the remaining 1,453 were unaffected
- **No evidence of pre-fix exploitation**: Investigation showed no evidence the vulnerability had been actively exploited before patching
- **Quick decision-making**: The CTO made the correct call to deploy the fix outside of normal change management due to the severity

## What Could Go Wrong

- **No URL allowlist in the original code**: The function accepted any URL, including internal IP addresses like the AWS metadata endpoint
- **Insufficient code review**: The vulnerability should have been caught by a security-aware code reviewer
- **No automated API security testing**: Tools like ZAP or Burp Suite would have flagged this vulnerability during development
- **Metadata endpoint was accessible**: The EC2 instance had unrestricted access to the metadata endpoint. IAM policies could have blocked this access to defense-in-depth
- **No security training for developers**: The engineer who wrote the code wasn't aware of SSRF vulnerabilities
- **Logging could have been better**: The 7-day log retention was lucky—if logs were only kept for 1 day, pre-fix exploitation might not have been discoverable

## Key Takeaways

- **[[Server-side-request-forgery|SSRF]] vulnerabilities can chain with cloud metadata endpoints to exfiltrate credentials**: Any function that makes HTTP requests to user-provided URLs is a potential SSRF attack surface.
- **[[Allowlist-based]] approach is essential for anything involving external requests**: Never use a blocklist (deny specific domains). Always use an allowlist (allow only specific, legitimate domains).
- **Automated API security testing should be in the CI/CD pipeline**: Tools like OWASP ZAP, Burp Suite, or Checkov can identify common API vulnerabilities before code reaches production.
- **Security training for developers must include [[application-attacks|application-layer vulnerabilities]]**: Developers need to understand SSRF, SQL injection, XSS, broken authentication, and other common attacks in their threat model.
- **Defense-in-depth applies to cloud metadata endpoints**: Even if SSRF is possible, blocking access to the metadata endpoint with IAM policies provides an additional layer of defense.
- **Incident response for critical vulnerabilities may require waiving normal change management**: A critical vulnerability that's actively being exploited should be patched immediately, even without full testing and approval workflows.
- **Security code review checklists improve consistency**: Rather than relying on reviewers to remember every security consideration, a checklist ensures consistent review of sensitive functions.

## Related Cases

- [[case-injection-attacks]] — Other forms of injection attacks (SQL injection, command injection) that can be similarly chained
- [[case-xss-and-csrf]] — Other application-layer attacks affecting APIs
- [[case-broken-authentication]] — How compromised credentials (like those exfiltrated from SSRF attacks) enable further attacks
