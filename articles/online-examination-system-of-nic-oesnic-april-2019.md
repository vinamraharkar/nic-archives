---
title: "Online Examination System of NIC (OESNIC)"
publication: "Informatics"
issue_date: "April 2019"
pages: [31, 32]
author: "REUBAN K (Editor), K. JAYABALAN (Sr. Technical Director), K.K. SIVA PRASATH (Scientist ‘D’)"
section: "E-GOV PRODUCTS & SERVICES"
---

## Online Examination System of NIC (OESNIC)

Boasting of a robust architecture enabling the simultaneous operation of multiple exams

OESNIC has replaced the existing examinations, conducted using paper, with online paperless system in government departments and schools, thereby ensuring 100% transparency in conducting examinations and mark sheet evaluation. Till date, more than 60 examinations have been conducted for NIC and the Government of Tamil Nadu. Around 3000 NIC officials have taken the exams.

Owing to a stable career and various other benefits, many students enrol for government exams after graduation. A well-strategised process, right from planning to execution to completion, is followed by the respective authorities to conduct these examinations. To ease their effort and bring transparency to the system, the Online Examination System of NIC (OESNIC) has been designed and developed as a product for conducting various Recruitment and Departmental Promotion Examinations for the State Government and Central Government Departments. The system supports multiple choice questions and the application is designed using Thick Client-Thin Server Architecture where the server load is reduced to the maximum extent.

The entire process of examinations is conducted in a safe and secure environment with questions and answers stored only in encrypted form. The encrypted and compressed question booklet gets downloaded to the client machine using the secure channel. The Application Architecture ensures minimum usage of server and also handles a large number of concurrent users. The GudApps Test of NIC is being conducted using this application. The Bilingual Data Entry Speed Test for English and Tamil has been introduced and can also be used for other Indian languages.

Highlights
••54 Tests were conducted for 2990 NIC employees.
••Knowledge of all the new entrants to NIC was also evaluated using the above software.
••A one-day test was conducted for 11,000 candidates in 4 batches from 85 engineering colleges across Tamil Nadu, using this application.
••The application is tested to withstand the load of 10,000 concurrent users.
••The application is developed using Open Source Technologies.

Technologies used
••LAPP (Linux-Apache-PHP-PostgreSQL Database)
••HTML5, CSS3, Javascript, Bootstrap Libraries, RESTful Web services

Features
The system facilitates the following features and these are configurable across examinations.
••Conducting different tests among multiple batches simultaneously for more than one department
••Random generation of Question Booklets
••Reshuffling of Question Booklet Serial Number within a batch
••Assigning Reshuffled Question Booklet to candidates using randomisation method
••Disabling all special keys in keyboards during exams to restrict candidates from using other modes of search operations
••Continuing with tests from the time of interruption in case of local hardware or network issues and completing within the left out time frame
••Assigning weightage of marks to each question based on the difficulty level
••Giving negative marks for wrong answers, if required

Application Architecture
The application works in the following manner.
••Questions and answers are stored in the database in an encrypted form.
••A booklet with N number of questions is generated through randomisation as JSON (JavaScript Object Notation) file for each batch and stored as an encrypted JSON file with SALT (a random generated number).
••A booklet generated for a batch is reshuffled to generate M number of question booklets by randomising the N number of questions selected for a batch. This activity changes the order of appearance of questions. Now, there are M numbers of reshuffled question booklets from a booklet generated for the batch.
••The next activity is to generate booklet for each candidate appearing in a particular batch. To do this, these M booklets (JSON file) were randomly selected and the JSON file name is assigned to each candidate. This process ensures the same booklet with same serial number does not appear for the consecutive candidates sitting next to each other in the examination hall.
••The M number of booklets (JSON) are kept in compressed and encrypted form in a separate folder, linked with batch number to increase the search speed during download of question booklet by candidates.
••Since the generation of booklets as JSON file is done before the exams begin, the database operation for generation of questions for each candidate from the database is completely avoided.
••A demo question booklet with 10 questions as JSON file is kept in the server for practice test before the actual online exam. When a candidate clicks “DEMO TEST”, the demo JSON file gets downloaded to the client. Since the navigation of questions is done from JSON file at the client end, there is no client and server communication for any updation till the candidate completes the DEMO TEST.
••When a candidate selects “ONLINE TEST”, the encrypted and compressed JSON file kept in a folder gets downloaded to client and JSON object is parsed to display question and choices on screen. Since the questions are attached to button number, when a candidate clicks on a particular number in the question pallet, the corresponding question is parsed from the JSON file in the client machine and displayed on screen. The network bandwidth usage is avoided for displaying the candidate’s desired question on screen from the database each time when the candidate clicks a button for a particular question. This architecture helps in scaling up the application and results in improved performance of online examination.
••When a candidate answers the question and clicks on “SAVE NEXT” button then only a web service is called through CURL (a tool to transfer data from or to a server) and gets updated in the Answer Table just by sending REGISTRATION No., QUESTION ID and ANSWER KEY. Based on the confirmation from the server about updation, the answer key of the candidate gets updated in JSON Object in the client and hence, client will always be in sync with the server.
••If anything goes wrong at client side (system hangs, power issues etc.), the candidate doesn’t need to worry. When the candidate logs in again from the same client or from any other client, a new encrypted and compressed JSON file gets generated from the database with whatever questions the candidate has answered, and is downloaded to client. An old screen with answered questions (GREEN BUTTONS) is displayed and the candidate can CONTINUE THE TEST. The system will calculate the time of their last answer and the balance time to be given to them. Thus, there will not be any loss of time to the candidate even in the case of any unexpected interruptions.
••In this architecture, the navigation between questions by the candidate is done only at the client end. Only when the candidate answers a question, a client server communication is initiated for updating the answer key of the candidate in the table. Due to this, the server and database load is very minimal.

Way Forward
It is planned to introduce OESNIC in other State/ Central Government Departments for conducting online exams for internal promotions and also to recruit data entry operators for using speed test feature available in all the Indian languages. Further, it is also envisaged to take this product to high/ higher secondary schools for students to take multiple choice questions tests in various subjects.
