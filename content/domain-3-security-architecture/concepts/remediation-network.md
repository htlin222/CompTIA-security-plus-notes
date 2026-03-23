---
title: "Remediation network"
description: "quarantine VLAN where non-compliant devices are placed to receive updates"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

A remediation network (also called a quarantine VLAN or remediation VLAN) is a restricted network segment to which NAC systems direct devices that fail compliance checks — such as devices with outdated antivirus, missing patches, or non-compliant configurations. While in the remediation VLAN, devices have limited network access sufficient to download required updates but cannot access production network resources.

## Key Details

- Devices are automatically redirected to the remediation VLAN when they fail NAC posture assessments
- The remediation network provides access to update servers, patch repositories, and antivirus update servers only
- After completing remediation and passing a re-assessment, devices are moved to the appropriate production VLAN
- Prevents non-compliant devices from posing a risk to production network resources while still allowing them to get compliant
- Often implemented using 802.1X VLAN assignment based on authentication and posture assessment results

## Connections

- Parent: [[nac]] — the remediation network is a key NAC implementation component
- See also: [[guest-networking]]
