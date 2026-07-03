import streamlit as st
from dotenv import load_dotenv

# LOAD ENV FIRST
load_dotenv()

from rag.loader import load_multiple_pdfs
from rag.chunker import chunk_documents
from rag.embedder import build_vector_store
from rag.retriever import retrieve_relevant_chunks
from rag.generator import generate_answer

st.set_page_config(
    page_title="DocMind — AI PDF Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 DocMind — AI PDF Assistant")
st.caption("Professional RAG-powered PDF question answering system")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

with st.sidebar:
    st.header("📄 Upload PDFs")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    chunk_size = st.slider("Chunk Size", 200, 2000, 1000)
    chunk_overlap = st.slider("Chunk Overlap", 0, 500, 200)
    top_k = st.slider("Top K Retrieval", 1, 10, 4)

    if uploaded_files:
        if st.button("🚀 Build Knowledge Base"):
            try:
                with st.spinner("Loading documents..."):
                    docs = load_multiple_pdfs(uploaded_files)

                with st.spinner("Chunking documents..."):
                    chunks = chunk_documents(
                        docs,
                        chunk_size,
                        chunk_overlap
                    )

                with st.spinner("Creating vector store..."):
                    vector_store = build_vector_store(chunks)

                st.session_state.vector_store = vector_store

                st.success("Knowledge base created successfully!")

            except Exception as e:
                st.error(f"Error: {e}")

if st.session_state.vector_store is None:
    st.info("Upload PDFs and create the knowledge base to begin.")
    st.stop()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask a question about your documents...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Searching documents..."):
                chunks = retrieve_relevant_chunks(
                    question,
                    st.session_state.vector_store,
                    k=top_k
                )

            with st.spinner("Generating answer..."):
                result = generate_answer(question, chunks)

            st.write(result["answer"])

            with st.expander("📚 Sources"):
                for source in result["sources"]:
                    st.write(f"• {source}")

            st.session_state.messages.append({
                "role": "assistant",
                "content": result["answer"]
            })

        except Exception as e:
            st.error(f"Error: {e}")
