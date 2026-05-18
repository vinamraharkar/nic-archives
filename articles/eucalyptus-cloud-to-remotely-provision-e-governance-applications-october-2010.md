---
title: "Eucalyptus Cloud to Remotely Provision e-Governance Applications"
publication: "Informatics"
issue_date: "October 2010"
pages: [28, 29, 30, 33]
author: "CSR Prabhu"
section: "Technology Update"
---

## Eucalyptus Cloud to Remotely Provision e-Governance Applications

Cloud computing can be defined as on-demand, scalable and elastic web services on public or private fabric consisting any of grid, cluster, virtual machines and physical machines. Ensuring high reliability, scalability, high availability of citizen centric e-Governance services is very important. Cloud computing makes it possible to accomplish this task cost effectively.
T
HE open source Infrastructure as a Service (IaaS) cloud based on Operating System virtual- ization (Xen, KVM, VMWare, HyperV) allows leasing computing as a utility.
IaaS Cloud allocation is
Set of Virtual Machines Set of storage resources Private network to minimize secu- rity vulnerabilities Application Virtualization
IaaS Benefits:
Share under-utilized software, net work, storage resources Efficient Server provisioning Effective Data Persistence
CURRENT STATUS OF PROTOTYPE
The Govt. of India, Department of Information Technology, has initiat- ed National e- Governance Plan (NeGP) for the execution of e-gover- nance projects in the country, both at Central and State levels. It has identified "Mission Mode" Projects at both the levels. The NeGP propos- es citizen service delivery up to the village level through common serv- ice delivery outlets and ensure effi- ciency, transparency & reliability of such services at affordable costs to realize the basic needs of the com- mon man. The citizen services to be delivered could be based on the Service Oriented Architecture para- digm (as against the present web enabled services). These services expect adequate networking and computing resources for effective and efficient service delivery.
National Informatics Centre (NIC) of the Department of Information Technology is providing network backbone and e-Governance support to Central Government, State Governments, UT Administrations, Districts and other Government bod- ies. It offers a wide range of ICT serv- ices including Nationwide Communication Network for decen- tralized planning, improvement in Government services and wider transparency of national and local Governments. SAN (Storage Area Network) Data Centers and SWANs (State Wide Area Network) have been established in all 35 states/UTs through NIC as a part of NICNET.
Presently SAN and SWANs are individually connected and are inde- pendently operating without any resource sharing or even without any replica or mirroring storage else- where. By connecting all these Data Centers (SAN) into a cloud, all the computational resources such as the CPUs, disk storage systems, special- ized software systems, etc., can be provisioned to all the users connect- ing to the cloud, including sophisti- cated users needing advanced capa- bilities like remote application host- ing space, data storage on cloud, per- sistent transaction states, and dis- tributed data mining.
Also, NIC is having various appli- cations which are running under dif- ferent platforms and operating with- out any resource sharing. These applications often need to interact with each other and may also need additional resources temporarily, for a small duration of time. There are many critical mission mode applica- tions where the services of computer are continuously required for any kind of citizen services. Under these cir- cumstances, breakdown of any machine or operating system or data- base server or application server brings the services to the citizens to a standstill. Hence, it is required to plan a business continuity model for such applications. Using the enabling tech- nologies enumerated below, the appli- cations can be deployed as web servic- es in the container to make them inter- operable and solution for business continuity plan (BCP) and disaster management and recovery (DR) can be provided.
HIGH PERFORMANCE ARCHI- TECTURE FOR A TYPICAL e-GOVERNANCE SERVICE
To ensure high reliability, availability and business continuity following empirical architecture is suggested for e-Governance applications.
The architecture has been devised based on the experience gained in launching several e-Governance appli- cations by NIC. The architecture com- prises following layers.
Governance Content Management Layer
Application Frameworks Layer
Service Mediation Layer
Process Service Layer
Interface Integration Layer
Client Layer
Management and Monitoring Layer
ENABLING TECHNOLOGIES
Given below are the cloud technolo- gy platform, grid and grid based cloud platform, data mining platform over grid and cloud.
Introduction to Eucalyptus
Elastic Utility Computing Architecture for Linking Your Programs To Useful Systems (EUCALYPTUS) -- is an open- source software infrastructure for implementing Elastic/Utility/Cloud computing using computing clusters and/or workstation farms. Eucalyptus is a distributed computing system implemented using commonly avail- able Linux tools and basic Web-service technologies. Eucalyptus implements private/hybrid cloud. A Eucalyptus cloud setup consists of five types of components. The cloud controller (CLC) and "Walrus" are top-level com- ponents, with one of each in a cloud installation. The cloud controller is a Java program that offers EC2- compat- ible SOAP and "Query" interfaces, as well as a Web interface to the outside world. In addition to handling incom- ing requests, the cloud controller per- forms high- level resource scheduling and system accounting. Walrus, also written in Java, implements bucket- based storage, which is available out- side and inside a cloud through S3- compatible SOAP and REST interfaces.
Top-level components can aggregate resources from multiple clusters (i.e., collections of nodes sharing a LAN seg- ment, possibly residing behind a fire- wall). Each cluster needs a cluster con- troller (CC) for cluster-level scheduling and network control and a "storage con- troller" (SC) for EBS-style block-based storage. The two cluster-level compo- nents would typically be deployed on the head-node of a cluster (in fact, this is required if the cluster is behind a fire- wall). Finally, every node with a hyper- visor will need a node controller (NC) for controlling the hypervisor. CC and NC are written in C and deployed as Web services inside Apache; the SC is written in Java. Communication among these components takes place over SOAP with WS- security.
Euca2ools are command-line tools for interacting with Web services that export a REST/Query-based API com- patible with Amazon EC2 and S3 serv- ices. The tools were inspired by com- mand-line tools distributed by Amazon (api-tools and ami-tools) and largely accept the same options and environment variables. Euca2ools use cryptographic credentials for authenti- cation. Two types of credentials are issued by EC2- and S3-compatible services: x509 certificates and keys. Euca2ools are used to learn about installed images, start VM instances using those images, describe the run- ning instances, and terminate them. Eucalyptus versions 1.5 and higher include a highly configurable VM net- working subsystem that can be adapt- ed to a variety of network environ- ments. There are four high level net- working "modes", each with its own set of configuration parameters, features, benefits and in some cases restrictions placed on local network setup.
Features of Eucalyptus 1.6.1 include:
Deployment on multiple clusters Deployment of components (Cloud controller, Walrus, Storage Controller, Cluster Controller) on different machines Enhanced maintenance support: components are now "crash consis- tent," maintaining state across process restart or machine crash Enhanced concurrency manage ment: cloud requests are serviced asynchronously with minimal lock- ing using eventual consistency for scale.
Networking improvements, includ- ing multi-cluster support Building and installation improve- ments
ISSUES
Some of the business-cases include:
Remote provisioning of Virtual Servers for application develop- ment and hosting :
The virtualization technologies in Eucalyptus, Nimbus allow efficient resource usage of the servers by decou- pling an operating system and the services and applications supported by that system from a specific physical hardware platform. Given specifica- tions, suitable virtual machine can be created and maintained at the nation- al and state data centers where required hardware, network exist. These virtual machines are remotely accessible by the users from interior areas of the states without the need to have the same facilities as those in state capitals. The provisioned virtual machines can then be used for applica- tion development and prototyping, hosting production environments con- sisting of operating systems, applica- tion servers, database servers, middle- ware systems.
Cloud Storage :
Eucalyptus distributed file system Walrus allows use-cases as diverse as effective backup of data securely, snap- shots of virtual machine states for per- sistence, seamless addition of load bal- ancers and application servers through snapshots, elastic IPs, VLANs and Security Groups.
Application Virtualization in Cloud :
From a value-add standpoint, applica- tion virtualization is more than cost effective hardware use and remote software hosting. Given a enterprise service registry, cloud layer abstracts enterprise infrastructure to dynami- cally provision network, storage, appli- cations according to user specifica- tions. Cloud layer of architecture inter- faces with other application layers through web services, thus enabling on-demand scalability, availability, interoperability of applications.
RECOMMENDATIONS
To ensure interoperability and inte- grate processes, create web service wrappers for existing application software. Develop new applications within the framework of SOA (Service Oriented Architecture) with the above mentioned layered architecture.
Setup IaaS cloud at national, state data centers. The resulting virtual machines can then be provisioned to remote locations like villages, talukas and even districts without incurring additional costs on infra- structure.
The virtual machines can be further utilized for application hosting, data and server migration over the cloud.
The Cloud can also be used for BCP (Business Continuity Planning), DR (Disaster Recovery), BPM (Business Process Modeling), Risk Management, Performance Management, Change Management etc.
Specialized e-Governance applica- tions involving data persistence across transactions and distributed data mining systems can be further explored.
Requirement based analysis of SOA Governance, On-Demand BPM and BPEL in IaaS cloud.
PLAN OF ACTION
The follow up Plan of action is pro- posed for implementation:
Web Services have to be developed wrapped around existing (legacy) e- governance applications. For new applications SOA can be adopted. Web Service Repositories can be developed at Central, State and District level. Simultaneously Eucalyptus may be installed in each data centre (on a cluster of at least two Servers) to create virtual machines (locally or remotely) clusters. Virtual Platforms (such as PostgreSQL) can be installed on all Virtual Machines as desired and made available as services. Web Service Repositories can be hosted on Virtual Machines using Virtual Platforms in the data center. Such artifacts shall have pre-config- ured application servers, database servers etc.
Thus, we will have all the three compo- nents of a cloud infrastructure:
IaaS
PaaS, and
SaaS (Web Services)
POC
The implementation of the above plan has been initiated in various States in the country. Initially at Hyderabad Data Centre of NIC Eucalyptus Cloud as IaaS is created and certain applica- tions (in open source platform) have been hosted as IaaS model. At Pune Data Centre of NIC Eucalyptus Cloud as IaaS has been created and e- Procurement application is proposed to be hosted and managed from NIC, Chennai. Similarly Eucalyptus Cloud as IaaS is being created at NIC, Bhopal Data Centre, NIC Trivandrum Data Centre and NIC, Haryana Data Centre, Chandigarh. In other remote locations as NIC Sikkim Data Centre Gangtok, NIC Tripura Data Centre Agartala and NIC Assam Data Centre, Guwahati, the initial steps are being taken towards the installation of Eucalyptus Cloud and hosting applications in SaaS model.
CONCLUSION
The Govt. of India, Department of Information Technology, has initi- ated National e- Governance Plan (NeGP) for the execution of e-gov- ernance projects in the country, both at Central and State levels. National Informatics Centre (NIC) of the Department of Information Technology is providing network backbone and e-Governance sup- port to Central Government, State Governments, UT Administrations, Districts and other Government bodies. SAN (Storage Area Network) Data Centers and SWANs (State Wide Area Network) have been estab- lished in all 35 states/UTs through NIC as a part of NICNET. By con- necting all these Data Centers (SAN) into a cloud, where in all the computational resources such as the CPUs, disk storage system, spe- cialized software systems, etc., will be provisioned to all the users con- necting to the cloud. Using the enabling technologies enumerated, e-governance applications can be deployed as web services to pro- vide interoperability, business con- tinuity, transaction persistence, server provisioning etc.
