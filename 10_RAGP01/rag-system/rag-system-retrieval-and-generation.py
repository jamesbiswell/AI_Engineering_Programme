### Import libraries ###
import time

from dotenv import load_dotenv, find_dotenv
import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


# ===================
# RETRIEVAL COMPONENT
# ===================
def retrieve_relevant_chunks(query, vectorstore, k=3):
    """
    Retrieve most relevant document chunks for a query

    Args:
        query: User's question
        vectorstore: Vector database instance
        k: Number of chunks to retrieve

    Returns:
        List of relevant document chunks with scores
    """

    # Perform similarity search with scores
    print(f"\n[RETRIEVAL] Retrieving relevant chunks for query '{query}' (top {k} chunks)")
    results = vectorstore.similarity_search_with_score(query, k=k)

    # Format results
    # formatted_results = [(doc.page_content, score, doc.metadata) for doc, score in results]
    # print(f"Retrieved {len(formatted_results)} relevant chunks")
    # return formatted_results

    retrieved_chunks = []
    for doc, score in results:
        retrieved_chunks.append({
            'content': doc.page_content,
            'source': doc.metadata.get('source', 'Unknown'),
            'score': score,
            'metadata': doc.metadata
        })

    print(f"\n[RETRIEVAL] Retrieved {len(retrieved_chunks)} relevant chunks")
    return retrieved_chunks


# ==================
# PROMPT ENGINEERING
# ==================
def build_rag_prompt(query, retrieved_chunks, verbose=True):
    """
    Construct prompt with context and query

    Args:
        query: User's question
        retrieved_chunks: List of retrieved document chunks
        verbose: Print detailed information

    Returns:
        Formatted prompt string
    """

    # Combine all retrieved chunks into the context
    context = "\n\n---\n\n".join([f"[Source: {chunk['source']}]\n{chunk['content']}" for chunk in retrieved_chunks])

    # Build structured prompt
    prompt = f"""
You are a helpful assistant that answers questions based on the provided context.

INSTRUCTIONS:
- Use ONLY the information from the context below to answer the question
- If the answer is not in the context, say "I don't have enough information to answer that question."
- Be concise and accurate
- Cite specific parts of the context when relevant

CONTEXT: {context}

QUESTION: {query}

ANSWER:

"""
    if verbose:
        print(f"\n[PROMPT] Prompt:{prompt}")
        print(f"\n[PROMPT] Prompt constructed with {len(context)} characters of context")
    return prompt


# ====================
# GENERATION COMPONENT
# ====================
def generate_answer(prompt, model="gpt-3.5-turbo", temperature=0.3):
    """
    Generate answer using LLM

    Args:
        prompt: Complete prompt with context and query
        model: OpenAI model to use
        temperature: Controls randomness (lower = more factual)

    Returns:
        Generated response string
    """
    print(f"\n[GENERATION] Generating response using model {model}")

    # Initialise LLM
    load_dotenv(find_dotenv(), override=True)
    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    # Generate response
    start_time = time.time()
    response = llm.invoke(prompt)
    end_time = time.time()
    print(f"\n[GENERATION] Response generated in {end_time - start_time:.4f} seconds")
    return response.content


# ===========================
# COMPLETE RAG QUERY PIPELINE
# ===========================
def query_rag_system(question, vectorstore, k=3, verbose=True):
    """
    Complete RAG query: Retrieve and Generate

    Args:
        question: User's question
        vectorstore: Vector database instance
        k: Number of chunks to retrieve
        verbose: Print detailed information

    Returns:
        Dictionary with answer and metadata
    """
    print(f"\n[RAG SYSTEM] Starting RAG query pipeline")
    if verbose:
        print(f"\n[VECTOR STORE] Using vector store with {vectorstore._collection.count()} documents")
    print(f"\n[QUERY] Processing query: {question}")

    # Retrieve relevant chunks
    retrieved_chunks = retrieve_relevant_chunks(question, vectorstore, k=k)
    if verbose:
        print("\n[RETRIEVED CHUNKS]")
        for i, chunk in enumerate(retrieved_chunks, 1):
            print(f"\nChunk {i} (Score: {chunk['score'] :.4f}):")
            print(f"\n{chunk['content'][:200]} ...")

    # Build prompt
    rag_prompt = build_rag_prompt(question, retrieved_chunks, verbose=verbose)
    # if verbose:
    print(f"\n[PROMPT] Length: {len(rag_prompt)} characters")

    # Generate answer
    answer = generate_answer(rag_prompt)
    # if verbose:
    print(f"\n[ANSWER] Length: {len(answer)} characters")

    # Return results
    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks,
        "num_chunks_used": len(retrieved_chunks)
    }

# =============
# EXAMPLE USAGE
# =============

if __name__ == "__main__":

    print("\n[MAIN] Starting example usage")

    # Load existing vector store
    load_dotenv(find_dotenv(), override=True)

    embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv('OPENAI_API_KEY')
    )

    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    # Example queries
    queries = [
        "What is this document about?"
        ,
        "What are the main landmarks of the city?",
        "What are the most common methods of building construction?"
    ]

    for query in queries:
        # results = query_rag_system(query, vectorstore, k=10, verbose=True)
        results = query_rag_system(query, vectorstore, k=10, verbose=False)
        print(f"\n[QUERY RESULT]"
              f"\nQuery: {results['question']}"
              f"\nAnswer: {results['answer']}"
              f"\nChunks used: {results['num_chunks_used']}")