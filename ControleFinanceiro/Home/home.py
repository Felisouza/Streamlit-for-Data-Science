import streamlit as st
import sys
import os

# Adiciona a pasta "Debito" ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Debito')))
from debito import EmManutencao

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'CartaodeCredito')))
from  paginaCredito import paginaCredito

# st.write(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'CartãodeCrédito')))




# Barra lateral com navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio("Selecione uma página", ["Home", "Cartão de Crédito", "Formulário Débito", "Upload Extrato Débito"])

#subcategoria upload de extrato

# Página principal
st.title("📊 Controle Financeiro")
st.write("Bem-vindo ao seu painel de controle financeiro!")

#Exibição dinâmica de páginas
if page == "Home":
    st.subheader("Visão Geral")
    st.write("Aqui você pode acompanhar seu saldo, investimentos e mais!")
elif page == "Cartão de Crédito":
     paginaCredito()
elif page == "Formulário Débito":
    EmManutencao()
elif page == "Upload Extrato Débito":
    EmManutencao()

    



