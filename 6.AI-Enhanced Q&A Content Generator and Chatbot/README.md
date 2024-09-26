### Project Title: AI-Enhanced Q&A Content Generator and Chatbot

1. Business Problem

Manual generation of course Q&A content is time-consuming and inefficient. Educators often spend a significant amount of time creating question and answer sets for various topics, which can detract from their primary teaching responsibilities.


2. Objective

The primary objective of this project is to automate the Q&A creation process while minimizing plagiarism. By leveraging advanced AI technologies, the goal is to provide an efficient solution for educators to generate unique and relevant Q&A content quickly.

3. Approach

To achieve the project objectives, we developed a real-time Q&A generator system utilizing:

Gemini-Pro: A generative AI model that enhances the quality and context of responses.
LangChain: A framework that simplifies the integration of language models for various tasks, including document processing and question answering.
Google Generative AI Embeddings: Used for embedding text into dense vectors for efficient similarity search.

4. Technologies Used
LangChain: For building chains of actions and integrating multiple language models.
Generative AI: To generate natural language responses and content.
Google Gemini: A large language model providing generative capabilities.
LLMs (Large Language Models): For understanding and processing the text.
Transformers: For leveraging state-of-the-art NLP techniques.

5. Implementation Steps
PDF Upload and Text Extraction:

Users can upload PDF documents, from which text is extracted using the PyPDF2 library.

Text Chunking:
The extracted text is divided into manageable chunks using the RecursiveCharacterTextSplitter to optimize processing for similarity searches and responses.
Creating FAISS Index:

A FAISS index is created to facilitate fast similarity searches on the text chunks, enabling the system to efficiently retrieve relevant information based on user queries.


User Interaction:
The application features a user-friendly interface where users can:
Generate Multiple Choice Questions (MCQs) based on specific topics.
Ask questions about the PDF content for instant answers.
Q&A Generation:

The system uses a tailored prompt to guide the language model in generating accurate answers based on the context extracted from the uploaded PDF.

Output:
Generated MCQs and answers to user questions are displayed in the application, allowing for immediate feedback and further interaction.

6. Conclusion
This project effectively automates the generation of Q&A content, saving time for educators and enhancing the learning experience for students. By leveraging cutting-edge AI technologies, the system provides a scalable and efficient solution to address the challenges of manual Q&A creation.


## Deployment

To deploy this project run

```bash
  streamlit run filename.py
```


