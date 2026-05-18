---
title: "Salted Hashing of Passwords"
publication: "Informatics"
issue_date: "July 2009"
pages: [32, 33]
author: null
section: "Technology Update"
---

## Salted Hashing of Passwords

What is a Hash?

Hash algorithms map binary values of an input of arbitrary length to a binary value of a fixed length, known as hash values. A hash value is a unique and extremely compact numerical representation of a piece of data. If you hash a paragraph of plaintext and change even one letter of the paragraph, then a subsequent hash will produce a different value. It is computationally improbable to find two distinct inputs that hash to the same value. A hash value is also known as a Message digest. MD5, SHA1 etc. are Hash Algorithms. The following sections illustrate salted hashing with respect to MD5 algorithm. Other hash algorithms such as SHA-1 may be used alternately.

During the course of Penetration testing of Web Applications at Cyber Security Division, NIC, several security vulnerabilities are identified. One of these vulnerabilities includes the finding that the credentials traveling in clear text can be sniffed from the network. The credentials can also be detected with the help of memory editing tools on shared systems which are used to access the authentication web pages. Considering the common nature of these problems and their solutions, throwing light on the underlying concepts is a must read for those targeting the problem while developing secure code in an effective manner. The following section sheds light on the solution to the problem.

Application of MD5 to protect passwords

— Problem: When a site visitor submits his/her credentials on a login page it is submitted in clear text and this can be obtained by malicious users from a browser of a user even though he/she may have logged out. But to make it possible, the hacker must have access to the user's system, which may be possible in the case of shared system in kiosks etc. Also, another precondition to this is that the browser must have not been closed.

Similarly, this can be illustrated with the help of Network sniffing tools when credentials are traveling in clear text.

— Solution: The problem outlined above can be solved with hashing. A hash of the password can be sent from the client browser to the server application. It is not possible to extract the clear text password from the network or from the browser memory as only the hashed form of the password can be obtained.

Threat of Hash Replay

However, a hashed password submitted from the client can be sniffed while in transit from the network or obtained from a shared system used to browse the web site with the help of tools. This hashed password can then be replayed or pasted while submitting to the server and access gained as seen from tests in the lab.

Solution: Salted Hashed Password

Salted MD5 hash of the password can be submitted to avoid the replay attack. In this case the password will vary every time the salted MD5 password is submitted to the server. Since the salt is a random number and changes every time, the salted hashed password also changes every time.

The pre-requisite to this is that the backend database stores a hash of the password. When a client requests for the login page, the server generates a random number or the salt, and sends it to the client along with the page. A JavaScript code on the client computes the MD5 hash of the password entered by the user. It then concatenates the salt to the hash and re-computes the MD5 hash. This result is then sent to the server. The server picks the hash of the password from its database, concatenates the salt and computes the MD5 hash. If the user entered the correct password, these two hashes should match. The server compares the two and if they match, the user is authenticated. This session persists or is valid till the user logs out or the session times out due to inactivity.

Verification of a salted hash implementation in an application

It can be seen from the above sample snapshots of an application with salted hash implementation in the authentication module, the salted hash passwords are different at the two instances of authentication and hence cannot be used in replay attacks.

Effective implementation of the above steps in the code logic is an adequate defense against the credentials leakage problem encountered in web applications accessed from shared client systems used for browsing authenticated sessions as well as from the network.

Step by step illustration of the salted MD5
