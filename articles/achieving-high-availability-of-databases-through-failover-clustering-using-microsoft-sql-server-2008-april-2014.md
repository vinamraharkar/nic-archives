---
title: "ACHIEVING HIGH AVAILABILITY OF DATABASES THROUGH FAILOVER CLUSTERING USING MICROSOFT SQL SERVER 2008"
publication: "Informatics"
issue_date: "April 2014"
pages: [29, 30]
author: "R. Gayatri, P. Gayatri"
section: "Technology Update"
---

## ACHIEVING HIGH AVAILABILITY OF DATABASES THROUGH FAILOVER CLUSTERING USING MICROSOFT SQL SERVER 2008

One of the major challenges which IT systems face today is ‘System Availability’. Availability is critical in terms of components viz., Web Server, Database Server, and Network. Without availability, services fail, SLAs exceed, revenue is lost and finally a bad publicity can leave a lasting effect on end-users. Availability of an IT system is being measured in currency, not in time anymore. Right strategies have to be adopted to make systems Highly Available. For a database, it’s not just availability but preservation without loss of data (till the point of failure) which is very important. SQL Server 2008 provides various High Availability technologies like Backup, Clustering, Mirroring, Log shipping and Replication. This paper gives an overview of High Availability technologies with primary focus on the Database Failover Clustering.

BACKUP & RESTORE
Generally Backup and Restore facility is not considered as a feature of availability. However, at some point, a need for restoring a backup always arises.
Important
• Know where backup is located.
• Test the backup randomly while performing a restore.

DATABASE MIRRORING
Database mirroring is one of the solutions to increase the availability of a SQL Server database and minimize or avoid server downtime. Mirroring requires creation and maintenance of redundant copy/copies of a database. Data Redundancy ensures that at least a copy of database is always available and remains accessible during the failure of primary database.
It is recommended to use AlwaysOn Availability Groups since mirroring will be removed in future versions.

LOG SHIPPING
Log shipping is considered as a technique than a technology. Database availability through log shipping is achieved by maintaining a backup server that can replace production server in the event of any failure at the Primary. The process includes-sending of transaction log backups from a primary database to one or more secondary databases automatically and restoring them at the receiving end there by bringing synchronization between the primary and the secondary database(s). An optional monitor server instance keeps recording the history and status of backup and restores operations. It raises alerts if these operations do not occur as scheduled.

Figure 1 – Active/Passive DB Clustering

REPLICATION
Definition (Source: MSDN): Replication is a set of technologies for copying and distributing data and database objects from one database to another and then synchronizing between databases to maintain consistency. SQL Server supports various types of Database Replication viz., Snapshot Replication, Transactional Replication, Transactional Replication with Updatable Subscriptions and Merge Replication. In any replication, there are important components called Publisher (Source Database), Subscriber (Destination Database), Article (Information to Replicate) and Distributor (Information Delivery Agent).

DATABASE CLUSTERING
SQL Server Failover Clustering is designed to provide high server availability. It helps keep applications online most of the time. When done properly, it makes the database highly available. Termed as Microsoft Cluster Service (MSCS), this works at the database level. Two systems are connected and configured in a Cluster. If primary server fails or is purposely brought down, SQL Server processing switches to the clustered system. This switch is known as Failover. Failover is designed to minimize system downtime.

Figure 2 – Failover Scenario

Once a failover occurs, the failed system may be restored, brought back online, and then it is possible to switch processing back to the restored system – this is called Failback.

HOW CLUSTERING WORKS?
In traditional setup between web and database servers, hardware/network failure on database side brings the whole service to a standstill.
Figure 1 gives Clustered Database Setup. This solution operates in active/passive (with Cluster Node 1 active and Cluster Node 2 passive) mode, which means that at any point in time only one of the nodes in the cluster is active.
The active node keeps writing data to a location on the shared drives called Quorum. Quorum is used to share state information whenever the cluster fails-over from one node to next. Quorum is basically a log file (like database logs). Its purpose is to record every change made on the active node. Thus, every recorded change in Quorum gets applied to passive node during active node failure. A signal called Heartbeat is periodically sent across the private network connection between servers. The passive node checks for Heartbeat and whenever owning resource is unavailable, it takes ownership of cluster resources and starts reading state information from Quorum.
Figure 2 shows Failover state where active node experiences failure and passive node takes over (ensuring minimum disruption). The failover is automatic and managed by Failover Cluster Manager. Once Node 1 is repaired and ready for use, Failback can be initiated from Failover Cluster Manager.
To conclude, there are situations where Clustering holds high importance and also situations when Clustering does not have a role.

Situations where Clustering is of Use
• Hardware failures
• Applying security patches, Windows Updates
• Transparent to calling application
• All databases, logins, agent jobs in Failover come-up together as single unit without scripting or configuration
• Clustering is additional tool in troubleshooting toolkit

Situations where Clustering has no role
• Doesn’t impact system performance
• No guarantee for storage availability. Doesn’t save space, effort for backups, maintenance. All maintenance to go as usual.
• SSRS (SQLServer Reporting Services) not “Cluster-aware”
• No guaranteed 100% availability. There could be downtime when SQL Server instance is “failing over” or moving between nodes.
