from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory
import chemSearch

tools = [
    Tool(
        name="Chemical Search",
        func=chemSearch.chemSearch,
        description="Useful when you want information about a chemical"
    ),
]

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)
agent_chain = initialize_agent(
    tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)

while True:
    print("AI: " + agent_chain.run(input=input("Human: ")))


# input output documentation 
# Human: What can you tell me about this chemical: CC(=O)OC1=CC=CC=C1C(=O)O
# > Entering new AgentExecutor chain...
# {
#     "action": "Chemical Search",
#     "action_input": "CC(=O)OC1=CC=CC=C1C(=O)O"
# }
# Observation: This chemical has these properties: Molecular weight: 180.042258736, Polar Surface Area: 63.60000000000001, LogP: 1.3101
# Thought: {
#     "action": "Final Answer",
#     "action_input": "The chemical CC(=O)OC1=CC=CC=C1C(=O)O has a molecular weight of 180.042258736, a polar surface area of 63.60000000000001, and a LogP of 1.3101."
# }

# > Finished chain.
# AI: The chemical CC(=O)OC1 = CC = CC = C1C(=O)O has a molecular weight of 180.042258736, a polar surface area of 63.60000000000001, and a LogP of 1.3101.
# Human:
