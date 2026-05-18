---
title: "On-Line Web Counseling"
publication: "Informatics"
issue_date: "January 2013"
pages: [20, 21, 22]
author: "D. KRISHNA RAO, VIJAY KUMAR VISHWAKARMA, MONAWAR HUSSAIN, S. V. KRISHNA PRASAD"
section: "E-Gov Products & Services"
---

## On-Line Web Counseling

Earlier counseling system was operated at six different locations simultaneously and eligible students have to visit any one of these counseling centers to seek admission. Students were to visit the counseling centers in person and the system used to cater 1000 / 2000 students a day, based on their rank in the entrance examination. Based on their eligibility, options and availability of seats, candidates were admitted in to various Colleges. Depending upon the vacancies / vacated seats, students had to visit the counseling centers more than once. The whole system used to take about 30-40 days for each round of counseling. The entire process of admissions to various courses (Polytechnic, Engg, MBA, MCA, M.Tech. etc.) used to take about 5-6 months and the students have to visit counseling center many times, waiting hours together for their turn.
In order to reduce the admission time and difficulties faced by the candidates in traveling to counseling centers, it was proposed to have a web based on-line counseling in the state.
WEB BASED COUNSELING
About 50 Help line centers (HLC) are established throughout the State and student can visit any of the 50 HLC for certificates verification. Students Bio-data is verified and the database is updated with corrections if any. Each student is given a scratch card and scratch card secret number is known only to the student. After verification, candidates can enter his options over the net from any internet center, home or from any Help Line Center. They can enter unlimited number of options and can edit their options any number of times till the last date.
After the last date, all the options are frozen and processed for seat allotment, based on the options given, entrance examination rank, reservation rules etc. Once the allotment is completed, results will be published over web. Students can download his allotment letter and report at the college. Respective colleges update counselling database with the student joining details.
In this way, the admission process is faster thus saving academic working days and candidates have to come to the counselling centres /help line centre only once.
SALIENT FEATURES
l Web based Hassel free admission
l Students and Parents need not travel to Counseling Centers and wait in the queues for long hours
Counseling College Students Options Students
(Course) Appeared Entered Admitted
EAMCET 962 (44) 2.1 lakhs 61 lakhs 1.34 lakhs
EAMCET (BiPC) 286 (2) 78,000 2.45 lakhs 8,048
ICET 1077 (8) 1.21 lakhs 7.14 lakhs 50,207
CEEP 311(32) 1.85 lakhs 27.23 lakhs 62,743
D.Pharmac 42 (2) 1,737 6,037 1025
EECC 944 (35) 29,437 3.48 lakhs 18,392
l Reduced Processing time for the entire Counseling
l Standardization of Counseling Procedures
l Admission rules and eligibility criteria are built-in
l Exhaustive Search algorithm to allot best seat
l Candidates can opt for as many as Colleges & Courses as he desires
l Allotment of best possible seat based on the options given
Admissions Conducted since 2009. Number of students / admissions made in 2012
THE MAJOR MODULES OF THIS APPLICATION ARE AS FOLLOWS
Student Module
Student module provides interface for :
l Registration of the Candidate: Allows students to register for counseling.
l Provides information about Colleges, Branches, Intake, Counseling procedures, Rules, Last year admission details etc
l Option Entry: Displays a list of eligible colleges and courses where candidates can give as many options as they desire. They can update/verify the options as many times as they can
l Download & Print Allotment Order
l Check Vacancy position
DEPARTMENT / COLLEGE / HLC MODULES
l Certificate verification: Allows physical verification of certificates at designated HLC and decides the eligibility of the candidate. Appropriate acknowledgement letters are printed and handed over to the candidate.
l Facilitates to rectify errors / update missing details in the application if any.
l Cancellation module: Cancelation details of candidates and returning their certificates is made possible through this module
l College Module: Each college has access to see the list of allotted candidates and update the database with the joining details of each candidate
ALLOTMENT MODULE
Seats are allotted based on the rank, options entered by the candidate, eligibility and reservation rules etc. Andhra Pradesh is divided in 4 regions (Andhra, Telangana, Rayalaseema and unreserved) for the purpose of admissions. The seats are reserved in to about 400 different categories based on gender, caste, region, physically handicapped, CAP, Sports, NCC etc. and AP has complex reservation rules. Candidates are eligible for admissions in multiple categories as per rules.
With about 700 engineering colleges and about 2 lakhs candidates and unlimited number of options, the allotment is a very complex process.
ENVIRONMENT & TESTING
This Counseling application developed is on Windows platform as a web based application using C#, ASP, Java Scripting, HTML using the IIS Web Server and MS-SQL Server 2008. Students need internet connection & browser to use the application. The application was tested for functionality, performance and security by professional auditing teams. The functionality was tested by STQC, Hyderabad and by user with about 5,000 students and about 50,000 options.
Performance
Various techniques were used to improve the performance. Some of them are: caching less frequently changing data, use of SQL procedures, closing the SQL connections at the earliest, analyzing all SQL queries with SQL analyzer, fine tuning the data types and field length etc. The average response time for 1000 virtual users for complete round trip is around 146.667 seconds as tested by STQC.
Security
Security audit was performed by different CERT-In certified security agencies every year. Besides the usual security precautions the other precautions taken are: double password for login, The scratch card technique , options encryption, salted password encryption, password hashing, option reconstruction, logging of every action by department , disabling SQL prompt are some of security features which protect the system and NIC employees.
APPLICATION HOSTING PLATFORM
For last so many years, Data Centre Web-Hosting team of Delhi, along with NDC Hyderabad team, have been functional in providing the web-hosting service support to various on-line counseling applications of various States Boards as well as Central Counseling Boards. Andhra Pradesh State Board counseling application is also one of them. Treating counseling application hosting as one of the most critical activity, special arrangements are made every year by setting up a dedicated team of highly skilled & experienced manpower and creating the setup of dedicated server infrastructure at NIC Data-Centre.
High capacity server clusters are deployed with requisite setup/configuration covering performance tuning, security hardening, load testing etc. Various state-of-art technologies like Load Balancing(LB), High Availability(HA) are used to handle any kind of heavy work load and hardware/software failures. Virtualization enabled Server setup is prepared for managing compute resources, quick provisioning, centralized monitoring etc. Intensive monitoring of the applications/server Infrastructure, continues on 24X7 basis, helps the data-centre team in providing seamless service to the end users.
Disaster Recovery setup is kept ready with having data replication happening continuously to remote site. A combination of replication technologies (in-house developed software as well as state-of-art software technologies) are used to handle the host based data replication between the primary and secondary sites.
