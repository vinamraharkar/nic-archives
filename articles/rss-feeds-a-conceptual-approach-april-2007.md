---
title: "RSS Feeds- A Conceptual Approach"
publication: "Informatics"
issue_date: "April 2007"
pages: [15, 20]
author: "M Manivannan, Kapil Kr Sharma, A Venkatesan"
section: "Technology Update"
---

## RSS Feeds- A Conceptual Approach

Background
Netscape is the originator of the RSS concept where the objective was to have an XML format that would get news stories and information from other sites and have them automatically added to their site. Many newspapers groups also realize the potential of RSS feeds as an easy way to share headlines and increase their audience.

What is RSS Feed ?
RSS is an XML format that provides a technique where users access some parts of a web site without directly visiting the site. RSS formats provide web content or summaries of web content together with links to the full versions of the content, and other meta-data. This information is delivered as an XML file called RSS feed. Feed is simply a set of items known as “entries”, each with an extensible set of attached metadata. Publishing data by RSS feeds is known as Syndication. Items published through an RSS feed are said to Syndicated.
Since RSS is an XML format and therefore needs to be processed before it can be viewed/read. Typically the XML document is made available on a web server and can be pulled down by an RSS reader (also called an aggregator). The reader then automatically rechecks the RSS files in the user’s list - according to a schedule defined by the user - to see whether new content has been added. RSS is generally created by server side software (usually written in a language like PHP, Java, C# or Python) on the web server.

Feeders/Aggregators
RSS reader is an application that provides the way to read the RSS file by checking RSS-enabled web pages on behalf of a user and display any updated articles that it finds. These aggregators can be Web based or Stand alone programs.
• Web based Feeders/Aggregators require no software installation and make the user’s “feeds” available on any computer with Web access.
• Stand alone Feeders/Aggregators are programs which can be downloaded and used on the desktop as standalone programs
Current Browsers like Microsoft’s Internet Explorer version 7.0, Mozilla’s Firefox, Opera etc include a built-in RSS reader as a standard feature.

RSS Versions
There are currently multiple versions of RSS in use including RSS 1.0, RSS 2.0 and many deprecated versions. Both RSS 1.0 and RSS 2.0 are being separately and independently developed i.e. RSS 2.0 is not next version RSS 1.0
As there are a number of different versions of RSS therefore RSS can stand for ‘Rich Site Summary’, ‘RDF Site Summary’ or ‘Really Simple Syndication’ depending on which version is being mentioned. They are brief explained below
• RSS 0.91
In this Version RSS stands for ‘Rich Site Summary’. This is the original version of RSS created by Netscape.
• RSS 1.0
In this version RSS stands for ‘RDF Site Summary’. RSS 1.0 utilizes the Resource Description Framework (RDF) which is the W3C recommendation for metadata. This is more modular, with many of the terms coming from standard metadata vocabularies such as Dublin Core.
• RSS 2.0
In this version RSS stands for ‘Really Simple Syndication’ and it follows on from the various RSS 0.9x specifications (RSS 0.90, RSS 0.91, RSS 0.92, RSS 0.93 )
• Atom
This is yet another feed format. Atom is an XML-based document format that describes lists of related. an XML-based Web content and metadata syndication format. The primary use case that Atom addresses is the syndication of Web content such as weblogs and news headlines to Web sites as well as directly to user agents.
The various Feed specifications are not fully compatible with each other, though many feeder softwares have been able to support multiple versions.

How does RSS works ?
The RSS format for syndication works in following manner
1. Sets of web pages to be displayed by websites are identified. This set of pages will be the RSS feed.
2. An XML file that defines the RSS feed will be created. This file holds URL, title and summary of each page to display.
3. Anybody wishing to use the RSS feed gets an RSS reader and adds (subscribes) the feed by putting the URL of the RSS feed in the aggregator. A website can also display the RSS feed by loading the RSS file from the provider. When someone visits the website of the receiver, the script is launched; it recalls the RSS file from the provider’s website and displays a list of news from extracted data.
4. By a click on a line of the list, visitors display a page from the provider.
5. Filename extensions with RSS can be filename with an .xml, .rss, .rdf or any other extension. The important thing is that web server must be configured to serve RSS files using a mime type of text/xml.

Example
As an example of Viewing RSS feeds we can visit the site http://egovstandards.gov.in/ and click on the RSS, it takes to feeds page where this portal offers many RSS feeds.
For this example, click on feed for ‘White Papers’. The browser would show the URL as http://egovstandards.gov.in/white_papers/RSS and the XML document in fig.1 would show up. (This is nothing but the RSS feed)
To understand what is being shown by this feed, we need to subscribe this URL in our feeder/aggregator. (Refer to Help on using RSS feeds on this site). Now whenever the “White Papers” are updated the aggregator will inform subscriber of this feed accordingly.

FEED Validation Service
This is the W3C Feed Validation Service, a free service that checks the syntax of Atom or RSS feeds. One can visit http://validator.w3.org/feed/ for accessing this service.

Conclusion
Governments, Publishers and content providers can create RSS feeds for information that is of interest to the public and allowing an individual to pick or personalize the list of feeds. This way the content can be accessed by a much broader audience. For portal administrator, new content can be easily integrated into web sites or portals, and for end users easy access to new content is greatly facilitated.

For further information, mail to egov@nic.in

Identifying the RSS feeds on Portal
Portals tell their users/visitors about RSS feeds by various Icons. Some of the popular ones are as below..
There is however no standard Icon for RSS feeds.
