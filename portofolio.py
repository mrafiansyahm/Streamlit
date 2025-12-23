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

with tab1:
    import about
    about.about_dataset()
with tab2:
    import visualisasi
    visualisasi.chart()
with tab3:
    import machine_learning
    machine_learning.ml_model()
with tab4:
    import prediction
    prediciton.prediction_app()

def about_dataset():
    st.write("**Tentang Dataset**")
