import os
from langfuse.client import Langfuse

langfuse = Langfuse(
    os.getenv("LF_PUBLIC_KEY"),
    os.getenv("LF_SECRET_KEY"),
    host="https://prod-langfuse.fly.dev"
)
