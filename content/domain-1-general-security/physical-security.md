---
title: "Physical Security"
description: "Tangible controls and measures that protect facilities, hardware, and personnel"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/medium
aliases:
  - "Physical Controls"
---

> [!eli5] ELI5: What is Physical Security?
> Physical security is all the real-world stuff that keeps bad people away from your computers and buildings -- fences around the property, locks on the doors, cameras watching the hallways, and guards checking who comes in. Even the best password in the world won't help if someone can just walk up to a computer and steal it. That's why protecting the actual building and the equipment inside it is just as important as protecting what's on the screen.

## Overview

Physical security encompasses the tangible controls that protect an organization's facilities, hardware, and personnel from unauthorized physical access, theft, damage, and environmental threats. It forms the outermost layer in a defense-in-depth strategy and is often the first line of defense against both external intruders and insider threats.

## Key Concepts

- **[[bollards|Bollards]]** — short vertical posts preventing vehicle ramming attacks
- **[[fencing|Fencing]]** — perimeter barriers; height determines deterrence level (3ft = deterrent, 6ft = hard to climb, 8ft+ = serious security)
- **[[access-control-vestibules-mantraps|Access control vestibules (mantraps)]]** — dual-door chambers allowing only one door open at a time; prevents tailgating
- **[[security-guards|Security guards]]** — human element providing judgment-based access control
- **[[video-surveillance-cctv|Video surveillance (CCTV)]]** — continuous monitoring and recording of facility areas
  - PTZ cameras (Pan-Tilt-Zoom) for active monitoring
- **[[access-badges|Access badges]]** — RFID or smart card-based identification for building entry
- **[[lighting|Lighting]]** — well-lit areas deter criminal activity; critical for CCTV effectiveness
- **Sensors**:
  - **Infrared** — detects body heat
  - **Pressure** — detects weight on floor surfaces
  - **Microwave** — detects movement via microwave signals
  - **Ultrasonic** — detects movement via sound waves
- **[[locks|Locks]]** — mechanical (key), electronic (keypad), biometric (fingerprint)
- **[[cable-locks|Cable locks]]** — physically secure laptops and equipment
- **[[screen-filtersprivacy-screens|Screen filters/privacy screens]]** — prevent shoulder surfing
- **[[secure-areas|Secure areas]]** — server rooms, data centers, wiring closets; require restricted access
- **[[environmental-controls|Environmental controls]]** — fire suppression (wet pipe, dry pipe, clean agent), HVAC, humidity control
- **[[faraday-cage|Faraday cage]]** — blocks electromagnetic signals; prevents eavesdropping and signal leakage

## Exam Tips

> [!tip] Remember
> **Access control vestibule** (mantrap) = prevents tailgating. **Bollards** = prevents vehicle attacks. **Faraday cage** = prevents electromagnetic eavesdropping. Know which physical control maps to which threat.

> [!tip] Fire Suppression
> Wet pipe = always has water, fastest response. Dry pipe = water held back by valve, for cold environments. Clean agent (FM-200, Halon replacement) = safe for electronics in data centers.

## Connections

- Forms the outermost layer of [[defense-in-depth]] security strategy
- Prevents physical social engineering attacks like tailgating (see [[social-engineering]])
- Protects [[embedded-systems-security]] devices that may be deployed in exposed locations
- Environmental controls support [[resilience-and-redundancy]] goals for facility uptime
- Access badges and biometrics tie into [[authentication]] as physical identity verification

## Practice Questions

> [!qbank]- Q-Bank: Physical Security (4 Questions)
>
> **Q1.** After a social engineering assessment reveals that unauthorized individuals frequently follow employees through the main entrance, which physical control should an organization implement FIRST to address this specific vulnerability?
>
> A. CCTV cameras at all entrances
> B. Access control vestibule (mantrap)
> C. Biometric fingerprint scanners
> D. Increased perimeter lighting
>
> > [!answer]- Show Answer
> > **B. Access control vestibule (mantrap)**
> >
> > An [[access-control-vestibules-mantraps|access control vestibule (mantrap)]] is a dual-door chamber that allows only one door to be open at a time and admits one person per authentication — it directly prevents tailgating. CCTV cameras record activity for review but do not physically prevent unauthorized entry. Biometric scanners strengthen authentication but do not prevent someone from following an authorized person through a single door. Increased lighting deters criminal activity in outdoor areas but does not address the tailgating problem at building entrances.
>
> **Q2.** A data center manager needs to select a fire suppression system for a room containing critical servers and networking equipment. Which system type is BEST suited to protect the electronics?
>
> A. Wet pipe system
> B. Dry pipe system
> C. Clean agent system (FM-200)
> D. Sprinkler with pre-action valve
>
> > [!answer]- Show Answer
> > **C. Clean agent system (FM-200)**
> >
> > [[environmental-controls|Clean agent systems]] like FM-200 suppress fire without leaving residue or water, making them safe for electronics in data centers and server rooms. Wet pipe systems always contain water and would damage electronic equipment. Dry pipe systems still release water when activated — they just hold it back with a valve for cold environments. Pre-action sprinklers also ultimately release water and are designed to prevent accidental discharge, not to protect sensitive electronics.
>
> **Q3.** A government facility needs to prevent adversaries from intercepting electromagnetic emanations from classified workstations. Which physical security measure BEST addresses this threat?
>
> A. Privacy screens on monitors
> B. Cable locks on all equipment
> C. Faraday cage around the secure room
> D. Infrared motion sensors
>
> > [!answer]- Show Answer
> > **C. Faraday cage around the secure room**
> >
> > A [[faraday-cage|Faraday cage]] blocks electromagnetic signals from entering or leaving an enclosed space, preventing eavesdropping on electromagnetic emanations from electronic equipment. [[screen-filtersprivacy-screens|Privacy screens]] prevent shoulder surfing (visual eavesdropping) but do not block electromagnetic signals. [[cable-locks|Cable locks]] prevent physical theft of equipment but do not address signal emanation. Infrared motion sensors detect physical movement for intrusion detection and have nothing to do with electromagnetic shielding.
>
> **Q4.** A facility security officer is evaluating perimeter fencing options for a high-security compound. What is the MINIMUM fence height recommended for deterring a determined intruder?
>
> A. 3 feet — basic deterrent
> B. 6 feet — difficult to climb
> C. 8 feet or higher — serious security
> D. 4 feet — standard commercial height
>
> > [!answer]- Show Answer
> > **C. 8 feet or higher — serious security**
> >
> > [[fencing|Fencing]] standards indicate that 8 feet or higher provides serious security appropriate for high-security facilities and deters determined intruders. A 3-foot fence is only a basic deterrent marking boundaries. A 6-foot fence is difficult to climb but may not deter a determined intruder at a high-security compound. A 4-foot fence is not a standard security classification and provides minimal deterrence.

## Scenario

> See [[case-physical-security]] for a practical DevOps scenario applying these concepts.
