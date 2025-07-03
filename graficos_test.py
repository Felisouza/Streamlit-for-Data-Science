import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


perc_heads = st.number_input(
    label='Chance of Coins Landing on Heads'
    , min_value=0.0
    , max_value=1.0
    , value=.5
)

graph_title = st.text_input(label='Graph Title')
binom_dist = np.random.binomial(1, perc_heads, 10)
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 10, replace=True).mean())