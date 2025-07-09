import pandas as pd
import streamlit as st

st.subheader("📂 Upload extrato mensal")

# Upload do arquivo
arquivo = st.file_uploader("🔼 Envie seu arquivo Excel (.xls ou .csv)", type=["xls", "csv"])
df = None  # Inicializa fora da condicional

# Processamento do arquivo
if arquivo is not None:
    try:
        if arquivo.name.endswith(".xls"):
            df = pd.read_excel(arquivo)
        elif arquivo.name.endswith(".csv"):
            df = pd.read_csv(arquivo, sep=";", encoding="utf-8")

        if df.empty:
            st.warning("⚠️ O arquivo enviado está vazio. Verifique o conteúdo e tente novamente.")
        else:
            st.success("✅ Arquivo carregado com sucesso!")
            st.dataframe(df)

    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {e}")
else:
    st.info("🔍 Aguardando envio do arquivo...")