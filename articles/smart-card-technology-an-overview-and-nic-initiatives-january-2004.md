---
title: "Smart Card Technology-An Overview and NIC Initiatives"
publication: "Informatics"
issue_date: "January 2004"
pages: [4, 5, 6, 7]
author: "S.K.Sinha, NIC HQ"
section: "E GOV INITIATIVES"
---

## Smart Card Technology-An Overview and NIC Initiatives

In this issue, we feature the technology behind Smart Cards which has heralded a new dimension in the area of security of distributed systems, personal identification and payment applications.

Plastic cards are a way of life in most developed countries. They are fast gaining momentum in the developing world too. Whether it is for certificate of identity, e-Purse, or Credit/Debit purposes, plastic cards have revolutionized the way business is performed in our day-to-day life. They have been in use for a long time in the form of Magnetic Strip Cards. However, magnetic strip technology has inherent security problems due to the un-intelligent nature of the card, which is basically a digital medium containing data in encrypted form. In that respect it is no different than a normal floppy disk, except with the difference in data writing format and devices.
Smart cards have heralded a new technology that has tremendous potential for enhancing the security of distributed systems, for personal identification and payment applications.

ž| The Technology :
A smart card is a credit card-sized, tamper-resistant security device that offers functions for secure information storage and information processing that rely on VLSI chip technology. A smart card contains a secure microprocessor chip embedded in the plastic card (Fig.1). The chip can implement an Operating System (OS) with a secure file-system, and the OS has the capability to compute cryptographic functions, and actively detect invalid access attempts onto the card file system. With proper application of file system access rights, a smart card can be safely used by multiple, independent applications.
A smart card is distinguished from a magnetic strip card (e.g., typical credit card), and laser optical cards, as the latter have no VLSI circuitry and Operating System and thus no active security procedures and no built-in tamper-resistance. Anyone with an appropriate card reader can read whatever is on the card.

ž| Information Storage :
Smart Card file system, which is implemented over the E2PROM (Electrically Erasable Programmable Read Only Memory) of microprocessor chip, contains hierarchical file system, with MF (Master File) at the top, DF (Dedicated File), and EF (Elementary File) as various entities in the hierarchy (Fig3). Data elements are grouped and stored in EF, which is the bottom level entity. Dedicated files (DF) are like directory files of conventional File Systems containing DF’s and EF’s. Dedicated Files are also the entities hosting all files related to one single application (viz. Driving License, Electoral ID Card, PAN Card etc), and therefore are also termed as Application Files. MF is top level Dedicated File. All kind of files i.e. MF, DF and EF can be configured for their security parameters (conditions) for various operations (Read, Modify, Delete) on their headers. Definable security conditions may be PIN verification, Key Authentication etc.

Reading and writing, information onto the card is carried out by the device called Smart Card reader. Since Smart Card is a passive device in itself, it draws power supply and clock from the smart card reader. Through a predefined set of protocols, communication is established between the Computer(PC) and Smart Card through the Smart Card reader.Standard set of API’s are available under Windows and other Operating Systems to integrate Smart Card capabilities into different software applications. Smart Card, which has the capability of a miniature computer, communicates with the PC to perform different operations on Smart Card data.

?| Smart Card Security :
Smart cards are the most secure devices to store small piece of information, which technologically makes it possible to impose desired security conditions/rules for accessing the required information. Following are the Security Mechanisms which Smart Card provides.
a. PIN Verification: PIN is like a password, which is securely stored in the Smart Card. Any specific Smart Card functionality (e.g. Performing Money Transaction, requesting for e-Service delivery), can be bound with the successful PIN verification. If PIN verification fails, built-in mechanism on the Smart Card disallows the functionality to get invoked. After three or four unsuccessful attempts Smart Card OS blocks the PIN usage and thereby protecting the valuable Smart Card resources.
b. Key based Authentication: Key based authentication is the biggest security strength of Smart Card, due to which they are considered to be most secure devices as compared with other cards (Magnetic, Optical etc.). Keys are typically used for cryptographically securing data on Smart Card, with the help of strong on-chip encryption algorithms like 3DES or RSA. Through challenge-response mechanism and encryption and decryption through the corresponding keys, two secure devices (with one or both as Smart Cards) can negotiate to authenticate each other (Fig 4). And this is the methodology through which a person proves his identity, what he claims to be, by possessing one of the keys, securely stored on his card. The authentication process can be based on symmetric keys (Master Key-Derived Key) or asymmetric keys (Public Key-Private Key). Smart Card technology provides the security against direct access to keys, and makes it possible that all kinds of security operations are performed internally on the chip, without sending keys out of the card. This enhances the security to a great extent. The Smart Card chip (Microprocessor), is strong enough to run various security related complex algorithms using keys internally.

