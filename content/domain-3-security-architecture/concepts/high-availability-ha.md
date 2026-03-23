---
title: "High availability (HA)"
description: "measured in \"nines\" (99.9% = 8.76 hours downtime/year; 99.999% = 5.26 minutes/year)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

High Availability (HA) is a system design approach aimed at ensuring a system remains operational for the maximum possible time, minimizing planned and unplanned downtime. HA is measured as a percentage of uptime, commonly expressed in "nines" — the number of nines in the availability percentage. Achieving high nines requires redundant components, automatic failover, and careful design to eliminate single points of failure.

## Key Details

- 99.9% ("three nines"): 8.76 hours downtime per year
- 99.99% ("four nines"): 52.6 minutes downtime per year
- 99.999% ("five nines"): 5.26 minutes downtime per year
- HA requires redundant hardware, automatic failover, load balancing, and geographic distribution
- Recovery Time Objective (RTO) defines the maximum acceptable downtime; HA systems minimize RTO

## Connections

- Parent: [[resilience-and-redundancy]] — high availability is the primary goal of resilient architecture design
- See also: [[failover]]
