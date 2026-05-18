---
title: "Open Source GIS Software"
publication: "Informatics"
issue_date: "October 2008"
pages: [36, 37]
author: "R. Gayatri"
section: "Technology Update"
---

## Open Source GIS Software

During the past few years, GIS has seen an exemplary growth in both the Government and Private Sectors. The GIS technology that was once considered too specialized has become just another widely talked about and essential enterprise technology.

GIS - as a good decision support tool, can be effectively used for managing, analysing and decision making, by seamlessly combining both spatial and non-spatial data. The maturity of Open Source Software (OSS) in the GIS arena has been highly impressive for obvious reasons. Distributed data environments, widespread deployment of custom software and strong in-house skills can be realised through the OSS.

Common Libraries
Many libraries are commonly shared among several desktop / server software for common functionalities. These include:

General Libraries
Library Purpose
Geographic Database Abstraction Library / Open GIS Vector Read/Write Library (GDAL/OGR) Support variety of raster and vector formats of both commercial and GIS OSS
Projection (Proj4) To enable on the fly projection changes
Java Topology Suite (JTS) An API of 2D spatial predicates supporting open GIS geometries & methods (JAVA)
Geometry Engine Open Source (GEOS) Open GIS geometries & methods similar to JTS in C++
GeoTools Java GIS toolkit for Open GIS with a core set of API interfaces and default implementations

Conversion Libraries
Library Purpose
ogr2ogr A command line utility bundled with GDAL/OGR
FDO Multi-format programming interface to read / write spatial datasets with locking, layers and access control features.

Simple Features Specification (SFS) for SQL

The JTS conforms to the Simple Features Specification for SQL published by the OGC and provides a complete, consistent, robust implementation of fundamental 2D spatial algorithms. GEOS also includes all the OpenGIS - Simple Features Specifications for SQL, spatial predicate functions and spatial operators, as well as specific JTS topology functions.

Desktop Tools

GRASS, Quantum GIS, OpenJUMP, uDig, gvSIG, OpenEV, Saga GIS, OSSIM and GMT are a few tools available as Desktop Software. While some of these tools enable viewing of spatial data as “GIS viewers” only, others provide spatial and attribute editing capabilities. Some are good at processing/ analysing GIS data. GRASS, OpenEV, Quantum GIS are all implemented in the C/C++ Category. OpenJUMP, gvSIG and uDig are based on JTS. Of these, GRASS provides excellent editing and analysing capabilities. GRASS, OSSIM and GMT are Image Processing software.

R. Gayatri
Regional Informatics Editor
gayatri@tn.nic.in

Spatial Database Servers

Spatial databases are at the core of any GIS application. Of all the available open-source database projects, the most advanced engine in open source for spatial applications is PostgreSQL with PostGIS extension supporting spatial data storage and retrieval conforming to OGC's specifications. MySQL also provides a spatial extension. Conversion utilities are provided by the software that helps in export/import of spatial data in the popular “shape” format to MySQL or PostGIS tables. Most of the OSS GIS Software provides drivers for storage and retrieval of PostGIS datasets either directly or through OGR implementations. Some of the latest releases of leading commercial software are also providing PostGIS drivers.

Web GIS Servers

For web enabling GIS data and applications, a GIS Server that understands spatial data is required that runs in-sync with the Web Server. University of Minnesota's MapServer, University of Bonn's DeeGree and MapGuide from AutoDesk are a few quite popular open source GIS Servers. Of these, MapServer is supported by many Rapid Application Development tools like MapLab, Chameleon and ROSA Applet viewer, MapScript in PHP, Perl, Python and Java environments.

GIS Web Services
GIS Web services are Internet applications that enable application developers to integrate GIS functionality into their Web applications without having to build GIS functionality or to host the spatial data locally. Web Map Service (WMS) and Web Feature Service (WFS) are promising services to work on collaborative / distributed GIS environments in the National scenario. The web services need to be OGC compliant so that these services could be consumed by any other GIS software open source or proprietary. While WMS will stream only an image at the client, WFS will stream the vectors to the client that supports queries, analyses and editing of simple features like adding point / line features (WFS Transaction) from the client end. The clients for these services can be any web browser based application or any GIS Desktop tool that supports OGC Specifications for Web Services.

Ka-Map, MapBuilder and Open Layers are some of the toolkits that provide AJAX based streaming modes of display (similar to Google maps) and editing capabilities. MapBender and Cartoweb are two major frameworks based on PHP / Javascript technologies that can provide more advanced and customisable applications.

Few of the Open Source GIS Implementations at NIC

The RS & GIS division at NIC, HQ is equipped with the required infrastructure to create and process spatial information for the entire country. In-house software development programme is supported in parallel for the products such as GISNIC, IPSNIC and GeoNIC to provide a low cost solution to meet the GIS needs in various sectors.

At NIC, Tamil Nadu State Centre, GIS Solutions for Internet based applications have been explored and implemented using OSS.

The General Land Records information on Raksha Bhoomi software, an Intranet application for Directorate General of Defence Estates has been integrated with a GIS interface that depicts respective Defence owned cantonment areas up to Survey number / sub division number level.

Interestingly, some rapid developments are underway through .Net GIS Communities. NTS (Net Topology Suite) - following the lines of JTS and Proj.Net following Proj4 libraries are under development. MapWindow, WorldWind and SharpMap are some of the emerging tools in the .Net scenario that utilise the above said libraries and native GDAL/OGR libraries.

Well-knit user communities helping developers / users through mailing lists shred the apprehensions on OSS. The large portion of the costs incurred by an organization embarking on an Enterprise wide GIS implementation, are in data conversion, hardware, software, system implementation and customization. By leveraging OSS, any organization can reap the benefits of cost effective implementations and subsequent maintenance. By hosting Internet/Intranet GIS applications, it is possible to provide planners, research scholars, administrators and others to use GIS technology as a good decision support tool for the upliftment of the society in general and for better utilisation of all resources.

For further information,contact
tngis@tn.nic.in
