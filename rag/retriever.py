

def retrieve_relevant_chunks(query, vector_store, k=4):
    return vector_store.similarity_search(query, k=k)
