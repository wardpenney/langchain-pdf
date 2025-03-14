from langchain.memory import ConversationBufferWindowMemory
from app.chat.models import ChatArgs
from app.chat.memories.histories.sql_history import SqlMessageHistory

def window_buffer_memory_builder(chat_args: ChatArgs):
  return ConversationBufferWindowMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="answer",
    chat_memory=SqlMessageHistory(conversation_id=chat_args.conversation_id),
    k=2
  )
