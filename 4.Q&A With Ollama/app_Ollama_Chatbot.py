import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama




import os
from dotenv import load_dotenv

load_dotenv()


###Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = "Q&A ChatBot With Ollama"
os.environ['LANGCHAIN_TRACING_V2'] = "true"



#### Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assitant.Please response to the user quries"),
        ("user","Question:{question}")
    ]

)


###Function
def generate_response(question,llm,temperature,max_tokens):
    llm = Ollama(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({'question':question})
    return answer
    

## #Title of the app
st.title("Question & Answering Chatbot With Ollama")


## Select the OpenAI model
llm = st.sidebar.selectbox("Select Open Source model",["llama3","mxbai-embed-large","gemma:2b","llama2"])

## Adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.5)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for user input
st.write("ASK  Any Question")
user_input = st.text_input("You:")



if user_input :
    response = generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")



