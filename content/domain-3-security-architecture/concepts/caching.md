---
title: "Caching"
description: "proxies store frequently accessed content to reduce bandwidth and improve response times"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Caching?
> Caching is like keeping a copy of your favorite book on your desk instead of walking to the library every time you want to read it. It saves time by storing things you use often in a nearby spot.

## Definition

Caching is a proxy server function that stores copies of frequently requested web content locally so that subsequent requests for the same content can be served from the cache without fetching it from the origin server. This reduces bandwidth consumption, improves response times for end users, and reduces load on origin servers.

## Key Details

- Forward proxies cache outbound web content for internal users
- Cached content serves requests faster and reduces external bandwidth costs
- Cache poisoning is a security concern — attackers can inject malicious content into a cache
- Time-to-live (TTL) values control how long content remains in cache before refresh
- HTTPS inspection may be required to cache encrypted content

## Connections

- Parent: [[load-balancers-and-proxies]] — caching is a core function of proxy servers
- See also: [[content-filtering]]