?| Smart Card and PKI :
PKI technology greatly depends on the security of the private key of the individual. Compromise of private key can lead to the failure of trust environment created for the security of cyber world. Smart Card technology helps implement this in following ways,
i. Secure storage of individual’s private key, inside the Card.
ii. On-Card generation of private key-public key pair.
iii. On-Card generation of digital-signature.
iv. On-Card encryption and decryption of data.
All the basic data/information security characteristics i.e. Authenticity, Integrity, Confidentiality and Non-repudiation can be ensured through above Smart Card PKI security mechanisms.

?| Smart Card for proof of Identity :
Identity fraud is a growing problem world wide ; specially in the context of the current world scenario. Whether it is the question of secure border control or delivery of citizen services to right person, ensuring the proof of identity becomes a matter of vital interest. Present form of ID are not secure enough or foolproof to stop the identity fraud. Almost every thing which can be printed can be faked. Terrorists regularly use fake passports to cross the world boundaries.
Smart Cards with biometrics having digital signature of issuer authority can effectively provide the fool proof mechanism to prove the identity of a person is what he claims to be. Using PKI technology on Smart Card, Identity Data of individual with his biometrics on the card can be digitally signed by an issuer certified by Trusted Certification Authority. Field verification process is performed to check for the following.

?| Card is Authentic :
Authenticity of card is established through challenge response mechanism between the secret key (Private key) stored on the card, and public key, which is available to the interface device (typically a simputer or a hand held terminal), off-line or on-line. A limited version of off-line CRL (Certificate Revocation List) can also be stored on these devices, as per requirement of PKI process. CRL can be synchronized time to time with the one available with Certification Authority.

?| Identity of card holder is authentic :
First the digital signature of the issuer authority which are stored on-card are verified through off-line or on-line verification process as explained above. Then the stored bio-metrics of card holder are matched with the one captured live at the point of verification. Since the stored bio-metrics are the same which were captured when card was issued and are the part of data which is digitally signed, matching with live capture, authenticates the identity of the person.

?| Smart Card for delivery of Citizen Services :
Smart Card technology can enhance the speed and authenticity of the process of efficient delivery of G2C services. Efficient delivery of services requires readily available proof-of-identity, authentic transaction history and entitlement details. In Indian context they may be services like ration card, passport, Land Records, Old age pension, different kind of subsidies and support in rural sector including health and education etc. All these kind of services require the on-site/field verification of proof of identity, entitlement details of beneficiary and application specific data. One of the biggest benefits of usage of smart card for these kinds of services is that, it makes it possible to provide authentic application specific data from the individual’s card at the place of business transaction, which otherwise would have been achieved only through creating an efficient data communication link and connecting to the central Service Database at some remote location. Therefore it not only eliminates the need of a vast data communication link across the country with very large number of nodes, but also its availability in all the places where service is being delivered.

?| Delivery of Services through Web :
With the advent of Internet and World Wide Web, delivery of information/ data to masses has become extremely easy just by publishing it over the web. But there are many situations under which the information service which is required to be delivered through internet, is private/ confidential to the person for whom it is meant to be. This kind of situation makes it essential to first establish the identity of the person remotely through internet. Once it is established that the remote user is a citizen who is genuine subscriber of the service, only then internet/network delivery is made for the required service. Smart Card technology provides the fool proof mechanism of remote authentication/ verification of the person through internet, in conjunction with PKI and biometrics technologies. Delivered information can also be written safely on the individual’s Smart Card for future use. Few examples of this kind of services are, e-Vote casting over web, Web submission of Income Tax returns, Delivery of Railway/Airlines Ticket, Road tax payment and delivery of receipt etc.

?| Smart Card and Access Control :
Smart Card technology provides very safe and convenient way of controlling and restricting the access of individuals to the critical infrastructure of Government or any other organization. Based on the sensitivity, a building or infrastructure can be categorized into multi tier levels of desired security, and divided into security zones. Access to these zones is regulated through Smart Card Reader controlled electronic/electromagnetic door locks. Smart Card and the Card holder is authenticated by these readers and the access privileges written on the card are read by the readers to control the release of the lock. Security mechanism can be enhanced by including smart card assisted biometrics verification. By carefully designing the entry and exit log, the movement of individuals can be tracked for later security analysis. This system can also be used in an organization or educational institution for attendance monitoring and punctuality analysis.

