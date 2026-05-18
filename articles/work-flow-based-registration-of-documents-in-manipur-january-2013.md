---
title: "Work Flow Based Registration of Documents in Manipur"
publication: "Informatics"
issue_date: "January 2013"
pages: [13, 14, 15]
author: "PRASHANT BELAWARIAR, JITEN SINGH HAOBAM, TARAKISHORI RAJKUMARI, Kh. Rajen Singh"
section: "E-Gov Products & Services"
---

## Work Flow Based Registration of Documents in Manipur

Marriage registration provides social security, self-confidence particularly among married women. This facilitates in obtaining passport, changing of name, proving of genuine nominee for pension or insurance benefits on expiry of the job holder etc.
Some people avoided the registration procedure when buying immovable properties. They fetched new Jamabandi / patta without confirming the actual change of ownership (mutation). The registration system mitigates such risk of fraud and disputes and underlines the importance of integration with Land Record (LR) Systems.
CHALLENGES
i. Consequence of fraud Jamabadi (Patta).
ii. Takes weeks to deliver signed registration certificate by the registration authority.
iii. Revenue loss to government due to non-transparency in computing of land valuation and registration fee.
iv. Lack of proper biometric verification and no instant photo evidence record.
v. Non integration with LR system.
vi. Non availability of digitally signed registration certificate to citizen.
SCOPE OF THE COMPUTERIZED SYSTEM
Implementation of the computerized system started in the year 2007-08 for all the four Sub-Registrar Office in Manipur viz. Imphal west, Imphal east, Thoubal and Bishnupur. Manpower training at different levels like computer fundamentals, software operations, scanning of deed documents, biometric operations, data backup-restore plans were imparted by NIC.
PLATFORM OF THE SYSTEM
I. Windows XP or Windows 7 OS were supported. Front end application developed in VB 6.0. Crystal report 7 was used for specific reports.
II. High quality finger print reader ‘SecuGen HamsterPlus FDU02’ model device with SDK library file SecuBSP.dll is used for capturing all the five finger prints of the presenters.
III. Web cam of high quality resolution to capture photo of presenters. Image is stored in database as binary data.
IV. Back end database is MSSQL server 2005 with full-on-incremental backup and restores strategy plans.
MASTER DATA
Master data for district, subdivision, circle and village used. The system relies on two most important master data sources, the census database and another the revenue database. Census master data is referenced in ownership transaction. Revenue master data is referenced in plot transaction.
PROCESS REENGINEERING
I. In addition to paper based recording of rolled thumb fingerprint, there is digital enrollment and verification module of fingerprints of presenters using ‘SecuGen HamsterPlus FDU02’ reader device.
II. An instant photo capturing module for the presenters before the registering authority.
III. A new module for Minimum Guidance Value (MGV) incorporated, vide the office order no. 2/1/SR/2007-Com (Rev) dated 20-Mar-2012.
DELIVERABLES
I. Non-encumbrance certificate for the purpose of buying, mortgaging, loan and for purposes in court.
II. Signed registration certificate issued by the registration authority within two days which earlier took weeks in the manual system.
SALIENT FEATURES
i. A client server, role based secured, efficient and work flow based system.
ii. Maintaining thorough scrutinized linkage of pertinent multiple ownership history with the mother deed history without missing a single link which can originate further transfers and transactions in a normalized database.
iii. Multiple official users are capable of doing transactions concurrently in a controlled work flow which enhances work productivity. Application maintains log trends of every transactions. This helps the registration officer in monitoring user activities.
iv. Instant photo capturing module for the presenters.
v. Digital enrollment and verification module of fingerprints of presenters using ‘SecuGen HamsterPlus FDU02’ reader device.
BIOMETRIC SYSTEM : BRIEF OVERVIEW
Biometric is an automated method of recognizing a person based on physical or behavioral characteristics. Biometric information, which can identify a person accurately includes fingerprint, voice, face, iris, hand and hand geometry.
There are two functional methods in biometric system. One is called identification (1 to many mapping) in which a recent captured biometric sample is compared with a set of samples, sequentially one by one. The other one is called verification (1 to 1 mapping) in which a recent captured biometric sample is compared with a single stored biometric sample.
With the wide spread acceptance, convenience and reliability; fingerprint identification is considered to be the least intrusive of all biometric verification techniques. Fingerprint is an intrinsic human token which is difficult to steal and can be read by an inexpensive reader whereas strip cards, passwords or user credentials etc. can be stolen.
Fingerprint Identification Record (FIR) has a unique structure, which consists of three fields: format, header and opaque fingerprint data.
If FIR format is changed the header or finger print data structure can be changed.
The header field contains information to processed fingerprint data. Header length is the length of the header. Data length is the length of the fingerprint data. Version is the FIR version number.
Data type indicates for raw, intermediate or processed. Purpose indicates for enrollment, verification or identification. Quality indicates for fingerprint quality in the scale of 1 to 100, 1 is the lowest and 100 is the highest. Reserved is for future usage.
Payload is any data like password, employee code or cryptographic key which is stored within the FIR and released after successful verification. FIR cannot be used as cryptographic key since no two fingerprints captured from the same finger are identical in all aspects.
G2C AND G2G E-GOVERNACE ORIENTATION
1. Drastic reduction of time in generation of signed registration certificate by the registration authority which is now one or two days but earlier took weeks in the manual system.
2. Transparency in calculation of land valuation since the introduction of the module - Minimum Guidance Value (MGV). It optimized revenue collection for the Government.
3. Transparency in computing registration fee (as 1%) and stamp value (as 3% on MGV for Rural and 4% on MGV for Urban)
4. Non-encumbrance certificate generation module benefits banks and litigants in case of mortgage and loan.
CONCLUSION
i. Devising and developing a secured web based system for integration of registration system and LRC under NLRMP is under way. NIC WiMAX connectivity has been installed in the valley SROs. The new system will strengthen and would be able to give seamless technical solution in smoothening the functionalities of e-Governance using the current ICTs in the most disputed and tiresome process of property registration.
ii. A system proposed to make the availability of digitally signed certificates (both for registration and LR) by DSC of the concerned officers in a common web based window to the citizens has been demonstrated by NIC Manipur to the Chief Secretary, Govt. of Manipur and to other revenue officers.
iii. There must be stringent and relevant Government orders in implementing computerization in earnest and with proper utilization of funds of the parent department to implement the computerized system.
iv. Application must be a secured web based version. It must be audited by a third party audit team. Web based application must be secured from vulnerabilities and intended attacks.
