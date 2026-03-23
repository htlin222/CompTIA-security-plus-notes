---
title: "Glossary"
description: "Alphabetical listing of all 563 security concepts"
draft: false
date: 2026-03-23
tags:
  - type/index
---

## #

- **[[3-2-1-backup-rule|3-2-1 backup rule]]** — 3 copies of data, on 2 different media types, with 1 copy off-site
- **[[8021x|802.1X]]** — IEEE standard for port-based network access control; uses EAP for authentication

## A

- **[[access-badges|Access badges]]** — RFID or smart card-based identification for building entry
- **[[access-control-lists-acls|Access control lists (ACLs)]]** — Defining explicit allow/deny rules for network traffic and resource access
- **[[access-control-vestibules-mantraps|Access control vestibules (mantraps)]]** — Dual-door chambers allowing only one door open at a time; prevents tailgating
- **[[account-indicators|Account indicators]]** — Multiple failed logins, privilege escalation attempts, account lockouts, new admin accounts
- **[[accounting|Accounting]]** — Logging and tracking user activities for audit and forensic purposes
- **[[active-active-vs-active-passive|Active-active vs. active-passive]]** — active-active uses all nodes; active-passive has standby nodes for failover
- **[[ad-hoc-vs-recurring-vs-continuous|Ad hoc vs. recurring vs. continuous]]** — assessments may be triggered by events, scheduled, or ongoing
- **[[adaptive-identity|Adaptive identity]]** — Authentication and authorization that adjust based on real-time risk assessment
- **[[administrative-controls|Administrative controls]]** — Policies, procedures, training, background checks
- **[[advisary-emulation|Advisary emulation]]** — Simulating known threat actor behavior to test detection capabilities
- **[[after-action-review|After-action review]]** — lessons learned documented after each test or actual incident
- **[[air-gap|Air gap]]** — complete physical isolation with no network connectivity; highest security, used for critical systems
- **[[always-on-vpn|Always-on VPN]]** — automatically connects when the device is powered on; ensures consistent policy enforcement
- **[[amplification-attack|Amplification attack]]** — Using protocols like DNS, NTP, or memcached to amplify a small request into a massive response
- **[[amplificationreflection|Amplification/Reflection]]** — Using third-party servers (DNS, NTP, memcached) to amplify and reflect traffic at the victim
- **[[anonymization|Anonymization]]** — irreversibly removes identifying information
- **[[anonymization-vs-pseudonymization|Anonymization vs. pseudonymization]]** — anonymization is irreversible; pseudonymization replaces identifiers but can be reversed with a key
- **[[anti-forensics|Anti-forensics]]** — Techniques attackers use to hinder forensic analysis (encryption, log wiping, timestomping)
- **[[anti-phishing-controls|Anti-phishing controls]]** — URL rewriting, sandbox analysis of attachments, impersonation detection
- **[[antivirus-anti-malware|Antivirus / Anti-malware]]** — Signature-based and heuristic detection of known and unknown malware
- **[[api-attacks|API attacks]]** — Exploiting insecure APIs through broken authentication, excessive data exposure, or lack of rate limiting
- **[[api-integration|API integration]]** — Connecting security tools through REST APIs for orchestrated workflows
- **[[api-security|API security]]** — cloud services are API-driven; securing APIs is critical to cloud security
- **[[application-allowlisting|Application allowlisting]]** — Only permitting approved software to execute — stronger than blocklisting
- **[[application-whitelistingallowlisting|Application whitelisting/allowlisting]]** — Only approved applications can execute on the endpoint
- **[[application-layer-attacks|Application-layer attacks]]** — Targeting specific services with legitimate-looking requests to exhaust application resources
- **[[arp-spoofingpoisoning|ARP spoofing/poisoning]]** — Sending fake ARP messages to associate the attacker
- **[[attack-surface-management|Attack surface management]]** — Continuously identifying and reducing exposure across all attack vectors
- **[[attestation|Attestation]]** — formal declaration by an auditor that controls are operating effectively
- **[[attribute-mapping|Attribute mapping]]** — Translating identity attributes (role, department) between different organizational schemas
- **[[attribute-based-access-control-abac|Attribute-Based Access Control (ABAC)]]** — Access decisions based on attributes such as department, location, or time of day
- **[[audit-scope|Audit scope]]** — defines what systems, processes, and controls are being examined
- **[[authentication|Authentication]]** — typically uses certificates, MFA, RADIUS, or LDAP for VPN user authentication
- **[[authorization-vs-authentication|Authorization vs. Authentication]]** — Authentication proves identity; authorization defines permissions
- **[[automated-response|Automated response]]** — Predefined playbooks can kill processes, quarantine files, or block IPs without human intervention
- **[[automation|Automation]]** — Executing repetitive tasks without human intervention — enriching alerts, blocking IPs, disabling accounts
- **[[availability|Availability]]** — Ensuring systems and data are accessible to authorized users when needed

## B

- **[[backoutrollback-plan|Backout/Rollback plan]]** — Predefined steps to reverse a change if it causes problems
- **[[baiting|Baiting]]** — Offering something enticing (USB drive, free download) to lure victims
- **[[bandwidth-monitoring|Bandwidth monitoring]]** — Detecting unusual spikes that may indicate DDoS attacks or data exfiltration
- **[[baseline-establishment|Baseline establishment]]** — Defining normal network behavior to identify deviations and anomalies
- **[[baseline-driven-hunting|Baseline-driven hunting]]** — Identifying deviations from known-good baselines in network traffic, process execution, or user behavior
- **[[behavioral-analysis|Behavioral analysis]]** — Detects threats based on anomalous behavior rather than known signatures
- **[[behavioral-indicators|Behavioral indicators]]** — Unusual login times, impossible travel, lateral movement patterns suggesting compromise
- **[[bell-lapadula-model|Bell-LaPadula Model]]** — \
- **[[benchmarks-vs-frameworks|Benchmarks vs. frameworks]]** — benchmarks are specific configuration guides; frameworks are broader programs
- **[[benefits|Benefits]]** — Speed, consistency, scalability, reduced human error, better documentation
- **[[bia-as-the-foundation|BIA as the foundation]]** — the Business Impact Analysis identifies critical functions and sets recovery priorities
- **[[biba-model|Biba Model]]** — \
- **[[biometric-authentication|Biometric authentication]]** — FAR vs. FRR; CER (Crossover Error Rate) measures biometric system accuracy
- **[[birthday-attack|Birthday attack]]** — Exploits the mathematics of hash collisions; finding two inputs that produce the same hash output
- **[[blind-sql-injection|Blind SQL injection]]** — Application does not return data directly; attacker infers information through true/false responses or time delays
- **[[bluetooth-attacks|Bluetooth attacks]]** — Bluejacking (unsolicited messages), Bluesnarfing (data theft), Bluebugging (full device control)
- **[[board-and-executive-involvement|Board and executive involvement]]** — governance starts at the top; senior leadership sets the tone and approves risk appetite
- **[[bollards|Bollards]]** — Short vertical posts preventing vehicle ramming attacks
- **[[boot-integrity|Boot integrity]]** — Secure Boot, Measured Boot, and TPM ensure the system hasn
- **[[botnet|Botnet]]** — Network of compromised devices controlled by an attacker to generate DDoS traffic
- **[[brand-impersonation|Brand impersonation]]** — Creating fake websites, emails, or social media profiles mimicking trusted brands
- **[[break-glass-accounts|Break-glass accounts]]** — Emergency access accounts with heightened monitoring for use when normal access paths fail
- **[[brute-force|Brute force]]** — Trying all possible keys or password combinations until the correct one is found
- **[[buffer-overflow|Buffer overflow]]** — Sending more data than a buffer can hold, overwriting adjacent memory to execute arbitrary code
- **[[bug-bounty-programs|Bug bounty programs]]** — Crowdsourced testing where external researchers report vulnerabilities for rewards
- **[[business-continuity-vs-disaster-recovery|Business continuity vs. disaster recovery]]** — BCP keeps the business running during disruption; DR restores IT systems after disruption
- **[[business-email-compromise-bec|Business Email Compromise (BEC)]]** — Social engineering attacks where attackers impersonate executives to request wire transfers or sensitive data

## C

