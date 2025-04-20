from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load the models and get the responses
model=genai.GenerativeModel("gemini-1.5-pro-latest")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text
    
### Initialize the streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM application")

input=st.text_input("Input :",key="input")

submit=st.button("Ask the question")

## When submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)