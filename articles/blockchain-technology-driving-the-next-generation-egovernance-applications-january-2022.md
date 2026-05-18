---
title: "Blockchain Technology Driving the Next Generation eGovernance Applications"
publication: "Informatics"
issue_date: "January 2022"
pages: [13, 14, 15, 16, 17, 18, 19, 20]
author: null
section: "In Focus"
---

## Blockchain Technology Driving the Next Generation eGovernance Applications

Blockchain technology has drawn significant attention from the Government due to the pain areas that it promises to address. Several schemes of the Government require the verification of the documents / facts to ensure the eligibility of the applicant. This is a time consuming process. Although some of the departments use the electronic data available with other agencies to verify the applicant’s claim electronically, the lack of confidence that the data has not been tampered has set the Government to look at alternatives such as blockchain. The menace caused by spurious drugs, liquor, contaminated blood etc. has cost the life of many a citizen. Tracking and tracing the source of various commodities such as medicines, seeds, organic products is now vital to providing better services to the citizens. Blockchain Technology provides the necessary impetus to move towards an intermediary-less system by providing a single source of truth and ensuing that the data is secure and tamper-proof.

This article provides details of the use-cases developed and deployed that have benefitted from Blockchain Technology.

Blockchain is a distributed system that deploys a peer-to-peer network of computes / nodes. All the nodes verify the transactions submitted to network and agree upon a set of the transactions (block) to be stored in the ledger (database). Each block of transaction is linked to the previous block cryptographically. All nodes maintain the same copy of the ledger. It is not possible to delete or overwrite any transaction once it is committed to the ledger.

Typical categories of applications that can benefit from blockchain implementations are Identities, Registries, Supply Chain, Licenses and permits. Specifically, applications related to issue of certificates like caste, income, birth, death, Surviving Family Members, Land Records, Driving License etc. and Supply Chain category of applications such as Drug Logistics, State Excise Supply Chain, Blood chain, Agricultural Commodities supply etc.

Blockchain Technology is a game changer in the way eGovernance solutions are conceptualised and implemented. Karnataka Government is working closely with the National Informatics Centre to leverage the adoption of this technology. The first BCT system, known as ‘CertChain’ system, has been developed and implemented by storing about 1.1 Crore mark-sheets of class X and Class XII students of past 7 years and this is going to reduce the time taken for document verification. This system is enhanced to capture the certificates of the various departments to build a repository of certificates issued such as caste, income, birth, death, ration card, agriculturist, domicile etc. These repositories will pave the way for easier verification of certificates by citizens and organisations and enable entitlement based service delivery targeting the eligible citizens. The Government is also working with NIC to build ‘LandChain’ to store land and property details that will provide immutable and trustworthy data to all stakeholders.
P. RAVI KUMAR I.A.S Chief Secretary Government of Karnataka

Centre of Excellence in Blockchain Technology
The decision makers in the Government are enthusiastic about adopting emerging technologies. However, the non-availability of sufficient experts in, the field, high cost of setting up and management of blockchain networks have been deterrents in its large scale adoption. Considering the above challenges, the Centre of Excellence in Blockchain technology was set up by NIC at Bengaluru. The CoE provides a platform that the Government departments can look for consultancy, capacity building and as an incubation centre where they can perform PoCs, evaluate different platforms etc. and migrate to production with confidence.

Activities of the CoE-BCT
The CoE has been exploring various Blockchain Frameworks to enable blockchain powered eGovernance applications. The CoE has deployed Hyperledger Sawtooth/ Fabric blockchain networks with nodes in different NIC cloud infrastructure across data centres. Blockchain network has been established with nodes located in NIC Mini Cloud infrastructure in Bengaluru, Pune, Jaipur, Delhi and Hyderabad. The Ministry of Electronics and Information Technology (MeitY) has funded the “Design and Development of Unified Blockchain Framework (UBF)”. The project is being executed in collaboration with Centre for Development of Advanced Computing (C-DAC), Indian Institute of Technology Hyderabad, Institute for Development and Research in Banking Transactions (IDRBT), Society for Electronic Transactions and Security (SETS) etc. NIC’s role in the project is to provide Blockchain As A Service. As part of this project, Hyper Converged Infrastructure is proposed to be established in Hyderabad, Bhubaneshwar and Pune. The infrastructure will be used to set up Kubernetes Clusters and UBF will be deployed over this. Development of blockchain related software modules such as smart contracts, APIs for interfacing with the eGoverance applications has been done. Organising user awareness workshops, Technical sessions on blockchain, deliberating with NIC officers handling various sectors for evangelizing the use of Blockchain are other activities performed by the CoE.

