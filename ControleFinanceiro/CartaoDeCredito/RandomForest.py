import streamlit as st
import pandas as pd
import sys
import os
import requests
from streamlit_plotly_events import plotly_events
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

caminho_atual = os.getcwd()

caminho_modelo = os.path.abspath(os.path.join(caminho_atual, 'modelos')) + "\RandomForest.pkl"


# Adiciona o caminho do diretório onde está o módulo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'CartaoDeCredito')))
from uploadArquivoCredito import uploadFile
from LimpaDados import LimpaDados

# Adiciona o caminho do Utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))


df_modelo = pd.read_csv(r'C:\Users\feh_s\Desktop\Faturas\2025faturas.csv', sep=',', decimal='.', encoding='latin1')

model = Pipeline([
    ('vectorizer', CountVectorizer(analyzer='char', ngram_range=(1, 8))),  # Captura padrões como "Spfc"
    ('classifier', RandomForestClassifier(
        max_depth=7, max_features=10, min_samples_leaf=1, n_estimators=1000))
])

model.fit(df_modelo['NmGasto'], df_modelo['Tipo'])

try:
    with open(caminho_modelo, 'wb') as arquivo:
        pickle.dump(model, arquivo)
    print('Modelo carregado com sucesso!')
except Exception as e:
    print(e)


    # 🔀 Divisão em treino e teste
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # modelo = XGBClassifier(objective='multi:softmax', num_class=len(encoder_tipo.classes_), use_label_encoder=False,
    #                        eval_metric='mlogloss')



