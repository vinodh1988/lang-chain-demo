from langchain.chains import LLMChain
from langchain_core.outputs import LLMResult
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

llm=ChatOpenAI()

template="""
  you are a chatbot desinged to talk about Python Coding.

  previous conversation:
  {chat_history}

  New Human Question: {question}
"""
memory = ConversationBufferMemory(memory_key="chat_history")

conversation=LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(template),
    verbose=True,
    memory=memory
)

while True:
    prompt=input()
    if prompt == "exit":
        break
 