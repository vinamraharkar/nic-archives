---
title: "PBOX Proctoring Based Online Examination System"
publication: "Informatics"
issue_date: "January 2022"
pages: [8, 9, 10]
author: "Edited by DR. DIBAKAR RAY"
section: "eGov Products & Services"
---

## PBOX Proctoring Based Online Examination System

Online examination system is the necessity of the current time but very few of the online examination systems allow examination to be conducted over a disturbed network along with online proctoring. With this inspiration NIC has developed PBOX which is a proctoring based system providing functionalities more focused towards network resiliency and security which are the two prime and critical aspects of an examination in the context of India. This system is powered by many prominent technology stacks like Big Data, Progressive Web App, Service worker, AI/ML and containerized platform which enable it to provide functionalities in a very unique way.

PBOX provides the ability to conduct exam in a much scalable, secured and network resilient way with additional provisions to be deployed in on-campus mode. It provides a mechanism to do auto proctoring powered by AI / ML on the edge device itself without sending each frame to the server. It allows the candidate to continue exams in disturbed network environment by buffering the answers during the offline period along with many other innovations.

Modes of implementation
Online mode
All candidates will appear for the examination remotely and central server will handle all the requests.

On-campus Mode
The candidates will appear the examination from the centres in an intranet environment, where the local server at the center will fetch the encrypted questions from the central server.

Features
Examination configuration
Each examination can be configured separately at a very granular level like examination specific instructions, slots and their timings, need of proctoring service or not, need of Face Authentication or not, various system generated messages, deployment related configuration like use of message broker is required or not etc.

Question & candidate Data Upload
The exam conducting body can upload candidates and questions against each section through excel sheet or by direct data entry through GUI or can be fetched from using API from a third party system.

Randomization of Question
The exam conducting body can generate randomized question set which then gets pushed to a different server from which the exam starts to keep the sanctity of the central question bank.

Proctor Dashboard
The exam conducting body can create proctor user and map candidates to the proctor whereas the proctor can monitor system identified violations. Proctor will have the facility to pause or terminate the exam of a specific candidate. He may also initiate a chat with a specific candidate which will be recorded for auditing purpose.

Question panel
Color coded and multi shape panel to show all question numbers clicking on which system will navigate to the specific question.

Network Resilient
Exam can be continued even if network fails in between. PBOX manages the traffic in intelligent way through Smart Bandwidth Management, so that the service continuity does not get disturbed.

Artificial Intelligence
Face Recognition for identification and Remote Proctoring with following features i.e. Multi-persons Detection, Absence Detection, Eye Ball tracking and Whispering Detection.

Subjective / Objective Question
The system facilitates of different types of questions like MCQ, MRQ, true/ false, subjective, case study, grouped comprehension. Questions and options can have image attachments too.

Answering Mode
Has provisions for descriptive answer, single choice and multi choice answer.

Reset & Review
Has provision to reset the already given answer and mark question for review which can be answered/confirmed at the later stage.

Automate Result
Test result processing of MCQ & MRQ type questions can be automated.

SmartLock App
Protects the environment by screen locking before starting the exam and blocking applications like Team Viewer, Anydesk, YouCam, ManyCam etc. to avoid any malicious activities and inform such activities with the web portal. This will run outside the scope of the browser but in handshaking mode with the web application. If the candidate tries to kill this application then PBOX web portal will stop working.

API Integration
Open API has been provided for integration with third party peripheral modules so that clients can do data transformation as per their own requirement and reporting

PBOX, is a proctoring based online examination system providing functionalities more focused towards network resiliency and security, which are the two prime and critical aspects of an examination in the context of India and is need of the hour during the Covid-19 pandemic. The product has been developed by NIC, Odisha with a focus to conduct online and on-campus examination with /without proctoring with the use of AI / ML for face recognition and proctoring activities.
KABITA ROY DAS Dy. Director General & SIO National Informatics Center, Odisha

Technologies Used
• OS: Linux
• Frontend: Angular, Javascript, Bootstrap, HTML5, Python
• Backend: Node.js
• Web Framework: Express.js
• Load Balancer: Ngnix
• Persistent Database: MongoDB
• In-Memory Database: Redis
• Message Broker: Kafka, Zoo keeper
• AI and ML: Deepface, Python, Flask, Face API, Tensorflow
• Cloud Platform: Openstack
• Orchestration Platform: Kubernetes, Rancher
• Containerization: Docker

Innovations Applied
• In addition to regular common functionalities related to conducting examination in either online or on-campus mode there are many innovations which have been included to make this product unique and contextual in Indian environment
• We have created one buffer zone on the client side to keep the attempted answers in the event of network failure and syncs to the server automatically sensing the network availability
• To reduce the latency there is no update or delete command executed with the request and response cycle while running in high performance mode. Update or delete operation are handled separately without blocking the I/O operation
• Exam module of the project is disassociated from the central question bank database neither for read nor for write. This module interacted with question bank database server through intermediate servers like Redis & Apache-Kafka reducing the cyber attack surface on the question bank
• Use of in-house developed bandwidth management algorithm to send data packets to server reducing the overall network congestion and allowing the candidate to operate with less bandwidth as well
• In house security algorithm implemented to protect client side database in the context of On-Campus examination in the event of both database admin and OS admin password are leaked
• AI/ML based image processing is done at the client side taking frames from the web camera and only the frames having suspicious activities will be reported to server

Way Forward
In the context of India, multi stakeholder’s involvement in conducting examinations is a common practice where exam is conducted by one agency and taking technical support from another agency, so integrity is the legal aspect which is very crucial in designing these types of systems.

So Blockchain has been put in design blueprint to keep a distributed ledger with every stakeholder to have more transparent and battle ready security system in coming phase of rollout. Whispering and different types of object detection will also be available in coming days to enhance the proctoring based offerings.

Contact for more details
State Informatics Officer NIC Odisha State Centre, Unit-IV, Sachivalay Marg Bhubaneswar, Odisha - 751 001 Email: sio-ori@nic.in, Phone: 0674-2508438
