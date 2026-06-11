### STEP 0: Import libraries ###
from dotenv import load_dotenv, find_dotenv
import os
import shutil
import sys
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredMarkdownLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# =============
# MAIN PIPELINE
# =============

def run_rag_pipeline(file_path):

    ### STEP 1: Load documents ###
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith('.txt'):
        loader = TextLoader(file_path)
    elif file_path.endswith('.md'):
        loader = UnstructuredMarkdownLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

    docs = loader.load()
    print(f"[1/4] Loaded {len(docs)} document(s) from {file_path}")

    ### STEP 2: Chunk documents ###
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(docs)
    print(f"[2/4] Created {len(chunks)} chunk(s) from {len(docs)} document(s)")

    ### STEP 3: Initialise embeddings ###
    load_dotenv(find_dotenv(), override=True)
    embeddings = OpenAIEmbeddings(
                openai_api_key=os.getenv("OPENAI_API_KEY"),
                model="text-embedding-3-small"
    )
    print("[3/4] Embeddings initialised")

    ### STEP 4: Create vector store ###
    persist_directory = "./chroma_db"

    # # Delete an existing Chroma store from a previous run
    # if os.path.exists(persist_directory):
    #     shutil.rmtree(persist_directory)
    #     print(f"Deleted existing Chroma vector store: {persist_directory}")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    print(f"[4/4] Vector store created with {len(chunks)} chunks")

    ### STEP 5: Test a document query ###
    print(f"\n[TEST] Testing similarity search for a document...")
    query = "What is this document about?"
    # results = vectorstore.similarity_search(query, k=3)
    results = vectorstore.similarity_search(query)
    print(f"Query: '{query}'")
    print(f"Found {len(results)} relevant chunks")
    print(f"Top results for query: '{query}'")

    for i, result in enumerate(results, 1):
        print(f"Result {i}:"
                # Print first 150 characters of each result
              f"{result.page_content[:150]}...")

# ==============
# MAIN EXECUTION
# ==============

if __name__ == "__main__":

    # # Check if filepath is provided as a command-line argument
    # if len(sys.argv) < 2:
    #     print("Usage: python rag-system-indexing-pipeline.py <filepath>")
    #     sys.exit(1)
    #
    # # Get the filepath from command-line arguments
    # filepath = sys.argv[1]

    filepath = "test_doc.txt"

    # Run the RAG pipeline with the provided filepath
    run_rag_pipeline(filepath)