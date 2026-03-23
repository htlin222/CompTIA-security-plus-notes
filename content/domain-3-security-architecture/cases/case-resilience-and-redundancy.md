---
title: "Case: The Generator Starvation — Dual Power Feed Failure During Ice Storm"
description: "Both power feeds to a primary data center fail during an ice storm in Atlanta. The generator runs out of diesel after 14 hours because the fuel delivery contract lapsed. The active-passive failover to the DR site has never been tested in production."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

CloudFirst Inc. operates a data center in Atlanta housing critical infrastructure for their SaaS platform serving 150,000 customers. The primary data center has:

- **Two power feeds** from different electrical substations, each rated for 100% facility load
- **Three diesel generators** capable of supporting the entire facility for up to 72 hours with a full fuel tank
- **UPS batteries** that provide 15 minutes of backup power during generator startup
- **An active-passive failover** to a secondary data center in Nashville, 4 hours away by truck

On January 12, 2024, an ice storm swept through Atlanta with unusual intensity. A power transmission line failed under the weight of accumulated ice. The first power feed went down at 2:17 PM. The facility automatically switched to the second power feed.

Twenty minutes later, a transformer at the second substation failed—likely from the surge when the first feed went down—and the second power feed went dark.

At 2:38 PM, the data center switched to generator power. The UPS batteries had bought 15 minutes for the generators to spin up. All three diesel generators engaged and started supplying power.

The facilities team expected the power to be restored within hours. Ice storms usually knocked out power for 4-6 hours. The fuel in the tank could support operations for 72 hours, so they didn't initiate the failover to the Nashville data center yet. Failover was a manual process that took about 30 minutes of downtime to execute.

But this ice storm was different. The damage was extensive. Downed power lines, fallen trees blocking maintenance vehicles, transformers exploding. The power utility estimated restoration at 48-72 hours.

By hour 8 of generator operation, the fuel tank had burned through 40% of its supply. The facilities manager, Tom Walker, did the math: at current burn rate, the generators would run out of fuel in approximately 14 hours.

Tom checked the fuel delivery contract. It specified emergency delivery of 20,000 gallons at any time, with a 4-hour response time. But when he called the fuel supplier, he got bad news: the contract had lapsed six months ago. The purchasing department had decided to renew it with a cheaper supplier, but the new supplier's contract wasn't finalized yet. There was no emergency delivery agreement in place.

Tom called the cheaper supplier—still unnamed in negotiations. They could promise delivery in 24-36 hours, but no guarantee of having 20,000 gallons immediately available.

The mathematics were brutal: the generators would run dry around 4:38 PM the next day (January 13). The power utility estimated restoration around January 14, 24 hours after that.

Tom escalated to Chief Technology Officer David Rodriguez. David had to make a decision: continue on generator power and hope fuel delivery happens before the tank runs dry, or execute a manual failover to the Nashville data center now while there was still time.

Executing the failover meant:

1. Breaking database replication from Atlanta to Nashville
2. Promoting the Nashville database to primary status
3. Redirecting all customer traffic from Atlanta to Nashville
4. Rolling back in-flight transactions from the past few hours
5. Accepting 30 minutes of downtime during the transition
6. Dealing with data consistency issues for a few minutes after failover

The alternative was to sit tight and hope the fuel arrived or the power was restored. If both failed, the data center would lose power completely, and all systems would go dark without a controlled failover.

David made the call at 10:45 PM on January 12: Execute the failover to Nashville.

The process took 42 minutes (longer than planned because they had to manually validate data consistency). At 11:27 PM, customer traffic shifted to Nashville. Within 10 minutes, all systems were operational in Nashville.

Meanwhile, in Atlanta, the generators continued running, supporting only the building systems (cooling, lighting, security) but not processing customer data.

At 2:14 PM on January 13—exactly 24 hours into the outage—the diesel tank ran completely dry. The generators spun down. The building lost power. The UPS batteries, designed for 15-minute backup, exhausted within minutes.

The facility went dark at 2:19 PM. No systems running. No cooling. No security systems. The equipment would start failing from heat within hours.

Power was finally restored at 4:47 PM on January 13—46 hours after the initial failure.

By that time, all customer processing was happening in Nashville. The Atlanta data center was just a dark building with idle equipment.

## Post-Incident Analysis

In the aftermath, CloudFirst's executives realized several critical failures:

**Failure 1: Fuel Supply Contract Lapsed**
- The purchasing department and facilities management didn't communicate
- No one verified that emergency fuel delivery was still available
- Saving $12,000/year on fuel delivery costs ended up costing millions in infrastructure investment to add redundancy

**Failure 2: Active-Passive Failover Had Never Been Tested in Production**
- The failover procedure existed on paper but had never been executed under real pressure
- During the actual failover, teams discovered that the database replication was slightly out of sync
- They lost approximately 30 seconds of customer transactions (orders, payment confirmations) that had to be manually reconstructed

