---
title: "WEBGL AND THREE.JS: 2D/ 3D graphic rendering Javascript API"
publication: "Informatics"
issue_date: "October 2018"
pages: [36, 37]
author: "MOHAN DAS VISWAM (Editor), G. PRASAD, Sr. Technical Director, RICHA TIWARI, Scientist -B"
section: "Technology Update"
---

## WEBGL AND THREE.JS: 2D/ 3D graphic rendering Javascript API

Computer Graphics have been part of the advent of the latest technology in ICT. Initially, web browsers were not planned for 3D graphics applications, but were designed for rendering simple web pages with static content.

With the use of dynamic content and scripting languages, the demand for 3D graphics support in browsers has grown immensely. 3D graphics is playing an important role in user’s multimedia desktop as well as web experience. There are different technologies used for rendering 3D objects in browser such as VRML, ShockWave, Flash, Silverlight, QuickTime and others. But, these technologies require browser plugin to be installed and there is no standardization for creation of these plugins. So, different plugins are required for rendering 3D Objects with different technologies, which results in installing multiple plugins in the browser. Sometimes, it leads to compatibility issues among plugins. WebGL (Web Graphics Library) 1.0 is one of the Javascript APIs for rendering interactive 3D and 2D graphics within any compatible web browser without the use of plug-ins. Sometimes, WebGL API may be tedious to use directly without any utility libraries. There are many Javascript libraries that abstract WebGL and result in higher code level. One of the utility libraries is Three.js, the most popular 3D library/ API that runs alongside feature-rich HTML5 to create and display animated 3D computer graphics in a web browser.

WEBGL (WEB GRAPHICS LIBRARY)
Web Graphics Library (WebGL) is one of the most important new technologies facilitating 3D visualisation on the browser platform. It is a cross-platform, royalty-free web standard for a low-level 3D graphics API. WebGL API is essentially a set of JavaScript functions which wrap around the OpenGL ES specification. It uses canvas element of HTML to render objects in browser. The HTML Canvas provides a destination for rendering 3D objects in web pages, and allows performing that rendering using different rendering APIs.

WebGL has compatibility and independence with underlying operating systems as it adopted web browsers as the content providing platform. Web browsers can provide overall programming interfaces, which are independent of underlying hardware, middleware, graphics library, and so on. A WebGL program can be executed on every platform, where a WebGL compatible web browser is available.

HOW WEBGL WORKS
WebGL programs are written in JavaScript language and embedded into HTML5 documents. The JavaScirpt codes call the WebGL API functions to finally get 3D output on the web browser. JavaScript sets up the initial data structures and sends them to the WebGL API, which sends them to OpenGL ES (OpenGL for Embedded Systems). The graphics driver supplies the implementation of OpenGL ES that actually runs the code. Finally, it is to be sent to the graphics hardware.

At the core of the WebGL technology are scripts known as shaders which are the small program written in GLSL that defines how the pixels of 3D object is drawn on the screen. There are two shaders in WebGL - vertex and fragment shader. The shaders are responsible for position calculation and colour specification respectively. The vertex shader converts the coordinates of the 3D model into 2D screen coordinates. It performs per-vertex computation. The fragment shader is responsible for generating colour output of each pixel. It performs per pixel commutation.

THREE.JS
The development of interactive 3D graphics program based on WebGL is sometimes complicated and time-consuming as it requires deep understanding of the library. To resolve this issue, there are a number of utility libraries such as Three.js, Babylon.js, A-Frame, SceneJS etc., which are built upon WebGL and provide framework for easy development of 2D and 3D graphic rendering applications. Among these libraries, ‘Three.js’ is probably the most widely used open source library (https://threejs.org. The source code is hosted in a repository on GitHub (https://github.com/mrdoob/three.js/). It is made available under the MIT license. The official documentation of Three.js is under construction, but it guides beginners very well to start with 3D graphical rendering application. Three.js is internally generating WebGL code while exposing a simpler API. Three.js also has pre-built components and helper methods that help to get things done faster.

APPLICATION AREAS
Today, 3D computer graphics have a vast domain of usage in different applications. They are used for 3D product design, gaming, city planning, disaster management, geo-spatial mapping, digital marketing, architect, medical imagery, education, fashion designing, art etc. Some of the examples where WebGL is being used are:

••Sony PlayStation 4 uses WebGL to render the user interface
••Google releasing demos under the chrome experiments collaborating with numerous world titles and developers
••Poly Google (https://poly.google.com) uses WebGL for 3D rendering
••Ironbane (http://play.ironbane.com/) is a massively multiplayer online game powered by WebGL and Three.js. One can collect items, interact with other players and explore the open world
••360 degree viewer (http://carvisualizer.plus360degrees.com/threejs/) for detailed car visualization with textures and environment mapping.

NIC has developed the 3D Web Viewer, ‘e-CollabCAD’ using Three.js technology. e-CollabCAD Web Viewer (https://collabcad.gov.in/eCollabCAD/) is a product for visualization and sharing of 3D design data of CollabCAD and open 3D data file formats (STL, OBJ, JSON). No software or plugin is required as the viewer works directly on WebGL compliant web browsers. User can upload, view and share 3D models and innovative designs with public. Number of visualization and rendering features have been provided in e-CollabCAD viewer. These include, 3D model viewer, shading (wireframe, facets), environment mapping, setting perspective and orthographic camera views, applying color gradients, setting different view.
