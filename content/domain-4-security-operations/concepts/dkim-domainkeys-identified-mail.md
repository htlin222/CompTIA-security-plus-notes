---
title: "DKIM (DomainKeys Identified Mail)"
description: "Adds a digital signature to outgoing emails to verify the message was not altered in transit"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - DKIM
---

## Definition

DKIM (DomainKeys Identified Mail) is an email authentication method that allows the sending mail server to digitally sign outgoing messages using a private key. The corresponding public key is published in the domain's DNS TXT record. Receiving mail servers retrieve the public key from DNS and use it to verify the digital signature, confirming that the message originated from the claimed domain and was not altered in transit.

## Key Details

- Uses asymmetric cryptography: private key signs, public key in DNS verifies
- Signs the message body and selected headers (From, Subject, Date)
- A valid DKIM signature proves message integrity and that the sending server was authorized by the domain
- DKIM passes even if the message goes through an authorized forwarding server that doesn't break the signature
- Works with SPF and DMARC to provide comprehensive email authentication

## Connections

- Parent: [[email-security]] — DKIM is one of three core email authentication protocols (with SPF and DMARC)
- See also: [[spf-sender-policy-framework]]
