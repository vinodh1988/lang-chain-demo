from typing import Dict, List
from uuid import UUID
from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_core.outputs import LLMResult
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from  langchain.callbacks.base import BaseCallbackHandler

llm=ChatOpenAI()

prompt_template=PromptTemplate(input_variables=["input"],
        template=" Give me a Mark down code for topic: {input}")

handler=StdOutCallbackHandler()
#chain = LLMChain(llm=llm,prompt=prompt_template,callbacks=[handler])
#print(chain.invoke(input="Basic prime number program in C"))

class OurHandler(BaseCallbackHandler):
    def on_chain_start(self, serialized, inputs, *, run_id, parent_run_id , **kwargs): 
        print("CHAIN START HOOK LOGIC")
        return super().on_chain_start(serialized, inputs, run_id=run_id, parent_run_id=parent_run_id, kwargs=None)
      
    def on_llm_end(self, response,  **kwargs):
        print("RESPONSE RECIEVED and parelling processed:",response)

chain = LLMChain(llm=llm, prompt=prompt_template)
print(chain.invoke({"input":"code to say hi is python"},{"callbacks":[OurHandler()]}))