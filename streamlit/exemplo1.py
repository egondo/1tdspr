import streamlit as st

st.set_page_config(layout="wide")
nome = st.text_input("Nome: ")
idade = st.number_input("Idade", min_value=0, max_value=150)
genero = st.selectbox("Gênero: ", ["masculino", "feminino", "não binário"])

disciplina = st.radio("Qual a disciplina que vc tem mais dificuldade?", ["Front", "CTP", "Banco", "DDD"])


if st.button("ok"):
    st.write(f"Seu nome é {nome} e vc tem {idade} anos! E vc se declarou com o genero {genero}")
    st.write(f"A diciplina mais difil é {disciplina}")