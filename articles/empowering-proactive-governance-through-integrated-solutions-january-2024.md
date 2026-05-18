---
title: "Empowering Proactive Governance through Integrated Solutions"
publication: "Informatics"
issue_date: "January 2024"
pages: [32, 33, 34]
author: "Edited by SANGEETHA MANJUNATH"
section: "eGov Products & Services"
---

## Empowering Proactive Governance through Integrated Solutions

The Government of Puducherry Union Territory is committed to provide various welfare schemes offered by both the Central and UT Governments to its citizens. Ensuring that these benefits reach the rightful recipients without any misappropriation or losses is a key priority. To achieve complete and effective coverage, the government aims to identify and address any gaps in the implementation of these schemes. While traditional methods such as officer-based models or performance rankings have been employed, they have proven inconsistent and unsustainable, necessitating a shift towards technological solutions.

The UT government welfare schemes, which often involve monthly and recurring benefits, encounter challenges in verifying beneficiaries due to the absence of dynamic data updating and validation checks. This results in complexities such as invalid Aadhaar details, incomplete data, and instances of duplicate records, creating obstacles in accurately identifying eligible beneficiaries. Furthermore, different departments maintain beneficiary data in separate formats without efficient collaboration.

UDH has established an adaptable system for validating and eliminating duplicate beneficiaries. Presently, it encompasses Puducherry’s residents and their enrolled schemes, incorporating 24 departments and 150 central and state schemes. Its scalability allows seamless integration with new schemes. The Cross-referencing feature, available to all welfare departments, streamlines beneficiary selection based on specific criteria, significantly reducing the time-consuming process of identifying eligible beneficiaries from months to just a few selections and menu clicks.

Contributors:
V. Gopi Swaminathan Sr. Technical Director & ASIO gopi.pon@nic.in
S. Arulraj Sr. Technical Director s.arulraj@nic.in
Sheik Rasheed Scientist-D sheik.rasheed@nic.in

In response to these challenges, in collaboration with NIC, the Government of Puducherry introduced the Unified Data Hub (UDH) web portal. UDH is designed to enhance public service delivery by minimising errors in beneficiary selection and creating a comprehensive and unified database encompassing all government schemes. By integrating with the Direct Benefit Transfer (DBT) system, UDH efficiently allocates resources to those genuinely in need, ensuring that welfare benefits are effectively targeted and delivered.

Process

UDH operates an efficient system for organising beneficiary data by employing online de-duplication and validation processes:

• Data Verification: Welfare departments cross-check data against UDH parameters, ensuring accuracy in district, scheme, age, and gender details while eliminating duplicated information
• Departmental Uploads: Each department adheres to UDH requirements by utilizing a designated service template to upload beneficiary data
• Validation Engine: An online validation engine scrutinises the uploaded records, distinguishing validated data and transferring it to UDH. Any erroneous records are promptly returned to the respective departments for rectification
• Unique Beneficiary Records: UDH exclusively maintains de-duplicated beneficiary data, ensuring that only unique beneficiary details are present. Summaries detailing accepted and rejected beneficiaries are available for reference

The Cross-referencing feature within UDH significantly simplifies and expedites the verification process across various departments:

• Beneficiary Verification: Departments can swiftly verify beneficiary data by applying inclusion/exclusion criteria for schemes, drastically reducing the time required for eligibility assessments
• User-Friendly Interface: An intuitive interface enables the selection of beneficiaries, criteria application, and comparison of data from different departments within UDH. This generates lists of eligible and ineligible beneficiaries, facilitating further necessary actions
• Adaptable Filtering: Criteria for filtering beneficiary data can be easily adjusted to accommodate changes in scheme details, ensuring the system remains flexible and responsive to evolving requirements

Figure: A basic overview of UDH application (What: Identification of eligible Beneficiaries for Government Welfare Schemes; How: Minimizing manual discretion, System-based, Real time Access to Concerned Officials; Objectives: Golden Data, Inclusion of Beneficiaries, Exclusion of Beneficiaries, Cross-Referencing & De-Duplication).

API Services

API services in UDH enable seamless data exchange between department databases and UDH through automated connections. Examples include:

• Verifying beneficiary details directly from a registration page
• Enhancing a Self-Care Portal for departments
• Downloading certificates from UDH to department websites

Additionally, welfare departments can automate incremental updates or deletions of data through web services, facilitating server-to-server interactions without manual intervention.

BCT integrated Certificates Generation

UDH advances paperless, faceless e-governance by offering electronic records of welfare assistance and integrating with blockchain certificates, covering:

• Beneficiary and family details
• Comprehensive list of welfare schemes utilized
• Blockchain-secured proof documents (e.g., marriage certificates, ration cards)
• Real-time beneficiary data, automatically updated through web services without manual intervention, ensuring continuous data accuracy

