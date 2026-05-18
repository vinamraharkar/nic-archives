---
title: "Implementation of Aadhar based Public Distribution System in Jharkhand"
publication: "Informatics"
issue_date: "July 2015"
pages: [23, 24, 25]
author: "Shiwani Korah, N. Rahman"
section: "E-GOV PRODUCTS & SERVICES"
---

## Implementation of Aadhar based Public Distribution System in Jharkhand

The Food, Civil Supplies & Consumer Affairs Department, Govt. of Jharkhand decided to develop Aadhar based, web enabled - Public Distribution System (PDS) using Hand held Terminals (HHT) at the 23614 Fair Price Shops (FPS) in the state. This enables end-to-end use of ICT ranging from ration card digitization, Aadhar seeding, commodity allocation to FPS, distribution to targeted beneficiaries, generation of reports & finally displaying all the data/ statistics on the portal – http://aahar.jharkhand.gov.in, thus greatly improving efficiency, transparency, minimizing pilferages and ensuring timely distribution of ration to millions of poor people.

To achieve the objective, Food, Civil Supplies & Consumer Affairs Department, Govt. of Jharkhand in consultation with NIC identified the following milestones for achievement in the first phase of the project:
yyCard Digitization
yyAadhar Seeding
yyAadhar enabled ration distribution at FPS through HHT
yyAllocation Generation
yyPortal Development
yyGrievance Redressal System – e-Samadhan

1. CARD DIGITIZATION
The digitization of ration card of every beneficiary was started by taking filled up prescribed form from the beneficiary. Special camps were organized for this purpose at every Panchayat. The software solution was designed by NIC Jharkhand and the PDS server was installed/configured at NIC Data Centre. The data entry work (digitization) was done online from all the districts by the District Supply Office under the technical supervision of NIC District Centres. Thereafter, entered data was verified & corrected by the Supply Office. After verification, ration card was generated in passport booklet form.

2. AADHAR SEEDING
It was decided to link Aadhar number (seeding) with the respective beneficiary for subsidy and ration distribution, hence a module was added in the PDS application to facilitate beneficiaries for seeding the Aadhar in PDS database against their ration card number. Aadhar seeding was done in following ways -
yyBeneficiaries can directly seed Aadhar (UID – Unique Identification number) through http://rasf.gov.in by selecting beneficiary type - ration card. The seeded Aadhar after verification by the District Verifier gets updated in PDS database & simultaneously PDS application gets data from RASF server through web services.
yyBeneficiaries can submit their Aadhar at District Supply Office where operator enters his UID in PDS application and verifier verifies it through SRDH server using web services.
yyBeneficiaries can seed their UID at FPS using HHT provided for ration distribution. The seeded UID comes to PDS server. At the end of day it is downloaded in CSV format and uploaded in RASF server through Seeder’s Bulk Upload Module. The District Verifier verifies the UID which gets updated in PDS database. Till date, around 7,99,070 UIDs have been seeded.

3. AADHAR BASED RATION DISTRIBUTION AT FPS THROUGH HHT
The module was first inaugurated in Ormanhji block of Ranchi district as a pilot project by the then Hon’ble Chief Minister. The beneficiaries are given ration after biometric authentication from Aadhar Server through HHT. After successful implementation in Ormanji block, it was rolled out in the remaining blocks of the district and Govindpur block of Dhanbad district. By 15th Jan, 2015 all FPS of Ranchi district were automated with HHT. Other districts are in the process to implement the application as Aadhar seeding and mobile seeding of dealers and beneficiaries is the mandatory criteria. The feature of transaction through OTP has been included as a fallback system. One can see the transaction report at http://aahar.jharkhand.gov.in.

4. ALLOCATION GENERATION
Department at state level declares the monthly policy of ration distribution and fixes scheme wise entitlement/ quota for each district. Thereafter, DSO (District Supply Officer) generates the dealer wise allocation. Once the allocation is frozen, the dealer gets the information of ration allocation through SMS. On the basis of SMS, dealer deposits the amount in the bank. This process has minimized the delay in communication from district to dealers. Dealers can also get their allocation details from the PDS portal.

5. PORTAL DEVELOPMENT (http://aahar.jharkhand.gov.in)
Dynamic and real time PDS portal, designed by NIC, provides all necessary information to beneficiaries, dealers, department and the public. Anyone can see the Distribution Policy declared by the department, different stakeholders, HHT status, dealers login status in HHT, transaction done by dealers, digitization progress & Aadhar seeding etc. Name Search facility has been provided to the beneficiary to search his ration card. Beneficiaries can know their entitlement, ration lifting status, dealer’s information etc. through the portal, making it fully transparent & highly informative. All the reports can be drilled down up to the village level.

6. GRIEVANCE REDRESSAL SYSTEM (e-SAMADHAN)
It is linked with PDS application. The stakeholders as well as public can raise their complaints to the competent authority for redressal.

TECHNOLOGIES USED
Various technologies used to develop the system are:
yyOpen Source based application in Java, J2EE
yyArchitecture - MVC III
yyFramework – Cakephp 1.3
yyOS – Ubuntu, Centos, Redhat
yyVirtualization – Proxmox, VMware, Oracle VM
yyDatabase – Mysql 5.5 (size 250 GB approx)
yyLoad balancer – Haproxy, apache reverse proxy, Mysql proxy
yySearch Engine – Apache Solr
yyProject Management Tool – Readmine
yyReport Management Tool – SpagoBI
yySMS Gateway – C-DAC
yyWeb caching server – varnish, APC
yyWeb server – Apache
yyApplication Server – Apache tomcat

MAJOR BENEFITS
yyThe system is available 24 X 7.
yyThe new system has removed invalid and duplicate ration cards.
yyEach beneficiary is authenticated through UID and biometric, ensuring ration is provided to only genuine beneficiaries.
yyDepartment/district & block level officials are able to monitor the complete process of ration allocation & distribution.
yyThe system enables ration card search based on name within the district.
yyMIS dashboard has been created – to analyze and monitor the ration card digitization, transaction through HHT, UID seeding, mobile seeding, State Distribution Policy, dealers login activity and transactions done by dealers.
yyAnyone can view the details of card holders, dealers, HHT tagging, dealer’s activity, allocation status, etc.
yyRe-designed ration card format with additional fields and categories as per the National Food Security Act (NFSA) guidelines
yyPrinting of new ration cards in passport booklet form at state level
yyAutomatic mobile seeding and Aadhar seeding of family members based on UID details
yyCentralized web enabled application for all stakeholders of PDS

For further information:
SHIWANI KORAH
Principal Systems Analyst
NIC, Jharkhand State Centre
E-mail: shiwani.korah@nic.in
