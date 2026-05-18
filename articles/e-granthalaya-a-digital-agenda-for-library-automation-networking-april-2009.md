---
title: "e-Granthalaya - A Digital Agenda for Library Automation & Networking"
publication: "Informatics"
issue_date: "April 2009"
pages: [13, 14, 15]
author: "M. Moni, Ram Kumar Matoria"
section: "E-Gov Products & Services"
---

## e-Granthalaya - A Digital Agenda for Library Automation & Networking

Libraries are the social institutions as they provide various kinds of services to the users and citizen of the city / country. They have been the essential part of the education system in the society since early days. In the modern India, libraries have become the integral part of not only educational institutions but also other government setup like ministries, departments, district centres, etc. Keeping in view the large number of Public and Government libraries in India and also the high cost of commercial software, it becomes imperative to provide zero-cost software along with free support, training and services.
NIC has been a pioneer source to design, develop and support ICT tools and services for the Indian Libraries since its existence as the latter are integral part / divisions of the ministries, departments and other Government organizations. From 1994 to 2000, NIC distributed the Techlib Plus / Bassis Plus software to Indian libraries. During 2002 it was found that NIC had developed over 30 different library automation software for various ministries and Government departments. All such software were designed by various NIC groups for their respective ministries without following the standards, rules and practices as prevalent in Indian libraries.
Later it was decided by the Committee constituted under the chairmanship of Sh. M Moni, DDG(NIC) to use e-Granthalaya Software among the many from NIC and to further develop and promote by the NIC.
e-Granthalaya
e-Granthalaya is a Library Management Software facilitates to automate not only the in-house activities of the library but also the user services. The first version of the Software was developed by the Karnataka State center of NIC, Bangalore. Later, the development was taken over by the Library and Information Services Division at NIC NICHQs, New Delhi. The following table shows the release of various versions of the software.
Ver. Year Technology/Platform DBMS
1.0 2003 VB6/ASP SQL Server 2000
2.0 2005 VB6/ASP SQL Server 2000
3.0 2007 VB.NET/ASP.NET 2.0 SQL Server 2005
*4.0 2010 ASP.NET 3.5 with Silverlight2 SQL Server 2008
*future version Release of e-Granthalaya Software
Why e-Granthalaya Free
There is no such a designated agency in India, either Governmental, Professional or Private, which can provide a free software and services to these libraries. Central Governments as well as State Governments seem no serious for Indian Libraries development. Similarly, professional bodies in LIS always engaged in over-glorifying the profession and not provided the solution / tools even after 35 years of Post-Ranganathan era. Also, there are many Library Networks (DELNET, ADINET, CALIBNET, PUNENET, MYLIBNET, INFLIBNET, etc) in existence; however, very few provide the library services in a network environment. The simple reason is that these networks have not developed any tool/software to automate the Indian libraries and provide the services to them; they are financially poor and thus can not purchase commercial tools also. So, at it had been decided to develop a good library automation software and to provide the same at zero cost to the Indian libraries. Moreover, we understand that the libraries are non-profit making and social institutions and serve the society for its development.
Few library automation software are LibSys, Alice For Window, SLIM, Autolib, EasyLibSoft, Gyanodaya, Libra 2000, Librarian, Libris, LibSuite, Nalanda, NewGenLib, NexLib, SOUL, SWIRL, VTLS, CDS/ISIS, DelDOS / DelPlus.
Architecture
e-Granthalaya Ver. 3.0, released during 2007 has been designed keeping in view the requirement of “Networking of libraries” to share the records (Shared Cataloging) among a cluster of libraries. Thus, it has been decided to use a common/single database for a group of libraries / branch libraries and a common search interface i.e. Web OPAC for Union Catalog kind of search. It will facilitate to avoid the duplicate entries of catalogs and other authority files data such as Authors, Publishers, Subjects, etc. Every record is identified by the Unique LIBRARY CODE which is assigned uniquely to each and every participating library in the cluster. Besides, it has been decided to make it a 3-tiers application as given below:-
— Presentation Layer Windows Forms (WPF)
— Business Logic Layer (BLL)
— Data Access Layer (DAL)
To make the application ready for WAN Based data entry also, it has been decided to use WCF technology (Windows Communications Foundation) which wraps the BLL and DAL Layers in it and is installed on the Server PC. At one end, WCF layer make connection to the back-end database (MS SQL Server 2005) specified in the “Web.Config” while on the other end, it serves to the Front-end data entry program of e-Granthalaya.
For Deployment of the software on client PCs, “Click-Once” technology has been used which deploys the application directly on the client PCs. This technology is also useful in up-dation of the client software automatically whenever latest updates are there on the web site.
Some Specials Features include
— Multi-lingual, UNICODE compliant database
— Stand-Alone/ LAN / WAN based data entry solution
— Covered all in-house activities and user services
— Common database for cluster of libraries
— Common web based search interface (Web OPAC)
— Authority files for common data e.g. Authors, Publishers, Subjects, Type of Documents, etc
— Member Registration with unique entitlement and due days
— Single form for circulation of all kinds of documents and Inter Library Load (ILL)
— Bar Code generation facility
— Automatic generation of journals Schedule
Standards Followed
While designing the e-Granthalaya Software, it has been kept in mind the workflow used in the Indian libraries while processing the records in books and serials acquisition. Also it has been tried to make the application well integrated, no need of duplication data, even across the participating libraries in a common database. Besides, as there are many international standards prevalent in the field, so it has been decided to make use of such standards like AARC2, MARC21, UNICODE etc. The software does not impose any catalog standard, although, the data entry of the catalog records are inclined towards the AACR2, an international standard for Cataloging. While designing the software, it has also been kept in view the fields/data elements suggested by the AACR2/MARC standards are included in the internal structure of the database to make it compliant with MARC 21 while making output (Export) and import options.
Keeping in view the common search of the library catalogs within the cluster of libraries as well as across the cluster, it has been decide to make use of the current technology from Microsoft i.e. SRW (Search and Retrieve Web service) which aims to integrate access to various networked resources, and to promote interoperability between distributed databases, by providing a common utilization framework. SRW is a web-service-based protocol which is regarded as the big brother of implementation of the Z39.50 Information Retrieval protocol with recent developments in the web technologies arena. SRW features both SOAP and URL-based access mechanisms (SRU) to provide for a wide variety of possible clients ranging from Microsoft's .Net initiative to simple Javascript and XSLT transformations. It leverages the CQL query language which provides a powerful yet intuitive means to formulate searches. The protocol mandates the use of open and industry-supported standards XML and XML Schema, and where appropriate, XPath and SOAP. SRW has been developed by an international team, minimizing cross-language pitfalls and other potential internationalization problems
Training and Support
NIC organizes regular training of 3-days duration for e-Granthalaya and NewsNIC users in various centres of the NIC. Many of the training have also been organized by the Users organization or some other Government Departments. Users of the software may also organize training in their respective organization where faculty from NIC participates for the benefit of the users. Besides, One-Day seminars, DEMO, and e-Learning Session are also organized for the software users.
An e-Granthalaya mail forum https://lsmgr.nic.in/mailman/listinfo/egranthalaya_forum is also in existence to share the messages among the users. The e-Granthalaya web site http://egranthalaya.nic.in is a good source of the information about the software and is a medium to distribute the Updates of the software. The web site publishes the list of the e-Granthalaya and NewsNIC users also.
Users Statistics
e-Granthalaya and NewsNIC software users belong to all kinds of categories like Academic, Governmental, public and Corporate libraries. In the Academic sectors, the users are school, colleges, universities and other institutions libraries. The software is being used in the offices of the State as well as Central Government ministries and departments.
Conclusion
e-Granthalaya Software provides an opportunity to the Indian libraries to adopt the software for use in the libraries. The software, support and training is provided at zero cost and the software is updated regularly for new and improved utilities as well the technology. Those libraries which can not purchase a commercial software may use the software. Public libraries and Government libraries may also host their catalog/database in NIC server to make available their catalog online. Other organizations in the field like libraries NETWOKS and associations may join hands with the NIC to get the benefits of the NIC tools and services for Indian libraries. Joint efforts from all sorts of parties in library profession may change the future of the Indian libraries in this way.
For further information contact:
P .K . Upadhyay
Technical Director & OIC
Library and Information Services Division
National Informatics Centre
pku@nic.in
