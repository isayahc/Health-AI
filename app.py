"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import smiles_to_2d 


def main():

    st.title("Drug Research and Discovery")

    compound = 0
    weight = 0
    toxicity = 0
    #data: compound {weight = 0, toxicity = 0}
    st.subheader('Compound Name')
    st.write(compound)




    test_compound = st.text_input("Enter the Test Compound")

    # Text Input Component 


    # Get the input type from the user (SMILES or Molecular Formula)
    input_type = st.radio("Input Type", ("SMILES", "Molecular Formula"))

    # Get the input from the user based on the selected type
    if input_type == "SMILES":
        input_value = st.text_input("Enter the SMILES string", "CCO")
    else:
        input_value = st.text_input("Enter the Molecular Formula", "C2H6O")

    # Generate and display the molecule image
    smiles_to_2d.generate_molecule_image(input_value, input_type)


