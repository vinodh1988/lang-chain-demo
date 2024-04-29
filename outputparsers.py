from langchain.output_parsers import ResponseSchema,StructuredOutputParser,XMLOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate,SystemMessagePromptTemplate

llm= ChatOpenAI()

response_schemas= [
   ResponseSchema(name="name", description="An indian name in any gender"),
   ResponseSchema(name="occupation",description="An major job role which could be as diverse from farmer to scientist, just one word"),
   ResponseSchema(name="annualincome",description="Relevant to the occupation , annual income in rupees", type="float")
  ]   

response_schemas2 = [
    ResponseSchema(name="people",description="""an array of objects like
                    [{name:string,occupation: string, annualincome: float}] 
                   name should indian name any gender,
                    occupation should be diverse, annual income is in indian currency""",type="array(objects)")
]
parser = StructuredOutputParser.from_response_schemas(response_schemas2)
format_instruction = parser.get_format_instructions()
print(format_instruction)

prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "Generate 50 json Records by taking instructions"
            "instructions: {input}\n"
            "{format_instructions} \n"
        )
    ],
    input_variables=["input"],
    partial_variables={"format_instructions": format_instruction}

)

final_prompt=prompt.format_prompt(input="list of people with varied occupations")

output = llm.invoke(final_prompt.to_messages())
print(output.content)

json_output=parser.parse(output.content)
print(json_output)