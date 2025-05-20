import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv("filmes.csv", sep=";")

diretores = df['Diretor'].unique()

lista = sorted(diretores)
lista.insert(0, "")
diretor = st.selectbox("Diretor(es): ", lista)

if diretor != '':
    df_filtrado = df.query(f"Diretor == '{diretor}'")
    st.write(df_filtrado)
else:
    st.write(df)

df_filmes_por_ator = pd.pivot_table(df, values="Titulo", index=["Ator"],aggfunc="count")
st.write(df_filmes_por_ator)