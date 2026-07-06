import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH, override=True)

try:
    import streamlit as st

    GOOGLE_API_KEY = (
        st.secrets.get("GOOGLE_API_KEY")
        or os.getenv("GOOGLE_API_KEY")
        or os.getenv("GEMINI_API_KEY")
    )
    MODEL_NAME = st.secrets.get(
        "MODEL_NAME",
        os.getenv("MODEL_NAME", "gemini-2.5-flash"),
    )
except Exception:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")
