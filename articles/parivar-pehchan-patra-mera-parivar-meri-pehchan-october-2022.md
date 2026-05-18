---
title: "Parivar Pehchan Patra - Mera Parivar Meri Pehchan"
publication: "Informatics"
issue_date: "October 2022"
pages: [18, 19, 20]
author: "Mukesh Kumar Ralli"
section: "eGov Products & Services"
---

## Parivar Pehchan Patra - Mera Parivar Meri Pehchan

Most government services and initiatives are provided to the populace in accordance with metrics related to their families, communities, and economies. There is no other method to determine how many family members are receiving benefits and how many are being left out if different departments extend benefits to different individuals. Parivar Pehchan Patra was designed with this fundamental idea in mind. All families and households residing in the state of Haryana are included in a dynamic database that was developed on the Hon’ble Chief Minister’s behest.

Parivar Pehchan Patra is an 8-digit unique alphanumeric number assigned to each family / household across the state of Haryana. Presently, 71.26 lakh families consisting of 2.81 crore members have been enrolled in the Family Identity Data Repository. The demographic details along with socio-economic details such as Name, Head of the Family, Parent’s Name, Date of Birth, Caste, Divyangta Status, Address, Annual Income, Land holdings are taken for each individual.

The Family Identity Data Repository #(FIDR) database assigns each family a personalized eight-digit alphanumeric number called a PPP. As of September 20, 2022, 2.81 crore families containing 71.26 lakh individuals had enrolled with FIDR. Each person’s demographic and socioeconomic details, including Name, Father’s Name, Mother’s Name, Date of Birth (DoB), Caste, Divyangta Status, Address, Annual Income, and Individual Land Holdings, is captured while creating the FIDR database. (Refer Fig. 6.1 & 6.2)

Overview
PPP helps in compiling a reliable and verifiable data set of each and every family or home in the State. It stores the family’s basic information, provided with the family’s consent, in a digital format that is linked to the records of births, deaths, and marriages to ensure that data is updated automatically when such events occur. In order to guarantee consistency and reliability, it is also linked to existing data from independent schemes, enabling the automatic selection of beneficiaries for different programs. Therefore, after creating a PPP, families are no longer required to complete paperwork and make separate scheme applications.

Implementation Strategy
Consent-based registrations for PPP started in August 2019, but the reception was underwhelming. It was then decided to implement a programme that would reward people for enrolling.
Mukhyamantri Parivar Samriddhi Yojana scheme was introduced in January 2020 and guarantees each registered household a financial help of Rs. 6,000, inclusive of insurance payments.
A door-to-door survey was conducted in April 2020 during COVID-19 to collect information from residents who required help.
A door-to-door survey was conducted in April 2020 during COVID-19 to collect information from residents who required help.
Social Security Pension Scheme was merged with PPP in June 2020, and as a result, all citizen- centric services were also integrated. That gave PPP a huge boost, and citizens began to show up on their own.
Birth / Death and Marriage data have been integrated with this site to maintain the dynamic nature of the data. The Registrar General of India pushes daily data of Births and Deaths registered in the State to the Government of Haryana.

Verification
Since the data provided is self-declared by the citizens, in order to provide services, the data is electronically verified to the greatest extent possible, and if necessary, the residual data is sent for field verification. Following are the sources used for electronic verification:
• Central Board of Direct Taxes (CBDT) Income Tax Return (ITR) data for Income Range Validation
• HRMS (Human Resource Management System)/
Contractual Employees / Government Pensioners
• EPFO for Private Sector Employees

Physical Verification
For a gathering of 250–300 households’ worth of residual data that wasn’t electronically checked, a Local Committee (LC) was formed. An LC consists of a state government employee, a local data entry operator, a social worker, a volunteer, and a student. A mobile app was also enabled, where each LC member could enter specific information regarding each individual family member during door-to-door visits.
The mobile app is geo-fenced to ensure accurate data collection. A backend algorithm calculates a family’s income range on the basis of field-collected data. (Refer Fig. 6.3)

Technologies Used
PPP is hosted at NIC State Mini Cloud and uses NIC Aadhaar Data Vault for safeguarding Aadhaar and other related data. Besides, it uses following technologies
• .Net Model View Controller (MVC) 4.5 framework for development
• MS SQL for backend
• HTML / jQuery / JavaScript used for front-end
• UIDAI database for demographic authentication and eKYC
• NIC Aadhaar Data Vault for storing Aadhaar data

Benefits
PPP has been integrated with SARAL portal, which hosts over 400 citizen-centric services from 60 State Government Departments. It eliminates the need of carrying several doc- uments to the government office to avail of the benefits of a government scheme. With the PPP, the process will be made much easier and more efficient.
This has resulted in 65 lakh PPP integrated SARAL transactions.
In addition, it offers following key benefits
• Pro-active service delivery
• Traces entitlements of families
• Weeds out ineligible beneficiaries
• Eliminates deduplication
• Integrated and continuously updated database
• Single source of truthing
• Service provision on validated data in FIDR
• Data enrichment with existing database, for example DoB is verified from school admissions
• Service provision on validated data in FIDR

Impact
• Old age pension is being proactively disbursed to the eligible citizens whose DoB and Income has been verified
• Caste verification has been done in advance, allowing citizens to generate SC and BC Certificate on the fly through SARAL portal
• Benefits of Mukhyamantri Vivah Shagun Yojna are delivered at time of Marriage Registration

Legal Framework
PPP is administered by the Haryana Parivar Pehchan Authority, which draws its power from the Haryana Parivar Pehchan Act, 2021.
The Act was passed in the Haryana Vidhan Sabha in August 2021 and later notified after assent in September 2021.

Way Forward
After looking at the success of PPP, the Prime Minister’s Office invited the Government of Haryana and NIC Haryana State Centre to look at the feasibility of a nationwide rollout. Various State Governments such as Punjab, Himachal Pradesh, Bihar, Jharkhand, Manipur, Goa, and Maharashtra have shown a keen interest in the same. Furthermore, the source code has been shared with NIC Bihar to replicate the project in the State of Bihar.
