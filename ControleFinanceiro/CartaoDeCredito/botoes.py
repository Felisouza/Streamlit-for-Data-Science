import streamlit as st
import pandas as pd

def listaGastos(df):
    if df == None:
        df = pd.DataFrame({'NmGasto': ['-'], "Data":['-'], "Valor":['-']})
    else: df
# Seleciona os gastos que vc quer arrumar
    chave = [
        df['Data'].astype(str) 
        + '_' + df['NmGasto'].astype(str) 
        + '_' + df['Valor'].astype(str) 
    ]
    # opcoes = ['Selecione o gasto'] + df['NmGasto'].tolist()
    opcoes = ['Selecione o gasto'] + chave
    print(opcoes)
    gastoSelecionado = st.selectbox("Gastos: ", opcoes)
    if st.button("Selecionar"):
        st.write(f"Nova movimentação adicionada:")

def botaoDatas():
    # Criando um seletor de data
    data_selecionada = st.date_input("📅 Selecione uma data:")
    print(data_selecionada)
    return data_selecionada