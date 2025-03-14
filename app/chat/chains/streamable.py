from threading import Thread
from queue import Queue
from app.chat.callbacks.stream import StreamingHandler

class StreamableChain:
  def stream(self, input: dict):
    queue = Queue()
    handler = StreamingHandler(queue)

    def task():
      self(input, callbacks=[handler])

    Thread(target=task).start()

    while True:
      token = queue.get()

      if token is None:
        break

      yield token
