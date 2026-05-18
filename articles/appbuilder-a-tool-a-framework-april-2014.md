---
title: "APPBUILDER: A Tool & A Framework"
publication: "Informatics"
issue_date: "April 2014"
pages: [23, 24]
author: "Deepak Goswami"
section: "Technology Update"
---

## APPBUILDER: A Tool & A Framework

Software developers quite often come across situations where fast prototyping of a software becomes absolutely essential. Most of these software are database-centric and CRUD (create, retrieve, update, delete) functionalities form about 30%-40% of the total development effort (if not more). Therefore, it will be of great help if forms with CRUD functionalities can be generated using some tools. AppBuilder is a code-generation software (and also a Framework) that auto-generates application objects such as Menus and Forms for Table Management.

AppBuilder is a code-generation software (and also a Framework) that auto-generates some of the application objects (e.g. Forms, Business Logic, Data Management Menus etc) using Database Metadata. With a well-designed database, a lot of details are already available in the Database Metadata, which can very much be used to generate application objects. Once a table is added to a database, a number of details are to be mandatorily defined, namely- Name of the Table, Name of the Columns, their type, length (if applicable) etc. A properly designed database contains other additional non-mandatory information like Descriptions (i.e. not only cryptic names) of Tables and Table Columns, definitions of Primary Keys, Foreign Keys and Unique Constraints. All these metadata details are available through various system views and tables. In order to generate a simple menu for table management, the descriptive names for tables are good enough as Menu Options. For generating a Form for a table with CRUD and other features, one needs to know the Column Descriptions, Length, Type (for display and validation), Foreign Keys and Unique Constraints for creating Drop-down-lists. An effort also has been made to generate application objects with an Object-Oriented (OO) approach. AppBuilder generates application objects such as Menus and Forms for Table Management. It is presently available in its best shape for JEE/PHP and MySQL/PostgreSQL database; but it is available under various stages of development for .NET and MS SQL Server 2000 and 2005 databases.

A form generated with AppBuilder with a few modifications

A Table Management Form for a table is created with the name <tablename>Form.php, it displays all the columns of the database table; normal columns are displayed with a Label (showing the Column Description if available, otherwise the Column Name) and TextField combination (TextField has proper length restriction); a Date Column is shown with a TextField and a Calendar control; all not-nullable columns are marked with a * to indicate these cannot be left blank; a Foreign Key Column is shown with a Drop-down List. The Drop-down List in such cases is created by using the Primary Key Column and the Unique Column of the referred table. This approach has been adopted on the basis of the author's observation of a large number of softwares that Drop-down Lists in Forms always refer to Foreign Keys; also the Text part (i.e. the part shown in such a list as distinct from the Value part which is normally not shown) of a Drop-down List always refers to the Descriptive part of a table row, which preferably should be unique (i.e. some kind of alternate or candidate key). In case such a Unique Column (apart from the Primary Key) cannot be defined for a table because of syntactic reasons, the most appropriate Column needs to be manually inserted in the generated Code. The basic CRUD operations are definitely parts of such a Form; Insertion, Retrieval, Updation and Deletion of a Record are basic features of such a Form; in addition, it provides a facility to list all records or list selectively depending on some filter criteria. While listing records, all Foreign Keys are replaced by their actual Descriptive Columns (e.g. A District Code will be replaced by the District Name). Such forms also have server-side default validation on the basis of data type, length as well as SQL Injection validations; in the case of Retrieval and Deletion, only the Primary Key values are validated (as these are the only inputs required for these two operations). For Insertion and Updation, all Column values are validated. For Filtered List Record, all column values are validated since filter criteria can set any column value. For any application with a large number of database tables, AppBuilder can definitely reduce development time to a great extent as all data management Forms can be generated in no time with the necessary business logic.

COMPONENTS/MODULES OF APPBUILDER
AppBuilder provides a rich library of classes; these are:
• DBManager: Wrapper Class to generalise database access independent of the actual database used
• FileManager: Utility Class to manage File Input/Output
• HTMLUtil: Class with useful methods to generate HTML controls with data
• MySQLDBManager & PGDB Manager: Actual database-manager classes for MYSQL & PostgreSQL databases; contains a large number of useful methods. It also contains other useful methods like querying for structure of tables with foreign key details, generating denormalised table structures etc.
• Validator: Class with necessary validation methods for different types of data
The methods available in these classes can be used in any application. This allows AppBuilder to be used also as a Framework.

APPLICATIONS DEVELOPED USING APPBUILDER TOOL
This tool has already been used to build up several projects in NIC Assam, notable amongst them being MIS for Small Tea Growers, GovPIS (a Personnel Information System for Govt of Assam), ERP for Assam Co-operatiove Jute Mill Ltd etc.

UNIQUE FEATURES OF THE INITIATIVE
None of the Code-generation software treat Foreign Keys the way the present tool does. Automatically generating relevant Drop-down Lists and maintaining them during the lifetime of a Form requires quite a lot of effort. Also the code generated by this tool is much easier to understand and modify.
