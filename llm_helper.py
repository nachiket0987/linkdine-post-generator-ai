import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
MODEL_NAME = "llama-3.3-70b-versatile"
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name=MODEL_NAME)


response = llm.invoke("Two most important ingredients in samosa are ")
response = llm.invoke("Two most important ingradient in samosa are ")
print(response.content)





