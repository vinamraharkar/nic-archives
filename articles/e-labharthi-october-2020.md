---
title: "e-Labharthi"
publication: "Informatics"
issue_date: "October 2020"
pages: [29, 30]
author: "DIBAKAR RAY"
section: "eGov Products & Services"
---

## e-Labharthi

Over the last decade, various state government departments followed isolated approaches to deliver benefits with different payment procedures leading to overlap, delay, and untargeted disbursement of benefit. eLabharthi is an integrated platform for handling transactions related to various social sector schemes supporting workflow-based system includes the creation of a centralized beneficiary/ transaction database and a reporting system integrated with other external systems like bio-metric enabled identification mechanisms – Aadhaar, PFMS, etc. The database augments various business rules and processes for the management and generation of MIS reports.
e-Labharthi Portal is a step towards creating centralized Social registry of State Beneficiaries for various social protection schemes. This promotes an integrated delivery approach and expands social care services for the poor and vulnerable households, persons with disabilities, older persons & widows, students and farmers etc. It can serve as a model and provide evidence of good governance practice which could be replicated in other states. The joint effort of Govt. of Bihar and NIC is a path breaking initiative which has resulted in streamlining beneficiary payment process and bringing transparency in social delivery systems. – Dr. S SIDDARTH, IAS, Principal Secretary, Finance Department, Govt. of Bihar
Features of the Product
• Centralized beneficiary database of Social Sector Schemes
• Integration with Aadhaar Platform
• Payment Bridge with PFMS and Banking Networks
• Automated reporting and Alert Systems
• Integrated with Common Service Centre
• End to end System for Beneficiary management and Payment
Technical Specifications
• Three-tier architecture for data, application, and middleware management
• Data Analytics to identify ghost beneficiary
• Developed on .net framework and PgSql Database
• Fuzzy logic for matching names of Beneficiary and the name received from Banks
• Aadhaar and PFMS Integration for payment bridge and MSDG for SMS
• Digital Signature for Data Transfer and Signing fund transfer Application Architecture
Application Architecture
Presentation Layer: The website, accessible over the URL http://elabharthi.bih.nic.in has been developed using Microsoft’s .NET technologies with PostgreSQL. It provides various user-level accesses (role-based) which allow different categories of users to view and edit information related to beneficiaries and their payments.
Application Layer : The application layer consists of business rules to validate beneficiaries, payments, posting of payments files to PFMS, etc. The application layer provides a database abstraction layer which is leveraged for making enquiries to the database and generate various reports using open APIs.
Database Layer: The database layer is an instance of PostgreSQL which houses the data in the RDBMS model.
Reports and Views: Analytical, periodic, and exception-related MIS reports provide a detailed view of beneficiary registration, enrolment, and payments processes.
Mobile Apps: e-Labharthi Mobile app provides real-time updates to beneficiaries registered, the status of pension registration, and payout. Jeevan Pramaan for Life Certificate has also been implemented for pensioners.
Beneficiary Phonetic Matching procedure: The system uses the phonetic matching process of identifying a set of strings that are most likely to be similar in sound to a given keyword using FuzzyWuzzy, a package in python.
Software Architecture
e-Labharthi framework creates beneficiaries data and payments files for various schemes with real-time integration with PFMS and UIDAI to enable direct payments into the bank account of the beneficiaries. Field formations prepare beneficiary data and payments files after thorough verification before sending them to e-Labharthi for aggregation, verification, and final approval. As a safety measure, the scheme owner at the district/ block level, ‘locks’ the beneficiary’s data by enabling write-protection on e-Labharthi to avoid any modification at a later stage. An aggregated payment file containing payment information such as name, bank account no., IFSC, scheme code, amount due, etc. of all beneficiaries are posted to PFMS for actual remittance to the bank account of the beneficiaries.
Subsequently, reconciliation process which is also called reverse MIS, PFMS receives the status of payments, either successful or failed from the banks which are then returned to e-Labharthi for record purposes and further action, if any, to be initiated by the concerned departments.
Impact Highlights
Students: A Centralised database of approx 2.7 Crore students has been created to deliver services under 28 schemes of the education department such as Dress, Textbook, Cycle, Napkins, Scholarships, etc.
Girl Child Assistance: Mukhyamantri Kanya Utthaan Yojana, ₹ 54100 as financial help right from their birth till they graduate
Old Age Persons: Under Mukhyamantri Virudh Jan Yojana persons with ages more than 60 years and more than 80 years are paid ₹ 400 and ₹ 500 per month respectively
ICDS: 1.92 Lakhs ICDS Workers (Sevika and Sahayika) are paid a monthly honorarium and 86 Lakh Anganwadi beneficiary Poshahar amount as DBT
Flood and Drought Beneficiary: 26 Lakh flood victims of 18 flood-affected districts are paid GR amount of ₹ 6000 each with an additional amount for house damage. A sum of ₹ 3000 each as tatkal sahayata are paid to drought victims
Farmers: 23 Lakh farmers are provided crop assistance based on scientifically calculated loss through crop cutting experiments under the Fasal Sahayata Yojana
Aids Patients: About 26,000 ART Centre-registered Aids patients are paid ₹ 1500 per month
Laborer: 33.06 Lakh Labourers are being paid Medical Assistance of ₹ 3000 per year through Labour Resources Department
Way Forward
e-Labharthi platform is essentially a repository of all verified and approved beneficiaries who are eligible to receive benefits through direct transfer. As more schemes are boarded on e-Labharthi, enhances it as a complete information system. The use of the right technology to implement the various components of a social registry has transformed e-Labharthi into a high-performance platform that offers an enhanced user experience while safeguarding the extensive use of information and personal data within the platform. The expansion of e-Labharthi into a comprehensive social registry will allow it to emerge as a game-changer in electronic service delivery in the country.
