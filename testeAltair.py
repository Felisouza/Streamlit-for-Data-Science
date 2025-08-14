import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Gráficos com Altair", layout="centered")
st.title("📊 Visualização com Altair")

# Dados simulados para gráfico de barras
bar_data = pd.DataFrame({
    'Produto': ['A', 'B', 'C', 'D'],
    'Vendas': [120, 340, 230, 150]
})

# Gráfico de barras
bar_chart = alt.Chart(bar_data).mark_bar(color='steelblue').encode(
    x='Produto',
    y='Vendas'
).properties(
    title='Vendas por Produto',
    width=500,
    height=300
)

st.altair_chart(bar_chart, use_container_width=True)

# Dados simulados para gráfico de linhas
line_data = pd.DataFrame({
    'Data': pd.date_range(start='2023-01-01', periods=6, freq='M'),
    'Vendas': [100, 150, 200, 180, 220, 260]
})

# Gráfico de linhas
line_chart = alt.Chart(line_data).mark_line(point=True, color='orange').encode(
    x='Data',
    y='Vendas'
).properties(
    title='Evolução das Vendas Mensais',
    width=500,
    height=300
)

st.altair_chart(line_chart, use_container_width=True)