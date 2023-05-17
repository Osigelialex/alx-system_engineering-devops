# Incident Report on Server Downtime

## Issue Summary

From 7:47PM to 8:45PM PT, all request to the web servers resulted in a 503 server error.
This issue affected 100% of Users on the application. The root cause of this problem was
a server overload, which resulted in downtime of our servers.

## Timeline

* 7:47: Issue Detected.
* 7:54: Pagers Alerted Teams.
* 8:10: Investgated CPU usage and discovered it was above 80%.
* 8:15: The incident was escalated to the networking teams.
* 8:20: Offloaded serving to other infrastructure.
* 8:40: server restarted.
* 8:45: Incident resolved.

## Root Cause

At 7:47PM there was a traffic spike which overwhelmed our servers. Server performance degraded
drastically as server usage reached 80%. Offloading serving to other infrastructure, reducing
expensive operations, and limiting the quantity of requests helped reduce CPU utilization, 
which ultimately resolved the incident.

## Corrective and Preventive measures

### Improvements

A major factor to prevent this incident is hardware improvement, better servers which are more
suited to handle request from the large user base should be set up.

### Tasks to address issue

* check that CPU utilization is not too high.
* check that system has enough memory.
* Implement a load balancer.
