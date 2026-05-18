---
title: "IntraGOV Portal Framework- Bringing Services Together"
publication: "Informatics"
issue_date: "October 2007"
pages: [29, 30, 48]
author: "Saroj Kumar Patro, Kapil Kumar Sharma"
section: "E-Gov. Products & Services"
---

## IntraGOV Portal Framework- Bringing Services Together

The objective of IntraGOV Framework is to provide a comprehensive and integrated G2E/G2G solutions for various e-government implementations. Realising the power of present day e-governance, the portal is a noteworthy step towards good governance and shall go a long way in streamlining e-information and services at a single point to the employees and as well as to the government. Efficient and timely delivery of services through extensive use of information and communication technology has revolutionised the concept of governance and enhanced its effectiveness. Empowerment of the employee with the deployments of G2E/G2G solutions plays a vital role in motivating employees and obtaining their commitment for total e-government implementations. IntraGOV portal framework - “Bringing Services Together”, an to provide a one-stop access point to organisation information and services, a flexible Platform for Document Management, Content Management, Collaboration and Workflow modules. Background Many governments and departments have started implementing electronic delivery of services targeted to its citizen, peer departments, the business community, and to the employees. An IntraGOV portal is a G2E solution developed by National Informatics Centre, with an aim to empower employees of an Organisation by bringing services, applications, office automation process together under one roof using a single window entry platform.
The main objective of the IntraGOV portal is:
¡ To provide a platform for personalised, role-based secure to one stop access point to all disintegrated applications and services that enables employees to receive electronic notifications of services and transactions based on their needs and contingencies.
¡ Efficient and Timely delivery of information and services in a transparent manner.
¡ To facilitate an environment and work area which can enable employee to create their own portals, add, share, e-mail and print content.
¡ To Build a sound internal infrastructure to facilitate electronic communication, information sharing.
¡ To provide reusable framework for easy and fast deployment across Ministries/Departments
Technology Solutions and Architecture
IntraGOV portal is a web-based software based on Linux/windows platform that has been developed using Zope-Application Server, Plone-Content Management System and Python/TAL (Template Attribute Language) scripting language.
Concurrent users' request to access the services provided by the IntraGOV Portal, passes through FIREWALL, reaches at Switch. The Switch, acting as Load Balancer, dynamically forwards request to one of the server from the farm of computers having least load.
Need for configuring IntraGOV with ZEO:
To make efficient use of the Load Balancer, ensuring highly availability of the portals, IntraGOV setup is configured with Zope Enterprise Objects or ZEO. ZEO is a system/architecture that allows running the portals on more than one computer A Portal serving more requests than it can handle, can affect the steed and responsive or possibly even crash. The obvious solution to this problem is to use more than one computer, each running a separate Zope Instance. But keeping all separate Zope installations synchronized manually can become a huge cumbersome task. Using ZEO, often called clustering and load balancing, the requests are spread evenly around many computers and more computers can be added as the number of requests grows. Further, if one computer fails or crashes, other computers can continue to service requests. ZEO runs Zope on multiple computers and takes care of ensuring that the entire Zope installations share the same database at all times. ZEO uses client/server architecture. The Zope processes are the ZEO Clients. All of the clients connect to one, central ZEO Storage Server (ZSS).
Each machine in that farm having the Apache Server to forward request to appropriate ZEO client. Each ZEO client has its corresponding ZSS. ZEO clients and servers communicate using standard Internet protocols, so they can be in the same room or in different locations. This ZSS is most important in entire setup, because if this is down or unavailable then entire setup is of no use.
This architecture (IntraGOV Setup) has many advantages.
¡ Deals with Single Point of Failure. However it does not fully eliminates the risk as the ZEO storage server now becomes a single point of failure. Keeping ZEO server behind SAN and taking periodic backup minimizes this risk.
¡ Provides the Scalability (allows a portal to increase capacity by adding computing resources to handle the load)
¡ Distribution (Portals can be dynamically distributed to multiple locations in multiple configurations).
¡ Ensures High Availability of portals, programs that have problem are skipped and can be terminated.
¡ The storage of the data is isolated from the application processes, significantly increases the Data Integrity of the portals.
Centralized Authentication Service using OpenLDAP
OpenLDAP, an open source implementation of directory service, has been used in some of the IntraGOV portals to maintain the user data in a central repository. This will enable Authentication, Authorization of user data & thus to remove the ambiguity, discrepencies & redundancy. This is especially useful in an organizational structure where applications run in heterogeneous platforms .It helps authentication from a single and common base of information, regardless of the geographical location.
Other Key Features of IntraGOV Portal are
¡ Cross Platform Support
¡ Multi Language Support
¡ Web Based Interface
¡ Web based Administration
¡ Role Based administration
¡ Auditing
¡ Document Management
¡ Robust search functions
¡ Role Based Security
¡ Non Programmer can deal with portal content management
¡ Provided with Messaging and Collaborative services such as: IM, E-mail Notification, Discussion Forum, private/shared calendars, chat sessions SMS notifications etc for effective internal communications.
¡ Available in Product form: Complete installable version of IntraGOV framework is available in CD.
¡ Associated with Workflow
¡ Integration with external applications (i.e. various in house databases).
The IntraGOV setup Intranet Portal solution provides a single interface to interact with relevant content, applications, processes and information, so employees can do their work more effectively and in a transparent manner. Integrated advanced collaboration features enable users to work together more efficiently via instant messaging, Discussion Forum, alerts and notifications, and etc. Intranet portal based on IntraGOV framework have been successfully implemented at following locations:
— Department of Information Technology
— Government of Orissa
— Ministry of Health and Family Welfare
— Planning Commission
— Ministry of Environment and Forest
— Ministry of Power
— Ministry of Home Affairs
— Ministry of Information and Broadcasting
— Press Information Bureau
— Prime Ministers Office
— Department of Telecom
— Department of Posts
— U.T. of Lakshadweep and many more…
IntraGOV portals are also under implementation at following locations
— Government of Andaman & Nicobar
— Ministry of Civil Aviation
— Ministry of Statistical and Program Implementation
— Department of Official Language and many more…
