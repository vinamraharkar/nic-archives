---
title: "Open Elecon: Managing Elections Meticulously in Jharkhand"
publication: "Informatics"
issue_date: "July 2009"
pages: [12, 13]
author: null
section: "E-Gov Products & Services"
---

## Open Elecon: Managing Elections Meticulously in Jharkhand

The general elections in India, the world's largest democracy, were recently held to elect its 15th Lok Sabha. Elections are conducted according to the constitutional provisions, supplemented by laws made by Parliament. The major laws are Representation of the People Act, 1950, which mainly deals with the preparation and revision of electoral rolls, the Representation of the People Act, 1951, which deals, in detail, with all aspects of conduct of elections and post election disputes.

Elections in India are an exercise involving political mobilisation, people participation and organisational complexity on mammoth scale and are said to be the largest event in the world.

To manage the event involving enormous complexity, a computer based system - “Open Elecon” was developed by NIC, Jharkhand using open source platform for conducting the parliamentary / assembly elections conforming to the guidelines of the Election Commission of India.

Software for managing elections (like Elecon etc.) has been used by various NIC centres all over the country earlier. But “Open Elecon”, true to its name, is reengineered software on open source technology, developed and implemented in a time bound manner during the recently concluded 2009 Lok Sabha elections.

Expert of the letter from Joint Chief Electoral Officer-cum-Joint Secretary Sh. Ashok Kumar Sinha, Dhurwa, Ranchi, Govt. of Jharkhand Cabinet (Election) Department.
This is to Certify that the “OPEN ELECON Software version 4.0” developed by NIC Jharkhand State Centre, Ranchi for supporting the Election process, confirms to the prescribed Guidelines of the ECI.
The software is approved for using in the Lok Sabha Election-2009

The web based system uses Apache Tomcat as Application Server, J2EE as development platform with MySql database. The software was installed at the central server, which was accessible from all the districts of the state. Districts were also given the option to implement the system on their local server at district NIC centres. The system required one time initialization with district name, names of parliamentary constituency with assembly segments, block names, etc.

Flow of the System - The overall flow of the system is as follows.

Users & Role

The system operates with four types of users having various roles for the smooth operation.

Administrator: is the super user having all the privileges to operate the software. User having Admin Role can enter, edit and delete any data or record as well as perform polling personnel randomization, EVM randomization, Polling Officer Replacement and Reports etc. Administrator has the privilege of creating all the master files.

Observer: Users having Observer Role can perform 2nd and 3rd polling personnel randomization, magistrate's randomization and party formation.

Election Officer: Election Officer Role is allowed to only view the results after counting. This role is used for media display.

Operator: Users having Operator Role are allowed to do all the data entry tasks, except some of the data that must be entered by the User having Admin Role.

The users of the system need to login using their own username and password. The password is authenticated using Salted Hash MD5, in order to make it hack proof.

On being logged in, the user finds an informative and attractive Dashboard, which gives graphical and tabular information to monitor the whole system as follows-

— Officers - gives the detailed information of officers posting block wise, officers assembly constituency wise and their duty wise in tabular as well as in a bar-chart.
— Booths - gives a tabular as well as bar-chart information of the nos. of voters assembly wise and gender wise, and the tabular and pie-chart information about the nos. of booths based on their sensitivity assembly wise.
— EVMs - gives separate information regarding the nos. of Control Units and Ballot Units allocated to each assembly constituency and how many are reserved. This is also shown graphically in bar-chart.
— Vehicles - gives information about the nos. of vehicles on election duty with their type in tabular form as well as graphically in pie-chart.

Dash Board

Modules of the system

Data Entry involved master entry of Departments, Offices, Officers, Booths, Electronic Voting Machines (EVM), Vehicle details etc.

Data Processing involves application of business rules as per the ECI guidelines and comprises the core of the Open Elecon system. It can be categorized as follows -

— Deployment of Polling Personnel - allocation of assembly segment to officers (1st polling randomization) based upon the predefined criteria. Party formation (2nd polling randomization) involving officers selected through the above process.
— Booth Tagging - allocation of booth to parties formed above (3rd polling randomization).
— Deployment of Micro Observers / Magistrates to Booths - the system facilitates deployment of micro observers and magistrates to various polling booths.
— EVM Randomization & Booth Tagging - assembly wise allocation of EVM's (1st EVM randomization) and thereafter tagging of EVM's to booth (2nd EVM randomization).
— Processing Parameters: Before processing for the deployment of personnel or EVMs , the system required the following parameters Place and date of training, Name & designation of returning officer, Material Collection centre with date & time, Material returning centre , No. of booths for lady officers, Percentage of reserve personnel, Percentage of reserve EVMs , No. of micro observers & magistrates, Additional Polling personnel for the booths where number of voters are exceeding a predefined figure.

Reports & Letters - The system has provisions for generating training duty and appointment letters / Tamila for Officers and Magistrates, identity cards for Polling Officers and Magistrates, list of booth-party-tagged, list of booth-EVM-tagged, list of Magistrate-booth-tagged, Reserve party list etc.

Counting - The last phase of the polling process was supported by the system which provided round wise compilation of votes polled for all the candidates at an EVM / booth for an assembly segment. The compiled result for all the assembly segment of parliamentary constituency was displayed instantly to the media from the server.

Salient features of the System : Generation of PIN for officers whose details are entered into the system, Reports generations like Training Duty letters, Individual duty letters, Appointment letters, Replacement list, Booth & Party Tagged List, Party Reserved List, Booth BU & CU tagged / Reserved list, Office wise Poll duty list, Presiding officers list etc, Master information entry like Blocks, Departments, Pay scale, Officers allowance, Duties etc apart from User management, Locking of executed randomization process at every stage, Selection of micro observers / magistrates and their booth tagging through randomization etc
