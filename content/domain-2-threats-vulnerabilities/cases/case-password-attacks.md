---
title: "Case: Credential Stuffing at TravelNow — 14,000 Compromised Accounts in 90 Minutes"
description: "A credential stuffing attack using a 2.3-billion-record leaked database compromises 14,000 customer accounts at a travel startup. Zero rate limiting and no MFA enabled fraudulent bookings worth $470K before discovery."
draft: false
date: 2026-03-21
tags:
  - domain/2
  - type/case
---

## The Scenario

TravelNow, a 200-person travel booking startup founded in 2019, has grown to serve 400,000 customers across the United States and Canada, offering real-time flight comparison and booking functionality. The platform is built on Django/PostgreSQL and handles approximately $18M in quarterly travel bookings. On March 5, 2026, at 4:12 AM PST, an automated [[credential-stuffing]] attack began hitting their customer authentication endpoint. The attack used a leaked credential database containing 2.3 billion username/password pairs compiled from previous major breaches (LinkedIn 2012, Yahoo 2013, Netflix 2019, Facebook 2019, Equifax 2017, and dozens of others).

The attacker's methodology was straightforward: a Python script running on a cloud server sent HTTP POST requests to `travelznow.com/api/auth/login` with credentials from the leaked database. The script attempted 50–100 login attempts per second, targeting usernames that matched TravelNow's customer base (identified via other leaked databases containing email addresses used on TravelNow). With no rate limiting, authentication throttling, or CAPTCHA challenges, each attempt took approximately 200–300 milliseconds, allowing the attacker to attempt 12,000–18,000 credentials per minute.

By 5:47 AM PST (95 minutes into the attack), the script had executed 1.2 million login attempts. Of those, 14,247 had succeeded. The attackers had identified accounts where customers had reused passwords from previous breaches. These accounts were now compromised and ready for exploitation. At 6:00 AM, the attackers began using the stolen credentials to book expensive international flights (average cost: $3,200) destined for popular resale hubs: Dubai, Istanbul, Singapore. The booking volume was unusual: some attackers booked 15–20 flights per account in a single hour, an impossible pattern for legitimate customers.

The breach was discovered when a legitimate customer, David Zhang, received a booking confirmation email for a flight to Mumbai (valued at $3,400) that he had never purchased. He immediately called customer support at 6:47 AM Pacific time. Support agent Michelle logged into David's account and confirmed the unauthorized booking. She also found three additional unauthorized bookings on the same account, all within the past 95 minutes. Michelle escalated the issue to the on-call security engineer, Derek Martinez, who immediately checked the authentication logs.

Derek's analysis revealed the smoking gun: between 4:12 AM and 5:47 AM, the login API had received 1.2 million requests from three distinct IP addresses (all originating from cloud providers in Eastern Europe and Russia). Login success rate was 1.2%—far below the normal 0.008% (which typically represents failed password attempts from legitimate users with typos). This pattern was unambiguous: a credential stuffing attack was in progress. Derek immediately triggered an incident response activation at 7:15 AM.

By 7:30 AM, Derek had disabled all accounts showing logins from the attacker IP addresses and initiated a password reset for all 14,247 compromised accounts. He also implemented emergency controls: rate limiting (5 login attempts per minute per IP address, 10 failures before 30-minute lockout), CAPTCHA challenges after 3 failed attempts, and mandatory password reset before account access. By 8:45 AM, TravelNow's CEO had notified affected customers via email and offered free flight rebooking and travel insurance. By 9:00 AM, the story had leaked to the press.

The financial damage was substantial: fraudulent bookings totaled $470,000 before the attack was contained. TravelNow absorbed the full loss ($3,200 × 147 fraudulent bookings). Additionally, they spent $120,000 on incident response consulting, credit monitoring for affected customers, and customer notification. The reputational damage was harder to quantify but resulted in a 28% drop in new customer signups for three months post-incident.

## What Went Right

- **Legitimate customer complaints triggered rapid escalation**: David Zhang's single booking confirmation email, while personally frustrating, enabled the attack's discovery within 95 minutes of initiation. Had the attackers been more cautious and booked fewer flights per account, the attack might not have been detected for days or weeks.

