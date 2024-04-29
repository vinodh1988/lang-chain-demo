from langchain_openai import ChatOpenAI,OpenAI
from dotenv import load_dotenv
from langchain.schema import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import GoogleGenerativeAI
import os 
load_dotenv()
llm=OpenAI()
llm2= GoogleGenerativeAI(model="models/gemini-pro",google_api_key=os.environ['GOOGLE_KEY'])


messages=[
  SystemMessage(content="""You are an Assistant thar resolves 
                   queries related To ABC Courses org"""),
  HumanMessage(content="""What courses do you support?"""),
  AIMessage(content=""" We support  only three courses Machine Learning, Prompt Engineering '
            and Data Engineering"""),
  HumanMessage(content="""do you support HTML and CSS?"""),            
              
]

result=llm.invoke(messages)
print(result)
result2=llm2.invoke(messages)
print(result2)


