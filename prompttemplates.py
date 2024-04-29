from langchain_openai import ChatOpenAI,OpenAI
from dotenv import load_dotenv
from langchain.schema import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import GoogleGenerativeAI
import os 
from langchain.prompts.prompt import PromptTemplate

load_dotenv()

llm=ChatOpenAI()
#chain of thoughts prompting
TEMPLATE="""
You are helpful assistant that analyses input string
you analyze its category 
Format output as Json With the keys 
Category: What category the input is?
Examples: List of strings that are examples for the Category


inputstring: {input}

samples: for input apple, category is brand and other examples are Google,Samsung 
            and for apple category is chosen as brand over fruit because we priorite
            business, products and things over generic catogorization
         if we get a device or product name has animal name we categorize it to
         product only
         for input tamil, category is spoken language and other examples are hindi,telugu
         instead of giving category as language we gave spoken language because
         we want to be contextually accurate
"""

prompt=PromptTemplate.from_template(TEMPLATE)
prompt = prompt.format(input="java")

#print(prompt)
print(llm.invoke(prompt).content)
prompttemplate=PromptTemplate.from_template(TEMPLATE)
prompt = prompttemplate.format(input="For Loop")

print(prompt)
print(llm.invoke(prompt).content)

prompttemplate.save("prompt.json")
#load using  load_prompt("prompt.yaml")