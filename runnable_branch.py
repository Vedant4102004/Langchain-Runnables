import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableBranch

load_dotenv()
token = os.getenv("HUGGING_FACE_API_TOKEN")

prompt_1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt_2 = PromptTemplate(
    template = 'Summarize the following text \n {text}',
    input_variables=['text']
)

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", 
    task="text-generation",
    huggingfacehub_api_token=token
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()
report_gen_chain = RunnableSequence(prompt_1, model, parser)
branch_chain = RunnableBranch(
    (lambda x : len(x.split()) > 500, RunnableSequence(prompt_2, model, parser)),
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_gen_chain, branch_chain, parser)

print(final_chain.invoke({'topic' : 'russia vs ukraine'}))