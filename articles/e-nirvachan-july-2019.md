---
title: "e-Nirvachan"
publication: "Informatics"
issue_date: "July 2019"
pages: [31, 32, 33]
author: "KAVITA BARKAKOTY, KABITA ROY DAS, JAYANTA KUMAR DEKA, BIJOY MAZUMDER, MRIDUL DEKA"
section: "E-GOV PRODUCTS & SERVICES"
---

## e-Nirvachan

An online Polling Personnel Management System for Election Department of Assam
The polling personnel must be preferably drawn from both the State Govt. Departments and the Central Govt. Offices during elections. To fulfil all these criteria, it is difficult to carry out such works by using a traditional methodology, and this necessitates the use of an IT application.
E-Nirvachan (Assam) is a solution product developed by NIC Assam for the management of election processes. It can be used for any election, be it parliamentary or assembly or any state level (Panchayat/Council) election. Initially, in order to ease the processes of manpower management for an election, this software was developed by NIC Nalbari, Assam, in consultation and guidance with NIC Assam State Unit and Chief Electoral Officer, Assam. The process of development of the application started during early 2014 Parliamentary Election. This Application was widely and successfully used by all the districts and subdivisions of Assam during all the elections held, including Local Body Elections, Panchayat Elections, Autonomous Council Elections and Bodoland Territorial Council Elections.

“To conduct free and fair elections, it is very important to allocate polling personnel at polling stations by using an automated randomization process to maintain impartiality, which is not possible without the help of an IT Application. To perform this in an easier way, an online application, Polling Party Management System (PPMAS) has been developed by NIC Assam and was successfully implemented in Bongaigaon District during Parliamentary Election 2019. It is found to be an excellent application with all requisite modules necessary for smooth working of the system. I congratulate the NIC team for putting in place this IT Application and wish all success in near future.”
ADIL KHAN, IAS Deputy Commissioner Bongaigaon

History
The randomization of polling person using Software Application was partially started in Assam since 2006 Assembly Election. During that period, a standalone Application using Visual Foxpro was developed and used in 3 or 4 districts of Assam. During the Parliamentary Election 2009, another application in ASP and SQL Server was developed and used in most of the districts of Assam as an offline web-based application. During the Assembly Election 2011, one more application with SQL Server and Dot Net Framework was developed and used in some of the districts of Assam. Since all the above applications need licensed version of SQL Server Database, it was not possible to implement it at the subdivision level. Hence, the need of the hour was to develop an application in Open Source Platform so that districts as well as sub-divisions could implement it without any legal issue. Therefore, a PHP/PostgreSql based application was developed during the Parliamentary Election 2014 and was used successfully by all the districts and subdivisions of Assam. The same application was also used during Assembly Election 2016 and BTC Election 2015 successfully.
Finally, it was decided to make the application a generic and secured web-based application so that it can be used in all types of election including the local body election.

Polling Personnel Management System (PPMS) is the outcome of all the experience gathered from previous elections in Assam.

“e-Nirvachan, the Polling Personal Management System, Assam has been extensively used by all Districts and Subdivisions of Assam in the recent Parliamentary Election 2019. It has been successfully developed by NIC Nalbari District Centre. During the election time, a large number of reports, as per the ECI norms, need to be generated. During this election, however, with the online application, all such reports could automatically be generated. I am very much impressed with the randomization process done by the software in presence of the central observer in a very short time and without any discrepancy. I wish all success to the project and implementing team of NIC Assam and DEO Office, Assam.”
BHARAT BHUSHAN DEV CHOUDHURY, ACS Deputy Commissioner Nalbari

Objectives
e-Nirvachan has been developed with the following objectives:
••To eradicate difficulties faced while using offline version of randomization software for the appointment of polling/ counting personnel till the current year like data integrity, software maintenance, version control etc.
••To bring each automation under one umbrella in connection with polling personnel and counting personnel appointments of the election districts of Assam, fulfilling all the guidelines laid down by the Election Commission of India (ECI).
••To have a centralized secure online system, which can make the whole process of automation more robust, controlled, easily available from everywhere and a system with easier maintenance.

