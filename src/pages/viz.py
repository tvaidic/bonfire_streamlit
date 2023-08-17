import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os

filepath = os.path.join(Path(__file__).parent[1], 'data\oracle_cards.csv')
df = pd.read_csv(filepath, low_memory=False)
viz_to_use = ['scatterplot', 'histogram','bar chart']
type_viz = st.selectbox('select a visualization type:', options = viz_to_use)
if type_viz == 'histogram':
    answer = st.selectbox('select a column to viz:', options = list(df.columns))
    if answer:
        try:
            st.plotly_chart(px.histogram(df,answer))
        except BaseException:
            print('cannot visualize')