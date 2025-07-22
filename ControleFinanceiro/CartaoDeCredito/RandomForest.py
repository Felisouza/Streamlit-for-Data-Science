import streamlit as st
import pickle
import os


import streamlit as st
import pandas as pd
import sys
import os
import requests
import streamlit as st
from streamlit_plotly_events import plotly_events
from sklearn.preprocessing import LabelEncoder
from  sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os
import sys
from xgboost import XGBClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Adiciona o caminho do diretório onde está o módulo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'CartaoDeCredito')))
from uploadArquivoCredito import uploadFile
from LimpaDados import LimpaDados

# Adiciona o caminho do Utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))


from st_aggrid import AgGrid

# Inserir nova fatura
arquivo = uploadFile()

# Processamento do arquivo
if arquivo is not None:
    df = LimpaDados(arquivo)
    df_modelo = pd.read_csv(r'C:\Users\feh_s\Desktop\Faturas\2025faturas.csv', sep=',', decimal='.', encoding='latin1')
    # 🔁 Codifica variáveis nominais (string → número)
    encoder_Nome = LabelEncoder()
    encoder_tipo = LabelEncoder()

    df_modelo['Nm_Encoded'] = encoder_Nome.fit_transform(df_modelo['NmGasto'])

    with open('modelos/encoder_nmgasto.pkl', 'wb') as f:
        pickle.dump(encoder_Nome, f)

    df_modelo['Tipo_Encoded'] = encoder_tipo.fit_transform(df_modelo['Tipo'])

    # 🔎 Separando variáveis preditoras e alvo
    X = df_modelo[['Nm_Encoded']]
    y = df_modelo['Tipo_Encoded']

    # 🔀 Divisão em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    # 🌳 Modelo Random Forest
    modelo = RandomForestClassifier(
        max_depth=7, max_features=10, min_samples_leaf=1, n_estimators=1000
    )

    # modelo = XGBClassifier(objective='multi:softmax', num_class=len(encoder_tipo.classes_), use_label_encoder=False,
    #                        eval_metric='mlogloss')

    modelo.fit(X, y)

    # 🔍 Previsões e avaliação
    # 🔮 Faz previsões no conjunto original (ou em outro)

    # 🔎 Separando variáveis preditoras e alvo
    with open('modelos/encoder_nmgasto.pkl', 'rb') as f:
        encoder = pickle.load(f)
    categorias_validas = set(encoder.classes_)
    df = df[df['NmGasto'].isin(categorias_validas)]
    df['Nm_Encoded'] = encoder.transform(df['NmGasto'])

    df['Nm_Encoded'] = encoder.fit_transform(df['NmGasto'])

    df['Previsao'] = modelo.predict(df[['Nm_Encoded']])
    df['Previsao'] = encoder_tipo.inverse_transform(df['Previsao'])


    st.write(df[['Nm_Encoded', 'NmGasto']].sort_values(by='Nm_Encoded', ascending=True).groupby('Nm_Encoded').max())
    st.write(df_modelo[['Nm_Encoded', 'NmGasto']].sort_values(by='Nm_Encoded', ascending=True).groupby('Nm_Encoded').max())


    # st.write("🎯 Acurácia:", accuracy_score(y_test, y_pred))
    st.dataframe(df)




else:
    st.info("🔍 Aguardando envio do arquivo...")










