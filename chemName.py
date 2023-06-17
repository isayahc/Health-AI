import pubchempy

def chemName(input):
    smiles = input
    compounds = pubchempy.get_compounds(smiles, namespace='smiles')
    match = compounds[0]
    return match.iupac_name
