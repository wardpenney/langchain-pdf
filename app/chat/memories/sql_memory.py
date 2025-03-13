from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory
from app.chat.models import ChatArgs
from app.web.api import(
  add_message_to_conversation,
  get_messages_by_conversation_id
)


class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
  conversation_id: str

  @property
  def messages(self):
    return get_messages_by_conversation_id(self.conversation_id)

  def add_message(self, message: dict):
    return add_message_to_conversation(
      conversation_id=self.conversation_id,
      role=message.type,
      content=message.content
    )

  def clear(self):
    pass

def build_memory(chat_args: ChatArgs):
  return ConversationBufferMemory(
    chat_memory=SqlMessageHistory(conversation_id=chat_args.conversation_id),
    return_messages=True,
    output_key="answer",
    memory_key="chat_history"
  )
