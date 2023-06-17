import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
import imageio
import os

# Get the SMILES string from the user
smiles = st.text_input("Enter the SMILES string", "CCO")

# Create an RDKit molecule object from the SMILES string
mol = Chem.MolFromSmiles(smiles)

if mol is not None:
    # Draw the 2D structure
    img = Draw.MolToImage(mol)

    # Save the image to a file in the "./assets" directory
    img_path = os.path.join("assets", "output.png")
    img.save(img_path)

    # Create a GIF from the image
    gif_path = os.path.join("assets", "output.gif")
    images = [imageio.imread(img_path) for _ in range(10)]  # repeat the image 10 times in the GIF
    imageio.mimsave(gif_path, images)

    # Display the GIF in Streamlit
    st.image(gif_path)
else:
    st.write("Invalid SMILES string")
