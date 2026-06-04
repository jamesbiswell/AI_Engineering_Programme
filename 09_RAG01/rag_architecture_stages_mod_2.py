from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

###
### INDEXING STAGE STEP 1: DOCUMENT LOADING

import pypdf
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredMarkdownLoader

# Load different document types
def load_documents(file_path):
    """Load documents based on the file type"""
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith('.txt'):
        loader = TextLoader(file_path)
    elif file_path.endswith('.md'):
        loader = UnstructuredMarkdownLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
    documents = loader.load()
    return documents

# Example usage - load document
docs = load_documents("company_handbook.pdf")
print(f"Loaded {len(docs)} document(s)")
print(f"First page preview: {docs[0].page_content[:200]}...")


###
### INDEXING STAGE STEP 2: TEXT CHUNKING

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Text chunking strategy
def chunk_documents(documents, chunk_size=1000, chunk_overlap=200):
    """
    Split documents into chunks with overlap to maintain context

    Args:
        chunk_size: Maximum characters per chunk
        chunk_overlap: Characters to overlap between chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)
    return chunks

# Example usage - process documents into chunks
document_chunks = chunk_documents(docs)
print(f"Created {len(document_chunks)} chunks")
print(f"Example chunk:\n{document_chunks[0].page_content}")


###
### INDEXING STAGE STEP 3: GENERATE EMBEDDINGS

from langchain_openai import OpenAIEmbeddings

# Initialize embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# Example usage - generate embeddings for a sample chunk
sample_text = document_chunks[0].page_content
embedding_vector = embeddings.embed_query(sample_text)

print(f"Embedding dimensions: {len(embedding_vector)}")
print(f"First 5 values: {embedding_vector[:5]}")


###
### INDEXING STAGE STEP 4: STORE IN A VECTOR DATABASE

from langchain_chroma import Chroma

persist_directory = "./chroma_db"

# Delete any existing Chroma store from previous runs
import os
import shutil

if os.path.exists(persist_directory):
    shutil.rmtree(persist_directory)
    print(f"Deleted existing Chroma vector store: {persist_directory}")

# Create vector store from documents
vectorstore = Chroma.from_documents(
    documents=document_chunks,
    embedding=embeddings,
    persist_directory=persist_directory
)

# Example usage - check Chroma persistence
print(f"Chroma vector store created with {vectorstore._collection.count()} vectors")


###
### RETRIEVAL STAGE

# Retrieval implementation
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
    # Perform similarity search
    results = vectorstore.similarity_search_with_score(query, k=k)

    # Format results
    retrieved_chunks = []
    for doc, score in results:
        retrieved_chunks.append({
            'content': doc.page_content,
            'score': score,
            'metadata': doc.metadata
        })

    return retrieved_chunks

# Example usage - query and display results
user_query = "What is the company's vacation policy?"
retrieved = retrieve_relevant_chunks(user_query, vectorstore, k=3)

print(f"Query: {user_query}\n")
for i, chunk in enumerate(retrieved, 1):
    print(f"Result {i} (Score: {chunk['score']:.4f}):")
    print(chunk['content'][:200] + "...\n")


###
### GENERATION STAGE STEP 1: CONTEXT AUGMENTATION

# Prompt template for RAG
def build_rag_prompt(query, retrieved_chunks):
    """Construct prompt with context and query"""
    # Combine all retrieved chunks
    context = "\n\n".join([chunk['content'] for chunk in retrieved_chunks])

    # Build structured prompt
    prompt = f"""You are a helpful assistant that answers questions based on the provided context.
Use only the information from the context to answer the question.
If the answer is not in the context, say "I don't have enough information to answer that question."
                 
Context: {context}
             
Question: {query}
             
Answer:"""
    return prompt

# Example usage - create a prompt
rag_prompt = build_rag_prompt(user_query, retrieved)
print("Prompt length: ", len(rag_prompt), "characters")


###
### GENERATION STAGE STEP 2: LLM GENERATION

from openai import OpenAI
client = OpenAI()

# Generate response using LLM
def generate_response(prompt):
    """Generate answer using LLM"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3  # Lower temperature for more factual responses
    )

    return response.choices[0].message.content

# Example usage - generate final answer
answer = generate_response(rag_prompt)
print(f"Question: {user_query}")
print(f"Answer: {answer}")