"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import smiles_to_2d


st.title("Toxicity of Test Compounds")



test_compound = st.text_input("Enter the Test Compound")

# Text Input Component 


