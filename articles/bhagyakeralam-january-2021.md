---
title: "Bhagyakeralam"
publication: "Informatics"
issue_date: "January 2021"
pages: [42]
author: "T Mohana Dhas (sio-ker@nic.in)"
section: "Appscape"
---

## Bhagyakeralam

Bhagyakeralam is an Android mobile application for Lottery Agents and citizens who buy Kerala Lottery Ticket. A buyer can check whether the lottery ticket is genuine or not by reading the QR Code. One can verify the prize eligibility after the Draw using this app. It also provides a facility to check the status of the claimed prize and different stages of the payment process. The app is introduced for the Lottery Department of the Government of Kerala.

Bhagyakeralam is the citizen interface for the Lottery Information System (LOTIS). LOTIS is a workflow-based software by NIC Kerala for the use of the Kerala State Lotteries Department. It includes Scheme management, Draw management, Variable data generation, Print order, Issue note generation and Centralized distribution, Agent Registration Service, Sales Counters, Result entry, Prize processing, Prize disbursement and E-payment of prize money to the winner’s bank account.

As a part of the security enhancement for the Lottery tickets printing, an AES encrypted code is embedded in the QR code and printed on the tickets. The decryption is done in the LOTIS server and is protected with a secure decryption key. The encryption key is regenerated for each draw. The Mobile App uses QR Code Scanning to achieve all its functionalities. The QRCode scanning in mobile App is implemented using an open-source ZXing library.

The ‘Bhagya Keralam’ mobile app provides the following services:
• Verify the authenticity of a ticket
• Check the Draw and Prize-winning status
• Check the prize claiming status
