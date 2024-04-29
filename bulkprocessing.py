from langchain_openai import ChatOpenAI,OpenAI
from dotenv import load_dotenv
from langchain.schema import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import GoogleGenerativeAI
import os 
load_dotenv()

llm=ChatOpenAI()

batch_messages = [
[   
    SystemMessage(content="""You are assistant that provide quotes on the request topics"""),
    HumanMessage(content="Belief")
],
[
    SystemMessage(content=""" You list out the books in a given topic"""),
    HumanMessage(content="Belief")
]
]

batch_result=llm.generate(batch_messages)
#print(batch_result)
print("Quotes\n--------------------------------------------------------")
print(batch_result.generations[0][0].text)
print("Books\n--------------------------------------------------------")
print(batch_result.generations[1][0].text)