---
title: "NIC's Election Experience: A Rich Harvest"
publication: "Informatics"
volume: 1
issue: 2
date: "October 1992"
pages: [4, 5]
author: null
section: "Cover Story"
---

## NIC's Election Experience: A Rich Harvest

The Tenth Lok Sabha Election heralded a new dimension in the elections process --- the large-scale use of
computers and satellite-based computer networks. The difference was felt as the Nation watched the election
results bulletins and analyses by Pranoy Roy and Vinod Dua with awe and admiration. Few however realized that
the show was, in essence, being run by people who worked with their terminals round-the-clock. Mr S Sarkar,
Technical Director, Teleinformatics Development Promotion Project (TDPP), NIC, speaks on the
role and relevance of NIC in this great exercise considered to be the foundation of any democracy.

For all of us in the National Informa-
tics Centre, the Tenth Lok Sabha
election was something of an eye-
opener. We learnt that society renews and
invigorates itself through elections, and all
those who participate in the electoral proc-
ess are themselves invigorated by it.


> **[Image]** *The image is a schematic diagram titled "COUPLING OF NICNET AND TV BROADCAST NETWORKS." It illustrates a hierarchical communication flow between two entities: the "DDK" (Digital Distribution Kernel) and the "NIC" (Network Interface Card). The diagram is set against a pale yellow background. 

The flow originates from the bottom with "440 DISTRICTS," represented by numerous arrows pointing upward. These arrows converge on the "NIC" box. From the "NIC," arrows point upward to the "DDK" box. 

The diagram includes a specific data annotation: "25 MILLION TELEVISION SETS" is written to the left of the "DDK" box. From the "DDK," multiple arrows radiate outward in a fan-like pattern, representing the broadcast signal. These arrows are depicted as dashed lines with arrowheads, indicating the direction of signal transmission. The diagram visually represents the coupling of the NICNET network with the TV broadcast network, showing how signals are distributed from a central hub (NIC) to a large number of destinations (440 districts) via the DDK.*


### The Credibility Factor

In a democratic society, elected rep-
resentatives can govern effectively only if
their electoral victory is deemed credible
by all citizens. Apart from vote casting, it is
vital that vote counting be fair, and also be
seen as fair. This implies immediate round-
by-round result reporting for each constitu-
ency to as large an audience as possible.

Should this not happen, the upshot
can be disastrous. The example of the re-
cent elections in the Phillipines is a case in
point. Although the actual voting went
through fairly smoothly, counting and tabu-
lation took over a month. This lead to all the
candidates making rigging and tampering
charges, and the resultant damage in over-
all credibility. Considering that India has
eleven times the land area and fourteen
times the population of the Phillipines, the
importance of the result reporting process
for India is obvious.


### The Indian Solution

That India found a reliable and nearly
instant solution for reporting election re-
sults was resoundingly demonstrated dur-
ing the nation-wide parliamentary elec-
tions to the Tenth Indian Lok Sabha.

The Solution was to couple the tele-
vision network as an output channel for
NICNET, thus combining the information
collecting power of the satellite data net-
work with the nation-wide broadcast ca-
pability of Doordarshan. The coupled net-
works achieved a tremendous throughput
of public information that sustained public
interest in, and monitoring of, the results
counting process.


### Build-up to the Polls

The Results Information Network

benefitted from the close
relationship built up by our
District Informatics Officers
with their respective Dis-
trict Collectors long before
the counting day. The NIC
district offices and State
Headquarters provided vi-
tal NICMAIL links in the
communication chain be-
tween the State Chief Elec-
toral Officer and his Re-
turning Officers in the dis-
tricts. This allowed the mas-
sive logistics involved to be
more closely supported.

In many districts, the
DIOs went one step further
and offered local comput-
erized planning support to
the District Commissioner,
who in most cases was also
the Returning Officer. ELE-
CON was the most widely
used of these packages, de-
veloped by the DIOs them-
selves based on their local
requirements.


### Significance of
Success

The success of NIC's
elections projects demon-
strated several points cru-
cial to the future of NIC.

NICNET perfomance was proved in
a "worst case" situation of on-line load. All
previous experience had been with indi-
vidual terminals connected to different
applications at different times in the nor-
mal time-sharing way. The Lok Sabha elec-
tions was different because all NICNET ter-
minals had to be connected to the same ap-
plication at the same time, thus testing
NICNET and the NEC host to the extreme.
NEC had to be completely reconfigured by
the ACOS unit to handle this new usage.

More significantly, the elections
exercise revealed hidden depths to NIC's
organizing ability. This was most clearly
demonstrated by the personal enterprise
and dedication shown by the District Infor-
matics Officers and Assistants in getting the
results from counting rooms and entering


### TECHNICAL OVERVIEW

The Elections Results Network was composed of three functional
layers. The bottom layer was the communications backbone, con-
sisting of the normal NICNET configuration of one micro-earth
stationat each of the 440 district collectorates, all connected to the
Master Earth Station packet switch at Delhi via the INSAT-1D
satellite.

