import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()
token = os.getenv("HUGGING_FACE_API_TOKEN")



prompt_1 = PromptTemplate.from_template("generate short notes from this: {text}")
prompt_2 = PromptTemplate.from_template("generate 5 questions from this: {text}")
prompt_3 = PromptTemplate.from_template("Summarize these notes: {notes} and these questions: {quiz}")


llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", 
    task="text-generation",
    huggingfacehub_api_token=token,
    max_new_tokens=512
)


model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt_1 | model | parser,
    "quiz": prompt_2 | model | parser
})


chain = RunnableSequence(parallel_chain, prompt_3, model, parser)

text = "Support vector machines (SVMs) are supervised learning methods for classification."

print("Running Chain with Zephyr...")

try:
    result = chain.invoke({"text": text})
    print("\n--- RESULT ---\n")
    print(result)
except Exception as e:
    
    import traceback
    print(f"\nAPI Error: {e}")
    traceback.print_exc()