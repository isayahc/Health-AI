import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
import imageio

# Define the SMILES string
smiles = "CCO"

# Create an RDKit molecule object from the SMILES string
mol = Chem.MolFromSmiles(smiles)

# Draw the 2D structure
img = Draw.MolToImage(mol)

# Save the image to a file
img.save("output.png")

# Create a GIF from the image
images = [imageio.imread("output.png") for _ in range(10)]  # repeat the image 10 times in the GIF
imageio.mimsave('output.gif', images)

# Display the GIF in Streamlit
st.image('output.gif')
