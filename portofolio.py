import pandas as pd
import numpy as np
import streamlit as st

st.header("Stroke Risk Analysis and Prediction")
st.write("Pelatihan Data Science Batch 1 - Dibimbing")
st.write("Jakarta, 23 Desember 2025")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["About Dataset",
                                       "Dashboards",
                                       "Machine Learning",
                                       "Prediction App",
                                       "Contact Me"])

df = pd.read_csv("healthcare-dataset-stroke-data.csv")