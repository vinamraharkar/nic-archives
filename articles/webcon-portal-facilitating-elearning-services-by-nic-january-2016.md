---
title: "WebCon Portal - Facilitating eLearning Services by NIC"
publication: "Informatics"
issue_date: "January 2016"
pages: [36, 37, 38]
author: "Varindra Seth, T.K. Jain, WebCon Team"
section: "TECHNOLOGY UPDATE"
---

## WebCon Portal - Facilitating eLearning Services by NIC

WebCon Portal of NIC facilitates online learning and web conferences services through open source software in the NIC cloud environment. The portal facilitates users for real time sharing of audio, video, slides, chat and presenter’s desktop. These services are provided under the umbrella of Web Learning Services for training, project implementation rollouts, iClass, iMeetings etc.

e-Learning services by NIC Telematics Division was launched in the year 2006 using AT&T Connect application (formerly known as Interwise) a proprietary software. It was used to provide e-Learning services such as trainings, project implementation rollouts, iClass, and iMeetings.

These services are now provided through WebCon using customised open source software and hosted at NIC’s Cloud environment. WebCon has a capacity to cater over 500 concurrent connections for each session with all features of AT&T Connect Application. These services are being provided under the Web Learning Services umbrella.

WEBCON PORTAL
WebCon Portal, based on the Open e-Gov Policy of DeitY, is an open source initiative to provide online learning and web conferencing services. This portal facilitates WebCon for real time sharing of audio, video, slides, chat and presenter’s desktop. The software used for WebCon does not limit the number of concurrent users, if the bandwidth is large.

Users can access the portal through web browsers to chat, send and receive audio and/or video to have quality online learning experience. The Session moderator can manage sessions with controls such as mute/unmute, block/unblock and upgrade/downgrade the participants. Changing the status of a current viewer to presenter or vice-versa is an example of controlling a participant by session moderator.

TECHNOLOGY FEATURES
WebCon use the Web Real Time Communications (WebRTC), audio sampled at 48KHz and encoded through Opus Codec, which is open source and royalty free. This communicates via UDP through an internal FreeSwitch and provides very high quality yet low latency audio with lower delay. Web browsers such as Chrome and Firefox use WebRTC. WebCon has the ‘Audio Check’ to ensure that all users have operational microphones during a session. This can be checked even before one joins the session. It also provides a ‘Listen Only’ mode for the users with no microphone, which converts the session that is similar to a webinar. The recording interface has control buttons for moderators to mark portions of recorded sessions to be saved for publishing. Once a session is over, WebCon server extracts marked segments for publishing.

WebCon runs on an open source platform comprising of Ubuntu 14.04 64 bit version with Tomcat 7, Java 1.7 and a suite of related open sopurce software.

HIGH LEVEL ARCHITECTURE
The client for WebCon is a ‘Flash’ application, which runs on a web browser that communicates to Red5 on the WebCon server through Real Time Messaging Protocol (RTMP) or Real Time Messaging Protocol Tunnelling (RTMPT) protocols in intranets. This also runs on restricted/under firewall networks where only port 80 is open. For restricted networks, WebCon uses Nginx for proxy connections to Red5. For voice conferencing clients, it uses WebRTC to communicate with FreeSwitch. With the use of Nginx, it also communicates with Tomcat for the WebAPI for third party applications like WordPress for managing WebCon.

WebCon is the main application, which in collaboration with a suite of software provides real-time e-Learning or meeting experience. It lists the users, chat, presentations and whiteboard in a meeting. Some of the relevant components used to communicate with the external world are Red5 Client Message Sender/Receiver, which communicates with Flash client on a web browser and publishing messages and events to Redis Database. VoiceService components use Free Switch for communication in voice conferencing. For recorded meetings, it uses the Redis Database through recording service and internally the recording processor for all recorded events including raw files like pdf, wav, flv etc. for processing. Libre-Office manages all uploaded content, converting them into either SWF or PDF using SWF tools. When a PDF page fails to be converted to SWF, an image snapshot of the page is taken using ImageMagick and GostScript, and then converted to PDF and SWF. Different server side components are coordinated and managed by the Redis PubSub. Managing of users, chats, whiteboard, presentation etc. are handled by the Red5Apps. DeskShare allows presenters to share their desktops, while the voice application allows users to call into voice conference either as active participants or as just listeners. Video app allows sharing of participants’ webcams during meetings.

WEBCON EVENTS OVERVIEW
• i-Class, 1049 sessions with 12,596 participants
• i-Meetings, 1142 sessions with 10,133 participants
• i-Seminar, 17 sessions with 1844 participants

IMPORTANT EVENTS UPDATE
Regular events
1. Consortium for Educational Communication (CEC) online orientation and training on a regular basis on MOOC’s for subject experts and technical staff located across 17 media locations pan India.
2. Training on Central Public Procurement portal on regular basis on all working days.
3. Computer networking of Consumer Forum (CONFONET) to 500 locations pan India
4. Soil Health Card Software demo for Department of Agriculture, GoI
5. National Animal Diseases Reporting System (NADRS)
6. Integrated Disease Surveillance Programme (IDSP) on regular basis for 800 locations
7. School Programme to blocks of Giridih District of Jharkhand

One-time events
1. Digital India Week web learning to impart training to 600 DIOs of NIC
2. Training for AEBAS and Aadhaar for Giridih district Jharkhand
3. Socio-Economic Caste Census 2011 training
4. Staff Selection Commission (SSC) Chairman’s meeting with all 16 regional heads for CGL exam
5. e-Learning sessions on various technology topics like .Net, Java, Linux etc. for NIC across the country
6. Webinar on User Awareness Programme for NIC S&T professionals
7. Electronic Performance Appraisal Report (e-PAR) training
8. Hindi Karyashala
9. GIGW (Guidelines for Indian Government Websites)
10. Awareness programmes on e-Resources
11. Source code review of application using Static Code Analyser
12. Webinar on Dial.Gov
13. Network technologies & management

HIGHLIGHTS
• WebCon eLearning software is hosted at ‘MeghRaj’ Cloud, which ensures safe and uninterrupted services
• To enhance the eLearning services further, Telematics Division is currently in the process of integration of it with open source LMS
• Being open source software, there is no development and maintenance cost implications. This benefits Government by saving time and money
