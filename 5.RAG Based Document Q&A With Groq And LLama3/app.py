import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain


from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
import openai

from dotenv import load_dotenv
load_dotenv()


## load the GROQ API Key
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

###Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = "Q&A ChatBot With Groq(pratice)"  ##Creating the New Project in Langsmith 
os.environ['LANGCHAIN_TRACING_V2'] = "true"



groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(groq_api_key = groq_api_key, model_name = "Llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Question:{input}

    """
)

#session state 
def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OpenAIEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("research_papers") ## Data Ingestion step
        st.session_state.docs = st.session_state.loader.load() ## Document Loading
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)


st.title("RAG Based Document Q&A With Groq And LLama3")

user_prompt = st.text_input("Enter your query from the Research Paper")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector Database is ready")


import time


if user_prompt:
    #document_chain = create_stuff_documents_chain(llm,prompt)
    #retriever =  st.session_state.vectors.as_retriever() #st.session_state.vectors.as_retriever()
    #retrieval_chain = create_retrieval_chain(retriever,document_chain)

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever =  st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input':user_prompt})
    print(f"Response time :{time.process_time() - start}")

    st.write(response['answer'])

    ## With a streamlit expander
    with st.expander("Document similarity Search"):
        for i,doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write('------------------------')





