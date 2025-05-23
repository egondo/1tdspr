#pip install streamlit
#pip install pandas
#pip install matplotlib

#para executar
#streamlit run dashboard_caged.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CAGED", layout="wide")

df_total = pd.read_csv("data.csv", sep=";")

#substituicao de valores da serie
df_total['saldomovimentacao'] = df_total['saldomovimentacao'].replace({-1: 'desligado', 1: 'admitido'}, regex=True)

df_total['sexo'] = df_total['sexo'].replace({1: 'masculino', 3: 'feminino'})
df_total['graudeinstrucao'] = df_total['graudeinstrucao'].replace({1: 'Analfabeto', 2: 'Fundamental', 3: 'Fundamental', 4: 'Fundamental', 5: 'Fundamental', 6: 'Médio', 7: 'Médio', 8: 'Superior', 9: 'Superior', 10: 'PG', 11: 'PG', 80: 'PG', 99: 'NI'})

df_resumido = df_total[['competenciamov', 'secao', 'saldomovimentacao', 'graudeinstrucao', 'sexo', 'idade', 'unidadesalariocodigo','salario']]

col1, col2 = st.columns(2)

with col1:
    anomes = st.selectbox("data", [202501, 202502, 202503])
    movimentacao = st.selectbox("movimentacao", ['admitido', 'desligado'])
    
    df_filtrado = df_resumido.query(f'competenciamov == {anomes} and saldomovimentacao == "{movimentacao}" and unidadesalariocodigo == 5')

    #st.write(df_filtrado)
    tabela = pd.pivot_table(df_filtrado, values="salario", index=['graudeinstrucao'], columns=['sexo'], aggfunc=["mean", "count"])
    st.write(tabela)

with col2:
    fig, ax = plt.subplots()
    ax.hist(df_filtrado['idade'], bins=30)
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of idade')
    st.pyplot(fig)
