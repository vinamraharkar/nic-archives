---
title: "Designing a Data Centre Facility"
publication: "Informatics"
issue_date: "July 2007"
pages: [35, 36, 37, 48]
author: "Neeta Verma"
section: "Technology Update"
---

## Designing a Data Centre Facility

With emphasis on electronic governance, on-line access to government information and electronic delivery of citizen services, the need for unified, high quality, secure and scalable e-governance infrastructure spread across the nation has become very vital. Data Centres form the foundation pillars of the e-governance Infrastructure. They shall become repositories of Government data & information be it primary data captured and digitized at the source, secondary data such as meta data, processed data, analysis reports to tertiary data about the usage or processing of the data such as transaction logs, usage logs, access & authentication data.

Government Data Centres are expected to house wide variety of applications, using varied spectrum of technologies with varying service level requirements with respect to performance, availability & Security. Setting up a Data Centre is a time & resource intensive activity and also requires a highly skilled & experience professionals to set up and manage the data centres (DC). Once set up, these DCs are expected to cater to the requirements of e-governance applications for a long time. Thus they should be designed with a lot of flexibility & scalability to meet the ever growing demand of forthcoming technologies as well as applications. Setting up a data centre involves two broad aspects. :
w Basic Site infrastructure inclusive of site preparation, power distribution system, cooling and fire protection & physical security
w ICT infrastructure inclusive of Computing, Storage, Backup, Networking and Security infrastructure.

While computing infrastructure grows over time, the core ICT infrastructure such as Storage System, Communication Network, Security infrastructure has to be planned in the beginning to ensure coordinated growth of DC Infrastructure over time.
Generally people do not pay as much attention on the Basic Site Infrastructure as is needed and face a lot of issues relating to power & cooling capacity in the DCs as they grow. During the past few years there has been a tremendous rise in the heat density of ICT equipments putting in a lot of pressure with respect to power & cooling requirements in existing DCs. Making any unplanned changes for something as basic as enhanced cool & power capacity may require huge shutdown and at times may not even be feasible. Therefore it is important to analyse and understand the present and forthcoming requirement of DC's physical Site infrastructure and do an extensive planning prior to designing the specifications. This Basic Site infrastructure should be generally planned & designed for about 10 years.

While flexibility & scalability should be the principle objectives behind this exercise, one should take a holistic approach in planning, designing and setting up the data centre. This shall essentially require work around following subsystems of the data centres:
Site Preparation
Location and Type of Building plays an important role in the overall performance of the Data Centre. If one is constructing the building from the scratch , then even the location of the building should be selected carefully keeping in view the Signal Interference, availability of utilities, accessibility, security , vulnerability to natural disasters, etc. However Quite often Data Centres are set up in the existing buildings. Following are some of the important features to look for during the selection of building for DC:
w Site Preparation
w Power Distribution
w HVAC System
w Fire detection & Suppression
w Security System

Most of the material used for Site Preparation for DC right from Flooring, Wall Panels, Glass Partitions, Ceiling should be thermal resistant. Further to facilitate maximum floor loading one should consider using cast aluminum floor tiles or something equivalent in the equipment area.

Power Distribution
Another key parameter is estimating the power rating for the data center. This includes power rating for the UPS system as well as for Diesel Generators. Power rating for UPS system is estimated based on the power requirement of the present & future ICT equipment to be housed in the data centre while total estimated power consumption of DC including power required for ICT equipment, Air conditioning system, Lighting etc. will determine the power rating of the standby diesel generators.
Due to constantly growing power ratings of ICT equipment, requirement for power has grown manifold in data centres (refer power trend chart) and it's expected to rise further for next five years. In view of this, one should design the power distribution system with sufficient scalability. One should also build additional capacity into the main electrical components to accommodate future growth.
Some of the guidelines for designing the power distribution system in Data Centre are :
1. Power to data centre shall be preferably provisioned from two independent sources
2. Provision for maintenance bypass and emergency shutdown.
3. Provide Redundancy in all critical components
4. Provision for a grounding system signal reference grid (SRG) to reduce high-frequency impedance.
5. UPS should be planned with enough battery backup to enable activation of DG Sets or graceful shutdown of the ICT systems in case of emergency.

