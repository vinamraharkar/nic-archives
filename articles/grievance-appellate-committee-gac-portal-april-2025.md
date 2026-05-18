---
title: "Grievance Appellate Committee (GAC) Portal"
publication: "Informatics"
issue_date: "April 2025"
pages: [24, 25]
author: "Edited by VINOD KUMAR GARG"
section: "e-Gov Products & Services"
---

## Grievance Appellate Committee (GAC) Portal

The Grievance Appellate Committee (GAC) is a transformative initiative established under the Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021, aimed at ensuring a Safe, Trusted, and Accountable Internet for Indian users. It provides an efficient, transparent, and user-centric online dispute resolution mechanism for citizens of India aggrieved by decisions of Grievance Officers of social media and other Intermediaries. The project digitizes the entire appeal process, right from filing to resolution, ensuring timely decisions within 30 days. By reducing dependency on manual processes and fostering accountability, the GAC online solution significantly enhances accessibility and efficiency. This initiative not only enforces the IT Rules but also empowers citizens, promotes digital governance, and strengthens trust in India’s Digital Ecosystem. Through its user-friendly platform, the GAC portal facilitates seamless interaction between Citizens, Intermediaries, GAC Secretariat and Experts, ensuring a fair and standardized grievance redressal process while contributing to the creation of a responsible and accountable digital environment.
Features of the Product
• Fully Digital Appeal Process: Entire grievance redressal process is digitized, from filing to resolution
• Dedicated Dashboard with MIS Data and Stats: The portal features a dashboard with clear MIS data and statistics, ensuring easy access to relevant information
• Grid view Interface for Appeals List: To enhance user navigation, an unique “Grid view” interface categorizes and present all appeals in an easily readable and accessible format
• Secure Access for GAC Secretariat: GAC officials can log in using Parichay SSO for secure access
• Aadhaar Authentication: Citizens (Digital Nagriks) can file appeals online after Aadhaar Authentication, ensuring transparency and accessibility
• Emails: Configurable formats for Gist, Decision and Formats of documents and email can be configured by portal admin
• Expert Observations and Voting Mechanism: Expert observations provide insights and members can participate in a structured Voting System (Agree/Disagree with remarks)
• Timely Resolution: Appeals are resolved within a time-bound manner, aiming for decisions within 30 days
• Data Sharing APIs: Social Media Intermediaries can onboard to access additional API-based data sharing features
Tech Stack & Architecture
The portal is developed using ASP.NET with C# programming language, following the MVC (Model-View-Controller) architecture to ensure a clean, scalable, and maintainable codebase. This architecture allows for seamless interaction between the front-end and back-end components. The backend is powered by Microsoft SQL Server 2019, providing a reliable and efficient database management system for securely managing user data, appeals, and other essential information. This ensures fast data retrieval and smooth platform operations. Various documents related to appeals are securely stored on a file server, providing centralized access and management of critical files within the system. Bootstrap is used extensively on the front-end, ensuring a responsive and user-friendly design across devices for enhanced user experience. ApexCharts are integrated into the user dashboard for visually rich and interactive data visualization, helping users better understand real-time information. To ensure secure user access, the system utilizes Parichay SSO (Single Sign-On) service for seamless authentication, allowing GAC Secretariat to log in securely. Additionally, the Aadhaar Authentication Service by UIDAI enables citizens to create their profiles securely, ensuring proper identification. This combination of modern technologies ensures a highly efficient, secure, and user-centric grievance redressal system that meets the needs of all the stakeholders.
The Grievance Appellate Committee (GAC), established under the IT Rules, 2021, ensures a Safe, Trusted, and Accountable Internet for Indian users. It provides an online dispute resolution platform for Digital Nagriks (Citizens of India) aggrieved by decisions of Grievance Officers on Social Media complaints. Notably, the entire appeal process is fully digital, with the GAC’s user-friendly web portal ensuring seamless, timely, and efficient resolution of appeals within 30 days.
• Frontend: A user-friendly interface with Grid view data display and ApexCharts-powered visualizations are used for accessibility across devices.
• Backend (Controller): Built with ASP.NET and C#, it manages business logic, user requests, and data flow between the frontend and database securely and efficiently
• Database (Model): Microsoft SQL Server 2019 securely stores and manages user data, appeals, and decisions, ensuring fast retrieval and efficient query handling
• Authentication & Security: Parichay SSO secures GAC Secretariat logins, while Aadhaar Authentication verifies citizen identities, enhancing transparency and accountability
• File Management: A centralized server securely stores appeal documents, ensuring easy access and efficient management
• APIs & Integration: Supports data sharing with social media intermediaries, improving communication and grievance resolution efficiency
This architectural flow ensures a smooth, secure, and scalable grievance redressal system for the GAC Portal.
Portal Workflow
The workflow of the GAC portal begins when an Appellant register using Aadhaar Authentication to ensure secure identity verification. Once registered, the Appellant can file an appeal, which is automatically mapped to the relevant GAC based on the complaint type. Once the appeal is filed, the system sends alerts to the concerned Social Media Intermediaries (e.g., Meta, Google) to respond within 96 hours. Following the Intermediary’s response, the Assistant Manager of the respective GAC prepares a Matter Summary, which is then reviewed by GAC Members. They provide their opinions and, if necessary, seek expert advice. The final decision is made by the GAC Chairman and copy of the decision is communicated electronically to all stakeholders automatically, including the Appellant and Intermediaries. The copy of the decision is also made available under each stakeholder’s portal login. Lastly, the Intermediaries are required to submit a Compliance Report along with the URL, confirming their adherence to the decision, ensuring accountability and transparency in the process.
Impact
The Grievance Appellate Committee (GAC) portal offers several key benefits and impactful outcomes for both citizens and digital intermediaries:
• Transparency and Accountability: Allows citizens to escalate unresolved complaints to social media platforms, ensuring fair grievance redressal
• Efficiency and Timeliness: Digital appeals ensure grievance resolution within 30 days, significantly faster than traditional methods
• Enhanced Accessibility: A user-friendly platform ensures easy navigation, promoting digital inclusion for all users
• Digital Governance: Strengthens trust in India’s online ecosystem by enforcing IT Rules and promoting a responsible digital environment
• Secure User Authentication: Aadhaar authentication and secure logins ensure identity verification and transparency
• Improved Communication: Real-time data sharing and API integration enable seamless collaboration among GAC secretariats, experts, and social media intermediaries
• Promotes Compliance: Ensures social media intermediaries submit compliance reports, fostering a safer and more accountable digital ecosystem
Ultimately, the GAC portal ensures a safe, trusted, and accountable Internet for Indian users, promoting a fair grievance resolution process and strengthening digital governance.
Way Forward
Moving forward, the GAC portal can be further enhanced by integrating more advanced AI-driven tools to automate decision-making processes and analyze appeal trends. Additionally, ongoing collaboration with more Social Media platforms and continuous monitoring will ensure adherence to evolving digital ethics and regulations. By scaling up the system and incorporating feedback from stakeholders, the GAC portal can evolve into a global model for digital grievance redressal, driving greater accountability and trust in the digital ecosystem.
