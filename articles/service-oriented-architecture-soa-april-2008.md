---
title: "Service Oriented Architecture (SOA)"
publication: "Informatics"
issue_date: "April 2008"
pages: [33, 34, 35]
author: "Srinivasa Raghavan K"
section: "Technology Update"
---

## Service Oriented Architecture (SOA)

This article describes the concept of Service Oriented Architecture (SOA), its benefits with Web Services and its impact on an organisation. The author recommends implementing SOA right now to survive in this competitive world. The adoption of such architectures in our software development process has resulted in achieving features such as separation of business logic from presentation, enhanced code re-usability and ease of maintenance etc.

Srinivasa Raghavan K
Senior Technical Director
NIC Tamil Nadu
raghavan@tn.nic.in

It is a well known fact that the development of Enterprise class of application software requires adoption of specific architectural framework and many applications are developed based on either 2-Tier or 3-Tier or N-Tier architectures adhering to various standards. There is no doubt that the adoption of such architectures in our software development process has resulted in achieving features such as separation of business logic from presentation, enhanced code re-usability and ease of maintenance etc.

However, any Organisation will always aim for achieving optimum use of complex heterogeneous computing environment spread across the Enterprise and also the integration and interoperability of the software systems within and outside the Enterprise. A new software architectural framework called Service Oriented Architecture (SOA) has emerged and it is focused on addressing issues such as integration and interoperability of software systems within and outside the Enterprise. SOA differs from other software architectural frameworks quite significantly. Software Services are the building blocks of SOA applications.

To any developer who hears the term SOA, the following questions may come up in her/his mind like: What is a Service Oriented Architecture? Are Web Services and SOA related? What are the kinds of applications that are suitable for SOA? How will it be useful to an organisation? Let us seek answers for these questions.

Service Oriented Architecture (SOA)
W3C defines SOA as “A set of components which can be invoked, and whose interface definitions can be published and discovered.”

In other words, SOA looks at software development as a process of assembling and orchestration of various software modules which are exposed and consumed as services over the network such as Web.

SOA applications are built based on services having well-defined business functionality. These services cane be accessed over web and can then be consumed by different applications or business processes. More over, these services are implementation-independent and can be discovered dynamically. SOA advocates loose coupling between software components.

SOA allows for the reuse of existing systems where new composite services can be created from existing services. In other words, SOA enables businesses to leverage existing investments by allowing them to reuse existing applications and services, and ensures interoperability between heterogeneous hardware and software environment.

SOA and Web Services
Many people think that SOA and Wes Services are same. SOA and Web Services are two different things, but Web Services are the preferred standards-based way to realize SOA. SOA extends Web services capabilities by creation of structures of services, while benefiting from the open standards model that Web services provide.

'Web Services' are software systems designed to implement interoperable machine-to-machine interaction over a network. This interoperability is achieved through a set of XML-based open standards, such as Web Service Description Language (WSDL), Simple Object Access Protocol (SOAP), and Universal Description, Discovery and Integration (UDDI).

Web Service Description Language provides a common language for describing services and a platform for automatically integrating those services. Using WSDL, a client can locate a web service and invoke any of its publicly available functions. With WSDL-aware tools, we can even automate this process, enabling applications to easily integrate new services.

Simple Object Access Protocol is a way for a program running in one kind of operating system to communicate with a program in the same or another kind of an operating system using the Hypertext Transfer Protocol and Extensible Markup Language the mechanisms for information exchange.

Universal Description, Discovery, and Integration (UDDI) is a platform-independent framework for describing services, discovering businesses, and integrating business services by using the Internet.

These standards enable a common approach for defining, publishing, and using web services. The flow diagram depicting the use of Web Services in SOA Applications is given below.

Activities involved in SOA

There are four broad phases of activities in realising SOA. They are

Conceptualization Phase
In this phase, activities such as gathering of requirements, analysis of business processes, mapping business processes on to services, design of service specifications that act as the contract between the service's clients and implementers, documenting the same are carried out.

Assembling Phase
As soon as the services which form part of business processes are designed and specified, they need to be constructed and implemented using some technology like J2EE. The implemented services are then assembled; that is, they are discovered, choreographed and composed to implement the enterprise business processes that meet out both functional and nonfunctional requirements

Deployment Phase
The implemented business processes have to be deployed on a run-time environment that supports the execution of dynamic business processes. The run time should provide open standards-based execution environment to allow services to readily invoke other services. The deployment environment should have the capability to do Protocol translation between various service invocations besides routing among various service providers. Adequate features for security and auditing are part of this deployment environment.

Monitoring Phase
The services and the business processes that are executing on the run time are monitored and analyzed to ensure their smooth operations. Availability and Performance statistics are monitored.

SOA and e-Governance
A lot of applications in e-Governance domain are suitable for adoption to SOA architecture especially those applications where multiple departments have to do some sort of value addition as part of the business processes.

For example if the Land Records Management System and Property Registration System can expose some web services on the network, then these web services can be integrated and orchestrated into a single window application in such a way that any property registration related activities automatically update the ownership details maintained by Land Records department and also associated mutation details if any. Adequate and robust security measures are also part of such application.

Similarly, if the application system at DGFT which interacts with Importers/Exporters can expose some web service and then these services can be consumed by Customs Application for on the fly verification of import/export related documents from such traders, as part of their process logic.

Many leading vendors like IBM, Oracle, SUN etc have come out with tools that will help implementation of SOA. This suite includes components related to Web Services Orchestration and Management, Business Process Management, Service Bus, Monitoring and Management tools.

There is no doubt that in future, most software applications will be delivered and consumed as services only. Therefore, it is imperative that we have to necessarily look at implementing SOA in our software development activities.

ICES 2008 : "International Conference on e-Society"
July 25th-27th, 2008
Prague, Czech Republic
http://www.waset.org/ices08/

eINDIA2008
July 29th - 31st, 2008
Pragati Maidan, New Delhi, India
http://www.eindia.net.in/2008/

ICCIT 2008: "International Conference on Communications and Information Technologies"
August 13th-15th, 2008
Vienna, Austria
http://www.wahss.org/iccit08/

International Conference on Soft Computing as Transdisciplinary Science and Technology
October 26th -30th, 2008
Cergy-Pontoise Paris, France
http://sigappfr.acm.org/cstst08/index.php

ECEL 2008: 7th European Conference on e-Learning
November 6th-7th, 2008
Agia Napa, Cyprus
http://www.academic-conferences.org/ecel/ecel2008/ecel08-home.htm

IEEE International Conference on Data Mining
December 15th - 19th, 2008
Pisa, Italy
http://icdm08.isti.cnr.it/