Application Workflow
At first, the District Administration collects the employee data list from various departments/offices in a specific format as per software data entry form, for example, employee name, designation, basic pay, date of retirement, home constituency, office constituency, educational qualification, mobile number etc. The collected data is then fed into the software by engaging data entry operators or office staff. After completing this data, entry of employees, polling station list and constituency list are prepared and updated in the software. As soon as the election date is declared, the process of training of polling personnel begins, and the software effectively manages the complete training process.
At first, information such as training venue, hall and capacity under hall is collected. Then the software picks up the required persons (presiding or polling) and arranges them within the hall. Thereafter, an order copy of training is generated and distributed to the employees. The order copy contains information such as venue, hall and date/ timings of training. There is one more facility to send SMS to the polling personnel about the training schedule. However, in order to use this facility, the District Administration has to purchase an SMS pack. In the same way, the software generates attendance sheet, payment register and identity card for the training batches.
After the training is over, the process of group formation of polling personnel begins. This is called second level randomization. There are certain conditions for group formation of polling personnel as per ECI guidelines. Same guidelines are also used in Panchayat Election. The conditions are:
••Polling person posted in a particular constituency should not come from the same home, residential or department location constituency.
••At least, presiding and first polling person in a group should not be from the same office.
These conditions are strictly maintained in the software. However, the first condition is not possible for a single constituency district, and hence, those districts need to take permission from the Election Commissioner for flexibility of guidelines to be allowed. After group formation of polling parties, final appointment letter is generated and distributed through the department. The final appointment letter, generated through the above stage, does not reveal the polling station detail for the particular polling personnel group.
The actual polling station is available only after the third level of randomization. In this step, constituency wise polling stations for every polling personnel group are generated and displayed on a notice board on a day before election. Besides, an SMS alert facility is available. The SMS contains material receipt counter number, name and phone number of sector officials etc. On the day of material receipt, the polling personnel group directly comes to the said counter and can collect the polling materials instead of waiting in long queue.
There is one more feature to manage counting supervisor and assistant for counting of votes. Here, some of the polling persons available in the database are marked as counting supervisor and assistant and counting group is formed. Also, training is organised for the group in the same way as for polling personnel mentioned above.
All the randomization processes are done in the presence of an election observer. On satisfaction of the observer, the process is locked by the software. The Product Version I for e-Nirvachan (Assam) is available at http://ppmsassam.gov.in. The Application platform is PostgreSQL Database as the backend and PHP as frontend and third party library TCPDF6 for PDF report generation.

Target Audience
Respective District Election Officer
Respective Election Officer
Manpower Management Cell
Training Management Cell
Polling and Counting Personnel

Features
Following are the main features of PPMS:
Data Entry/ Edit Module
Using this module, data from various State/ Central Government Department officials are entered into the system to make a complete database of available manpower in the district. A provision to import data from excel format (by converting to CSV), as per need, is also there to ease the process.

First Randomization
Using randomization technique, the system picks suitable personnel with required percentage of reserve personnel to be used as polling personnel.

Training Batch Creation and Generation of Training Letters
After first randomization, training venue and room wise training batches can be created through the system. Accordingly, all the training letters (office wise), including forwarding letters to the HoDs, can be generated accurately without any hassle. Since the volume of polling personnel data is generally high, using PPMS system simplifies the process of training letter/forwarding letter generation etc., while ensuring accuracy.

Second Randomization
The Legislative Assembly Constituency wise random group formation process is termed as second randomization, and PPMS system has the facility to do this within a few clicks. The process is also witnessed by election observers during the second randomization.

Generation of Group Letters/ Group Training Letters
After second randomization, all the appointment letters can be generated in specified formats, and training schedule etc., can be dynamically added in the appointment letters itself, using the PPMS system.

Third Randomization
In this step, all the groups formed after second randomization are assigned polling station number randomly. This step is also required to be done in the presence of observer. The PPMS system can effectively and flawlessly-perform this function.

Counting Modules
Similarly, counting personnel for counting of votes can be drafted and appointed using the system by following all the randomization guidelines, and this has completely replaced the manual system used earlier.

Report Modules
The application has been enhanced with various types of report modules, and it enables decision-making related to Manpower Management Cell (MPMC) and Training Management Cell (TMC).

Security Features
The security related modules of the application encompass measures taken to improve the security of the application by finding and fixing all the security loopholes.

Outcome
During Parliamentary Election 2019, total 14 Parliamentary Constituencies including 126 Legislative Assembly Segments of Assam implemented the online PPMS portal for randomization of about 2,70,000 employees from various State Governments/ Central Government/ PSU organizations, and all the District Election Officers smoothly completed the randomization process in due time.
