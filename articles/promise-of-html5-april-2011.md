---
title: "Promise of HTML5"
publication: "Informatics"
issue_date: "April 2011"
pages: [28, 29]
author: "Shashi Kant Pandey"
section: "Technology Update"
---

## Promise of HTML5

The Hypertext Markup Language (HTML) is meant for describing the structure of the Web Pages. HTML5 is the newest major revision of HTML. It has been built around the principles of Compatibility, Utility, Interoperability and Universal Access. Its goal is to improve semantics, efficiency, and usability of web development as well as the deployment and usability of the World Wide Web.
TILL now the structuring of a web page for layout and content was achieved using a generic element like a div with an id of "header" or "navigation". The idea with HTML5 is to identify common patterns and use them to impart real meaning on standard web page elements. So, instead of using a generic element like a div with an id of "header," a new element called header was created. This will allow for much smarter interactions between web browsers/search engine spiders and web content.
Take the example of input validations. The developer has to keep in mind the input fields that were required for form processing and then write complex code for validating the inputs. Now with HTML5 just add another attribute "required" to the form control where input is mandatory and you are done. No separate coding hassle for simple things. Developers were required to write their own complex code or use third party components for displaying Web controls like calendar, date or time. With HTML5, it is just another input type date that displays a calendar on the web page with all ease.
Here we are going to cover some features of HTML5 that shows the significant improvement over its previous version HTML4:
BETTER STRUCTURE
HTML5 introduces a whole set of new elements that make it much easier to structure pages. Most HTML4 pages include a variety of common structures, such as headers, footers and columns and today, it is fairly common to mark them up using div elements, giving each div a descriptive id or class. Take a look at new elements which minimises the use of divs and make the page more structured.
In HTML5, there is only one doc type. It is declared in the beginning of the page by <!doctype html>.
The nav tag is used to contain navigational elements, such as the main navigation on a site or more specialized navigation like next/previous-links.
The section tag is used to denote a section in the document.
Multiple sections can be nested inside each other.
The article tag represents an independent piece of content of a document, such as a blog entry or newspaper article.
aside tag is used to wrap around content related to the main content of the page that could still stand on it's own and make sense.
The footer tag may contain additional information about the main content, such as information about the writer, copyright information and so on.
THE CANVAS
A canvas is a rectangular area on your page where JavaScript can be used to draw anything you want. This feature allows rendering of graphs, game graphics, or other visual images on the fly. HTML5 defines a set of functions (canvas API) for drawing shapes, defining paths, creating gradients, and applying transformations.
SUPPORT FOR VIDEO AND AUDIO
The video tag is one of those HTML5 features that get a lot of attention. No more plugins for video/audio is required. Its just a few line of html code and you are done:
<video src="mymovie.webm" controls="controls"/> your browser does not support the video tag </video>
SMARTER FORMS AND ENHANCED CONTROL OVER INPUTS
HTML5 defines over a dozen new input types that can be used with forms. It reduces lot of programming effort and provides standard way of handling inputs. Some important input types are:
Email address, URL, Number, Range, Date & time, Color picker
Gone are the days when you used third party controls and struggled a lot for their browser compatibility and implementation with your web apps. Think of a calendar control which you can now use with a single line of code. <input name="startdate" type="date"> and the calendar is displayed. Further the date and time related inputs can be handled in several ways like "date", "month", "week", "time", "datetime" or "datetime-local".
Similarly, for any input field that is a required field, simply add an attribute "required" and it works fine. No need to write complex javascript codes. <input name="empname" required> With "placeholder" attribute you may assign significant information for users while they fill up the form. With "autofocus" attribute you can easily set focus to any form element when the form loads.
WEB WORKERS
Web Workers provide a standard way for browsers to run JavaScript in the background. With web workers, you can spawn multiple "threads" that all run at the same time, more or less (Similar to the way computer can run multiple applications at the same time). These "background threads" can do complex mathematical calculations, make network requests, or access local storage while the main web page responds to the user scrolling, clicking, or typing.
OFFLINE WEB APPLICATIONS
Using HTML5 you can build offline web applications. During your first visit to an offline enabled website, a list of all the dependent files (HTML, JavaScript, images etc.) is downloaded and stored on the visitor's computer. After that you use the website in offline mode. The changes made during your offline operation, is uploaded to the website when you visit it in online mode.
GEOLOCATION
The geolocation APIs make location, whether generated via GPS, cell-tower triangulation or wi-fi databases available to any HTML5-compatible browser-based application.
The power of HTML5 is already being unleashed in the smartphone/tablet space. Owing to the lack of mobile flash support and the presence of robust Webkit-based browsers in Android, Apple and Palm's smartphones, HTML5 applications and media are strong in the mobile space.
The developer community world over is excited by the features and promises of HTML5. New experiments, comments and testing are going on new specifications. Recent versions of Firefox, Google Chrome, Opera and Apple Safari support majority of the specification. With lot more companies developing authoring tools and browsers promising to come up with new versions supporting HTML5 specification we expect that in the next two or three years HTML5 will reach a critical mass and begin to dominate the web.
CONCLUSION
HTML5 shows all promises of becoming a platform for the web that is state-of-the-art as well as broadly available. Together with browser improvements, especially regarding script engines, HTML will become an adequate development platform for state-of-the-art web applications and the emerging mobile area. Any organization with a stake in the web needs to be prepared for the paradigm shift that is going to happen soon.
