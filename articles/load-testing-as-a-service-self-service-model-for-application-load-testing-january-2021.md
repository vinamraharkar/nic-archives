---
title: "Load Testing as a Service - Self Service model for application load testing"
publication: "Informatics"
issue_date: "January 2021"
pages: [37, 38, 39]
author: "MOHAN DAS VISWAM"
section: "Technology Update"
---

## Load Testing as a Service - Self Service model for application load testing

Load testing is a non-functional form of application testing in which we measure performance metrics and throughput against the expected requirements, industry guidelines and standards and examine the resources provisioned for the application. It simulates the behaviour of the application under both normal and at peak conditions by creating artificial traffic of concurrent virtual users on the application thereby identifying any bottlenecks in the system which might degrade the performance in production.

Modern-day G2C services expect very high concurrency in production. To ensure that the quality of service matches the expectations of the end-user, it is vital to perform a thorough load testing of the application before its release. Load testing of such an application requires considerable investment in setting up a cluster of load generator servers, which may not be possible for all the projects. Load testing service makes it possible to test any application with desired user load without incurring any cost on license procurement or management overhead of provisioning a set of load generator servers.

Load testing of an application is very important step executed before the deployment of the application in production environment.

Key advantages of performing load testing
• Estimation of infrastructure
• Performance measurement
• Minimize system downtime risks
• Identify inefficient code

A load testing project begins with the identification of test scenarios, quality parameters for acceptance, test environment setup followed by test script creation and execution with desired user load.

Technology Brief

Apache JMeter
The Apache JMeter™ application is an open-source Java application designed to load test functional behaviour and measure performance. It was originally designed for testing Web Applications but has since evolved to test many different applications/ server/ protocol types such as Web - HTTP, HTTPS (Java, NodeJS, PHP, ASP.NET), SOAP/ REST Webservices, FTP, Database via JDBC. It can be used to simulate load on a server, group of servers, network or object to test its strength or to analyze overall performance under different load types.

Components of JMeter

Test Controller or Test Workbench
Test Controller is a local machine where the test script is created by recording the browser actions using the Apache JMeter’s recording functionality. Test Controller is also used to configure the load distribution on local or remote machines. For the greater user load, the test is configured to execute on remote machines running the agent service of JMeter.

Test Agents
The load test agent machine is a remote machine with a high-end configuration that runs ‘server’ component of JMeter. The virtual user load is distributed to multiple agent machines through the controller and thus the test is virtually fired from remote locations. Once the test is completed, the agent machines send their results to the test controller that collects this data to create a detailed load test report which is available offline for further analysis.

Load Testing as a service by NIC
The NIC CCC has provisioned Apache JMeter based load testing infrastructure which has multiple agent machines to scale up the concurrency up to 20K virtual users. The controller has been made available as a web-based application where user can upload the JMeter Test Script, execute the load test and download the report. Load testing as a service application hosted at CCC which is using a farm of load generator servers at various locations for generating high concurrency traffic on the application as and when required. It is an online self-service at https://lts.ccc.nic.in and can be used by any project team for performance testing of respective application within NICNET.

Service 3-tier architecture
The core of the service is Apache JMeter, which is a leading open-source tool for load, performance and scalability testing. JMeter is a java application and not a web-based solution accessible via a browser which is a pre-qualification for use as a service. To overcome this, a web orchestration layer is developed on PHP with PostgreSQL as a backend. While the front end application takes care of features such as user authentication, creation of projects, test resource upload and test report download, the DB server stores metadata of parameters to be passed to JMeter for Test Execution. Parameters for Load test execution is captured by the web layer which runs the load test leveraging the command-line interface (CLI) of JMeter invoked through bash shell scripts. The test runs are configured to run from all the available load generators.

Availing Load Testing Service
Developing Test Scripts is the first activity to be carried out before availing of the service. After the scope of testing, the project is finalized and test cases are identified, the tester executes the application module step by step on the browser and records a series of HTTP requests using the recording controller of Apache JMeter to create the test scripts. Once the JMeter Test script is created and tested on a local machine for a small number of users, the user can avail the Load Testing service to execute the script for greater user load. The service request can be created through the cloud portal. The credentials for the Load Testing service application (https://lts.ccc.nic.in) will be created by NIC-CCC Administrator and shared with the user for the execution of Load test with the desired concurrency.

The overview of different modules of Load Testing Service application is as under:

Reserve Slot for Performance testing
A slot of Test execution is the duration for which the load generator servers are available exclusively for the given user. The system will display the available slots. The user would select and reserve the slot as per convenience.

Create Project
User can create a Performance test project by filling up the ‘Create Project’ form. User can create multiple projects and organize the test scenarios / scripts under relevant projects.

Upload Test Script
User should test the script on this local machine for 5-10 users and ensure its completeness from all aspects. Once the script is ready to be uploaded, the user would log in to the application and upload the script under the project created. Test data would be uploaded similarly.

Test Execution
Test execution module will be available during the duration reserved. The user would specify the project, test script and enter the test execution parameters like duration, concurrency, ramp-up time etc and run the test.

Download Report
The test report may be downloaded by visiting the report download module post-execution. The download report module would be a repository of all previous test executions. Test report of the last test execution is made available as soon as the test duration is complete and the report is ready.

Benefits of Load Testing Service
• Available to all applications hosted in NIC data centres or Cloud
• NIC-CCC team shall provide training on writing test scripts and using the self-service model which makes it simple and easy to avail
• Archival of test reports done for future reference
• Being internal service therefore may be availed as many times as required at different stages of deployment
• NIC project teams need not hire an agency for test execution

Application Areas
The service can be availed by any NIC project team developing web/ mobile applications, APIs, web services to test their application with the desired concurrency and ascertain their readiness for production deployment. Simulation of production-like traffic would help to identify any potential issues in the application code which may lead to performance downgrade. It will also help in estimating the resources required to sustain the expected traffic without compromising on the response time. Being black-box testing, it is agnostic of the inherent technologies and frameworks used for development.

For further information, please contact: Anil Rathore Senior Technical Director National Informatics Centre A-Block, CGO Complex Lodhi Road -110003 NEW DELHI Email: anilr@gov.in, Phone: 011-24305043