- **[[cable-locks|Cable locks]]** — Physically secure laptops and equipment to prevent theft
- **[[caching|Caching]]** — proxies store frequently accessed content to reduce bandwidth and improve response times
- **[[capacity-planning|Capacity planning]]** — ensuring sufficient resources to handle peak loads and growth
- **[[case-management|Case management]]** — Tracking incidents from detection through resolution with full documentation
- **[[centralized-logging|Centralized logging]]** — Aggregating logs from all sources into a single repository for unified analysis
- **[[centralized-vs-decentralized-governance|Centralized vs. decentralized governance]]** — centralized offers consistency; decentralized gives business units flexibility
- **[[certificate-formats|Certificate formats]]** — PEM (.pem, .crt), DER (.der), PKCS#12 (.pfx, .p12), PKCS#7 (.p7b)
- **[[certificate-lifecycle|Certificate lifecycle]]** — request (CSR), issuance, usage, renewal, revocation
- **[[certificate-pinning|Certificate pinning]]** — application hardcodes the expected certificate or public key to prevent MITM with rogue certs
- **[[certificate-based-authentication|Certificate-based authentication]]** — Uses digital certificates from a PKI for mutual authentication
- **[[chain-of-custody|Chain of custody]]** — Documented record of who handled the evidence, when, and what was done — breaks invalidate evidence
- **[[chain-of-trust|Chain of trust]]** — each certificate is signed by the CA above it; browsers trust the root CA
- **[[change-advisory-board-cab|Change Advisory Board (CAB)]]** — Group of stakeholders who review and approve/deny change requests
- **[[chosen-plaintextciphertext-attack|Chosen plaintext/ciphertext attack]]** — Attacker can encrypt or decrypt chosen data to extract information about the key
- **[[cis-benchmarks|CIS Benchmarks]]** — Industry-standard security configuration guidelines from the Center for Internet Security
- **[[cis-controls|CIS Controls]]** — prioritized list of cybersecurity best practices (formerly SANS Top 20)
- **[[classification-criteria|Classification criteria]]** — regulatory requirements, business value, sensitivity, impact if disclosed
- **[[cloud-deployment-models|Cloud deployment models]]** — public, private, hybrid, community, multi-cloud
- **[[collision-attack|Collision attack]]** — Specifically crafting two different inputs that produce an identical hash — compromises integrity verification
- **[[command-injection-os-injection|Command injection (OS injection)]]** — Inserting operating system commands through application inputs to execute on the host system
- **[[commercial-private-sector-classifications|Commercial / private sector classifications]]** — Confidential/Restricted, Private/Internal, Public
- **[[common-delivery-methods|Common delivery methods]]** — Phishing emails, exploited vulnerabilities (especially RDP), drive-by downloads, supply chain compromise
- **[[common-tools|Common IaC tools]]** — Terraform, AWS CloudFormation, Azure ARM/Bicep, Ansible, Puppet, Chef
- **[[common-siem-platforms|Common SIEM platforms]]** — Splunk, Microsoft Sentinel, IBM QRadar, Elastic Security
- **[[communication-plan|Communication plan]]** — Who to notify (management, legal, law enforcement, customers, regulators)
- **[[compensating-controls|Compensating controls]]** — Alternative measures when the primary control cannot be implemented
- **[[compliance-automation|Compliance automation]]** — tools that continuously assess configurations against baselines and flag deviations
- **[[compliance-monitoring|Compliance monitoring]]** — ongoing checks to ensure controls remain effective and policies are followed
- **[[compliance-reporting|Compliance reporting]]** — documentation submitted to regulators or auditors demonstrating adherence
- **[[conditional-access|Conditional access]]** — Dynamic authorization based on risk signals (device compliance, location, behavior)
- **[[confidence-levels|Confidence levels]]** — Rating how reliable and accurate a piece of intelligence is
- **[[confidentiality|Confidentiality]]** — Protecting data from unauthorized access or disclosure
- **[[configuration-drift|Configuration drift]]** — when running infrastructure diverges from its defined state; IaC detects and corrects this
- **[[configuration-management|Configuration management]]** — Maintaining a consistent, secure baseline of system configurations and detecting drift
- **[[consequences-of-non-compliance|Consequences of non-compliance]]** — fines, sanctions, loss of certifications, lawsuits, reputational harm
- **[[containment|Containment]]** — Short-term (isolate the system) and long-term (apply temporary fixes while building permanent solutions)
- **[[content-filtering|Content filtering]]** — proxies can inspect and block traffic based on URLs, categories, or content types
- **[[continuous-integrationdeployment-cicd-security|Continuous integration/deployment (CI/CD) security]]** — Embedding security checks into automated build and deployment pipelines
- **[[continuous-monitoring|Continuous monitoring]]** — Agents on endpoints record process execution, file changes, registry modifications, and network connections
- **[[contractual-compliance|Contractual compliance]]** — obligations defined in business agreements and SLAs
- **[[control-diversity|Control diversity]]** — Combining different types of controls (technical + administrative + physical) at each security layer
- **[[correlation-rules|Correlation rules]]** — Logic that identifies patterns across multiple events that indicate an attack
- **[[credential-rotation|Credential rotation]]** — Automatically changing privileged passwords on a schedule or after each use
- **[[credential-stuffing|Credential stuffing]]** — Using stolen username/password pairs from breached databases to log into other services
- **[[credentialed-vs-non-credentialed-scans|Credentialed vs. non-credentialed scans]]** — Credentialed scans log into systems for deeper analysis; non-credentialed scans show the external attacker
- **[[critical-business-functions|Critical business functions]]** — processes that, if disrupted, would cause significant harm to the organization
- **[[cross-certification|Cross-certification]]** — two CAs trust each other
- **[[cryptocurrency-payment|Cryptocurrency payment]]** — Bitcoin or Monero used to make ransom payments difficult to trace
- **[[csa-cloud-controls-matrix-ccm|CSA Cloud Controls Matrix (CCM)]]** — cloud-specific security control framework
- **[[csr-certificate-signing-request|CSR (Certificate Signing Request)]]** — generated by the applicant; contains the public key and identity information
- **[[example|CSRF Example]]** — A hidden image tag that triggers a bank transfer while the victim is logged into their banking site
- **[[mechanism|CSRF Mechanism]]** — Attacker crafts a request using hidden forms or image tags that perform actions using the victim
- **[[culture-of-security|Culture of security]]** — training should foster a culture where reporting suspicious activity is encouraged, not punished
- **[[cve-common-vulnerabilities-and-exposures|CVE (Common Vulnerabilities and Exposures)]]** — Unique identifiers for publicly known vulnerabilities
- **[[cvss-common-vulnerability-scoring-system|CVSS (Common Vulnerability Scoring System)]]** — Standardized 0-10 scoring system for vulnerability severity

## D

