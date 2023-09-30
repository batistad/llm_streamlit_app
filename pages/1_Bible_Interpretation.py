import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import requests

GPT_MODEL = "gpt-4"
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

st.title('The Holy Giggle 😇')

def generate_response(input_text):
    chat = ChatOpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY, model=GPT_MODEL)
    messages = [
        SystemMessage(content="The user will provide you a Bible verse. Your job is to come up with a very funny interpretation of that quote."),
        HumanMessage(content=input_text)
    ]
    return chat(messages)

def get_bible_verse():
    res = requests.get(url='https://bible-api.com/?random=verse')
    res = res.json()
    return res['text'], res['reference']

if st.button(label='Get verse'):
    verse, reference = get_bible_verse()
    for line in verse.split('\n'):
        st.write('### ' + line)
    st.write('*' + reference + '*')
    with st.spinner(text='Asking God for advice...'):
        interpretation = generate_response(verse)
    st.write('### `' + interpretation.content + '`')
