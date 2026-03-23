---
title: "Rights management (DRM/IRM)"
description: "controls that persist with the data (who can view, edit, print, forward)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
aliases:
  - DRM/IRM
---

## Definition

Digital Rights Management (DRM) and Information Rights Management (IRM) are technologies that attach persistent access controls directly to data files, so that permissions travel with the data regardless of where it is copied or stored. Unlike traditional access control (which controls access at the storage level), rights management controls what authorized users can do with data they have legitimately accessed.

## Key Details

- Controls persist with the document: an emailed document still enforces who can view, edit, print, or forward
- Can set expiration dates: document automatically becomes unreadable after a specified date
- Requires IRM infrastructure: a rights management server validates permissions when a user opens a protected document
- Common implementations: Microsoft Purview Information Protection (Azure Information Protection), Adobe Experience Manager
- Used to protect intellectual property, legal documents, and sensitive business information from unauthorized distribution

## Connections

- Parent: [[data-protection]] — rights management extends data protection controls beyond the organization's boundary
- See also: [[data-loss-prevention-dlp]]
