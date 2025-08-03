# %%
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

data = {
"states": ["Alabama", "Alaska", "Arizona", "Arkansas", "California"],
    "states_code": ["AL", "AK", "AZ", "AR", "CA"],
    "id": [1, 2, 4, 5, 6],
    "year": [2010, 2010, 2010, 2010, 2010],
    "population": [4785437, 713910, 6407172, 2921964, 37319502]

}

pd.dataF