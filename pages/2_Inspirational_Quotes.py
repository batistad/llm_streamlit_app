import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import requests

GPT_MODEL = "gpt-4"
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

st.title('Inspirational Laughs 🤯')


def generate_response(input_text):
    chat = ChatOpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY, model=GPT_MODEL)
    messages = [
        SystemMessage(content="The user will provide you an inspirational quote. Your job is to come up with a very witty, sarcastic, or just plain funny response or comment to it."),
        HumanMessage(content=input_text)
    ]
    return chat(messages)

def get_quote():
    res = requests.get(url='https://api.fisenko.net/v1/quotes/en/random')
    res = res.json()
    return res['text'], res['author']['name']

if st.button(label='Get quote'):
    quote, author = get_quote()
    st.write('### ' + quote)
    st.write('*' + author + '*')
    with st.spinner(text='Loading humor...'):
        interpretation = generate_response(quote)
    st.write('### `' + interpretation.content + '`')
