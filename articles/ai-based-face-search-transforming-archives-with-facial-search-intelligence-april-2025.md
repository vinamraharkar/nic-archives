---
title: "AI-Based Face Search: Transforming Archives with Facial Search Intelligence"
publication: "Informatics"
issue_date: "April 2025"
pages: [35, 36]
author: "Edited by MOHAN DAS VISWAM"
section: "Technology Update"
---

## AI-Based Face Search: Transforming Archives with Facial Search Intelligence

The President’s Secretariat maintains an extensive repository of photographs taken during official events held at Rashtrapati Bhavan and across various tours and engagements of the Hon’ble President of India. These images, captured by official photographers, document state functions, ceremonial occasions, and national milestones. Over time, this has resulted in the creation of a vast digital photo archive, a portion of which is publicly accessible through the Digital Photo Library (DPL) portal (https://dpl.rashtrapatibhavan.gov.in/).
While metadata-based search (by event, date, or keywords) is available, it becomes increasingly difficult to locate specific individuals across different events—especially when the user does not recall the event name or date. To address this, an AI-powered FaceSearch service has been introduced. This system enables users to search for photos by uploading a photo or taking a selfie, allowing facial recognition to identify images containing the same individual across the archive.
The Need for an AI-Driven Solution
Whenever the Hon’ble President participates in an event—be it at Rashtrapati Bhavan or during a state visit—the official photographer documents the occasion in detail. These photos are systematically uploaded to the Digital Photo Library. However, the need often arises to locate photographs of a specific person across multiple events. Without knowing the exact event name, date, or other metadata, finding such images through traditional filters can be time-consuming and ineffective.
Face-based search offers a more intuitive solution: by simply uploading an image, the system can identify and retrieve all photographs in which that person appears, regardless of the event context.
Background on Facial Recognition Technology
The core of the FaceSearch system lies in AI-based facial recognition, which uses deep learning models-primarily convolutional neural networks (CNNs)—to analyze and compare faces.
The facial recognition process involves:
• Face Detection: Identifying and isolating faces from the background in an image
• Feature Extraction: Generating unique facial embeddings—numerical vectors that represent the distinctive features of each face
• Similarity Matching: Comparing embeddings using cosine similarity or other metrics to determine how closely they match
These techniques have evolved to handle challenges such as changes in lighting, facial angles, age progression, or expressions, making them highly effective for large-scale photo retrieval.
Face search technology uses AI to identify and match faces across large photo collections. It extracts unique facial features from an image and compares them with stored data to find matches-regardless of lighting, angle, or expression. It enables fast, photo-based search without relying on names or dates.
System Architecture and Technical Details
The FaceSearch functionality has been integrated into the Digital Photo Library platform with a modular, scalable architecture comprising the following components:
Digital Photo Library Platform
• Frontend and Backend: Developed using PHP and PostgreSQL
• Photo Storage: Images are stored in a secure file system; metadata is stored in PostgreSQL
FaceSearch System
The facial recognition system is built in two layers:
• FaceSearch Web API:
• Built using FastAPI (Python)
• Manages incoming requests (image uploads), interfaces with the database, and communicates with the GPU-based encoding service
• Stores image encodings and metadata linkages
• Face Encoding Service
• Deployed on a GPU server
• Performs the facial feature extraction using pre-trained deep learning models
• Returns encodings to the Web API for storage and comparison
Workflow
• Image Upload & Storage
• A user uploads a photo to DPL or captures a selfie
• Metadata is stored in PostgreSQL
• The image is stored in the file system and sent to the FaceSearch API
• Encoding & Matching
• The API sends the image to the GPU-based encoding service
• The encoding service extracts facial features and returns a vector
• This vector is stored alongside the photo metadata
• When a search is initiated with a photo, the uploaded image is similarly encoded
• The system compares the query embedding with those in the database (filtered by other criteria like date/event)
• Matches are returned to the user, showcasing relevant photos
Key Features
Selfie and Photo-Based Search
Users can find photos using an image instead of relying on metadata
Advanced Filtering
Supports traditional filters like event name, date range, and keywords
Fast, Scalable Performance
GPU-backed encoding and efficient search mechanisms ensure quick results
Secure and Modular Design
Separation of services ensures maintainability and scalability
Future Enhancements
To further enhance the system’s capability and user experience, the following improvements are proposed:
Multi-Face Search
Enable simultaneous recognition of multiple faces within a single photo, useful for group photos.
Improved Facial Recognition Models
Continuously retrain the AI model using more diverse and up-to-date datasets to handle age variations, occlusions (like masks), and lighting differences more accurately.
Face Clustering and Similarity Grouping
Automatically group similar faces across the dataset using clustering algorithms to assist archivists and researchers.
Natural Language-Based Search
Integrate natural language processing (NLP) to support conversational queries like “Show all events with foreign dignitaries in 2024.”
Text-Image Multimodal Search
Use Multimodal Large Language Models (LLMs) to enable image retrieval based on text descriptions, even in the absence of detailed metadata.
Conclusion
The integration of AI-powered facial recognition into the Digital Photo Library marks a significant step toward modernizing archival access and enriching user experience. By allowing intuitive, image-based searches, the system not only enhances accessibility but also opens up new possibilities for historical research, documentation, and public engagement.
The journey ahead involves making the system smarter, faster, and more inclusive— ensuring that this national visual archive continues to serve as a living chronicle of the Presidency and the people of India.
