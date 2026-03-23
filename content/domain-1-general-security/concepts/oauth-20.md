---
title: "OAuth 2.0"
description: "Authorization framework for delegated access; issues access tokens (not authentication)"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

OAuth 2.0 is an open authorization framework that allows third-party applications to access specific resources on behalf of a user, without sharing the user's credentials. Instead, an authorization server issues access tokens that represent limited, delegated permissions. It is an authorization protocol—not an authentication protocol (that distinction belongs to OpenID Connect, which is built on top of OAuth 2.0).

## Key Details

- **Key distinction**: OAuth 2.0 is about **authorization** (what you can access), not **authentication** (who you are)—OpenID Connect adds authentication.
- **Flows**: Authorization Code (web apps), Implicit (deprecated), Client Credentials (machine-to-machine), Device Code (TVs/IoT).
- **Tokens**: **Access token** (short-lived, used to access resources), **Refresh token** (longer-lived, used to get new access tokens).
- Common use case: "Login with Google/Facebook"—your identity from one provider is used to authorize access to another application.
- Security concerns: **token leakage**, **improper scope**, **redirect URI manipulation**—proper implementation is critical.

## Connections

- Parent: [[authorization]] — OAuth 2.0 as a delegated authorization framework
- See also: [[conditional-access]]
