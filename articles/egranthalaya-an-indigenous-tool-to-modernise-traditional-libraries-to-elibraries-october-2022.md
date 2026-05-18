---
title: "eGranthalaya - An Indigenous tool to modernise traditional libraries to eLibraries"
publication: "Informatics"
issue_date: "October 2022"
pages: [21, 22, 23]
author: "Mohan Das Viswam"
section: "eGov Products & Services"
---

## eGranthalaya - An Indigenous tool to modernise traditional libraries to eLibraries

Libraries play a vital role in the overall development of society by providing a variety of information services to citizens. In the modern era of information, they have become an integral part of both public and private organisations, enabling their employees to satisfy their information requirements and perform their duties effectively.
According to one estimate, only a few thousand libraries are fully automated, whereas the majority of libraries are either partially automated or have not yet begun the automation process. When presented with a challenge, NIC has taken the initiative to computerise government libraries by implementing eGranthalaya software. This initiative has helped libraries to transform themselves and become eLibraries in order to meet the growing information needs of library members.

eGranthalaya is a digital platform developed for the automation and networking of Government Libraries. It helps in converting traditional libraries to eLibraries. It provides a complete solution for Library Computerisation with Integrated Library Management Software, a Digital Library Module, and a Library Portal. Currently, it has been implemented across 6000 libraries, including Rashtrapati Bhawan and PMO Library.

eGranthalaya Introduction
eGranthalaya first started as an internal project at NIC Karnataka State Centre. The initial version was created for the Karnataka State Public Libraries. Realising its immense potential, the project was subsequently given to the NIC Library and Information Services Division, which assisted the software in reaching its full potential. The application was redesigned with input from library professionals, who helped in improving the user interface and streamlining the workflow of library functions so that it can be used in any type of library.

Technology Overview
eGranthalaya was originally developed using Microsoft Technologies and was using the same till its third release. However, in consideration of the utility, economy, and popularity of Open Source technologies, efforts are being made to migrate the application onto the same in a phased manner.
In the first phase, the back-end component of the application has been migrated from Microsoft SQL Server to PostgreSQL, an Open Source database management system.
In subsequent phases, it is decided to migrate the front-end components of the application to an Open Source platform. Currently, the front-end is built with ASP.NET 4.0 and runs in a Windows environment using .NET Framework 4.7.
Table 7.1 shows the evolution of eGranthalaya over a period of 18 years since its first release.

eGranthalaya 4.0
eGranthalaya 4.0 is a web-based, cloud-ready application that can be used by member libraries for live data entry, issue-return, and other member services. It is hosted on NIC Cloud as a SaaS application in cluster mode with a central database for a group of libraries.
The benefits of the cloud version include the avoidance of local application installation, thus not requiring a server at the user’s end; not requiring maintenance or backup at the user’s end; and not requiring the participation of library staff in the implementation process, allowing them to focus solely on utilising the services.
It streamlines in-house activities of the library as well as member services. It helps traditional libraries to transform themselves to Digital Libraries. It provides
• Integrated Library Management Software (ILMS) with Digital Library Module along with a Mobile– Responsive Open Public Access Catalog (OPAC)
• An android-based mobile app for members;
• A cloud-based hosting environment with disaster recovery services
• Training, migration, roll-out services, and Help- desk support
Table 7.2 briefly describes both domain-specif- ic and product-oriented features of eGranthalaya version 4.0.

Technology Used
• Front-end: ASP.NET 4.0
• Back-end: PostgreSQL 14.3
• Interface: CSS/ JavaScript / jQuery with AJAX enabled controls
• Cloud Resources: 6 web servers with a load balancer; 7 database servers; and 2 digital library / file servers (Refer Fig. 7.1)

Architecture
In a three-tier architecture, the presentation layer and business logic layer are hosted on web servers, while databases are hosted on a separate virtual machine (VM).
Many of the common services (email, SMS, RFID, catalogue search) have been integrated as APIs that are consumed by all instances, while several external APIs are integrated within the application layers to download catalogues from external resources. Each cluster consists of a replicated instance of the same application with a centralised database. As depicted in Fig. 7.1, approximately 50 clusters have been created using 15 VMs and one load balancer.

Modules
eGranthalaya 4.0 features two modules. These are described below:

Data Entry Modules
• Database Administration
• Library Administration
• Master Data
• Books Acquisition
• Books Cataloging
• Circulation
• Serials Management
• Micro-Document Manager
• Library Budget
• Staff Search

Web OPAC Module
• Browser-based Interface
• Search Library Catalog
• Basic / Advance Search
• Uses Boolean Operators
• Federated Search
• Results get integrated with Net APIs to
• Display details of the documents from NET
• Recent Additions to Library
• Members Services behind Login
• Access Digital Library Online

Implementation
Since 2002, four versions of eGranthalaya have been released and are Implemented successfully across 6000 libraries in the country. Besides, here are few key stats about implementation of eGranthalaya
• Implemented over 6000 libraries including Rashtrapati Bhawan Library, Prime Minister’s Office Library, Vidhan Sabha Libraries and others
• 2600 libraries are running on NIC Cloud, which has generated 1.92 crore holdings records belonging to 1.16 crore books catalogue records
• 9.36 Lakh members are registered to access eLibrary online
• Over 25000 full-text documents are uploaded
• Over 175 training programmes have been conducted and trained over 4000 librarians

Benefits
eGranthalaya has been developed keeping in view the requirements and workflow of government libraries in the country and provides a user-friendly interface for library staff as well as library members. Some of the key benefits of using eGranthalaya are
• Fully funded and freely available by Government of India
• Follows International standards prevalent in libraries such as MARC21, AACR2, UNICODE, SRU / SRW, Z39.50, NCIP / SIP2 for RFID, Barcode, Smart Card, E-Books Viewer, XML / JSON based web services, W3C standards
• Integrated with Open APIs such as RFID, ISBN Downloader, News API, ILL API and Portal API, to extend its services beyond the scope of platform
• Stable product releases
• Standard tools for Library Automation
• Android-based mobile app for library members Built-in Data migration service
• Shared cataloging
• Union catalog as a by-product
• Mobile responsive OPAC
• Integrated with email and SMS for generating alerts and notifications
• Nominal cost for setup by NICSI
• Training and tech support by NICSI

Way Forward
eGranthalaya is not only an ILMS product, but it has evolved as a go-to solution for government libraries with the passage of time. In future, in order to take it to a new level as a discovery tool, it will feature a more powerful search engine. It will be integrated with other similar products, including the Union Catalog and Shodh Ganga of INFLIBNET, the National Digital Library of IIT Kharagpur, and the Union Catalog of DELNET. This will aid in the development of an integrated network of automated libraries—a system with a single access point.
