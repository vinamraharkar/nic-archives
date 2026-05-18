---
title: "De-Mystifying Technology behind Dynamic Portals"
publication: "Informatics"
issue_date: "January 2004"
pages: [17, 23]
author: "Rama Hariharan, NIC HQ"
section: "T ECHNOLOGY UPDATE"
---

## De-Mystifying Technology behind Dynamic Portals

With the advent of the Internet and the recognition of the potential of web sites as a prime vehicle for disseminating information, web sites evolved into two major areas. One was the evolution of web applications. Web applications provided the necessary dynamism to web sites by interacting with the organizational database. They practically dispensed with the need for the continued support of a web page designer and also eliminated the problems of inconsistency that might creep in due to manual re-entering of the data and the time lag caused due to manual updation process.

Another direction in which web sites evolved was the development of web portals. Web portals are special web sites that address a wider spectrum of the domain. A web portal may be a public portal, available on the Internet or an intranet portal, available only to the employees and partners of an organization.

However, as the complexity of web portals and sophistication of the end-users increased, it became difficult to sustain the management of the portal through manual processes. The obvious outcome of the above developments was the marriage between static web portals and the dynamic web applications, resulting in what is well known today as dynamic web portals.
A number of dynamic portal solutions are available in the market, the major ones include IBM’s WebSphere, Enterprise Information Portal, Lotus K-station, Microsoft’s SharePoint Portal Server and Oracle’s Oracle9iAS, to name a few.

?| Features
Dynamic portal solutions vary widely in their feature offerings.
?    Distributed Content management with facility for taxonomy creation, automatic tagging and indexing of content
?    Workflow Management
?    Powerful search facilities
?    Personalization at the level of the organization, a community or group of users and also at the individual level
?    Subscription & alert facilities
?    Analysis reports based on user profile & navigation data
?    Security features that may be rule-based or role-based or both
?    Multilingual Support
?    Facility to plug-in custom modules

?| Architecture
A dynamic portal solution framework generally adopts a three-tier architecture
?   The front-end tier interacts with the users. Invariably, there are two user interfaces. The first interface interacts with the target end-users of the portal. They visit the portal site to access the content posted in the portal. The second interface is typically a management console that facilitates content contributors & portal administrators to handle various portal management activities such as content management, workflow management, multilingual support, plugging in custom modules etc. There is no direct interaction between the two front-end interfaces. The changes administered through the management interface are persisted in a persistent store. The data from the persistent store is retrieved by the web server (with the help of the middle tier) and rendered on the portal site as per the needs of the end-users.
?   The middle tier consists of a web server and an application server such as COM+ or J2EE server. The application server hosts pre-built & custom-built software components.
?   The persistent store acts as the data tier of the portal solution. It consists of a database, a content repository where the content files of the portal are stored and an authentication source, which houses the user details & is used to validate the authenticity of the visiting end-user.
Besides the architecture adopted by dynamic portal solutions, a number of design issues also need to be addressed. Major issues are:

?    The ability to use any front-end device to access the portal as well as use any layout requires a finer level of differentiation where the presentation data is further separated from the presentation logic itself. This is generally achieved by using XML to describe the structure of the presentation data.
?    Since every element that gets displayed on the front-end is retrieved from the persistent store, it could negatively impact the performance of the portal. In order to reduce the load on the back-end database, extensive caching is used. Frequently accessed content that is more or less static are retrieved from the database and cached in the web server as HTML or XML fragments or files. These cached fragments are updated automatically as and when changes are applied to the underlying database.
?   To facilitate quick & easy search, the content contributor is required to tag the content with attributes such as author, title, keywords etc. Wherever possible, each attribute is stored within the file, as meta-tags in HTML documents and in the document properties of the documents such as Word, Excel etc. Documents for which information cannot be directly written into the files (e.g. .exe file) have an HTML stub file created for them which stores the content attributes as meta tags and have a redirect to the actual file. Sometimes, keywords are built dynamically based on user search.
?   Multilingual support is extended to the portal by storing all labels, messages etc. in the database. To boost performance, these labels are retrieved and cached in the web server.
?   Personalization is carried out through explicit as well as implicit profiling. Explicit profiling is achieved by explicitly asking the user to state his/her preferences when signing up. In implicit profiling, user behavior is captured invariably through a web log, which is then analyzed to judge user preferences. Both explicit as well as implicit profiling, when combined with user details, provide analytical insights that can be used to improve the site.

The paucity of space restricts a full-blown discussion on many more challenging design issues handled by such portal solution frameworks. Attention may, however, be drawn towards the development of a similar solution framework by NIC.

eNRICH (http://enrich.nic.in) was conceptualized, jointly by NIC & UNESCO, as a simple browser-based solution to enable rural communities to access information they need through a single one stop portal. Though any of the above portal solutions could have been used, the need was for a very low end computing solution that could be installed in a desktop environment.

eNRICH was further enhanced to cater to the need for the development of block community portals for the 487 blocks under the Community Information Centre (CIC) project of the 7 North-Eastern states and Sikkim. Some of the features offered by eNRICH include:

?    Content management including facility for building content taxonomy, distributed content contribution (by CIC operators, domain experts & government functionaries), provision for content tagging, moderation of content etc.
?    Role-based security
?    Personalization at the level of block community as well as individual both in terms of appearance as well as content
?    Analysis reports based on the user profile & navigation data
?    Multilingual support
?    Search facilities
?    Sharing of content among multiple online block communities

eNRICH is also being customized to generate dynamic portals for more than 550 DRDAs of the country. Efforts are also underway to customize eNRICH to act as an integrated solution for health workers in PHCs, allowing sharing of health related information as part of WHO’s Health Inter Network Pilot Project. All these customization efforts are providing valuable insights for making the portal framework more generic.

Dynamic portal frameworks offer opportunities to address a wide spectrum of application areas ranging from a highly complex one-stop, integrated government portal such as the proposed India Online portal on the one hand to a fairly simple portal required by a large number of rural communities who lack the technical expertise to manage the portal.
