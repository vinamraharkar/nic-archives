---
title: "Network Management System"
publication: "Informatics"
issue_date: "July 2008"
pages: [33, 34, 35]
author: "Vivek Verma"
section: "Technology Update"
---

## Network Management System

Network management is arguably one of the most important challenges faced by the owners and operators of advanced networks and services. This resulted in an urgent need to have an automated network management integrated across diverse environments. A standardised management framework contributes to making that network easier and cheaper to operate and maintain and clearly reduces overhead, speed up fault resolution and aid in capacity planning.

Network management provides the means to keep networks up and running in as orderly a fashion as possible. It includes planning, modeling, and general operation and also provides command-and-control facilities. International Standards Organisation (ISO) has divided the network management task into five conceptual areas (FCAPS), mentioned below:

*   Fault: Any device at some point can become faulty, and virtual connections, links, and interfaces can go up or down thereby generating network fault data. Fault Management takes care of the detection, isolation, resolution, and recording of network problems, before they degrade network performance noticeably. It should be automated as much as possible and rely heavily on the use of the Simple Network Management Protocol (SNMP), either to poll the network for health reports or to accept reports asynchronously from various network devices. Various reporting mechanisms, such as colour changes, flashing icons or audible alarms may be used to alert operations staff members of potential problems.
*   Configuration: All devices tend to require some type of configuration or tuning. Configuration settings may be both written to and read from devices. It also involves maintaining a database, describing all devices within the network. This database may contain both physical and logical configurations, including hardware and software versions, and provides a means to track network upgrades and, in the event of failure, to roll back to an earlier configuration.
*   Accounting: Billing for service is an important component of enterprise network management (e.g., for departmental service billing). This function can be used for charging back the use of resources, such as dial-up facilities, to individual departments as well as for verifying the bills submitted by a service provider.
*   Performance: Performance management involves monitoring the network, sounding alerts when certain thresholds are exceeded and collecting statistics that enable the administrator to predict future needs and perform capacity planning. As user populations and bandwidth needs grow, it is essential to be able to measure performance in order to avoid onset of congestion.
*   Security: It covers the control of access to any information on the network including host and database access mechanisms, firewalls, transactions logging and a myriad of other security-related functions that prevent intentional or unintentional misuse of resources and ensuring the overall operational integrity of the network. This includes limiting, controlling, and recording the access and abuse of routers within the core and distribution networks, as well as authenticating routes and applying policies. Attacks against networks can include unauthorized access, data modification or theft and so on. Security is needed to ensure that both data and the underlying network are protected.

Providing all this management capability is a big challenge, especially for large distributed networks containing lots of legacy equipment. A good management system should therefore, fulfill all the FCAPS areas, which are inter-dependent.

Network Management Systems (NMS)

A well-structured NMS is an integrated conglomeration of functions that may be on one machine but may span thousands of miles, different support organisations and many machines and databases to assist the network managers with Graphical representation of the state of the network; Downloading, uploading and tracking device configurations; SNMP polling, trap collection and logging; Showing historical information via graphs, tables or simple ASCII outputs; Provide automatic network management with minimal human interference; Keep the performance of the network at very high levels; Protect network from hackers and unauthorized users; Control the network traffic, network security, network resource management; Detection and correction of network malfunctions (both hardware and software)

SNMP is used in network management systems to monitor network-attached devices for conditions that warrant administrative attention. It consists of a set of standards for network management, including an application layer protocol, a database schema and a set of data objects. Some network operators use a script-based approach to setting up and monitoring devices which involves writing large and complex vendor specific scripts adhering to manufacturer's CLI.

NMS Architecture

NMSs can be arranged in a centralized, hierarchical or fully distributed architecture; as below

Centralised architecture: It is the most cost-effective solution for smaller networks, with NMS located physically at a “well-connected” point in the network. Some of the limitations of such setup are that it introduces a single point of failure in two ways: by the NMS being cut off from the network due to network failure and because of failure of the NMS itself. It does not scale well and funneling of network-management data from polling/traps can consume enormous bandwidth and high CPU load.

Hierarchical architecture: Each element, or sub-NMS, is responsible for managing the facilities within its level of the hierarchy. NMS may also request reports from sub-NMS elements lower (or possibly higher) in the hierarchy. This arrangement alleviates the scaling problem, but still suffers from increased levels of criticality at the upper levels of hierarchy with a single point of failure at the top of hierarchy.

Distributed Architecture: It offers the most scalable and reliable architecture in which each sub-NMS element is relatively autonomous and responsible for a certain area of the network and is a peer with other sub-NMS elements. Distributed NMS architectures are much more complicated than centralized architectures as there is a need to exchange and synchronize reports and data.

Benefit of using NMS

A good quality NMS broadens the operator's view of the network thus leveraging the increasing intelligence of modern Network Elements. If Network Elements do not support SNMP, then an NMS can facilitate a superior CLI because security can be imposed, actions are recorded and scripts can be managed (stored, updated, etc.). Apart from providing network-wide object support for service profiles, it also gives an overview of an entire network which helps in creating objects like connections particularly useful for aggregate objects. It maintains useful records and audit trails of past configuration/ actions facilitating useful network-wide services like traffic engineering, QoS (Quality of Service), planning, modeling and backup/restore of firmware/configuration data. Besides, fast access to faults and some network faults can be meaningfully processed only by an NMS thereby assisting in rebalancing networks as networks expand and new switches and routers are added.

NMS Packages

Some of the common NMS packages are

*   HP OpenView (http://www.openview.hp.com)
*   IBM Tivoli Netview (http://www.tivoli.com/products/index/netview/)
*   Castle Rock SNMPc (http://www.castlerock.com)
*   Computer Associates Unicenter TNG Framework (http://www.cai.com)
*   Veritas NerveCenter (http://www.veritas.com)
*   GxSNMP (http://www.gxsnmp.org)
*   OpenNMS (http://www.opennms.org)

NMS is expected to be able to deal in terms of services rather than just connections and devices. It must also increasingly support high levels of Reliability, Availability - failover for the entire system or just a critical component such as the database and Maintainability - the software should be written to easily support future extensions.

2nd IEEE International Symposium on Advanced Networks and Telecommunication Systems
December 15th - December 19th, 2008
Mumbai, India
http://www.antsconference.org/index.html

The 2008 IEEE International Workshop on Cyberspace Safety and Security
December 12, 2008
Sydney, Australia
http://2008css.googlepages.com/

IARCS Annual Conference on Foundations of Software Technology and Theoretical Computer Science
December 9th December 11th, 2008
Bangalore, India
http://www.fsttcs.org/

IEEE 6th International Conference on Computational Cybernetics
November 27th - November 29th, 2008
Stara Lesná, Slovakia
http://www.bmf.hu/conferences/iccc2008/

Workshops in ICT 2008 - University of Malta
November 17th- November 18th, 2008
Malta
http://www.um.edu.mt/ict/events/wict

10th International Conference on Distributed Computing and Networking
January 3rd - January 6th, 2009
Hyderabad, India
http://www.iiit.ac.in/ICDCN09/
