import pandas as pd
import plotly.express as px
import requests
import streamlit as st

# add streamlit lottie
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events

def load_lottieurl(url: str):
    r = requests.get(url)
    print(r.status_code, "-"*100)
    if r.status_code == 200:
        return r.json()
    else:
        return None


url = "https://lottie.host/e7600393-46e8-456a-92a6-18b011c08889/ZK9eOLek7G.json"
# lottie_penguin = load_lottieurl( "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json" )
lottie = load_lottieurl(url)
st_lottie(lottie, height=200)

st.title("Streamlit Plotly Events + Lottie Example: Penguins")

