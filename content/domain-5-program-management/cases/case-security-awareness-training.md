---
title: "Case: The Phishing Epidemic — Awareness Training Redesigned"
description: "Phishing simulations reveal a 38% click rate across the organization, with sales team at 52%, triggering a complete training program redesign."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

CloudScale is a mid-market SaaS company with 520 employees split across sales, engineering, operations, and customer success teams. In January 2025, the Chief Information Security Officer, Patricia Torres, decided to conduct a comprehensive [[phishing-simulations]] exercise. She wanted to understand how many employees would fall for a realistic phishing attack.

The company had been conducting quarterly security awareness training for three years. Every employee had completed the annual training module "Email Security and Phishing Awareness"—a 20-minute video-based course with a 15-question quiz. The training covered warning signs of phishing, how to report suspicious emails, and the importance of not clicking suspicious links.

Patricia engaged an external security firm (Proofpoint) to conduct a phishing simulation campaign. Over two weeks, they sent 1,800 simulated phishing emails to employees across all departments. The emails were realistic: some spoofed email addresses to look like they came from internal systems (fake "password reset required" emails), some used executive impersonation (fake CEO requesting urgent wire transfer), some claimed to be from well-known services (Amazon, Microsoft, Slack).

The results were alarming:
- **Overall click rate: 38%** (684 out of 1,800 employees clicked phishing links)
- **Sales department: 52% click rate** (182 out of 350 sales staff)
- **Customer Success: 36% click rate**
- **Engineering: 12% click rate**
- **Operations: 28% click rate**

Patricia broke down the data further. The types of emails with highest click rates were:
- Executive impersonation (CEO asking for urgent payments): 44% click rate
- Password reset spoofs: 41% click rate
- Package delivery failures: 39% click rate
- DocuSign signature requests: 38% click rate

By role, the vulnerability pattern was clear:
- **Sales staff**: 52% click rate (high urgency, client-focused, less technical)
- **Finance/accounting**: 44% click rate (transaction-focused, interact with payment systems)
- **HR**: 38% click rate (employee-focused, deal with credential changes)
- **Engineering**: 12% click rate (technically sophisticated, aware of attack vectors)
- **Security team**: 3% click rate

Patricia presented the findings to the executive team. The reaction was shocked. One quarter of the company was actively vulnerable to a basic phishing attack that could lead to credential compromise, wire fraud, or ransomware infection.

The Chief Operating Officer immediately asked: "Why is the current training not working?"

Patricia recognized the issue: the existing training was generic. Everyone watched the same 20-minute video, took the same quiz, and thought they were done. But the actual risks employees faced varied dramatically by role:

- **Sales staff** get spammed with urgent customer requests, deal with payment discussions, and are trained to act fast. They're high-risk targets for executive impersonation and payment fraud.
- **Finance staff** regularly handle wire transfers and invoices. They're targets for payment manipulation.
- **HR staff** manage employee data and credential changes. They're targets for social engineering.
- **Engineering staff** are targets for credential compromise (to access code) and supply chain attacks.
- **Customer Success staff** manage customer accounts and may have access to customer data. They're targets for account compromise.

Patricia proposed a complete redesign of the security awareness program:

**New [[training-frequency]] and [[role-based-training]] approach:**

1. **Sales team** (52% baseline vulnerability):
   - Monthly role-specific training modules on executive impersonation, payment fraud, and urgency tactics
   - Scenario-based training: "Your VP urgently needs $50K for a deal. Who do you verify with?"
   - Quarterly simulations specific to sales attack vectors
   - Individual feedback: "You clicked this type of email; here's what you should have done"
   - Incentive: "Sales team with lowest click rate wins lunch"

2. **Finance team** (44% baseline vulnerability):
   - Bi-weekly alerts about trending payment fraud schemes
   - Approval process review: "Before wiring money, verify with phone call to known number"
   - Quarterly simulations of invoice fraud, spoofed vendor emails, payment manipulation
   - Collaboration with accounts payable: "Here's how to verify payment requests"

3. **HR team** (38% baseline vulnerability):
   - Monthly training on credential compromise and social engineering
   - Process verification: "Before resetting a password, verify the request through secondary channel"
   - Simulations of credential reset requests, employee data requests

4. **Engineering team** (12% baseline vulnerability—low risk, but not ignored):
   - Focus on supply chain attacks and code repository compromise rather than phishing
   - Quarterly training on protecting SSH keys, API tokens, and source code access
   - Simulations of compromised dependency alerts and malicious package submissions