Solution Architecture
The blockchain implementation in the eGovernance applications will ensure that the existing applications continue to function as per the business logic presently adopted. At critical stages in the workflow of the application or at stages when the information needs to be stored in the blockchain, these applications will submit data to blockchain or fetch data from the blockchain through the APIs. The APIs in turn will submit/ retrieve the data to/ from the blockchain ledger. Smart contracts/ chain code will be executed by the Blockchain platform before the data is written to the ledger. To ensure non-repudiation of the data being sent to the blockchain, the data is to be digitally signed by the authority who issues the documents or updates the data.

The data submitted to the blockchain will be stored in the off-chain database and the hash of the data is stored in the ledger. The off-chain database can be any conventional database. Postgres RDBMS is used to store the off-chain data. When the data is retrieved from the blockchain system, the hash of the data from the off-chain database is compared with the hash retrieved from the ledger to confirm if data has not been tampered in the off-chain database.

Blockchain Use Cases
Two categories of applications that benefit from the use of Blockchain were identified for implementation – Document Repository and Track and Trace System.

Certificate Chain (A Blockchain Powered for certificates)
Several certificates issued by the government are essential for the citizens, especially for - claiming benefits of various social welfare schemes, employment, legal purposes and admission to educational institutions. These documents need to be stored safely and produced on demand to the authorities. Most of these documents are issued to citizens in a paper-based format even though the data is stored electronically.

Challenges in the current system
Fake documents
With the improvement in the technologies and internet, the generation of fake certificates has become even more rampant and is exploited by unscrupulous elements of society. Many times these fake certificates can have a detrimental effect on the government exchequer and, more so, deprive the benefits to genuine beneficiaries.

Enhanced paperwork
The process of obtaining a duplicate certificate involves a lot of paperwork, right from lodging a complaint with police, filling up a request for a duplicate certificate, payment of fees, and of course, waiting for the concerned authority to retrieve the certificate from the record room and issue the duplicate certificate.

Cost of printing and storage
The cost of paper and printing itself are not the only items of expenditure related to documents received upon completing education. Major institutions and schools spend enormous amounts of time and money on storing these documents.

Delay in verification
Ascertaining the authenticity of certificates issued by issuing institutions has become a major cause of concern these days due to the prevalence of malpractices like fraud and misrepresentation of records. Manual verification of documents is a lengthy process that could be as simple as examining the original document produced by the applicant or as complex as sending the document to the issuer to ascertain if the document was indeed issued by that person.

Data can be changed, hacked, or lost due to natural disasters
With data being stored in a centralized location, there are chances of the data being tampered in addition to be a single point of failure. The loss and damage to documents in education is quite a common basis for litigation, which results in financial costs and wasted time.

Need for carrying original certificates to verify the authenticity
The students need to produce the original documents to various authorities for higher studies/ employment etc. Loss or damage to these documents during travel is a cause for concern.

To circumvent the above problems associated with paper-based documents, National Informatics Centre (NIC) has proposed blockchain technology for secured storage and retrieval of such certificates. It has developed the blockchain technology-based solution called Certificate Chain which can be used explicitly for storing documents in the digital format. The Certificate Chain ensures that the Certificates are recorded securely, tamper-proof, and easily traceable. The main advantage of this Certificate Chain system is that the Certificate could be accessed online by any authorised person/ institution and be assured that it is genuine and not tampered – all this without the need for an intermediary. This provides the necessary trust to the agencies which use these documents to ascertain the eligibility for providing benefit to the citizens.

In pursuit to achieve Digital Excellence, IT Dept. of CBSE implemented yet another “Emerging Technology”, i.e. “Blockchain” for its results and academic documents in technical collaboration with Centre of Excellence in Block-Chain Technology, National Informatics Centre. This system has been named as “Academic {BlockChain} Documents (ABCD). The Academic {Block-Chain} Documents (ABCD) ensures that Academic documents are recorded in secured, tamper-proof and transparent manner. Blockchain maintains the history of changes to the documents as well. The platform thus eliminates the challenges with respect to non-availability of instant Academic documents and lengthy process of verification of these documents. CBSE is happy to have partnered with CoE {Blockchain Technology}, NIC which is a pioneer in the country to provide such a system.
Dr. ANTRIKSH JOHRI Director (IT & Project), CBSE

Benefits of blockchain implementation
• Transparent
• Tamper-proof
• Paperless
• Intermediary free.
• Trail of the certificates is available

