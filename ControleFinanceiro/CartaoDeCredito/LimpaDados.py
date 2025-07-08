#!/usr/bin/env python
# coding: utf-8

# # Libs

# In[1]:


import pandas as pd
import streamlit as st

def LimpaDados(df):
    if df == None:
        st.write('estou aqui')
        df = pd.DataFrame()
    else:
        st.write(df)
        df.drop(columns='Unnamed: 2', inplace=True)
        df.head()
        


        # ## Renomeia colunas

        # In[4]:


        NomesColunas = {
            0:'Data'
            , 1: 'NmGasto'
            , 2: 'Valor'
        }

        df.columns = [NomesColunas[i] if i in NomesColunas else df.columns[i] for i in range(len(df.columns))]
        df.head()


        # ## Retirando NaN

        # In[5]:


        df_SemNulo = df[(~df['Valor'].isnull()) & (~df['Data'].isnull())].reset_index(drop=True)


        # In[7]:


        df_SemNulo[df_SemNulo['Valor'].isnull()]
        # print(df_SemNulo)
        


        # ## Selecionando os valores verdadeiros

        # ## Limpa data

        # In[9]:


        # Expressão regular para encontrar datas no formato dd/mm/yyyy
        padrao_data = r"^\d{2}/\d{2}/\d{4}$"

        # Filtrar linhas com datas no formato certo
        filtro = df_SemNulo["Data"].astype(str).str.match(padrao_data)
        df_Union = df_SemNulo[filtro].reset_index(drop=True)

        # df_Union.head()


        # ## Retira total

        


        # df_Union['Valor'].sum()


        # # Check base

        # In[16]:


        # df_Union.info()


        # In[19]:


        # df_Union.describe()

        # print("Estou aqui Agora"*100)
        return df_Union