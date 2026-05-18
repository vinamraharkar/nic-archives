---
title: "Y2K : Problems and Solutions"
publication: "Informatics"
issue_date: "July 1999"
pages: [2, 3, 4, 5, 6, 7, 8]
author: null
section: "Lead Story"
---

## Y2K : Problems and Solutions

Nature of the Problem

Legal Implications

Methodology

Computer Hardware

System Software

Applications Software

Data Communication Systems

Embedded Systems

High Level Y2K Action Force

International Scenario

Strategy for Success

National Resource Web Site

"Year 200 compliance"- a term which no computer user can afford to ignore today....What exactly is Y2K Problem...and what needs to be done ? Find out in this Lead Story which attempts to present a perspective on the much dreaded "Millenium Bug"

Historically, computer systems have been programmed with a two-digit date field to represent the year. With the arrival of the next millenium, '00' will stand for the Year 2000. The hardware and software in many computers , however, will wrongly interpret it as 1900 in place of 2000 for all calculations, comparison, sorting etc.

As a result, many systems, which compare dates to decide which is earlier, will no longer work. Systems, which calculate length of time also, may not compute accurately. There are other possible effects of the date change in computer software, depending on the assumptions made and programming techniques used by the designer of the software.

This is what is known as the Year 2000 (Y2K) problem or some times called the millennium bug.

Nature of the Problem

Immovable Deadline : The Y2K problem has an immovable deadline. All the corrective steps have to be taken before the deadline i.e. before the start of Year 2000. In some applications, which project into the future, corrective steps may have to be taken even earlier.

All Pervasiveness: As the problem is all pervasive, i.e. it affects the hardware, software, communication sub-systems and all digital systems having firmware or software (Embedded Systems), it is a big management challenge to affect all the changes concurrently.

Legal Implications

The Year 2000 crisis is a foreseeable issue (certain and material) and widely known.Thus, the failure of an organization/ corporation to develop and implement a remedial plan may be a breach of their duty and hence may have serious legal implications.

As Y2K compliance decisions and project planning is the responsibility of the management of an organization, any inaction in this regard makes the management legally responsible.

Vendors, who have supplied non-compliant system especially in recent past, also make themselves legally responsible. The extend of liability is also dependent on the contractual terms and conditions.

Methodology

To tackle the Y2K problem in an organization effectively, a five-phase methodology is followed.

Inventory

Impact Analysis & identification of Mission Critical systems

Rectification

Testing

Implementation

The first phase involves, making an inventory of all the hardware, system & application software and embedded systems. The second phase involves Y2K impact analysis and identification of critical systems for priority remediation. Plan made at the end of the second phase forms the basis of monitoring by the management. Rectification is followed by rigorous testing of the entire system before implementation.

Computer Hardware

As the system date & time is taken from the hardware by the operating system for onward transmission to applications development tools and software, the basic hardware (Real Time Clock) and firmware (BIOS) need to support the complete date & time information. RTC stores the date & time except the century part, which is stored in CMOS as 19. In most of the systems, century stored in CMOS does not change to 20 at century roll over time. However, it can be reset to 20 manually by giving a full date on Jan 1' 2000. For critical on-line applications, a Y2K utility can be installed, which can monitor the change over and set the century part in CMOS to 20 automatically. Alternatively, BIOS can be suitably upgraded to support automatic century rollover.

System Software

Operating System : Support for complete date at the operating system level is also very essential. Date & time are involved in many OS commands like Directory listing, Backup etc. Incomplete date may lead to problems in chronological ordering and manipulation of file objects. Testing of OS for Y2K compliance is not easy as many different components of OS deal with date. Just testing the system date is not enough. For compliance status, one has to depend on the information from the vendor. According to the information available on the Internet, almost all the operating systems, except those supplied in late 1998 onwards require Y2K patches or new versions to be installed for Y2K compliance.

System Software Tools like office suite etc need to support complete date formats for proper functioning beyond Year 2000. Impact of Year 2000 on such tools should be known. Information about the compliance of various tools is readily available on the Internet. Patches as well as compliant version of many software tools are also available for upgradation. Tools are available which can scan a workstation, identify all off the self products loaded in the system, and produce a Y2K compliance status report for corrective action.

Applications Software

For an Application software, the following three options are possible

Rectify : The application may have to be made compliant by suitable modifications and testing.

Replace : Redevelopment in a new platform may be a better option. So it provides an opportunity to switch over to new technologies

Retire : The application may be in the process of getting phased out & hence would not require any action.

Data Communication Systems

Network services such as E-mail, Web services, EDI, Electronic Commerce etc. pose a serious Y2K challenge. It requires all the data communication sub-systems LAN, bridges, routers, and Communication protocols to be made compliant for above services to run successfully in Year 2000. As these services involve sub-systems across organizations, any non-compliant link in between would lead to breakdown of services. Tools are available today, which can scan a data network, identify all the devices (hardware, firmware or software), their versions and produce a compliance status report, which can be used for further corrective action.

Embedded Systems

