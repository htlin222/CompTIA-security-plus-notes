---
title: "Threat Actors"
description: "Categories of adversaries and their motivations, capabilities, and attack methods"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/high
aliases:
  - "Threat Agents"
---

> [!eli5] ELI5: What are Threat Actors?
> Threat actors are the different kinds of "bad guys" in the computer world. Some are like professional burglars backed by a whole country's government. Some are criminals looking to steal money. Some are angry employees who already have the keys. Others are just bored kids trying to show off. Knowing which type you're dealing with helps you figure out what they're after and how to defend against them, because each group has different skills and goals.
>
> > [!eli5] ELI5: Threat Actors (繁體中文版)
> > 威脅行為者就是那些想搞破壞或偷東西的人。包括業餘駭客 (指令小子)、商業間諜、內部員工、甚至是國家級的專業組織。
> >
> > ```ascii
> > [內部威脅] <--- [系統] ---> [外部威脅]
> >                           (駭客/國家/組織)
> > ```

## Overview

Threat actors are individuals or groups that pose a risk to an organization's security. Understanding their motivations, capabilities, sophistication levels, and resources is essential for effective risk assessment and building appropriate defenses. The SY0-701 exam tests the ability to distinguish between different actor types and predict their likely tactics.

## Key Concepts

- **[[nation-state-actors|Nation-state actors]]** (APT — Advanced Persistent Threat)
  - Highest sophistication and resources; government-sponsored
  - Motivations: espionage, sabotage, political influence
  - Long dwell times; use zero-day exploits and custom malware
- **Organized crime**
  - Financially motivated; well-funded and structured
  - Ransomware, banking trojans, identity theft, fraud
- **Hacktivists**
  - Ideologically or politically motivated
  - Website defacement, DDoS, data leaks to embarrass targets
- **Insider threats**
  - Current or former employees, contractors, partners
  - May be malicious (intentional) or negligent (unintentional)
  - Hardest to detect; already have legitimate access
- **Script kiddies / unskilled attackers**
  - Low sophistication; use pre-built tools and exploit kits
  - Opportunistic rather than targeted
- **Shadow IT**
  - Employees using unauthorized technology; creates unmanaged risk
- **Attributes of threat actors**:
  - **Internal vs. External** — insider or outsider to the organization
  - **Level of sophistication** — ranges from script kiddie to APT
  - **Resources/Funding** — determines tools, persistence, and capabilities
  - **Intent/Motivation** — financial gain, espionage, disruption, ideology, revenge
- **Attack surface** — the totality of points where an attacker can try to enter (see [[attack-vectors]])
- **Wardriving** / **Warflying** — scanning for wireless networks from a moving vehicle or drone to identify vulnerable access points

## Exam Tips

> [!tip] Remember
> **Motivation mapping**: Nation-state = espionage/sabotage, Organized crime = money, Hacktivists = ideology, Insiders = revenge/negligence, Script kiddies = curiosity/notoriety.

> [!tip] Insider Threat
> Insider threats are the most dangerous because they bypass perimeter defenses. The exam often presents scenarios where an employee is the threat — look for signs of excessive access or unusual behavior.

## Connections

- Threat actors exploit [[attack-vectors]] to reach their targets
- Social engineering by threat actors is detailed in [[social-engineering]]
- Risk from threat actors is assessed and managed through [[risk-management]] and [[risk-assessment]]
- Defending against threat actors requires understanding their TTPs via [[threat-intelligence]]
- Insider threats are mitigated through [[security-awareness-training]] and [[privileged-access-management]]

## Practice Questions

> [!qbank]- Q-Bank: Threat Actors (4 Questions)
>
> **Q1.** A cybersecurity analyst discovers that an attacker has maintained persistent access to the organization's network for over 18 months, using custom-developed malware and zero-day exploits to exfiltrate intellectual property. Which threat actor type is MOST likely responsible?
>
> A. Hacktivist
> B. Script kiddie
> C. Nation-state actor (APT)
> D. Organized crime
>
> > [!answer]- Show Answer
> > **C. Nation-state actor (APT)**
> >
> > [[nation-state-actors|Nation-state actors]] (Advanced Persistent Threats) exhibit the highest sophistication, use custom malware and zero-day exploits, maintain long dwell times, and are motivated by espionage — all characteristics described in the scenario. Hacktivists are ideologically motivated and typically use disruptive tactics (DDoS, defacement) rather than long-term stealthy espionage. Script kiddies lack the sophistication to develop custom malware or discover zero-day exploits. Organized crime is financially motivated and typically seeks quick monetization, not 18 months of patient data exfiltration.
>
> **Q2.** A disgruntled former contractor who still has active VPN credentials downloads and leaks confidential customer data two weeks after their contract ends. Which threat actor attributes BEST describe this individual?
>
> A. External, low sophistication, financially motivated
> B. Internal, high sophistication, ideologically motivated
> C. Internal, varies in sophistication, revenge-motivated
> D. External, high sophistication, espionage-motivated
>
> > [!answer]- Show Answer
> > **C. Internal, varies in sophistication, revenge-motivated**
> >
> > Former contractors with active credentials are classified as [[threat-actors|insider threats]] — they are internal actors who already have legitimate access. Revenge is a common motivation for disgruntled former employees/contractors. They are not external because they have legitimate access credentials and knowledge of internal systems. The scenario does not indicate financial motivation. Espionage and high sophistication point to nation-state actors, not a single disgruntled contractor.
>
> **Q3.** A group of attackers defaces a multinational corporation's website and publishes internal emails to protest the company's environmental practices. Which threat actor category and PRIMARY motivation BEST fit this scenario?
>
> A. Nation-state actor — espionage
> B. Organized crime — financial gain
> C. Hacktivist — ideology
> D. Insider threat — revenge
>
> > [!answer]- Show Answer
> > **C. Hacktivist — ideology**
> >
> > [[threat-actors|Hacktivists]] are ideologically or politically motivated attackers who use tactics like website defacement and data leaks to embarrass targets and draw attention to their cause — protesting environmental practices is a classic hacktivist motivation. Nation-state actors pursue espionage or sabotage on behalf of governments, not public protest. Organized crime seeks financial gain, not ideological statements. Insider threats originate from within the organization, and the scenario describes an external activist group.
>
> **Q4.** A teenager uses a publicly available exploit kit downloaded from a hacking forum to scan the internet for vulnerable web servers and deface any sites they can access. Which threat actor type does this BEST represent, and what is their PRIMARY characteristic?
>
> A. Hacktivist — ideological motivation
> B. Script kiddie — low sophistication using pre-built tools
> C. Insider threat — legitimate access abuse
> D. Organized crime — structured financial operation
>
> > [!answer]- Show Answer
> > **B. Script kiddie — low sophistication using pre-built tools**
> >
> > [[threat-actors|Script kiddies/unskilled attackers]] have low sophistication and rely on pre-built tools and exploit kits created by others — the teenager using a downloaded exploit kit for opportunistic attacks is the defining example. Hacktivists have a specific ideological or political cause driving their actions, not random defacement for notoriety. Insider threats have legitimate organizational access, which an external teenager does not. Organized crime involves structured, well-funded groups pursuing financial gain, not individual opportunistic attacks.

## Scenario

> See [[case-threat-actors]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [2.1 – Threat Actors](https://www.youtube.com/watch?v=6xUH0t6ugIM)
