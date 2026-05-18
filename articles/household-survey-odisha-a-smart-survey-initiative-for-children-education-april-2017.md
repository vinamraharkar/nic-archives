---
title: "Household Survey, Odisha: A Smart Survey Initiative for Children Education"
publication: "Informatics"
issue_date: "April 2017"
pages: [38, 39, 40]
author: "Edited by Prashant Belawariar, Sushanta Kumar Bhol, Malaya Kumar Das, Venkataramana Boddepalli"
section: "E-GOV. PRODUCTS & SERVICES"
---

## Household Survey, Odisha: A Smart Survey Initiative for Children Education

Household Survey is a smart initiative of School and Mass Education Department which enables efficient and convenient computerization of the collected information of children through Block level MIS personnel and preparation of the Child database, Data consolidation, Data verification and Web hosting.

Right of Children to Free and Compulsory Education (RCFCE) Act. 2009 and State RCFCE Rule-2010 instructs to maintain the Records of 6 to 14 years age group children in the State and to ensure elementary education is provided to each and every such child. There was a need to conduct a Household Survey through door to door enumeration to identify each and every child up to 14 years age and maintain the Child Records as per the parameters prescribed. The database was created for the Household Survey for:
1. Assessing the enrollment position as well as number of out of school children.
2. Tracking each and every out of school child in 0-14 age group and providing need based inputs to bring back them to the schooling system.
3. Identifying the reason for dropping out of school so that remedial action can be initiated.
4. Identifying the pre-school age children in Anganwadi Centers and Pre-Schools and assess the future school going population in villages for advance action in terms of providing infrastructure, teachers, text books, uniforms etc.
5. Identifying the class wise in school children and track the attendance & achievement and provide facilities like free text books, Uniform, Aids & Appliances for CWSN etc.
6. Identifying the Children reading in various institutions and eliminate fake & duplicate enrollments from the system.
7. Integrating child data with Aadhaar Number (UID) for identification and use by the department for several welfare schemes initiated by Government of Odisha as well as Government of India.
8. Planning all activities related to implementation of RTE-SSA in the State with need based planning.

We acknowledge the efforts of all District Education officers (DEOs), District Project Coordinators (DPCs), Block Education Officers (BEOs), ABEO-cum-BRCCs, Cluster Resource Centre Coordinators (CRCCs), State/District/Block level MIS staff, all Head Masters & Teachers and SMC members for their cooperation and dedication to make the Household Survey a success in the State. We acknowledge NIC-Bhubaneswar for their technical support in database creation, web hosting and reporting for Household Survey 2016.
— Mahendra Kumar Mallik, IAS State Project Director, OPEPA

OBJECTIVE
The objective of the Household Survey was to identify each and every child in 0-14 age group throughout the State through door-to-door survey in each habitation by enumerators and create a database which can be updated monthly/annually with little efforts carrying the change in the educational status of each child.

INNOVATIONS APPLIED
Survey
The first phase is door-to-door survey by school teachers and Anganwadi workers for filling of the Child Record Formats (CRF). The objective was to cover each and every household and identify each child in 6-14 age group & record the information in the CRF. The available Anganwadi registers may be referred for ensuring the coverage of all children in the survey. Department of School and Mass Education Odisha collected the data with the help of enumerators.

Digitization
The second phase is to computerize the collected information of children through Block level MIS personnel and prepare the Child database, data consolidation, data verification and webhosting.

Getting the huge Household survey data to central server is the main problem. There are many issues like lack of systems and connectivity in block level. In addition the offline system needs workstations with multiple dump terminals at block level so that multiple data entry operators can enter the collected data at the same time. In order to solve this, a generic approach was needed which could work both offline and online.

Before uploading the data to the central server, master data had to be prepared properly. So a model was designed to collect master data of all districts, blocks, GPs (Gram panchayats), clusters, villages and habitations. Another goal of this model is to assign MIS PC (Manage information System Planning Coordinator) to each block with the names and mobile numbers. Once the door-to-door survey was completed by the enumerators, Digitization of Household Survey data at block level was started. If net connectivity is available at the block level data will be entered to the system through the portal by data entry operators after login with valid credentials. But where at block level, systems are not available for multiple data entry operators, another offline model (UNIX workstation) was prepared so that multiple data entry operators can enter the data from dumb terminal. All the data entered by multiple data entry operators at same time will be stored in the database of workstation. Data entered by multiple data entry operators from the dump terminals will be stored in SQLite database of workstation.

Once the data entry is completed the SQLite database backups can be brought to the corresponding Block/District education office and the backups are uploaded to the server through portal.

PROGRAM MANAGEMENT
Planning
Odisha Primary Education Program Authority (OPEPA) decided to sample Household survey data to help the Administrative unit down the line i.e. District and Block level, so that huge sampling work can be completed on time.

Stakeholder Management
There are different stakeholders in the process which had to be managed viz. Block, GP, District and OPEPA. Block Education Officer (BEO), District Education Officer (DEO), Odisha Primary Education Programme Authority (OPEPA), NIC

Performance Management
The Master data populated by the Block level resources need to be validated by District level resources. Extreme care has to be taken at this phase to avoid additional efforts at later stage of the project. Again, once the data is published online and the stake holders are responsible for updating of their respective data within a timeframe.

Organization change management
The changes due to the introduction of new sample survey of Household data has caused the OPEPA to monitor the picture and information uploaded by the Block and District level Program manager. It also made necessary the verification of the information before it is uploaded to the web.

Communication Management and Governance
A Nodal officer has been appointed to oversee that the process is carried out smoothly and no grievance is pending at the Government end.

Process Re-engineering
Earlier, the online data collection module was restricted to District with good net connectivity but the combination of offline and online module helps to reach the last mile to collect data from Block level. Now this new idea has given them opportunity to concentrate on the quality of the data and stick to the commitment to deliver it on time.

Training and Workshop
MIS PC (Manage information System Planning Coordinator) of all blocks were called during the workshop and educated regarding office setup procedure and data entry module. Training was imparted to the team to expedite the job at Block and District level.

SUMMARY
1. Total 85,63,970 Households in 95,105 habitations of the state were surveyed.
2. Detailed database of 84,24,700 children between 0-14 years has been prepared.
3. 42,125 children were identified as Out of school and steps have been taken to enroll them into schools.
4. Data of 0-14 years were handed over to W&CD Department for ensuring their enrollment in Anganwadis.
5. Database of all In-School children were tagged to their respective classes in the schools.
6. Fake duplicate names from enrollment were removed during the survey
7. All activities of SSA, MDM etc. were made child centric.
8. Steps have been taken to link Aadhaar number to each child in the database.
9. Household Survey data will be updated annually during April-June to update the educational status of each child and add to new entrants to this age group.

WAY FORWARD
Simplifying the process of offline and online integration of Household Survey Data to HHL portal is one important aspect and creating opportunity for the state level administrator and HRD Ministry to explore the portal as decision support system. After successful implementation of the model, Government of India scrapped the old method i.e. UDISE and the entire project was awarded to National Informatics Centre. In the age of Digital India the significance of the project is vital for NIC as well as Ministry of HRD. The following objectives have been decided:
1. All areas of the application need to be made generic
2. Initial processes were already started with Ministry of HRD to roll out the project in pan India level
3. Setting of a PMU at OPEPA
