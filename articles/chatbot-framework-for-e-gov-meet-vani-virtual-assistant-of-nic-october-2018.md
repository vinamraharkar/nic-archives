---
title: "Chatbot Framework for e-Gov: Meet VANI - Virtual Assistant of NIC"
publication: "Informatics"
issue_date: "October 2018"
pages: [34, 35]
author: "MOHAN DAS VISWAM (Editor), VARINDRA SETH, Sr. Technical Director, JOHN PHILIP, Technical Director, NIDHI LOHAT, Scientific Officer-SB"
section: "Technology Update"
---

## Chatbot Framework for e-Gov: Meet VANI - Virtual Assistant of NIC

Chatbot is a piece of software that aims to interact, and respond with a user like any human would. Unlike a traditional software application whose behaviour is tightly bound by its design and code, a chatbot relies more on underlying machine learning algorithms that help it to recognize and identify patterns, make classifications into different classes of data or make decisions based on threshold set for a continuous type of data. It’s an accessible form of Artificial Intelligence (AI) that is increasingly being put to use in businesses everywhere. Right from travel enquiries to bank loans, we see chatbots being the primary point of contact for most common enquiries and issues across all the fields of work today.

TECHNOLOGY BRIEF
Chatbots are the prime and most easily implementable example of AI, encompassing deep learning, natural language processing, and machine learning algorithms. Like any AI driven application, Chatbots also need massive amounts of data to produce fruitful results. The more an end user interacts with the bot, the better recognition becomes at predicting what the appropriate response is when communicating with an end user. This process is called training the engine.

Chatbots can be stateless or stateful. A stateless chatbot approaches each interaction as if it was with a new user. A stateful chatbot is more sophisticated; it can review past interactions and frame new responses in same context. Consider the following chat (figure 1).

This chat snippet is an example of a ‘stateful’ bot. The user has mentioned only once in the beginning that his/her overall issue is email related. From the next response onwards, the bot implicitly understands that further responses will be related to email. This is called maintaining a particular context. The fact that the bot could identify that the user wants a new email account out of the whole conversation is called identifying the intent.

Conducting a conversation is an extremely difficult task for even humans, for everyone interprets a spoken sentence according to their own understanding of language, past experiences, etc. This is one of the main reasons chatbots misunderstand, or are unable to understand user sentences. Over a period of time, there has been paradigm shift in how chatbots understand and respond to human queries. These paradigms are classified into three generations (figure 2).

GENERATION 1
Based on simple written rules, chatbot handles only the specific rules that are known to it. If the user says something other than what is known to the chatbot, it results in a failure condition.

GENERATION 2
Based on supervised machine learning, one needs to label the training data and then train a model to learn how to accordingly respond to the user. This also needs a lot of labelled training data. The more a model is trained, the more accurate responses to the user are.

GENERATION 3
Based on adaptive unsupervised learning, the AI Chatbot can learn from unlabelled data. This generation generally combines the benefit of previous generations. It can use rules and labelled data and the ability to learn from unlabelled data to handle more complex conversations.

GENERIC FEATURE REQUIREMENT IDENTIFICATION
A number of features can be implemented in an e-Gov services scenario for a chatbot:

••Identification of the issue
••On the spot solution
••Raising tickets for grievances
••Authentication
••Chat transfer to a human agent as a fall-back mechanism
••Voice chat
••Status/ Results
••Analytical Dashboard (Only for analysis purposes – not for user)
••Sentiment and Mood Analysis (not directly used by the end user)
••Accessible from different media like Web, Mobile App and even from an ordinary mobile phone through voice

CHATBOT FRAMEWORK IMPLEMENTATION - TECHNOLOGY

UI+Business Logic Layer
It is the point of interface with the user. All the business logic, validations, and exception handling are implemented here.

Middle-ware Layer
Works as an API Manager – manages the communication between UI layer and back-end AI engine via APIs, and also manages the chat transfer mechanism with the human agent.

AI Engine Layer
Heart of the whole AI Engine. It can take the user input in natural language format and classifies it into a specific problem-subproblem domain.

Human Agents
Work as a fall-back arrangement in case the engine failed to classify the given user input into any specific problem domain.

FEATURES CURRENTLY IMPLEMENTED IN VANI (VIRTUAL ASSISTANT OF NIC)
VANI is a Chatbot of NIC which is having the following implemented features:

••Identification of the issue
••Raising tickets for grievances
••OTP Authentication
••Chat transfer to a human agent as a fall-back mechanism
••Analytical Dashboard

UPCOMING FEATURES
The following features are currently in testing phase, and will later be released in pilot mode to gauge user acceptance:

••Voice Chat (as a Mobile App like a WhatsApp voice chat) and would also be available on the voice enabled IVRS (Interactive Voice Response System)
••On the spot solutions (instead of raising tickets directly, where applicable)

USE CASE IMPLEMENTATION
VANI is currently employed for the help-desk services at servicedesk.nic.in. In its current form, VANI recognises and classifies the specific user problem, and its subproblem, from the user text received. It was decided to design the engine in a way where each main problem category like Email, VPN, AEBAS, Network etc., was imagined as a container, and their subcategories were like objects inside the container. Much like the Figure 4.

POTENTIAL FOR E-GOV
VANI sees its application in a number of ventures that are run for the citizens such as application statuses, info foraging, grievance and redressal.
