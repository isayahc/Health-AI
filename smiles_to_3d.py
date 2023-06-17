import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw
import imageio
import os
import glob

# Define the SMILES string
smiles = "CCO"

# Create an RDKit molecule object from the SMILES string
mol = Chem.MolFromSmiles(smiles)

# Generate the 3D coordinates
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol)
AllChem.MMFFOptimizeMolecule(mol)

# Get atom coordinates
conf = mol.GetConformer()
atom_coords = [conf.GetAtomPosition(i) for i in range(mol.GetNumAtoms())]

# Get x, y, and z coordinates
x = [coord.x for coord in atom_coords]
y = [coord.y for coord in atom_coords]
z = [coord.z for coord in atom_coords]

# Create directory for temporary images
os.makedirs("images", exist_ok=True)

# Create temporary images for GIF
for angle in range(0, 360, 2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.view_init(30, angle)
    plt.savefig(f"images/temp{angle}.png")
    plt.close()

# Create GIF
images = []
for file_name in sorted(glob.glob("images/*.png")):
    images.append(imageio.imread(file_name))
imageio.mimsave('movie.gif', images)

# Display the GIF using Streamlit
st.image('movie.gif')

# Delete temporary images
for file_name in glob.glob("images/*.png"):
    os.remove(file_name)
