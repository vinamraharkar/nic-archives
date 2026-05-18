---
title: "Samay Sudhini Seva- Online Monitoring of Time bound Services"
publication: "Informatics"
issue_date: "July 2013"
pages: [18, 19]
author: "Utpal Mehta and Nitin Bamania"
section: "e-Gov Products & Services"
---

## Samay Sudhini Seva- Online Monitoring of Time bound Services

Edited by Anshu Rohatgi
The UT Administrations of Daman & Diu, and Dadar & Nagar Haveli provide various services to the citizens in time bound manner. The administration has prepared a Citizen Charter defining the time limit for the selected 60+ services from various departments such as Electricity, VAT, Transport, Excise, Revenue etc. All the services are required to be delivered as per the Citizen Charter. In order to track and monitor the progress of the services, and remove inherent deficiencies and bottlenecks, an ICT based approach has been used by the administrative officers in form of ‘Samay Sudhini Sewa’ (SSS).
The major aim of the initiative was to equip the administrative officers and higher authorities with web based tools to track the applications received for these time bound services and monitor the timely disposal of the applications.
eSLA-Framework
After a detailed study of the system and the functionality required, it was decided to adopt the framework of eSLA, (electronic Service Level Agreement) developed by NIC State Unit, NCT Delhi.
eSLA is a comprehensive system designed and built around services. The back-end processes of the services are already computerised and it provides various MIS reports at different levels to monitor the delivery/disposal of the applications. However, the scenario is a little different in the UTs as the computerisation of backend processes is not complete for all the selected services. It is at different level, making it quite difficult and challenging task to enter the application details into the eSLA system. As a result the eSLA framework had to be customised for the two UTs and a separate module was developed to capture the application details into the system. The customised version of the eSLA framework has been implemented for the two UTs.
Single Window Implementation
The administration established ‘Single Window Counter System’ at all the departments where the applications of the identified services are received through Single Window User Interface. The operator of Single Window receives the application from applicants and enters into the system. The system generates receipt with a Unique Application Number. One copy of the receipt is given to the applicant, while another copy is attached with the application. The application is now sent for the processing. The processed application returns back to the Single Window operator with the deliverables, if disposed-off, otherwise with the reason for pendency/rejection. The status is also captured in the system.
Salient Features
All the users at various levels have been provided user credentials with different user rights. The user intended to capture the application details enters application into the system and generates receipt with Unique Number. The applicant can track the status of the application online using the combination of the Unique Application Number and the mobile number, provided earlier.
The system generates different MIS reports for various levels of monitoring. The MIS reports highlight the number of applications received and disposed within SLA and those disposed after the SLA period or delayed as per the SLA period. Based on the MIS reports, the senior authorities can then take appropriate actions against the erring officer/official.
All the users of the system have been provided secured access through VPN.
How It Works
The application works in three different layers:
1. Data Capture/Application Management:
The module has been developed in PHP/MySQL technology by NIC-Daman centre. It is hosted on Linux server and is accessible through Internet. The SSS operator captures the application details using this module. This module covers extensive application management like disposal, rejection, suspension and revocation of the application using various user rights at appropriate level. If any application needs to be kept in suspended state, it is not counted under the SLA days. This module also covers the online status display to the applicant. Applicant can access the website http://daman.nic.in to see the status of their application.
2. Data Bridging:
At the end of each day, this module accumulates the applications entered into the Data Capture module to the eSLA/SSS monitoring module. The eSLA uses MS-SQL as backend database server. This module uploads the application details captured from the Data management module to eSLA module.
3. Monitoring:
This module processes the application details and generates various MIS reports as per the requirement.
Advantages
The pendency of the application has reduced considerably due to regular monitoring by the administrative authorities.
The applicant can see the status of their application online using the Unique Application Number.
The whole application development uses hybrid environment like PHP/MySQL/MS-SQL/.NET.
Impact
Samay Sudhini Sewa was inaugurated by the Hon’ble Administrator of Daman Diu and Dadra Nagar Haveli in the presence of Hon’ble Member of Parliament, District Panchayat Presidents, Municipal Presidents and other public representatives on 7th May, 2013. The effort was highly appreciated by the Administrator and other dignitaries.
At present, the system has been implemented in 10 departments covering 60 services across both the UTs and many other services are in pipeline. The application is also being replicated in Diu district.
The success of the project can be gauged with the improvement in disposal rate of the applications and reduction in pendency levels. NIC, Daman and Diu is in process of integration of SMS gateway with the application and very soon, the applicants will be kept well informed of every activity regarding their applications.
