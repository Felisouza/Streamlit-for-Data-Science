# Libs
# add streamlit lottie
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events
import os
import requests
import streamlit as st

def load_lottieUrl(url: str):
    r = requests.get(url)
    print(r.status_code, "-"*100)
    if r.status_code == 200:
        return r.json()
    else:
        return None