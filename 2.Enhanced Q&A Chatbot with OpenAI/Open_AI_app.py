import streamlit as st
import openai


#############################################################################
#------------------  Enhanced Q&A Chatbot with OpenAI-----------------------
#############################################################################

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

########################################################################
### Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = "Q&A ChatBot With OPENAI"
os.environ['LANGCHAIN_TRACING_V2'] = "true"

###Openai Api key
openai_api_key = os.getenv("OPENAI_API_KE")


#### Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Helpful AI Assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)


### Function to Generate Response
def generate_response(question, llm, temperature, max_tokens):
    # Set the OpenAI API key directly
    openai.api_key =  openai_api_key  #OpenAI API key

    llm = ChatOpenAI(model=llm)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer


#### Title
st.title("Enhanced Q&A Chatbot with OpenAI")

## Sidebar for Settings
st.sidebar.title("Settings")

#### Drop Down to Select Various OpenAI Models
llm = st.sidebar.selectbox("Select an OpenAI Model", ["gpt-4o", "gpt-4-turbo", "gpt-4"])

##Response Parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

### Main Interface for User Input
st.write("Go Ahead and Ask any question")
user_input = st.text_input("You:")


if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please Provide the Query?")