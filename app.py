"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import smiles_to_2d

st.title("Drug Research and Discovery")

compound = 0
weight = 0
toxicity = 0
#data: compound {weight = 0, toxicity = 0}
st.subheader('Compound Name')
st.write(compound)




test_compound = st.text_input("Enter the Test Compound")

# Text Input Component 


