---
title: "IVRS@NIC: Kailash Mansarovar Yatra (KMY) 2015"
publication: "Informatics"
issue_date: "July 2015"
pages: [31, 32]
author: "Varindra Seth, John Philip, Nidhi Lohat"
section: "TECHNOLOGY UPDATE"
---

## IVRS@NIC: Kailash Mansarovar Yatra (KMY) 2015

NIC TDPP division’s IVRS has been an integral part of the telephony revolution that the country has witnessed since the last decade. Right from the challenging period of analog cards and C++ codes interacting with card API for creating a call flow in the late 90s, the IVRS evolved to GUI Call-flow Management. These phases made NIC-IVRS pioneer in the government by rolling out the CBSE Results over telephone for the first time, and later projects like Court-NIC, passport projects to AG offices for Haryana, Nagpur, etc.

Even though India now has one of the highest telephone densities in the world, smart phone penetration stands at 15-18%, that too in urban and semi urban areas. Hence, NIC IVRS with the latest Voice and Speech technology stands high potential to reach the grass root levels of the country.

NIC IVRS runs on the Nuance Voice Platform Version 5.2.2 with 6 PRI lines (180 voice channels) and capacity to add another 4 PRI lines which run on Windows 2008R2 server virtualised on a standard 32GB 4 Processor (8 core) sever. PRI lines terminated on router with voice cards provide PSTN connectivity. It has also been integrated with SIP EPBX for connectivity to and from any IP phones across the NICNET and has been utilised for running call centres and help desks.

FACILITIES AVAILABLE
yyAutomatic Speech Recognition (ASR) in 14 Indian languages including Indian accent English
yyText-to Speech (TTS) in Hindi and Indian accent English for reading out free text
yyCaters concurrent inbound calls on IP or on PSTN with 100 MSN, i.e., 100 applications can be serviced simultaneously
yyOutbound calls using outbound dialler (OBD)
yyIntegration with SIP based EPBX where IP phones placed on NICNET or extended NICNET
yyApplications developed are in W3C compliant Voice XML (VXML) 2.1 with Speech Recognition Grammar Specification (SRGS) grammar for voice as well as DTMF (key press/ Touch tone), which are open standards compliant
yyReal-time monitoring with alerts and a comprehensive dashboard for calls and status of appliances and servers
yyIntegration with a variety of SIP based media gateways
yyCustomised call reports

TECHNOLOGY
Users can now speak and select options, instead of DTMF, in VXML applications using ASR. It can speak out Indian languages using TTS engine. Applications, either as plain or code generated VXML, using any language like ASP.Net, PHP, JSP, etc., can access various backend data servers. Functionality can be enhanced using inline or offline ECMA Script, a version of Java Script.

Calls can now be transferred between the SIP EPBX and IVRS, like dialling 8971 on IP phone is routed to the IVRS, giving the possibility of running call centre application. With this infrastructure, IVR can forward calls to agent and agents can pass calls back to IVR.

CASE STUDY: KAILASH MANSAROVER YATRA (KMY) 2015 (IVR NO: 011-24300655)
Introduction
KMY is an annual event conducted by the Ministry of External Affairs (MEA) GoI for pilgrims visiting Mt. Kailash. A new website along with the IVRS was launched by the Hon’ble Minister for External Affairs Smt. Sushma Swaraj on 19th February 2015 for facilitating the pilgrims, who do not have access to internet or smartphones.

Requirements to be met by IVR
yyCategorised information in six groups (Routes, Eligibility, Selection Process, Fee and expenses, How to Apply and Application Status)
yyTalk to Help Desk on working days from 9:30AM to 5:30 PM
yyRegisters call back to the caller, when help desk is not available
yyDaily call back request report to MEA for the Helpdesk Assistant to make calls back
yyStatus Request :- Initially provides application submission details; after lucky draw, batch details for selected or waiting list with batch details for non-selected applicants

Implementation
The application was built with ASR for Hindi and Indian accent English. All the prompts, what the caller hears for input, were played out using TTS in Hindi/Indian accent English. Menu available for selection, by voice or DTMF has the following:

1. Application Status
2. Eligibility
3. Selection Process
4. Fee & Expense Details
5. How to Apply
6. Yatra Routes

In the above options menu, “Eligibility”, “How to Apply” and “Application Status” options are implemented as separate VXML pages. Fee & Expenses and Selection Process details are played out directly within the menu itself. VXML Tags used are Form, Block, Field, Prompt, Prosody, Grammar, Filled, IF Else, Go to, Subdialog, Transfer, Data and Submit.

For other menu options
yyApplication Status: Takes phone number and Date of Birth of the applicant, connects to the backend Oracle database in NDC Shastri Park using the Data tag and a data fetch implemented in .Net page handler.
yyHow to Apply: Options to hear details of applying as a normal yatri or as a Liaison Officer
yyYatra Routes: Option to hear details for routes via Nathu La and Lipu lekh

The transfer to helpdesk and call back functionality in Eligibility, How to Apply & Yatra Routes are implemented using Subdialog tag. The calls are transferred by Transfer tag using the SIP based EPBX to an IP phone at MEA, South Block.

Global options, “Previous Menu”, “Exit” and “Repeat” (at appropriate places) to hear the details again, are all implemented as Subdialogs. Calls made to the KMY are logged while monthly detailed reports are mailed to all the concerned.

For further information:
TDPP DIVISION
National Informatics Centre,
CGO Complex, New Delhi – 110003
Email: India.ivrs-support@nic.in
Ph: +91-11-24305240
