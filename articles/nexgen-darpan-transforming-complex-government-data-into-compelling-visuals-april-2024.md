---
title: "NexGen DARPAN Transforming Complex Government Data Into Compelling Visuals"
publication: "Informatics"
issue_date: "April 2024"
pages: [28, 29, 30]
author: "I. P. S. Sethi, Sunil Sharma, Ajai Gopal Bharatariya, Vaibhav Agarwal"
section: "eGov Products & Services"
---

## NexGen DARPAN Transforming Complex Government Data Into Compelling Visuals

The implementation of the Darpan Dashboard was driven by the urgent need to enhance transparency and operational efficiency within the government. Recognizing the evolving expectations of citizens and the global trend towards digital governance, there was a clear requirement for a platform capable of providing quick, real-time insights into government initiatives, budget allocations, and performance metrics. Uttar Pradesh has made significant strides in advancing its e-Governance framework through the deliberate adoption of the Darpan Dashboard. This dashboard serves as a crucial tool in promoting administrative accountability, providing seamless access for stakeholders, and facilitating the evaluation of relevant information. Leveraging Meghraj Cloud Services, the dashboard currently manages an extensive portfolio comprising 805 projects across 67 departments, encompassing a total of 5837 registered Key Performance Indicators (KPIs).
A vital aspect of this initiative involves the rigorous implementation of a Data Quality Index (DQI) and Star Rating mechanism. This evaluative framework relies on meticulously sourced data from diverse departments, contributing to the Chief Minister’s dashboard. Through thorough analysis of this data, a monthly compilation of Rankings and Gradings is conducted, covering Projects, Departments, Districts, and Composite entities.
The Darpan Dashboard was inaugurated by Hon’ble Chief Minister Yogi Adityanath, in the presence of Hon’ble Deputy Chief Ministers Shri Brajesh Pathak and Shri Keshav Prasad Maurya, along with Shri Swatantra Dev Singh, Minister of Jal Shakti, Government of Uttar Pradesh (GoUP), Shri Suresh Kumar Khanna, Minister of Finance, GoUP, and Shri Arvind Kumar Sharma, Minister of Urban Development and Minister of Energy, GoUP, on July 30th, 2023.
The CM Command Centre and DARPAN Dashboard will play a pivotal role in evaluating the performance of officials across sectors such as Police Service, Municipal Corporations, and Development Authorities. Furthermore, they will assess the effectiveness of various government schemes through monthly ranking and grading processes.

The Legacy System
    The creation of the DARPAN Dashboard arose from the urgent necessity for a centralized platform to monitor government projects and streamline data management. It seamlessly integrates with multiple online systems, each offering varying levels of data granularity, and amalgamates information from diverse departments. Through this process, it transforms this heterogeneous data into actionable insights, thereby facilitating more efficient governance.

NexGen DARPAN (Dashboard for Analytical Review of Projects Across the Nation) is con-figurable, generic and bilingual copyright product of NIC and provides the administrations with at-a-glance insights into departmental activities and scheme monitoring. DARPAN enables dynamic project moni-toring without coding, featuring drilldown capabilities for quick and detailed perspectives of all flagship government projects. With its unparalleled adaptabil-ity and versatility, the DARPAN platform stands ready for seamless integration, offering its robust functionality across various States as well as Central Ministries/ Departments.

UP CM DARPAN Dashboard empowers informed decision making and facilitates seamless integration of departmental MIS portals with the Dashboard. Its prowess in project monitoring ensures culture of healthy competition among departments. Much success to the UP Dashboard group as they work to shape a future where technology is the driving force.
S.P. Goyal, ias
Additional Chief Secretary Govt. of Uttar Pradesh

Fig 8.1: Hon’ble Chief Minister, Yogi Adityanath Ji, inaugurated Darpan 2.0 and the CM Command Centre at Shastri Bhawan, Lucknow

Process at Glance
    The system architecture comprises two closely integrated modules: Data Integration Services and Data Visualization (Dashboard) Services. Within this structure, the Data Validation module ensures Data Quality by detecting and eliminating Data Outliers. DARPAN provides users with the flexibility to access data at various granularities, including Time-stamped Master Data and the most recent Master Data. Moreover, DARPAN optimizes processes through automated workflows, establishing a resilient approval-based Content Management System. It also employs a robust authentication mechanism for web API Data consumption and integration with Management Information Systems (MIS).

