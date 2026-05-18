---
title: "RESPONSIVE WEB DESIGN: Device Friendly Web Viewing"
publication: "Informatics"
issue_date: "October 2013"
pages: [33, 34]
author: "Alka Mishra, D.P. Misra"
section: "Technology Update"
---

## RESPONSIVE WEB DESIGN: Device Friendly Web Viewing

India is a fast growing market for internet users. Technological innovations and availability of new handy devices help people to access internet more on their smart phones, tablets, net-books and other such mobile devices than the desktop PCs. Nowadays, every website owner wants a mobile version of their website to cater to the growing number of non PC users. In many cases there are separate designs for the BlackBerry, Android Phone, iPhone, iPad, Windows Phone, net-book, Kindle, etc. This changing demand of website viewing allows many web owners to adopt the new trend called Responsive Web Design.

WHAT IS RESPONSIVE WEB DESIGN?
Responsive Web Design is a web design approach aimed at crafting sites to provide an optimal viewing experience. This also suggests that design and development should respond to the user’s behavior and environment based on screen size, platform and orientation. As the user switches from their desktop to tablet, the website should automatically switch to accommodate for resolution, image size and scripting abilities. In other words, the website should have the technology to automatically respond to the user’s devices.

MAIN FEATURES
Responsive Design basically allows a website to respond or adapt to a different viewport sizes without setting a specific domain/sub-domain for people using mobile devices or switch to a different set of code bases. The look and feel of the website can be maintained so as to have similar experiences across different device sizes. This is possible with the use of viewport Meta-tag and CSS3 media queries. The Responsive Web Design must have the following features:
  l The site must be built with a flexible grid foundation.
  l Images that are incorporated into the design must be flexible themselves.
  l Different views must be enabled in different contexts via media queries.
  l Viewport Meta-tag is placed inside the <head> tag and is used to control the scale of the web page.
  l The second component is the CSS3 media queries, which specify the styles for specific viewport sizes.

IMPLEMENTATION IN DATA PORTAL INDIA
We have used the following basic techniques to implement the responsive web design in the upcoming version of the Data Portal India (www.data.gov.in)
  l Flexible/Adaptive layout – There is an intelligent use of CSS media queries to modify the layout in ways that suit different screen sizes. Responsive Grid has been used to quickly build responsive layout. The flexible grid helps to make a design flexible and fluid.
  l Fluid grids and layouts – It uses relative units like percentages instead of fixed width units like pixels. The best solution for flexible web design will be achieved by defining parameters for columns, spacing and containers. Size and spacing are the two main components to focus on creating your flexible grid system. In place of pixels, use ems and percentages as your units of measurement.
  l Flexible media/images - Images and other media (like videos) are scaled using relative units so that they don’t expand beyond their containing element.
    n To maintain fast loading time, use images of a manageable size.
    n An alternative to scaling is cropping. The CSS overflow property (e.g. overflow: hidden) gives us the ability to crop images dynamically.
    n The option is available to have multiple versions of the same image and then serve up the appropriate sized version depending on the user.

MEDIA QUERIES
Media queries allow the page to use different CSS rules based on characteristics of the device the site is being displayed on, most commonly the width of the browser. Conditions such as min-width, max-width, device-width and orientation, control how content is displayed differently. For example, max-width sets a maximum browser width that a certain set of styles would apply to.

FRAMEWORKS FOR RESPONSIVE WEB DESIGNS
There are various open source responsive HTML5 frameworks, boilerplates and tools for front-end web development using HTML, CSS, and JavaScript. Here are glimpses of top ten frame works that one can try:
  l Twitter Bootstrap (Licence: Apache Licence v2.0): Bootstrap was made to not only look and behave great in the latest desktop browsers (as well as IE7!), but in tablet and smart-phone browsers via responsive CSS as well. It has been packed with features like a 12-column responsive grid, dozens of components, typography, JavaScript plug-ins, form controls, and even a web-based Customizer to make Bootstrap customized.
  l Foundation (Licence: MIT Licence): Foundation is developed in SaaS, which is powerful CSS pre-processor that helps you to write cleaner, more organized CSS. You can maintain it easily over time without the typical headaches faced in vanilla CSS.
  l Skeleton (Licence: MIT Licence): Skeleton is a small collection of CSS files that can help you rapidly develop sites that look beautiful at any size, be it a 17" laptop screen or an iPhone. Skeleton is built on three core principles: responsive grid down to mobile, fast to start, agnostic style.
  l HTML5 Boilerplate (Licence: Multiple open source licenses): HTML5 Boilerplate assists the users to build fast, robust and malleable web apps or sites. HTML5 Boilerplate has distinct build script projects to help augment the performance of the site/app in a production environment.
  l HTML KickStart (Licence: MIT Licence): HTML KickStart is an ultra–lean set of HTML5, CSS, and jQuery (javascript) files, layouts, and elements designed to develop a responsive design.
  l Montage - HTML5 Framework (Licence: BSD License): MontageJS supports simple and two-way data binding between objects, components, and collections. Data binding helps keep your UI and model data in sync to avert manually tying your data into the DOM.
  l SproutCore (Licence: MIT Licence): SproutCore is an open-source JavaScript framework. Its goal is to allow developers to create web applications with advanced capacity and a user experience equivalent to that of desktop applications. When developing a SproutCore application, all the code is written in JavaScript. A notable divergence of SproutCore is Ember.js. Both projects are maintained separately and have taken different directions.
  l Zebra (Licence: LGPL): Zebra brings fresh views and possibilities to develop web based Rich UI applications. The approach sits on top of HTML5 Canvas element that makes it possible to render any imaginable UI. Zebra development is much closer to software engineering, where you write well structured, manageable, extendable code basing on easy Zebra OOP concept.
  l CreateJS (Licence: Liberal MIT Licence): CreateJS is a suite of modular libraries and tools which work together to enable rich interactive content on open web technologies via HTML5. These libraries are designed to work separately, or mixed and matched to suit your needs. The CreateJS Suite is comprised of: EaselJS, TweenJS, SoundJS, PreloadJS, and Zoë.
  l Less Framework (Licence: MIT Licence): Less Framework is a CSS grid system for designing adaptive websites. It contains 4 layouts and 3 sets of typography presets, all based on a single grid.
