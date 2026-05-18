---
title: "INFRASTRUCTURE PROJECT MONITORING SYSTEM OF MoSPI"
publication: "Informatics"
issue_date: "October 2013"
pages: [14, 15, 16]
author: "D. K OJHA Director (IPMD), MoSPI"
section: "E-Gov Products and Services"
---

## INFRASTRUCTURE PROJECT MONITORING SYSTEM OF MoSPI

Infrastructural development mirrors the overall health of a nation’s economy. This is particularly true for developing economies where investments in infrastructure development lead to growth, life improvement and poverty alleviation. India has invested heavily on infrastructure development and in order to realize the benefits, it is vital that the projects are implemented as per the approved plan and within the budgeted time and cost. Presently, there are several Central Public Sector Undertakings, which are implementing multiple infrastructure projects across the length and breadth of the country. Infrastructure and Project Monitoring Division, a division of Ministry of Statistics and Programme Implementation (MoSPI) is mandated with the task of monitoring the infrastructure projects being implemented by the Central Public Sector Undertakings.

The term infrastructure is defined as a set of interconnected structural elements which provide a main framework supporting an entire structure of development. Efficient infrastructure is crucial and is directly proportionate to the growth of a country.

The Central Public Sector Undertakings (CPSUs) holds a key role in the development process of our nation and forms the cornerstone of the infrastructure development in the country; though in today’s time more and more Private sector entities too are getting increasingly involved in the process.

Currently, the CPSUs are engaged in executing over 560 major projects costing above Rs 150 crores in 14 different infrastructure sectors. The total original cost of these projects is more than Rs. 790,000 crores. Successful completion and timely implementation of these infrastructure projects would be critical for fair indexing of economic development and social growth.

Due to various reasons, some of these projects are delayed from the actual schedules and are suffering from cost overruns. Constant, efficient project monitoring and adapting effective control measures would be vital for better management and control to prevent further delay ensuring successful implementation of such projects.

ROLE OF IPMD, M/O STATISTICS & PROGRAMME IMPLEMENTATION
The Infrastructure and Project Monitoring Division (IPMD) in the Ministry of Statistics & Programme Implementation (MoSPI) is the management arm of the Government of India. The division has been mandated with process of monitoring of all Central Public Sector Infrastructure projects which have the cost of above Rs. 150 crores.

PROJECT MONITORING SYSTEM
The Project Monitoring System forms the source of information for most of the activities of IPMD, MoSPI.

The date of approval of the project by the concerned sanctioning authority is generally taken as the zero date for the project. The approved date of commissioning of the project is taken as the original date of commissioning. Once the project is in the execution phase, based on the ground realities, the project executing agencies regularly update the anticipated date of commissioning. The variance between the original and the anticipated dates of commissioning forms the basis for analyzing delays in the projects. A similar approach is employed to monitor the health of the project with respect to the costs.

Based on the above principles, the Infrastructure and Project Monitoring Division, MoSPI has designed and developed a software solution that can collate macro-level information from Government of India sponsored infrastructure projects. This can also generate analytical reports for the consumption by various stakeholders.

As soon as a project is approved, it is brought under monitoring by assigning a unique identifier to it in the system. The associated data sets that define the project are also created at this point in time.

All the agencies executing projects are assigned User IDs & passwords, with which they can access the system to add/modify the data related to the projects being executed by them. The basic process flow of the system is given below.