Secure Web API
    Our versatile RESTful web-API, fortified with 256-bit AES Encryption and G-zip Compression, ensures seamless data consumption across diverse environments. Additionally, HMAC, which combines a cryptographic hash function with a secure Cryptographic key, guarantees real-time validation of client payload data. The deployment of SSL further underscores our commitment to robust security measures.

Authenticated MIS
    DARPAN simplifies the integration of departmental MIS portals with its Dashboard, enabling monitoring officers to swiftly access beneficiary-level data. Project administrators have the option to implement Secure MIS (DARPAN Authenticated MIS) to prevent unauthorized access. Enhanced security measures, such as MIS key and token validation processes, are employed to restrict access solely to authorized parties, ensuring data confidentiality and integrity.

Key Highlights
• The platform offers specialized dashboards customized for various organizational levels and functions:
    • Sectoral Dashboards
    • Departmental Dashboards
    • Ministry Dashboards
    • Project Dashboards
• The dashboard offers thorough insights into government schemes, aiding informed de-cision-making and performance evaluation through the following options:
    • Scheme Overview
    • Descriptive Analysis
    • Comparison Series
    • Demographic Analysis
    • Trend Timeline Series
    • Peer Analysis
• The platform includes these essential features to ensure data accuracy and reliability, empow-ering stakeholders to make confident, informed decisions:
    • Data Quality Index (DQI)
    • Star Rating
    • DQI Mark sheet
• The product provides versatile ranking capa-bilities for districts, divisions, departments, and projects with various modes:
    • Fixed Formula: Consistent criteria-based ranking
    • Dynamic Formula: Adapts to changing fac-tors
    • Delta Ranking: Focuses on progress made from onetime period to another. It helps in identifying top / bottom performers
• The system allows authorized users to tailor their views, prioritize important information, and customize chart options for a personalized experience, enhancing perspectives on priority projects.
• The system generates a comprehensive book-let offering detailed insights into project perfor-mance across various levels. It provides a holistic view, highlighting both underperforming and suc-cessful projects.
• This feature offers users a dynamic viewing experience, enabling them to review specific projects in real-time. It operates from a gallery of project information based on user-selected crite-ria, such as project and timeframe.
• The mobile app empowers users to seamlessly monitor projects and performance across diverse platforms, ensuring flexibility and accessibility.

Timely implementation of numerous government flagship projects and convenience of single window monitor-ing have both been greatly facilitated by the UP CM Dashboard. I want to thank the NIC team for all of their hard work and dedication, and I hope that they will continue to work diligently to make e-Governance a success on every level.
Sanjay Prasad, ias
Principal Secretary Govt. of Uttar Pradesh

Integrated dynamic rating and grading capabilities helps in transparent perfor mance comparison of schemes in UP CM Dashboard. It also guarantees data con-sistency and secure data collection, al-lowing for fair resources allocation. Star ratings enhances efficacy of government machinery in implementation of flagship proj-ects. Congratulations to the team DARPAN for their successful IT ap-plication imple-mentation.
Alok Kumar, ias
Principal Secretary Govt. of Uttar Pradesh

Fig 8.2 Data Consumption Process Flow
START
Method : GetDATE ( ) State Code =.......... Dept. Code =.......... Project Code =.......... Sec. Code =.......... HMAC SIGNATURE
1 Pass project Parameter to Getdate method
DARPAN SERVER
Verify HMAC Token
Validate User Input
No Data Validation failed
2 Validate and Verify Client Request
3 Log and acknowledge the error to client
Yes
Method : GetDATE( ) State Code =.......... Dept. Code =.......... Project Code =.......... Sec. Code =.......... Encrypted Data =.......... HMAC SIGNATURE
4 Pass date range data and project parameter to Pushdata method
DARPAN SERVER
Verify HMAC Token
Validate User Input
No Data Validation failed
5 Validate and Verify Client Request
6 Log and acknowledge the error to client
END
Yes
6 Store the pushed data and acknowledge to client
Method 1- Getdate Process
Method 2- Pushdata Process
Store pushed data and acknowledge to user
• For More than one date range process no. 4 to 6 will repeat.
• Every API request is serve with new token
Process Number
Alternate Process Number

