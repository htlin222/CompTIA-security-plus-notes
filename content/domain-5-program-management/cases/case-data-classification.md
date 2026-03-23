---
title: "Case: The Uncharted Data Ocean — Classification Crisis at Scale"
description: "A biotech firm's internal data discovery scan finds 14TB of unlabeled research data, including what appears to be export-controlled information shared with international collaborators."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

Neuravance Biotech is a $80M computational biology startup based in Cambridge, Massachusetts, developing machine learning models to predict protein folding for drug discovery. The company has 180 employees across four offices and maintains intellectual property that represents nearly its entire valuation. On a Tuesday morning in late January, the Chief Information Officer, Dr. Sarah Kim, received an unexpected email from the VP of Research asking a simple question: "What's our [[data-classification]] policy for research data?"

Sarah realized that Neuravance, despite being a decade old and managing some of the most sensitive data in drug development (pre-patent research, clinical trial data, government grant collaboration details), had never formally implemented a [[data-classification]] system. She commissioned an internal data discovery scan using Stormshield DataSecure, expecting to find maybe 2-3 terabytes of data scattered across file servers and cloud storage.

The scan completed in 72 hours. The results were staggering: **14.2 terabytes of data** across approximately 9,847 files in 300+ SharePoint sites, 47 departmental file shares, and various cloud applications like Box and OneDrive. The security team began the thankless task of trying to understand what any of it meant.

What they found sent chills through the executive team:

1. **Unclassified export-controlled research**: In a SharePoint site labeled "US-Japan Collaboration Q4 2024," the team discovered detailed molecular structure data and machine learning model weights that appeared to match the Export Control Classification Number (ECCN) category for controlled biological/chemical technologies. This data had been shared with four Japanese researchers at the University of Tokyo and Kyoto University via shared links. No [[handling-procedures]] documentation existed. No export approval process had been followed.

2. **Mingled sensitive and non-sensitive data**: Many sites contained a chaotic mix of [[commercial-private-sector-classifications]] levels. A single SharePoint containing board minutes (confidential), employee email addresses (internal), and pre-clinical trial designs (extremely restricted) was accessible to anyone in the organization and several contractors.

3. **Missing [[labeling-and-marking]]**: Of the 14.2TB scanned, approximately 96% had zero classification labels. Files were named things like "Final_Data_v3_REAL.xlsx" with no indication of sensitivity level, ownership, handling requirements, or required access controls.

4. **Contractor and collaborator access**: The scan revealed that seven external researchers, three contract manufacturers, and two consulting firms had access to SharePoint sites containing [[data-protection]]-sensitive information. Nobody had documented what data each party was supposed to access, what [[handling-procedures]] they were supposed to follow, or when their access should terminate.

Sarah immediately escalated to the Chief Legal Officer, Marcus Webb. They brought in outside counsel specializing in export control compliance. The assessment was grim: the potential export violations alone could trigger an investigation by the Department of Commerce Bureau of Industry and Security (BIS). The company could face fines up to $300,000 per violation and potential criminal charges if the violations were deemed willful.

The team pivoted to crisis mode:

1. **Immediate access quarantine**: All external researcher access to the Japan collaboration site was revoked pending review.

2. **Data inventory and [[classification-criteria]] definition**: Sarah worked with research, legal, and the export control consultant to define five classification levels:
   - **Public**: Marketing materials, published research, press releases
   - **Internal**: Employee directories, internal policies, process documentation
   - **Confidential**: Customer data, business financials, non-patented research
   - **Restricted**: Pre-patent research, active clinical trial data, export-controlled information
   - **Highly Restricted**: Board-level strategic data, trade secrets, pending patent applications

3. **Retroactive [[declassification]] and [[labeling-and-marking]]**: The team began the painstaking process of reviewing the 14.2TB and applying appropriate classifications. They wrote a Python script to extract file metadata, created a prioritization matrix based on sensitivity and business value, and systematically reviewed and tagged files.

4. **Export control assessment**: The external counsel conducted a formal review of the Japan collaboration data. While violations appeared to have occurred, the university researchers were classified as non-proliferation-risk parties, and the research was ultimately determined to be dual-use but not strictly controlled under current export regulations. The violations were reported to BIS proactively with a commitment to remediation, likely avoiding enforcement action.

5. **[[Data-protection]] and [[handling-procedures]]**: New policies were implemented requiring classification at file creation, [[labeling-and-marking]] with metadata tags, and access control enforcement tied to classification levels.

Six months later, Neuravance had a complete data inventory with formal classifications. All external researcher access was governed by documented agreements specifying exactly what data could be accessed and under what [[handling-procedures]]. The company implemented a [[data-states]] policy ensuring that classified data couldn't be exported to personal cloud storage or printed without audit logging.

## What Went Right

- **Proactive discovery rather than forensic incident response**: Sarah commissioned the scan before a breach or regulatory notice forced it. That gave the company time to remediate, report voluntarily to BIS, and avoid escalated enforcement.
- **Escalation and legal engagement**: The team didn't try to handle export control issues internally. Engaging outside counsel and voluntary reporting to regulators transformed potential violations into evidence of good compliance culture.
- **Comprehensive [[classification-criteria]]**: The five-level system was detailed enough to drive different [[handling-procedures]] but simple enough for researchers to actually use.
- **Systematic [[labeling-and-marking]] execution**: Rather than asking researchers to retroactively classify 14TB, the security team did the heavy lifting with scripted analysis and reviewed edge cases manually.

## What Could Go Wrong

- **No [[data-protection]] baseline**: Companies that don't define classification levels early end up with this exact scenario: years of accumulated data with no way to determine what's sensitive.
- **External collaborator access without [[handling-procedures]]**: Sharing intellectual property with external researchers without documented access controls and handling requirements is both a security and legal risk.
- **Missing export control awareness**: Many biotech companies don't understand that certain research data requires export control compliance. This complacency can result in willful violations.
- **[[Data-states]] without enforcement**: If classification and [[handling-procedures]] exist only in policy but aren't enforced technically (preventing email export, logging access, blocking personal cloud sync), compliance becomes advisory.
- **No remediation pathway**: If Sarah had hidden the findings rather than reported them, a later discovery would have made things exponentially worse.

## Key Takeaways

- **[[Data-classification]] must start early and be mandatory at creation**: Retroactive classification of 14TB is painful. Enforce classification as a metadata requirement when files are created.
- **[[Classification-criteria]] should tie directly to [[handling-procedures]]**: Each classification level should specify: who can access it, how it can be stored, whether it can be shared externally, how long it must be retained, and how it must be destroyed.
- **[[Government-military-classifications]] and export control require specialized expertise**: Biotech, aerospace, and defense companies must engage export control specialists. These regulations are complex and violations are severe.
- **External collaborators need [[labeling-and-marking]] and [[handling-procedures]]**: Sharing data with universities, contractors, or international partners must be governed by explicit agreements that define classification levels and required handling.
- **[[Data-states]] protection requires technical controls**: Classification in a spreadsheet doesn't prevent exfiltration. Implement DLP tools that enforce handling based on classification tags.

## Related Cases

- [[case-data-protection]] — Broader data protection strategy beyond classification
- [[case-compliance]] — How classification supports regulatory compliance requirements
- [[case-dlp]] — Technical controls that enforce classification-based handling procedures
- [[case-privacy]] — Classification as foundation for privacy-by-design approach
