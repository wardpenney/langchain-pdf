from langchain.memory import ConversationBufferMemory
from app.chat.models import ChatArgs
from app.chat.memories.histories.sql_history import SqlMessageHistory

def build_memory(chat_args: ChatArgs):
  return ConversationBufferMemory(
    chat_memory=SqlMessageHistory(conversation_id=chat_args.conversation_id),
    return_messages=True,
    output_key="answer",
    memory_key="chat_history"
  )
