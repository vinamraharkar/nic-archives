---
title: "LAN TECHNOLOGIES"
publication: "Informatics"
issue_date: "January 1999"
pages: [2, 3, 4, 5, 6, 7, 8, 9]
author: null
section: "Lead Story"
---

## LAN TECHNOLOGIES

Continuing with our on-going series of Lead Stories on Networking Technologies, we present another important aspect, namely, LAN technologies and Internet Access over LAN.

In general terms, LAN (Local Area Network) refers to a group of computers interconnected into a network so that they are able to communicate, exchange information and share resources (e.g. printers, application programs, database etc). In other words, the same computer resources can be used by multiple users in the network, regardless of the physical location of the resources.

Each computer in a LAN can effectively send and receive any information addressed to it.

This information is in the form of data 'packets'. The standards followed to regularize the transmission of packets, are called LAN standards. There are many LAN standards as Ethernet, Token Ring , FDDI etc. Usually LAN standards differ due to their media access technology and the physical transmission medium . Some popular technologies and standards are being covered in this article.

Media Access Control methods

There are different types of Media Access Control methods in a LAN, the prominent ones are mentioned below :

Ethernet - Ethernet is a 10Mbps LAN that uses the Carrier Sense Multiple Access with Collision Detection (CSMA/CD) protocol to control access network. When an endstation (network device) transmits data, every endstation on the LAN receives it. Each endstation checks the data packet to see whether the destination address matches its own address. If the addresses match, the endstation accepts and processes the packet. If they do not match, it disregards the packet. If two endstations transmit data simultaneously, a collision occurs and the result is a composite, garbled message. All endstations on the network, including the transmitting endstations, detect the collision and ignore the message. Each endstation that wants to transmit waits a random amount of time and then attempts to transmit again. This method is usually used for traditional Ethernet LAN.

Token Ring - This is a 4-Mbps or 16-Mbps token-passing method, operating in a ring topology. Devices on a Token Ring network get access to the media through token passing. Token and data pass to each station on the ring. The devices pass the token around the ring until one of the computer who wants to transmit data , takes the token and replaces it with a frame. Each device passes the frame to the next device, until the frame reaches its destination. As the frame passes to the intended recipient, the recipient sets certain bits in the frame to indicate that it received the frame. The original sender of the frame strips the frame data off the ring and issues a new token.

Fast Ethernet - This is an extension of 10Mbps Ethernet standard and supports speed upto 100Mbps. The access method used is CSMA/CD .For physical connections Star wiring topology is used. Fast Ethernet is becoming very popular as an upgradation from 10Mbps Ethernet LAN to Fast Ethernet LAN is quite easy.

FDDI (Fiber Distributed Data Interface) - FDDI provides data speed at 100Mbps which is faster than Token Ring and Ethernet LANs . FDDI comprise two independent, counter-rotating rings : a primary ring and a secondary ring. Data flows in opposite directions on the rings. The counter-rotating ring architecture prevents data loss in the event of a link failure, a node failure, or the failure of both the primary and secondary links between any two nodes. This technology is usually implemented for a backbone network.

Topologies

The various ways in which cables are arranged constitute the topologies in a LAN. Some of the Ethernet Topologies are described here :

Bus Topology : Thick and thin Ethernet LANs use a bus topology, in which devices connect directly to the backbone at both the physical and logical levels . This type of LAN is very easy to use and cheap to implement, but the problem is to troubleshoot and maintain.

Star Topology : In this topology , a individual twisted pair or fiber optic cable is coming from each node and terminating at central network concentrator as hub/switch. The star wiring simplifies LAN administration and maintenance.

Token Ring Topology : Stations on a Token Ring network attach to the network using a multistation access unit (MAU ) through UTP/STP cable. Although the Token Ring is logically a ring, physically it is a star, with devices radiating from each MAU .

Basic LAN components

There are essentially five basic components of a LAN.

Network Devices such as Workstations, Printers, File Servers which are normally accessed by all other computers

Network Communication Devices i.e. devices such as hubs, routers, switches etc., used for network operations

Network Interface Cards (NICs) for each network device required to access the network .

Cable as a physical transmission medium.

Network Operating System - software applications required to control the use of the network LAN standards.

Network Communication devices

A LAN comprises of different communication devices across the network such as the following :

Repeater : A Device that amplifies and regenerates signals , so that they can travel for longer distance on the cable.

