---
title: "NICNET TRANSMISSION FOR ELECTIONS'98"
publication: "Informatics"
issue_date: "April 1998"
pages: [11, 12]
author: null
section: null
---

## NICNET TRANSMISSION FOR ELECTIONS'98

Delhi : The Trends Transmission of the 1998 Lok Sabha Elections was the most challenging of all the election transmissions projects handled by NIC so far. The simultaneous challenges were to :

● Bring up the application on the C-Band network, for which a transponder on INSAT 1-D was made available to NIC on January 24, just three weeks before the first date of voting.
● Develop the Elections system on a modern LAN platform to replace the NEC mainframe.
● Collect more information about elections rather than just trends. In the past, only trends were collected through the Elect Program on NEC, but now, the candidate list, turnout, exit poll and counting centre status were also collected under the same umbrella interface.
● The central database machine had to be shielded from having to handle direct logins and interaction with the database was connectionless.
● A web site on Intranet was used to train and manage the variety of DIO activities required in the one-month run up to the elections.

As the existing C-200 VSATs at the District Centres use X.25 protocol, the above design specifications were met by running the LYNX Internet browser on a X.25 login host. This login host had an X.25 port for DIO connectivity as well as an IP port for local LAN connection to the main database machine.

On getting a X.25 connection to a login host, the DIO had to run LYNX, get the appropriate empty data entry HTML forms from the database and transmit the completed forms back to the database machine in a connectionless way.

In future, as the District Centres acquire Internet browsers and high speed communication links, they would be able to contact the database directly from their local browser, bypassing the LYNX component. The rest of the system would be unchanged.

Finally, through the KU-Band network via INSAT-2C, the Elections data was transmitted to the server set up at Doordarshan.

The C-Band Monitoring Station worked hard to make sure that the whole transmission was smooth and also communicated detailed instructions regarding the use of new procedures to the District Informatics Officers using the interactive chat facility.

The contribution of the NICMAIL-400 system to the 'message handling' part of the entire procedure was absolutely vital. More than four thousand election-related mails were processed. The fact that all NICMAIL-400 boxes reside on the same machine meant that the District NIC officials could interact with the Headquarters within fifteen minutes of a mail-request.

For further information, contact ssarkar@sansad.nic.in
