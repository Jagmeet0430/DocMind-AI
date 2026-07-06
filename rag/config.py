from pathlib import Path
from dotenv import dotenv_values
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

print("ENV PATH:", ENV_PATH)
print("Exists:", ENV_PATH.exists())

print("dotenv_values:", dotenv_values(ENV_PATH))

from dotenv import load_dotenv
load_dotenv(dotenv_path=ENV_PATH, override=True)

print("os.getenv:", os.getenv("GOOGLE_API_KEY"))

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = "gemini-2.5-flash"