Quote from Dr. D. Manikandan IAS, Secretary (IT), Government of Puducherry:
“I am happy to inform you that the Uni-fied Data Hub (UDH) designed by NIC, Puducherry has been a very convenient and robust tool that has on boarded all the 23 welfare Departments and around 150 schemes implemented in the UT. These Departments are performing on-line validation, de-duplication through onboarding mechanisms in UDH. Fur-ther, the cross referencing facility has been provided to all Departments for identifying eligible beneficiaries by ap-plying inclusion and exclusion crite-ria through UDH. The Birth and Death integration with UDH has immensely benefit the Departments to update the beneficiaries details in the respective schemes. The API integration, 360 de-gree view of beneficiaries, integration of Block chained certificates and auto enrolment of pension beneficiaries are some of the visionary objectives to-wards pro-active governance.

I would like to congratulate the NIC team, Puducherry for developing such a collaborative mechanism to effec-tively identify the intended eligible beneficiaries as well as update the beneficiary de-tails and pro-viding the nec-essary trainings for on boarding all the welfare schemes.”

Technologies Used

Technologies in UDH adhere to UIDAI guidelines by utilizing Aadhar Data Vault for secure Aadhar storage, following the Aadhar security act of 2016. Beneficiary data is uploaded in JSON format and stored as documents in MongoDB. Web APIs use JSON Web Token (JWT) for authentication, enabling secure data retrieval and storage on the UDH server.

The 12-digit Aadhar numbers are transformed into 36-digit reference numbers stored in the Aadhar Data Vault, linked to 5-digit randomized UDH Codes for inter-departmental sharing and cross-referencing. Alerts and Notifications are shared across departments for necessary beneficiary updates.

Dynamic Dashboards, tailored to defined roles, empower welfare officials in effective data utilization. UDH operates as a Service (UaaS), allowing seamless onboarding and utilization for new welfare departments or schemes.

Figure: UDH Process Flow (Blockchain Technology, Online Services - web portal, On-boarding mechanism, Ration cards & Aadhaar at one place, Notify Invalid details, Schemes enrolled, Aadhaar Data Vault, Golden Records, Central Repository).

UDH Ecosystem

Though, started as a tool for Online de-duplication, validation and cross referencing, UDH has brought a major impact on the complete gamut of activities after integrating nearly 23 major welfare departments including Public distribution system, Social Welfare, Women and Child development, Fisheries, Adi-dravidar welfare as single point access. Some of its benefits are briefly listed below:

• API integration has provided instant verification of beneficiaries by welfare departments.
• Birth and Death registrations are updated from local bodies directly to UDH in turn prepare the new born child data to various welfare assistance programs. The updation of expired beneficiary details are given as alerts to welfare departments through portal for downloading and deleting the same in the respective beneficiary database of the department. The process already has saved several lakhs of rupees for the exchequer.
• 360 degree view of beneficiaries help to view the beneficiary and the household details along with welfare benefits availed by them at one place. The eligibility as well as verification mechanism has found immense benefits for quick decision making through this facility.

Figure: UDH Architecture diagram (API and Service Gateways, De-Duplication & cross reference requests, Scope & Criteria based on available parameters, Department Officers, Civil Supplies, Education, Social Welfare, Fisheries, Revenue, Labour, Health, ADW, Staging Repository, Beneficiary DB, Error Reports, Periodic Updates, Databases of Individual Departments, Unified Data Hub Reports & Dashboards, Onboarding process through DIT, Woman & Child Development, Old Age Pensioner, Aadhaar Data Vault, Ration Card Data Vault, Relevant Data, Periodic Reports, Periodic Updates, Department Officers).

Figure: UDH Ecosystem (NPCI Lookup, Welfare Departments, API Services, Unified Data Hub, Aadhaar Data Vault, UDH Code, 360° View, Self Care Portal, Block Chain).

• Aadhaar Data Vault (ADV) integration helps the UDH for the safe and secured storage of Aadhaar details by storing Aadhaar as well as generating a UDH code for equivalent reference key. By this, the footprints of Aadhaar has been reduced as well as usage for comparison of beneficiary data.
• Block chain certificates can be easily integrated with UDH with the beneficiary data to save papers for proof of documents as well as using the original documents. An electronic copy of the UDH certificate with block chained certificates will help the beneficiary to have an electronic way for availing all the welfare assistance and delivery of benefits.

Conclusion

UDH’s transformative approach enables efficient beneficiary identification based on set criteria, eradicating the need for new registrations. With its dynamic database updated through daily Web API transactions, departments can access, verify, and notify eligible beneficiaries seamlessly. Field verifications, if necessary, streamline enrollment without the hassle of extensive paperwork. SMS notifications facilitate swift benefit disbursal, empowering proactive governance for departments to access pertinent beneficiary details as needed.