?| Smart Card based Network Access Control and in-transit data security:
Current password based security for network log-on has weaknesses due to the vulnerability of passwords being stolen while keying-in or through a malicious program recording the key depressions on the background and passing-on the stolen log-on details to a rogue server. Smart Card based remote authentication comes handy to effectively eliminate this problem of network security which can be implemented for Secure Intranet or Virtual Private Networks (VPN).
Smart Card technology can also be effectively used for network data confidentiality and data authenticity. Data confidentiality is implemented by on-card encryption and decryption of in-transit data between sender and receiver, through robust encryption algorithms implemented on the Card chip. Data authenticity can be implemented by digitally signing the data with sender’s smart card and transmitting data along with digital signatures. Received data with signatures can be verified for integrity and authenticity by verifying digital signatures through sender’s public key.

?| Smart Card technology for e-purse and stored value :
Smart Card technology offers a most promising way of storing digital money and conveniently transacting it for small business transactions. Several payment systems world wide either use smart cards today or have announced plans to do so in the near future. For security reasons, current credit card payment systems have made on-line connectivity mandatory for business transactions. This hugely increases the operational cost for the systems where amount of money per transaction is relatively smaller.
For the payment systems where transaction amount is smaller, Smart Card based e-Purse system provides a secure, reliable and inexpensive solution. As an e-Purse, smart card stores an actual balance of money, as secure data. e-Purse system on smart card provides functionality of crediting and debiting the balance, after authenticating the cards mutually. Money can be credited on seller’s card and debited from buyer’s card, in an off-line mode, with the help of an off-line smart card terminal. Both the cards can load and unload balance from their bank account, by visiting a bank which provides this service. This concept of e-Purse transaction can also be successfully applied in automatic vending machines, like milk vending, tea/coffee vending machines etc where seller’s card can be fixed inside the vending machines, and accumulated digital money collected in a desired frequency.

NIC Initiatives in Smart Card Technology
ž| Smart Card in Transport Sector :
Ministry of Road Transport and Highways, in conjunction with few State Transport Authorities, took up the project of nation wide introduction of Smart Cards for Driving License (DL) and Vehicle Registration Certificates (RC). NIC was entrusted by the Ministry to help and provide its services as consultant for the complete project, which comprises,
v Development of Smart Card Technology Standards for interoperability across the Nation.
v Development and deployment of Symmetric Key Infrastructure for Smart Card Security.
v Development of Smart Card interface software with back-end Vahan (For RC) and Sarathi (For DL) softwares.
v To establish a Smart Card Compliance Certification body, to test and certify the compliance of smart cards with evolved national standards, for the various products brought into market by different industry players.

a) Development of National Standards for Transport Sector :
For any technology to work with compatibility across the country, it is essential that all the deployment agencies (States) follow same technology standards for their technology enabled delivery of service (in this case Smart Card based DL and RC). NIC led a team of professionals, domain specialists, academia and industry players, to evolve a technology standard for Smart Cards to be used for DL and RC, for interoperability across the Nation. Various standards which were evolved are,
v SCOSTA (Smart Card Operating System for Transport Applications)
v DL and RC related on-chip Card Data Layout
v Smart Card Hardware specifications
v Hand Held Terminal Application Specifications
v Key Management System

b) Development of Symmetric Key Infrastructure :
Security of data against fake duplication/ generation and prevention of road offences are the two major reasons for introduction of smart card technology for DL/RC. Smart Card security mainly banks upon the proper design of the Key Management System and its safe deployment. Symmetric Key based security was considered to be most suitable for field authentication of DL/RC and on-card booking of road offences at the field (Fig 6).

c) Smart Card interface software with back-end :
For performing various process operations in RTO office, interface software for Smart Card is required to read and write DL/RC data from the chip e.g. Personalization and issuance of DL and RC cards at RTO, addition of more vehicle classes in DL Card, Modifying the Road Tax data in RC Card, Permit issuance etc. A standard software has been developed to take care all these business processes.

d) Smart Card Compliance Certification body :
With the authorization from the Ministry of Road Transport and Highways, NIC has established a Smart Card lab, for testing and certification of Smart Cards brought about by industry players for supplying to deployment agencies. Smart Card brands, certified by this body can only be issued as DL and RC Cards in the country.

ž | Access Control System at NIC Headquarters :
After establishing sophisticated infrastructure for Communication and Cyber security monitoring and Control at NIC Headquarters, and also after establishing Digital Signature Certification Authority, NIC HQ has become a critical infrastructure for Government. Due to this sensitivity, NIC has established a Smart Card based access control system at NIC HQ building. Smart Cards have been issued to all employees as well as regular and occasional visitors for entry into the building. Access privileges have been defined in each card for visiting to various bays. For more secure zones, biometric verification has been made a precondition for access. All entry and exits points are being recorded to trace the movement.
