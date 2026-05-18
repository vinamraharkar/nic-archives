---
title: "DGCA Examination System: UDAAN"
publication: "Informatics"
issue_date: "July 2012"
pages: [8, 9, 10, 11]
author: "Deepak Khare, Shilpi Jain, Parveen Bhardwaj"
section: "E-Gov Products & Services"
---

## DGCA Examination System: UDAAN

Since the Launch of Udaan in October 2011, it has increased the transparency in whole process of conduction of examination for the issue of licenses in respect of pilots, engineers including pilots holding foreign license.
The Directorate General of Civil Aviation is an attached office of the Ministry of Civil Aviation and is the regulatory body in the field of Civil Aviation, primarily dealing with safety issues. It is responsible for regulation of air transport services to/from/within India and for enforcement of civil air regulations, air safety and airworthiness standards. It also co-ordinates all regulatory functions associated with International Civil Aviation Organisation.
Its Headquarter is located in New Delhi with regional offices in the various parts of India.
The main function of the Directorate General of Civil Aviation is to regulate all civil aviation matter. Some of the salient functions are as under:
1. Regulation of air transport services to/from/within India in accordance with the provisions of the Aircraft Rules, 1937, including bilateral and multilateral with foreign countries and the policy pronouncements of the government;
2. Registration of civil aircraft;
3. Licensing of pilots, aircraft maintenance engineers and monitoring of flight crew standards;
4. Licensing of aerodromes and air carriers;
5. Supervision of training activities of Flying/Gliding etc.
There are certain requirements to be fulfilled in fixed time to obtain a Pilot Licence. The computerised system for generation of Pilot Licensing, developed by NIC Team at DGCA, is already implemented. These are flying experience, fulfilling pre-defined medical parameters, radio-telephone licence and passing of DGCA exams. As there are different categories of licences such as PPL (Private Pilot Licence), CPL (Commercial Pilot Licence) & ALTP (Airline Transport Pilot Licence) etc., the candidates have to pass different sets of papers for each category and the aircraft to be endorsed on the licence. DGCA Exams are conducted by Central Examination Office of DGCA on a regular basis i.e. 4 times in a year.
THE HISTORY OF EXAMINATION SYSYTEM
The examination system of DGCA was computerised way back in early 1990s using the platform Sybase. It was redesigned in the year 2000-2001 to work in local environment of Examination Office on the Microsoft platform of Visual Basic 6.0 and SQL Server 2000.
In the year 2008-09, DGCA desired to switch over to web-based examination system with online application and online payment of fee and declaration of results.
With the new requirement, the scope of the project was to build a web-based application for the defined functionalities. The NIC Team at DGCA undertook the development of new Web application with the new scope and requirements as given by DGCA.
IMPLEMENTATION METHODOLOGY
The current application is developed using Java and MS SQL SERVER 2005 and is hosted at http://udaan.nic.in in the National Data Centre at Hyderabad with Apache Tomcat as web server. This was implemented for the Pilot Exam conducted by DGCA in October 2011 session.
The Application consists of 3 modules, Pre-exam processing (L1), the examination (OMR and Online), and post exam processing (L3) along with the data migration.
The salient features of the above modules are as follows:
DATA MIGRATION
The most important step for effective launching of the UDAAN application was migration of the data from old database to the new one. The old data consisted of the personal details of the candidates along with their history of attempts taken for the DGCA examinations, marks secured, previous examination schedules etc.
The following steps were used for complete migration:
l Template Design: The data migration templates were defined to map the existing database to the new database to enable the porting of data.
l Data Migration Scripts : Data migration scripts were written to enable the one time data migration
l Data migration on day Zero : All the required data in the existing database was migrated to the new database
SHRI AJIT SINGH Minister of Civil Aviation Government of India
I am happy to learn that ‘Informatics’ - an e-Governance publication from National Informatics Centre, is bringing a special issue featuring DGCA in particular and Civil Aviation in general.
Information technology holds the potential providing the critical information and delivery of public services in fast, more effective and efficient manner.
NIC Civil Aviation Team is playing a pivotal role in providing and promoting ICT culture by delegating accurate, transparent and responsive information and services to the Ministry of Civil Aviation and its attached offices.
I appreciate the NIC efforts in computerizing the Pilot Examination System and successful conduction of Online Examination for Pilots in last 3 sessions. This has increased the transparency and efficiency in examination process of DGCA and resulted in timely dissemination of information and results to the Pilot candidates.
I wish the ‘Informatics’ all success.
L1 MODULE (PRE EXAM PROCESSING)
l Online application for new Registration with DGCA.
l Verification of application by DGCA Officers and subsequent generation of his / her Computer Number along with his login details for further using of the Udaan (Exam) application i.e. new candidate profile creation.
l Generation of login details for the already registered candidates (old Sybase and VB applications) i.e. old candidate profile creation and updation.
l Releasing of Exams Schedule by DGCA Officers using Udaan application, along with the choice of examination venues and defining the paper policy for various papers i.e. maximum marks, pass marks, oral / essay components etc.
l Online Application for OMR exam, Online exam, Oral Exam by the registered candidate. The candidates are allowed to apply for a particular exam based on his previous attempts history. This eligibility check is done online at the time of application submission.
l Online payment of fee using e-Payment Gateway with ICICI Bank
l Verification of applications and Generating Roll Numbers by DGCA Officers
l Allotment of seat for the online exam, based on the candidate’s choice and availability of seats at various venues.
l The candidates are sent automatic mails at various stages of application processing that keeps them updated about the status of their application (application submission, verification, rejection/acceptance of application with reason etc.)
l Alternatively the candidate can query his application status by logging in the Udaan System using his login details
l Transferring of eligible candidate’s data to L2 Process along with their paper, roll number, venue details, and login details for using L2.
l Various Pre Examination Reports like computer numbers generated / rejected lists, centre / paper / category wise admitted candidates list, Pre – exam analysis reports, Fee reports, attendance sheets etc.
L2 MODULE (EXAMINATION)
l OMR Based Exam - The DGCA conducts the OMR based Exams after collecting information and generation of roll numbers using the L-1 module.
l Online Exam (VIMANIC) – The online examination of candidates is conducted using the VIMANIC application. VIMANIC is developed & maintained by NIC Hyderabad Transport Project team and hosted at National Data Centre in Hyderabad. DGCA hires various test centres with suitable infrastructure, in different cities of India for the conduction of Examination. All the venues are connected to VIMANIC application server using the NKN connectivity. The connectivity with suitable bandwidth is looked after by NIC Network division on all India basis. The salient features of VIMANIC are
l Only the predefined exam venues can access the VIMANIC application
l A continuous connectivity is maintained with the client machine and the VIMANIC server
l All the data transfer between the client and the server takes place in SSL mode in encrypted format.
l VIMANIC application generates a secret pin for each candidate before the actual exam time. This secret pin is handed over to the candidate just before the commencement of the exam by the Centre Controller at the exam venue
l In addition to the login / password provided by the L1 Process, this secret pin is used by the candidate to initiate the exam.
l All the candidates are posed with same sets of questions though in different order
l If there is any abrupt disruption in any candidate’s exam because of hardware, link or application failure, VIMANIC has a provision of restarting the candidate’s exam from the same place where the disruption took place. In such a case a Master Password, which is in possession of the Centre Controller is also needed to relogin
l Candidates have the provision of revisiting the already attempted questions and modifying their answers till the time they finally submit their exam.
l VIMANIC also gives a provision to the candidate for recording an objection against a particular question, if he feels there is some discrepancy in it.
l An objection review committee at DGCA reviews the objection and if it is found valid, the marks for all the candidates, who were asked that question, are adjusted accordingly.
l Once all the objections are removed, the complete L2 data along with the marks and status of candidate (Present / Absent / Terminated) is transferred to L3 for post exam processing.
L3 MODULE (POST EXAM PROCESSING)
l Uploading and processing of VIMANIC Data
l Absentees Entry for the OMR exam
l Uploading of OMR Data
l Processing of OMR Data – Absentee / paper / category etc mismatch
l Scheduling of Oral exams for eligible candidates. Eligibility lists are prepared based on the processed VIMANIC data in conjunction with the Paper Policy defined in L1.
l Declaration of eligible candidates list for oral exam (for some papers where the final result is declared along with the OMR/Online exam)
l Oral Marks Entry (for some papers where the final result is declared along with the OMR/Online exam)
l Essay Marks Entry (for some papers where the final result is declared along with the OMR/Online exam)
l Result Declaration – Based on the paper policy defined by DGCA Officers in L1, The candidates are marked Pass / Fail.
l Final Publishing of the result on UDAAN, where candidates can query their marks.
l Post Examination Reports – Oral eligibility Lists, Result Checklist, Register Print for physical archiving of declared result, post exam analysis etc.
I-CARD GENERATION
The module for generation of I-card has been developed and tested by DGCA officers. This will be implemented in the 2nd phase of Udaan application. The module has the provision for
l Capturing and updating of the photograph of the candidate
l Capturing of fingerprint of the candidate
It is proposed that the candidate will be required to come at any one of the designated DGCA Offices where his biometric credentials will be captured and an I-card will be generated then and there only that will be signed by the candidate and the authorised DGCA Officer before handing it over to the candidate. This will be done at any time after registration and before the candidate’s 1st attempt at the exam, after the implementation of this module.
OTHER FEATURES
l The System has the provision for updating of candidate profile by DGCA Officer
l Creation of new role and profile for the Udaan use.
l Resetting of Password by DGCA officer
l Various Master Data entry screens.
BENEFITS
l The system has increased the transparency in whole process of conduction of examination.
l No manual intervention, right from the application acceptance till result declaration, in case of online examinations.
l Reduced time to declare the results.
l Reduced workload on DGCA staff in terms of data entry.
l Applicants can check the status of their applications online at various processing stages of the applications.
l The online examination history of the candidate is available to the candidate also
STATISTICS
Since the Launch of Udaan in October 2011
l New Registrations 3500
l Applications rejected for registration 310
l Candidates appeared for Online Exam 5000
l Online Papers conducted 12282
l Online Exam Centres in India 10
l Candidates appeared for OMR Exam 2150
FOR MORE DETAILS CONTACT:
Mr Deepak Khare Scientist ‘F’ R No 263, B Wing Rajiv Gandhi Bhawan, Aurobindo Marg, New Delhi Tel No. 011-24602731 E-Mail - dkhare@nic.in
