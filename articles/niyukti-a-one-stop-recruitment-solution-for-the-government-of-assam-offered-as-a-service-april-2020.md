---
title: "Niyukti: A one stop recruitment solution for the Government of Assam offered as a service"
publication: "Informatics"
issue_date: "April 2020"
pages: [20, 21]
author: "Dr. DIBAKAR RAY"
section: "eGov Products & Services"
---

## Niyukti: A one stop recruitment solution for the Government of Assam offered as a service

Since its inception in the year 2017, Niyukti has quickly evolved as a widely used recruitment solution in Assam Government. Its USP lies in the fact that it is offered as a service to the recruiting agencies, thereby allowing them to quickly onboard with a recruitment process in no time. Already 16 recruitments have been successfully conducted so far and the number is ever increasing.
The genesis of Niyukti goes back to the year 2017 when the Office of the Deputy Commissioner, Darrang decided to conduct recruitment for few posts of Junior Assistant. To avoid tedious process of recruiting offline, Darrang District Administration decided to accept applications online and NIC Darrang was requested to provide a solution. Accordingly, a web-based recruitment system was developed by NIC Darrang for Darrang district administration and the whole recruitment process was conducted successfully. Immediately after that, requests for similar recruitment system came from Assam Information Commission and Deputy Commissioner, Jorhat as they were planning to recruit for multiple posts. The recruitment system developed for Darrang District was successfully used for these two recruitments too. Subsequently, when a common recruitment platform for the entire state was envisaged to cater to the growing need of recruitment solution for various quarters in the government, the application developed at Darrang District was adopted for use across the State and necessary work for extending and scaling up the application was taken up. The portal got named as “Niyukti” the Assamese synonym for the word recruitment and is currently available at https://niyukti.assam.gov.in.
Introduction
As on date, Niyukti is serving as a complete recruitment solution offered as a service to various recruiting agencies of the Government of Assam. The project has reached a high efficiency as well as maturity level after being used by as many as thirteen different institutions among which the state’s Secretariat Administration Department, Assam Information Commission, Majuli District Administration, Sonitpur District Administration, Biswanath District Administration, Office of the Commissioner Upper Assam Division, Barpeta District Administration are to name a few. The usage statistics of Niyukti over time depicts how the system has evolved as a solution within a short span of time.
Technical overview
Niyukti is a web-application developed using the open-source technology stack and works as a multi-tenant application with single instance of the web-application and multiple instance of the databases. Each recruiter gets his own instance of database. The technical specifications are mentioned below.
Web Server: Apache
RDBMS: MySQL (MariaDB, Postgres compatible)
Languages & Technology: PHP, Javascript, CSS
Framework: CodeIgniter, JQuery, Bootstrap
Design Pattern: Model-view-Controller (MVC)
The application is currently hosted in NIC Assam mini cloud on Linux virtual machines.
Salient features
• Niyukti offers the recruitment solution as a service. A recruiting agency can come onboard as a recruiter in the Niyukti portal and can immediately initiate their recruitment process with minimum amount of application level configurations. Therefore, need of owning a product or website to conduct a recruitment is not necessary.
• The application has no hard coded values so any recruiter can go on-board without any code level changes.
• As it is a single instance multi-tenant solution which is already security audited and hosted, any recruitment can go live within a minimum time frame.
• Once on-boarded, every department gets its own dedicated home page for publishing information specific to their recruitment and an authorised dashboard with real-time information about their on-going recruitment.
• All the major processes like setting up of application receiving window, exam venue/ hall assignment, issuing of admit card and call letters, publishing of results etc. are available at the login of the recruiter.
• As majority of users these days prefer to apply from their mobile phones, the system is designed as a complete responsive web application and can be used seamlessly from mobile devices.
• The user interface for the applicants is kept quite simple and intuitive so that user with any level of competency can use it with ease.
• The tedious job of exam/interview venue assignment to verified applicants is just reduced to one single button click thereby making the life of a recruiter lot easier.
• Readily available integration with SMS and email gateways makes the job of notifying the applicants easier.
• Integration with payment gateway enables the recruiter to collect the necessary application fees online.
Future Scope
Niyukti is already serving as a unified job board for the entire state of Assam, a common meeting point for both Government recruiters as well as for the job seekers. However, Niyukti aspires to be a unique platform crossing the barriers of a traditional recruitment system and not just remain a mere web application for receiving applications from job seekers. The development work is already underway for features like progressive web interface, applicant profiling, job alerts as push notification for applicants, multiple simultaneous recruitment processes for same organisation. More advanced features like user profile screening using analytics, applicant usage mining, etc., may enable the portal to bridge the gap between applicant and recruiter thereby allowing the right candidate to find the right job or vice versa.
For further information, please contact:
State Informatics Officer
NIC Assam State Centre, First Floor, Composite Building
Near Last Gate of Assam Secretariat, Dispur, Guwahati
Assam -781006
Email: sio-asm@nic.in, Phone: 0361-2237164
Tapan Gogoi
Sr. Technical Director
tapan.gogoi@nic.in
Rahul Deka
Scientist-C
ar.deka@nic.in
Gautam Ch. Deva
Sarma
Scientist-C
gcd.sarma@nic.in
Figure 1: Niyukti Process Workflow
1 Publishing the Recruitment Notice
Recruiter Publishes the recruitment notification inNiyog portal
2 Verification &
Venue Assignment
• Recruiter verifies applications on the system
• Assign venue to applicant with one button click
3 Creating Attendance sheets
Attendance sheets are auto-generated for conducting the exams.
6 Applicant Applies for a Post
• Applicant registers & submits applications on Niyog Portal.
• Instant email & SMS alerts.
5 Publishing Results
• After exam, recruiter publishes result in the notice board.
• Instant email & SMS alerts.
• Applicants are further shortlisted for next round.
4 Issuing Admit Card/ Call letters
• Admit cards are automatically issued as per the configured template
• Instant email & SMS alerts.
Figure 2: Growing usage of Niyukti
Niyukti, Online Recruitment System developed by National Informatics Centre, Assam to automate the process of recruitment has made the entire process very convenient for the Government as well as for the applicants. Applicants can apply from anywhere anytime making it a very cost effective and convenient solution. The Secretariat Administration Department has adopted the system for its recruitment process. Niyukti is being adopted by several districts for their recruitment. We will recommend other departments also to use Niyukti in their recruitments. I wish all the success to the project.
Dr. M. Angamuthu, IAS
Commissioner and Secretary
Government of Assam
Figure 3: The multi-tenant architecture of Niyukti
Web Interface for Applicants
Recruiter A Web Interface for Recruiter
Recruiter C Database Instance
Niyukti Application
Recruiter B Web Interface for Recruiter
Recruiter B Database Instance
Recruiter C Web Interface for Recruiter
Recruiter A Database Instance
