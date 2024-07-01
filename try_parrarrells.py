from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
model=Ollama(model="llama3")

chain = prompt | model | StrOutputParser()

from langchain_core.output_parsers import StrOutputParser

analysis_prompt = ChatPromptTemplate.from_template("is this a funny joke? {joke}")

composed_chain = {"joke": chain} | analysis_prompt | model | StrOutputParser()

print(composed_chain.invoke({"topic": "bears"}))