---
title: "Samagra Kutumba Survey Household Information Capturing System for Telangana Government"
publication: "Informatics"
issue_date: "January 2016"
pages: [16, 17, 18]
author: "Dr. Y. Satya- Narayana Murty, A. Srinivasa Subba Rao, T. Sridhar Sharma, Dr. A. Rama Mohan Rao"
section: "E-GOV PRODUCTS & SERVICES"
---

## Samagra Kutumba Survey Household Information Capturing System for Telangana Government

Samagra Kutumba Survey was conducted in all the districts of Telangana State ensuring that each household is surveyed once at one place. It was also aimed to have a high degree of accuracy in the data & statistics to enable the government to make appropriate strategic planning for citizen centric services

The task of design and development of data input system and necessary software for capturing the citizen data along with preparation of MIS reports of Samagra Kutumba Survey (SKS) for Telangana State was bestowed to National Informatics Centre, Telangana State Centre (NIC-TSC), Hyderabad. The NIC, TSC took up this extensive task and then successfully executed in a stipulated short period. This challenging activity also involved software management, data warehousing, database management and preparation of MIS reports. The highlight is that using this system, the data of 3.60 Crore citizens got captured in just 20 days.

TECHNOLOGY
The system for Samagra Kutumba Survey was developed using the technologies mentioned below:

Application: HTML5, Struts Framework and JSON

Database: MS- SQL Server 2012

Web Server: Apache Tomcat 7.0
CISCO application load balancing with multiple application servers installed on TOM CAT into 8 VMWare servers of Linux, databases maintained in the active clusters.

THE PROCESS
The concept of Fixed Public IP access for the software was presented to all District Collectors for collating the lists of IP-address of computers, data entry operators and data entry stations. The collated list was then provided to the District Informatics Officer for generation of user ID and password for each computer operator who carry out data entry. IP address of the computers / data entry stations were captured during the data entry process and the list was submitted to the District Informatics officer, who only has the privilege to access the link at the data entry website.

DATA COLLECTION SHEET
SIO & DDG, NIC Telangana State Centre has conceptualized and designed the data collection sheet and explained the data entry fields to the State Government authorities during the brain storming session on the survey. The format was finalized after various meetings with the State Government authorities. A unique 9 digit alphanumeric SKS number concept was derived, in which the prefixed first two digits represent respective District code. The SKS number has been taken as the primary key for all transactions of the application.

BACK END PROCESS
• Data capturing of 3.6 Crore family members and 105 indicators
• Cleaning of Data
• Age and Name verification with Aadhaar data
• Processing of data for correction
• Generation of PDFs for verification
• Processing of data for various reports
• Analysis of data for various beneficiary schemes
• Integration of data for Pension and Food Security processing
• Replication of Data
• Integration of data with various line departments’ Applications

FRONT END PROCESS
• Generation of sanction letters for beneficiaries

USER MANAGEMENT
Identification of users:
The task involved identifying the end users (stake holders) of the SKS data entry and report level users. The main administration module for creation of users and assigning roles and privileges were given to an officer of NIC Telangana State centre. NIC District Informatics officers were given user IDs by the State official and assigned to be the administrators for user ID generation for Data Entry Operators and Mandal Revenue Officers. At the state level, the Principal Secretary (PR & RD) and CEO (SERP) & Commissioner and Spl. Commissioner (GHMC) were the identified users to view various statistical, analytical and MIS reports.

Component II – ePOS (http://epos.ap.gov.in/ePos)
The challenge in this task was to generate user IDs for the data entry operators at various places in the Districts without knowing their identity. After a series of brain storming sessions, a unique approach was derived to generate user ID for users at various levels.
• The ID consisted of a total of 8 characters; District Code + Mandal Code + three digit running serial numbers. Based on this criterion, in a Mandal, a maximum of 9999 data entry operator IDs could be generated
• It was made mandatory to change the original password of each user on first login, during which all the user details were captured
• User levels were identified based on the three parts in the user Id along with a unique level code
The above user Id formation has several advantages. One advantage is that based on the login, location details can be captured in each Form

Security & Session Management:
The password was encrypted by salted Sha1 algorithm. All the users logged in were maintained in unique session ID individually.

User ID intimation:
User ID’s generated by DIO’s of NIC were communicated in a sealed cover to District Administration for onward transmission to end-users.

User locking mechanism:
User Id will be locked after three consecutive failed login attempts. The privileges for resetting password for locked users were given to NIC DIO’s (MRO’s and DEO’s). Remaining password-resetting privileges were with state NIC officer.

Roles & Privileges:
Data Entry Operator: SKS survey format data entry
Mandal Revenue Officer: Statistical Reports
District Collectors: MIS & Statistical Reports
State Level Officers: Analytical, GIS, MIS and Statistics Reports

MIS REPORTS
• Developed MIS report formats as communicated by the Government of Telangana
• The Telangana Government conducted workshops along with eminent personalities and NGOs for arriving at criteria of exclusion, inclusion and deprivation
• A Portal was Developed for accessing the reports such as Exception, Demographic, Analytical, Housing, Pensioners, Food Security Cards, Socio-Economic, Vulnerable and GIS

UNIQUE, INNOVATIVE AND REUSABLE TECHNOLOGIES
• Usage of JSON (JavaScript Object Notation) for storing and exchange of data
• All the Masters converted to JSON object to reduce the database hits
• Pouch DB: Enables to store the data locally when Internet connectivity goes offline and the same be synchronized to main database in the encoded JSON Format whenever connectivity is online

UNIQUE HIGHLIGHTS
• For the first time in India, such a combination of technologies used with identified parameters for capturing information on 3.68 Crore citizens
• The entire data entry got completed in a record time of 14 days
• The combination of the system and technology can be a role model for many other citizen centric applications
