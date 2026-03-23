---
title: "Default credentials"
description: "Factory-set usernames and passwords that are publicly documented and easily exploited"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Default Credentials?
> Many devices come with a password like "admin/password" printed right in the manual. If you never change it, anyone who reads the manual can walk right in.

## Definition

Default credentials are the factory-preset username and password combinations that vendors install on devices, software, and systems for initial setup. Because these credentials are publicly documented (in manuals, vendor websites, and databases like defaultpasswords.in), any attacker who gains access to a device or service that still uses default credentials can immediately authenticate without any prior knowledge of the specific target.

## Key Details

- Extremely common on **IoT devices** (routers, cameras, printers, industrial controllers)—many ship with `admin/admin` or `admin/password`.
- The **Mirai botnet** exploited default credentials on IoT devices to build a massive DDoS botnet.
- Changing default credentials is one of the **first hardening steps** for any new device or system.
- **Shodan** can be used to find internet-exposed devices still using default credentials.
- Some modern devices ship with unique, device-specific default credentials printed on the device—better than universal defaults but still require changing.

## Connections

- Parent: [[vulnerability-types]] — a common and easily exploited vulnerability class
- See also: [[misconfigurations]]