Apart from the computer hardware & software, embedded systems i.e. systems, which have microprocessor chips with associated firmware, pose a bigger challenge for achieving Year 2000 compliance. These microchips have proliferated in very large variety of equipment. According to estimates, more than 25 billion microchips are scattered all over the world in almost all kinds of objects like VCR, elevator, medical equipment, automobiles, traffic lights, Automatic teller machines, airplanes, satellites, telecommunication systems, control systems of power & chemical plants etc. It is estimated that at least a small percentage (5-10%) of such devices will be affected by Year 2000 problem. If suitable corrective steps are not taken, malfunctioning of these devices can have serious impact on the functioning of the organizations as well as the entire society.

It has been realized the world over that fixing embedded systems is a much bigger challenge compared to fixing software and hardware systems. The organization is highly dependent on the vendor for identification of the problem (as one cannot change the date externally for testing) as well as for fixing the problem. Moreover, vendors of some of the control systems acquired a long time ago, may not be in business any more. Vendors themselves are dependent on other vendors for supply of sub-systems. Therefore, the vendor who has supplied the end equipment may not be capable of resolving all the problems. In case the problem cannot be resolved, the sub system may have to be replaced, thus increasing the cost of Y2K remediation substantially.

High Level Y2K Action Force

Recognizing the significance of Year 2000 problem, a High Level Action Force on Managing the Impact of Year 2000 Problem in India has been constituted under the chairmanship of member (Planning Commission). The Terms of Reference of the Action Force are as follows:

To identify critical sectors in the country which are required to be monitored for handling the Year 2000 Problem in the country.

To get Sector-specific action plan prepared by the respective organization/ agencies for remedial work related to the Year 2000 Problem.

Periodically monitor the implementation of the Action Plans

To make plans for Awareness building among the affected categories of organizations, the Parliament, the Press and the Public.

To take necessary steps for the establishment of a corpus fund of Rs.700 crores to address the Year 2000 Problem in India.

To evolve a mechanism for providing financial support, out of the Corpus fund, to various government organizations/ PSUs/ Companies and other affected organizations/ activities in handling the impact of Year 2000 Problem on the computer based activities and services offered by them.

To keep contingent action plans for various sectors in readiness to meet possible post 1999 outbreak situations.

The Following Utility and service sectors, which are critical from Y2K perspective in India, are listed below.

Finance - Banking & Insurance

Power

Petroleum and Natural Gas

Telecom

Surface Transport

Railways

Civil Aviation

Space Research

Atomic Energy

Defence

International Scenario

World bodies like World Bank etc. have taken initiatives to organize Y2K awareness workshops across the globe and made grants and funds available for Y2K activities.

United Nations General Assembly passed a resolution on Y2K issue and organized a special Workshop of National Y2K coordinators in December'98 to communicate the importance and urgency of the Y2K problem. Experience sharing, International cooperation and Contingency planning to deal with this gigantic man made problem, unparalleled in the history of man kind, have been emphasized.

Strategy for Success

For the organization to succeed in its Y2K compliance, the following elements would play a critical role :

Methodology : The 5-step methodology described in the previous section is very critical to the success of Y2K remidiation effort.

Y2K Coordinator : One senior person of the management should be made responsible for the Y2K compliance process in the organization.

Effective Monitoring : As the Y2K deadline cannot be moved, a strict monitoring by the management is very crucial.

Technology updates using Internet : Keeping uptodate on the Y2K technology front is very important. And for this, there is no better tool than the Internet Compliance information on hardware, system software, Y2K tools; consultancy, downloadable patches etc. are readily available on the Internet.

Vendor Management : Vendor plays an important role in the Y2K compliance process. Vendor is responsible for proliferating the non-compliant systems in the first place. By his effort, he can resolve the problem once and make it available to so many of his customers. This is especially true for hardware, system software and embedded systems.

Experience sharing : Sharing experience and problems with other organisations in the same sector, can help in expediting the process as well as invoking better vendor cooperation and solution negotiations.

Contingency Planning : An organization faces Y2K risk from possible failure of Y2K compliance systems, non- compliant systems, external interfacing agencies for inputs and national infrastructure like power, telecom etc. A contingency plan needs to be made to address any of the above failures, so that functions critical to the survival of the organization can continue.

Y2K Compliance Audit : It is not enough that systems are reported as compliant. An external audit team should make anindependent assessment of Y2K remidiation effort. Any shortcoming discovered during the audit should be brought to the notice of the management for corrective action.

National Resource Web Site

A National Y2K resource Web site has been created with URL

www.nic.in/y2kactionforce

It is planned to enrich the above Year 2000 Action Force Web site on a continuous basis so that all relevant aspects of Y2K are covered with highly focussed references which are of direct use to the end users of this information. As searching the Internet directly for the required information is like searching a needle in a haystack, directly relevant information linked on this site will help the organizations spread throughout the country to make a head start.

For further assistance and information, please contact :

Y2K Action Force Secretariat
National Informatics Centre
A-Block, CGO Complex,
Lodhi Road

New Delhi - 110003
