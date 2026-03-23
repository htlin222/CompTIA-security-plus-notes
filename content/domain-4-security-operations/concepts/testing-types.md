---
title: "Testing types"
description: "Black box (no prior knowledge), white box (full knowledge), gray box (partial knowledge)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Testing Types?
> Testing types describe how much information a tester gets before starting -- full knowledge, partial knowledge, or none at all. It is like taking a test open-book, with a cheat sheet, or completely cold.

## Definition

Penetration testing can be conducted with varying levels of information provided to the testing team about the target environment. The level of prior knowledge affects what the test simulates — an outside attacker with no information, an insider threat with full access, or something in between. Each testing approach has different value for different security assessment objectives.

## Key Details

- **Black box**: tester has no prior knowledge of the target; simulates an external attacker; most realistic external attack simulation; highest level of effort
- **White box**: tester has complete knowledge (network diagrams, source code, credentials); enables comprehensive testing in less time; simulates insider threat or privileged attacker
- **Gray box**: tester has partial knowledge (network topology, some credentials); most common in practice; balances realism with efficiency
- Choice depends on assessment objectives and available time/budget
- Gray box testing is typically most cost-effective for comprehensive vulnerability discovery

## Connections

- Parent: [[penetration-testing]] — testing type selection is a fundamental scoping decision for any assessment
- See also: [[red-team-vs-pen-test]]