- **[[dad-triad|DAD Triad]]** — Disclosure, Alteration, Destruction — the attacker
- **[[dashboards-and-reporting|Dashboards and reporting]]** — Visual representation of security posture, trends, and compliance metrics
- **[[data-breach-notification|Data breach notification]]** — regulations often require notifying affected individuals and authorities within a set timeframe
- **[[data-loss-prevention-dlp|Data loss prevention (DLP)]]** — tools that detect and prevent unauthorized data exfiltration
- **[[data-masking|Data masking]]** — obscures portions of data (e.g., showing only last 4 digits of a credit card)
- **[[data-ownership-and-processing-agreements|Data ownership and processing agreements]]** — clearly define who owns data and how it is handled, stored, and deleted
- **[[data-retention-policies|Data retention policies]]** — define how long data must be kept and when it must be destroyed
- **[[data-sources|Data sources]]** — EDR telemetry, SIEM logs, network flow data, DNS logs, authentication logs
- **[[data-sovereignty|Data sovereignty]]** — data stored in the cloud is subject to the laws of its physical location
- **[[data-states|Data states]]** — data at rest, data in transit, data in use; each requires appropriate protection
- **[[deauthentication-attack|Deauthentication attack]]** — Sending forged 802.11 deauth frames to disconnect clients from a wireless network
- **[[deception-platforms|Deception platforms]]** — Enterprise solutions that automate deployment and management of decoys across the network
- **[[declassification|Declassification]]** — reducing the classification level when sensitivity decreases over time
- **[[decommissioning|Decommissioning]]** — Properly retiring end-of-life systems that can no longer be patched
- **[[default-credentials|Default credentials]]** — Factory-set usernames and passwords that are publicly documented and easily exploited
- **[[defense-in-depth|Defense in depth]]** — layered security controls so that if one fails, others still protect the environment
- **[[defenses|Defenses]]** — HTTPS everywhere, HSTS, certificate pinning, mutual TLS, encrypted protocols; anti-CSRF tokens, SameSite cookies
- **[[dependencies|Dependencies]]** — upstream and downstream systems that a critical function relies on
- **[[deprecated-algorithms|Deprecated algorithms]]** — MD5, SHA-1, DES, RC4 — algorithms that are cryptographically weak and should not be used
- **[[detection-and-analysis|Detection and analysis]]** — Identifying incidents through alerts, logs, user reports, and threat intelligence
- **[[dictionary-attack|Dictionary attack]]** — Using a wordlist of common passwords and variations to guess credentials
- **[[digital-signatures|Digital signatures]]** — hash the message, then encrypt the hash with the sender
- **[[directory-services|Directory services]]** — LDAP, Active Directory — centralized authentication and identity stores
- **[[directory-traversal|Directory traversal]]** — Using \
- **[[disable-unnecessary-services-and-ports|Disable unnecessary services and ports]]** — Reduce potential entry points by turning off what is not needed
- **[[disk-imaging|Disk imaging]]** — Creating a bit-for-bit copy of storage media for analysis without altering the original
- **[[diversity|Diversity]]** — using different vendors, technologies, or paths to avoid common-mode failures
- **[[dkim-domainkeys-identified-mail|DKIM (DomainKeys Identified Mail)]]** — Adds a digital signature to outgoing emails to verify the message was not altered in transit
- **[[dll-injection|DLL injection]]** — Forcing a process to load a malicious dynamic-link library into its address space
- **[[dmarc-domain-based-message-authentication-reporting-conformance|DMARC (Domain-based Message Authentication, Reporting & Conformance)]]** — Policy that tells receiving servers what to do when SPF/DKIM fail (none, quarantine, reject)
- **[[dmz-demilitarized-zone|DMZ (Demilitarized Zone)]]** — screened subnet between the internet and internal network for public-facing services
- **[[dns-amplification|DNS amplification]]** — Using open DNS resolvers to amplify DDoS attacks — small queries generate large responses
- **[[dns-hijacking|DNS hijacking]]** — Compromising a domain
- **[[dns-over-https-doh-dns-over-tls-dot|DNS over HTTPS (DoH) / DNS over TLS (DoT)]]** — Encrypts DNS queries to prevent eavesdropping and manipulation
- **[[dns-poisoning-dns-cache-poisoning|DNS poisoning / DNS cache poisoning]]** — Injecting false DNS records into a resolver
- **[[dns-sinkholes|DNS sinkholes]]** — Redirect malicious domain requests to a controlled server to disrupt botnets and detect infected hosts
- **[[dns-spoofing|DNS spoofing]]** — Forging DNS responses to redirect queries to malicious IP addresses
- **[[dns-tunneling|DNS tunneling]]** — Encoding data within DNS queries and responses to exfiltrate data or establish C2 channels
- **[[dnssec-dns-security-extensions|DNSSEC (DNS Security Extensions)]]** — Adds digital signatures to DNS records to verify authenticity and integrity
- **[[documentation|Documentation]]** — recovery procedures, contact lists, system dependencies, vendor information
- **[[dom-based-xss|DOM-based XSS]]** — Script executes by modifying the DOM in the victim
- **[[domain-hijacking|Domain hijacking]]** — Taking control of a domain name through social engineering or exploiting weak registrar account security
- **[[double-extortion|Double extortion]]** — Attackers exfiltrate data before encrypting — threaten to publish if ransom is not paid
- **[[downgrade-attack|Downgrade attack]]** — Forcing a system to use a weaker, vulnerable cryptographic protocol or cipher
- **[[due-diligence-vs-due-care|Due diligence vs. due care]]** — Due diligence is researching and understanding risks; due care is acting responsibly to mitigate them

## E

- **[[e-discovery|E-discovery]]** — Legal process of identifying and collecting electronically stored information (ESI) for litigation
- **[[east-west-traffic-control|East-west traffic control]]** — segmentation is essential for monitoring and controlling internal lateral movement
- **[[east-west-vs-north-south-traffic|East-west vs. north-south traffic]]** — east-west is internal lateral; north-south crosses the network boundary
- **[[email-encryption|Email encryption]]** — Protects email content in transit and at rest; can be gateway-based or end-to-end
- **[[email-indicators|Email indicators]]** — Phishing sender addresses, malicious attachment hashes, suspicious URLs in email bodies
- **[[encryption|Encryption]]** — Protecting data at rest and in transit to ensure confidentiality even if intercepted
- **[[encryption-modes|Encryption modes]]** — ECB (insecure, patterns visible), CBC, CTR, GCM (authenticated encryption)
- **[[encryption-based-ransomware|Encryption-based ransomware]]** — Encrypts files using strong cryptographic algorithms; data is unrecoverable without the key
- **[[environmental-controls|Environmental controls]]** — Fire suppression, HVAC, and humidity controls protecting physical infrastructure
- **[[environmental-factors|Environmental factors]]** — internal (staffing, technology) and external (regulatory, geopolitical)
- **[[ephemeral-keys|Ephemeral keys]]** — temporary keys used for a single session; provide perfect forward secrecy
- **[[eradication|Eradication]]** — Removing the threat — deleting malware, closing vulnerabilities, resetting compromised credentials
- **[[evidence-collection|Evidence collection]]** — logs, configurations, policies, interviews, and observations gathered during audits
- **[[evil-twin|Evil twin]]** — Rogue access point that mimics a legitimate network
- **[[exception-process|Exception process]]** — formal mechanism for requesting and approving deviations from policy
- **[[exploitation|Exploitation]]** — Attempting to gain unauthorized access using discovered vulnerabilities
- **[[external-audit|External audit]]** — performed by an independent third party; required for certifications and regulatory compliance

## F

- **[[failback|Failback]]** — returning to the primary system after it is restored
- **[[failover|Failover]]** — automatic switching to a standby system when the primary fails
- **[[fake-telemetry|Fake telemetry]]** — Generating false network data to confuse attackers performing reconnaissance
- **[[false-positives|False positives]]** — Legitimate activity that matches IoC patterns — tuning is essential to reduce alert fatigue
- **[[false-positivesnegatives|False positives/negatives]]** — Validating scan results to avoid wasting resources or missing real vulnerabilities
- **[[faraday-cage|Faraday cage]]** — Blocks electromagnetic signals; prevents eavesdropping and signal leakage
- **[[fencing|Fencing]]** — Perimeter barriers; height determines deterrence level for physical security
- **[[ferpa|FERPA]]** — US law protecting student education records
- **[[file-integrity-monitoring|File integrity monitoring]]** — comparing current file hashes to known-good baselines to detect tampering
- **[[file-system-permissions|File system permissions]]** — Restricting access to sensitive files and directories
- **[[file-based-indicators|File-based indicators]]** — Malicious file hashes, suspicious file names, unexpected file locations
- **[[fileless-malware|Fileless malware]]** — Operates entirely in memory using legitimate tools (PowerShell, WMI) — leaves no files on disk
- **[[fileless-malware-detection|Fileless malware detection]]** — Identifies threats that operate in memory without writing to disk
- **[[findings-and-remediation|Findings and remediation]]** — audit results include findings (issues) and recommendations with timelines for remediation
- **[[firmware-updates|Firmware updates]]** — BIOS/UEFI and device firmware must be kept current
- **[[fourth-party-risk|Fourth-party risk]]** — risk from your vendor
- **[[full-disk-encryption-fde|Full disk encryption (FDE)]]** — Encrypts the entire drive to protect data at rest (e.g., BitLocker, FileVault)

## G

- **[[gamification|Gamification]]** — using competitions, rewards, and interactive elements to increase engagement
- **[[gdpr|GDPR]]** — EU regulation protecting personal data; applies to any org processing EU residents
- **[[geographic-considerations|Geographic considerations]]** — different jurisdictions have different requirements; data sovereignty matters
- **[[glba|GLBA]]** — US law requiring financial institutions to protect customer information
- **[[governance-committees|Governance committees]]** — cross-functional groups that review security posture, approve policy changes, and allocate budgets
- **[[government-military-classifications|Government / military classifications]]** — Top Secret, Secret, Confidential, Unclassified
- **[[guardrails|Guardrails]]** — Safety controls in automation to prevent unintended actions (approval gates, rollback capabilities)
- **[[guest-networking|Guest networking]]** — NAC can direct unknown or personal devices to an isolated guest network

## H

