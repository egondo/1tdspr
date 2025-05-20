import streamlit as st

st.set_page_config(page_title="Primeiro exemplo Streamlit", layout="wide")
nome = st.text_input("Informe o seu nome")

curso = st.selectbox("Qual o seu curso?", ["ADS", "SI", "TJ", "TBD", "CC"])
nota = st.slider("Qual nota vc daria para o curso de ADS?", 0, 10, 0)
disciplinas = st.multiselect("Quais disciplinas vc tem mais dificuldade?", ["CTP", "AI", "DATABASE", "FRONTENT", "DDD"])

botao = st.button("Cadastra")

if botao:
    st.write(f"{nome} estuda {curso}: {nota}")
    for item in disciplinas:
        st.write(item)
 