The second layer consists of the NEC S-1000 large mainframe
with the Elect results entry software at NIC headquarters and the
PC/386s and dumb terminals, one at each district collectorate. This
layer used the underlying communication backbone to exchange in-
formation. Menu screens and prompts were emitted from the NEC
to the network via the packet switch, while commands and round-
by-round results flowed in from the district offices.

Forming another part of the second layer were the specially
written communication modules which enabled the NEC to transmit
the results out to the presentation locations.

The third functional layer consisted of hardware and software
that consolidated and presented the results. Consolidated results
were presented by a third level programme on NEC that read
detailed constituency files provided by the ELECT module and
output statewise party positions and overall national party position.

At remote sites the presentation hardware included:

the NDTV television graphics generator at Doordarshan Delhi
studios. This provided colourful templates into which the results
data could be slotted, and output in the form of a PAL TV signal,
suitable for national telecast by Doordarshan.

three 486 machines at NIC Headquarters, used for interactive
retrieval of results by all sites hooked up with NICNET.

a PC/386 at the Press Information Bureau (PIB) for generating
printouts of query answers for newspaper reporters.

them over a period of 48 hours, often
without sleep. In those cases where
counting for one parliamentary con-
stituency was split up over several
district collectorates, the State Infor-
matics Officer and DIOs concerned
responded by organizing their own
NICNET sub-networks to accumu-
late round results for that constitu-
ency at one place before using the
ELECT program.


### Future Possibilities

In view of the current liberaliza-
tion effort underway in the Govern-
ment, it is possible that NIC may be
able to offer its services to private us-
ers. The Elections Results Network is
an example of the wide area on-line
capability of NICNET. A head office
anywhere in the Country can collect
data from remote warehouses, facto-


> **[Image]** *The image is a schematic diagram illustrating the "NICNET" (National Informatics Centre Network) infrastructure for the "THE NETWORK 1991 ELECTIONS" in India. The diagram is organized into a central hub and radiating nodes. The central hub is a large rectangle labeled "NICNET". Surrounding this hub are various nodes representing different entities and their connectivity. At the top center is the "LOK SABHA" (Indian Parliament). To the left of the Lok Sabha is the "DICs/State Hqs" (District Information Centres/State Headquarters). Below the Lok Sabha is the "DOORDARSHAN NETWORK" (a blue box), and to the bottom right is the "PIB" (Planning Commission). On the left side, three computer monitors are connected to the NICNET hub. On the right side, two computer monitors are connected to the NICNET hub, and above them is a label "CEO's Offices at State Level". A vertical arrow labeled "Latest Position Display" points upward from the center of the NICNET hub towards the Lok Sabha. The diagram visually represents the network architecture connecting central government offices, state headquarters, and the CEO's offices.*

ries and offices not only for Management
Information Systems, but also for daily op-
erations streamlining. Lower inventories
could be maintained, shipments could be
monitored, and any emerging shortage or
irregularity could be spotted in advance.

The Elections Results Network points
the way to all these future applications.The
role of the National Informatics Centre in
the 1990 elections has paved the way for
extensive use of computer networks in
nationwide on-line information collection.

(For further information please contact
Mr S Sarkar, Technical Director, Telein-
formatics Development Promotion Proj-
ect, National Informatics Centre, A-Block,
CGO Complex, Lodhi Road, New Delhi -
110 003).

The involvement of NIC in the Tenth lok Sabha Elections resulted in a rich harvest in experience. Problems faced, and how to tackle these
in the future; plans for improvement and new ideas are the manifestations of experience. An example is in what Mr Mohan Reddy, Software
Development Project Leader, Headquarters, has to say on the collection of candidate names and their party affiliations:

"One system improvement that will definitely be required will be in the collection of candidate names and party affiliations through a forms
program similar to ELECT. Last time, this voluminous basic information was sent in over NICMAIL, and had to be typed in again at Headquar-
ters. Thanks to the two trial runs, the DIOs were able to point out all the spelling mistakes and wrong party assignments. But all of us have other
urgent matters to attend to in those last few days, and we have to avoid this duplication of effort."

DIOs are requested to contribute similar feedbacks.We will publish the most interesting ones here, but all articles will be studied at
Headquarters for ideas and information. State Informatics Officers are also requested to enlighten us on the state level planning they have to
undertake for the elections.


### PHOTOTALK

The underground Master Earth Station (MES) with its antennas against a back-
drop of the SAIL Building adjoining NIC Headquarters at Lodhi Road, New Delhi.


> **[Image]** *The image presents a composite scene featuring a large, white satellite dish in the foreground, superimposed over a background of a campus-like environment. The satellite dish is centrally located, with its dish facing upwards and a conical feed horn at its center. It is positioned on a grassy area, with a white railing structure visible in the lower-left foreground. The background consists of several large, reddish-brown brick buildings with arched windows and multiple stories, suggesting an institutional or university setting. These buildings are partially obscured by green trees. The sky is a pale, overcast grey. The overall image appears to be a photograph with a graphic overlay, possibly for illustrative purposes.*