- **[[handling-procedures|Handling procedures]]** — storage, transmission, retention, and destruction rules per classification level
- **[[hardening-the-hypervisor|Hardening the hypervisor]]** — patching, disabling unnecessary services, restricting management access, enabling secure boot
- **[[hardware-security-module-hsm|Hardware Security Module (HSM)]]** — tamper-resistant hardware device that manages keys and performs cryptographic operations
- **[[hardware-vulnerabilities|Hardware vulnerabilities]]** — Side-channel attacks, firmware flaws (Spectre, Meltdown), end-of-life hardware
- **[[hash-verification|Hash verification]]** — Using MD5/SHA-256 hashes to prove the forensic copy is identical to the original
- **[[health-checks|Health checks]]** — load balancers monitor backend server health and remove unhealthy nodes from rotation
- **[[high-availability-ha|High availability (HA)]]** — measured in \
- **[[hipaa|HIPAA]]** — US law protecting health information (PHI); applies to covered entities and business associates
- **[[hmac-hash-based-message-authentication-code|HMAC (Hash-based Message Authentication Code)]]** — combines a hash with a secret key to provide integrity AND authentication
- **[[honeyfiles|Honeyfiles]]** — Fake files placed on systems to trigger alerts when accessed by attackers
- **[[honeynets|Honeynets]]** — Networks of honeypots simulating an entire environment to study attacker behavior
- **[[honeypots|Honeypots]]** — Decoy systems designed to attract and trap attackers for detection and analysis
- **[[honeytokens|Honeytokens]]** — Fake data (credentials, database records, API keys) that alert when used
- **[[host-based-firewall|Host-based firewall]]** — Controls inbound and outbound traffic at the individual device level
- **[[host-based-idsips-hidships|Host-based IDS/IPS (HIDS/HIPS)]]** — Monitors system activity and file integrity on the endpoint
- **[[host-based-indicators|Host-based indicators]]** — Unexpected processes, registry changes, scheduled tasks, unauthorized accounts, modified system files
- **[[host-based-vs-network-based|Host-based vs. network-based]]** — host firewalls protect individual systems; network firewalls protect entire segments
- **[[hotp-hmac-based-one-time-password|HOTP (HMAC-based One-Time Password)]]** — Counter-based OTP that remains valid until used
- **[[html-injection|HTML injection]]** — Inserting HTML markup into web pages to alter content or redirect users
- **[[https-spoofing|HTTPS spoofing]]** — Presenting a fraudulent certificate to intercept encrypted web traffic
- **[[human-factors|Human factors]]** — Lack of training, social engineering susceptibility, insider threats
- **[[human-vectors|Human vectors]]** — Social engineering exploiting human psychology as an attack vector
- **[[hunt-maturity-model|Hunt maturity model]]** — Levels from HM0 (initial, relies on automated alerts) to HM4 (leading, creates new detection content)
- **[[hybrid-attack|Hybrid attack]]** — Combining dictionary words with brute-force modifications to crack common password patterns
- **[[hybrid-encryption|Hybrid encryption]]** — uses asymmetric to exchange a symmetric session key, then symmetric for bulk data (TLS uses this)
- **[[hypothesis-driven-hunting|Hypothesis-driven hunting]]** — Starting with an educated guess about attacker behavior and searching for evidence to confirm or deny it

## I

- **[[identity-and-access-management|Identity and access management]]** — federated identity, SSO, and strong IAM policies for cloud resources
- **[[identity-governance|Identity governance]]** — Periodic access reviews and certification to ensure least privilege is maintained
- **[[identity-lifecycle-management|Identity lifecycle management]]** — Joiner-mover-leaver processes that track an identity from onboarding to offboarding
- **[[identity-provider-idp|Identity Provider (IdP)]]** — The organization that authenticates users and vouches for their identity
- **[[immutable-infrastructure|Immutable infrastructure]]** — servers are never modified after deployment; updates create new instances that replace old ones
- **[[impact|Impact]]** — Session cookie theft, account hijacking, defacement, keylogging, phishing via injected forms; unauthorized actions as authenticated user
- **[[impact-categories|Impact categories]]** — financial loss, reputational damage, regulatory penalties, safety, operational disruption
- **[[implicit-deny|Implicit deny]]** — If no rule explicitly grants access, access is denied by default
- **[[implicit-trust-zones|Implicit trust zones]]** — Zero Trust aims to eliminate these; every zone is treated as untrusted by default
- **[[indicators-of-attack-ioa|Indicators of Attack (IoA)]]** — Proactive behavioral signals suggesting an attack is in progress (more real-time than IoCs)
- **[[industry-standards|Industry standards]]** — voluntary or contractually required frameworks (PCI DSS, ISO 27001, NIST CSF)
- **[[influence-campaigns|Influence campaigns]]** — Large-scale disinformation operations to manipulate public opinion
- **[[information-sharing-and-analysis-centers-isacs|Information Sharing and Analysis Centers (ISACs)]]** — Industry-specific organizations for sharing threat intelligence
- **[[infrastructure-as-code-iac|Infrastructure as Code (IaC)]]** — Managing and provisioning infrastructure through code (Terraform, Ansible, Puppet)
- **[[inherent-risk|Inherent risk]]** — risk present before any controls
- **[[inline-vs-passive-deployment|Inline vs. passive deployment]]** — IPS must be inline to block; IDS can be passive via port mirroring
- **[[input-validation|Input validation]]** — Allowlisting acceptable characters and rejecting or sanitizing everything else
- **[[insecure-protocols|Insecure protocols]]** — Using unencrypted protocols (Telnet, FTP, HTTP, SNMPv1/v2) that expose data in transit
- **[[insider-threat-awareness|Insider threat awareness]]** — recognizing behavioral indicators of potential insider threats
- **[[integer-overflow|Integer overflow]]** — Exceeding the maximum value of an integer variable, causing unexpected behavior
- **[[integration-apis|Integration APIs]]** — SOAR platforms connect to dozens of security tools to take coordinated action
- **[[integrity|Integrity]]** — Ensuring data is accurate, complete, and unaltered by unauthorized parties
- **[[intelligence-driven-hunting|Intelligence-driven hunting]]** — Using threat intelligence reports, IoCs, or known TTPs as starting points
- **[[internal-audit|Internal audit]]** — conducted by the organization
- **[[internal-vs-external-compliance|Internal vs. external compliance]]** — internal policies may exceed regulatory minimums
- **[[ip-spoofing|IP spoofing]]** — Forging the source IP address of packets to impersonate another system or hide the attacker
- **[[iso-27001-27002|ISO 27001 / 27002]]** — international standard for information security management systems (ISMS); 27001 is certifiable

## J

- **[[jamming|Jamming]]** — Flooding the wireless spectrum with noise to prevent legitimate wireless communication (DoS)
- **[[journald|journald]]** — Linux systemd journal for structured logging
- **[[jumpbox-jump-server|Jumpbox / jump server]]** — hardened system used to access management networks securely
- **[[just-in-time-jit-access|Just-in-time (JIT) access]]** — Granting privileged access only when needed and automatically revoking it after a set period

## K

