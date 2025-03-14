from langchain.chat_models import ChatOpenAI
from app.chat.models import ChatArgs

def build_llm(chat_args: ChatArgs, model_name: str):
  return ChatOpenAI(
    streaming=chat_args.streaming,
    model=model_name
  )
