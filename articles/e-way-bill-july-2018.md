---
title: "e-WAY BILL"
publication: "Informatics"
issue_date: "July 2018"
pages: [23, 24, 25]
author: "P V BHAT; DIPANKAR SEN GUPTA; H L RAVINDRA; SUNITA BENNUR"
section: "e-Gov Products & Services"
---

## e-WAY BILL

One Nation - One Tax - One Market - One e-Way Bill
The e-Way Bill System provides multiple modes of e-way Bill generation including web, bulk upload, SMS, Mobile App and API for large Tax Payers/ GST Suvidha Providers (GSPs).

As a part of the anti-tax evasion measures under the new indirect tax regime, the GST e-Way Bill System was rolled out all over India, initially for Inter-State movement of goods from 1 April, 2018. Gradually, the scope of generation of electronic permits were extended for movement of goods within the states and the final country-wide rollout was completed by June 3, 2018 except Delhi. The complete e-Way Bill System, which includes development of web-based IT Application, hosting IT infrastructure (which includes network, computing and security) and operation & management of the system is the responsibility of National Informatics Centre (NIC).

INTRODUCTION
In the previous VAT regime, one Transit Pass was required for each State through which the truck passes, if the value of goods transported was above the defined amount. For example : If a truck carrying goods from Delhi to Chennai, had to pass through 6 States/ UTs, then it needed to obtain Transit Pass from each one of the six States the truck was passing through. Transit Pass was issued online by 15 States/UTs and rest of the States followed manual process of issuing the Transit Pass. Advent of GST regime presented an opportunity to facilitate creation of a single nation-wide e-Way Bill in self-service mode by the consigners/ consignees/ transporters. The application is accessible through URL https://ewaybillgst.gov.in.

e-Way Bill is a document which gives details regarding the movement of goods and has to be carried by transporters for any consignment exceeding Rs 50,000.

OBJECTIVES
• Single and Unified e-Way Bill for Inter and Intra-State movement of goods for the whole country
• Fully online and enabling ‘Paperless’ movement to track and monitor movement of goods across various States
• Improve service delivery with quick turnaround time for the entire supply chain and to provide anytime anywhere access to data/ services
• Minimal physical interaction with the concerned departments and hassle-free movement of goods

TECHNOLOGY USED
• Front end forms are developed using ASP.Net with C# as the scripting language using framework 4.0
• Backend database is SQL Server 2017
• Redis Enterprise NOSQL for Caching
• APIs using JSON for android/IOS Mobile App and integration with systems of large Tax Payers/ GST Suvidha Providers(GSPs)
• Akamai CDN for distribution of static content such as user manual, FAQs etc.
• PRTG for monitoring of infrastructure
• App Dynamics to monitor Application Performance

MAJOR MODULES CONSIGNER/ CONSIGNEE/ TRANSPORTER
These can be categorized as Tax Payers who are registered on GST common portal and have obtained GSTIN and transporters who are not registered on the GST common portal. As a first step to use the system, the first category of users need to register in application through registration process by providing GSTIN whereas the second category of users need to enroll by providing PAN. After completing these steps, they can use the application to perform various activities.

MAJOR FEATURES
e-Way Bill Process
• Generation
• Cancellation
• Rejection
• Extension of validity
• Change of transporter

Consolidated e-Way Bill
• Generation
• Regeneration

Others
• Update profile from GST common portal
• Register for Mobile App/ API/ SMS
• Register for GSP
• Detention Report
• Reports
• Masters Creation
• User Management

Department officers
• Verification
• Detailed Verification Report
• Reports

MODES OF GENERATION
Application provides multiple modes through which the user can generate e-Way Bills. These include:

Web
Details of goods to be carried, consigner/ consignee, transporter/vehicle etc. can be entered through web form.

Bulk upload
Excel-based utility has been provided to users. This utility can be used to enter data and generate a JSON file which can be uploaded to generate multiple e-Way Bills in one go.

SMS
User has to register his/ her Mobile number for SMS and then e-Way Bill can be generated from the registered Mobile number by using keywords and required parameters.

Mobile App
GApp on Android and IOS platforms are available to facilitate various functions which can be performed through web. User has to register on web to use Mobile App.

API
This option is provided to large Tax Payers and GSPs to on-board the system using APIs for system to system integration. These APIs are implemented as Restful Web-Services.

The users test the APIs in sandbox environment before being provided access to the production server. To enable them to securely access the APIs, a Client ID and Secrect Key is provided to each user and required IPs are whitelisted. As first step to use APIs, user obtains an authentication token which remain valid for six hours through Authenticate API. In order to access other APIs, Client ID, Secret Key, GSTIN of the required user and session token are passed in API request header along with other parameters required by API as request payload.

KEY INTERVENTIONS
PAN validation through NSDL
At the time of enrolment of transporter, validation of PAN is carried out through NSDL.

Updation of profile of Tax Payers through GST common portal
At the time of registration as well as at anytime subsequently, the user can update his profile by extracting data from GST common portal through APIs.

