import openai
import threading
import os

client_lock = threading.Lock()
client = None


def get_openai_client():
    global client
    with client_lock:
        if client is None:
            # Check if the API key is set
            api_key = openai.api_key or os.getenv('OPENAI_API_KEY')
            if api_key is None:
                raise ValueError("OpenAI API key is not set. Please set it using set_openai_key.")
            client = openai.OpenAI(api_key=api_key)
    return client


def set_openai_key(key):
    if not key:
        raise ValueError("Invalid API key. The API key cannot be empty.")
    openai.api_key = key