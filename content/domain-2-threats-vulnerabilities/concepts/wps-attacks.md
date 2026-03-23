---
title: "WPS attacks"
description: "Exploiting Wi-Fi Protected Setup PIN vulnerability to recover the WPA key"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

WPS (Wi-Fi Protected Setup) attacks exploit a design vulnerability in the WPS PIN authentication mechanism that allows easy network setup using an 8-digit PIN. Due to a flaw in the WPS protocol's verification process, the 8-digit PIN is effectively split into two halves that can be attacked separately—reducing the attack space from 10^8 to roughly 11,000 combinations. This allows recovery of the WPA/WPA2 passphrase in hours.

## Key Details

- **WPS PIN flaw**: The access point verifies the first 4 digits and second 4 digits (with one check digit) separately—effectively 10^4 + 10^3 = 11,000 possible combinations, not 10^8.
- Tool: **Reaver** and **Bully**—automate WPS PIN brute-force attacks; classic attacks take 4-10 hours.
- Some vendors added **rate limiting** and **lockout** to mitigate brute-force—but many routers remain vulnerable.
- **Mitigation**: **Disable WPS** entirely on all wireless access points—there is no secure way to use WPS PIN mode; WPS button press (PBC) is slightly safer.
- WPS was introduced in 2007 for ease of use; it became a notorious security weakness.

## Connections

- Parent: [[wireless-attacks]] — a Wi-Fi protocol implementation weakness
- See also: [[wpawpa2-handshake-capture]]
