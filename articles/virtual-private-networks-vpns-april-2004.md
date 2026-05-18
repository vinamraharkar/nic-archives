---
title: "Virtual Private Networks (VPNs)"
publication: "Informatics"
issue_date: "April 2004"
pages: [1, 5, 6]
author: "Anjana Chowdhary & R.S Mani, NIC HQ"
section: "Special Feature"
---

## Virtual Private Networks (VPNs)

Introduction
As all of us are aware of various security issues with the Internet, it has become mandatory to provide safe access to various internal resources to the users who are on the Internet. These users can be on the enterprise network in the Internet or can be from various ISP Dial-up networks. In the recent past NIC has launched the Virtual Private Network (VPN) services for these kinds of users. Some of the activities that will be diverted through the VPN include: Updation of sites through various mechanisms like front-page, ssh, ssftp and ftp.

Overview
A virtual private network (VPN) is a private data network that makes use of the public telecommunication infrastructure, maintaining privacy through the use of a tunneling protocol and security procedures. The main purpose of a VPN is to provide any organization the same capabilities as private leased lines at a much lower cost by using the shared public infrastructure. There are three types of VPNs, namely trusted VPN, Secure VPN, Hybrid VPN.

Trusted VPN
A virtual private network consisted of one or more circuits leased from a communications provider. Each leased circuit acts like a single wire in a network that was controlled by customer. The privacy afforded by these VPNs is basically based on the trust that all the routes within the VPN are kept without sharing it with any other customer/ Internet. This allowed the organizations to have their own IP addressing and their own security policies. The VPN customer trusted the VPN provider to maintain the integrity of the circuits and to use the best available business practices to avoid snooping of the network traffic. Thus, these are called Trusted VPNs. Trusted VPNs provide assurance of properties of paths such as QoS, but no security from snooping or alternation. In India this kind VPN is becoming more and more popular as the cost to the organization in building the network is reduced and these are named as MPLS (Multi Protocol Label Switching) VPNs. These can generally be separated into “layer 2” and “layer 3” VPNs. Technologies for trusted layer 2 VPNs include: ATM circuits, Frame relay circuits.

Transport of layer 2 frames over MPLS are as described in draft-Martini L2 MPLS and other related Internet Drafts. Figure-1 shows typical MPLS network where the customer connects to the local POP of BSNL at that location and creates a virtual Private Network.

Secure VPN
Networks that are constructed using encryption are called secure VPNs. Trusted VPNs offered no real security with respect to data confidentiality, the industry started to create protocols that would allow traffic to be encrypted at the edge of one network or at the originating computer, moved over the Internet like any other data, and then decrypted when it reached the corporate network or a receiving computer. This encrypted traffic acts like it is in a tunnel between the two networks: even if an attacker sees the traffic, he can not decipher the same. No change in the payload can be done by the snoopers/ attackers and the change will get reflected and the end node comes to know of the change and rejects the packet and requests for a re-transmission. Secure VPNs provide security but no assurance of paths.

Secure VPN technologies
This includes IPsec with encryption in either tunnel and transport modes. The security associations can be set up either manually or using IKE with either certificates or preshared secrets. IPsec is described in many RFCs, including 2401, 2406, 2407, 2408, and 2409. IPsec inside of L2TP (as described in RFC 3193) has significant deployment for client-server remote access secure VPNs.

Hybrid VPN
A secure VPN can be run as part of a trusted VPN, creating a third type of VPN called hybrid VPNs. The secure parts of a hybrid VPN is created by the customer himself and is fully under the control of the end user. (such as by using secure VPN equipment on their sites) or by the same provider that provides the trusted part of the hybrid VPN. This provides the assurance in the path of traversal and also encryption of payload. The secure VPN acquires the advantages of the trusted VPN, such as having known QoS features.

VPN in NICNET
The VPN Services currently provided in NIC come under the category of secure VPN. (IPSec VPN tunnel between VPN Appliance and VPN Client). The diagram on this page displays how the VPN services are implemented in NICNET.

Components used for this VPN setup
VPN Appliance
VPN Client 4.0.3 on a PC running Windows XP/Windows 2000 Prof / Linux
A Windows 2003 CA server is used as the CA server for issuing client certificates
Radius Server for authenticating the user and application of access control so that the user after having connected to VPN can only access the designated IP and PORT.

In the near future the VPN Services will be using NIC CA Certificates.
The VPN Service provides a secure communication channel for updating the websites and access to various resources that are internal to an organization. The VPN supports all the IPSec related Internet Standards.

The secure VPN acquires the advantages of the trusted VPN, such as having known QoS features.

A user with a VPN client connects and receives an IP address from the Internet service provider (ISP). This is then replaced by an IP address from the IP pool defined on the VPN Appliance. The user has access to everything on the inside of the firewall, including networks.

Users who are not running the client can connect to the web server using the address provided by the static assignment. Traffic of inside users does not go through the IPSec tunnel when the user connects to the Internet. Each user is given access to only those servers which are relevant to the particular web server for updating his page.

The VPN is made available at http://ftp.ren.nic.in/pub/vpn/ and can be downloaded and installed. The documentation file is also available at the same site. A mailing-list called vpnservices@nic.in has been created to support this service. Any issue with respect to this service can be sent to this mailing list so that it can be addressed.
For further information, mail to vpnservices@nic.in