Verification Methodologies
The retrieval process of certificates from the Certificate chain system can be enabled by multiple methods. Web portal for verification enables verification of certificates one-by-one or in bulk mode. In addition the API will help two IT systems to exchange data in machine readable form and internally use the data thus retrieved.

Verification By Citizens
Citizens can verify the Certificates by going into the Web portal. Verification by the citizens could be carried out using different methods – Based on document details or based on Certificate ID (A unique ID for the certificate in the blockchain).

Verification by Organisations
As a first step, the organisations need to register to avail the service. The department or organisation can carry out verification in following ways
• One-by-one verification on the portal : The orgnaisation can enter the details of the certificate such as the document type and the ID and the details will be displayed.
• Bulk Verification : The organisation can upload a list of certificate IDs for which the document details are required to be verified. The portal will retrieve the Certificate details from the blockchain and prepare a file that can be downloaded by the organisation.
• API to integrate with the line of business application : The organisation can use APIs to fetch the data from the Certificate chain and integrate it with their application so that the logic for automatic verification can be built. This will help to automate their process of verification.

Certificate chain has been implemented for Central Board of Secondary Education and the Karnataka State Education Board for storing the marks sheets of students of class X and class XII

Karnataka State Education Board
1.4 Cr Marks-sheet ( 2015 onwards)

Central Board of Secondary Education
1 Cr Marks-sheet ( 2019 onwards)

Certificate Chain as a service
A Generic certificate chain service has been deployed and a portal for on-boarding of the stakeholders has been developed. The two main stakeholder categories include Certificate Providers and Certificate Verifiers. The system is flexible enough to enable the Certificate providers to self-register and indicate the documents to be stored in the blockchain and submit the underlying schema of the documents. The providers can also list the data items to be displayed to the verifiers and provide bi-lingual content. This provides a common platform for the verifiers to verify documents submitted by candidates across the country using the same interface rather than going to multiple portals.

The Certificate providers can then submit the certificates to the blockchain in bulk or the individual transaction can also be submitted. The CoE provides the APIs which can be consumed by the Certificate providers to send data to the blockchain and receive the transaction ID as response, which can be stored in the provider’s database as a reference.

The Aushda system has been enriched by integrating it with Blockchain platform with the support provided by NIC. Karnataka Drug Logistics department is one of the first in the country to have leveraged the benefits of blockchain technology in Supply Chain. Availability of tamper proof information about the medicines in the complete chain gives all stakeholders the option to verify the authenticity of the origin of the medicine and other critical information such as quality of the drug and expiry date etc which is critical to ensure supply of quality medicine to patients.
K.S. LATHAKUMARI, I.A.S Director Karnataka State Medical Supplies Corporation Ltd.

The Certificate verifiers can also self-register in the portal and use the portal for verification of individual certificates or a batch of certificates.

Drug Logistics Chain (Aushada) (A Supply chain system for procurement and issue of medicines to Government Hospitals)
The supply of drugs to the Government hospitals involves the procurement of drugs from the Manufacturers and ensuring its transportation to the designated warehouses located in different districts and facilitating the supply to hospitals periodically. The patients are supplied these drugs on prescription by the doctors.

Specifically, the Government of Karnataka procures and supplies free drugs for patients across the state to enable them to get treatment on time without any shortage of drugs. Around 2,911 hospitals are covered under this scheme and every year more than Rs. 300 crores worth of medicine is procured and supplied to these hospitals through 26 Warehouses.

Challenges
Visibility
Lack of visibility raises issues like counterfeits, drug shortages - Patients, retailers and regulators don’t know where drugs have originated. The consumer has no way of ascertaining the genuineness of the drug, its manufacturer, the quality and date of expiry which lends itself to entry of spurious drugs into the system.

Difficulty in tracking and tracing
The stakeholders of the supply chain maintain their own ledgers that are not accessible to others. This results in low visibility in tracing and tracking the drugs in the complete supply chain. It is a cumbersome process to collect the data required to produce the history of all the transactions made so far leading back to the manufacturer.

Regulatory compliance
Compliance with regulations under the Drug Supply Chain laws involves lengthy paperwork and substantial time.

Cold-chain shipping
Storing the essential information related to cold-chain shipping in centralized databases can be prone to manipulations or data hacks.

Recalling
Inability of Procurement manager to trace the medicines that are ‘not of standard’ or that are going to expire at various locations in the supply chain.

Theft
Theft of medicine in the supply chain and replacing them with counterfeit medicine is risky to the patient

Blockchain implementation in Aushada
Drug Supply Blockchain system is integrated with the existing online Supply Chain Management System (Aushada) to record the transactions in the blockchain. In the current version of implementation, the purchase order details, the inward of the drugs at the warehouse, the details of the drugs sent to the hospital, the inward entry at each hospital and issue of drug from the hospital store are recorded in the blockchain.

