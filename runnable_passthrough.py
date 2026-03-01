import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough

load_dotenv()
token = os.getenv("HUGGING_FACE_API_TOKEN")

prompt_1 = PromptTemplate(
    template="Write a joke about - {text}",
    input_variables=['text']
)
prompt_2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=['text']
)

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", 
    task="text-generation",
    huggingfacehub_api_token=token
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt_1, model, parser)
parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt_2, model, parser)
})
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
print(final_chain.invoke({'text' : 'virat kohli'}))