---
title: "LEVERAGING EMERGING TECHNOLOGIES IN INTEGRATED PROPERTY REGISTRATION & LAND RECORDS SOLUTION"
publication: "Informatics"
issue_date: "April 2014"
pages: [27, 28]
author: "Vivek Verma, G.S. Bansal, G.S. Saini"
section: "Technology Update"
---

## LEVERAGING EMERGING TECHNOLOGIES IN INTEGRATED PROPERTY REGISTRATION & LAND RECORDS SOLUTION

Emerging technologies like biometric authentications, DSCs, 2-D Bar Code along with QR Code, OTP, Web services based data replication, SMS, Web based access and AMS etc. have been increasingly employed in Property Registration and Land Records Solutions to ensure secure & authenticated access, enhanced quality & hassle free service delivery with appropriate information security to the general public. This article introspects on how these novel technologies have been integrated with the HARIS – HALRIS software solutions to facilitate the citizens to access their Records-of-rights on anywhere, anytime basis.

Many innovative initiatives in computerization of property registration and land records have been taken up by the Government of Haryana. The property registration work has been computerized using the HARIS (Haryana Registration Information System) software, developed by NIC –Haryana, which is working at all 122 SRO (Tehsils & Sub-Tehsils) offices across Haryana and providing the property registration services in efficient manner. General public is getting diverse services like stamp duty evaluation and registration across the counter in the tehsil. The photographs of witnesses are also taken along with the sellers and buyers on-line. This has reduced the incidents of wrong witnesses, which was prevalent before the implementation of this system. To enhance the transparency in the deed registration work, Appointment Management System (AMS) of giving appointments for deed registration has been introduced with the help of NIC Haryana. This is a Queue Management at HARIS centres for deed registration in First In First Out order. Now the citizens know beforehand what charges/fee they are required to pay. Collector rates are also available on http://jamabandi.nic.in website. These features have helped in elimination of the middlemen, who were the main source of corruption in the process.

Copy of Record of Right (Jamabandi)

The major land records document such as Jamabandi and Mutation have been computerized using the Haryana Land Records Information System (HALRIS) software, developed by NIC. HALRIS provides a workflow-based approach for the management of the land record documents and it has changed the delivery model from patwari centric to tehsil centric, where all the revenue related services are provided from tehsil/sub-tehsil level centers. For integrating the digitized maps with the Record of Right and Mutation, Bhu-Naksha software is being used. All the three i.e. HARIS, HALRIS and Bhu-Naksha seamlessly integrated to provide a platform for dynamically integrating the property registration, land records and Cadastral Maps.

For ensuring secure & authenticated access, enhanced quality & hassle free service delivery with appropriate information security to the general public, a number of emerging technologies (like biometric authentications, DSCs, 2-D Bar Code along with QR Code, OTP, Web services based data replication, SMS, Web based access and AMS etc.) have been integrated with the HARIS – HALRIS software solutions, facilitating the citizens to access their Records-of-rights on anywhere, anytime basis and helping in reduction of litigations and frauds, as well as elimination of middle men from the service delivery process.

Team with the award

SYNCHRONIZATION OF TEHSIL LEVEL SERVERS WITH STATE DATA CENTER
Solution to synchronize the Jamabandi Web Nakal data hosted at State Data Center within 15 minutes of the occurrence of any transaction like deed registration, mutation etc at tehsil/sub-tehsil level is implemented using a set of .Net based windows and web services. Solution can run using different connectivity modes like SWAN, NICNET, and broadband in a very simplified manner.

Digitally signed Record of Right
To provide the digitally signed copies of ROR (Jamabandi Nakal), digital signature certificates of the patwaries posted in HALRIS centers have been created. Nakal module of HALRIS has been enhanced to generate the nakal in pdf format and digitally signed using the DSC token of the patwari on duty. Every digitally signed Nakal carries a 15 digit unique ID and copy of the Nakal is transmitted to State Data Center so that it can be verified using the unique ID from jamabandi.nic.in.

Digital Signing of ROR Database
Revenue department decided to digitally sign the ROR data stored at State Data Center. Main idea behind this is to provide the ROR copy from digitally signed database on web. Database Signer application is developed to digitally sign & verify the database record by record. Windows service responsible for data synchronization of tehsil server with data center is also enhanced to transmit the digitally signed records.

Mobile app for project monitoring
Android based mobile apps has been developed to fetch the implementation status of HARIS and HALRIS by giving the tehsil code as input. It uses a web service to fetch the status of the selected tehsil from the data center. This application is useful for monitoring the project implementation by the Senior Revenue Officers.

User access through mobile-based OTP
Jamabandi website is enhanced to authenticate the users using the SMS based OTP. This OTP based authentication is required to access the ROR generated from digitally signed database, scanned deeds and mutations.

Two Dimensional bar coded RORs
Jamabandi nakal module of HALRIS is enhanced to print the 2-D bar code using PDF 417 format, XML and hashing techniques. This solution has two main components - first is generation of 2-D bar code and second is bar code verification. The main objective of devising this solution is to generate the copies of ROR that can be verified to check any kind of tampering.

QR Code on ROR generated from web
Jamabandi website is enhanced to print the QR Code on the copies of ROR. Smart phone users can easily get the ROR issued from the website by scanning the QR code.

Biometrics based Access & Authentication
Biometric based authentication is provided in HALRIS and all critical save points in HALRIS like mutation sanctioning and incorporation etc can be accessed by biometrics only.

“Dynamic Integration of Property Registration, Land Records and Cadastral Maps” has received National Silver Award on e-Governance 2013-14 under the category “Incremental Innovation in Existing Project”.