- **[[kerberoasting|Kerberoasting]]** — Extracting and cracking service account ticket hashes from Active Directory
- **[[kerberos|Kerberos]]** — Ticket-based authentication protocol used in Active Directory environments; uses port 88
- **[[key-escrow|Key escrow]]** — third party holds a copy of the key for recovery; controversial due to trust implications
- **[[key-length|Key length]]** — longer keys = stronger encryption; AES-256 is the current gold standard
- **[[key-splitting-secret-sharing|Key splitting / secret sharing]]** — divide a key among multiple custodians; requires a threshold to reconstruct (Shamir
- **[[key-stretching|Key stretching]]** — Techniques (PBKDF2, bcrypt, scrypt) that make brute force against passwords computationally expensive
- **[[keylogger|Keylogger]]** — Records keystrokes to capture passwords, credit card numbers, and other sensitive input
- **[[keylogging|Keylogging]]** — Capturing passwords as users type them using hardware or software keyloggers
- **[[known-plaintext-attack|Known plaintext attack]]** — Attacker has both plaintext and corresponding ciphertext and uses them to derive the key
- **[[krack-key-reinstallation-attack|KRACK (Key Reinstallation Attack)]]** — Exploiting a flaw in WPA2

## L

- **[[labeling-and-marking|Labeling and marking]]** — applying headers, footers, watermarks, or metadata tags to classified data
- **[[lateral-movement|Lateral movement]]** — Ransomware and attackers spread across the network before detonating to maximize impact
- **[[ldap-injection|LDAP injection]]** — Manipulating LDAP queries to bypass authentication or enumerate directory information
- **[[least-functionality-principle|Least functionality principle]]** — Systems should only have the minimum capabilities needed for their role
- **[[least-privilege|Least privilege]]** — Users and processes should only have the minimum permissions necessary to perform their function
- **[[least-privilege-enforcement|Least privilege enforcement]]** — Ensuring even administrators only have access to what their role requires
- **[[legal-hold|Legal hold]]** — Directive to preserve all relevant data when litigation is anticipated
- **[[lessons-learned-post-incident-review|Lessons learned / Post-incident review]]** — Documenting what happened, what worked, what failed, and how to improve
- **[[lighting|Lighting]]** — Well-lit areas deter criminal activity and are critical for CCTV effectiveness
- **[[live-forensics-vs-dead-forensics|Live forensics vs. dead forensics]]** — Live = analyzing a running system (captures volatile data); dead = analyzing powered-off media
- **[[live-migration-security|Live migration security]]** — encrypting VM data during migration between hosts to prevent interception
- **[[locker-ransomware|Locker ransomware]]** — Locks the user out of the system entirely without necessarily encrypting files
- **[[locks|Locks]]** — Mechanical, electronic, and biometric locks as physical access control mechanisms
- **[[log-aggregation|Log aggregation]]** — Collecting logs from firewalls, servers, endpoints, applications, and cloud services into one platform
- **[[log-forwarding-agents|Log forwarding agents]]** — Software installed on endpoints to collect and send logs to central systems
- **[[log-integrity|Log integrity]]** — Protecting logs from tampering using write-once storage, hashing, or digital signatures
- **[[log-retention-policies|Log retention policies]]** — Defining how long logs are stored based on regulatory and organizational requirements
- **[[log-sources|Log sources]]** — OS event logs, firewall logs, IDS/IPS alerts, authentication logs, application logs, DNS query logs, proxy logs
- **[[logic-bomb|Logic bomb]]** — Malicious code that triggers when specific conditions are met (date, user action, system event)
- **[[logical-segmentation|Logical segmentation]]** — VLANs, subnets, and software-defined boundaries on shared infrastructure

## M

- **[[mac-flooding|MAC flooding]]** — Overwhelming a switch
- **[[maintenance-windows|Maintenance windows]]** — Scheduled periods for implementing changes with minimal user impact
- **[[man-in-the-browser-mitb|Man-in-the-Browser (MitB)]]** — Malware in the browser modifies transactions in real time (e.g., changing bank account numbers)
- **[[maximum-tolerable-downtime-mtd|Maximum Tolerable Downtime (MTD)]]** — the longest period a function can be unavailable before causing irreversible damage
- **[[mean-time-between-failures-mtbf|Mean Time Between Failures (MTBF)]]** — average time a system operates before failing
- **[[mean-time-to-repair-mttr|Mean Time to Repair (MTTR)]]** — average time to fix a failed component
- **[[memory-vulnerabilities|Memory vulnerabilities]]** — Buffer overflows, use-after-free, memory leaks that can be exploited for code execution
- **[[metamorphic-malware|Metamorphic malware]]** — Completely rewrites its own code while maintaining functionality to evade detection
- **[[metrics|Metrics]]** — phishing click rates, training completion rates, incident report volumes, time to report
- **[[metrics-and-reporting|Metrics and reporting]]** — Tracking MTTR, MTTD, analyst workload, and automation effectiveness
- **[[mfa-fatigue-attacks|MFA fatigue attacks]]** — Attackers bombard users with push notifications hoping they approve one
- **[[micro-segmentation|Micro-segmentation]]** — granular segmentation within a network, often at the workload level
- **[[misconfigurations|Misconfigurations]]** — Default settings, open ports, unnecessary services, overly permissive rules — the most common vulnerability type
- **[[mitre-attck-framework|MITRE ATT&CK framework]]** — Knowledge base of adversary tactics, techniques, and procedures (TTPs) used to structure hunts
- **[[mobile-device-management-mdm|Mobile Device Management (MDM)]]** — Centralized control of mobile endpoints — remote wipe, enforce policies, manage apps
- **[[monitoring-and-reporting|Monitoring and reporting]]** — KPIs and KRIs measure governance effectiveness and communicate risk to leadership
- **[[multitenancy-risks|Multitenancy risks]]** — data isolation between tenants; side-channel attacks; resource contention

## N

- **[[nation-state-actors|Nation-state actors]]** — Advanced Persistent Threat (APT) groups sponsored by governments with significant resources and long-term objectives
- **[[need-to-know|Need to know]]** — Access to information is restricted to those who require it for their role
- **[[netflow-sflow-ipfix|NetFlow / sFlow / IPFIX]]** — Protocols that collect metadata about network traffic flows without capturing full packets
- **[[network-segmentation|Network segmentation]]** — Dividing the network into isolated zones to limit lateral movement and blast radius
- **[[network-taps|Network taps]]** — Hardware devices that copy network traffic for monitoring without affecting the traffic flow
- **[[network-zones|Network zones]]** — segments with different trust levels (DMZ, internal, guest, management)
- **[[network-based-idsips|Network-based IDS/IPS]]** — Inline or passive devices that inspect network traffic for known attack signatures and anomalies
- **[[network-based-indicators|Network-based indicators]]** — Known malicious IPs, suspicious domains, unusual outbound connections, C2 traffic patterns
- **[[nfc-attacks|NFC attacks]]** — Eavesdropping on or manipulating Near Field Communication transactions
- **[[nist-cybersecurity-framework-csf|NIST Cybersecurity Framework (CSF)]]** — Identify, Protect, Detect, Respond, Recover; voluntary, widely adopted in the US
- **[[nist-ir-lifecycle|NIST IR lifecycle]]** — Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity
- **[[nist-sp-800-53|NIST SP 800-53]]** — comprehensive catalog of security and privacy controls for federal systems
- **[[non-persistence|Non-persistence]]** — systems rebuilt from known-good images; live boot media, revert to snapshot
- **[[non-repudiation|Non-repudiation]]** — Ensures actions cannot be denied after the fact; achieved through digital signatures and audit trails
- **[[normalization|Normalization]]** — Converting logs from different formats into a common schema for analysis
- **[[notable-examples|Notable examples]]** — WannaCry, NotPetya, LockBit, BlackCat/ALPHV — major ransomware campaigns
- **[[ntp-synchronization|NTP synchronization]]** — All systems must use the same time source — accurate timestamps are critical for event correlation

## O

- **[[oauth-20|OAuth 2.0]]** — Authorization framework for delegated access; issues access tokens (not authentication)
- **[[offboarding|Offboarding]]** — revoking access, retrieving data, and ensuring secure data destruction when a vendor relationship ends
- **[[open-design-principle|Open design principle]]** — Security mechanisms should not depend on secrecy of implementation
- **[[open-service-ports|Open service ports]]** — Unnecessary services listening on the network increase the attack surface
- **[[openid-connect|OpenID Connect]]** — Modern federation protocol built on OAuth 2.0; uses JSON Web Tokens (JWT)
- **[[openid-connect-oidc|OpenID Connect (OIDC)]]** — Authentication layer built on top of OAuth 2.0, commonly used for consumer-facing SSO
- **[[operational-intelligence|Operational intelligence]]** — Details about specific campaigns or threat actor groups to inform security teams
- **[[orchestration|Orchestration]]** — Connecting and coordinating multiple security tools (SIEM, firewalls, EDR, ticketing) through APIs
- **[[order-of-restoration|Order of restoration]]** — critical systems first, based on BIA priorities and RTO requirements
- **[[order-of-volatility|Order of volatility]]** — Collect the most volatile evidence first — CPU registers → RAM → swap → disk → logs → network → archival media

## P

- **[[packet-capture-pcap|Packet capture (PCAP)]]** — Full capture of network packets for deep analysis using tools like Wireshark or tcpdump
- **[[parameterized-queries-prepared-statements|Parameterized queries / Prepared statements]]** — The primary defense against SQL injection — separates code from data so input is never executed as SQL
- **[[pass-the-hash|Pass-the-hash]]** — Using a captured NTLM hash to authenticate without knowing the actual plaintext password
- **[[password-hashing|Password hashing]]** — uses salting and key stretching to protect stored passwords
- **[[password-spraying|Password spraying]]** — Trying a small number of common passwords against many accounts to avoid lockout thresholds
- **[[password-vaulting|Password vaulting]]** — Storing privileged credentials in an encrypted vault; users check out passwords for time-limited sessions
- **[[passwordless-authentication|Passwordless authentication]]** — FIDO2/WebAuthn, passkeys — eliminates password-related vulnerabilities entirely
- **[[patch-management|Patch management]]** — Keeping OS and applications up to date to close known vulnerabilities
- **[[patching|Patching]]** — Applying vendor-supplied fixes to close known vulnerabilities — the most fundamental mitigation
- **[[pci-dss|PCI DSS]]** — payment card industry standard; required for any organization handling cardholder data
- **[[perfect-forward-secrecy-pfs|Perfect forward secrecy (PFS)]]** — compromising long-term keys does not compromise past session keys
- **[[permission-inheritance|Permission inheritance]]** — Child objects inherit permissions from parent containers in access control systems
- **[[phases|Phases]]** — Planning/scoping → Reconnaissance → Scanning → Exploitation → Post-exploitation → Reporting
- **[[phi-protected-health-information|PHI (Protected Health Information)]]** — health-related PII governed by HIPAA
- **[[phishing|Phishing]]** — Fraudulent emails impersonating legitimate entities to steal credentials or deliver malware
- **[[phishing-simulations|Phishing simulations]]** — controlled phishing emails sent to employees to test awareness and measure click rates
- **[[physical-controls|Physical controls]]** — Locks, fences, mantraps, and security guards as physical access control mechanisms
- **[[physical-segmentation|Physical segmentation]]** — separate physical network infrastructure for different zones
- **[[pii-personally-identifiable-information|PII (Personally Identifiable Information)]]** — data that can identify an individual (name, SSN, email, biometrics)
- **[[pivoting|Pivoting]]** — Using a compromised system as a launchpad to attack internal networks
- **[[playbooksrunbooks|Playbooks/Runbooks]]** — Predefined workflows that codify incident response procedures into automated steps
- **[[policies-standards-baselines-guidelines-procedures|Policies, standards, baselines, guidelines, procedures]]** — the governance hierarchy from most authoritative to most flexible
- **[[policy-actions|Policy actions]]** — alert, block, encrypt, quarantine, log, notify manager
- **[[policy-administrator|Policy administrator]]** — Establishes and removes communication paths based on policy engine decisions in Zero Trust
- **[[policy-as-code|Policy as code]]** — defining security policies in code that automatically validates IaC templates before deployment
- **[[policy-enforcement-point-pep|Policy enforcement point (PEP)]]** — Gateway that enforces access decisions at the data plane level in Zero Trust
- **[[policy-engine|Policy engine]]** — Evaluates access requests against policies, risk signals, and threat intelligence in Zero Trust
- **[[policy-lifecycle|Policy lifecycle]]** — create, approve, distribute, enforce, review, revise, retire
- **[[polymorphic-malware|Polymorphic malware]]** — Changes its code signature with each infection to evade signature-based detection
- **[[port-mirroring-span|Port mirroring (SPAN)]]** — Switch feature that copies traffic from one port to a monitoring port
- **[[port-scanning|Port scanning]]** — Enumerating open ports and services on target systems during the reconnaissance phase
- **[[potentially-unwanted-programs-pups|Potentially Unwanted Programs (PUPs)]]** — Adware, toolbars, and bundled software that degrades security without being strictly malicious
- **[[preparation|Preparation]]** — Building the IR team, creating playbooks, deploying tools, conducting tabletop exercises
- **[[pretexting|Pretexting]]** — Creating a fabricated scenario to gain trust and extract information from a target
- **[[preventive-detective-corrective|Preventive, Detective, Corrective]]** — Security controls categorized by when they act relative to an incident
- **[[principle-of-least-privilege|Principle of least privilege]]** — Grant only the minimum access necessary for a role or task
- **[[privacy-by-design|Privacy by design]]** — embedding privacy controls into systems from the beginning, not as an afterthought
- **[[privacy-impact-assessment-pia|Privacy Impact Assessment (PIA)]]** — evaluates how a project or system will affect individual privacy
- **[[privilege-escalation|Privilege escalation]]** — Exploiting flaws to gain higher-level access (vertical) or access other users
- **[[privileged-accounts|Privileged accounts]]** — Service accounts, admin accounts, and root accounts require additional controls
- **[[protocol-analysis|Protocol analysis]]** — Inspecting traffic to detect protocol misuse or tunneling (e.g., DNS tunneling for data exfiltration)
- **[[protocol-attacks|Protocol attacks]]** — Exploiting protocol weaknesses to consume server resources (SYN flood, Ping of Death, Smurf attack)
- **[[provisioning-and-deprovisioning|Provisioning and deprovisioning]]** — Creating, modifying, and removing user accounts throughout the identity lifecycle
- **[[pseudonymization|Pseudonymization]]** — replaces identifiers with pseudonyms; reversible with a key
- **[[push-notifications|Push notifications]]** — Authentication apps send approve/deny prompts to registered devices

## Q

- **[[qualitative-risk-assessment|Qualitative risk assessment]]** — uses subjective ratings (high, medium, low) based on expert judgment; faster but less precise
- **[[qualitative-vs-quantitative-analysis|Qualitative vs. quantitative analysis]]** — qualitative uses categories (high/medium/low); quantitative uses dollar values (SLE, ALE, ARO)
- **[[quantitative-risk-assessment|Quantitative risk assessment]]** — uses numerical values and formulas; more precise but requires reliable data
- **[[quantum-computing-threat|Quantum computing threat]]** — Shor

## R

- **[[race-condition-toctou|Race condition / TOCTOU]]** — Exploiting the timing gap between checking a condition and using the result
- **[[race-conditions|Race conditions]]** — Timing-dependent flaws where concurrent processes can interfere with each other
- **[[radius|RADIUS]]** — UDP-based AAA protocol that encrypts only the password; commonly used for Wi-Fi and VPN authentication
- **[[rainbow-table-attack|Rainbow table attack]]** — Using precomputed hash-to-password lookup tables to crack hashed passwords quickly
- **[[ransomware-as-a-service-raas|Ransomware-as-a-Service (RaaS)]]** — Criminal developers provide ransomware tools to affiliates in exchange for a cut of profits
- **[[rat-remote-access-trojan|RAT (Remote Access Trojan)]]** — Gives attackers full remote control of a compromised system
- **[[real-time-alerting|Real-time alerting]]** — Immediate notification when correlation rules or thresholds are triggered
- **[[reconnaissance|Reconnaissance]]** — Passive (OSINT, DNS lookups) and active (port scanning, service enumeration) information gathering
- **[[recovery|Recovery]]** — Restoring systems to normal operations, monitoring for re-infection
- **[[recovery-point-objective-rpo|Recovery Point Objective (RPO)]]** — the maximum acceptable data loss measured in time (e.g., 4 hours of transactions)
- **[[recovery-time-objective-rto|Recovery Time Objective (RTO)]]** — the target time to restore a function after disruption; must be less than MTD
- **[[red-team-vs-pen-test|Red team vs. pen test]]** — Red teams simulate real adversaries over extended periods; pen tests are time-boxed technical assessments
- **[[reflected-xss|Reflected XSS]]** — Malicious script in a URL parameter is reflected back in the server
- **[[registry-and-gpo-hardening|Registry and GPO hardening]]** — Windows Group Policy Objects enforce security settings across domains
- **[[regulatory-audit|Regulatory audit]]** — mandated by a governing body (e.g., PCI QSA audit for PCI DSS compliance)
- **[[regulatory-compliance|Regulatory compliance]]** — meeting requirements imposed by law (GDPR, HIPAA, SOX, GLBA, FERPA)
- **[[relay-attacks|Relay attacks]]** — Forwarding authentication exchanges between a victim and a legitimate service (common with NFC/RFID)
- **[[remediation-network|Remediation network]]** — quarantine VLAN where non-compliant devices are placed to receive updates
- **[[remediation-vs-mitigation|Remediation vs. mitigation]]** — Remediation fixes the vulnerability; mitigation reduces the risk without fully eliminating it
- **[[remove-default-accounts-and-passwords|Remove default accounts and passwords]]** — Default credentials are publicly known and easily exploited
- **[[replay-attack|Replay attack]]** — Capturing and retransmitting valid network traffic to gain unauthorized access or duplicate transactions
- **[[replication|Replication]]** — real-time or near-real-time copying of data to a secondary location
- **[[residual-risk|Residual risk]]** — risk remaining after controls are applied
- **[[resource-contention|Resource contention]]** — VMs competing for shared CPU, memory, storage, and network resources
- **[[resource-exhaustion|Resource exhaustion]]** — Consuming all available memory, CPU, disk, or connections to cause denial of service
- **[[retention-and-archival|Retention and archival]]** — Storing log data for compliance requirements and forensic investigations
- **[[revocation|Revocation]]** — CRL or OCSP; reasons include key compromise, CA compromise, or affiliation change
- **[[rfid-cloning|RFID cloning]]** — Copying RFID badge data to create unauthorized duplicate access cards
- **[[right-to-audit|Right to audit]]** — contractual clause allowing the organization to audit the vendor
- **[[rights-management-drmirm|Rights management (DRM/IRM)]]** — controls that persist with the data (who can view, edit, print, forward)
- **[[risk-threat-x-vulnerability-x-impact|Risk = Threat x Vulnerability x Impact]]** — all three factors must be present for risk to exist
- **[[risk-appetite-vs-risk-tolerance|Risk appetite vs. risk tolerance]]** — appetite is the overall willingness to take risk; tolerance is the acceptable deviation from appetite
- **[[risk-identification|Risk identification]]** — asset inventory, threat modeling, vulnerability scanning
- **[[risk-matrix-heat-map|Risk matrix / heat map]]** — visual tool plotting likelihood vs. impact
- **[[risk-register|Risk register]]** — a living document tracking identified risks, owners, responses, and status
- **[[risk-based-prioritization|Risk-based prioritization]]** — Considering exploit availability, asset criticality, and exposure when deciding remediation order
- **[[risks|Risks]]** — Automation of bad processes amplifies mistakes; credential management for automated tools; single point of failure
- **[[rogue-access-point|Rogue access point]]** — Unauthorized AP connected to the corporate network, creating a backdoor past perimeter security
- **[[rogue-dhcp-server|Rogue DHCP server]]** — Unauthorized DHCP server providing malicious gateway or DNS settings to clients
- **[[role-based-access-control-rbac|Role-Based Access Control (RBAC)]]** — Assigning permissions based on job roles rather than individual users
- **[[role-based-training|Role-based training]]** — different roles receive different training (developers learn secure coding; executives learn BEC threats)
- **[[roles-and-responsibilities|Roles and responsibilities]]** — CISO, data owner, data custodian, data steward, data processor, data controller
- **[[root-cause-analysis|Root cause analysis]]** — EDR tools trace the full attack chain from initial access to impact
- **[[rootkit|Rootkit]]** — Hides deep in the OS (kernel-level or boot-level) to maintain persistent, stealthy access
- **[[rules-of-engagement-roe|Rules of engagement (ROE)]]** — Legal document defining scope, timing, allowed techniques, and emergency contacts

## S

- **[[smime|S/MIME]]** — Certificate-based encryption and digital signing of email content
- **[[salting|Salting]]** — Adding random data to passwords before hashing to defeat rainbow table attacks
- **[[saml|SAML]]** — Most common enterprise federation protocol; uses XML assertions exchanged via browser redirects
- **[[saml-security-assertion-markup-language|SAML (Security Assertion Markup Language)]]** — XML-based standard for exchanging authentication and authorization data between an IdP and SP
- **[[sandboxing|Sandboxing]]** — using VMs as isolated environments for testing suspicious code or malware analysis
- **[[scalability|Scalability]]** — vertical (scale up: more resources) vs. horizontal (scale out: more instances)
- **[[scan-scheduling|Scan scheduling]]** — Regular scans (weekly, monthly) plus ad-hoc scans after major changes
- **[[scheduling-algorithms|Scheduling algorithms]]** — round-robin, least connections, weighted, IP hash, health-based
- **[[screen-filtersprivacy-screens|Screen filters/privacy screens]]** — Physical filters that prevent shoulder surfing by limiting viewing angles
- **[[screened-subnet-dmz|Screened subnet (DMZ)]]** — uses firewalls to create a buffer zone for public-facing services
- **[[scripting-languages|Scripting languages]]** — Bash, PowerShell, Python are the most common in security operations
- **[[secrets-management|Secrets management]]** — storing credentials, keys, and tokens securely in cloud environments
- **[[secure-access-service-edge-sase|Secure Access Service Edge (SASE)]]** — cloud-delivered convergence of network and security services
- **[[secure-areas|Secure areas]]** — Server rooms, data centers, and wiring closets requiring restricted physical access
- **[[secure-baseline-images|Secure baseline images]]** — Golden images with pre-hardened configurations for consistent deployment
- **[[secure-email-gateway|Secure email gateway]]** — Filters inbound and outbound email for spam, phishing, malware, and DLP violations
- **[[security-awareness-training|Security awareness training]]** — Educating users to recognize and respond to social engineering and phishing attacks
- **[[security-baselines-and-hardening|Security baselines and hardening]]** — Configuring systems according to CIS Benchmarks or STIGs before deployment
- **[[security-guards|Security guards]]** — Human element providing judgment-based physical access control
- **[[security-layers|Security layers]]** — From outer to inner: perimeter, network, host, application, data — the layers of defense-in-depth
- **[[security-through-obscurity|Security through obscurity]]** — Relying on secrecy of design rather than robust controls; considered insufficient on its own
- **[[self-service-capabilities|Self-service capabilities]]** — Password resets and profile updates reduce helpdesk burden while maintaining security
- **[[separation-of-duties|Separation of duties]]** — Dividing critical tasks among multiple people to prevent fraud and detect errors
- **[[server-side-request-forgery-ssrf|Server-Side Request Forgery (SSRF)]]** — Tricking the server into making requests to internal resources on behalf of the attacker
- **[[service-account-management|Service account management]]** — Tracking and securing non-human accounts used by applications and scripts
- **[[service-level-agreements-slas|Service Level Agreements (SLAs)]]** — contractual terms defining uptime, response times, and security obligations
- **[[service-provider-sp|Service Provider (SP)]]** — The organization that accepts identity assertions from the IdP
- **[[session-hijacking|Session hijacking]]** — Stealing or predicting a valid session token to impersonate an authenticated user
- **[[session-recording|Session recording]]** — Recording all actions taken during privileged sessions for audit and forensic purposes
- **[[session-replay|Session replay]]** — Capturing and retransmitting a valid authentication exchange to gain unauthorized access
- **[[shared-responsibility-model|Shared responsibility model]]** — security \
- **[[shoulder-surfing|Shoulder surfing]]** — Physically observing someone entering their password or viewing sensitive information
- **[[side-channel-attacks|Side-channel attacks]]** — Exploiting physical characteristics (timing, power, EM emissions) rather than algorithmic weaknesses
- **[[single-point-of-failure-spof|Single point of failure (SPOF)]]** — any component whose failure would bring down an entire system
- **[[single-point-of-failure-risk|Single point of failure risk]]** — If SSO is compromised, all linked applications are at risk
- **[[single-factor-authentication-sfa|Single-factor authentication (SFA)]]** — Uses one authentication factor; least secure authentication method
- **[[slowloris|Slowloris]]** — Keeps many HTTP connections open by sending partial headers, exhausting the server
- **[[smishing|Smishing]]** — SMS-based phishing via text messages
- **[[smurf-attack|Smurf attack]]** — Sending ICMP echo requests with spoofed source (victim
- **[[snapshot-management|Snapshot management]]** — snapshots capture VM state; old snapshots may contain outdated or vulnerable configurations
- **[[snmp-simple-network-management-protocol|SNMP (Simple Network Management Protocol)]]** — Used to monitor and manage network devices; SNMPv3 adds encryption and authentication
- **[[soc-reports|SOC reports]]** — SOC 1 (financial controls), SOC 2 (security/availability/confidentiality), SOC 3 (public summary)
- **[[software-defined-networking-sdn|Software-Defined Networking (SDN)]]** — programmatic control of network infrastructure; separates control plane from data plane
- **[[software-defined-perimeter-sdp|Software-defined perimeter (SDP)]]** — Creates one-to-one encrypted connections between users and resources; hides infrastructure
- **[[something-you-are|Something you are]]** — Biometrics — fingerprint, facial recognition, iris scan, voice recognition
- **[[something-you-do|Something you do]]** — Behavioral biometrics such as typing patterns or gait analysis (less common on exam)
- **[[something-you-have|Something you have]]** — Smart cards, hardware tokens (YubiKey), mobile authenticator apps, OTP devices
- **[[something-you-know|Something you know]]** — Passwords, PINs, security questions
- **[[somewhere-you-are|Somewhere you are]]** — Geolocation or IP-based restrictions (sometimes considered a factor)
- **[[sox-sarbanes-oxley|SOX (Sarbanes-Oxley)]]** — US law requiring financial reporting integrity and internal controls
- **[[spf-sender-policy-framework|SPF (Sender Policy Framework)]]** — DNS TXT record that specifies which mail servers are authorized to send email for a domain
- **[[spyware|Spyware]]** — Secretly monitors user activity, capturing keystrokes, screenshots, or browsing habits
- **[[sql-injection-sqli|SQL injection (SQLi)]]** — Inserting SQL commands into input fields to manipulate database queries — can read, modify, or delete data
- **[[ssltls-interception-ssl-proxy|SSL/TLS interception (SSL proxy)]]** — Using a trusted certificate to decrypt, inspect, and re-encrypt TLS traffic
- **[[ssltls-offloading|SSL/TLS offloading]]** — load balancer handles encryption/decryption, reducing server workload
- **[[ssltls-stripping|SSL/TLS stripping]]** — Downgrading an HTTPS connection to HTTP so the attacker can read traffic in plaintext
- **[[stig-security-technical-implementation-guide|STIG (Security Technical Implementation Guide)]]** — DoD-specific hardening standards for government systems
- **[[stix-structured-threat-information-expression|STIX (Structured Threat Information eXpression)]]** — Standardized language for describing cyber threat information
- **[[stixtaxii|STIX/TAXII]]** — Standards for formatting (STIX) and sharing (TAXII) IoC data between organizations
- **[[stored-persistent-xss|Stored (Persistent) XSS]]** — Malicious script permanently stored on the server — affects all users who view the infected content
- **[[stored-procedures|Stored procedures]]** — Pre-compiled database queries that can limit injection surface when used correctly
- **[[strategic-intelligence|Strategic intelligence]]** — High-level trends and risks for executive decision-making
- **[[succession-planning|Succession planning]]** — ensuring leadership continuity if key personnel are unavailable
- **[[supply-chain-risk|Supply chain risk]]** — compromised hardware, software, or services introduced through the supply chain (e.g., SolarWinds)
- **[[syn-flood|SYN flood]]** — Sending many TCP SYN packets without completing the handshake, filling the target
- **[[syslog|Syslog]]** — Standard protocol (UDP 514, TCP 514, or TLS 6514) for transmitting log data to a centralized server

## T

- **[[tabletop-exercises|Tabletop exercises]]** — Discussion-based simulations that walk through IR scenarios without touching systems
- **[[tacacs|TACACS+]]** — TCP-based AAA protocol that encrypts the entire payload; separates AAA functions independently
- **[[tactical-intelligence|Tactical intelligence]]** — TTPs (tactics, techniques, procedures) used by adversaries — informs detection rules
- **[[tailgatingpiggybacking|Tailgating/Piggybacking]]** — Following an authorized person through a secured door without independent authentication
- **[[taxii-trusted-automated-exchange-of-intelligence-information|TAXII (Trusted Automated eXchange of Intelligence Information)]]** — Protocol for exchanging STIX data
- **[[technical-controls|Technical controls]]** — Firewalls, encryption, access control systems, IDS — technology-based security mechanisms
- **[[technical-intelligence|Technical intelligence]]** — Specific IoCs — IP addresses, file hashes, domain names — fed into security tools
- **[[telemetry-correlation-xdr|Telemetry correlation (XDR)]]** — Combines data from endpoints, network, cloud, and email to detect multi-vector attacks
- **[[testing-the-drp|Testing the DRP]]** — same test types as BCP (tabletop, simulation, parallel, full interruption)
- **[[testing-types|Testing types]]** — Black box (no prior knowledge), white box (full knowledge), gray box (partial knowledge)
- **[[third-partysupply-chain-risks|Third-party/supply chain risks]]** — Vulnerabilities in vendor software, libraries, or dependencies (e.g., Log4Shell)
- **[[threat-actor-profiling|Threat actor profiling]]** — Understanding adversary motivation, capability, and intent
- **[[threat-assessment|Threat assessment]]** — evaluating threat sources and their capabilities
- **[[threat-containment|Threat containment]]** — Ability to isolate a compromised endpoint from the network in real time
- **[[threat-feeds|Threat feeds]]** — Automated IoC data streams from commercial and open-source providers for security monitoring
- **[[threat-intelligence-enrichment|Threat intelligence enrichment]]** — Automatically querying threat feeds to add context to alerts before analysts review them
- **[[threat-intelligence-integration|Threat intelligence integration]]** — EDR/XDR platforms cross-reference activity with known threat indicators
- **[[timeline-analysis|Timeline analysis]]** — Reconstructing the sequence of events using file timestamps, logs, and artifacts
- **[[token-based-authentication|Token-based authentication]]** — SSO systems issue tokens (JWT, SAML assertions) that prove identity to relying parties
- **[[tokenization|Tokenization]]** — replaces sensitive data with non-sensitive tokens; original data stored in a secure vault
- **[[totp-time-based-one-time-password|TOTP (Time-based One-Time Password)]]** — Algorithm that generates codes valid for a short time window (e.g., Google Authenticator)
- **[[training-frequency|Training frequency]]** — onboarding training plus regular refreshers (annual at minimum, quarterly preferred)
- **[[transitive-trust|Transitive trust]]** — If A trusts B and B trusts C, A may transitionally trust C — this can introduce risk
- **[[triple-extortion|Triple extortion]]** — Adds DDoS attacks or contacting victims
- **[[trojan|Trojan]]** — Malware disguised as legitimate software; provides backdoor access or delivers additional payloads
- **[[trust-relationships|Trust relationships]]** — Formal agreements between identity providers and service providers defining how identity data is shared
- **[[trusted-platform-module-tpm|Trusted Platform Module (TPM)]]** — chip on the motherboard that stores keys and supports measured boot
- **[[tuning|Tuning]]** — adjusting sensitivity and rules to reduce false positives without increasing false negatives
- **[[typosquatting|Typosquatting]]** — Registering domains similar to legitimate ones to capture mistyped URLs
- **[[typosquatting-url-hijacking|Typosquatting / URL hijacking]]** — Registering look-alike domains (e.g., googel.com) to capture users who mistype URLs

## U

- **[[unified-threat-management-utm|Unified Threat Management (UTM)]]** — all-in-one appliance combining firewall, IDS/IPS, antivirus, content filtering, VPN
- **[[unpatched-software|Unpatched software]]** — Known vulnerabilities with available fixes that have not been applied — one of the most exploited vulnerability types
- **[[use-cases|Use cases]]** — specific automation scenarios: user provisioning, alert triage, patch deployment, threat containment
- **[[user-and-entity-behavior-analytics-ueba|User and Entity Behavior Analytics (UEBA)]]** — uses ML to baseline normal user/entity behavior and detect anomalies indicating insider threats or compromise

## V

- **[[vendor-assessment|Vendor assessment]]** — questionnaires, on-site audits, penetration test results, and SOC reports used to evaluate vendor security
- **[[vendor-diversity|Vendor diversity]]** — Using products from multiple vendors so a vulnerability in one doesn
- **[[vendor-lock-in|Vendor lock-in]]** — dependency risk when switching providers is costly or technically difficult
- **[[version-control|Version control]]** — Tracking changes to configurations, code, and documentation for accountability and rollback
- **[[video-surveillance-cctv|Video surveillance (CCTV)]]** — Continuous monitoring and recording of facility areas for physical security
- **[[virtual-network-security|Virtual Network Security]]** — Virtual switches, virtual firewalls, and micro-segmentation within virtualized environments
- **[[virus|Virus]]** — Requires a host file to execute; spreads when the infected file is opened or executed
- **[[vishing|Vishing]]** — Voice-based phishing via phone calls to trick victims into revealing information
- **[[vlan-hopping|VLAN hopping]]** — Exploiting trunk port configurations to access traffic on VLANs other than the attacker
- **[[vlans-virtual-lans|VLANs (Virtual LANs)]]** — logically separate broadcast domains on a single switch; require a router or Layer 3 switch to route between VLANs
- **[[vm-escape|VM escape]]** — attacker breaks out of a VM and accesses the hypervisor or other VMs; a critical virtualization threat
- **[[vm-isolation|VM isolation]]** — ensuring one VM cannot access another VM
- **[[vm-sprawl|VM sprawl]]** — uncontrolled proliferation of VMs that become unpatched, unmonitored, and forgotten security liabilities
- **[[volumetric-attacks|Volumetric attacks]]** — Flooding the target with massive traffic to saturate bandwidth (UDP floods, ICMP floods)
- **[[vpn-concentrator|VPN concentrator]]** — dedicated device that terminates large numbers of VPN tunnels, centralizing remote access management
- **[[vulnerability-assessment|Vulnerability assessment]]** — identifying weaknesses that could be exploited
- **[[vulnerability-scanning|Vulnerability scanning]]** — automated probing of systems to identify known vulnerabilities, misconfigurations, and missing patches

## W

- **[[war-driving|War driving]]** — Scanning for wireless networks while moving through an area to map vulnerable access points
- **[[watering-hole-attack|Watering hole attack]]** — Compromising a website frequently visited by the target group to infect visitors
- **[[weak-encryption|Weak encryption]]** — Using deprecated algorithms (DES, MD5, SHA-1, RC4) or insufficient key lengths
- **[[windows-event-log|Windows Event Log]]** — built-in Windows logging system capturing security, system, and application events; critical for SIEM ingestion
- **[[worm|Worm]]** — Self-replicating malware that spreads across networks without user interaction
- **[[wpawpa2-handshake-capture|WPA/WPA2 handshake capture]]** — Capturing the 4-way handshake to perform offline brute-force password cracking
- **[[wps-attacks|WPS attacks]]** — Exploiting Wi-Fi Protected Setup PIN vulnerability to recover the WPA key
- **[[write-blockers|Write blockers]]** — hardware or software devices that prevent any writes to digital evidence media, preserving forensic integrity
- **[[ws-federation|WS-Federation]]** — web services federation standard for sharing identity across security domains using passive and active profiles

## X

- **[[x509-certificate-fields|X.509 certificate fields]]** — subject, issuer, serial number, validity period, public key, signature algorithm, and extensions
- **[[xml-injection-xxe|XML injection / XXE]]** — Injecting malicious XML to read files, perform SSRF, or cause denial of service

## Z

- **[[zero-trust-architecture|Zero trust architecture]]** — never trust, always verify; authenticate and authorize every access request regardless of network location
- **[[zero-day-vulnerabilities|Zero-day vulnerabilities]]** — Flaws unknown to the vendor with no available patch — exploits are highly valued by attackers
