---
title: "UPSC’s new ICT Infrastructure setup"
publication: "Informatics"
issue_date: "July 2018"
pages: [26, 27, 28, 29]
author: "K S NAGESH; ASHUTOSH GUPTA; PUJA KHATTRI"
section: "e-Gov Products & Services"
---

## UPSC’s new ICT Infrastructure setup

Designed and Implemented for efficiency improvement and uninterrupted availability
UPSC Projects are mission critical projects with the fixed timelines and these projects have to be implemented successfully on time. This new ICT setup is capable of handling huge load on the UPSC servers smoothly and efficiently. The performance of the system has improved drastically due to the enhanced capacity of servers and the modifications made in the system

The Software for various examinations of UPSC such as the prestigious Civil Services Examinations (flagship exam of UPSC), National Defence Academy (NDA), Enforcement Officer/ Accounts Officer (EPFO) etc., are handled by UPSC using the software SOAP (System of Online Application Processing). The various recruitments in different ministries are handled by UPSC using the software, ORA (Online Recruitment Applications). Apart from these two major applications, various software applications like e-Admit Card(s), e-Summons, detailed application form(DAF), All India Service (AIS) etc., are deployed on the website https://upsconline.nic.in. The physical servers were commissioned in the year 2010. It is observed that there is an annual increase of 15 percent in the number of applications received by UPSC. Hence, the load on the servers has increased considerably over the years since its inception. In order to address the increasing demand of applications on the UPSC servers, NIC along with UPSC Officials has suggested that UPSC should go for the strengthening of UPSC hardware setup. It was suggested that new ICT setup has to be replaced with high capacity servers and different system architecture, both at application layer as well as database layer for better performance of the system. The funding of the project has been entirely by UPSC.

BACKGROUND AND THE OLD ICT SETUP
UPSC Projects are mission critical projects with the fixed timelines and these projects have to be implemented successfully on time. It was observed that in the last few days of the closing date of online applications for any given examination/ recruitments, the online traffic is very high, leading to slow response time from the servers, especially during the high candidature examinations for Civil Services Preliminary, National Defence Academy (NDA), Enforcement Officer/ Accounts Officer (EPFO) etc. The present system is not able to fully cope up appropriately with the high traffic surge due to high candidature.

UPSC was earlier having five rack mounted servers (Server configuration. - 4 processor with 8 core 2 GHz Intel CPU and 256 GB RAM). There were three application servers, which are connected to load balancer for the distribution of load among three servers. The two database servers were being used in active passive cluster mode. The Redhat Linux Version 6.4 has been installed in all these servers and PostgreSQL 9.4 has been used as database. The different applications of UPSC like SOAP, ORA, e-Admit etc. were running on these servers. There were two application servers and one database server.

NEW ICT SETUP AND SYSTEM ARCHITECTURE
The old architecture was designed in the year 2010 and since then it had been working fine, but as the physical server hardware was seven years old and the number of software applications i.e., load on the server has also increased exponentially, UPSC has decided, in consultation with NIC, to replace the existing servers with the new high-end robust servers having high CPU performance, more CPU core, high memory and other related components etc., with new system architecture. It was proposed to replace the existing hardware (Servers) - ICT setup with new ICT Setup which should have the capacity to cater the future additional demands of UPSC. The candidates traffic is increasing about approximately 15% per year, so, the hardware and system architecture should be designed in such a way that it can take care of the load for at least next five years.

UPSC also has a setup for staging environment that duplicates the production environment (same hardware, same software and same settings). UPSC now evaluates/ tests their application code before being placed into production.

In the Disaster Recovery (DR) site, the Application Servers as well as database servers are replaced with high capacity servers having 4 processors with 10 Core and 512GB RAM/ 1 TB RAM.

TECHNOLOGIES USED IN NEW SYSTEM ARCHITECTURE OF UPSC
APPLICATION SERVER
There are four physical application servers installed which are used for virtualization. These servers are high-end configuration (4 Processors having 10 core with 512 GB RAM). Red Hat Enterprise Virtualization Manager was used to virtualize the servers.

The four physical servers are virtualized to create the Virtual Machines (VM) i.e., each application server/ hypervisor is running 3 VMs over it behind the hardware load balancer. Each VM is capable to handle 1000 to 1500 concurrent applications. Twelve virtual machines are connected to Network File System (NFS) server storage to store candidates’ details like photos, signatures and documents (in pdf format). All UPSC physical servers have been connected by 10 Gigabit network connectivity with 1 Gigabit network connectivity as a secondary network.

It delivers a centralised management system to administer and control all aspects of a virtualized infrastructure from host and guest management through storage management and high availability. Red Hat virtualization for servers builds upon the Red Hat Enterprise Linux platform and consists of the following two components:

