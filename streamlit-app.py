import streamlit as st
import numpy as np
import pandas as pd
import polars as pl
import altair as alt

st.title("OHTANI-SAN 2021")

#### read data
base = pd.read_csv("data/Ohtani2021.csv")
base["pfx_x"] = base["pfx_x"]*30.48
base["pfx_z"] = base["pfx_z"]*30.48
base = pl.from_pandas(base)

#### sidebar part
ss = st.sidebar
ss.header("Setting")
pitch_type = ss.selectbox("Pitch Type", ["4-Seam Fastball","Cutter","Slider",
                    "Curveball","Split-Finger"])


#### sidebar part
dat = base.filter(pl.col("pitch_name")==pitch_type)

col1, col2, col3, col4 = st.columns(4)
col1.header("Pitch  Speed")
release_speed = np.nanmean(dat["release_speed"]*1.609).round(1)
col1.subheader(f"`{release_speed} km/h`")

col2.header("Spin  Rate")
release_spin_rate = int(np.nanmean(dat["release_spin_rate"]))
col2.subheader(f"`{release_spin_rate} rpm`")

col3.header("Horizontal  Break")
pfx_x = np.nanmean(dat["pfx_x"]).round(1)
col3.subheader(f"`{pfx_x} cm`")

col4.header("Vertical  Break")
pfx_z = np.nanmean(dat["pfx_z"]).round(1)
col4.subheader(f"`{pfx_z} cm`")

st.write("\n\n")

st.header("Plot")
scatter = alt.Chart(base.to_pandas()).mark_circle().encode(
    x='pfx_x', y='pfx_z', color="pitch_name"
  ).interactive()
st.altair_chart(scatter, use_container_width=True)

