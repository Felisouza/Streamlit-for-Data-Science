import streamlit as st
import pandas as pd
from datetime import datetime

# Função para salvar dados em um arquivo CSV
def salvar_no_csv(data):
    try:
        # Tenta ler o CSV existente para adicionar os dados
        df = pd.read_csv("dados_financeiros.csv").drop_duplicates()
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    except FileNotFoundError:
        # Cria um CSV novo se não existir
        df = pd.DataFrame([data])
        df = df.drop_duplicates()

    df.to_csv("dados_financeiros.csv", index=False)

# Função para exibir o formulário financeiro
def formulario():
    st.title("Formulário Financeiro")

    # Criando o formulário com Streamlit
    with st.form(key="formulario_financeiro"):
        data_da_compra = st.date_input("Data da compra", value=datetime.now())
        valor_da_compra = st.number_input("Valor da compra", min_value=0.0, format="%.2f")
        nome_do_estabelecimento = st.text_input("Nome do estabelecimento")
        tipo_de_compra = st.selectbox(
            "Tipo de compra",
            options=["Comida fora", "Mercado", "Gás", "Luz", "Internet", "Gatos"],
        )

        submit_button = st.form_submit_button(label="Salvar informações")

    # Verifica se o botão foi clicado
    if submit_button:
        # Cria um dicionário com as informações preenchidas
        data = {
            "Data da Compra": data_da_compra,
            "Valor da Compra": valor_da_compra,
            "Nome do Estabelecimento": nome_do_estabelecimento,
            "Tipo de Compra": tipo_de_compra,
        }

        # Salva os dados no CSV
        salvar_no_csv(data)

        st.success("Informações salvas com sucesso!")

    # Mostra os dados já registrados, se quiser visualizar
    try:
        df_existente = pd.read_csv("dados_financeiros.csv")
        st.write("Dados já registrados:")
        st.dataframe(df_existente)
    except FileNotFoundError:
        st.write("Nenhum dado encontrado ainda.")