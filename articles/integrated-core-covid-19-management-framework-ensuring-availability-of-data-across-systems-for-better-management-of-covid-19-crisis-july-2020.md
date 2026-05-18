---
title: "Integrated Core COVID-19 Management Framework: Ensuring availability of data across systems for better management of COVID-19 crisis"
publication: "Informatics"
issue_date: "July 2020"
pages: [20, 21, 22]
author: "Pawan Joshi, Sunil Kumar, G. Mayil Muthu Kumaran"
section: "In Focus"
---

## Integrated Core COVID-19 Management Framework: Ensuring availability of data across systems for better management of COVID-19 crisis

Corona virus pandemic has spread across the world at a fast pace disrupting life in unprecedented ways. Government of India has taken multiple measures like nation-wide lockdown, identification of hotspots/ containment zones, isolating patients and suspects, contact tracing, surveillance besides planning and managing health infrastructure like hospitals, beds, ventilators, quarantine facilities, testing labs etc. For effective planning, decision-making and implementation of these measures, timely access to accurate information is the key.

Some of the major ICT systems that are put in place by the Government are:
• Testing and Lab System of ICMR to capture all COVID Test related data from authorized Government and Private Labs
• RTPCR & RATI Apps for sample collection
• Special Surveillance System (S3) by Ministry of Health & Family Welfare (“MoHFW”)
• Aarogya Setu App for Bluetooth based contact tracing & information dissemination

NIC was entrusted with the responsibility to provide necessary technical consultancy support to ICMR and MoHFW for improving the testing module and surveillance system to migrate on a highly available and scalable architecture. RT-PCR & RATI Apps to augment sample collection process has been designed and developed by NIC. Aarogya Setu App has been developed in collaboration with industry for digital contact tracing. A centralized Data Hub has been established to facilitate real-time integration of these systems through secure APIs. These systems support the government in the effective management of the pandemic.

Following sections document the role played by NIC in establishing and supporting these systems.

Testing & Lab system of ICMR
For effective management of COVID, both testing and timely availability of the test results are of critical importance. The Testing and Lab Systems developed by ICMR in-house facilitates labs to update demographic and clinical data for tests conducted by them. This data is the single source of truth which is used by all District and State Officials for patient management and contact tracing.

NIC provided technical advisory and consultancy to ICMR in improving the existing system and migrating it on highly available & scalable architecture on NIC Cloud. The major services extended by NIC are:

Architecture Redesign & Migration on NIC Cloud
The deployment architecture has been redesigned and migrated to the scalable infrastructure of NIC Cloud considering future load along with availability requirement. A DR site was created to mitigate the risk of failure and data loss. NIC also assisted in the de-duplication process by identifying duplicate records of patients.

Standardization of Database Schema & Query Optimization
The Database Schema was improved for better performance and aligned with metadata standards. Appropriate validations were incorporated, queries were optimized and tuned for performance.

Data Exchange through APIs
The data related to COVID Positive and Tests are the single source of truth from this system being used by all the other agencies. NIC designed and developed various APIs with relevant documentation to facilitate integration.

RT-PCR & RATI Apps
As an extension to Testing and Lab System, NIC has developed RT-PCR App to support sample collection at the patient doorstep and helping in minimizing the data entry burden on Labs. The data captured by RT-PCR Lab is integrated with the Testing & Lab module. NIC has also developed RATI App for sample collection and result dissemination of Rapid Antibody Tests. A centralized portal https://covid19cc.nic.in/ has been developed to facilitate registration of sample collectors, technicians and dissemination of information.

Special Surveillance System (S3 System) – COVID India Portal
NIC is closely working with MoHFW in leveraging technology solutions for effective COVID management. The Special Surveillance System (S3) implemented for surveillance officers at state and district level facilitates management of activities like surveillance, contact tracing, logistics planning & management including quarantine facility and patient management. The system is the centralized data source for state and district officials for all major activities related to COVID management.

NIC has provided necessary consultancy and support to MoHFW in managing the overall system, its deployment on high availability and scalable infrastructure. Some of the major services extended by NIC follows:

Design & Development of Additional modules
NIC has developed a module to integrate patient and test data from the Testing & Lab module of ICMR with S3 system to make it available to field health functionaries at national, state and district level. Positive case management has been extended by developing Status and Outcome updation module. Another module has been developed to integrate Bluetooth contacts and self-assessment data from Aarogya Setu to augment surveillance and contact tracing. Dashboards and action taken reports have been developed to facilitate monitoring at National and State levels. Besides, NIC also provided necessary technical support on other modules Logistics Management, Dashboards and Surveillance modules.

Deployment Architecture Redesign & Implementation
Looking at the future requirements, NIC provided necessary guidance in redesigning, proper sizing of deployment infrastructure and assisted in its implementation. The performance issues were resolved through the implementation of Application Monitoring Tool and query optimization.

API Integration
NIC developed APIs for the integration of near real-time COVID-19 Positive Patient Data from ICMR. To extend the reach of contact tracing and surveillance, Bluetooth contact tracing, self-assessment and projected hotspot data has been integrated from Aarogya Setu through Central Data Hub. To provide a 360-degree view of data at National Level, API based integration of S3 has been implemented with various third-party apps and systems developed at state-levels. API is also developed and integrated with Central Data Hub to provide data related to Outcome updated on Positive patients, surveillance information, manual contact tracing information and logistics information.

Coordination with States/Districts and Technical Support
NIC is extending necessary guidance and technical support at central, state and district levels on various aspects of S3 implementation. NIC officers from States and Districts are also actively involved in extending the support.

Dashboard and Data Analytics
NIC also assisted in designing appropriate dashboards and analytics for central, state and district officers.

Aarogya Setu
Aarogya Setu is a COVID-19 tracking mobile application developed by NIC with voluntary support from industry. The purpose of this app is to spread awareness on COVID-19 and to connect essential COVID-19 related health services to the people of India. The app facilitates Bluetooth based contact tracing of suspected contacts of COVID Positive patients. The app provides an option of self-assessment by the users and reports their symptoms.

Aarogya Setu integrates through Exchange Module of Central Data Hub to share data with Lab Module and S3 System. An analytical dashboard has been implemented by Aarogya Setu as part of the solution for state and district officers.

Centralized Covid Data Hub (CDH)
Data is powerful only if it is gathered in real-time from its sources and securely shared with all the stakeholders to leverage its full potential. Looking at the importance and sensitivity of data, it was decided by the Empowered Group on Technology and Data Management that the important COVID related Data from various source systems would be consolidated and minimal data would be shared with various agencies from Government and private with approval of Empowered Group.

Accordingly, NIC created a Central Data Hub at NIC Data Centre, which facilitates the integration of data from various source systems including of ICMR and S3. The data is then shared with authorized agencies and systems in a restricted and secured manner for contact tracing and surveillance. The Centralized Data Hub enables seamless connectivity exchange of data between various systems and services.

Further, NIC has also designed and developed analytical dashboards for use by various government agencies for decision-making. An exclusive Data Quality and API Exchange dashboard has been developed to monitor the quality of data received from various sources and take corrective measures as per requirement.

Way Forward
NIC Technical support & services in management and integration of diverse systems along with the establishment of state-of-the-art data exchange framework are playing a vital role in planning, monitoring and management of different aspects of the pandemic. Sharing of data from the source in near real-time has helped in establishing integrated view and reliability in the overall system. The processes put in place have also helped in improving the quality and security of data exchange across systems for better planning and decision-making. NIC will keep on striving to further enhance and improve the services, to help government, front-line workers and citizens to fight the pandemic.
