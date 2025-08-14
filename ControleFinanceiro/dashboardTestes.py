
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from dash import Dash, html
import dash_bootstrap_components as dbc


df = pd.read_csv(r'C:\Users\feh_s\Desktop\Faturas\2025faturas.csv', sep=',', decimal='.', encoding='latin1')
st.dataframe(df.head())

st.markdown("<h1 style='text-align: center;'>Dashboard cartão de crédito</h1>", unsafe_allow_html=True)
alt.themes.enable("dark")

with st.sidebar:
    date_list = list(df['DataDaFatura'].unique())[::-1]
    date_list.append('Todos')

    selected_year = st.selectbox('Selecione uma data', date_list, index=len(date_list) - 1)
    if selected_year != 'Todos':
        df_dash = df[df['DataDaFatura'] == selected_year]
    else:
        df_dash = df
st.write(df_dash)
# "*********************************************************************************************"

import streamlit as st
import streamlit.components.v1 as components

# Título da página
st.markdown("<h1 style='text-align: center;'>📊 Painel de Indicadores</h1>", unsafe_allow_html=True)

# Dados simulados
valor1 = 1250
valor2 = 87.5
valor3 = 42

# Estilo dos cards com HTML + CSS
card_style = """
    <style>
    .card-container {
        display: flex;
        justify-content: space-around;
        margin-top: 30px;
    }
    .card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        width: 25%;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .card h2 {
        font-size: 2em;
        margin: 0;
        color: #4a4a4a;
    }
    .card p {
        font-size: 1em;
        color: #888;
        margin-top: 5px;
    }
    </style>
"""

# HTML dos cards
card_html = f"""
<div class="card-container">
    <div class="card">
        <h2>{valor1}</h2>
        <p>Vendas</p>
    </div>
    <div class="card">
        <h2>{valor2}%</h2>
        <p>Taxa de Conversão</p>
    </div>
    <div class="card">
        <h2>{valor3}</h2>
        <p>Novos Clientes</p>
    </div>
</div>
"""

# Renderizar estilo + cards
st.markdown(card_style, unsafe_allow_html=True)
st.markdown(card_html, unsafe_allow_html=True)




# def calculate_population_difference(input_df, input_year):
#   selected_year_data = input_df[input_df['year'] == input_year].reset_index()
#   previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
#   selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
#   return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)
#
#
# def make_donut(input_response, input_text, input_color):
#     if input_color == 'blue':
#         chart_color = ['#29b5e8', '#155F7A']
#     if input_color == 'green':
#         chart_color = ['#27AE60', '#12783D']
#     if input_color == 'orange':
#         chart_color = ['#F39C12', '#875A12']
#     if input_color == 'red':
#         chart_color = ['#E74C3C', '#781F16']
#
#     source = pd.DataFrame({
#         "Topic": ['', input_text],
#         "% value": [100 - input_response, input_response]
#     })
#     source_bg = pd.DataFrame({
#         "Topic": ['', input_text],
#         "% value": [100, 0]
#     })
#
#     plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
#         theta="% value",
#         color=alt.Color("Topic:N",
#                         scale=alt.Scale(
#                             # domain=['A', 'B'],
#                             domain=[input_text, ''],
#                             # range=['#29b5e8', '#155F7A']),  # 31333F
#                             range=chart_color),
#                         legend=None),
#     ).properties(width=130, height=130)
#
#     text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700,
#                           fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
#     plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
#         theta="% value",
#         color=alt.Color("Topic:N",
#                         scale=alt.Scale(
#                             # domain=['A', 'B'],
#                             domain=[input_text, ''],
#                             range=chart_color),  # 31333F
#                         legend=None),
#     ).properties(width=130, height=130)
#     return plot_bg + plot + text
#
# col = st.columns((1.5, 4.5, 2), gap='medium')
#
# with col[0]:
#     st.markdown('#### Gains/Losses')
#
#     df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)
#
#     if selected_year > 2010:
#         first_state_name = df_population_difference_sorted.states.iloc[0]
#         first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
#         first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
#     else:
#         first_state_name = '-'
#         first_state_population = '-'
#         first_state_delta = ''
#     st.metric(label=first_state_name, value=first_state_population, delta=first_state_delta)
#
#     if selected_year > 2010:
#         last_state_name = df_population_difference_sorted.states.iloc[-1]
#         last_state_population = format_number(df_population_difference_sorted.population.iloc[-1])
#         last_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[-1])
#     else:
#         last_state_name = '-'
#         last_state_population = '-'
#         last_state_delta = ''
#     st.metric(label=last_state_name, value=last_state_population, delta=last_state_delta)
#
#     st.markdown('#### States Migration')
#
#     if selected_year > 2010:
#         # Filter states with population difference > 50000
#         # df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference_absolute > 50000]
#         df_greater_50000 = df_population_difference_sorted[
#             df_population_difference_sorted.population_difference > 50000]
#         df_less_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference < -50000]
#
#         # % of States with population difference > 50000
#         states_migration_greater = round(
#             (len(df_greater_50000) / df_population_difference_sorted.states.nunique()) * 100)
#         states_migration_less = round((len(df_less_50000) / df_population_difference_sorted.states.nunique()) * 100)
#         donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
#         donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')
#     else:
#         states_migration_greater = 0
#         states_migration_less = 0
#         donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
#         donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')
#
#     migrations_col = st.columns((0.2, 1, 0.2))
#     with migrations_col[1]:
#         st.write('Inbound')
#         st.altair_chart(donut_chart_greater)
#         st.write('Outbound')
#         st.altair_chart(donut_chart_less)
#
# with col[1]:
#     st.markdown('#### Total Population')
#
#     choropleth = make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme)
#     st.plotly_chart(choropleth, use_container_width=True)
#
#     heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population', selected_color_theme)
#     st.altair_chart(heatmap, use_container_width=True)
#
# with col[2]:
#     st.markdown('#### Top States')
#
#     st.dataframe(df_selected_year_sorted,
#                  column_order=("states", "population"),
#                  hide_index=True,
#                  width=None,
#                  column_config={
#                      "states": st.column_config.TextColumn(
#                          "States",
#                      ),
#                      "population": st.column_config.ProgressColumn(
#                          "Population",
#                          format="%f",
#                          min_value=0,
#                          max_value=max(df_selected_year_sorted.population),
#                      )}
#                  )
#
#     with st.expander('About', expanded=True):
#         st.write('''
#             - Data: [U.S. Census Bureau](<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html>).
#             - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
#             - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
#             ''')
