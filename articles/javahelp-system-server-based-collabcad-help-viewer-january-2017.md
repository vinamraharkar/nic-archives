---
title: "JavaHelp System: Server Based CollabCAD® Help Viewer"
publication: "Informatics"
issue_date: "January 2017"
pages: [40, 41, 42]
author: "Edited by MOHAN DAS VISWAM, GUNTUKU PRASAD, RICHA TIWARI"
section: "TECHNOLOGY UPDATE"
---

## JavaHelp System: Server Based CollabCAD® Help Viewer

The JavaHelp System allows users to access the help files and topics for the CollabCAD® software from their desktop or their browser application without necessarily having to install the CollabCAD® software. It allows for easy access to help for beginning users and a quick reference guide for the more experienced users.
CollabCAD® is a 3D CAD Software system for collaborative design & development of Industrial Designs. It provides a total solution from product design, drafting, numerical control, visualisation to workflow and enterprise resource planning. It is an initiative of National Informatics Centre (NIC, Department of Information Technology), Bhabha Atomic Research Centre (BARC, Department of Atomic Energy) and Vikram Sarabhai Space Centre (VSSC, Department of Space). CollabCAD® has its comprehensive HTML documentation with supporting images in software installation.
The Help System of CollabCAD® has been developed using JavaHelp 2.0 API which provides a fully featured, easy to use system for presenting information to users. It has a help viewer interface with a Table of Contents, Glossary, Index and Search options for easy access to the documentation. For CollabCAD®, a server based help viewer has also been implemented to provide online access to documentation through a web browser without installing the software.
JAVAHELP SYSTEM
The JavaHelp 2.0 binary distribution is available on the JavaHelp home page (https://javahelp.java.net/) to build a standard, full-featured help system for a simple Java application. JavaHelp software can be installed by extracting the downloaded zip file to any directory. In a Windows Only environment, variables such as JAVAHELP_HOME which contain the path to the installation folder of JavaHelp 2.0 need to be set. %JAVAHELP_HOME%\javahelp\lib\jhall.jar needs to be put in classpath. It is adviced to remove all prior releases of JavaHelp from your system before installing version 2.0.
HELPSET:
JavaHelp help system contains a set of files called the HelpSet. Together, these files provide the foundation of a working application help system. The JavaHelp HelpSet includes three types of files:
1. HelpSet data files: There are two HelpSet data files named the helpset file and the map file. The helpset file is the master control file for your help system. It must have the file extension .hs. The typical helpset file has four sections: the maps section, the views section, the presentation section, and the implementation section. When a user accesses the help system, the system starts by reading the .hs file. The map file is used to associate an ID to each help topic by mapping the ID string to the URL of the help topic file for navigational purpose. The map file has the file extension .jhm.
2. Navigation files: Four types of navigation files are TOC, Index, Glossary, and Favourites. The help system reads the information in these files to build the four types of navigation views and then displays them in the navigation pane.
3. Topic files: Topic files are in HTML format. It is advisable to specify the <title> tags in the HTML files, because the <title> tags will be used in the search database for the full text search.
Once topic files, navigation files, the map file and the helpset file have been coded, the helpset can be opened by running hsviewer.jar in %JAVAHELP_HOME% \demos\bin.
FEATURES
Many of the features of JavaHelp have been incorporated into the Desktop based CollabCAD® Help System. Some of the salient features are:
• Context-Sensitive help: Context-sensitive help is an especially user-friendly way to deliver information to the users. When a user clicks a particular icon or field, a pop-up window explains the function or the next step that goes with that field. CollabCAD® supports Window Level Help i.e. User can use Help Key (F1) to invoke help system for introductory topics or topic specific help. CollabCAD® also provides Field-level Help. When a specific component on the Java application's GUI, such as a text field or button, has the focus, the user presses the Help key (F1) or clicks a button to launch the help system with a specific topic describing the current component.
• Search Database: CollabCAD® uses Java Help API which will automatically index help topics directory and build the search database for the application. Search functionality is an essential part of the help system.
• Merging helpsets: Large, modularized applications may require the creation of numerous helpsets, perhaps even by different teams working on various aspects of the application. Merging helpset helps in viewing different helpsets as one. In CollabCAD®, there are diffent helpsets for Plot Configurator module and CAD Modeling Module of CollabCAD®. These are merged using this feature in order to display it in a single Help Viewer. There are four merge types in JavaHelp 2.0: SortMerge, UniteAppendMerge, AppendMerge and NoMerge.
SERVER-BASED HELP SYSTEM
Server−based applications have the same need for online help as client based applications, but they require that the helpset runs in a web browser, as the applications do, and that it be accessed from a server. CollabCAD® has provided web help (https://collabcad.gov.in/CollabCADHelp/) to the registered users, so that they can access it without installing the software. For the CollabCAD® Server based Help Setup, the code from JavaHelp 2.0's serverhelp demo is used. This code is in the %JAVAHELP _HOME%/demos/ serverhelp/web directory.
SERVER−BASED JAVAHELP ARCHITECTURE
The diagram below illustrates the architecture. A browser initiates a JSP request. Examples of a JSP request are displaying the help content in the helpset, the navigators, or the data for a given navigator. Typically, the JSP request contains JavaBeans™ components as well as JSP tag extensions. The Java server turns the request into a Java Servlet. The servlet accesses the appropriate information from the helpset by using the classes in the JavaHelp library (jh.jar) and the JavaHelp tag library (jhtags.jar) and returns HTML and possibly JavaScript or dynamic HTML (DHTML) to the browser.
JAVAHELP SERVER COMPONENTS
Access to the helpset data on a server is accomplished through a combination of JavaBeans components specific to the JavaHelp system and JSP tag extensions.
• JSP files:
JSP enables web developers to develop dynamic web pages. JSP uses XML like tags to encapsulate the logic that generates web content. There are several important JSP files. navigator.jsp is used to get the views from the helpset file. javax.help.TOCView.jsp, javax.help.SearchView.jsp, and javax.help.Index View.jsp each build their corresponding views. The help.jsp file controls the overall presentation of the help window. All these files are used in CollabCAD® that helps to control the presentation and flow of the CollabCAD® Help System.
• JavaHelp server bean:
ServletHelpBroker is the JavaBeans component that stores help state information, such as the helpset in use, the current ID, the current navigation view, and other pieces of help information. The ServletHelpBroker is used in the JSP request with a session scope.
• JavaHelp JSP Tag Extensions:
There is a standard set of tag extensions in the JavaHelp tag library that can be used to invoke application functionality. Like validate tag is to validate Help broker and helpset and then to load the helpset that has been defined either in the validate tag with the helpSetName attribute.
• Navigator Scripting Variables:
The navigator, tocItem, indexItem, and searchItem tag extensions introduce a predefined set of scripting variables into a page. These variables enable the calling JSP to control the presentation without having to perform processing to determine the content. Unless otherwise specified, each scripting variable creates a new variable, and the scope is set to NESTED. NESTED variables are available to the calling JSP only within the body of the defining tag.
• JavaScript files:
There are several important JavaScript files. tree.js is used to build a tree. The navigation trees for the TOC and Index views can be created using this file. The file searchList.js can be used to build a tree for the Search view. util.js checks whether any change in the content has occurred. If a change has occurred, an update will be fired with the change.
CONCLUSION
This article gives a brief overview of JavaHelp 2.0 technology, the Java platform's help system API. JavaHelp, is a full-featured, standard help system that can be easily implemented into any Java application. JavaHelp 2.0 also provides an option to develop a web based help system for users on a network application.
References
1. https://javahelp.java.net/
2. https://docs.oracle.com/cd/E19253-01/819-0913/819-0913.pdf
3. http://www.ibm.com/developerworks /library/j-javahelp2/
4. https://java.net/projects/javahelp/sources/svn/show/branches/index-keywords-27/JavaHelp/demos/serverhelp?rev=89
For further information, please contact:
GUNTUKU PRASAD
Sr. Technical Director & HoD
CollabCAD Division, NIC, A-Block
CGO Complex, Lodhi Road, New Delhi- 110 003
Email: gprasad@nic.in
Phone: 011-24305177
