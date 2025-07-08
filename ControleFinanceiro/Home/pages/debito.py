import streamlit as st
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import json
# from lePlanilha import lePlanilhaCSV, lePlanilha
import os
# from extrato import uploadExtrato

def EmManutencao():
    st.subheader("🚧 Página em Construção")
    st.warning("⚠️ Esta funcionalidade ainda está sendo desenvolvida. Volte em breve para novidades!")

EmManutencao()


# # Nome do arquivo e diretório onde será salvo
# caminho_relativo = categorias
# # st.write(caminho_relativo)
# caminho_completo = os.path.abspath(caminho_relativo)  # Obtém o caminho absoluto
# # st.write(caminho_completo)

# # Lendo o arquivo JSON
# with open(categorias, "r", encoding="utf-8") as arquivo:    
#     categoriasDict = json.load(arquivo)  # Carrega o conteúdo JSON para um dicionário

# def pag_debito():
#     # Lê a planilha CSV (verifica se existe)
#     try:
#         sheet = pd.read_csv(caminho_data, sep=";", encoding="utf-8")
#     except FileNotFoundError:
#         st.write('Erro as')

#     # Título do aplicativo
#     st.title("📋 Informações de Gastos")

#     # Criando duas colunas
#     col1, col2 = st.columns(2)
#     with col1:
#         data = st.date_input("Data do gasto:")
#         categoria = st.selectbox("Qual categoria:", categoriasDict.keys())
#         divide = st.radio("Divide?", ["Sim", "Não"])
        
#     with col2:
#         subcategoria = st.selectbox("Subcategoria:", categoriasDict[categoria])
#         valor = st.number_input("Valor (R$):")
#         saidaEntrada = st.radio("Saída ou Entrada?", ["Entrada", "Saída"])

#     # Botão para adicionar dados
#     if st.button("Adicionar gasto"):
#         if data and categoria and subcategoria and divide and valor:
#             if divide == "Sim":
#                 valor = valor / 2
#             if saidaEntrada == "Saída":
#                 valor = valor * -1

#             # Criando DataFrame com a nova linha
#             dadoNovo = pd.DataFrame([[data.strftime("%Y-%m-%d"), categoria, subcategoria, divide, valor]], columns=sheet.columns)
#             dadoNovo.to_csv(caminho_data, sep=";", mode="a", header=False, index=False, encoding="utf-8")

#             st.success("✅ Dados adicionados e arquivo atualizado com sucesso!")
#         else:
#             st.error("⚠️ Preencha todos os campos antes de enviar!")

#     # Exibir os dados atuais
#     st.subheader("📊 Dados na Planilha:")
#     st.dataframe(sheet.sort_values(by="data", ascending=False))
#     return st.dataframe(sheet)