import os
import json 


from dotenv import load_dotenv
load_dotenv()


import streamlit as st
from groq import Groq



#Streamlit Code
# streamlit page configuration
st.set_page_config(
    page_title="LLAMA 3.1. Chat",
    page_icon="🦙",
    layout="centered"
)

###USe the Groq API Key
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

groq_llm = Groq()

## Intialize the ChatHistory as Streamlit session State.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


#Streamlit Page Title
st.title("🦙 LLAMA 3.1. ChatBot")

##Display the ChatHistory
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



##Input box for the user message
user_prompt = st.chat_input("Ask Question... ")

###Append the userChat to the ChatHistory
if user_prompt:
    st.chat_message("user").markdown(user_prompt) ##this is from user
    st.session_state.chat_history.append({"role":"user","content":user_prompt})
    

    ##send user's Message to the LLM na dGet A Response
    messages = [
        {"role":"system","content":"you are a helpful Assistant"},
        *st.session_state.chat_history  ##Unpacking all the LLM and send to the LLM 
    ]


    ####
    response = groq_llm.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages = messages
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display the LLM's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)




        


