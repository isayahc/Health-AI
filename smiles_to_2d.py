import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
import imageio
import os
from typing import Union

def generate_molecule_image(input_value: Union[str, int], input_type: str) -> None:
    """
    Generate and display the molecule image based on the input value and type.

    Args:
        input_value (Union[str, int]): The input value, either the SMILES string or Molecular Formula.
        input_type (str): The type of input, either 'SMILES' or 'Molecular Formula'.
    """
    # Create an RDKit molecule object from the input value
    mol = None
    if input_type == "SMILES":
        mol = Chem.MolFromSmiles(input_value)
    elif input_type == "Molecular Formula":
        mol = Chem.MolFromSmarts(input_value)

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
        st.write("Invalid input")


def main():
    # Get the input type from the user (SMILES or Molecular Formula)
    input_type = st.radio("Input Type", ("SMILES", "Molecular Formula"))

    # Get the input from the user based on the selected type
    if input_type == "SMILES":
        input_value = st.text_input("Enter the SMILES string", "CCO")
    else:
        input_value = st.text_input("Enter the Molecular Formula", "C2H6O")

    # Generate and display the molecule image
    generate_molecule_image(input_value, input_type)


if __name__ == "__main__":
    main()