RED HAT VIRTUALIZATION HYPERVISOR
This is the server (or cluster of servers) that runs the virtualization layer, and then runs several virtual server instances on top of it. A hypervisor is a function which abstracts/ isolates operating systems and applications from the underlying computer hardware. This abstraction allows the underlying host machine hardware to independently operate one or more Virtual Machines as guests, allowing multiple guest VMs to effectively share the system's physical computer resources, such as processor cycles, memory space, network bandwidth and so on. It is also referred to as Virtual Machine Monitor.

RED HAT VIRTUALIZATION MANAGER (RHVM)
It is a software tool that provides centralised management over the physical and logical resources available within an environment, virtualized with Red hat Virtualization. This functions as management server for the entire virtual environment. RHVM also includes a comprehensive system dashboard enabling virtualization administrators to see an overview of the environment, and also to drill down into operational and performance details of any VM in the setup.

PostgreSQL DATABASE SERVERS WITH EFM
Three high-end physical servers having server configuration, 4 Processor with 10 core 2.1 GHz Intel CPU and 1TB RAM, is running in the new server setup. The database server is running on Master- Slave mode. As high availability is required, one master and two slave concepts have been implemented. Real-time replication is running in these two slave servers. EnterpriseDB Failover Manager (EFM) utility is being used for database servers. EFM monitors the members of a PostgreSQL cluster, identifies and verifies database failures quickly and reliably, and if needed, promotes a standby mode to become the cluster master and issues alerts. To handle the peak load/ connections which come during the starting weeks and closing weeks of an examination/ recruitment, connection pooler utility (PgBouncer) has been installed on each DB server. The PgBouncer is a lightweight connection pooler for PostgreSQL that dramatically reduces the processing time and resources for maintaining a large number of client connections to one or more databases.

SOLUTION TO THE TECHNICAL CHALLENGES
It has been observed for the last couple of years that during the peak load (first week and the last few days of the closing date of online application filling process) for any important examinations like Civil Services Examinations (Preliminary), NDA etc., the number of applications received on the servers used to be huge, which creates a heavy load on the UPSC servers, which in turn creates high concurrent connections on the application servers. It has also been observed that sometimes servers start responding very slow and database servers were also unable to respond quickly to the request received from application servers during peak loads.

The new system architecture is designed to address the above mentioned issues which were identified in the UPSC old system setup. The old servers were replaced with the new high capacity servers both at the application level and at the Database level. The Database Server is installed with PostgreSQL and augmented with EnterpriseDB Failover Manager (EFM) utility, which enables database server with one master and two slaves in order to manage the failover of databases. Connection pooling utility (Pgbouncer) has been installed on each database server. It reduces the processing time and resources for maintaining a large number of client connections to one or more databases.

The new ICT setup of UPSC has been put on the production environment in January 2018. The new ICT setup has successfully handled major examinations of UPSC like Civil Services Examinations (Preliminary) 2018, NDA-I 2018 etc. More than 12 Lakhs candidates (approx) have successfully applied for CSP-2018 exam on the new ICT setup. One lakh (approx) candidates have filled the application forms of the Civil Services Examinations (Preliminary) 2018 on closing days without any problems. The UPSC servers are functioning smoothly and efficiently and are able to handle the peak loads effectively.

DEVELOPMENT ENVIRONMENT
The various open source software tools used in the new ICT setup of UPSC both at the application layer as well as database layer are as detailed below:

APPLICATION LAYER
RHV Manager (Version 4.1), PHP (Version 5.4), Java (Version 1.8), Apache (Version 2.4.6)

DATABASE LAYER
Redhat Linux (Version 7.4), Java (Version 1.8), PostgreSQL – (Version 9.6), EnterpriseDB Failover Manager (Version 3.0)

STATISTICS OF THE EXAMINATIONS & RECRUITMENTS OF UPSC
The statistics of the major examinations conducted by UPSC like CSP and NDA-I are as shown in the Table-1. The statistics of the various recruitments is as shown in Table-2. The Figure-1 shows the graphical representation of the major examinations like NDA-I and CSP conducted by UPSC for the last few years. The new ICT setup of UPSC has successfully handled the peak load on servers as shown in Table-1 and Table-2.

The Figure-2 shows the load balancer connection statistics of UPSC. It has been observed that approximately 30 crores new TCP connections had been successfully made on the last day of application filling of Civil Services - Preliminary exam-2018.

CONCLUSION
The new ICT setup of UPSC was implemented successfully within the timeframe given by UPSC. The setup is capable of handling huge load on the UPSC servers smoothly and efficiently. The Multiple Applications of UPSC like SOAP, ORA, e-Admit card, DAF, e-Summons etc., are already running successfully on the new ICT setup. The new servers are able to handle the heavy load coming from different examinations and recruitment advertisements of UPSC with good response. The performance of the system has improved dramatically due to the enhanced capacity of servers and the modifications made in the system architecture at the Application Layer & Database Layer. The enhanced performance is also due to the fine tuning and optimization of source code of the various UPSC applications like SOAP, ORA etc.
