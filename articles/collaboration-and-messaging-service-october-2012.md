---
title: "COLLABORATION AND MESSAGING SERVICE"
publication: "Informatics"
issue_date: "October 2012"
pages: [12, 13]
author: "YERUR SIRAJ AHMED"
section: "E-Gov Products & Services"
---

## COLLABORATION AND MESSAGING SERVICE

eOffice-CAMS is focused on providing effective communication between departmental applications through collaboration and the obvious solution is to have Collaborative service. The idea is to facilitate action oriented team to work together over a geographical distance and let internal users, systems and departments to communicate. Collaboration (act of working jointly) is the only way to make users, systems and departments to communicate effectively.
INTRODUCTION
Communication is an important facet of life. Effective communication centers around the usage of words, speed of delivery of words, media used, place and time of communication. Users need to be updated about transactions or modification from the departmental applications. By providing application update to the users, interest to use the application is generated. The issue is to facilitate action oriented team to work together over a geographical distance and let internal users, systems and departments to communicate. The obvious solution to the issue is to have a collaborative service. Collaboration (act of working jointly) is the only way to make users, systems and departments to communicate effectively and the service to work jointly is called Collaborative Services. The article describes how the eOffice- CAMS will help in collaborating (for communicating and be updated about the applications).
BACKGROUND
There are various definitions for Collaboration with respect to Information technology. There are three primary ways in which human interact: Conversational interaction, Transactional interaction and Collaborative interaction.
Conversational interaction just exchanges information between two participants, where the primary purpose of the interaction is discovery or relationship building like Instant Messaging Service (IMS), email etc. Transactional interaction, involves the exchange of transaction entities where a major function of the transaction entity is to alter the relationship between participants. For example, the user inviting other users to attend a meeting place a role of organizer and the users who attend are called as participants. Collaborative interaction is to alter a collaboration entity (i.e. converse of transactional entity) like document management, threaded discussions etc.
TECHNOLOGY SOLUTIONS AND ARCHITECTURE
The question that arises about HOW, WHAT, WHEN, WHOM and WHERE to collaborate. The obvious answer is using text or media, anything, anytime and anywhere. But WHERE to start collaboration still exists. The most obvious answer was the WEB and we started with Intranet (eOffice). Answering WHOM to collaborate was difficult, as it would be unfair if it is restricted to a specific person or users of a department. There is no restriction with respect to collaborating users and for users of a department. Then comes the WHAT question which needed a little bit of understanding. Consider looking at the meaning of collaboration from a different point of view. Instead of having users work jointly, it’s the modules that will help users to collaborate upon identical operation. Few of the services have been identified which are being used by different modules of Intranet like sharing, alerts, notifying users, updating with new features etc. The identified services answers the WHAT question. The approach was to have application(s) over the existing intranet applications. Two applications namely eTalk and eAlerts were identified. Basic version of eTalk includes Chat and eAlerts notifies users about any changes on documents / appointments / events / files from already existing modules (i.e. KMS, appointments etc.) from eOffice.
The functionality of eTalk and eAlerts actually answers HOW. The application is developed independent of all the intranet applications. In order to have chatting facility anywhere, the design of eTalk was developed in such a way that it was independent of all other applications. For which purpose all the end points (frontend, backend and information exchange) from where these features are accessible are made independent. eTalk was developed as an independent module with basic functionality of Chatting (simple text messages). A JavaScript API (Application Programming Interface) was developed and made openly available to be used by all the intranet applications. Currently eTalk can be seen accessible from all the pages of intranet (“Active Users” at bottom right corner of every page).
HOW IT WORKS?
All the most common functionalities (i.e. Chatting, Send IM, Add Contact, eTalk status, Availability etc) were identified and made as a page (front end HTML) in eTalk. In order to have these accessible from all applications, an API is written which is made openly accessible to be used by all other applications. Sample template along with JavaScript code was provided to all the modules to be included in their applications. The JavaScript code handled all the functionality from the frontend.
In order to have all these features to be called from frontend, the features were inherited in the backend (on the server) and were being called from frontend.
ADVANTAGES
l Active participation of Users - facilitates the users to actively participate to use these resources.
l One stop access point to all disintegrated application and services
l Direct manipulation - users can work & update their contact details from anywhere
l Ease of use - intuitive design and easy to use web interface
l Interoperability - combining of different applications and their data as one instance.
l Flexibility - The application is flexible in nature as new features can be inherited and called upon.
l Reusability of the alert mechanism by other department applications.
IS THAT ALL, THAT CAN BE COLLABORATED?
The obvious answer is NO. So far we have collaborated eOffice applications and its services. If these services are extended to other services of departments., like eGranthalaya will notify users about list of new books that are being taken or remind specific users about the last date of the books issued (through alerts). Similarly Accounts Division can send alerts to users about their payments or tour bill clearances.
SCOPE
This section defines the scope of these applications. Use of these applications is not limited to either e- Office or other departments. Due to the independent nature of the application it can also be inherited or called using the API from other ministries which have e-Office and the divisions of these ministries.
CONCLUSION
Continuous integration of new features from eOffice applications is still going on. Updating API functions and development of new API functions are being developed to be used by eOffice applications and other department applications. This topic is not just restricted to collaborating users, but rather the data and the documents, which can be called as MASHUP (is a web page or application that combines data, functionality from two or more source to create a new service). Happy Collaborating!!!
