import streamlit as st
import pandas as pd
from uploadArquivoCredito import uploadFile
from LimpaDados import LimpaDados
from botoes import listaGastos, botaoDatas

def paginaCredito():
    # Configuração da página
    
    # Título principal
    st.title("📊 Controle Financeiro - Crédito")

    # Resumo financeiro
    st.subheader("Resumo Financeiro")
    saldo_total = 5000.00  # Exemplo de saldo disponível
    credito_disponivel = 10000.00
    gasto_mes = 2500.00

    # Exibição de métricas
    col1, col2, col3 = st.columns(3)
    col1.metric(label="💰 Saldo Atual", value=f"R$ {saldo_total:.2f}")
    col2.metric(label="🏦 Crédito Disponível", value=f"R$ {credito_disponivel:.2f}")
    col3.metric(label="📉 Gastos no Mês", value=f"R$ {gasto_mes:.2f}")

    # Inserir nova fatura
    arquivo = uploadFile()

    # Limpa os dados
    df = LimpaDados(df=arquivo)
    
    botaoDatas()
    listaGastos(df=df)


    # Simulação de gastos
    st.subheader("Histórico de Movimentações")
    st.dataframe(df)



# Executar a função
if __name__ == "__main__":
    paginaCredito()