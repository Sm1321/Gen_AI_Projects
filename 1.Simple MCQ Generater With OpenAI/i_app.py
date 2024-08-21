from openai import OpenAI
import streamlit as st

# Load the API key
with open("keys/.open_AI_Key.txt") as f:
    key = f.read()

# Initialize the OpenAI client
client = OpenAI(api_key=key)

##########################################
##Title
##st.snow()
st.title("💬MCQ Generater With OpenAI")
st.subheader("A simple Web application ")


#################################################
# Take User's Input
prompt = st.text_input("Enter the Data Science Topic:")

# If the button is clicked, generate response
if st.button("Generate"):
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI Assistant. Given a Data Science topic, you always generate 3 MCQ questions and answers for the test."},
            {"role": "user", "content": prompt}
        ]
    )

    # Print the response on the web app
    st.write(response.choices[0].message.content)
