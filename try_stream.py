from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
parser = StrOutputParser()
llm = Ollama(model="llama3")

chain = prompt | llm | parser

for chunk in chain.stream({"topic": "parrot"}):
    print(chunk, end="|", flush=True)