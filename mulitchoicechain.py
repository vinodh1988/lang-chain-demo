
from langchain_openai import ChatOpenAI
from langchain.chains.router import MultiPromptChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
llm = ChatOpenAI()

cricket_template = """You are an AI that is specialized to answer queries on 
cricket by introducting yourself as crickmate . Here is the text:
{input}"""

math_template = """You are an AI that is specialized in 
 solving math problems introducting yourself as mathgeek.  Here is the text:
{input}"""

java_template = """You are an AI Thatis specialized in solving 
Java language related questions introducting yourself as javajohnson. Here is the text:
{input}"""



prompt_infos = [
    {
        "name": "cricket",
        "description": "Good for analyzing cricket related queries ",
        "prompt_template": cricket_template,
    },
    {
        "name": "math",
        "description": "Good for analyzing math related queries",
        "prompt_template": math_template,
    },
    {
        "name": "java",
        "description": "Good for analyzing Java related queries",
        "prompt_template": java_template,
    },
]

# Creating LLMChain for each context
destination_chains= {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template=p_info["prompt_template"]
    prompt=PromptTemplate(template=prompt_template,input_variables=["input"])
    chain=LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

#print(destination_chains)

destinations =[f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)


print(destinations_str)

router_template= MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)

router_prompt =PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser()
)

router_chain =LLMRouterChain.from_llm(llm,router_prompt)

chain=MultiPromptChain(
    router_chain= router_chain,
    destination_chains = destination_chains,
    default_chain= destination_chains["java"],
    verbose=True
)

result = chain.invoke({"input": " How to overcome depression?"})

print(result)