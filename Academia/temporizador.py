import streamlit as st
import time

# Configuração da página
def temporizador():
    # st.set_page_config(page_title="⏳ Temporizador")

    # Título
    st.title("⏳ Temporizador")


    # Entrada do usuário para tempo em segundos
    tempo = st.number_input("Digite o tempo em segundos:", min_value=1, value=10)

    # Botão para iniciar o temporizador
    if st.button("Iniciar Temporizador"):
        with st.empty():
            for t in range(tempo, 0, -1):
                st.write(f"⏳ Tempo restante: {t} segundos")
                time.sleep(1)  # Aguarda um segundo
            st.write("⏰ Tempo finalizado!")

    # Adicionando um áudio ao final
        st.markdown(
            """
            <audio autoplay>
                <source src="https://www.soundjay.com/human/sounds/applause-01.mp3" type="audio/wav">
            </audio>
            """,
            unsafe_allow_html=True
        )
