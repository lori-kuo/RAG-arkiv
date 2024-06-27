from langchain.llms import OpenAI
from langchain_community.llms import OpenAIChat
import os
os.environ["OPENAI_API_KEY"] = "None"
os.environ["OPENAI_API_BASE"] = "http://10.58.0.2:8000/v1"
llm_completion = OpenAI(model_name="Qwen1.5-14B")
llm_chat = OpenAIChat(model_name="Qwen1.5-14B")

print(llm_chat)


