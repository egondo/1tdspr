import streamlit as st
import pandas as pd 


data = {
    "nome": ["Eduardo", "Martins", "Sérgio", "Roberto"],
    "nota": [6.5, 8.5, 4.9, 6.8],
    "salario": [3500, 5000, 7689, 4309]
}

df = pd.DataFrame(data)
st.write(df)