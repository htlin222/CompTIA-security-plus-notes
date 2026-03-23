---
title: "Case: The Terraform Credential Leak — Secrets in Source Control"
description: "A junior DevOps engineer accidentally commits Terraform state files containing AWS access keys and RDS passwords to a public GitHub repository. The credentials are harvested by automated scanners within 47 minutes and used to deploy cryptocurrency miners in the AWS account."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

ContourAI is an AI/ML startup that uses Terraform to manage their AWS infrastructure. On a Tuesday afternoon in March 2025, junior DevOps engineer David Nakamura was onboarded by the infrastructure team. His manager, James Chen, asked him to deploy a test RDS database for a data pipeline experiment. David created a Terraform configuration:

```hcl
resource "aws_db_instance" "test_postgres" {
  identifier = "test-postgres-ml-pipeline"
  allocated_storage = 100
  engine = "postgres"
  engine_version = "15.2"
  instance_class = "db.t3.medium"
  username = "admin"
  password = var.db_password
  publicly_accessible = false
}

resource "aws_s3_bucket" "ml_data" {
  bucket = "contourlabs-ml-data-test"
  acl = "private"
}

resource "aws_iam_access_key" "terraform_user" {
  user = aws_iam_user.terraform_deployer.name
}

output "db_password" {
  value = var.db_password
  sensitive = false
}
```

David also created a `terraform.tfvars` file to test the deployment:

```
db_password = "Contour2025!ML#Pipeline"
aws_access_key_id = "AKIA47K8Q3Z2X9W6C7Q2"
aws_secret_access_key = "9x8k2l9m5n3b9c7v4x1z3e5r7t9q2w4e6y8u0i2o"
region = "us-west-2"
```

After the Terraform deployment succeeded, David pushed all files to GitHub to make them available to his teammate for review. He created a new repository: `github.com/contourlabs/terraform-ml-pipeline` with public visibility (the default for his GitHub account).

The repository was public for 47 minutes.

