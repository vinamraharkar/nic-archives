---
title: "Ruralsoft : The New Version of Crisp Software Based on Component Development Approach"
publication: "Informatics"
issue_date: "January 2000"
pages: [12, 13]
author: null
section: null
---

## Ruralsoft : The New Version of Crisp Software Based on Component Development Approach

A new version of CRISP software package called "RuralSoft" has been designed and developed using latest technologies to meet the needs of new poverty alleviation schemes, which have emerged as a result of restructuring of the earlier schemes by the ministry. The requisite computing and communication environment has already been approved by the Ministry which includes one Server (Windows NT) and five clients (Windows 95 or latest), SQL Server 7.0, Visual Basic (Enterprise version or later) and MS-Office 97 (or latest). VSAT based connectivity has also been sanctioned which will take effect in 15 districts selected by the ministry, in the pilot phase and is likely to be extended to all DRDAs.

Ruralsoft Technology

RuralSoft is based on three-tier architecture, wherein the Presentation, Business and Database logic have been segregated and addressed to as distinct entities. Visual Basic has been used to develop the front end, whereras the business logic resides at the MTS and SQL Server7.0 has been used for the database.

The application has been designed based on object-oriented line of thinking. Component Development approach has been adopted to split the software into various components, each meant for a specific kind of functionality. There are components (Infrastructure Objects e.g. RuralSoft specific controls like 'List of values', 'Grid' etc.) which handle the GUI, while there are other components to deal with business rules (Business Objects e.g. Classes for creating beneficiary for a particular poverty alleviation scheme, like 'SGSY' ) and data services (Data Service Components e.g. 'DB Connection'). These components adhere to the Component Object Model (COM) specifications. Interface inheritance has been used to achieve reusability leading to simplified design at the User Interface level. The entire approach yields several benefits. In future, if any change occurs in any of the application tiers, only the affected component will need to be plugged off to make the required change without disturbing the rest of the application. The design also promotes reuse. Any customisation in the software can easily be effected using the already existing components which have been made generic enough to take care of future customisations. Besides the component based structure, another important feature of RuralSoft is its Web-based Report section, which will highly strengthen the monitoring process. The reports are actually Active Server Documents developed using IIS Application feature of Visual Basic. The template for each of the poverty alleviation schemes have been so designed that a single template is used for generating reports on-the-fly depending upon the district selected by the user. The data is supplied to the reports via a COM component, which is specially designed for the purpose. The reports contain textual as well as graphical data incoporated at appropriate places. These reports can be accessed from within RuralSoft or directly from Internet Browser by connecting to the web-site which will be hosted at the Ministry Server, thus facilitating on-line monitoring of data. This web site will also provide other State-of-the-art technologies like OLAP, GIS and dynamic queries to strengthen off-line monitoring.

Another notable aspect of RuralSoft is its data transmission over Wide area Network. Each of the district will be able to send its regular monthly report to the ministry using Exchange Server and SQL Mail. The data will be sent through the mail as an attachment file which will be detached automatically at the other end, followed by automatic insertion of the data into the database.

Ruralsoft is going to provide benefits to all its users, right from the data entry staff at DRDA to the monitoring officials in the ministry. Its easy-to-use and intutive GUI will facilitate the data entry operation, the web-enabled reports, OLAP & GIS features will strengthen the on-line as well as off-line monitoring process both at ministry and DRDAs. And the objected-oriented technology behind its development will not only help the future developers to easily maintain the software but also ease a lot of burden in case of future customisations.

For further information, please contact :
CRISP Division
3rd Floor, NIC Headquarters
Tel No. 91-11-4360563
Email : crisp@hub.nic.in
