---
title: "XML injection / XXE"
description: "Injecting malicious XML to read files, perform SSRF, or cause denial of service"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is XML Injection / XXE?
> The attacker sends a specially crafted document to a website that tricks the server into loading secret files or making requests it shouldn't. It's like handing someone a recipe that secretly tells them to open your diary and read it out loud.

## Definition

XML External Entity (XXE) injection is an attack against applications that parse XML input, exploiting poorly configured XML parsers that allow the definition and loading of external entities. By injecting a crafted XML document with a malicious external entity reference, attackers can read arbitrary files from the server, perform server-side request forgery (SSRF), cause denial of service (Billion Laughs attack), or in some cases execute code.

## Key Details

- **File disclosure**: `<!ENTITY xxe SYSTEM "file:///etc/passwd">` — causes the parser to include the contents of `/etc/passwd` in the response.
- **SSRF via XXE**: `<!ENTITY xxe SYSTEM "http://internal-service.local/api">` — uses the server as a proxy to access internal resources.
- **Billion Laughs DoS**: Nested entity expansion creates exponential growth in memory usage—crashes the parser.
- **Defense**: **Disable external entity processing** in the XML parser configuration (this is the primary fix); use **JSON APIs** instead of XML where possible; validate XML against a strict schema.
- Relevant in **SOAP web services**, **file format parsers** (SVG, DOCX), and any application that accepts XML input.

## Connections

- Parent: [[injection-attacks]] — an XML-specific injection attack
- See also: [[server-side-request-forgery-ssrf]]
