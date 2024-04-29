from langchain_openai import ChatOpenAI,OpenAI
from dotenv import load_dotenv
from langchain.schema import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import GoogleGenerativeAI
import os 
from langchain.prompts.prompt import PromptTemplate
load_dotenv()
from langchain.chains import SequentialChain,LLMChain

llm=ChatOpenAI()

quote_prompt=PromptTemplate.from_template(template="""
     generate any random quote in the given topic {topic}
""")
chain_quote=LLMChain(llm=llm,prompt=quote_prompt,output_key="quote")

quote_summary=PromptTemplate.from_template(template="""
    for the quote {quote}, Share your explanation and meaning of
 it and in what context it could be used
""")
chain_summary=LLMChain(llm=llm,prompt=quote_summary,output_key="summary")

quote_words=PromptTemplate.from_template(template="""
Given the {summary}, identify the verbs, adjectives ,nouns and adverbs
used and generate a json object that lists out words in each category
                                         """)
chain_json=LLMChain(llm=llm,prompt=quote_words,output_key="quote_json")

chain_of_chains=SequentialChain(
    chains=[chain_quote,chain_summary,chain_json],
    input_variables=["topic"],
    output_variables=["quote","summary","quote_json"]
)

result=chain_of_chains.invoke({"topic":"Anger"})

print(result)