SYSTEM PROCESS FLOW
The Project Monitoring System has a web-based simple interface for updating the project related data such as the original and revised dates, original and anticipated costs, expenditure and the background information. The data for each project is collected every month in the following manner:
l Data entry for the projects is allowed for a particular month. Project agencies would have to use the web-interface to fill in the data related to all projects being implemented by them. Each agency is provided with a unique user-id. Each project is identified by a unique-id. The user can also select a project by its name.
l After allowing entry of project data for a limited period, the data entry for the month is frozen. In order to weed out data entry errors and other inconsistencies, the system generates algorithm-based error reports. These reports are used to cross check the data and if required, data verification is also done with the reporting agencies. Any inconsistency found is corrected during this phase.
l After data correction, the data entry for the month is closed and the data entry for the next month is opened for the project agencies to enter data for the next month.
l Post to the data collection phase, the data is analyzed, and various reports are prepared.
l The highlights of the reports along with detailed analysis are distributed among various stakeholders such as Administrative Ministries of the Project Executing Agencies, Planning Commission, PMO etc.

System Architecture of the Project Monitoring System (Image description: A diagram showing System Architecture of the Project Monitoring System)

PHYSICAL IMPLEMENTATION
The Project Monitoring System has been implemented on the client-server model with servers located behind a Firewall. Application and Web Servers: This has been implemented as a two-node failover cluster. For the external users, application and web servers are accessible only through the Firewall. The failover cluster provides better availability of the application. Database The database is set up on a raid-5 configuration. Database can only be accessed from the application and web servers. The raid-5 configuration provides fault tolerance through redundancy. Scheduled backups are stored at different locations.

TECHNOLOGY
The system has been developed using the following technology:
l Operating System – Windows 2003 Server
l Web Server - Apache Tomcat
l DataBase – Oracle 9i
l Application Server – Oracle 10g
l Front End – Forms 10g, Report 10g, PLSQL Server Pages.

REPORTS & OTHER OUTPUTS
Some of the most used reports generated from the system are:
l Monthly Flash Report - This report presents a sector-wise overview of all the projects on the monitor.

Decrease in percentage of delayed CPSU Infrastructure projects (Image description: A graph showing decrease in percentage of delayed CPSU Infrastructure projects)

Decrease in cost overrun in CPSU Infrastructure projects over the years (Image description: A graph showing decrease in cost overrun in CPSU Infrastructure projects over the years)

l Quarterly Progress Report- QPR is an in-depth analysis of all the ongoing projects and their progress vis-à-vis the last quarter. This report also includes detailed analysis of every project on the monitor.
l Mega Progress Report- This monthly generated report provides an overview of the mega projects (costing over Rs 1000 crores).
l Snapshot- The purpose of the report is to provide a consolidated snapshot of all the ongoing projects with the aid of limited charts and graphs.

The analyses in all the reports are based on the following criterion:
l Changes in anticipated schedule of the projects vis-à-vis the schedule reported in the last period
l Changes in anticipated cost of the projects vis-à-vis the cost reported in the last period
l Track budgeted and actual expenditure for the period and the cumulative for the financial year
l Check whether the expenditure on the projects has surpassed the originally approved cost
l Check whether the projects have reported a revised scheduled or cost
l Check for new projects and projects that have been completed
l Monitor the individual projects as well as the sectors to which these projects belong
l Analyses of projects based on the specific regions/states of the country
l Categorization of projects in groups - having time overruns, having cost overruns and having both time and cost overruns
l Highlighting projects that are not reporting critical information like anticipated schedules and costs
l Capture and analyze the reasons for the time and cost overruns in the projects
l Monitor the achievements of the project milestones
l Highlight delays in completion of critical milestones as delay in critical milestone signify delay in the project itself

BENEFITS OF MONITORING
There has been a continuous decline in the extent of time and cost overruns, which can be attributed to better monitoring and system improvements by the concerned ministries, with the active support of MoSPI. An analysis of cost overruns in the last 15 years with respect to the originally approved cost shows that the cost overruns have declined from 40.90% in March 1999 to 14.72% till March 2010 and then it has more or less stabilized in the range of 17% to 19%. An analysis of percentage of projects delayed over the last 15 years with respect to the originally approved schedule shows that the percentage of delayed projects has declined from 59.11% in March 1999 to 34.13% till March 2007. There is an upward trend from March 2007 to 48.11 % in March 2009 and since then it has more or less stabilized.
