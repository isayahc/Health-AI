import streamlit as st
import pandas as pd
import smiles_to_2d 

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory

def main():
    st.title("Drug Research and Discovery")

    # Fields to enter API keys
    serp_api_key = st.text_input("Enter SerpAPI key", type="password")
    chat_openai_key = st.text_input("Enter ChatOpenAI key", type="password")

    # Create a SerpAPIWrapper and ChatOpenAI instances with provided keys
    search = SerpAPIWrapper(api_key=serp_api_key)
    llm = ChatOpenAI(api_key=chat_openai_key, temperature=0)

    # Initialize a ConversationBufferMemory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Initialize the agent chain
    tools = [
        Tool(name="Search", func=search.run, 
            description="Useful when you want to answer questions about current events or things found online")
    ]
    agent_chain = initialize_agent(tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)

    # Get the input from the user
    user_input = st.text_input("Enter your message")

    # Run the agent chain and get the AI's response
    ai_response = agent_chain.run(input=user_input)

    # Display the AI's response
    st.text("AI: " + ai_response)

    # Get the input type from the user (SMILES or Molecular Formula)
    input_type = st.radio("Input Type", ("SMILES", "Molecular Formula"))

    # Get the input from the user based on the selected type
    if input_type == "SMILES":
        input_value = st.text_input("Enter the SMILES string", "CCO")
    else:
        input_value = st.text_input("Enter the Molecular Formula", "C2H6O")

    # Generate and display the molecule image
    smiles_to_2d.generate_molecule_image(input_value, input_type)

if __name__ == "__main__":
    main()
