---
title: "Ente Bhoomi Integrated Land Information Management System of Kerala"
publication: "Informatics"
issue_date: "January 2025"
pages: [24, 25, 26, 27]
author: null
section: "eGov Products & Services"
---

## Ente Bhoomi Integrated Land Information Management System of Kerala

Kerala’s Integrated Land Information Management System (ILIMS), epitomized by the groundbreaking Ente Bhoomi digital land survey project, marks a transformative leap in land governance. In the domain of sustainable land administration, precise and up-to-date cadastral data is indispensable for managing land tenure, ownership, valuation, and utilization. Kerala, a pioneer in innovative governance, has continuously evolved its land administration systems since 1905. However, the separation of textual and spatial records often hindered the reflection of real-time land transactions and updates.
To address these challenges, the Kerala government launched the Digital Resurvey Mission under the Ente Bhoomi initiative. This ambitious project reimagines land administration, creating a holistic, citizen-centric Integrated Land Information Management System (ILIMS). Aligned with the Revenue Department’s mission statement—”Land for all, records for all the land, and all services smart”— ILIMS sets a new standard for transparency, efficiency, and inclusivity in land governance.
Background
Kerala’s diverse topography and fragmented landholdings have historically posed challenges for traditional land administration. The 2018 and 2019 floods exposed the vulnerabilities of outdated and incomplete land records, underscoring the urgent need for digital transformation.
• Previous resurvey attempts struggled due to:
• Paper-based inaccuracies
• Outdated spatial records
• Limited accessibility to data
• Incompatibility of legacy survey data with modern geospatial platforms
To overcome these issues, Kerala launched the Digital Land Survey Program, a comprehensive initiative integrating advanced technologies to enable real-time data sharing, ensure disaster preparedness, and enhance overall governance efficiency.
Objectives
Accurate and Transparent Land Mapping
• Conducting comprehensive cadastral surveys to generate precise Land Parcel Maps (LPMs) with geospatial accuracy.
• Eliminating land record discrepancies and ensuring legally binding land demarcation for dispute-free ownership.
Seamless Land Records Integration
• Unifying revenue, registration, and survey systems to facilitate a single-window digital service for land transactions.
• Enabling real-time synchronization between textual and spatial records to reflect accurate land ownership details.
Issuance of Tamper-proof Records of Rights (RoR)
• Providing legally authenticated Records of Rights (RoR) to landowners to establish ownership security.
• Digitizing land records to prevent fraudulent claims, unauthorized land conversions, and encroachments.
Development of a Multipurpose Cadastral Database
• Creating a centralized digital repository of land information to support urban planning, disaster management, and infrastructure development.
• Utilizing GIS-based analytics for data-driven policymaking and resource management.
Technologies Used
Given Kerala’s challenging terrain and dense tree coverage, cutting-edge technologies were adopted, including:
• Continuously Operating Reference Stations (CORS): Ensuring high-precision geospatial data.
• RTK-based GNSS systems and Robotic Total Stations (R-ETS): Delivering positional accuracy within 3–5 cm.
• Drones: Supporting aerial mapping and detailed terrain analysis.
These advanced technologies enable precise and reliable data collection, perfectly tailored to Kerala’s complex landscape.
Complete Re-engineering and Digital Transformation
This program signifies a complete overhaul of traditional land administration practices, replacing manual processes with digital solutions to achieve:
• Enhanced efficiency: Automation of pre-survey, survey, and post-survey operations.
• Improved accuracy: Digital tools minimize human error and enable real-time updates.
• Transparency: A centralized platform empowers citizens and stakeholders to track progress and access services effortlessly.
Phased Implementation Strategy
To ensure effective execution, the program adopts a phased implementation strategy:
• Surveying 200 villages simultaneously within six months.
• Annual coverage of 400 villages to ensure steady progress.
• A unified portal to manage continuous land record updates and transactions.
This phased approach ensures scalability, efficient progress tracking, and timely achievement of ambitious targets.
Major Technological Achievements
The program has achieved significant milestones through innovative technology:
• Advanced Survey Instruments: RTK rovers, R-ETS, and rugged tablet PCs enhance accuracy and reliability.
• CORS Network: A robust network of 28 stations covers over 80% of the state, delivering unmatched geospatial accuracy.
• Ente Bhoomi Portal: A single-window platform integrating revenue, registration, and survey services, ensuring continuous updates and citizen-centric service delivery.
Innovative Features
The Digital Land Survey Program incorporates cutting-edge features that redefine efficiency, accuracy, and citizen-centric service delivery:
• Automated Pre-Mutation Sketches: Real-time generation of essential sketches required for land transactions.
• Auto-Mutation: Seamless synchronization of textual and spatial data to ensure real-time updates.
• Online Services: Providing access to critical documents like Thandaper certificates, location sketches, and encumbrances certificates through an integrated portal.
• Grievance Redressal Mechanism:
• OLC (Original Land Complaints): For raising survey-related grievances.
• ALC (Appeal Land Complaints): For appeals against survey resolutions.
• LRM Complaint Module: An online platform for addressing post-survey land complaints.
Powered by Bhunaksha 5.0
The management of land parcel maps is driven by the advanced Bhunaksha 5.0 platform, offering an array of innovative tools:
• Interactive Map Visualization: Provides users with layered, marker-rich maps for easy interaction and analysis.
• Geospatial Data Management: Ensures efficient storage, querying, and analysis of geographic data.
• Online Digitization Module: Enables the creation and editing of geographic features directly on the map.
• ULPIN (Unique Land Parcel Identification Numbers): Automates the generation and management of ULPINs for every land parcel.
• Reporting Module: Produces detailed reports with sketches, measurements, area calculations, and attribute summaries.
• Quality Check and Fixing: Identifies and resolves topology errors, overlaps, gaps, and boundary inconsistencies in cadastral maps, guaranteeing superior data quality.
ILIMS Architecture
The Integrated Land Information Management System (ILIMS) is built on a robust microservices architecture, consisting of core microservices, authentication and proxy services, and departmental services. These components work in unison to deliver a unified citizen portal and enable cross-department workflows. Key components of the ILIMS architecture include:
• Ente Bhoomi Portal: A single-window citizen portal for all land-related transactions, providing seamless access to services.
• ILM Gateway: An internal API gateway enabling access to departmental services and the integrated land bank.
• ILT Service: The Integrated Land Transaction service acts as a transaction broker and workflow engine for all land-related transactions. It generates a unique Land Transaction Identification Number (LTIN) and facilitates data exchange between departments during transaction workflows.
• Integrated Land Bank (ILB): A centralized repository of land records, registered document information, and cadastral maps. It includes the Unique Thandaper (UTR) for ownership representation and ULPIN data published by the Revenue Department.
• Authentication Proxy Services: Integration microservices that streamline the incorporation of departmental systems into the ILIMS framework.
• Single Sign-On (SSO) Service: A cornerstone of Ente Bhoomi’s e-Governance strategy, enabling seamless integration across the Survey, Registration, and Revenue Departments. It uses FIDO-compliant WebAuthn technology for passkey integration, ensuring enhanced security and user convenience.
• ReLIS Service: A service provided by the Revenue Department for integrated workflows like tax and fee collection and land records management (LRM).
• Pearl Service: A service offered by the Registration Department to track the status of registrations in both front-office and back-office systems.
• RMIS Service: A service from the Survey Department for map-related transactions within the integrated workflow.
Integrated Land Transactions
One of ILIMS’s flagship implementations is the Integrated Land Sale Process, which spans the Registration, Revenue, and Survey Departments. The process is initiated by citizens through the Ente Bhoomi portal, leveraging the SSO service for front-end integration and the ILT service for back-end workflow coordination.
Key Stages of an Integrated Land Transaction
• The citizen initiates a land sale through the Ente Bhoomi portal, generating a Land Transaction Identification Number (LTIN).
• The Revenue module collects fees for the premutation sketch and Thandaper certificate.
• The Survey system prepares the digital premutation sketch as per requirements.
• The Registration system facilitates template-based registration of the sale deed.
• The Revenue system performs auto-mutation of land records using the registered document and digital premutation sketch.
• The updated land parcels are pushed to the Integrated Land Bank for record management.
The LTIN enables transparent tracking of the transaction’s status through the Ente Bhoomi portal, while SMS/Sandes notifications provide instant updates to stakeholders (buyers and sellers).
Way Forward
The program has already achieved significant milestones, including the completion of field surveys in 230 villages, with work progressing in an additional 228 villages, as part of its target to survey 1,550 villages within four years. It has also integrated blockchain technology to ensure secure and immutable storage of land transaction records, while enabling external stakeholders to access the comprehensive integrated land data bank. Additionally, the program has streamlined unified service delivery, offering all land-related services across various departments through the Ente Bhoomi portal, ensuring transparency and efficiency.
