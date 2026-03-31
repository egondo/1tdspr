import pandas as pd
import streamlit as st


df = pd.read_csv("faturamento_2025.txt", delimiter=";")


#datas = df['data'].unique()
#print(f"Tipo da coluna data: {type(datas[0])}")

df['data_real'] = pd.to_datetime(df['data'])
df['total'] = df['valor'] * df['qtd']

#st.write(df)
lojas = df['loja'].unique()

#loja_selecionada = st.selectbox("Loja", lojas)
#df2 = df.query(f"loja == '{loja_selecionada}'")
#st.write(df2)

df['mes'] = df['data_real'].dt.month


produtos = df['produto'].unique()
prod = st.selectbox("Produto: ", produtos)
df_filtrado = df.query(f"produto == '{prod}'")
tabela_dinamica = df_filtrado.pivot_table(values="total", index=["mes"], columns="loja", aggfunc="sum")

st.bar_chart(data=tabela_dinamica)
st.write(tabela_dinamica)

