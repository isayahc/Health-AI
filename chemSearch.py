from rdkit import Chem
from rdkit.Chem import Descriptors

def chemSearch(input):
    smiles = input
    molecule = Chem.MolFromSmiles(smiles)

    molecular_weight = Descriptors.ExactMolWt(molecule)
    polar_surface_area = Descriptors.TPSA(molecule)
    logP = Descriptors.MolLogP(molecule)

    description = f"Molecular weight: {molecular_weight}\n"
    description += f"Polar surface area: {polar_surface_area}\n"
    description += f"logP: {logP}"

    return description