In addition, the details of the drugs sent to the laboratories for the quality check and the results of the quality checks are recorded. Smart contracts put in the checks and balances at each stage in the supply chain and also ensure that non-standard drugs are not moved down the supply chain. While the Aushada system implements these business logic, the blockchain provides the Aushada system a platform that gives immutability, provenance and finality to the data stored in the blockchain. Events such as recording the result of the quality check can result in “freezing” the drug and recalling them to ensure that non-standard drugs are not issued to the patients.

60 lakhs transactions of the last 2 years are available in the blockchain.

Benefits
• Patient can check the manufacturer details, expiry details & quality of the medicine before consumption.
• The Blockchain technology allows for documenting the transactions in a decentralized manner. It enhances precision and brings transparency at the same time saving crucial resources like time, cost and efforts.
• It not only results in integrated supply chain information but also maintains traceability of the transactions.
• Blockchain technology also facilitates tracking the movement of drugs from producer to the patient and reduces the chances of entry of counterfeit medicine in the supply chain.

Remote Voting
The remote voting system is blockchain-based distributed system developed to enable migrants and other in-service voters posted at different locations to cast their votes in a secure and tamper-proof way. Migrants and other in-service personnel can cast their votes from their place of work (Host Constituency) without commuting to their Parent constituencies, thereby saving time and money and enabling higher voter turnout. A Proof of Concept(PoC) was demonstrated to the Election Commission of India.

Process of Remote Voting
The remote voting process involves 3 main stages:
Pre-poll activities
Voters desirous of availing remote voting, register themselves in the ECI portal & after approval by the returning officer of the parent constituency, the details of the voter and the host constituency are stored in the distributed ledger. Preparation of ballot by the Returning Officer of the parent constituency and submitting the same to the distributed ledger is carried out.

Poll day activities
The voter would present himself/ herself at the Host polling station and identification and verification of the remote voter details is done by the presiding officer of the Host constituency. After verifying the details in the remote voter slip with the data retrieved from the blockchain, the officer allows the voter to cast the vote. Casting of the ballot by the voter and storage in the distributed ledger are carried out in a secured manner by storing the encrypted vote in the blockchain. The encryption is carried out using the public key of the Returning Officer (RO) of the Parent Constituency.

Counting day activities
On the day of counting in the parent constituency, the RO downloads the encrypted votes for that constituency, decrypts the same using his private key and counting of votes would be performed.

The CoE-BCT at Bengaluru has established Blockchain networks with nodes across the Country to accelerate adoption of Blockchain in eGovernance applications. The implementation of Certificate chain for certificates of class X and XII for Central Board of Secondary Education and Karnataka Education Board and Drug Logistics Supply chain for Govt. of Karnataka has provided the necessary impetus for pan India roll-out. The Generic Certificate Chain Platform has been established to bring together the producers and consumers of certificates. This solution will enable easy on-boarding of various Central & State Government Departments to build a repository of immutable certificates issued to citizens. This repository can be leveraged by various Government Departments and other agencies such as employers, financial institutions etc. to access immutable certificates and take the G2C & B2C Service delivery to the next level.
NAGESH SHASTRI Dy. Director General, NIC

The way forward
Land being a very important asset, prospective buyers need to ensure the ownership details before any purchase. Property disputes constitute a significant chunk of cases filed in various courts in the country. The CoE is working on designing a system for building a land chain consisting of a distributed ledger of land parcels/ urban property and maintaining all the transactions on the land. This will facilitate all the stakeholders such as Revenue, Registration departments, banks, judiciary and citizen to get access to the authentic and tamper-proof details of the land.

While the Government departments have been able to maintain electronic records of the assets, medical records, benefits received, there is a need felt for implementing a consent mechanism to the owners of the data so that data is shared with only those agencies which the owner approves of. It is also proposed to integrate the consent management system developed by NIC, Karnataka with Blockchain to store the consent in a tamper-proof system.

P.V. Bhat Dy. Director General & SIO bhat.pv@nic.in
Jayanthi. S Dy. Director General s.jayanthi@nic.in
T. Pechimuthu Sr. Technical Director tpmuthu@nic.in

Contact for more details
State Informatics Officer NIC Karnataka State Office 7th Floor, Visveswaraya Centre (Mini Tower) Dr. Ambedkar Veedhi, Rajbhavan road Bengaluru, Karnataka 560 001 Email: sio-kar@nic.in, Phone: 080-22863790
