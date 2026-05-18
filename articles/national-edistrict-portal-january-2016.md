---
title: "National eDistrict Portal"
publication: "Informatics"
issue_date: "January 2016"
pages: [12, 13]
author: "Mala Mittal, M. Nazieruddin, Siva Prasath"
section: "E-GOV PRODUCTS & SERVICES"
---

## National eDistrict Portal

National eDistrict Portal provides a real time view of the State-and category wise eDistrict services available to citizen such as Issue of Certificates, Social Welfare Schemes, Revenue Court, Ration Card, Grievance redress, RTI services and also various optional services.

eDistrict is one of the 31 Mission Mode Projects (MMPs) under National e-Governance Plan of Indian government. Department of Electronics and Information Technology (DeitY) is the nodal Department for e-District project, which is being implemented by State Governments through their designated agencies. The MMPs aims at electronic delivery of identified high volume citizen centric services at district and sub-district level through automation of workflow, backend computerization and data digitization across participating departments.

Under the project, it was envisaged to have a common platform to facilitate content creation, monitoring and interaction between all states involved in eDistrict MMP. Thus the National eDistrict Portal [http://edistrict.gov.in] was designed and developed by NIC. The portal enables better coordination among States to ensure faster implementation of eDistrict MMP. The Portal is also a knowledge repository and single point of reference for all eDistrict MMP related progress data, information, circulars, guidelines, RFPs, demo URLs, applications etc.

HIGHLIGHTS
• A gateway to the Demo site/URL of existing eDistrict Modules /Applications for the other states to have hands-on experience
• A Repository of generic Modules/ Applications related to e-district MMP which can be used by other State units
• Model MoUs for NIC’s role as Application Development Agency and System Integrator
• A medium for States to connect with each other for sharing artifacts
• Facility for uploading/updating the best practices followed by various States with reference to eDistrict services
• Collection of FAQs, case studies and circulars related to eDistrict MMP
• A forum to discuss common issues with respect to eDistrict

The Portal has an online tool for monitoring & tracking project implementation. Besides, the physical and financial progress of eDistrict MMP can be viewed at State level. It has a real-time dashboard summarizing the category coverage of the eDistrict services being offered by various States and the total number of services in each State. The portal facilitates State-wise status tracking of services through application number and makes it available for citizens at a single click by providing the application number.

Along with other optional services, following are the mandatory service categories: Issue of Certificates, Social Welfare Schemes, Revenue Court, Ration Cards, Redressing of Grievance & RTI service.

“NATIONAL E-DISTRICT SERVICE TRACKER”- A CENTRALIZED MOBILE APP FOR STATUS TRACKING
For providing status-tracking facility to citizens through a single interface for all States, an android based mobile app called “National eDistrict Service Tracker” was developed which is available on Google App Store and Mobile App Store of DeitY

FEATURES OF “NATIONAL EDISTRICT SERVICE TRACKER”
• Provides State-wise/Category-wise listing of services available in all the States under eDistrict MMP.
• To track status of the application for services submitted by a citizen in his local district office of any state running eDistrict MMP services by providing his/her unique registration number.

TECHNOLOGY
Centralized eDistrict Server receives requests from multiple users through devices such as mobiles, tablets & desktop computers. The server has all the functional software components to handle the requests, accessible via REST APIs and all the meta information of State servers such as web service URLs written in REST or SOAP and return type format XML or JSON. All data processing are performed at the centralized eDistrict server.

List of States and services information is computed on Centralized eDistrict server and the response is returned to the device in JSON. Service information is captured through State servers using web services. The centralized eDistrict Server sends the application status requests to the relevant State eDistrict Servers. Based on application number/registration number provided by each user, State servers process requests and return the results to the Centralized eDistrict Server in different formats such as SOAP primitive, SOAP object and REST. Centralized eDistrict Server processes the data coming from State servers and then sends back response to device in JSON. Internally, the device handles JSON and then displays the data in a user-friendly manner.

IMPLEMENTATION
18 States running eDistrict MMP services are integrated with the centralized Mobile app – “National eDistrict Service Tracker” for providing Status Tracking Services. It has been planned to make the mobile App more generic and currently the cross platform development is also in progress.
