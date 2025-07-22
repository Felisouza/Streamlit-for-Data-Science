# %%
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

# %%
df_modelo = pd.read_csv(
    r'C:\Users\feh_s\Desktop\Faturas\2025faturas.csv', sep=',', decimal='.', encoding='latin1')
df_modelo.head()

# %%
# 🔁 Codifica variáveis nominais (string → número)
encoder_Nome = LabelEncoder()
encoder_tipo = LabelEncoder()

# %%
df_modelo['Nm_Encoded'] = encoder_Nome.fit_transform(df_modelo['NmGasto'])
df_modelo['Tipo_Encoded'] = encoder_tipo.fit_transform(df_modelo['Tipo'])
df_modelo.head()

# %%
# Pipeline: Vetorização de texto + Random Forest
model = Pipeline([
    ('vectorizer', CountVectorizer(analyzer='char', ngram_range=(1, 8))),  # Captura padrões como "Spfc"
    ('classifier', RandomForestClassifier(
        max_depth=7, max_features=10, min_samples_leaf=1, n_estimators=1000))
])



# %%
X = df_modelo[['NmGasto']]
y = df_modelo['Tipo_Encoded']

model.fit(df_modelo['NmGasto'], df_modelo['Tipo'])
# %%

modelo = RandomForestClassifier(
    max_depth=7, max_features=10, min_samples_leaf=1, n_estimators=1000
)
modelo.fit(X, y)
# %%
df = pd.read_excel(r'C:\Users\feh_s\Desktop\Faturas\2025\Fatura-Excel-202506.xls')
df = df.loc[
    (df['Logotipo Itaú'].notna())
    &  (pd.to_numeric(df['Unnamed: 3'], errors='coerce').notna())
    & (df['Unnamed: 1'].notna())
]

df.drop(df.index[0], inplace=True)

# %%


# %%
X_ = df['Unnamed: 1']
df['predicao'] =  model.predict(X_)
# %%
    df['Nm_Encoded'] = encoder.fit_transform(df['NmGasto'])

    df['Previsao'] = modelo.predict(df[['Nm_Encoded']])
    df['Previsao'] = encoder_tipo.inverse_transform(df['Previsao'])


    st.write(df[['Nm_Encoded', 'NmGasto']].sort_values(by='Nm_Encoded', ascending=True).groupby('Nm_Encoded').max())
    st.write(df_modelo[['Nm_Encoded', 'NmGasto']].sort_values(by='Nm_Encoded', ascending=True).groupby('Nm_Encoded').max())


    # st.write("🎯 Acurácia:", accuracy_score(y_test, y_pred))
    st.dataframe(df)




else:
    st.info("🔍 Aguardando envio do arquivo...")










