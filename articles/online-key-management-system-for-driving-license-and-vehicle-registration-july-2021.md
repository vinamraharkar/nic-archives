---
title: "Online Key Management System for Driving License and Vehicle Registration"
publication: "Informatics"
issue_date: "July 2021"
pages: [27, 28]
author: "RamaKrishna Y, Rajdeep Choudhury, and Jyoti Bhan Kaul"
section: "eGov Products & Services"
---

## Online Key Management System for Driving License and Vehicle Registration

The gazette notification No G S R 400(E) dated 31st May 2002 was issued by the Ministry of Road and Transport Highways (MoRTH) for the issuance of Smart Card-based DL/RC. Based on the notification, homegrown Operating system specifications (SCOSTA/ SCOSTA-CL) were developed which conforms to International Organization for Standardization (ISO)/International Electro-Technical Commission (IEC) standards. The gazette notification allowed each state to have separate processes for the issuance of the DL and RC Cards.

To bring uniformity across the country, the gazette notification of 1st March 2019 was notified. The technical inputs to the new Gazette notifications were given by NIC. The new format will bring in a unified system across the country. It also permits having more data stored on Smart Card Chip. The main objectives of the system are:
• To facilitate effective and time-bound citizen-centric service delivery
• To provide an affordable, accessible, cost-effective, and transparent system
• To increase productivity with efficiency through automation of processes

Features of the Product
• Security against fake Duplication/ Issuance
• Additional Pin Authentication
• Interoperability achieved across the country
• Secure data storage
• Secure communication
• Enhance Privacy protection
• Better Law enforcement
• Ease of handling

Technologies Used
• Client End Smart Card Manager, Browser
• Database PostgreSQL
• Operating System SCOSTA/SCOSTA CL, Windows
• Coding Language JAVA(JDK), JS, Spring-Hibernate, Tomcat
• Development Environment Eclipse

The New KMS for Issuance of Smart Card based DL/RC Cards at RTO will follow as below:
Retrieval of DL/RC user data from the API hosted by Vahan/Saarthi. Field by field matching of Data. Matching of Card File Parameters with those defined in DL/RC Card layout published in www.scosta.gov.in.
KMS application parses the data retrieved from the JSON string retrieved from the DL/RC card. After successful matching initiates the process of KMS. KMS process Completed.
Data is viewed on Screen. KMS application reads data from the DL/RC card. Writing the keys in the DL/RC Card and activate the DL/RC card. Post the data to the Saarthi/Vahan database using post API service hosted by Saarthi/Vahan.

Benefits of Project Implementation
• With the introduction of a web-based system, the interaction of the application with the local database has been eliminated making the system work faster. In an older system, the data was stored locally first before pushing it to the central database thereby increasing the data redundancy.
• The web KMS system has resulted in saving infrastructure at the local level.
• In an older system, a setup was needed to be created and installed in individual RTOs. But with a web-based KMS system, using a single url the application and its supporting software automatically get installed without any additional efforts.
• The Web-based KMS system also results in automatic updation at the client end.
• The project has helped in saving the time and ease of use by RTO’s officials for the issuance of DL/RC Smart cards.
• All the benefits stated above have resulted in making the entire project cost-effective.

Proposed solution for centralized Card Issuance management system with HSM Impact or benefits of ICT initiatives.
To enhance the security of online web services for the issuances of DL/RC Cards, it is proposed to use Hardware Security Module (HSM) to secure the key storage. It also provides cryptographic operation within a tamper-resistant hardware device. HSM has dedicated and powerful crypto processors which can simultaneously carry out thousands of crypto operations thereby making the KMS work fast and helping in bulk issuance.

NIC has developed a smart card application using HSM in National Population Register (NPR), Fisheries, etc. HSM shall be used for secure storage and fast access of master keys for various projects. HSM provides enhanced security and flexibility in KMS operations. Every KMS system will act as a client and will be connected to HSM through a secure network. KMS of personalized DL and RC cards will be done on KMS client systems by invoking a centralized Vahan/ Sarthi KMS application. The application will use authority keys from HSM.