Data Visualization of UP CM DARPAN allow for rapid comparisons and in depth analysis. The extensive Insight of schemes highlights the strengths and areas for improvement by showcasing its performance across micro levels. Specifi-cally designed to be used in performance review meetings, it gives officers access to relevant dashboard data. The integrat-ed Command Centre adeptly facilitates video conferencing, call centre and col-laborating seamlessly with the DARPAN UP team. Well done to the teams at the NIC and the command centre for their unwav-ering dedication to providing ex-ceptional service.
Prathmesh Kumar, ias
Special Secretary Govt. of Uttar Pradesh

Technology Stack
    The system is built using cutting-edge .NET web technologies and seamlessly integrated with SQL Server. RESTful APIs are structured meticulously following the Model, View, and Controller (MVC) architecture, while jQuery and JavaScript libraries are utilized for efficient client-side activity management.

Impact
• The DARPAN Dashboard is utilized by the Hon’ble Chief Minister’s Office of Uttar Pradesh and reviewed by government officials involved in policy and decision-making at both state and district levels.
• It empowers Hon’ble Chief Ministers, Commis-sioners, DMs, CDOs, SPs, and Police Commission-ers to efficiently monitor critical information, streamlining decision-making processes.
• The dashboard enables real-time district-level project monitoring, providing Hon’ble Chief Min-isters with direct insights for swift decision-mak-ing and timely interventions.
• A strategic ranking system based on KPIs en-sures accountability and healthy competition among departments, driving continuous im-provement.
• DARPAN offers an objective assessment of de-partmental activities up to the district level, en-abling informed decision-making by identifying successes and areas for improvement.

Advantages
    The benefits of the DARPAN Dashboard are extensive, enhancing efficiency and decision-making across administrative levels:
• Streamlined KPI Visualization: The web-based dashboard simplifies KPI visualization across de-partments, enabling quick assessments without navigating intricate source systems.
• Real-Time Project Evaluation: Real-time proj-ect evaluation empowers decision-makers to swiftly measure progress, fostering an adaptive and responsive approach to project management.
• Detailed Information Accessibility: Dashboards allow users to seamlessly drill into detailed infor-mation by selecting desired variables or objects from complex datasets, facilitating nuanced un-derstanding for informed decision-making.
• Universal Accessibility: DARPAN’s programming ensures universal accessibility, reaching diverse stakeholders anytime, anywhere, aligning with in-clusivity and expeditious decision-making.

Accolades
    The DARPAN Dashboard was honored with the Award of Excellence at the CSI SIG e-Governance Awards 2021, recognizing its remarkable contribution to digital governance.

Ending Remarks
    The DARPAN Project Management Unit (PMU) at NIC Uttar Pradesh State Unit, Lucknow, is headed by Shri Ajai Gopal Bhartariya, Senior Technical Director with Shri Vaibhav Agarwal, Smt. Shalini Singh, Shri Vijay Singh Pal, and Shri Kamlesh Singh actively contributing to product development and implementation. They operate under the guidance of Shri I.P.S Sethi, Deputy Director General (DDG) at NIC Headquarters, New Delhi with consistent support from Shri Sunil Sharma, State Informatics Officer (SIO), Uttar Pradesh.

Contact for more details
Ajai Gopal Bhartariya
Senior Technical Director & Project Head
NIC Uttar Pradesh State Unit
Lucknow, Uttar Pradesh - 226001
Email: ajai.gopal@nic.in, Phone: 0522-2298828

The state of Uttar Pradesh has taken major strides towards implemen-tation of UP CM Dashboard powered by NexGen DARPAN. The system is excep-tional in ensuring ease of single window monitoring of various schemes across state at various levels. Good luck to Team DARPAN! I’m excit-ed for all the future e Governance proj-ects that NIC has in store.
Amit Singh
Secretary Govt. of Uttar Pradesh

Fig 8.3 Advantages of NexGen DARPAN
Officers Login
Access 24x7
Prioritize Statistics
Dashboard Settings
Admin Login
Periodically Updated
Analytical Review
