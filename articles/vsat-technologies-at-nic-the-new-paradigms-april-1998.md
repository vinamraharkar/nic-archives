---
title: "VSAT Technologies at NIC : the New Paradigms"
publication: "Informatics"
issue_date: "April 1998"
pages: [2, 3, 4, 5, 6, 7]
author: null
section: null
---

## VSAT Technologies at NIC : the New Paradigms

The Internet technology has grown tremendously over the past few years and consequently, a dire need for high speed access mechanisms has arisen. Being a pioneer in India in the field of VSAT technologies, NIC has kept pace with the latest by acquiring three new VSATs recently.

In order to meet its networking requirements, NIC has been operating the 850-node CDMA network and the 20-node SCPC network, which have already been discussed in a previous issue of Informatics (October '94). To fulfill the growing demand of the NICNET users for a direct Internet access from their premises (eliminating the last-mile problem) and to support a number of value-added services, NIC has recently introduced three new types of VSATs namely, FTDMA, DirecPC and IP Advantage.

FTDMA

The FTDMA VSAT system is a private communication network designed for bi-directional traffic that includes interactive transactions, batch file transfers, data broadcast and voice communications. Broadcast of audio and video can also be included as add-on options.

The FTDMA features a unique and patented two-dimensional satellite access scheme which combines the TDMA slotted ALOHA and FDMA techniques.

The star topology of a FTDMA network is well suited for use in configurations where corporate headquarters or data centres communicate with hundreds or thousands of geographically dispersed locations. The System supports a variety of data protocols and applications as well as voice, providing central 'host-to-remote terminal' and remote terminal-to-remote terminal connectivity.

A FTDMA network consists of the following components:
● A Master Earth Station and a control facility or Hub.
● A number of VSATs located at the customers' remote sites.
● Ku-band satellite channels which provide the transmission medium interconnecting the Hub and the VSATs.

In a typical FTDMA network, many remote locations with end-user terminals and optional voice equipment can be connected through VSATs to a centralized processing centre (hub) or to the other remote locations through the hub. The hub is connected to the customer's host computer and voice systems either directly or through dedicated communication links. The central location may have several host computers and voice systems, each assigned to specific regions or applications of the network.

The FTDMA network supports multiple outbounds (256kbps) and multiple inbounds (76.8 kbps). The modular hub design allows each customer's network to be sized cost-effectively to meet the existing and future needs. It also permits an easy incorporation of new features as well as independent sizing of host ports and in-bound and out-bound bandwidths.

Components of the FTDMA VSAT
● A small outdoor antenna (1.2/1.8/2.4 metres)
● A low power Outdoor Unit (ODU)
● An Indoor Unit (IDU)

The VSAT supports TCP/IP, X.25 and X.28 protocols. The IDU provides the following interfaces for connecting the user's machines:
● LAN port with UTP (RJ45) interface.
● Four Serial ports which could be configured for X.25 or X.28.
● Voice port with RJ11 interface (optional)

The system utilizes a "Television Receive Only" technology by using mass-produced Low Noise Blocks (LNBs) on the VSAT receipt channel.

The various applications supported on the FTDMA network include:
Corporate communication
E-mail
EDI
Internet/Intranet Solutions
Web enabled database access
Point-to-Point voice communication
Databroadcast
Multimedia Broadcast

DirecPC

DirecPC is a high-speed satellite broadcast system featuring a PC plug-in card satellite receiver. In order to receive the DirecPC broadcast carrier, a PC should be equipped with an ISA adapter card and a 1.2/1.8/2.4 -m antenna.

The System provides a 12 Mbps broadcast channel from a single uplink earth station called Network Operations Centre (NOC). Data Encryption Standard (DES) encryption-based conditional access ensures that a receiver PC may only access that data which it is authorized to receive.

The DirecPC system primarily offers the following three kinds of services to Intel x86 PC servers and workstations:
Digital Package Delivery : This is a service that uses the broadcast nature of DirecPC's satellite communication technology to provide an efficient mechanism to transfer any collection of PC files (called a Package) to widely distributed multiple receiving PCs. Packages are stored-and-forwarded through the DirecPC NOC.

As such, Package Delivery is not a real-time service. DirecPC package takes advantage of the broadcast nature of satellite communication in greatly reducing the cost of transferring relatively large packages such as those occupying more than 100 MB, to multiple locations by having a single broadcast received in parallel by all addressed sites. The service is typically used with a selective retransmission technique to ensure error free delivery to each location.

Multimedia Service : DirecPC's multimedia service provides IP multicast transport via the DirecPC service. The NOC relays a configurable set of IP multicast addresses across the space link. The information provider passes IP multicast packets to the NOC via an Ethernet link or by any wide area network connection. Remote DirecPC adapter card accesses the IP multicast through the standard Winsock API allowing many off-the-shelf applications to operate with no modification.

Turbo Internet Access : This allows a PC high-speed (upto 400kbps) access to the Internet. At the remote host, an NDIS device driver operates with the native TCP/IP stack for Win95. Reception from the Internet takes place via the DirecPC. Transmission into the Internet takes place via a dial-up Serial Line Internet Protocol (SLIP) or Point-to-Point Protocol (PPP) connection into an Internet access provider. The DirecPC architecture is open, thus allowing the information provider, complete control over their content and the user interface with it.

IP Advantage

The IP Advantage VSAT comprises of ISBN (Integrated Satellite Business Network) and DirecPC. ISBN is a two-way transmission system for data traffic between a HUB and many remote locations or Personal Earth Stations (PES). All ISBN traffic is carried digitally between the HUB and remote PES via one or more transponders aboard a Geostationary Satellite.

A single large sophisticated HUB station supports many small PES stations. The HUB-to-PES direction of transmission is termed as "outroute", while the PES-to-HUB transmission is termed as "inroute".

Since the remote stations have small antenna and low transmit power levels, the inroute signals are relatively weak. The HUB, with its high power amplifier, transmits a sufficiently strong signal for reception by the small remote stations; and the large HUB antenna with its large receive gain compensates for the weak signals transmitted by the remote stations.

The Time Division Multiplexed Outbound is a 512kbps continuous bit stream, consisting of concatenated (i.e. linked together) variable length packets. The ISBN inbound, from the remote station to the Hub, consists of multiple independent Time Division Multiple Access of 64kbps bit streams. The inroute data is packetized and transmitted as bursts. The assignment of time slots in which each user is permitted to transmit its burst of traffic is centrally controlled at the Hub and can be tailored to the needs of each user.

The IP Advantage network supports multiple outbounds (512kbps) and multiple inbounds (64kbps). The modular hub design allows each customer's network to be sized cost-effectively to meet the existing and the future needs. It also permits easy incorporation of new features as well as independent sizing of host ports and inbound and outbound bandwidths.

Components of IP Advantage VSAT
● A small outdoor antenna (1.2/1.8/2.4 metres)
● A low power outdoor unit (ODU)
● An indoor unit (IDU)

The VSAT supports TCP/IP X.25 and X.28 protocols. The IDU provides the following interfaces for connecting the user's machines:
● LAN Port with BNC (10base2) or UTP (RJ45)
● Two serial ports which can be configured for X.25 or X.28.
● TVRO out which is used to connect to DirecPC adapter card installed in the PC.

The System utilizes a television receive only (TVRO) technology by using mass-produced Low Noise Blocks (LNBs) on the VSAT receipt channel.

The applications supported on the IP Advantage network include:
Corporate communication
E-mail
EDI
Internet/Intranet Solutions
Web enabled database access
Data and Video Broadcast
Multimedia Broadcast
Package Delivery

Each of the VSATs described above, have been carefully designed to meet the user-specific requirements. The Hub equipment corresponding to all the three VSATs is already operational and all of them have been seamlessly integrated with the existing network for smooth interoperability.

In order to derive full advantage of DirecPC and to extend the Internet access to the District Centres of NIC, the DirecPC VSAT has been integrated with the already working C-200 VSAT. With this, the entire NICNET has been fully converted to TCP/IP based network. An advanced Object-oriented Network Management System (NMS) has also been installed for an efficient management of the entire network.

For further details, please contact:
Satcom Division, NIC Headquarters
A-Block, CGO Complex, Lodhi Road, N. Delhi
Ph.No. 91-11-4361609; Fax: 91-11-4362489
Email: satcom@nicnet.nic.in
www: http://satcom.nic.in
