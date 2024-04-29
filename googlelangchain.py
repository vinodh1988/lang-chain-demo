from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
llm= GoogleGenerativeAI(model="models/gemini-pro",google_api_key=os.environ['GOOGLE_KEY'])
response=llm.invoke("Give me  quotes by EINSTIEN and Gandhi")
print(response)
