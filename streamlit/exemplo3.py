import streamlit as st
import requests

data = requests.get("http://127.0.0.1:5000/perguntas/1")
lista = data.json()
for pergunta in lista:
    
    if pergunta['tipo'] == 'aberta':
        resp = st.text_input(pergunta['questao'], key=f"{pergunta['id']}")
    elif pergunta['tipo'] == 'unica':
        st.radio(pergunta['questao'], pergunta['itens'], key=f"{pergunta['id']}")
    elif pergunta['tipo'] == 'multipla':
        st.checkbox(pergunta['questao'], pergunta['itens'], key=f"{pergunta['id']}")
        st.write(pergunta['itens'])