Heating, Ventilation and Air Conditioning (HVAC) System
Due to tremendous growth in heat density of ICT equipments as well as need for vertical growth in Data Centres, provision of adequate and appropriate cooling is one of the major challenge for Data Centre Managers. Correct estimation of cooling capacity, selection of cooling technology and distribution of cool air vs placement of ICT equipment to position of floor tiles are important parameters/ factors to be considered during the design of HVAC system in the DC. One should also plan for redundancy in cooling solution by installing multiple HVAC units, rather than a single, centralized Unit.
Cooling technology could be refrigerant based or water based. However, to avoid risks due to water leakage in the data centres, in small & medium size data centres refrigerant (DX) based cooling is used. While in very large data centre with very high heat density (20-25 KW) water based cooling becomes more economical. Under floor distribution of air can be an effective means of cooling.

Raised Floor
If underfloor cooling is deployed, height of Raised Floor shall be adequately selected. Height of raised Floor is determined based on two factors :
- Size of the DC, particularly equipment or Server Area. Larger equipment area shall require higher raised floor to achieve requisite air flow.
- Heat Density or cooling requirements of the ICT equipments, proposed to be installed in the data centre. Higher Heat Density shall require higher raised floor.
However one needs to look into cost effectiveness of the solution as beyond a certain point (more than 10 KW per rack), under-floor cooling is not effective and one needs to augment it with supplementary cooling technologies such as in row cooling, in rack cooling etc.

Cold Aisles & Hot Aisles
To achieve more-efficient cooling, server racks are placed in a manner (ref diagram) to create alternate cold aisles and hot aisles. Further , perforated tiles are positioned in the raised floor to direct adequate chilled air into the racks. Layout of cable trays & ducts should also be so designed that it does not obstruct the airflow making cooling less effective. Generally all cable trays should be aligned in Hot Aisles. Over head cable trays could also be considered wherever possible, particularly if one is not able to get adequate raised floor space.

Effective Airflow
Airflow is another important parameter to be considered during the design of HVAC system. Layout & positioning of Equipment in DC affects the movement of air through, between and over the rack area and if not planned properly, it can lead to formation of hot spots. One can use special purpose software to achieve optimimum airflow through appropriate location of racks, air-conditioning units and high-density equipment leading to enhanced cooling efficiency and reduced costs.

The power and cooling challenge will not be a perpetual problem. A series of innovations will converge during the next five years that will stabilize the growth in power, particularly for cooling high-density equipment. Innovations are occurring at every level of this ecosystem. The leading processor manufacturers are striving hard to produce increasingly energy-efficient chip sets. Server manufacturers are employing more-efficient power supplies, heat sinks and power management systems, and are also offering a host of in-rack cooling solutions. - Gartner

Fire Detection & Suppression system
Protection from Fire should be one of the important criterion while designing the specifications for DC. As stated above all the material used in building including the furniture & other equipment should be thermal resistant and should have minimum fire propagation or smoke generating properties.
Comprehensive fire suppression system should be installed in the DC consisting of highly sensitive smoke & heat detection, pre-action and fire suppressants. Fire Suppressant system should meet the building codes recommended by the government agency.
Fire suppression system shall deploy FM-200 or Inergen based gas suppression systems as they are human safe and do not harm the servers. These detectors should be arranged in a manner that they activate the suppression system zone wise to cater to only the affected area and thus optimise the cost. Fail-safe alarm system should also be in place to prevent false discharge of gas or tampering. Additionally, Portable Extinguishers shall be placed at strategic locations in the Data Centre.

Multi Grade Security
As stated above, Data Centres form the foundation pillars of the e-Governance Infrastructure. They shall be the repositories of Government data & Information. Hence Security is of paramount importance to the Government Data Centres. One needs to devise multi-grade security Infrastructure.
The Data Centre shall be divided into multiple zones with graded security for restriction of physical movement and entry into the Data Centre. Access should be controlled through proximity cards, biometric identification, pin number etc. One can also use a combination of these technologies in different zones in DC to provide desired level of security without causing any inconvenience in operations. Access policy could be based on the role, responsibility as well as on time zone. Further, all activities in the DC should be monitored using CCTV surveillance system with Recording and Replay facilities.
Data Centres form the foundation of e-Governance infrastructure in the country and play a very significant role in electronic delivery of government information and services to the citizens. Performance, Security & Scalability of Data Centre Services is one of the critical factor behind the success of any citizen oriented e-governance initiative. Data Centres should therefore be designed with utmost care & thorough understanding of the present & future need of ICT technologies as well as e-governance applications proposed to be hosted in the Data Centre.
