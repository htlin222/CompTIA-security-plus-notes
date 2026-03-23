---
title: "Session recording"
description: "Recording all actions taken during privileged sessions for audit and forensic purposes"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Session Recording?
> Session recording captures everything an admin does on a computer, like a video camera in a control room. If something goes wrong, you can replay the tape to see exactly what happened.

## Definition

Session recording is a PAM capability that captures a complete record of all activities performed during a privileged access session, including keystrokes, commands executed, files accessed, and screen activity. These recordings provide an auditable trail of what privileged users did during their sessions, supporting forensic investigations, compliance auditing, and insider threat detection.

## Key Details

- Records can be keystroke logs, video recordings of screen activity, or both
- Stored securely in the PAM vault and protected from tampering or deletion by the user being monitored
- Users should be informed that privileged sessions are recorded (deterrence effect and legal compliance)
- Session recordings are invaluable for forensic investigation when a privileged account is compromised
- Required by various compliance frameworks for privileged access: PCI DSS, HIPAA, SOX

## Connections

- Parent: [[privileged-access-management]] — session recording is a key PAM control for privileged access accountability
- See also: [[password-vaulting]]
