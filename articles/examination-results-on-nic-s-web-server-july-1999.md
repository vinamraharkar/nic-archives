---
title: "Examination Results on NIC's Web Server"
publication: "Informatics"
issue_date: "July 1999"
pages: [13]
author: null
section: null
---

## Examination Results on NIC's Web Server

During the past quarter, results of various important examinations such as Tamilnadu SSLC, Rajasthan Board, Maharshtra Board etc. were hosted on NIC's web server. These sites received a large number of hits from students all across the country.

Based on the experience, NIC has formulated a standard pattern for hosting of similar Resultsin future which is being described here.

Dedicated servers were set up in Delhi and mirror sites established at State Headquarters for ensuring fast access anticipating a high traffic on the Results site. All these servers would be using Internet Information Server (4.0) as their web publishing server and SQL server (7.0) as the Database server. The technology of Active Server Pages was used as the front end to receive the request and post the result back to the User. The data needs to be originally sent in dbase format which was subsequently converted to the SQL server database and distributed among multiple database servers. In order to ensure the effective processing and transmission of simultaneous requests, the COM object would be created and used through Transaction Server to get the connectivity with the SQL server. The multiple servers were configured to work in a round robin manner for distributing the hits.

This approach was highly successful in handling heavy traffic to the Results Web Site, especially during the first few hours. Announcements of Results on the web in future may be done using the same technology. For any further details, mail to :

mmapd @www.nic.in

Tamil Nadu SSLC Results on the Net
