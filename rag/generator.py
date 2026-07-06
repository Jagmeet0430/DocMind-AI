import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=True)


def get_llm():
    google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash")

    if not google_api_key:
        raise ValueError(
            "GOOGLE_API_KEY is missing. Add it to your .env file."
        )

    return ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=google_api_key,
        temperature=0.2,
    )


def generate_answer(question, context):
    llm = get_llm()
    context_text = "\n\n".join(doc.page_content for doc in context)
    sources = sorted({
        doc.metadata.get("source", "Unknown source")
        for doc in context
    })

    prompt = f"""
You are a helpful AI assistant.

Answer the question using only the given context.

Context:
{context_text}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)
    return {
        "answer": response.content,
        "sources": sources,
    }
