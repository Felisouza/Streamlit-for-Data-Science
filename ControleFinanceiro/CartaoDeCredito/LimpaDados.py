#!/usr/bin/env python
# coding: utf-8

# # Libs
import pandas as pd
import streamlit as st
import re

# Função REGEX
def limparNmGasto(col):
    # Se terminar com caracteres não alfabéticos, remove-os do final
    return re.sub(r'[^a-zA-ZÀ-ÿ\s]+$', '', col)


#Função principal de limpeza dos dados
def LimpaDados(df):
        df.drop(columns='Unnamed: 2', inplace=True)

        # ## Renomeia colunas
        NomesColunas = {
            0:'Data'
            , 1: 'NmGasto'
            , 2: 'Valor'
        }

        df.columns = [NomesColunas[i] if i in NomesColunas else df.columns[i] for i in range(len(df.columns))]
        df.head()


        # ## Retirando NaN
        df_SemNulo = df[(~df['Valor'].isnull()) & (~df['Data'].isnull())].reset_index(drop=True)

        df_SemNulo[df_SemNulo['Valor'].isnull()]

        # ## Selecionando os valores verdadeiros

        # ## Limpa data
        # Expressão regular para encontrar datas no formato dd/mm/yyyy
        padrao_data = r"^\d{2}/\d{2}/\d{4}$"

        # Filtrar linhas com datas no formato certo
        filtro = df_SemNulo["Data"].astype(str).str.match(padrao_data)
        df_Union = df_SemNulo[filtro].reset_index(drop=True)

        # Aplica a função à coluna
        df_Union['NmGasto'] = df_Union['NmGasto'].apply(limparNmGasto)

        return df_Union