# Postmortem

### Issue Summary
For 6 minutes from 0233 to 0239 on 15Sep94, service was unavailable on smallbusiness.com. Users would experince a 'This site can’t be reached' error. The root cause was that the server was accidentally powered off. The number of users is unaffected, but based on the historical usage of the site during this time, an estimated average of 4 users may have been affected.

### Timeline
- **02:15 CST**: Engineering brought child into server room
- **02:33 CST**: Child accidentally depowers server by hitting power switch on power strip
- **02:33 CST**: Engineering notices that server was powered off
- **02:33 CST**: Engineering powers server back on
- **02:36 CST**: Server is live

### Root Cause and Resolution
Non-authorized personnel was allowed access to the physical server, and the server power system has no fail-safe. The root cause was a combination of loose access controls, and a single point of failure for the server power.

### Corrective and Preventative Measures
Server should be placed in a more secure area so that tampering is reduced. Furthermore, an uninterruptible power supply should be invested in to provide a more robust power source.

Based on a true story.