**Failure 3: Generator Fuel Capacity Was Undersized**
- 72 hours of fuel capacity sounds good, but it was calculated based on "standard" load, not worst-case
- During the power failure, the facility ran cooling systems, lighting, security, and some critical systems—higher load than estimated
- The actual burn rate was 2.8x the "standard" rate
- 72 hours of standard load became 26 hours of actual load

**Failure 4: No Redundancy on the Redundancy**
- The fuel delivery contract was the single point of failure for the generator system
- There was no secondary fuel supplier
- There was no on-site fuel storage beyond the main tank
- There was no plan for obtaining emergency fuel from other sources

**Failure 5: Power Feeds Weren't As Independent As Assumed**
- The company believed the two power feeds were from completely independent substations
- In reality, they shared some common infrastructure upstream
- A single transformer failure cascaded to both feeds

## Lessons and Remediation

CloudFirst spent $8.4 million on infrastructure improvements to prevent a recurrence:

**1. Dual Fuel Supplier Contracts**
- Establish primary and secondary emergency fuel delivery agreements
- Both suppliers pre-stage 10,000 gallons at an off-site fuel depot
- 4-hour emergency delivery guarantee from both suppliers

**2. Increased Generator Capacity**
- Upgraded the three existing generators and added a fourth
- Increased fuel storage capacity from 20,000 to 40,000 gallons
- Validated that even at worst-case load, the generators could run for 120 hours

**3. Quarterly Failover Drills**
- Execute the active-passive failover to Nashville at least quarterly
- Validate that data replication is in sync before failover
- Practice the manual processes and time them
- Identify any issues before they occur during a real emergency

**4. Redundant Power Infrastructure**
- Investigated whether the two power feeds were truly independent
- Discovered they shared a common transformer
- Added a third power feed from a different utility company entirely
- Installed a second UPS system for additional fault tolerance

**5. [[Diversity]] in Infrastructure**
- The company realized having two data centers in different cities was only good if failover actually worked
- Added a third data center on the West Coast for true geographic diversity
- Implemented automatic failover based on health checks (not just manual failover)

**6. [[High-availability|HA]] Without Geographic Separation**
- For critical systems that can't afford the latency of geographically distributed failover, implemented local HA with clustering
- Database clustering within the Atlanta facility provided [[failover]] without geographic distance

## What Went Right

- **Failover infrastructure existed**: Even though it had never been tested, the Nashville data center had the capacity to handle full production load when needed.
- **Failover was executed appropriately**: David made the decision to failover before total system failure, preventing complete data center darkness.
- **Manual procedures worked**: The team was able to execute the failover in 42 minutes despite not having practiced it.
- **Operational resilience kicked in**: Even though some transactions were lost, the failover recovered 99.98% of data.

## What Could Go Wrong

- **If fuel had arrived even 1 hour later**: The generator would have completely run out of fuel, causing a full blackout 45 minutes earlier.
- **If Nashville failover had failed**: With no fuel and no power restoration in sight, the Atlanta facility would have lost all systems completely.
- **If the failover had been attempted and failed**: A botched failover attempt would have caused data corruption or inconsistency that would take weeks to repair.
- **If power feeds truly were from independent substations**: The company's assumption would have lulled them into a false sense of security.

## Key Takeaways

- **[[High-availability-ha]] and [[disaster-recovery]] are different**: HA is about fast failover within the same region. DR is about having a remote facility that can take over if the primary is destroyed. Both are needed.
- **[[Failover]] procedures must be tested regularly**: A procedure that's never been executed under real pressure is just documentation. Test quarterly and record metrics (time to failover, data loss, customer impact).
- **Single-point-of-failure analysis must include supplier contracts**: A 72-hour diesel supply is meaningless if the fuel delivery contract expires. Audit supplier agreements like infrastructure.
- **[[Redundancy]] on critical systems includes their dependencies**: Backup power is only useful if you can get fuel. Backup generators are only useful if cooling systems also survive. Think about second and third-order dependencies.
- **[[Diversity]] reduces risk of correlated failures**: Two power feeds from the same utility can fail together. Two generators from the same manufacturer might have the same defect. Two data centers in the same region can both experience the same natural disaster.
- **[[Capacity-planning]] must account for worst-case load**: Generators rated for "100% facility load" might fail if load spikes beyond expectations during stress (cooling systems working overtime, security systems ramped up, etc.).

## Related Cases

- [[case-business-continuity]] — The broader business continuity planning that encompasses generator fuel and failover
- [[case-disaster-recovery]] — DR site activation and failback procedures
- [[case-load-balancers-and-proxies]] — Load distribution across multiple data centers

