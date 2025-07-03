import streamlit as st
import pandas as pd

def uploadExtrato():
    # Título do aplicativo
    st.subheader("📂 Upload extrato mensal")

    # Upload do arquivo
    arquivo = st.file_uploader("🔼 Envie seu arquivo Excel (.xlsx ou .csv)", type=["xlsx", "csv"])

    # Inicializa df como None para evitar erro
    df = None

    if arquivo:
        # Lendo o arquivo Excel ou CSV corretamente
        if arquivo.name.endswith(".xlsx"):
            df = pd.read_excel(arquivo)
        elif arquivo.name.endswith(".csv"):
            df = pd.read_csv(arquivo, sep=";", encoding="utf-8")

        # Exibe os dados carregados
        st.subheader("📊 Dados Originais:")
        st.dataframe(df)

    # Botão para processar os dados
    if st.button("🚀 Aplicar Transformações"):
        # Verifica se o df foi carregado corretamente
        if df is not None:
            if "data" in df.columns:
                df["data"] = pd.to_datetime(df["data"])  # Converte para datetime
            
            # Correção: Use `.loc` para evitar erro ao modificar colunas
            df.loc[df["divide"] == "Sim", "valorFinal"] = df["valor"] / 2

            # Exibe os dados transformados
            st.subheader("🔄 Dados Transformados:")
            st.dataframe(df)
        else:
            st.error("⚠️ Nenhum arquivo foi carregado! Faça o upload antes de aplicar transformações.")
    return
