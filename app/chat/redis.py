import os
import redis

client = redis.Redis(
  decode_responses=True
)

