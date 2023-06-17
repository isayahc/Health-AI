from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
text = input("What can you tell me about this: ")

print(llm(text))


# llm = OpenAI(temperature=0.9)
# text = input("What can you tell me about this: ")

# print(llm(text))
# with "Benzene" input, output is Benzene is a versatile chemical compound used as a raw material in the production of numerous products. 
# These products include plastics, nylon, polystyrene, detergents, fragrances, dyes, drugs, explosives, and rubber. Benzene is also used 
# as a solvent for fats, oils, waxes, resins, and rubber. It is also used to produce a number of other industrial chemicals including 
# styrene, toluene, xylene, and cumene. Other products created from benzene include lubricants, gasoline, and solvents used in the printing industry.
