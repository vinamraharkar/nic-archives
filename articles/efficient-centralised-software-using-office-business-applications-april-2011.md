---
title: "Efficient Centralised Software using Office Business Applications"
publication: "Informatics"
issue_date: "April 2011"
pages: [30, 31, 32]
author: "Mayank Pratik"
section: "Technology Update"
---

## Efficient Centralised Software using Office Business Applications

Centralized Software are the genre of applications which uses the latest advancements in technology providing solutions that are easier to implement, saves in a lot of money and are highly scalable. Implementing Centralized Software using Office Business Application results in effective harnessing of the power of latest advancements in technology thereby producing software that is easily maintainable and has great acceptability amongst the users.
Reviewed by D C Misra, Sr TD, NIC HQ
IMAGINE a situation wherein we have a large user set spread across the country and everyday at end of day they have to send a daily report to their central office. The mechanism is pretty similar to what traditional bank systems were implementing in the last decade, but their solutions involved huge cost overruns (due to high cost of setting up the infrastructure and their maintenance). To offset high investment in setting up the required hardware in numerous places and later spending money on their maintenance and purchase of software for this, an alternative cheaper, technologically advanced way is to implement centralized software.
What is an Office Business Application (OBA)?
As the name suggests OBA is used to refer to class of applications intended to perform business operations using productive tools (such as Microsoft Office) as frontend.
It aims to bring the users close to interacting with the Database (which can be anything ranging from a standalone database application to Line of business applications) comfortably. The main idea behind an OBA solution is that users are comfortable using the regular ms-office tools for doing their day to day office activities. For interacting with the database they have to move back to traditional applications to perform certain Create Read Update Delete (CRUD) operations. This is where OBA comes into action and scores over the traditional approach - user does all his work in the Office Application such as Word or Excel and when he wishes, saves the changes back to database or the line of business application.
OBA applications not only presents the user with the option of comfortable and friendly user interface but also takes care of all the prerequisites and makes the working for the user very easy and comfortable .
The OBAs developed for this purpose presents the user with the office interface with which he is comfortable in working with, the OBAs in turn will have some intelligence built into it which performs validation on the data that the user has entered.
After the data has been validated the user makes a request to the server to save the data. This can be particularly useful for users who have an intermittent web connection. When the user is connected to the web he can fire his updates right from the Office application meanwhile working on the data in between.
Users in the government sector are not always very IT savvy. Many a times we have faced situations where users are concerned with the difficulties faced in the installation of prerequisites for installing a software. The installations of the prerequisites and the technical complexities that come with it are one the hurdles in adopting the software. Everyone will cherish the idea of a software which detects all its prerequisites, installs them and keeps the user interference to the minimum.
OBA - Model
OBA can be perceived to be a simple model consisting of three parts:
The Office client that integrates with the Line of Business system, the web server (essentially MOSS) that which might integrate with the Line of Business system and the Line of Business system itself. Note that when building OBAs, developers can also leverage other Microsoft server products such as Exchange Server 2007, PerformancePoint Server 2007, and so on.
Architecturally different from the SOA (service oriented architecture) OBAs can be developed by using standard Microsoft technologies such as Visual studio tools for office (VSTO 3.0 available in visual studio 2008).
Subsets of the following set of technologies can be used for leveraging the full power of OBA solutions -VSTO, MOSS , BDC, Open XML, Web Parts VSTO(ribbons custom panes, etc.) , BDC excel services ,Windows Workflow Foundation, Windows SharePoint services, InfoPath form services.
OBA - Office System integration Models
Mediated Integration requires creation of a services layer which mediates integration between the Line of Business system and the custom client components (for example, the custom task pane), thus facilitating reuse across multiple systems and loose coupling between the client and server. For a typical data entry OBA application used in the government scenarios we can now create a Web service that wraps around the data entry module (where all of the data is entered) and integrate that Web service with all client interfaces. So if someone wants to integrate the Line of Business system with Excel, it is possible now. This service can then be used by creating a proxy stub in Visual studio 2008 or using Business Data Catalog (BDC) in case of SharePoint.
The resulting architecture leverages the Mediated Integration pattern; that is, an OBA that leverages Web services to provide desired functionality in Excel and SharePoint. The bigger advantage is, now the user can fire read/write queries right from the client side customization (in this case the Excel Sheet)
Office system is a good way to surface capabilities from other platform technologies e.g. SQL Server (data, integration / reporting / analysis services), BizTalk Server (business process management / monitoring), Active Directory (identity management).
OBAs can extend the reach of familiar frontend interfaces into the data stores in the back office.
For modeling business process we can use workflow technologies available in SharePoint. It can range from simple sequential workflows to complex state machine workflows.
For managing the lifecycle of business processes / business entities (esp. when coordinating across multiple groups or organizations), we can use BizTalk to handle business processes external to SharePoint.
Three tier applications are best suited to transactional tools (that handles data entry). OBAs when used in collaboration with SharePoint and MOSS capabilities can also include human workflows and system workflows.
Advantages of using this modified approach of implementing centralized softwares
Using this approach the client becomes a smart client though being light and requiring no installation on the user end such as database license and additional hardware purchases.
Using WCF has a lot of advantages over the traditional Web services. It is state based, can be used to perform transaction, provides concurrent access and can use any protocol to communicate. Further they can be made very secure so as not to be tampered with and they also support https. They can also synchronize huge amount of data.
Using Click once download facility.
This facility is a boon for developers whose solutions are being used by user spread across far off places. The updates are hosted on a single place on the web server. The applications go and check whether newer updates are available notifies the user and with the permission of the user installs the newer version. All these things happen automatically with least user intervention.
Future of OBAs
OBA Applications when used in integration with moss and SharePoint will give the class of business applications a new value. OBA applications, if properly implemented could serve as a boon to the users working in the Government administration, saving time and enhancing the usability and functionality of Business applications.
For further information
MAYANK PRATIK
Scientific Officer
Accounts Informatics Division,
National Informatics Centre
O/o Controller General of Accounts, 401, Loknayak Bhavan, Khan Market New Delhi-110003
Ph: 011-24640085
mayank.pratik@nic.in
