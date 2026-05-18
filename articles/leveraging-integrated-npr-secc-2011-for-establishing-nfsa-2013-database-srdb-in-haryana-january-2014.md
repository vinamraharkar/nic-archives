---
title: "LEVERAGING INTEGRATED NPR & SECC-2011 FOR ESTABLISHING NFSA 2013 DATABASE & SRDB IN HARYANA"
publication: "Informatics"
issue_date: "January 2014"
pages: [21, 22]
author: "Dilip Goyal and Neeraj Singhal"
section: "E-Gov Products and Services"
---

## LEVERAGING INTEGRATED NPR & SECC-2011 FOR ESTABLISHING NFSA 2013 DATABASE & SRDB IN HARYANA

On July 9, 2013, Government of Haryana announced implementation of National Food Security Act 2013 (NFSA 2013) from 20 August 2013 and decided to utilize provisional data of Socio Economic and Caste Survey (SECC-2011) and National Population Register (NPR-2011) on as-is-where-is basis for identification of nearly 126.49 lac eligible beneficiaries from the state population of 2.53 crore.

APPROACH
Decision to apply inclusion/exclusion criteria on SECC-NPR merged data has been taken separately for urban and rural areas. NIC Haryana was given the challenging time bound task to process the provisional data sets & to generate village/ward wise provisional lists of the priority households.

METHODOLOGY
Bharat Electronics Ltd. (BEL) conducted the SECC-2011 survey in Haryana. After completion of SECC-2011 the provisional data was loaded on National Data Centre at Delhi, along with the image files of NPR-2011. There was a requirement of merging the SECC digitized data with NPR images after converting them into digital format. Correctness of basic NPR data was to be verified by DCO Haryana, office of RGI.

The digitized NPR-2011 data was merged with SECC-2011, by BEL, using a 29 character AHL-TIN (Abridged Household List - Transaction Identification Number) as common key. AHL-TIN composed of concatenated values of code for Schedule, State, District, Tehsil, Town, Ward, Block/Sub Block, HH # and Member #.

The merged data was uploaded on NDC server in Delhi on 7 August 2013, by BEL from NIC-Bangalore office. The processing/compilation was done at NDC and the merged provisional data was received on as-is-where-is basis for processing and applying criteria. NIC-Haryana, designed & developed necessary queries & reporting modules to generate the provisional lists.

S.No. Parameters Rural Urban
1 Type of House Hold Y Y
2 Name of Person Y Y
3 Relationship with Head of Family (Un-codified) Y Y
4 Gender Y Y
5 DoB Y Y
6 Marital Status Y Y
7 Father Name Y Y
8 Mother Name Y Y
9 Occupation Y N (Highest Education Level-codified)
10 Disability (codified) Y Y
11 House ownership/Material/ No. of rooms (codified) Y Y
12 Employment Type/Income/Tax status Y N
13 Monthly income of highest earning member Y N
14 Main source of HH income (codified) Y Y
15 Assets Ownership Y N (1,2,3) (1,2,3,4,5,6,7)
1. Refrigerator
2. Telephone
3. 2/3/4 Wheeler
4. Computer/laptop
5. Mobile
6. Air Conditioner
7. Washing Machine
16 Land Ownership (Un-irrigated/ irrigated) Y N
17 Other Assets Y N (Amenities-codified)
1. Mech. 3/4 wheeler agri equipment
2. Irrigation equipment
3. Kisan Credit Card

The criteria for urban and rural population were finalized on 10th August 2013. The voluminous data was processed, checklists were generated and ported into pdf format. Printable lists were handed over to district administration on 12th August 2013 in a meeting presided over by Chief Secretary, Haryana. The scheme was successfully launched by Hon’ble Chief Minister of Haryana on 20th August 2013 at Panipat with simultaneous launch functions held in the rest of the state.

CRITERIA APPLIED
1. Rural: Firstly, households satisfying any of following criteria were included:
• houseless HH or
• HoF disabled or
• landless agricultural labour or
• small and marginal farmers or
• headed by widow or single woman or
• occupationally vulnerable.
Then on above list, following exclusion criteria was applied:
• Income tax payee or
• own land > 5 acres or
• salaried Govt./PSU job or
• own/operate an enterprise registered with Govt. or
• own a four wheeler.

2. Urban: Only exclusion criteria were applied. Households having a four-wheeler or A/C were excluded.

Print files were displayed in all Panchayats and Wards. Claims and objections were called from residents. Additionally, an undertaking was taken from the prospective beneficiaries.

FUTURE PROSPECTS
In order to facilitate the field officials in processing of claims, a web-enabled module has been hosted. It allows quick search on various parameters and reconciles claims received. Further, software modules are under development to bridge gaps of missing mandatory Ration Cards attributes in the database. The provision of capturing UID/Aadhaar has been made in s/w modules under development. Once, Aadhaar numbers are seeded & the data attributes are verified & validated, the finalized database can be easily integrated with SRDH, leading to establishment of SRDB.

TEAM
NIC Haryana Project Team: Ghan Shyam Bansal DDG & SIO; Dilip Goyal TD; Sundeep Moudgil TD; Amit Mittal PSA; Neeraj Singhal SSA; Ramandeep SSA; Ashish Dhingra, Programmer; Sunil Kumar, Programmer
Supported by NIC-HQ & NIC-KSU: Ms. Rama Nangpal, DDG, Varinder Seth TD, Dr. Pramod Sharma PSA, NDC, Shastri IT Park, & NIC-Bangalore N/W Team.
