---
title: "Data Centre: Building Blocks"
publication: "Informatics"
issue_date: "October 2008"
pages: [33, 34, 35]
author: "Neeta Verma"
section: "Technology Update"
---

## Data Centre: Building Blocks

Data Centres lie at the core of e-governance infrastructure. They provide controlled physical environment with appropriate security measures to house ICT infrastructure to store & deliver Government information, Critical governance applications as well as facilitate electronic delivery of Citizen Services.

Data centre strategy is one of the key components of any e-governance initiative concerning delivery of services. Citizens, Business as well as Government itself depend heavily on the information & services housed in the data centre to interact, transact, participate in governance

Lot of initiatives are being taken by government at various levels to build data centres. Data Centre are being set up to in generic mode to facilitate delivery of wide range of government services. Some of the major projects involving nationwide delivery of service are also building special purpose data centres to cater to a specific application or services.

Besides Servers & Software, Data Centres (DCs) house a lot of associated infrastructure, together which make the Data Centre function in Reliable, Available & Secure (RAS) mode. At a broad level DCs comprises of four major components viz. Physical Infrastructure, ICT Infrastructure, People & Processes

Physical Infrastructure

Physical infrastructure consists of Server Room, Power, Cooling, Fire Detection, Suppression and Physical Security Systems. Informatics July 2007 discusses in detail about the physical infrastructure.

However, due to increased density of ICT equipment, shrinking foot print, multi-core CPUs there has been a paradigm shift in the way data centres are designed & planned for future growth. The traditional wisdom for designing data centers has been towards design for long term with adequate floor space, power and cooling capacity for growth. This led to the creation of data centers that were often larger than needed initially and also over provisioned for power and cooling.

Newer philosophy is towards modular approach even while building data centre. Energise only as much space with Power, UPS, Chillers and Generators, as is required in near future, however, plan for long term requirement and make basic minimum provisions for the same in place to avoid disruption of services during upgrade. This approach shall not only result in cost saving but shall also enable you to leverage on newer & more energy efficient power and cooling equipment during upgrades.
Due to increase power requirements of data centre with associated cooling loads there has been a shift in Power &

In-Row Cooling

As power and cooling requirements within a rack rise, it becomes increasingly difficult to deliver a consistent stream of cool air to the intakes of all the servers when relying on airflow from vented floor tiles. In-row cooling architecture focuses on heat removal and eliminates the concern of proper cold air distribution from floor tiles. By placing the cooling equipment in the row, the heat is captured and neutralized before mixing in the room. To further improve the efficiency and predictability of an in- row system, either rack or row-based containment systems can be added.

Neeta Verma
Senior Technical Director
neeta@nic.in

Cooling Technologies deployed in the Data Centres. Emphasis is on Modular, Scalable UPS systems to In-row cooling; Liquid based cooling to Intelligent Infrastructure etc.

Besides there has been a lot of concern on increasing the energy efficiency of DCs to reduce energy consumption as well as reduce environment impact.

There has also been concern over environmental impact of use of FM 200, so far most commonly used as fire suppressant gas in data centres. Being a halocarbon agent, it's considered to have some ozone depletion potential. Now a day, use of combination of inert atmospheric gases such as Inergen, Argonite etc is being recommended. As far as Physical Security to data Centres is concerned, besides choosing a strategically secure location for the data centre, Smart card based access to Data centre with Biometric identification for access to sensitive areas is suggested.

ICT Infrastructure

ICT infrastructure consists of Compute, Storage & Network Infrastructure.

Architectural view of ICT Infrastructure in DC

Compute Infrastructure

Servers are at the core of Data Centre infrastructure. Data Centre servers run on 24x7x365 basis with very little time for any maintenance. They should be fault tolerant machines with a lot of redundancy in its components to give high reliability & performance.

However it's not necessary to buy the latest and most powerful machines for all applications. There is a need to size the server configurations based on the application/ purpose it shall be used for. Server performance benchmarks are a good tool to size the servers.

Computer Benchmarks

