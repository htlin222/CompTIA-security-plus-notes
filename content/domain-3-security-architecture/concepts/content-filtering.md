---
title: "Content filtering"
description: "proxies can inspect and block traffic based on URLs, categories, or content types"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Content filtering?
> It's like a school librarian who checks what books you are picking up and says "this one is not appropriate for you." Content filtering looks at websites and files and blocks the ones that break the rules.

## Definition

Content filtering is a proxy server capability that inspects network traffic and blocks or allows access to web resources based on configured policies. Policies can be based on URL categories (gambling, adult content, malware sites), specific URLs or domains, MIME types, file types, or keyword matching within content. Content filtering enforces acceptable use policies and protects users from malicious sites.

## Key Details

- URL categorization databases classify billions of domains into categories for policy enforcement
- HTTPS inspection (SSL/TLS decryption) is required to filter encrypted traffic content
- Can block downloads of specific file types (executables, certain document types)
- DNS-based filtering is a lightweight alternative that blocks at the DNS resolution level
- Modern Secure Web Gateways (SWGs) combine content filtering with DLP and threat protection

## Connections

- Parent: [[load-balancers-and-proxies]] — content filtering is a key security function of proxy servers
- See also: [[data-loss-prevention-dlp]]
