---
title: "Timeline analysis"
description: "Reconstructing the sequence of events using file timestamps, logs, and artifacts"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Timeline Analysis?
> Timeline analysis puts all the events in order by time, like reading a story from beginning to end. It helps you understand exactly how an attack unfolded, step by step.

## Definition

Timeline analysis is a digital forensics technique that reconstructs the chronological sequence of events on a system by correlating timestamps from file system metadata, registry entries, browser history, event logs, and other artifacts. A detailed timeline helps investigators understand exactly what happened, when it happened, and in what order — essential for understanding the full scope of an attack.

## Key Details

- File system timestamps: MACB (Modified, Accessed, Changed, Born/Created) — each carries different information
- Windows event logs, web browsing history, registry last-write times, and prefetch files contribute to the timeline
- Tools: Autopsy (open-source), EnCase, FTK, Plaso/log2timeline (timeline supertimeline creation)
- Anti-forensics: timestomping can manipulate file timestamps — analysts must look for inconsistencies
- Correlating the attacker's timeline with business events (detected, contained, eradicated) supports the final report

## Connections

- Parent: [[digital-forensics]] — timeline analysis is a core forensic analysis technique
- See also: [[anti-forensics]]
