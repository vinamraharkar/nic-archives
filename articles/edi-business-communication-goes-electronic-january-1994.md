---
title: "EDI : Business Communication goes Electronic"
publication: "Informatics"
issue_date: "January 1994"
pages: [1, 4, 5]
author: null
section: "COVER STORY"
---

## EDI : Business Communication goes Electronic

NIC Infrastructure gears up for Electronic Data Interchange (EDI) for Paperless Trade

Electronic Data Interchange (EDI) is the inter-organizational exchange of business documentation in structured, machine-processable form. EDI is actually a way of replacing manual data entry with electronic data entry. The purpose of EDI is to eliminate delays in processing and data re-entry.

Electronic Data Interchange can be used to electronically transmit documents such as purchase orders, invoices, shipping notices, advice and other standard business correspondence between trading partners. EDI can also be used to transmit financial information and payments in electronic form. When used as such, EDI is usually referred to as Electronic Funds Transfer (EFT).

## EDI Solutions from NIC

National Informatics Centre has been offering messaging services to its corporate customers. These include electronic mail service based on NIC's satellite-based computer-communication network, NICNET. With the growing international acceptance of X.400 standard (Please refer X.400 Standard Model Description in Box) and EDI technology, NIC recognizes the opportunity to significantly increase its business volume through differentiated services. In order to meet the new demand from the business community, NIC has established an EDI/E-Mail Value-Added Network (VAN) Server over NICNET.

## Network Server Configuration

At present, this Message Handling System (MHS) consists of only one central MTA based on VAX/4300 dual node cluster and TELECOM 400/G-X (or TC400) Message Switching (XS) software of Digital Equipment Corporation. The TC400 is based on the 1984 implementation of X.400. The VAX cluster is connected to the packet switch on two 64 kbps links. The TC400 MTA will be interconnected with VSNL's MTA using P1 protocol. Similarly, it can be interconnected with any MTA supporting P1 protocol for messages relaying purposes.

## Telecom 400 Implementation

The UA and MTA are co-located on the VAX/VMS platform. With this kind of configuration the UA is often called LUA. Using this LUA, both E-Mail and EDI messages can be exchanged. Separate mailboxes are maintained for EDI and E-Mail. NICNET Users with accounts on TC400 MTA can access the LUA to submit/ collect the messages. LUA also gives a limited facility to create E-Mail; but creation of EDI standard message should be done outside LUA.

To cut down the access time on the Network Server, a Remote User Agent (RUA) software named PC-BOX/UNI-BOX will be given to Users. The PC-BOX is a stand-alone software resident on DOS platform. The UNI-BOX on UNIX platform can create the E-Mail messages and submit them to MTA. The protocol used between RUA and MTA (via LUA) is Digital's proprietary protocol (Common Definition Interface Format, CDIF). This kind of format is adopted by almost every vendor to minimize the cost at the user site.

## Utility Features of Network Server

The NIC Network Server is also hosting a DEC/EDI central translator software to provide:

> Value-added services such as EDI standards translation.

Mailbox Users may want to convert the structured message (created using forms) into EDI standard message or require translation from one EDI standard to another (eg. from X12 to EDIFACT) before delivering the message to the trading partner.

> **EDI capability for infrequent Users**

A User can upload ASCII flat-files extracted from his in-house computer application into DEC/EDI through an application interface specific to him. DEC/EDI translates the flat-file into a defined standard message (eg. EDIFACT, X12 etc.) and forwards it to the trading partner. In the same way, it can receive EDI messages from the trading partner, convert into flat-file, and make it available for the User to download into his in-house computer application for processing.

## Transport Media for EDI

The actual movement of EDI data can take many forms. The transmission can be directly between two parties; or it can be transmitted indirectly via a third party which acts as a service provider (VAN). Also, the transmission can be made in the form of computer tapes and disks (where large volumes are involved), or any other forms of physical storage of data as long as the data can be processed by the receiving computer without re-keying.

## EDI Requirements

Along with some sort of hardware for communications, the basic requirement is a software capable of handling and controlling incoming or outgoing EDI messages to any number or combination of trading partners. Such a software is generally called an EDI converter or translator and is totally independent of the computer applications that pass data to it, or receive data from it. NIC provides such an EDI convertor software, based on DOS, to be used as RUA for EDI-message class. This package operates both as a stand-alone workstation as well as an unattended, front-end processor. It comes with a built-in, user-friendly development tool kit for customization of EDI message templates, screens, printouts and flat files for uploading and downloading. The package supports all versions of EDIFACT and X12 standards and is upgradable to any other industry standard including proprietary messages. (For further information please contact:

TDPP EDI Group,

National Informatics Centre,

A-Block, CGO Complex, Lodhi Road,

New Delhi - 110 003.

Phone: 4360597, Fax: 91-11-4362489.)

**X.400 Standard Model**

**Message Handling System (MHS) Model**

Recommendation X.400 describes the system model and service elements that administrations provide for subscribers to exchange messages on a store-and-forward basis. In essence, X.400 MHS conventions provide two fundamental types of Message Handling (MH) services — Interpersonal Messaging (IPM) and Message Transfer (MT).

Interpersonal Messaging (IPM) (encoded in P2 protocol) is a person-to-person communication of electronic mail (E-Mail). Message Transfer (MT) service supports general, application-independent message transfer. Message Handling System (MHS), which describes sub-layers within the Application layer, supports both services.

An MHS User (depicted in figure), can be either a person or computer application.

A corresponding User Agent (UA) represents a User, classified as an originator or recipient, in the MHS. UAs interact with Message Transfer Agents (MTAs) and, with MTAs, form the Message Transfer Systems (MTS). UAs are grouped into classes based on the types of messages they handle; each identifying its class by facilities in the MTS.

Collectively, all these elements make up the Message Handling Environment. Functions performed solely by the UA and not standardized as part of the MH services, such as those proprietary features of a vendor's UA implementation, are called local UA functions.

An originator prepares messages with the assistance of a local UA, which structures the information into envelope and content entities. After the envelope and contents are submitted to the MTS, the MTS initiates a generalized store-and-forward service. The MTS must support both submission and delivery interactions with the appropriate UAs.

Using the relaying interaction (P1 protocol) and its associated relaying envelope, each MTA passes an outbound message to another MTA until the message is received by the recipient's MTA, where it is delivered to the recipient UA via the delivery interaction (P3 protocol). The relaying envelope contains information related to MTS operation as well as the service elements requested by the originating UA. Generally, MTAs transfer messages of binary information and do not alter or interpret the contents unless instructed by a service element to do so.

Organizational Mapping Facility: Since a large-scale implementation of the MHS often links geographically and logically-separate Users, some means for distributing system administration tasks are necessary. A Management Domain (MD) fulfills this task. An MD consists of at least one MTA and can contain UAs owned by an organization or public administration. Domains managed by administrations (such as P&T) are Administration Management Domains (ADMDs), while those maintained by private organizations are Private Management Domains (PRMDs).

Source: Datapro Reports
