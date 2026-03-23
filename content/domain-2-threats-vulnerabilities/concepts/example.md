---
title: "CSRF Example"
description: "A hidden image tag that triggers a bank transfer while the victim is logged into their banking site"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A classic Cross-Site Request Forgery (CSRF) example demonstrates how an attacker tricks a victim's authenticated browser into performing an unwanted action on a trusted website. By embedding a malicious request (e.g., as a hidden image tag or form) in an attacker-controlled page, the victim's browser automatically includes their session cookie when the request is sent, making it appear as a legitimate authenticated action.

## Key Details

- **Classic example**: `<img src="https://bank.com/transfer?to=attacker&amount=10000">` embedded in an attacker's webpage.
- When the victim (who is logged into bank.com) visits the attacker's page, their browser automatically sends the request with their session cookie.
- The bank server sees a request from an authenticated user—it processes the transfer.
- The victim's browser **cannot distinguish** this forged request from a legitimate one without CSRF protections.
- This is why **anti-CSRF tokens** (unique, random values embedded in legitimate forms) are essential—the attacker cannot forge a valid token.

## Connections

- Parent: [[xss-and-csrf]] — an illustrative example of a CSRF attack
- See also: [[mechanism]]
