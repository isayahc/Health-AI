from rdkit import Chem
from rdkit.Chem import Descriptors

# Let's consider Aspirin for our analysis
smiles = 'CC(=O)OC1=CC=CC=C1C(=O)O'
molecule = Chem.MolFromSmiles(smiles)

molecular_weight = Descriptors.ExactMolWt(molecule)
polar_surface_area = Descriptors.TPSA(molecule)
logP = Descriptors.MolLogP(molecule)

print(f'Molecular weight: {molecular_weight}')
print(f'Polar Surface Area: {polar_surface_area}')
print(f'LogP: {logP}')
