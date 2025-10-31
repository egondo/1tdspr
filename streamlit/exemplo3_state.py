import streamlit as st

#instanciando uma lista e guardando na sessão http
if not "alternativas" in st.session_state:
    st.session_state.alternativas = []

#criando caixa de texto para adicionar alternativas
alt = st.text_input("Alternativas: ", value="")

#clicou no botao ADD, a alternativa é adicionada
if st.button("Add"):
    st.session_state.alternativas.append(alt)
    st.write(st.session_state.alternativas)
