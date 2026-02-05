import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
PORCUPINE_ACCESS_KEY = os.getenv("PORCUPINE_ACCESS_KEY")
