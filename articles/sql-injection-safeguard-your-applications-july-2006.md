---
title: "SQL Injection Safeguard your Applications"
publication: "Informatics"
issue_date: "July 2006"
pages: [17]
author: "Punam Gupta & Vanashree Ramteke, NIC Pune"
section: "Technology Update"
---

## SQL Injection Safeguard your Applications

What is SQL injection?
SQL injection is a hacking technique used to exploit web applications that use client-supplied data in SQL queries without validating the input. This is one of the most common application layer attacks currently being used on the Internet. The technologies vulnerable to this attack are dynamic scripting languages like ASP, ASP.NET, PHP, JSP, CGI, etc. This kind of attack is not a technological security hole in the Operating System or server software, but rather it depends on the way a web site is developed. Some developers are unaware of this kind of attack and unknowingly develop web applications which open doors for hackers to inject SQL Queries / Commands into the system.
Techniques of SQL Injection
The basic concept behind a SQL injection attack is that a web-page allows the user to enter text into a textbox that is used to execute a query against a database. A hacker enters a malformed SQL statement into the textbox that changes the nature of the query so that it can be used to break into, alter, or damage the back-end database. The level of security set by the database and the coding of the website determines the type of access the attacker gets on the database. In general, the SQL injection happens through two modes
1. Access through Login Page -
The easiest SQL injection is to bypass the logon forms where the user is authenticated against a password supplied by him.
· Using ‘or’ condition – the attacker bypasses the username/password authorization using (‘or 1=1-) code in the password field.
· Using ‘having’ clause - ‘having’ clause can be used to know the database table name with its attribute, the error message tells the attacker the name of one field from the database.
· Using multiple queries - SQL Server, delimits queries with semi-colon. The use of semi-colon allows multiple queries to be submitted as one batch and executed sequentially.
· Using extended stored procedures.
2. Access through URL
·By manipulating the query string in URL.
·Using the ‘SELECT & UNION’ statements.
The attackers use system tables - sysobjects & syscolumns to make a UNION statement and ascertain schema information for a database
Preventing SQL Injection attacks
The best way to defend against SQL injection attacks it to filter extensively any input that a user can give. One should ‘remove everything but the known good data’ and filter meta characters from the user input. This will ensure that only what should be entered in the field will be submitted to the server.
Escape Quotes
By using a simple replace function and converting all single quotes to two single quotes, one can greatly reduce the chance of an injection attack succeeding.
Sanitize the input or Remove Culprit Characters
Certain characters and character sequences such as ;, —, select, insert and xp_ can be used to perform an SQL injection attack. By removing these characters and character sequences from user input before we build a query, we can help in reducing the chance of an injection attack further.
Limit the Length of User Input
- Keep all text boxes and form fields as short as possible
- While accepting a query string value for a numeric field, always use a function to check if the value is actually numeric.
- Always use method attribute set to POST.
Prevention Principles
SQL injection attacks are a serious concern for application developers as they can be used to break into supposedly secure systems and steal, alter, or destroy data. E-Commerce web applications are most vulnerable to such attacks. Any application that queries a database using user-entered data is a potential target of an injection attack.
It is also important to realize that SQL injection attacks are not limited to MS-SQL Server. Other databases, including Oracle, MySQL, DB2, Sybase, etc. are also susceptible to this type of attack.
As far as SQL injection attacks are concerned – ‘prevention is the only cure’. All developers should take necessary precautions to thwart these attacks before they actually happen.
For more information, pls mail to punam@nic.in
