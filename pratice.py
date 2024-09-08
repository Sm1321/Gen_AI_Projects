import streamlit as st
import os




if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.session_state.uploaded_file = uploaded_file





user_input = "Bhai"

if "form_step" not in st.session_state:
    st.session_state.form_step = 1

if st.session_state.form_step == 1:
    user_input = st.text_input("Enter your name:")
    if st.button("Next"):
        st.session_state.form_step += 1
elif st.session_state.form_step == 2:
    st.write(f"Hello, {user_input}!")
    # Proceed to the next steps or finish the form
