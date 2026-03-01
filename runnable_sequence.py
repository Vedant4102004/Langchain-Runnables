import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence 

load_dotenv()
token = os.getenv("HUGGING_FACE_API_TOKEN")

# Use a standard PromptTemplate
prompt_1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
prompt_2 = PromptTemplate(
    template='Explain the following joke - {topic}',
    input_variables=['topic']
)


llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", 
    task="text-generation",
    huggingfacehub_api_token=token
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()


chain = RunnableSequence(prompt_1, model, parser, prompt_2, model, parser)

print(chain.invoke({'topic' : 'AI'}))