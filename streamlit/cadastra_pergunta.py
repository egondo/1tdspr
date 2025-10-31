import streamlit as st

def copia(lista: list) -> list:
    resp = []
    for item in lista:
        resp.append(item)
    return resp

st.set_page_config(layout="wide")

if not "alternativas" in st.session_state:
    st.session_state.alternativas = []

if not "perguntas" in st.session_state:
    st.session_state.perguntas = []


st.subheader("Insere pergunta")
enunciado = st.text_input("Enunciado: ")
tipo = st.selectbox("Tipo: ", ['aberta', 'única', 'múltipla'])

col1, col2 = st.columns(2)
with col1: 
    alt = st.text_input("Alternativa: ")
with col2:
    if st.button("Add"):
        st.session_state.alternativas.append(alt)
        st.write(st.session_state.alternativas)

if st.button("Cadastra"):
    pergunta = {
        "enunciado": enunciado,
        "tipo": tipo,
        "itens": copia(st.session_state.alternativas)
    }
    st.session_state.alternativas = []

    st.session_state.perguntas.append(pergunta)

st.write(st.session_state.perguntas)