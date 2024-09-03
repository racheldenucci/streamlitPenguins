import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.header('Penguin Species Prediction')

st.subheader('Currently predicting: Palmer Penguin')

st.sidebar.header('User Input Features')
st.sidebar.markdown("""
[Example input file] (https://github.com/dataprofessor/data/blob/master/penguins_example.csv)
""")

#collect user input into dataframe
uploaded_file = st.sidebar.file_uploader('Upload CSV file', type=['csv'])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    