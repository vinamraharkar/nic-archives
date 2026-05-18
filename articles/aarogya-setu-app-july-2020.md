---
title: "Aarogya Setu App"
publication: "Informatics"
issue_date: "July 2020"
pages: [8, 9, 10]
author: "R.S. Mani, Dr. Seema Khanna, Amit Kumar, Hariharan M, Syed Mahmood Hasan"
section: "In Focus"
---

## Aarogya Setu App

Aarogya Setu is a mobile application launched by the Government of India on 2nd April 2020, to aid the COVID-19 containment efforts of the Government. The App works based on contact tracing method and helps in identifying, monitoring and mitigating the spread of COVID-19 across the country.

The Aarogya Setu App augments the COVID-19 containment initiatives of the Government in proactively reaching out to and informing the users of the app regarding risks, best practices and relevant advisories pertaining to the containment of COVID-19.

The App is currently being used by over 140 million users and has successfully predicted a large number of potential COVID-19 hotspots also, well before the actual COVID-19 outbreak started in many regions across India. Most of the predictions have come true and the advance prediction has helped the Government to plan and deliver necessary medical interventions to control the spread in a proactive manner. Aarogya Setu plays a crucial role in the overall COVID-19 containment efforts of India.

Key Features
• Automatic contact tracing using Bluetooth
• Self-Assessment test based on ICMR guidelines
• Updates, advisory and best practices related to COVID-19
• Integration with e-Pass
• Geo-location based COVID-19 statistics
• Nation-wide COVID-19 statistics
• Emergency COVID-19 Helpline contacts
• List of ICMR approved Labs with COVID-19 testing facilities
• Risk Status of User
• QR Code
• Support for over 12 Languages

Supported Platforms
AarogyaSetu is currently supported on the following mobile operating systems:
• Android version 5.0 and above
• iOS version 10.3 and above
• KaiOS (available on jio phones)

Aarogyasetu for Landlines and Feature Phones:
For feature phones and landlines, Aarogya-Setu Interactive Voice Response System (IVRS) has been launched as a service, with the number 1921. This service can be availed by anyone in India, including the users of feature-phone (who are not able to use the App). The users can give a missed call to 1921 and they will receive a callback from Aarogya Setu IVRS. The IVRS platform would prompt the citizens with the same questions and in the same format as the Aarogya Setu app, thereby enabling them to complete their self-assessment. This IVRS service is available in 12 languages. After the self-assessment, users get a summary of their health condition on SMS. Those who report that they are unwell through their self-assessment also get calls from the Government for medical assistance.

Technical Architecture
Aarogya Setu’s front-end and back-end architecture is very robust and highly scalable. The architecture can seamlessly handle hundreds of millions of requests. The user requests to the backend are validated using an ‘Authorization Token’. The backend is protected by a security gateway, which blocks DDoS attacks, hacking attempts etc. The app leverages NIC’s SMS gateway, through which millions of SMSs have been sent to the users. The static content of the app is hosted on a content delivery network, so as to facilitate faster response times for the end users. The back-end is also integrated with ICMR and e-pass systems.

Aarogya Setu has recently introduced QR Code feature, which can be scanned to know the health status of an individual. This feature ensures that the real time status of the health of a citizen is shown to the QR scanning app. This QR Code once generated is valid for 45 minutes and it can be used at the entry/exit points of offices, malls, metros and other public places, to ascertain the health status of the individuals entering/exiting the premises.

How the App works
The Aarogya Setu app on a user’s phone detects other devices that have the Aarogya Setu app when they come within the Bluetooth proximity of your phone. When this happens, both the phones securely exchange a digital signature of this interaction, including time, proximity, location and duration. This data is stored on the device of the respective Users in an an encrypted form. In the unfortunate event that any of the people that a user came in contact with during the last 14 days, tests positive for COVID-19, the platform calculates the user’s risk of infection based on number of interactions and proximity of the user’s interaction and recommends suitable action. This action is displayed on the app’s home screen. The updated risk of infection is analyzed by Government, to facilitate suitable medical interventions, as and when required. So far the app has identified more than 12 lakh individuals through contact tracing and these individuals were provided with appropriate advise based on their proximity, duration of interaction and display of any COVID-19 related symptoms. The figures for such Bluetooth Contact Tracing (BCT) done so far, is given Figure-1 (previous page).

What does the Colours in AarogyaSetu signify

Colour and Risk of Infection | What does it mean | What to do
---|---|---
You are COVID-19 Positive | You are COVID-19 Positive | Contact 1075 immediately for further advice, from medical experts
High Risk of Infection Recent contact with infected person | You have indicated COVID-19 symptoms during self-assessment and/or You recently met any COVID-19 positive person or came in close contact and came in close proximity and for a significant period of time | Self-Quarantine and isolation is must. If symptoms persist, then Testing is recommended. Use masks, practice handwashing and social distancing
Moderate Risk of Infection Recent contact with infected person | You met someone who tested COVID-19 positive but your interaction was limited and socially distant and/or You have indicated one or more COVID-19 symptoms during Self-Assessment | Self-Quarantine and isolation is must. Keep monitoring symptoms. Use masks, practice handwashing and social distancing
Low Risk of Infection Recent contact with infected person | You have declared a mild COVID-19 symptom during self-assessment or You have come in contact with a COVID-19 positive person, but at a relatively long distance or for a short duration | Keep monitoring symptoms. Self-Quarantine is advisable. Use masks, practice handwashing and social distancing
You are Safe | You haven’t met any COVID-19 positive person, or You haven’t declared any COVID-19 symptoms during Self-Assessment, or You haven’t taken the self-assessment yet | Keep monitoring for symptoms. Use masks, practice handwashing and social distancing

Security and Privacy
The Aarogya Setu App has been designed and developed, with utmost focus on security and privacy. The App has various in-built security measures which protects the user’s data and also prevents any kind of security compromise through which any personal data could be exposed. The data is encrypted while stored on the user’s phone and while in transit, when it is being sent to the backend server.

The privacy policy and terms of services, present in the App clearly define the following:
• Working mechanism of the app
• What data is collected
• How the data is collected
• The purpose for which the data will be used
• How long the data will be retained
• Security & privacy measures undertaken to safeguard the user’s data

The Terms of Service are accessible from https://static1.swaraksha.gov.in/tnc/ and the Privacy Policy is accessible from https://static1.swaraksha.gov.in/privacy/

Each version of the app is released to the public only after proper security audit clearance. The source code of the App has been released in the public domain on 26th May 2020 and a bug bounty programme has also been announced to encourage the public to identify and report any security vulnerabilities/bugs/ code improvements in the App.
