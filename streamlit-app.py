import streamlit as st
import pandas as pd
import numpy as np

st.title("MLB Player Data")

#### read data
#ydat = pd.read_csv("data/")

#### sidebar part
ss = st.sidebar
ss.write("test")
ss.selectbox("Select Pitcher:", ["Shohei Ohtani","Yu Darvish"])


#### sidebar part

st.selectbox("球種", ["Four-Seam","slider"])

st.write("球速")

st.write("回転数")

st.write("回転軸")

st.write("変化量")

st.write("変化量プロット")

