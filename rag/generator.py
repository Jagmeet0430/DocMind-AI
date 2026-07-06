from langchain_google_genai import ChatGoogleGenerativeAI
from rag.config import GOOGLE_API_KEY, MODEL_NAME


def get_llm():
    if not GOOGLE_API_KEY:
        raise ValueError(
            "GOOGLE_API_KEY is missing. Add it to local .env or Streamlit Secrets."
        )

    return ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2,
    )


def generate_answer(question, context):
    llm = get_llm()

    prompt = f"""
You are a helpful AI assistant.
Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)
    return response.content
