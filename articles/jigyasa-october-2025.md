---
title: "Jigyasa"
publication: "Informatics"
issue_date: "October 2025"
pages: [24, 25]
author: "Sapna Kapoor, Sneha Lotankar, Gangashankar Singh"
section: "e-Gov Products & Services"
---

## Jigyasa

The digital revolution now touches every corner of India. Millions of government services are online, delivering transparency, inclusion and broader access. Yet citizens still face fragmented portals, unintuitive UI/UX and complexity that turn simple civic tasks into prolonged, often discouraging journeys.
India has proven its global leadership in cost-effective e-Governance solutions, yet citizens still struggle with interfaces that fail to provide meaningful, guided interactions. Jigyasa revolutionizes this landscape as a seamless, AI-powered, multilingual conversational layer that can be plugged into existing e-Gov solutions. It transforms complex systems into intuitive, human-centered experiences where users simply ask and are navigated to the relevant sections. With Jigyasa, digital governance becomes not just accessible but profoundly intuitive, inclusive, and empowering.
Jigyasa resolves that friction to some extent. As an AI-empowered sahayika for Digital India, it is a plug-in conversational layer that integrates with any government website or app. Users speak in natural language; Jigyasa understands intent, retrieves answers or points to the exact form or page, and can translate instantly via services like Bhashini, turning the whole interaction into a calm, guided conversation.
Features & Capabilities
• No hassle integration: Easily integrates into existing government websites through API calls
• Customizable AI models: Can be tailored to use different AI models for different use cases
• Multilingual Support: Supports multiple languages with optional integration of translation services such as Bhashini
• Feedback driven training: Continuously improves through real user feedback
Sapna Kapoor
Dy. Director General & SIO
sapna.kapoor@nic.in
Sneha Lotankar
Sr. Technical Director
sneha.nl@nic.in
Gangashankar Singh
Scientist-B
sg.indra@nic.in
• CPU & GPU variants: Variants available for both CPU and GPU infrastructures.
• Customizable chatbot UI and themes: Dynamic chatbot customizable to match the specific look and feel of any application or website.
Technology and architectural flow
At the heart of Jigyasa lies a carefully engineered intelligence pipeline which can be understood through five powerful pillars that transform raw queries into meaningful, guided experiences.
Special Semantic Search
Unlike conventional keyword-based search, Jigyasa infuses semantic intelligence that harmonizes keyword signals with deep contextual understanding. The user has the liberty to choose either keyword search, semantic search, or both, depending on their needs. With adjustable weights, it balances domain-specific keywords and nuanced meanings, capturing intent, relationships, and context. This ensures that even vague or unstructured queries are resolved with precise, relevant results.
AI-based Reranking
Once candidate results are retrieved, Jigyasa applies advanced reranking models. Each result is scanned and re-evaluated to determine whether it truly answers the query. This ensures that the system does not just return “something similar” but instead pushes the contextually aligned answers to the top.
Knowledge Graph Synthesis
Raw answers alone are not enough, Governance information is often interconnected. Jigyasa transforms retrieved knowledge into a structured knowledge graph, weaving together information located on different pages into a coherent storyboard, giving user a complete, context-rich response that truly resolves his/her Jigyasa (curiosity).
AI-based Navigation
Through its interactive storyboard, users can navigate directly to the exact piece of information with a single click. It transforms static portals into living, conversational journeys where information is both delivered and contextually explored instantaneously even if it’s buried deep within the sitemap.
Feedback and Enhancement
Every interaction is a learning opportunity. Jigyasa collects user feedback and performance data, feeding it back into its models to constantly refine accuracy, responsiveness, and contextual depth. This closed-loop system ensures that Jigyasa is not static but an ever-evolving AI assistant that grows sharper with every query.
Tech Stack and Workflow
Jigyasa is designed to work with containerized components, ensuring scalability and performance with Docker. Each of the following components communicates via APIs built on Python FastAPI.
• Data Extraction: Crawls, chunks, and stores content in text and vector formats using FastAPI + Qdrant DB
• Information Retrieval: Delivers the most relevant content via keyword and semantic search, powered by open-weight AI models
• Optional LLM: Converts retrieved data into a knowledge graph, revealing deep insights
• Pluggable Frontend: Dynamic, customizable JS interface that learns from feedback and integrates effortlessly
Benefits
Jigyasa delivers immediate, measurable value to every stakeholder, transforming the e-governance experience from a challenge into an opportunity.
For Citizens
• Zero-Learning-Curve Access: Find information instantly by asking naturally in your preferred language
• Enhanced Digital Inclusion: Breaks down barriers for non-tech-savvy users, non-native English speakers, and persons with disabilities
• Time and Cost Savings: Drastically reduces the time and effort spent on simple tasks, from form searches to scheme eligibility checks
For Government Departments
• Reduced Support Burden: Cuts down helpline calls and in-person queries, freeing staff for complex, high-value tasks. Data-Driven Insights: Gain real-time analytics on citizen pain points, popular queries, and portal inefficiencies
• Seamless Integration: Low-cost, API-based plugin works with existing infrastructure, protecting previous investments
• Accelerated Digital Adoption: Intuitive interaction builds trust and encourages wider use of e-governance services
• Unified, Multilingual Access: Delivers a consistent, high-quality experience across all portals, strengthening the Digital India brand
• Increased Transparency: Provides clear, direct pathways to information fostering greater public trust
Conclusion
A functional model of Jigyasa was recently demonstrated to the Principal Secretary of IT, Maharashtra, leading to the department’s decision to sponsor GPU resources under the IndiaAI mission. As we move towards securing the production infrastructure, our parallel objective is to evolve Jigyasa from a standalone solution into a foundational, open-source platform. This strategic transformation will enable NIC to build and deploy intelligent assistants across its projects, driving a significant shift in the e-Governance ecosystem.
Contact for more details
State Informatics Officer
NIC Maharashtra State Centre
11th Floor, New Administrative Building
Madam Cama Road, Mumbai-400032
Email: sio-mah@nic.in, Phone: 022-22046934/ 22837339