Within those 47 minutes, automated credential-scanning services (like GitHub's own secret scanning, GitGuardian, and various open-source tools) detected the credentials and extracted them. At minute 38, an attacker with a list of harvested AWS credentials tried the keys against the AWS API. They succeeded.

At minute 42, the attacker created an EC2 instance (m5.4xlarge, a computationally expensive machine) and installed cryptocurrency mining software. Within minutes, the instance was consuming 95% CPU, mining Monero for the attacker.

At minute 46, GitHub's secret scanning alert reached David's email inbox. He immediately checked GitHub and realized the repository was public. He deleted the repository and messaged his manager.

James immediately called the AWS Account Security team, who noticed the rogue EC2 instance being launched at minute 42. They were able to terminate it and begin the incident response at minute 51. But in the 9 minutes the instance ran, it consumed $840 in AWS compute costs (billed to ContourAI) while mining approximately $1,200 worth of cryptocurrency for the attacker.

The incident response team's findings were sobering:

**What the attacker accessed:**
- AWS account: full administrative access via the compromised access key
- RDS password: exposed in plaintext
- S3 bucket: all contents accessible
- IAM roles: could have pivoted to other services

**What happened during the 9-minute window:**
- Created 1 EC2 instance (crypto miner)
- Listed all EC2 instances and security groups
- Enumerated all S3 buckets
- Checked CloudTrail logs (deleted some audit entries)
- Attempted to create additional IAM users (failed due to service control policies)

**What didn't happen:**
- No data exfiltration (data in S3 was research-only, not sensitive)
- No credential modification (AWS key rotation happened within 30 minutes)
- No additional service compromise (other AWS accounts were isolated)

If the credentials had remained valid longer, or if the attacker had found sensitive data, the impact could have been orders of magnitude worse.

## Post-Incident Actions

James and Chief Security Officer Dr. Michelle Wong implemented several changes:

**1. Secrets Management System** (Completed in Week 1):
- Deployed HashiCorp Vault to manage all secrets, API keys, and database passwords
- Integrated Vault with Terraform via the Vault provider, so credentials are injected at runtime, not stored in code
- Updated the Terraform configuration to fetch credentials from Vault instead of storing them in `.tfvars` files

```hcl
data "vault_generic_secret" "db_password" {
  path = "secret/contour/ml-pipeline/db-password"
}

resource "aws_db_instance" "test_postgres" {
  password = data.vault_generic_secret.db_password.data["password"]
  # ... rest of configuration
}
```

**2. Secret Scanning in CI/CD** (Completed in Week 1):
- Implemented pre-commit hooks that scan files for credential patterns before they can be committed
- Added GitHub secret scanning (GitHub's native feature) which automatically detects exposed secrets
- Configured automatic credential rotation for any detected exposure

**3. [[Configuration-drift]] Detection** (Completed in Week 2):
- Implemented Terraform Cloud with policy-as-code to enforce security guardrails
- Prevented any Terraform run that included hardcoded secrets
- Required all changes to use Vault-sourced credentials

**4. [[Immutable-infrastructure]] and [[policy-as-code]]** (Completed in Week 2):
- Signed all Terraform runs with GPG, preventing unauthorized changes
- Implemented Sentinel policies to enforce security: required MFA for account deletion, prevented public S3 buckets, required encryption on all databases

**5. Access Control Review** (Completed in Week 3):
- Revoked all long-lived AWS access keys—replaced with STS temporary credentials
- Implemented IAM role assumption instead of access key usage
- Required all infrastructure changes to go through role-based access, never direct credentials

**6. Training and Operational Changes** (Completed by Week 4):
- All engineers took security training on secrets management
- Created a `.gitignore` file that prevents `.tfvars`, `.tfstate`, and `credentials` files from being committed
- Implemented a checklist before any repo push: "Are there secrets in this commit?"
- Made repository security public by default with secret scanning enabled

## What Went Right

- **Automated detection caught the exposure quickly**: GitHub's secret scanning alerted within 5 minutes, and other automated systems detected the credentials within 47 minutes total.
- **AWS account isolation prevented lateral movement**: Service control policies prevented the attacker from creating additional IAM users or modifying critical services.
- **Attacker had limited time**: The 47-minute window and immediate remediation limited the damage to a single rogue instance and computational cost.
- **Audit trails existed**: CloudTrail logs (before the attacker deleted them) provided forensic evidence of what was accessed.
- **Impact was financial, not data**: The attacker achieved monetary gain but didn't access or steal sensitive data.

## What Could Go Wrong

- **If credentials had remained valid longer**: An 8-hour exposure instead of 47 minutes would have given the attacker time to exfiltrate data, create backdoors, or compromise other AWS accounts.
- **If DataLoss had occurred**: If the S3 bucket contained customer data, HIPAA data, or source code, the breach would have been catastrophic—not just a $840 compute bill.
- **If audit trails had been disabled**: Without CloudTrail, the incident response team would have no forensic record of what the attacker accessed.
- **If service control policies hadn't existed**: The attacker could have created IAM users, assumed roles, or pivoted to other services.
- **If credentials were never rotated**: A 6-month old credential leak would continue to grant attacker access indefinitely.

## Key Takeaways

- **Never commit credentials, API keys, or database passwords to Git**: Use a secrets management system (Vault, AWS Secrets Manager, Google Secret Manager) that injects credentials at runtime. Treat any committed credential as immediately compromised.
- **Pre-commit hooks and CI/CD scanning are essential**: Every commit should be scanned for credential patterns before it's pushed. Tools like `git-secrets` and `truffleHog` are free and should be mandatory.
- **[[Immutable-infrastructure|Immutable infrastructure]] requires signed, versioned changes**: Every Terraform run should be signed and approved by an authorized human. Policy-as-code should prevent overly permissive configurations.
- **Long-lived credentials are a liability**: Use temporary STS credentials with time limits (1 hour maximum). Access keys should expire after 90 days and be rotated continuously.
- **Repository security is the first line of defense**: Make repositories private by default. Enable secret scanning. Require branch protection and code review before any change.
- **Service control policies limit blast radius**: Even if credentials leak, SCPs can prevent account-wide compromise (e.g., no root account operations, no access key creation, no bucket policy changes).
- **[[Configuration-drift]] detection catches unauthorized changes**: Continuous validation of infrastructure against policy prevents "hidden" attacker modifications.

## Related Cases

- [[case-cloud-security]] — Broader AWS security patterns that could have prevented this incident
- [[case-secrets-management]] — Vault and other systems for managing credentials at scale
- [[case-policy-as-code]] — Automated policy enforcement that prevents insecure infrastructure

