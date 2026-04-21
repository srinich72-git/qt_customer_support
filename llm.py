from langchain_core.language_models.chat_models import BaseChatModel
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_llm(model: str = "openai:gpt-4o-mini") -> BaseChatModel:
    return init_chat_model(model=model, temperature=0)

if __name__ == "__main__":
    llm =get_llm()
    response = llm.invoke("What is the capital of France?")
    response.pretty_print()