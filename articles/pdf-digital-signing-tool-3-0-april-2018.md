---
title: "PDF Digital Signing Tool 3.0"
publication: "Informatics"
issue_date: "April 2018"
pages: [32, 33, 34]
author: "KAPIL KUMAR SHARMA, NAVNEET KAUR"
section: "eGov Products & Services"
---

## PDF Digital Signing Tool 3.0

PDF Digital Signing Tool 3.0
A Feature-rich Workplace Solution with Intuitive signer interface

PDF Digital Signing Tool 3.0 has been built on latest technology using JavaFX with enhanced features, improved and intuitive signer interface. This new version facilitates digitally signing of the electronic documents (pdf) by reading Digital Certificates (X.509) from USB token provided by the Certifying Authority.

With the emergence of Digital India and success of various initiatives under the programme, the electronic signatures have gained acceptability as a trustworthy signing mechanism for maintaining identity, authenticity and security of the electronic documents and transactions.

Digital Signature is the subset of the electronic signatures that uses Public Key Infrastructure (PKI) to digitally sign an electronic document and provide assurances of the evidence to provenance of identity of signer and integrity of the document. This means that the content of the document cannot be altered after signing and the receiver of a document is assured of the signer authenticity.

The Information Technology Act, 2000 and subsequent amendments provides the required legal sanctity to the digital signatures based on asymmetric cryptosystems.

DIGITAL SIGNATURES VS PHYSICAL SIGNATURES

A physical signature (also called ink or wet signature) can be applied on a paper document only and can be replicated from one document to another by copying the image manually or digitally. But to have credible signature copies that can resist some scrutiny is a significant manual or technical skill and to produce ink signature copies that resist professional scrutiny is very difficult. Also in a physical paper document, there is always a concern about its durability.

Digital Signatures use Digital Signing Certificate to establish an electronic identity to an electronic document. The Digital Signature cannot be copied to another document. Paper contracts sometimes have the ink signature block on the last page, and the previous pages may be replaced after a signature is applied. Digital signatures can be applied to the entire document, such that the Digital Signature on the last page will indicate tampering if any data on any of the pages have been altered (However, this can also be achieved by signing with ink on all pages of the contract). Additionally, Digital

DST 3.0 Architecture

Unsigned PDF Document % PDF
.
.
(PDF Content)
....>%EOF

Signing Process (PAdES)

Signed PDF Document % PDF
.
.
(PDF Content)
Signature Dictionary /ByeRange (........) / Contents <.........
• Certificate....................
• Certificate Chain..........
• Signed Massage Digest
• Revocation Information
• Timestamp
....>%EOF

Digital ID of Signer Private Key Certificate • Serial No. • Public Key • Identify Info