5. **Everyone else** (28-36% baseline vulnerability):
   - Monthly awareness newsletter highlighting trending attack types
   - Quarterly simulations
   - Annual comprehensive training

**Gamification approach:**

Patricia implemented a point system:
- Successfully report a phishing email to the security team: +10 points
- Complete a [[role-based-training]] module: +5 points
- Don't click on a simulation phishing email: +1 point per simulation

Employees accumulated points toward rewards: gift cards, extra PTO, preferred parking.

**Metrics and [[metrics]] tracking:**

Monthly metrics tracked by department:
- Click rate on phishing simulations (trend down)
- Reported phishing emails (trend up)
- Training completion rate (maintain 100%)
- Awareness scores on spot-check quizzes

**[[Insider-threat-awareness]] integration:**

The program also integrated insider threat education:
- What to do if you notice suspicious peer behavior
- How to handle accidental data exposure
- Reporting processes for policy violations

**[[Culture-of-security]] building:**

Patricia launched a "Security Champion" program where selected employees from each department received enhanced training and became ambassadors for their teams. These champions received exclusive training sessions, early warning about emerging threats, and recognition in company all-hands meetings.

After six months of the new program:
- Overall click rate: Down to 22% (from 38%)
- Sales team click rate: Down to 28% (from 52%)
- Finance team click rate: Down to 18% (from 44%)
- Reported phishing emails: Up from average 2/month to 35/month

The program wasn't perfect—some employees still clicked phishing emails. But the trend was moving in the right direction, and, more importantly, the organization was developing [[culture-of-security]]. People were thinking about security in their daily work, not just during the annual training requirement.

The executive team was impressed enough to allocate additional budget for the program. A year later, when the board asked about cybersecurity metrics, the CISO could present trending phishing awareness scores and incident data showing that credential compromise attempts had dropped significantly.

## What Went Right

- **Role-based approach**: Rather than treating all employees the same, training was tailored to the actual risks employees faced in their roles.
- **[[Phishing-simulations]] as ongoing feedback**: Instead of annual testing, simulations became a regular learning tool with immediate feedback.
- **Gamification for engagement**: The point system and rewards made security training something people engaged with, not something they endured.
- **[[Insider-threat-awareness]] integrated**: Training included reporting mechanisms for suspicious peer behavior, helping catch threats early.
- **[[Metrics]] demonstrated value**: Quarterly metrics showed improvement, which justified continued investment and helped build [[culture-of-security]].
- **Security Champions program**: Elevating peer ambassadors created grassroots security culture that top-down training alone couldn't achieve.

## What Could Go Wrong

- **One-size-fits-all training**: If Patricia had kept the generic 20-minute video that "worked for everyone," click rates would have remained high. Role matters enormously.
- **Training without reinforcement**: If the new program had been training without ongoing [[phishing-simulations]], people would forget what they learned within weeks.
- **No [[metrics]]**: If Patricia hadn't tracked click rates by department and shown improvement, the program would have been hard to justify to budget-conscious executives.
- **No consequences for repeated failures**: If employees could click phishing emails repeatedly with no feedback or retraining, behavior wouldn't change. Feedback loops are essential.
- **Culture imposed top-down**: If the program had been "mandatory training" without gamification and champion programs, it would have felt like punishment rather than building [[culture-of-security]].

## Key Takeaways

- **[[Role-based-training]] is more effective than generic training**: Tailor content to the actual risks people face. Sales needs to know executive impersonation; finance needs to know payment fraud; engineering needs to know supply chain attacks.
- **[[Phishing-simulations]] must be followed by education, not punishment**: When someone clicks a phishing email, the goal is to teach, not shame. Provide immediate feedback explaining the attack and how to recognize it.
- **[[Training-frequency]] matters more than length**: A 60-minute annual course is less effective than monthly 5-minute modules with quarterly simulations. Frequency builds muscle memory.
- **[[Gamification]] drives engagement**: Point systems, rewards, and competition motivate people to engage with security training. It becomes something they want to do, not something they have to do.
- **[[Culture-of-security]] is built through peer influence**: Security Champions and ambassador programs create grassroots culture change that top-down mandates can't achieve. Empower people to be security advocates in their teams.

## Related Cases

- [[case-social-engineering]] — Understanding the attacker techniques that training should prepare people to resist
- [[case-security-policies]] — Policy enforcement that training supports
- [[case-governance]] — Board-level understanding of security awareness metrics
