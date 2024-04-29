from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# THis example works based on env variable fed in .env file
llm=OpenAI()
print(llm.invoke("just give me a quote"))