Logs (Stored in client’s machine

PDF Signature

xxxxxxxxxxxx Logs...... xxxxxxxxxxxx

Digital ID of Signer Private Key Certificate • Serial No. • Public Key • Identify Info
Certificate 1 Certificate 2 .. Certificate n

Figure - 1

Signatures also provide encryption if required and thus provide privacy as well.

BASIC ARCHITECTURE OF DST 3.0

The basic architecture of DST 3.0 is given in Figure-1.

The tool facilitates Digital signing of PDF documents using PAdES (PDF Advanced Electronic Signatures) standard. The signature data is incorporated directly within the signed PDF document, allowing the complete self-contained PDF file to be copied, stored, and distributed as a simple electronic file.

ABOUT DIGITAL SIGNING TOOL 3.0

PDF Digital Signing Tool Version 1.0 was released in the year 2014 and made available through e-Gov App store. Version 3.0 of this open source desktop tool is now being released with enhanced features, improved and intuitive signer interface and built on latest technology using JavaFX. It provides digitally signing of the electronic documents (pdf) by reading Digital Certificates (X.509) from USB token provided by the CA. The digital signing functionality is provided for single or multiple signatures on a single pdf document as well as bulk signing of pdf documents.

FEATURES AVAILABLE
• Simple signing of single PDF files
• Multiple signs on a single PDF
• Bulk singing of multiple documents with single sign
• Enabling/ Disabling signature visibility in the PDF based on signer’s choice
• Enabling the signature image to be carried out on all pages of document
• Co-ordinates selection to sign on desired location in single signing
• Co-ordinates selection to sign on desired location in bulk signing. (In this case the bulk documents should be of same structure so that sign is placed properly uniformly at the chosen location
• Password window is provided for

PDF Signing Workflow

DST 3.0

Single PDF Signing

Bulk PDF Signing

Signing Certificate Selection

Certificate Revocation and Selection

Client’s Machine

Capture Co-ordinates

No

Valid

Invalid

Yes

Password protected PDF

Terminate

Placement of Sign accordingly

Protected

Not Protected

Bulk Signing

Single Signing

Single/Bulk Signing

Skip protected file

Prompts for password

Logs (Stored in client’s machine in case of bulk signing)

Single Process

Signed PDF

Figure - 2

signing password protected PDF files of persons that can sign the same document. The default is ten persons. This configuration is also available for bulk signing

• Certificate Revocation List check before signing
• Configuration to set maximum number of files signed in one go. Default value is 5,000 pdf files
• Configuration to set Maximum number
• View Signature details on any signed PDF file(s)
• Quick Help

Multiple Signing on single PDF

% PDF Original Document

Digital Signature 1

%% EOF

Signature 1 applies to these bytes

% Additional Content 1
................

Digital Signature 2

%% EOF

Signature 2 applies to these bytes

% Additional Content 2
................

Digital Signature 3

%% EOF

Signature 3 applies to these bytes

Figure - 3

HOW THE TOOL WORKS

Figure-2, depicts the working of the Digital Signing Tool. Digital Signing Tool version 3.0 checks CRL before signing the document. In this, CRL Distribution Point (CDP) will be picked while signing. If CRL file already exists at the user home directory location, it will simply check revocation status and proceed but if file is not updated, it will use the internet and download the latest file and proceed to put signature on PDF. If due to any reason, CRL checking is not performed, it will not allow the signer to sign the document.

SIGNING THE PDF FILES

The signer is prompted to provide the PDF file(s) for signing and the folder location where the signed document to be stored with some optional parameters as follows:

SIGNATURE VISIBILITY
This is related to appearance of signature on the document. Documents with invisible Digital Signatures carry a visual indication of a blue ribbon on the task bar. One can use visible Digital Signatures if one does want to display the signature, but only needs to indicate the authenticity of the document, its integrity etc.

COPY SIGNATURE
Placing image of Digital Signature on all pages of signed PDF file. By default signatures will appear only on first page of pdf file.

CAPTURE CO-ORDINATES
Signer can select the location where he wants to place the signature image.

MULTIPLE SIGNATURES ON SINGLE PDF
More than one signer can put their Digital Signatures on a previously digitally signed paper. Figure-3 shows the signatures of single and multiples signers in a single document.

BULK SIGNING
Signer can sign more than one pdf with a single click using bulk signing option. Further, user can select coordinates on single pdf and signatures will appear at same location in all PDF’s. Signature visibility and signature appearance on all pages can be controlled through options provided in the form (Figure-2).

Digital Signing Tool version 3.0 checks Certification Revocation List(CRL) before signing the document. In this, CDP point will be picked while signing, if CRL file already exists at the user home directory location, it will simply checks revocation status and proceed but if file is not updated, it will use the internet and download the latest file and proceed to have signature on PDF. Due to any reason if CRL checking is not performed, it will not allow the signer to sign the document.

CONFIGURATION

A simple interface to set limit on maximum number of PDF files that can be signed in Bulk signing (Figure-3).

Maximum number of signatures that can be carried on one PDF is also configurable.

Signature Valid
Digitally signed by Class 2 individual test
Date: 2018.03.05 15:50:42 IST

Figure - 4

VIEW SIGNATURE DETAILS
Another simple interface where signer can view signers’ details of signed PDF.

HOW TO OBTAIN THE TOOL
Digital Signing Tool 3.0 will be made available in e-Gov App Store by the mid of May, 2018. After downloading the tool, it can be easily installed like any other Desktop Application depending on the platform. It has a simple interface with four tabs as in Figure-5.

REQUIREMENTS
The tool uses Java FX & JCA and requires Java 8 in the client machines. It will be supported on Windows, Linux and MAC clients that have Java 8.

Figure - 5
