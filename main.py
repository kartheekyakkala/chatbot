import os
import streamlit as st
from langchain.document_loaders import UnstructuredFileLoader
from langchain.indexes import VectorstoreIndexCreator

if os.getenv("OPENAI_API_KEY") is None:
    # Replace with your OpenAI API key
    os.environ["OPENAI_API_KEY"] = "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"

st.title("Chatbot App")

# Initialize the chatbot components
loader = UnstructuredFileLoader(f'./700754606.pdf')
index = VectorstoreIndexCreator().from_loaders([loader])

def get_response(user_input):
    return index.query(user_input)

st.sidebar.header("Chat Options")
st.sidebar.write("You can chat with the AI in the main panel on the left.")

st.text("Chat with the AI:")
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        ai_response = get_response(user_input)
        st.text("AI:", ai_response)

st.write("To stop the chat, simply clear the input box or type 'stop'.")
