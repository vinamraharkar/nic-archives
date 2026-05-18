---
title: "Judgment Information System for High Court of Karnataka using open source digital repository software DSPACE"
publication: "Informatics"
issue_date: "October 2009"
pages: [10, 11]
author: "Veena P Oak, Vaijayanti Vaidya, Suresh Meti"
section: "e-Gov Products & Services"
---

## Judgment Information System for High Court of Karnataka using open source digital repository software DSPACE

Judgments passed in the High Court of Karnataka are a rich source of information for many stakeholders. There was a strong need for making this treasure accessible freely and effortlessly. And the answer was DSPACE, an open source software customized for repository of Karnataka High Court Judgments. This is the first initiative in India to use open source tools for handling electronic judgments.
Digital Collection of High Court Judgments is a web-based solution, http://karnatakajudiciary.kar.nic.in for storing and retrieving judgments in digital form. After a judgment is released, the stakeholders like petitioners, respondents, general public, advocates, other judges, courts etc would like to have early access to the judgment. Therefore the judgment in the electronic form needs to be made available as soon as it is released. Secondly a powerful search to help the stake holders to get the required information is the need for starting this initiative.
In case of High Court of Karnataka, court cases details like case number, case year, type, judge name, petitioner, date of judgment etc is already available in the court information system which is being as metadata for the respective judgments. However section and subject were not been updated for old judgments, hence provision was made to update the same. Technology used is, Open source digital repository software Dspace, Tomcat Java container, Oracle 10g database server, Windows 2003 server. Further District courts also can be added as sub communities and judgments can be added to the respective collections. It is workflow-based judgments publishing system. Here submitter, approver, collection administrator or DSPACE administrator are part of the workflow.
Salient Features
— Metadata is fetched from the Court information system and hence, there is lot of timesaving as far as the Meta data entry is concerned.
— DSPACE supports almost all types of file formats hence; it is easy to recognize file formats.
— As the solution is web based, multiple numbers of submitters and approvers are possible.
— Search based on case number, case type, subject, judgment date, judge name, petitioner name, respondent name are available.
— Advanced search can be used to search by any term to get desired results.
Submitter
Submitter has been assigned the work of submitting the documents to the task pool. He is the starting node in the workflow. There can be more than one submitter in the workflow. He logs in to the system using his user id and password. There are 65 types of collections under “High Court of Karnataka community”. The submitter needs to select the case type from the collection list, based on the case number and year; the system will fetch desired data from the court case information system. There is a provision to enter section and subject for the judgment. Judgment is scanned and stored in PDF format with watermark on every page. Water mark is basically to indicate that the electronic judgment is only for the reference purpose and not for any official use. This file is uploaded using the upload option in the system.
Once the file is uploaded by the submitter, it is listed in the task pool to be viewed by the Approvers.
Approver
After submitter, approver is the next person in the workflow who has been assigned the job of verifying the metadata and the judgment files attached.
All the documents submitted by submitters are verified by at least one approver. There can be number of approvers who are assigned to verify the submissions. In the workflow of digital judgments, approvers are the domain experts who verifies the documents submitted against the metadata and they either approve the document or reject the same with appropriate reason. After approver approves the document, it gets published in the collection and is available in the repository for search and download for anybody who has access to the repository. In case of any discrepancies, he can edit the same and approve, or reject the same with a message.
After approval of the approver, a handle is created for each of the approval and this is the unique id for the document submitted. Hence a note of the above mentioned handle is very important. This helps for further editing/correction etc.
Once a document is published in the repository, collection administrator or DSPACE administrator only can edit it.
Collection Administrator
He is the administrator for all the 65 collections coming under High Court Karnataka.
In case of editing of Meta data or withdrawing the documents, which are already published in the repository, he can do the needful using withdraw option. The item withdrawn is not deleted but removed from public view.
Accessing the repository
Browse: One can reach the required judgment by browsing through the repository based on Case Type, Case Number, Judge Name, Subject and Date of Judgment which appears in ordered list.
Search: Other way of reaching to the judgment is through advanced search option where one can search based on judge name, case number, petitioner name, respondent name, section, subject, concerned case number or previous disposal dates.
To avoid erratic outcome while browsing / searching, Search and Browse indices have to be indexed regularly.
Tuning: As the size of the repository increases certain tuning requirements arise. The Heap size of Tomcat Server has to be set to certain adequate value. The Oracle database server parameters like System Global Area, Number of open cursors have to be set for appropriate values. The Tuning requirement may also depend on the no. of concurrent users involved in the workflow.
