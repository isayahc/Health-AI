import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem

# Define the SMILES string
smiles = "CCO"

# Create an RDKit molecule object from the SMILES string
mol = Chem.MolFromSmiles(smiles)

# Generate the 3D coordinates
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol)
AllChem.UFFOptimizeMolecule(mol)

# Save the 3D structure to a file in PDB format
Chem.MolToPDBFile(mol, "output.pdb")
