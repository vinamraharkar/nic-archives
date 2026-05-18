---
title: "OpenLDAP: Open Source Implementation of Directory Services"
publication: "Informatics"
issue_date: "July 2008"
pages: [36, 37, 39]
author: "Saroj Kumar Patro"
section: "Technology Update"
---

## OpenLDAP: Open Source Implementation of Directory Services

The existence of multiple applications in a department/organisation each having to maintain its own user (employee) information database has led to ambiguity, discrepancies & redundancy in user data, often times. Further, users need to be enabled with multiple logins for accessing data from various sites within their own department. All this and more, has made the need for departments to have a Centralized Directory Service that will serve as an information repository for user management and authentication. An Open Standards based Directory Server meet the needs for and provide a secure repository for storing user credentials and related information of the ministry/department employees.

OpenLDAP, an open source and standards-based implementation of directory service, has been used in the IntraGOV (Intranet for Government) portals to maintain the user data in a central repository. This enables the authentication from a single and common base of information, regardless of the geographical location

This has been implemented in IntraGOV portal of Govt. of Andaman and Nicobar (IntraAND), Govt. of Sikkim (IntraSikkim) and Govt. of Orissa (IntraOrissa) to store their employees (Sikkim-28000, A&N-30000) basic details.

OpenLDAP is a LDAP compliant Open Source suite of directory software developed by the Internet community based upon prior work by University of Micheigan, freely downloadable at http://www.openldap.org/, its binary and source code available for all major platforms under the OpenLDAP public license. It includes: LDAP Server (slapd), LDAP replication server (slurpd), Software Development Kit (ldap), Utilities, tools, sample clients, and contributed packages.

LDAP, light weight Directory Access Protocol, based on the X.500 standard, widely used Internet Standard Protocol (runs over TCP/IP) for accessing information stored in an information directory (also known as an LDAP directory), such as organizations, individuals, phone numbers, addresses, customer details and etc.

The key advantages of LDAP are Cross-platform and open standards-based, Internationalization using Unicode Transformation Format, Support for Secure Sockets Layer and Simple Authentication Security Layer, One of the best ways to achieve the Single-Sign-On, Easy and Effective means to Replicate Data, Secure delegation of control access using Access Control List.

Open LDAP Server architecture

The LDAP directory service is based on a client-server model.

LDAP Models

The four basic models of LDAP are as follows:

*   Information model: It describes the structure of information stored in the LDAP directory. LDAP directory servers store their data hierarchically, that provides a method for logically grouping (and sub-grouping) certain items together, useful in a number of ways such as: Replication of Data, Security and Access Control, Scalability, and etc. The basic unit of information stored in the directory is called an entry. Entries represent objects of interest in the real world such as people, servers, organizations, and so on. Entries are composed of a collection of attributes that contain information about the object. Every attribute has a type and one or more values. The type of the attribute is associated with syntax. The syntax specifies what kind of values can be stored, how those values behave during searches and other directory operations.

Some of the LDAP Attribute Syntaxes are: dn - Distinguish name, int - Integer, ces - case exact string, tel - telephone number and etc.

| Attribute, Alias | Syntax | Description | Example |
| :--------------- | :----- | :---------- | :---------------------------------------------------- |
| common Name, cn | cis | Full name | Saroj Kumar Patro |
| surname, sn | cis | Surname | Patro |
| Telephone Number | Tel | Telephone number | 011-24305049 |
| organisation, o | cis | Organisation name | Nic |
| organisational Unit Name, ou | cis | Organisational unit name | Employee |
| Owner | dn | Distinguished name | cn=Saroj Kuamr Patro, ou=employee, o=nic, c=in |

Schema, data model of an information directory, defines the type of objects that can be stored, list the attributes of each object type. It helps maintaining consistency and quality of data.

*   Naming model: It describes how the information, entries in the directory is organised and identified. Entries are organised in a tree-like structure called the Directory Information Tree (DIT). Each entry has an attribute that is unique among all siblings of a single parent, called as Relative Distinguished Name (RDN). You can uniquely identify any entry within a directory by following the RDNs of all the entries in the path from the desired node to the root of the tree. This string created by combining RDNs to form a unique name called Distinguished Name (DN).

The directory's top level, referred to above as the root of the directory tree, is also known as the base. The name of that base is the Base Distinguished Name, or base DN. In principle, it's up to you to choose the format for your base DN.

Recommended base DN format for the organizations having the Internet presence say nic.in for NIC is: dc=nic, dc=in. "dc" stands for "Domain Component."

LDIF

The LDAP Interchange Format (LDIF) is a standard text file format for storing LDAP configuration information and managing directory contents. A typical directory entry represented in LDIF:

dn: uid=nic5121, dc=nic, dc=in
uid: nic5121
objectClass: person
cn: Saroj Kumar Patro
sn: Patro
telephoneNumber: 011-24305049
mail: sk.patro@nic.in
userPassword: {SSHA}aknbKIfeaxsfgtds

The attribute userPassword stores the password of a person in encrypted form using SSHA - Salted Secure Hash Algorithm.

Some other common encrypting methodologies LDAP supports are: {CRYPT}, {MD5}, {SHA}(Secure Hash Algorithm).

*   Functional model: It describes what operations can be performed on the information stored in the directory. LDAP has nine basic protocol operations, which can be divided into three categories viz:

*   Interrogation operations: search, compare
*   Update operations: add, delete, modify, modify DN (rename)
*   Authentication and control operations: bind, unbind, abandon

Bind operation is client authentication to the directory, unbind operation is to terminate a session, and the abandon operation allows a client to abruptly terminate the session.

*   Security model: It describes how the information in the directory can be protected from unauthorized access.

OpenLDAP (LDAPv3) provides following mechanisms for authenticating clients:

*   Simple Authentication: For Simple Authentication, the login name in the form of a DN is sent with a password in clear text to the LDAP server.
*   Simple Authentication over SSL: Sending usernames and passwords over the network, wrapping the information in an encrypted transport layer. LDAP can negotiate an encrypted transport layer prior to performing any bind operations.
*   Simple Authentication and Security Layer (SASL): SASL supports a pluggable authentication scheme by allowing a client and server to negotiate the authentication mechanism prior to the transmission of any user credentials using SSL.

Once users are authenticated, it must be determined if they have the authorization or permission to perform the requested operation on the specific object. Authorization is often based on access control lists (ACLs), attached to objects and attributes that describe what type of access each user is allowed.

Thus implementing a Centralised Open LDAP Server, enables an organisation-wide Authentication System, integration of applications with a unified sign on and provides a single authoritative source for user management, roles, and hierarchy helping to maintain the data integrity of users. Personalized, role-based, secure access to information is thus enabled for each and every authorised employee in a department/ organisation.