- **Rapid account disabling prevented further fraud**: Once the attack was detected, Derek immediately disabled all affected accounts and forced password resets. This prevented the attackers from continuing to book flights or accessing sensitive booking history and payment methods.

- **Post-incident controls addressed the root cause**: Rate limiting, CAPTCHA, and eventually [[mfa]] ensured that the credential stuffing attack class became infeasible. Attackers couldn't repeat this specific attack against TravelNow again.

- **Transparent customer communication preserved some trust**: By immediately notifying customers, offering rebooking, and providing credit monitoring, TravelNow retained 72% of affected customers. Delayed notification would have damaged trust further.

## What Could Go Wrong

- **No [[brute-force|rate limiting]] allowed 1.2 million login attempts**: This is the most glaring failure. Rate limiting is a trivial control: limit login attempts from a single IP to 5–10 per minute. Implement account lockout after N failures. CAPTCHA after 3 failures. None of these were present, allowing the attacker to probe credentials at industrial scale.

- **No [[credential-stuffing|credential stuffing]]-specific detection**: TravelNow had no monitoring system that flagged unusual login patterns (high failure rate, many logins from single IP, successful logins immediately followed by API calls to book expensive flights). A system that detected 10,000 failed login attempts in 90 minutes would have raised alerts within seconds.

- **No [[mfa|multi-factor authentication]]**: Even with compromised passwords from external breaches, MFA would have prevented account takeover. SMS-based or TOTP-based MFA, while imperfect, would have blocked the attackers' automated script. MFA adoption post-incident became mandatory for all new accounts.

- **No behavioral anomaly detection**: When an account that typically books one flight per week suddenly books 15 flights to international hubs in 60 minutes, that's obvious fraud. A simple rule like "flag accounts that book more than 5 flights in 60 minutes" would have caught every fraudulent transaction within minutes and triggered manual review.

- **No monitoring of password reuse across services**: TravelNow could have partnered with a service like Have I Been Pwned to check customer passwords against known breach databases and proactively warned customers who were reusing compromised credentials. This would have prevented 90% of the compromised accounts.

## Key Takeaways

- **[[credential-stuffing]] is effective because passwords are reused across services**: When LinkedIn, Yahoo, or Netflix are breached, those credentials work elsewhere. Organizations can't prevent external breaches, but they can [[detect|detect]] and [[defend|defend]] against credential stuffing attacks on their own platforms.

- **[[brute-force]] attacks require rate limiting and account lockout**: Limit login attempts per IP (5–10 per minute), limit failures per account (lockout after 5–10 failures), implement CAPTCHA to distinguish bots from humans. These are trivial controls that should be standard on all login forms.

- **[[mfa|Multi-factor authentication]] is the most effective defense against credential stuffing**: Even if passwords are compromised, attackers can't gain account access without the second factor. MFA adoption should be mandatory, not optional.

- **Behavioral analysis catches fraud that simple rate limiting misses**: Book 1 flight per week normally? Flag accounts booking 10+ flights in 1 hour. Login from unusual geography? Flag it. Unusual payment method? Flag it. Fraud detection should use multiple signals, not just password validation.

- **Monitor for signs of [[credential-stuffing]] on your platform**: High login failure rates, many failed attempts from single IP, successful logins immediately followed by anomalous API calls (booking expensive flights, changing payment methods) are all indicators of credential stuffing in progress.

## Related Cases

- **[[case-mfa]]** — Multi-factor authentication is the most effective defense against credential compromise; understand [[authentication]], TOTP, push notifications, and hardware tokens as second factors.

- **[[case-authentication]]** — Passwordless authentication (WebAuthn, FIDO2) eliminates the need for passwords entirely, making credential stuffing impossible; understand modern authentication mechanisms.

- **[[case-sso]]** — Single sign-on services like Okta and OneLogin centralize authentication and can implement security controls (MFA, [[credential-stuffing|brute force]] detection, compromised credential monitoring) at scale.

- **[[case-password-attacks]]** — Understand [[dictionary-attack]], [[hybrid-attack]], [[kerberoasting]], and [[pass-the-hash]]; credential stuffing is one attack class among many password-based attacks.
