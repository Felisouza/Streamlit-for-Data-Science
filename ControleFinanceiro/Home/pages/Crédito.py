import streamlit as st
import pandas as pd
import sys
import os
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events
import pickle

# Adiciona o caminho do diretório onde está o módulo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'CartaoDeCredito')))
from uploadArquivoCredito import uploadFile
from LimpaDados import LimpaDados

# Adiciona o caminho do Utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from lottie_animation import load_lottieUrl
from st_aggrid import AgGrid



# caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils'))

# # Agora você pode importar a função
# from uploadArquivoCredito import uploadFile
# from LimpaDados import LimpaDados
# from botoes import listaGastos, botaoDatas
# from
#
lottie_card = "https://lottie.host/4fb821c9-1d70-48c0-8a34-a3a1809dd47d/ZjCrGMPKTx.json"

lottie = load_lottieUrl(lottie_card)
st_lottie(lottie, height=150)

#Título principal
st.markdown("<h1 style='text-align: center; color: white;'> 📊 Controle Financeiro - Crédito</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;'> Insira a fatura atual</h2>", unsafe_allow_html=True)

# Inserir nova fatura
arquivo = uploadFile()


# Processamento do arquivo
if arquivo is not None:
    df = LimpaDados(arquivo)

    # Modelo random forest
    caminho_atual = os.getcwd()
    caminho_modelo = os.path.abspath(os.path.join(caminho_atual, 'CartaoDeCredito\modelos')) + "\RandomForest.pkl"
    with open(caminho_modelo, 'rb') as arquivo:  # 'rb' = read binary
        modelo = pickle.load(arquivo)
    df['Tipo'] = modelo.predict(df['NmGasto'])
    df['Dono'] = ''


    response = AgGrid(df, editable=True)
    df_editable = response["data"]
    st.write("DF Editado")
    st.dataframe(df_editable)
else:
    st.info("🔍 Aguardando envio do arquivo...")



# botaoDatas()
# listaGastos(df=df)
#
#
# # Simulação de gastos
# st.subheader("Histórico de Movimentações")
# st.dataframe(df)


# # Resumo financeiro
# st.subheader("Resumo Financeiro")
# saldo_total = 'XXXXX'
# credito_disponivel = 'XXXXXX'
# gasto_mes = 'XXXXX'
#
# # Exibição de métricas
# col1, col2, col3 = st.columns(3)
# col1.metric(label="💰 Saldo Atual", value=f"R$ {saldo_total}")
# col2.metric(label="🏦 Crédito Disponível", value=f"R$ {credito_disponivel}")
# col3.metric(label="📉 Gastos no Mês", value=f"R$ {gasto_mes}")
#
