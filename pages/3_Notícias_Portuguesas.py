import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import requests
import random

GPT_MODEL = "gpt-4"
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

st.title('Ridicularizando as Manchetes 📰')


def generate_response(input_text):
    chat = ChatOpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY, model=GPT_MODEL)
    messages = [
        SystemMessage(content="O utilizador vai fornecer um título de uma notícia. O teu trabalho é inventar uma notícia que corresponda com o título. A notícia deve ser engraçada, ou até mesmo ridícula, e deve caber num pequeno parágrafo"),
        HumanMessage(content=input_text)
    ]
    return chat(messages)

def get_quote():
    res = requests.get(url='https://newsapi.org/v2/top-headlines?country=pt&apiKey=b9be9dbbf470423285ec760333432d4c')
    res = res.json()
    article = random.choice(res['articles'])
    return article['title'], article['source']['name']

if st.button(label='Obter notícia'):
    quote, author = get_quote()
    st.write('### ' + quote)
    st.write('*' + author + '*')
    with st.spinner(text='Recuperando a notícia...'):
        interpretation = generate_response(quote)
    st.write('### `' + interpretation.content + '`')
