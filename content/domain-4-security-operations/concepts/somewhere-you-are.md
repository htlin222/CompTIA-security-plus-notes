---
title: "Somewhere you are"
description: "Geolocation or IP-based restrictions (sometimes considered a factor)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

"Somewhere you are" is a contextual authentication factor that uses physical location information — such as GPS coordinates, IP geolocation, network location, or presence on a trusted Wi-Fi network — to verify or restrict authentication attempts. While not a primary MFA factor in most implementations, location context is used as an additional signal for adaptive/risk-based authentication.

## Key Details

- IP-based geolocation: authentication from unexpected countries or high-risk regions can trigger additional verification or blocking
- Trusted network detection: being on the corporate network may reduce the MFA requirements
- GPS location from mobile devices can be used for more accurate location verification
- "Impossible travel" detection: logins from two distant locations within too short a time period indicate compromise
- Used in conditional access policies (Azure AD, Okta) as an environmental factor

## Connections

- Parent: [[mfa]] — location is an environmental/contextual authentication factor
- See also: [[attribute-based-access-control-abac]]
