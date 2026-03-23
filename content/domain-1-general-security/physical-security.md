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

## Scenario

> See [[case-physical-security]] for a practical DevOps scenario applying these concepts.
