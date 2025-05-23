import streamlit as st
import pandas as pd

#alterando a pagina para usar a largura inteira da tela
st.set_page_config(layout="wide")

#lendo o arquivo csv e gerando data-frame
df = pd.read_csv("filmes.csv", sep=";")

#lista de diretores unica do data-frame
diretores = df['Diretor'].unique()

lista = sorted(diretores) #ordenando a lista
lista.insert(0, "")       #colocando um item vazio na lista

#caixa de seleção do diretor
diretor = st.selectbox("Diretor(es): ", lista)

if diretor != '':
    df_filtrado = df.query(f"Diretor == '{diretor}'")
    st.write(df_filtrado)
else:
    st.write(df)

df_filmes_por_ator = pd.pivot_table(df, values="Titulo", index=["Ator"],aggfunc="count")
st.write(df_filmes_por_ator)