Caching Tax Payers’ data in Redis
Redis NOSQL is used for caching data of entire set of tax payers. Thus, application first connects to the caching layer to obtain data related to tax payers and helps to reduce latency.

My Masters
The Users are provided with option to create their own masters of clients, suppliers, transporters and products to enable them to enter these details by typing their first few characters and this also speeds up the search process.

Databases sharding
Database is divided into 8 zones each zone is a group of states. E-way bills are created in the zone corresponding to state of the creator. This facilitates aproximate equal distribution of load across the databases.

Use of a sync database for reporting
As the application has very high level of concurrency, the reporting is carried out from a sync database instead of OLTP database to improve the performance.

Load Testing
As the application has very high level of concurrency, extensive load testing was carried out to tune infrastructure, application and database for good performance.

API
This option is provided to large Tax Payers and GSPs to on-board the system using APIs for system to system integration. These APIs are implemented as Restful Web-Services.

The users test the APIs in sandbox environment before being provided access to the production server. To enable them to securely access the APIs, a Client ID and Secrect Key is provided to each user and required IPs are whitelisted. As first step to use APIs, user obtains an authentication token which remain valid for six hours through Authenticate API. In order to access other APIs, Client ID, Secret Key, GSTIN of the required user and session token are passed in API request header along with other parameters required by API as request payload.

QR Code
e-Way Bill is generated with a QR code which can be scanned by the Mobile App provided to Departmental Officers for verification.

Data Exchange with GSTN/States
The e-way bill data will be shared with the State and Centre Tax Authorities and GSTN through APIs for further analysis at their end.

Dissemination of static content through CDN
Static content such as user manuals, FAQs, circular/OMs etc. are deployed on another Sub Domain of the application viz. docs.ewaybillgst.gov.in which is serviced through Akamai CDN thereby reducing traffic to the main e-Way Bill portal.

INFRASTRUCTURE
As 24x7 accessibility is a critical requirement of the application, infrastructure is designed to provide redundancy at multiple levels including firewall, load balancer, switches, racks, virtual machines(web servers), database servers and MPLS links (for connecting to GSTN servers).

Virtual machines for web-servers are created on Hyper-V clusters. 24 VMs are used as front-end (with IIS). Number of other VMs have been created for API, Mobile App, GSTN API and Redis.

Two Availability Groups of four Database Servers, Each are configured to ensure redundancy at the Database level. In each Availability Group, out of four Database Servers, two servers store data of two zones each and sync copies of two other zones whereas the other two servers are async copies of the data of four zones used for reporting purposes. The third availability group has two database servers which store session and authentication databases respectively.

HELP-DESK & MONITORING
Considering criticality of the application, 24x7 Help Desk is set up at NIC Centre, Koramangla, Banglore to provide L2 support to the issues forwarded by the GSTN Help Desk. The Help Desk functions 24x7 which enables quick resolution of the issues and closing of tickets forwarded by GSTN Help Desk.

A part from this, the application performance is monitored round the clock. PRTG is configured to monitor the health of the infrastructure i.e. Web VMs, Database Servers, Firewalls etc. The parameters monitored include utilization of processor and memory, ping, HTTP response time etc. Additionally, a Dashboard is also provided to display State-wise/ Zone-wise e-Way Bills generated in every five minutes. These tools and mechanisms facilitate the team to identify any system or service outage within no time and respond quickly.

IMPLEMENTATION APPROACH
Till April 1, 2018, the Tax Payers were allowed to generate e-Way Bills on trial basis and during this period, the system was tested on all parameters like load, integration and application testing. Numbers of training sessions were conducted for officers of different State Governments who in turn conducted sensitization sessions for Tax Payers and transporters in respective states.

As recommended by GoM on IT, e-Way Bill was implemented from April 01, 2018, for Inter-State transactions only in the first phase. e-Way Bill portal was made accessible for Intra-State movement after examining the usage pattern and the system performance for Inter-state e-Way Bills for first two weeks. The states were covered in phased manner in groups of 5-6 states at a time.

As of 23rd May2018, 22 states had notified and started e-Way Bills for Intra-State movement of goods and 2 states had started generating e-Way Bill for Intra-State movement on trial basis. These states were generating around 6 Lakh Intra-State e-Way Bills daily. By first week of June, 2018 all the states were covered for generation of Intra-State e-Way Bills also.

KEY STATISTICS
• Average Inter-State e-Way Bills per day: 6.72 Lakh
• Average Intra-State e-Way Bills per day: 5.58 Lakh
• Tax Payers registration till date: 22.22 Lakh
• Unregistered transporters enrolment till date: 28,638
• In April 2018, 279.96 Lakh e-way bills were generated. In that 205.58 Lakh for inter-state and 74.37 Lakh for intra-state movement
• In May 2018, 372.32 Lakh e-Way Bills were generated out of which 211.32 Lakh were for Inter-State and 161.01 Lakh for Intra-State movement.
• In June 2018, 467.65 Lakh e-Way Bills were generated out of which 194.91 Lakh were for Inter-State and 272.74 Lakh for Intra-State movement.