Router : The basic function of the router is to route the traffic from one network to another network efficiently. It provide intelligent redundancy and security required to select the optimum path. Usually routers are used for connecting remote networks.

Hub : A typical hub is a multi-port repeater. The signals received at the backbone is regenerated and transmitted to all other ports.

Switch : This is a device with multiple ports which forwards packets from one port to another. In case of 10Mbps Ethernet switch, each port supports dedicated 10Mbps bandwidth. Ethernet switch is fast emerging as a replacement of the traditional thick backbone and best way to improve performance of the network.

Physical Transmission Media

Cables constitute the Physical Transmission Medium in a LAN and could be of the following types.

Coaxial cable : Coaxial cable consists of a stiff copper conductor wire as core surrounded by an insulating material. There are two type of coaxial cables used in Ethernet LAN - Thick coaxial cable used for distances upto 500m and thin coaxial cables upto 185m.

Twisted pair cable: They are four pairs of insulated copper conductors twisted and bounded by single plastic sheath with or without conductor shield termed as STP and UTP respectively.

Fiber Optic Cables : In Fiber Optic cable, the medium used is optical fiber instead of any conductors .The information is transmitted in form of optical signal. Due to the high speed of optical signals the cable can support high bandwidth for longer distance. Depending upon the type of fiber, there are two types of Fiber Optic cables, single mode and multi-mode.

Asynchronous Transfer Mode (ATM)

In recent years, with the boom in information technology leading to new GUI based applications, more emphasis is being given to improving backbone and inter LAN performance. This has lead to a new concept of connecting the backbone through ATM switches. ATM (asynchronous transfer mode) is the switching technology where data is sent in forms of fixed length cells instead of packets of various lengths. The speed of , in case of the ATM switches, is comparatively much faster than the traditional Ethernet switch, as the network overhead is less for ATMs.

Internet Access over LAN

There are various methods of connecting a LAN to the Internet Gateway, which are explained as below :

Dial-up
Leased Line
ISDN
VSAT Technology
RF Technology (Wireless Access)
Cable Modem

Dial - Up

A common way of accessing Internet over LAN is the Dial-Up approach. In this method, a remote user gets to Internet as follows - Initially the remote user's PC is linked to the local gateway through an existing dialup line using modems, once the user has reached the local gateway, further routing up to Internet is taken care of, by the local gateway itself. The routing procedures are transparent to the end user.

Leased line

Leased line facility provides reliable, high speed services starting as low as 2.4kbps and ranging as high as 45 Mbps (T3 service). A leased line connection is an affordable way to link two or more sites for a fixed monthly charge. Leased Lines can be either fiber optic or copper lines High capacity leased line service is an excellent way to provide data, voice and video links between sites. Leased line service provides a consistent amount of bandwidth for all your communication needs.

ISDN

Integrated Services digital Network (ISDN) is a digital telephone system. ISDN involves the digitization of telephone network so that voice, data, graphics, text, music, video and other source material can be provided to end users from a single end-user terminal over existing telephone wiring.

ISDN BRI (Basic Rate ISDN) delivers two 64 kbps channels called B channels and one at 16kbps (D channel). ISDN offers speed at 64 Kbps and 128 Kbps and is an alternative for those with a need for greater Bandwidth than dial service. For utilizing the ISDN service, the User needs to have an ISDN Terminal Adapter and an ISDN Card on the system.

VSAT

VSAT technology has emerged as a very useful, everyday application of modern telecommunications. VSAT stands for 'Very Small Aperture Terminal' and refers to 'receive/transmit' terminals installed at dispersed sites connecting to a central hub via satellite using small diameter antenna dishes (0.6 to 3.8 meter). VSAT technology represents a cost effective solution for users seeking an independent communications network connecting a large number of geographically dispersed sites. VSAT networks offer value-added satellite-based services capable of supporting the Internet, data, voice/fax etc. over LAN. Generally, these systems operate in the Ku-band and C-band frequencies.

RF Technology (Wireless Access)

Please refer to cover story of October,1998 issue (Volume 7 No.2) of Informatics

Cable Modem

The Internet Access over cable modem is a very new and fast emerging technology. A "Cable Modem" is a device that allows high speed data access via a cable TV (CATV) network. A cable modem will typically have two connections, one to the cable wall outlet and the other to the PC. This will enable the typical array of Internet services at speeds of 100 to 1000 times as fast as the telephone modem. The speed of cable modems range from 500 Kbps to 10 Mbps.
