# DocMind AI PDF Assistant

Features:
- PDF upload
- Semantic search
- FAISS vector database
- Local LLM using Ollama
- Source citations

Tech:
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Ollama

DocMind is a modular Retrieval-Augmented Generation (RAG) project for PDF question answering.

## Structure

- `app.py` — Streamlit frontend
- `rag/` — modular RAG pipeline
- `data/uploaded_pdfs/` — uploaded documents
- `vector_store/` — persistent vector index storage
- `.env` — environment variables

## Run

1. Activate your Python environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`
