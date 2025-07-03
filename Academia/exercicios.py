import streamlit as st
import sys
import os

# Importanto página de crédito
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'temporizador.py')))
try:
    from temporizador import temporizador  # Importando função de Crédito
except ModuleNotFoundError:
    st.error("Erro: O arquivo ")

# Configuração da página
st.set_page_config(page_title="Lista com Temporizador", layout="wide")

# Lista de itens e subitens
itens = {
    "Tarefa 1": ["Passo 1", "Passo 2", "Passo 3"],
    "Tarefa 2": ["Passo A", "Passo B", "Passo C"],
    "Tarefa 3": ["Etapa X", "Etapa Y", "Etapa Z"]
}

# Estado inicial no session_state
if "item_atual" not in st.session_state:
    st.session_state.item_atual = list(itens.keys())[0]  # Primeiro item da lista
    st.session_state.subitem_atual = 0  # Primeiro subitem

st.title("📋 Lista com Temporizador")

# Selecionar item principal
item_selecionado = st.selectbox("Escolha um item:", list(itens.keys()), index=list(itens.keys()).index(st.session_state.item_atual))

# Atualiza o item atual no session_state
st.session_state.item_atual = item_selecionado

# Exibe o subitem atual
subitens = itens[item_selecionado]
st.write(f"🔹 Subitem atual: {subitens[st.session_state.subitem_atual]}")

import streamlit as st
import time

if st.button("Avançar"):
    with st.empty():
        for t in range(3, 0, -1):
            st.write(f"⏳ Tempo restante: {t} segundos")
            time.sleep(1)  # Pausa de 1 segundo

    st.write("⏰ Tempo finalizado!")

    # Adicionando um áudio ao final
    st.markdown(
        """
        <audio autoplay>
            <source src="https://www.soundjay.com/human/sounds/applause-01.mp3" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )


    # Avança para o próximo subitem
    if st.session_state.subitem_atual < len(subitens) - 1:
        st.session_state.subitem_atual += 1
    else:
        st.session_state.subitem_atual = 0  # Reinicia se chegar ao último subitem







