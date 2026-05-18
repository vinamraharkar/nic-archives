---
title: "NIC's Election Experience: A Rich Harvest"
publication: "Informatics"
issue_date: "October 1992"
pages: [4, 5]
author: "Mr S Sarkar, Technical Director, Teleinformatics Development Promotion Project (TDPP), NIC"
section: "Cover Story"
---

## NIC's Election Experience: A Rich Harvest

For all of us in the National Informatics Centre, the Tenth Lok Sabha election was something of an eye-opener. We learnt that society renews and invigorates itself through elections, and all those who participate in the electoral process are themselves invigorated by it.

## The Credibility Factor

In a democratic society, elected representatives can govern effectively only if their electoral victory is deemed credible by all citizens. Apart from vote casting, it is vital that vote counting be fair, and also be seen as fair. This implies immediate round-by-round result reporting for each constituency to as large an audience as possible.

Should this not happen, the upshot can be disastrous. The example of the recent elections in the Philippines is a case in point. Although the actual voting went through fairly smoothly, counting and tabulation took over a month. This lead to all the candidates making rigging and tampering charges, and the resultant damage in overall credibility. Considering that India has eleven times the land area and fourteen times the population of the Philippines, the importance of the result reporting process for India is obvious.

## The Indian Solution

That India found a reliable and nearly instant solution for reporting election results was resoundingly demonstrated during the nation-wide parliamentary elections to the Tenth Indian Lok Sabha.

The Solution was to couple the television network as an output channel for NICNET, thus combining the information collecting power of the satellite data network with the nation-wide broadcast capability of Doordarshan. The coupled networks achieved a tremendous throughput of public information that sustained public interest in, and monitoring of, the results counting process.

## Build-up to the Polls

The Results Information Network benefitted from the close relationship built up by our District Informatics Officers with their respective District Collectors long before the counting day. The NIC district offices and State Headquarters provided vital NICMAIL links in the communication chain between the State Chief Electoral Officer and his Returning Officers in the districts. This allowed the massive logistics involved to be more closely supported.

In many districts, the DIOs went one step further and offered local computerized planning support to the District Commissioner, who in most cases was also the Returning Officer. ELECON was the most widely used of these packages, developed by the DIOs themselves based on their local requirements.

## Significance of Success

The success of NIC's elections projects demonstrated several points crucial to the future of NIC.

NICNET performance was proved in a "worst case" situation of on-line load. All previous experience had been with individual terminals connected to different applications at different times in the normal time-sharing way. The Lok Sabha elections was different because all NICNET terminals had to be connected to the same application at the same time, thus testing NICNET and the NEC host to the extreme. NEC had to be completely reconfigured by the ACOs unit to handle this new usage.

More significantly, the elections exercise revealed hidden depths to NIC's organizing ability. This was most clearly demonstrated by the personal enterprise and dedication shown by the District Informatics Officers and Assistants in getting the results from counting rooms and entering them over a period of 48 hours, often without sleep. In those cases where counting for one parliamentary constituency was split up over several district collectorates, the State Informatics Officer and DIOs concerned responded by organizing their own NICNET sub-networks to accumulate round results for that constituency at one place before using the ELECT program.

## TECHNICAL OVERVIEW

The Elections Results Network was composed of three functional layers. The bottom layer was the communications backbone, consisting of the normal NICNET configuration of one micro-earth station at each of the 440 district collectorates, all connected to the Master Earth Station packet switch at Delhi via the INSAT-1D satellite.

The second layer consists of the NEC S-1000 large mainframe with the Elect results entry software at NIC headquarters and the PC:386s and dumb terminals, one at each district collectorate. This layer used the underlying communication backbone to exchange information. Menu screens and prompts were emitted from the NEC to the network via the packet switch, while commands and round-by-round results flowed in from the district offices.

Forming another part of the second layer were the specially written communication modules which enabled the NEC to transmit the results out to the presentation locations.

The third functional layer consisted of hardware and software that consolidated and presented the results. Consolidated results were presented by a third level programme on NEC that read detailed constituency files provided by the ELECT module and output statewide party positions and overall national party position.

At remote sites the presentation hardware included:

- the NDTV television graphics generator at Doordarshan Delhi studios. This provided colourful templates into which the results data could be slotted, and output in the form of a PAL TV signal, suitable for national telecast by Doordarshan.
- three 486 machines at NIC Headquarters, used for interactive retrieval of results by all sites hooked up with NICNET.
- a PC:386 at the Press Information Bureau (PIB) for generating printouts of query answers for newspaper reporters.

## Future Possibilities

In view of the current liberalization effort underway in the Government, it is possible that NIC may be able to offer its services to private users. The Elections Results Network is an example of the wide area on-line capability of NICNET. A head office anywhere in the Country can collect data from remote warehouses, factories and offices not only for Management Information Systems, but also for daily operations streamlining. Lower inventories could be maintained, shipments could be monitored, and any emerging shortage or irregularity could be spotted in advance.

The Elections Results Network points the way to all these future applications. The role of the National Informatics Centre in the 1990 elections has paved the way for extensive use of computer networks in nationwide on-line information collection.

(For further information please contact Mr S Sarkar, Technical Director, Teleinformatics Development Promotion Project, National Informatics Centre, A-Block, CGO Complex, Lodhi Road, New Delhi - 110 003).

The involvement of NIC in the Tenth lok Sabha Elections resulted in a rich harvest in experience. Problems faced, and how to tackle these in the future, plans for improvement and new ideas are the manifestations of experience. An example is in what Mr Mohan Reddy, Software Development Project Leader, Headquarters, has to say on the collection of candidate names and their party affiliations:

"One system improvement that will definitely be required will be in the collection of candidate names and party affiliations through a forms program similar to ELECT. Last time, this voluminous basic information was sent in over NICMAIL, and had to be typed in again at Headquarters. Thanks to the two trial runs, the DIOs were able to point out all the spelling mistakes and wrong party assignments. But all of us have other urgent matters to attend to in those last few days, and we have to avoid this duplication of effort."

DIOs are requested to contribute similar feedbacks. We will publish the most interesting ones here, but all articles will be studied at Headquarters for ideas and information. State Informatics Officers are also requested to enlighten us on the state level planning they have to undertake for the elections.
