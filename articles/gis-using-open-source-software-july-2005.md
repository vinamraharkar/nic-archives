---
title: "GIS Using Open Source Software"
publication: "Informatics"
issue_date: "July 2005"
pages: [16]
author: "Mahalakshmi Narayanan, NIC Tamil Nadu"
section: "Technology Update"
---

## GIS Using Open Source Software

GIS has become an indispensable tool for managing, analyzing and decision making, by seamlessly combining both spatial and non-spatial data. The growth of Open Source Software (OSS) in the GIS arena has been sky-rocketing for obvious reasons. Distributed data environments, widespread deployment of custom software and strong in-house skills can be realised through the OSS.

| Desktop Tools
Open Source GIS currently fall under two categories viz. C and Java. GRASS, Thuban, uDig, JUMP/JCS, OpenMap, fGIS, Mapbender, Gratis are a few tools available as Desktop versions. While some of these tools enable viewing of spatial data as “GIS viewers” only, others provide editing capabilities and some are good at processing/ analysing GIS data. Java Topology Suite enables open GIS Geometries and Methods in the Java domain. OpenEV, QGIS, fGIS, Thuban are all viewers in the C Category. OpenMap, JUMP/JCS, uDig and GeoServer are based on Java Topology Suite (JTS). Of these, GRASS provides excellent editing and analysing capabilities and enables PostGIS tables’ storage/retrieval.

| Spatial Database Servers
Spatial data in many GIS software are stored in the form of flat files. Internet/Intranet/LAN based geographical data services involve management and sharing of both spatial and non-spatial (attribute) data. If spatial data could also be managed in an RDBMS environment similar to non-spatial data, it would allow:
• Easy storage/retrieval of spatial data
• Spatial data sharing across many applications possible
• Easier backup/restoration (maintenance)
• Efficient development and deployment of GIS applications.
The extension for storage of spatial data in RDBMS is provided by the two popularly known open source database servers: MySQL spatial extension and PostgreSQL/PostGIS extension. They also provide conversion utilities that export/ import spatial data in the popular “shape” format to MySQL - spatial table or PostgreSQL/PostGIS table.

| Web GIS Servers
For web enabling GIS data and applications, a GIS Server that understands spatial data is required that runs in-sync with the Web Server. University of Minnesota’s MapServer, University of Bonn’s DeeGree, JTS based GeoServers are a few quite popular open source GIS Servers. Of these, MapServer is supported by many Rapid Application Development tools like MapLab, Chameleon and ROSA Applet viewer, MapScript in PHP, Perl, Python and Java environments. MapServer also supports OGR vector formats, GDAL raster formats and on the fly projection support.

| Conversion Tools
Interoperability in GIS had been a major concern for GIS community. FW Tools under OpenEV supports conversion of spatial data from most of the standard GIS software to another including OSS (PostgreSQL/PostGIS) formats.

| Simple Features Specification for SQL
The JTS is an API of 2D spatial predicates and functions. It conforms to the Simple Features Specification for SQL published by the Open GIS Consortium and provides a complete, consistent, robust implementation of fundamental 2D spatial algorithms. GEOS (Geometry Engine - Open Source) is a C++ port of the JTS. This also includes all the OpenGIS - Simple Features Specifications for SQL, spatial predicate functions and spatial operators, as well as specific JTS topology functions.

| Open Source GIS Implementation at NIC
The RS & GIS division at NIC HQ is equipped with the required infrastructure to create and process spatial information. In-house software development program is supported in parallel for the products such as GISNIC, IPSNIC and GeoNIC to provide a low cost solution to meet the GIS needs in various sectors. At NIC, Chennai, GIS Solutions for Internet based applications have been explored and implemented using OSS. Two websites that have been launched with GIS solutions using Open Source are http://www.census.tn.nic.in and http://www.animaldiseaseinfo.tn.nic.in. The Census 2001 website includes the voluminous and valuable Primary Census Abstract, Disabled Population Data, Religion wise Population Data and Age wise Population Data. In the website, dynamic mapping and charting facility is included with PCA data, Disabled Population data and Housing & Households data apart from tabular data retrieval. The user can customize the map (for the ranges, colours, legends and titles) and get the output map in the required format. UMN MapServer GIS Server, PHP/MapScript and ROSA Applet were used for building the dynamic GIS pages in the website. Figure below shows a dynamic thematic map generated from Census 2001 PCA data.

| Conclusion
A well-knit user community which helps developer through mailing lists shreds the apprehensions on OSS. The large portion of the costs incurred by an organization embarking on a GIS implementation, are in data conversion, hardware, software, system implementation and customization. By leveraging OSS, any organization can reap the benefits of cost effective implementations and subsequent maintenance. By hosting Internet/Intranet GIS applications, it is possible to provide planners, research scholars, administrators and others to use GIS technology as a decision support tool for the upliftment of the society in general and for better utilization of all resources.

For further details, please mail to tngis@tn.nic.in
