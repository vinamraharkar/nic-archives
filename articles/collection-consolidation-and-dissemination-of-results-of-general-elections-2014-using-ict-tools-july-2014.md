---
title: "Collection, Consolidation and Dissemination of Results of General Elections 2014 using ICT Tools"
publication: "Informatics"
issue_date: "July 2014"
pages: [5, 6, 7, 8]
author: "MOHAN DAS VISWAM (Edited by), Dr. V.N. SHUKLA, CHANDER SHEKHAR JAIRATH, R. K. AGRAWAL, SHRI V.S. SAMPATH (quoted), Dr. ALOK SHUKLA (quoted), Dr. (Mrs.) SHEFALI S. DASH (quoted)"
section: "E-Gov Products and Services"
---

## Collection, Consolidation and Dissemination of Results of General Elections 2014 using ICT Tools

Real Time Election Information Portal registers 467 Million Hits!

India is the largest democracy of the world. Considering vast geographical expanse and large size of electorate, carrying out free and fair election process in India is quite complex and challenging. With 814.5 million registered voters taking part, General Elections 2014 have proved to be biggest election event in the history. Election Commission of India has teamed up with National Informatics Centre for successfully carrying out the whole election process and on the counting day – May 16th, 2014 real-time dissemination of election results was carried out through http://eciresults.nic.in, which was channelized from 989 Counting Centres.

INTRODUCTION
The penetration of ICT in election process has strengthened the cause of democracy in the country. Election Commission of India utilized Information Technology in a big way in the General Election, 2014, to ensure easy access of services by the voters and to enhance the service delivery, transparency, information dissemination and management of the election procedures. India is the world’s largest democracy; Election process in the world’s largest democracy poses immense challenges with respect to collection of huge data from the geographically diverse area. Further processing, presentation, and real-time, worldwide dissemination of the election results is quite a daunting task in itself.

To manage various challenges, Election Commission of India worked in close collaboration with National Informatics Centre to provide real time information on election results all over the world on the counting day i.e. May 16, 2014. The high-end servers created supercomputing centres at NIC’s National Data Centres at New Delhi and Hyderabad as the primary and DR site respectively. NIC along with ECI designed the results delivery architecture in high availability (HA) environment for high performance keeping in view the high computational requirements. Anticipating very high traffic from across the world, CDN technology was deployed for smooth delivery of election results. The results delivery proved to be a big hit across the world. Total 467 million hits were recorded with peak of 13357 hits per second. The whole system worked in tandem successfully without any technological glitch in spite of such high demand on the infrastructure resources. This has set an example of large scale of appraisal.

“NIC empowered us to deliver the largest elections in the world most effectively and efficiently.”
SHRI V.S. SAMPATH, Chief Election Commissioner, Election Commission of India

SITUATION
The General Elections to the House of People- 2014 to constitute the 16th Lok Sabha were held in nine different phases in the month of April and May-2014. Counting of the votes polled was held on 16th May-2014 simultaneously at all the 989 Counting Centres located across the nation. The results of counting were captured with the valuable efforts of field level administrative officers i.e. Returning Officers (ROs) and technical officers i.e. District Informatics Officers (DIOs) of NIC District Centres from all the Counting Centres. The information was disseminated in real time to public all over world through url http://eciresults.nic.in. The data flow diagram of the same process has been depicted in Figure 1.

The first key challenge is to ensure free, fair counting and make sure the information is disseminated by the Election Commission of India (ECI) in almost real time. Therefore, it needed a solution that collects data from each of 989 Counting Centres, so that counted votes are sent to the NIC Data Centres, Shastri Park, New Delhi. This application must seamlessly integrate with backend database to ensure smooth flow of accurate and real time data from the Mini Data Centres. The data of 9,30,000 Polling Stations was transmitted from 989 Counting Centres with about 5000 concurrent users which required a highly available application.

The second challenge is to make this information available on their website, as this is the first source of election information. It caters to the interest of Indian citizens, government officials across the world, NRIs and analysts watching and working on these results. Uninterrupted, real-time, election trends and results on ECI website from 8:00 AM was very critical. Our website had to be robust enough to handle millions of visitors and thousands of concurrent hits. Performance and high availability of the website were extremely essential. Finally, to ensure there is no downtime at all, all applications must replicate in real time, and a Disaster Recovery (DR) site is essential.

KEY DELIVERABLES
The comprehensive information which was made available to the public includes:

*   All India Party wise Result Status along with Vote Share
*   State wise, Party wise Result Status along with Vote Share
*   Constituency wise All Candidate’s Vote Details
*   State wise, Constituency wise Leading Candidate, Leading Party, Trailing Candidate, Trailing Party, Margin of Votes, Result Status.

TECHNOLOGY USED
The Results Delivery Architecture was designed in High Availability (HA) mode keeping in view of the high computational requirements. High end servers were deployed at supercomputing level. The 989 Counting Centres where counting for all the 543 Parliamentary Constituencies was carried out throughout the country were connected directly to NIC Data Centre, Shastri Park using web services for sending the round wise result on counting data in real time. Counting was carried out from 4125 Assembly Segments and the setup was so prepared to take the load of 5000 concurrent live connections from Counting Centres. All committed transactions were mirrored to Disaster Recovery site at Hyderabad. Partial data was replicated to ECI, Nirvachan Sadan, New Delhi. HTML pages were generated to disseminate the results all over the world through url: http://eciresults.nic.in. Anticipating large number of hits from across the world, CDN technology was used for smooth delivery of election results.

NDC, Shastri Park, New Delhi was the primary site and NDC, Hyderabad, Andhra Pradesh acted as DR Site.

The primary site (NDC, Shastri Park) was configured as tier 3 Data Centre with expected availability of 99.982%. The tasks performed to achieve the set goals of the project includes Virtualization of Servers, Setup of DR/Mirror Site, Replication to ECI, NLB Configuration, Pre counting data availability, Live Data Fetching from Counting Centres, Business Logic Implementation, Web page generation, Emailing trends/results to given emails etc. The work flow diagram of the entire process is given in the Figure 2 while architecture of the infrastructure has been represented in Figure 3.

“…467 million users….with a peak of 13,357 hits/ second….We leveraged National Informatics Centre to attain such performance, delivery, uptime and availability.”
Dr. ALOK SHUKLA, Deputy Election Commissioner, Election Commission of India

“The smooth delivery of IT services for the 16th general elections of India is a great achievement for NIC. In spite of such high demand on the resources, our teams across the country were able to help deliver results without a glitch.”
Dr. (Mrs.) SHEFALI S. DASH, Dy. Director General, National Informatics Centre

For further information:
CHANDER SHEKHAR JAIRATH
Senior Technical Director, NIC HQs
E-mail: cjairath@nic.in
OR
R.K. AGRAWAL
Technical Director
NIC HQs
E-mail: agrawal.rk@nic.in
