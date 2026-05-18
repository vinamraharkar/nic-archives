---
title: "The External Assistance Monitoring System A Network Computing Application"
publication: "Informatics"
issue_date: "July 1997"
pages: [7, 8, 9, 10, 11, 12]
author: null
section: null
---

## The External Assistance Monitoring System A Network Computing Application

INTRODUCTION The External Assistance Monitoring Information System (EAMIS) has been developed with a view to closely monitor the Externally Aided Projects. The design of EAMIS is based on the concept of network-centric computing, which exploits the potential of powerful application servers and high-speed networks, with low cost end User devices that support a rich Graphic User Interface (GUI) environment and are able to query over a network.

BACKGROUND The Government of India is one of the major recipients of assistance provided by the Asian Development Bank (ADB), the World Bank and other bilateral and multilateral agencies. This assistance plays a very important role in the development of various sectors such as Agriculture; Power; Health; Education etc. These Projects are spread all over the Country and contribute significantly to the Nation's progress. The large volume of existing aid commitments and low disbursement ratios are matters of serious concern shared by the Government of India (GOI) with the donor agencies. Besides initiating other steps to resolve the problem, the GOI felt a need for a Computer-based Information System (CBIS) which would enable a closer monitoring of approvals, sanctions, disbursement and utilization of foreign aid from different sponsoring agencies. As a result EAMIS came into existence. The Software envisages a closer monitoring of Externally Aided Projects to improve the disbursement ratio. The Computerized Rural Information Systems Project (CRISP) Group was entrusted with the responsibility to design and develop the Software based on Client/Server architecture with distributed servers over WAN.

External Assistance Monitoring Information System (EAMIS)
Client - Department of Economic Affairs (DEA), Ministry of Finance, Government of India
Users - Project Monitoring Units (PMUs) of State, Centre, DEA, Controller of Aid, Account & Audit (CAA&A) and Donor.
Funded by - Asian Development Bank and World Bank
Consultant to Sponsoring Agency - Kampsax International, A/S Jakarta, Indonesia
System Design, Document & Software Development - Regional Computer Centre Calcutta & National Informatics Centre, New Delhi

THE SOFTWARE MODULES The EAMIS consists of seven modules viz:

1. Proposal Monitoring System (PMS): The PMS module begins with the receipt of Project proposals from implementing agencies and ends with the identification of the donor followed by posting the proposals to the donor. The main Users of this module are Credit Division of Department of Economic Affairs (DEA); the State and Central Line Ministries (CLMs).

2. Statutory Approval Monitoring System (SAMS): The SAMS traces the various approvals required for the proposal and the status thereof. The main User of this module is CLM.

3. Pre-Loan Monitoring System (PLMS): The PLMS captures the various steps of the donor appraisal process and ends in signing the loan agreement. This module is also mainly used by the Credit Division of DEA.

4. Planning and Budget Formulation Monitoring System (PBFMS): The PBFMS deals with planning and budget formulation activities at the Centre and State level. The Users of this module include the CLMs, State Project Monitoring Units (PMUs) and the DEA Project Monitoring Unit as well.

5. Package Bid Monitoring System (PBMS): The PBMS monitors the activities leading to the award of contract, such as investigations, design, tender opening and closing etc., which are also known as milestones. State PMUs and CLMs are the main Users of this module.

6. Disbursement Monitoring System (DMS): The DMS commences with the details of the claims filed by the implementing authority and ends with the reimbursement of the claims. The main Users of this module are the Controller of Aid, Account & Audit (CAA&A), CLM, PMU and the State PMUs.

7. Implementation Monitoring System (IMS): The IMS captures the details of the physical progress and expenditure incurred by the project. This module is mainly used by the State PMUs and the CLMs.

These modules cover the various stages of life cycle of Externally Aided Projects, from proposal formulation to project implementation. EAMIS consists of 35 data entry forms, 25 processes and 56 output reports.

THE SALIENT FEATURES

Client/Server Architecture: EAMIS has a strong Graphic User Interface (GUI) and is based on Client/Server design to be implemented over LAN (within site) environment and is one of its own kind.

The System runtime support is provided by UNIXWARE 2.1/Oracle 7.1 at server and WINDOWS 3.1/Developer 2000.

Distributed Organization on WAN: The design is based on Client/Server architecture within a 'site' and bears a few characteristics of distributed database organization among the sites over NICNET info highway. EAMIS has the ability to automatically transmit the data to remote server over Wide Area Network (WAN) using NICNET. Hence routing and transmission of EAMIS information is not transparent to the User. Local operations are independent of transmission methodology. The operations could be carried out even if network link is down or remote server is not responding. This maintains complete site autonomy. The transmission is initiated by a background process at fixed interval of time, enabling data insertion, modification and deletion to be performed at remote site.

Graphic User Interface: EAMIS has a strong GUI. The Software is highly interactive and it not only alerts the User with proper error messages in case of any logical error but also provides directions for correct entry of the data. Clickable buttons have been provided to perform common commands such as saving the data; executing query; deleting unwanted data etc. The Software not only enables smooth navigation between various modules but also performs simple arithmetic calculations whenever required. The design and documentation confirm to IEEE Standards.

Data Security/Deletion: EAMIS provides complete security of data, on site as well as in network environment by defining Access Rights for State, CLM and DEA Users, thus preventing an unauthorized entry. One can input or update an information only if one has the privilege to do so, otherwise the data is available to the User only in display mode. The Software makes sure that the data pertaining to one State or CLM is not available to some other State or CLM. However, although the DEA can view the data pertaining to any of the States/CLMs, but can input or update only those fields for which it has the access to do so. The process of deletion of data could be initiated by the concerned site and has to be agreed by other participating sites. In case of mutual consent, the process of deletion is performed and controlled by Master Server at all the sites.

Auditing/Backup/Recovery: Site-specific auditing of all User activities are carried out upto the record level. Also, auditing can be enabled/disabled as per the User requirements. In order to maintain the data consistency among all the sites in the network, the Master Server acts as the back-up server for carrying out the back-up/recovery at any site. In case of crash/failure, site specific EAMIS database could be downloaded from Master Server over WAN through Recovery option.

IMPLEMENTATION In pilot phases, it is proposed to implement the Project in nine States and five CLM and DEA respectively. The Software Package has been successfully tested by Users from Jaipur, Calcutta and Hyderabad using NICNET Ku-band facility from respective NIC State Units. The demonstration of the Package was organised by CRISP Group with the help of respective NIC State Officials, for the Officials from Department of Economic Affairs; GOI; State Finance Directorate; National Institute of Finance Management (NIFM); Asian Development Bank (ADB) and other concerned agencies.

CONCLUSION EAMIS architecture is generic in nature and could be made suitable to similar setup to improve information availability to strengthen the planning and monitoring of various schemes. Mr. Aubrey G Newman, Project Consultant, Kampsax International A/S, Indonesia states "RCC/NIC has produced an excellent Software Package ie EAMIS. Once this is introduced and used by the various agencies utilizing External Assistance, the GOI will become more aware of the delays which may be occurring in implementing Projects and will therefore have a better understanding of what management interventions are necessary. In this way the EAMIS will contribute to the capability of the GOI in increasing the disbursement ratio and hence in enhancing the effective use of External Assistance".

FOR ANY FURTHER INFORMATION PLEASE CONTACT
CRISP Division
National Informatics Centre
3rd Floor
NIC Headquarters
New Delhi- 110003
Phone: 4360563
E-mail: crisp@hub.nic.in
