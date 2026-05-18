---
title: "Apache Cordova: Hybrid Mobile Apps"
publication: "Informatics"
issue_date: "January 2015"
pages: [27, 28]
author: "Niladri B. Mohanty, D. Madan Prabhu"
section: "Technology Update"
---

## Apache Cordova: Hybrid Mobile Apps

With the low cost smart phones creating buzz in the market, mobile application development is grossing highest craze than ever among the user groups. Many Government departments of India, including Election Commission of India, have tested the flavour of mobile applications. However, challenges in the mobile application development era are many. High developmental cost and platform specificity are the most vital issues. Different mobile manufactures use different platforms and different developmental languages, which is leading to sharp development time curve.
What is Apache Cordova?
Apache Cordova is a set of device APIs that allow a mobile app developer to access native device function such as the camera or battery status or geo-location from JavaScript. This basically works like a wrapper so that developer does’nt have to use platform specific native APIs and wrapper enable developers to write mobile applications using HTML, JavaScript and CSS only using Cordova.
Platform Supported by Cordova
Cordova support platform in three different modes as Sun Set, Core and Horizon. Cordova supports for Sun Set category of platforms are slowly being withdrawn whereas Core platforms are strongly supported. The Cordova development community is eyeing the horizon category of platforms.
Why now we are serious about the Cordova?
Visual studio and .net are mostly used in software development environment. But it was facing strong criticism from pro open source community. To address the criticism on its Proprietary Licensing System, Microsoft first took a major step by opening the source code of .net Framework for viewing with restriction to build. In the next concrete step it announced .net Framework as complete open source. Not only this, it also announced the release of Visual Studio Community Edition completely free for individuals and for companies having less than five employees. Companies with unlimited employees, contributing to .Net Open Source Foundation, can avail it free even for commercial purposes. The Cross Platform Support has been further extended to Linux and Mac Systems.
In this context, the important dimension of Cordova is that “Visual Studio now supports Cordova”. Hence, one can:
yyWrite Cross Platform mobile Applications using Visual Studio,
yyGet good intelligence while writing code for mobile devices,
yyGet multiple mobile simulator programs directly from the Visual Studio.
Cross-platform Mobile Apps development for iOS, Android, Windows devices and many more using Visual Studio Tools for Apache Cordova is now possible. With an extension for Visual Studio 2013 Update 4 or Visual Studio 2015 Preview, Visual Studio provides the tools one needs to get started building the application using HTML, CSS, and JavaScript based on Apache Cordova. In simple word, using Visual Studio one can write mobile application using only HTML, JavaScript and CSS which can be packaged to be installed in various mobile platforms with little or no change in code.
Native API and Cordova Relationship
Every hardware device is controlled by a piece of software popularly known as drivers. These drivers expose APIs to allow other applications to communicate with it. To assure the security level, it only allows the application running behind the OS level Sand Box. In mobile application development, for interaction with the APIs of device drivers, one should have in-depth knowledge of the native APIs of all platforms you need to provide. Cordova works like a wrapper to all those native APIs so that the developer only needs to communicate with the Cordova API. Cordova having the understanding for all the major mobile platforms communicates with the native APIs. These wrappers are bundled as plugins. Let us explore this through an example of camera capture module:
Call Cordova_Camera_ API_ takePicture() -----------------------Cordova API to take control on camera
{ If (Device_type== “Android”)
{ Call android.hardware.camera2API(); ---------- Android API to take control on camera}
If (Device_type== “IoS”)
{ Call IoSUIImagePickerController(); ------------------ IoS API to take control on camera}
If (Device_type== “Windows”)
{ Call Windows. Media.Capture API(); --------- Windows API to take control on camera}
Power of Cordova
Accessing the device’s resources through native code requires lot of initialization and permission setting, bunch of code etc. Whereas using Cordova it can be achieved through few lines of elegant coding to access the same. Due to the single codebase of application, it is easy to maintain the apps for any bug closing and new features enhancement.
Extended time and cost involved for acquisition of new skills may be avoided using Cordova as the same web development skills can be re-used for m-Governance.
