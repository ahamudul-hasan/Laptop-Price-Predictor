import streamlit as st
import pickle

# import the model
pipe = pickle.load(open('../Models/pipe.pkl', 'rb'))
df = pickle.load(open('../Models/df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Brand
company = st.selectbox('Brand', df['Company'].unique())

# Type of laptop
type = st.selectbox('Type', df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight