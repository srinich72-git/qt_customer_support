from langchain_core.language_models.chat_models import BaseChatModel

def get_llm(model: str = "gpt-4o-mini") -> BaseChatModel:
    return ChatOpenAI(model=model, temperature=0)