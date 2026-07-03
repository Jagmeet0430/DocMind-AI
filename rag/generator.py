from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="phi3:mini"
)


def generate_answer(question, chunks):

    context = "\n\n".join([
        c.page_content[:500]
        for c in chunks
    ])

    prompt = f"""
You are a helpful PDF assistant.

Answer only using the context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response,
        "sources": list(set(
            [
                c.metadata.get("source", "Unknown")
                for c in chunks
            ]
        ))
    }