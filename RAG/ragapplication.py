from fastapi import FastAPI, HTTPException

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores.faiss import FAISS


embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

app = FastAPI()


# Updated template with examples, context, and a non-related example
template = """
You are an agent for an online Software training platform called SmartLearn
 based on the
{context}

Now, adhering to the context, process the text below and give your best answer:
text: {question}



"""

PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])


chain_type_kwargs = {"prompt": PROMPT}


vectorstore = FAISS.load_local("smartlearn-index", embeddings,allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs=chain_type_kwargs,
)


@app.post("/conversation")
async def conversation(query: str):
    try:
        print(query)
        result = qa.run(query=query)
        previous_question="Q: "+query+ "\n A:"+result
        return {"response": result}
    
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=500)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5566)



