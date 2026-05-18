---
title: "C Library for xbase Products"
publication: "Informatics"
issue_date: "April 1997"
pages: [7]
author: "From our Assam Correspondent"
section: "Products/Services"
---

## C Library for xbase Products

The existence of a large number of databases in FoxBase+ format in NIC necessitates porting of these to ORACLE table structure in case it is decided to switch over completely to ORACLE, or integration is required between ORACLE and FoxBase databases. Complete porting of FoxBase+ databases to ORACLE again results in the problem of non-accessibility of ORACLE tables from previous applications. In order to solve this problem, the NIC Assam State Unit has developed a C Library (cdbflib) for xbase products which will enable application developers to access data from xbase databases (including index files) and integrate it seamlessly in a Pro*C programme. In such an application, embedded sql statements will access the data from ORACLE tables and library (cdbflib) functions will access data from dbf files.

Actually, the library developed is not only for ORACLE-xbase integration but can also be used independently for application development using C with functions having the same look and feel as their xbase counterparts. It includes most of the functions for database access, modification, use of index files, screen input-output, string and date functions etc.

Developers conversant with xbase environment and willing to switch over to C will certainly find this library useful. It presently runs under XENIX/SCO UNIX Rel 3.2/ Unixware.
