import streamlit as st
import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem

def visualize_3d_structure(smiles):
    # Create an RDKit molecule object from the SMILES string
    mol = Chem.MolFromSmiles(smiles)

    # Generate the 3D coordinates
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.UFFOptimizeMolecule(mol)

    # Read the 3D coordinates from the molecule
    coords = mol.GetConformer().GetPositions()

    # Create a py3Dmol view
    view = py3Dmol.view(width=600, height=400)
    view.addModel(Chem.MolToMolBlock(mol), "mol")
    view.setStyle({"stick": {}})
    view.zoomTo()

    try:
        # Render the py3Dmol view in Streamlit as HTML
        html = view.render()
        st.components.v1.html(html, width=600, height=400)
    except TypeError:
        st.write(html)

# Streamlit app code
def main():
    st.title("3D Structure Visualization")

    # Get the SMILES input from the user
    smiles_input = st.text_input("Enter the SMILES string")

    if smiles_input:
        # Call the visualization function with the user input
        visualize_3d_structure(smiles_input)

if __name__ == "__main__":
    main()
