import streamlit as st
import pandas as pd

def uploadFile():
    st.subheader("📂 Upload extrato mensal")

    # Upload do arquivo
    arquivo = st.file_uploader("🔼 Envie seu arquivo Excel (.xls ou .csv)", type=["xls", "csv"])

    # Inicializa df como None para evitar erro
    df = None

    if arquivo:
        # Lendo o arquivo Excel ou CSV corretamente
        if arquivo.name.endswith(".xls"):
            df = pd.read_excel(arquivo)
        elif arquivo.name.endswith(".csv"):
            df = pd.read_csv(arquivo, sep=";", encoding="utf-8")
    return df