A computer benchmark is a set of programs that perform predefined operations on a system & returns back the capability of the tested Configuration. Different benchmarks are defined for different applications. Some of the international organizations such as SPEC (http://www.spec.org) , TPC (http://www.tpc.org), Linpack (http://www.netlib.org/linpack) regularly publish benchmarks for different configuration of servers from different manufacturers.

During the last 4-5 years, lot of development have taken place in compute technology such as blade servers, multi core CPUs etc. All these initiatives are packing more & more processing capacity in the same or smaller form factor. Quad Core, Dual Processor system with 16 GB RAM can be packed in a server of 1U form Factor. 10-16 dual Processors, multi core blades can be fitted into an 8U chassis with integrated network. This has also increased the cooling requirements of Data Centres enormously. Not only one is needed to increase the cooling capacity, one is also needed to deploy alternate cooling techniques.

Consolidation of multiple applications on single machine is another way to optimize Compute infrastructure in DC. However at times due to different configuration requirements of different applications as well as administrative controls, its not possible to consolidate beyond a certain point. Virtualization of servers becomes quite useful in such a scenario whereby one can install number of independent virtual machines on a single physical machine. This is becoming more and more relevant with exponential growth in processing power as well as throughput of the new servers.

Consolidation & Virtualization also help in reducing the power, cooling as well as space requirements in data centre and at the same time enhancing the energy efficiency of Data Centre.

Storage Infrastructure

Storage space requirement is growing at an exponential rate. Server Centric Storage solution becomes a big constraint in such scenario. Besides scalability of storage, availability & performance are also major concerns in such a approach. Dedicated storage network is a common approach and today along with TCP/IP network, Storage Network forms a core of ICT Infrastructure in Data Centre. Different Storage technologies are used for different setups with NAS & SAN being the most common. In Network Attached Storage (NAS), a set of servers access the storage over the existing TCP/IP network. In the case of Storage Area Network (SAN), servers are connected via Fibre channel (FC) switches to storage devices. SANs are easy to manage, flexible, reliable & scalable. In SAN, however all Servers must be equipped with FC adapters. As the Data Centre grows, one may have multiple Storage systems in the Data Centre. To effectively manage & efficiently utilize these expensive resources, one can consider Storage Virtualization as well.

Network Layer

Network Architecture is fundamental to the success of Data Centre & its services. With the advent of WWW & Internet access, lot of critical applications has also been delivered through the net. Therefore its not only the availability to network, but equally important are quality of access, performance & Security over network. Data Centre networks should be fault tolerant with no single point of failure & should be designed with scalability, interoperability & flexibility in mind. Design should be agile enough to accommodate varying requirement of variety of applications hosted or to be hosted in DC, such as N-tier Application Architecture, Web Applications, HPC/Grid computing, Blade Servers etc. as well demands of virtualization & consolidation of DC infrastructure.

Network layout in Data Centre

Data Centre Network comprises of multiple Switches at Rack level aggregating to core switch which then passes through multilayer security infrastructure to finally connect to outside world through a gateway router. Below placed diagram clearly highlights the interconnection of various components in DC network. Besides application specific devices are also deployed in the network such as Load Balancers, Content Switching/ Caching, SSL, WAM Accelerators etc.

Security infrastructure is another important component. With increasing nature of threats varied in nature, multi layer security techniques are deployed. Firewalls are a first level of protection in Data Centres. Generally data centres are divided into multiple zones of security and firewalls are placed between these zones and different set of rules are defined on movement of traffic among these zones. Firewalls are not sufficient to mitigate all types of network threats. Therefore divices such Intrusion Selection & Intrusion Preventions Systems are position in the network which examine the traffic passing through the network and based on predefined policy raise alerts or deny access to spurious or suspicious traffic. Application Firewall are another level of defense to protect from application level attacks. Above infrastructure with right kind of policies for servers & services provides desired security in data centre.

We shall discuss about the Operations & Management of the Data Centre in the next issue of Informatics.

We would like you to share your expressions and suggestions on setting a Data Centre. Can mail at neeta@nic.in
