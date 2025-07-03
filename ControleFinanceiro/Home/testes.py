import streamlit as st
import pandas as pd
import numpy as np

dataCaminho = "./ControleFinanceiro/Debito/data/dataExtrato.csv"

st.subheader("📂 Upload extrato mensal")

# Upload do arquivo
arquivo = st.file_uploader("🔼 Envie seu arquivo Excel (.xlsx; .csv ou .txt)", type=["xlsx", "csv", "txt"])

df_antigo = pd.read_csv(dataCaminho, sep=';')


if arquivo:
    # Lendo o arquivo Excel ou CSV corretamente
    if arquivo.name.endswith(".xlsx"):
        df = pd.read_excel(arquivo)
    elif arquivo.name.endswith(".csv"):
        df = pd.read_csv(arquivo, sep=";", encoding="utf-8")
    elif arquivo.name.endswith(".txt"):
        df = pd.read_csv(arquivo, sep=";", encoding="ISO-8859-1")

    # Exibe os dados carregados
    st.subheader("📊 Dados Originais:")
    st.dataframe(df)

# Botão para processar os dados
if st.button("🔼 Subir dados"):
    # Verifica se o df foi carregado corretamente
    if df is not None:
        if "data" in df.columns:
            df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")  # Converte para datetime
        
        df["valor"] = df["valor"].astype(float)  # Converte a coluna para float
        
        df["valorFinal"] = np.where(df["divide"] == "sim", df["valor"] / 2, df["valor"])        
        df['mes'] = df["data"].dt.strftime("%B")        
        df = df.loc[df['valorFinal'] <= 0]
        print(df)
        print('*'*100)
        df = pd.concat([df_antigo, df])
        print(df)        
        df.drop_duplicates(inplace=True)
        
        df.to_csv(dataCaminho, sep=";", mode="a", header=False, index=False, encoding="utf-8")


        # Exibe os dados transformados
        st.subheader("🔄 Dados Transformados:")
        st.dataframe(df)
    else:
        st.error("⚠️ Nenhum arquivo foi carregado! Faça o upload antes de aplicar transformações.")





