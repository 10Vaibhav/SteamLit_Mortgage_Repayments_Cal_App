import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World!")
x = st.text_input("Favourite Movie?")
st.write(f"Your Favourite Movie is : {x}")

data = pd.read_csv("movies.csv")
st.write(data)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.write("Bar Chart")
st.bar_chart(chart_data)

st.write("Line Chart")
st.line_chart(chart_data)
