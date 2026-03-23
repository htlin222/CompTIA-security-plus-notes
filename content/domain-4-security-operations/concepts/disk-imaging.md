---
title: "Disk imaging"
description: "Creating a bit-for-bit copy of storage media for analysis without altering the original"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Disk Imaging?
> Making a disk image is like photocopying an entire book page by page. You get an exact copy of everything on a hard drive so you can study it without touching the original.

## Definition

Disk imaging in digital forensics is the process of creating an exact bit-for-bit copy (forensic image) of a storage device, including all allocated and unallocated space, deleted files, and file system metadata. All forensic analysis is performed on the image, not the original media, to preserve evidence integrity and maintain chain of custody.

## Key Details

- Tools: FTK Imager, dd (Linux), Autopsy, EnCase
- Write blockers must be used during imaging to prevent accidental modification of the original
- Hash values (MD5, SHA-256) are calculated before and after to verify image integrity
- Captures deleted files, file slack space, and unallocated clusters that may contain evidence
- Forensic image formats: RAW (dd), E01 (EnCase), AFF (Advanced Forensic Format)

## Connections

- Parent: [[digital-forensics]] — disk imaging is a foundational forensic evidence collection technique
- See also: [[write-blockers]]
