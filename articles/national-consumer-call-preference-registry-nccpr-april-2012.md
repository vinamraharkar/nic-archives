---
title: "National Consumer Call Preference Registry (NCCPR)"
publication: "Informatics"
issue_date: "April 2012"
pages: [12, 13, 14]
author: "DR. SHEFALI S DASH, IPS SETHI"
section: "e-GOV PRODUCTS & SERVICES"
---

## National Consumer Call Preference Registry (NCCPR)

Mobile phones were a boon which came very late to India, but the spam calls and messages came pretty quick. Not a day would pass without getting a message/call selling a credit card, insurance policy or a bank loan. Telemarketing calls are a major cause of worry not only for people in India, but across the globe. Common man life was getting difficult due to Unsolicited Commercial Communications (UCC) on mobile/landline phones, when Telecom Regulatory Authority of India (TRAI) step in and decided to set up NCCPR.
The objective of NCCPR is to curb UCC. UCC has been defined as "any message, through voice or SMS, using telecommunications service, which is transmitted for the purpose of informing about, or soliciting or promoting any commercial product or service, which a subscriber opts not to receive, but does not include any transactional message; or any messages transmitted on the directions of central Government or State Government or agencies authorized by it". The Indian telecom Industry with nearly 900 million subscribers is the second largest wireless market in the world. To holistically curb this growing menace and effectively regulate UCC, TRAI came up with the new regulation “The Telecom Commercial Communications Customer Preference Regulations, 2010" on 1st December 2010. To implement the provisions of the regulation, NCCPR has been set up by NIC for TRAI at http://nccptrai.gov.in

fEATuRES of NccpR
Telemarketer(TM) Registration: According to the new regulation every TM shall register with the TRAI and obtain a registration number for carrying out telemarketing activities. Single registration required for all the locations pertaining to a TM. The registration fee can be paid online (Net banking/Credit/Debit cards) and offline mode (DD/Cash). A separate number series 140 is allocated for telemarketing activity by Access Providers (AP) to the TM.
Telecom Customers Registration: A customer can register his/her number by calling or sending SMS at 1909. Registration with NCCPR can be for fully/partially blocking of unsolicited communication which will be effective within 7 days. Calls are fully blocked, however Subscribers can choose the type of SMS they want from the TMs by setting the preferences.
NCCPR Database: The customer data in NCCPR is updated twice a week by APs and provided online to APs/TMs for downloading so that the calling list could be scrubbed by them before making any call.
Complaint Handling: Provision has been made for Complaint monitoring and blacklisting of TMs. The APs have to upload the complaints received online so that it could be monitored for the violations and blacklist the TMs. The defaulter TMs will face disconnection of telecom service and blacklisting in case of continuous sending of UCC even after being penalized.

fuNcTioNAl coMpoNENTS of NccpR
Following diagram gives a brief view of the functional components of NCCPR.
Customer’s request for registration on the NCCPR is effected within 7 days from the date of registration with the AP.
Customer can register either in Fully Blocked category or Partially Blocked category Ex: SMS START 0 or START 1, 4, 5 to 1909.
The categories are:
1: Banking/ Insurance/ Financial products/credit cards
2: Real estate
3: Education
4: Health
5: Consumer goods and automobiles
6: Communication / Broadcasting / Entertainment/IT
7: Tourism & Leisure
Customer can change preference after 7 days.

TM REGiSTRATioN AND RESpoNSiBiliTy
Any person or legal entity engaging in the activity of Telemarketing is required to register with TRAI by paying Registration Fee - Rs 1000/- and Customer Education Fee of Rs 9000/- which could be made Online by Debit card, Credit card or Net Banking or Offline by Cash or DD.
Validity of the registration shall be 3 years unless revoked earlier.
TM shall enter into a standard agreement with the AP before applying for any telecom resources.
TM shall not send any commercial communications to any Customer whose telephone number appears on the NCCPR, except for sending SMS in respect of categories of preference opted by the customer.
The TM shall update their Customer Preference data regularly. They should scrub their calling list against the Customer Preference data before sending any SMS or telemarketing call.
No UCC to be made between 2100 Hrs to 0900 hrs irrespective of customer registration with NCPR.
The TMs can deregister themselves if they have decided to not to do any telemarketing business.

RolE of AccESS pRoViDERS (Ap)
AP shall provide toll free short code 1909 for Registration of number by customer, De-registration of number, Change of preference, Registration of complaints.
AP shall ensure that no telecom resource is provided unless TM is Registered with TRAI, signed the standard agreement with AP & Not blacklisted.
Resource allocation to TM is made under 140 series.
Maintain and upload Provider Customer Preference Register (PCPR) to NCCPR.
Keep PCPR updated by downloading incremental data from NCPR every Tuesday and Friday.
Upload the TMs who are exempted from sending more than 200 SMS on every Monday.

NccpR DATA SyNcHRoNizATioN
This module provides all functionality required to update NCCP registry. The process followed is:
System synchronizes NCCP registry on every Tuesday and Friday between 12.00 PM and 6.00 AM when the registry will not be available to the APs to upload new numbers.
The synchronized data will be available for download from 7:00 AM of Tuesday till 11:59 PM of next Thursday and from 7:00AM of Friday till 11:59 PM of next Monday.
System generates CSV files containing NCCP full registry for respective service provider and NCCP incremental data for all service providers.

ucc ViolATioN
Calls/SMS made by the TMs, not complying with the Provisions of Regulations are termed as violations.
TM violating the regulations are penalized between Rs 25000/- for first violation to Rs. 250000/- for sixth violation followed by blacklisting and de-barding the TM for 2 years.

REGiSTRATioN of ucc coMplAiNTS
Customer should register the UCC complaints within 3 days of receiving any UCC with their respective APs either by dialing or sending an SMS to 1909 as “COMP TEL NO XXXXXXXXXX; dd/mm/yy; Time in hh:mm; short description of UCC” where XXXXXXXXXX is the telephone number or header of the UCC.
Unique complaint number will be sent by the AP through SMS.
The APs update the status of complaints on the portal.
AP will inform the action taken to the customer within 7 days.

pAyMENT REcoNciliATioN
Banker uploads the file containing the details of the successful transactions (online/offline) in the pre-defined format and frequency in the NCCPR and initiates the reconciliation process.
NCCPR reconciles the payments made by the TMs for registration and APs for penalty deduction.
Bank would be intimated about unreconciled transactions.

cuSToMER QuERiES AND MiS REpoRTS
Telecom Customer can view on the portal:
TRAI Regulations
Registration status of a telephone number
List of Registered TMs
Status of Complaint registered
Guidelines for Customers, Telemarketers, Access Providers
TRAI can monitor the functioning of all the TMs and APs by various MIS reports:
Registration Details
Resource Allocation
Compliant Resolution
Delay in action taken for complaints
Notice Sent to TMs
Penalty Deduction
Payment reconciliation
Blacklisted TMs
Resource Disconnection
TM agreement with Access Provider
Audit Trial

TEcHNicAl ARcHiTEcTuRE
NCCP uses MVC architecture. Usage of this pattern isolates business logic from user interface considerations, resulting in an application where it is easier to modify either the visual appearance of the application or the underlying business rules without affecting the other components.

NccpR iNAuGuRATioN
National Consumer Call Preference Registry (NCCPR) was launched by, Hon’ble Union Minister of Communications and Information Technology Shri Kapil Sibal and Hon’ble MoS(C&IT) Shri Milind Deora and Shri Sachin Pilot on 27/09/2011. NCCPR is designed and developed by NIC for TRAI.
