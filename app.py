"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd


st.title("Toxicity of Test Compounds")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df


test_compound = st.text_input("Enter the Test Compound")

# Text Input Component 


