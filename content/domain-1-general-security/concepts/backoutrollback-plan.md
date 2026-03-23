---
title: "Backout/Rollback plan"
description: "Predefined steps to reverse a change if it causes problems"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is a Backout/Rollback Plan?
> It's like drawing your room layout before rearranging the furniture. If the new layout is terrible, you can look at the drawing and put everything back exactly the way it was.

## Definition

A backout (or rollback) plan is a documented set of procedures that outlines how to reverse a change to a system if that change causes unexpected problems or failures. It is a required element of any well-structured change management process, ensuring that systems can be restored to their prior known-good state quickly and reliably when a change goes wrong.

## Key Details

- Should be prepared **before** any change is implemented—not created reactively after a failure.
- Must be tested where possible, especially for critical infrastructure changes.
- Includes: specific steps to revert the change, estimated time to execute, personnel responsible, and validation checks to confirm successful rollback.
- Stored as part of the **change request documentation** submitted to the Change Advisory Board (CAB).
- Critical for **maintenance windows**—if rollback can't be completed within the window, the change may not be approved.

## Connections

- Parent: [[change-management]] — a required component of the change management process
- See also: [[change-advisory-board-cab]], [[maintenance-windows]]
