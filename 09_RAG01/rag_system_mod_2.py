# Complete RAG system implementation
from openai import OpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

class RAGSystem:
    # def __init__(self, openai_api_key):
    def __init__(self):
        # """Initialize RAG system with API key"""
        # self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = None
        self.client = OpenAI()
        # openai.api_key = openai_api_key

    def index_documents(self, file_paths, chunk_size=1000, chunk_overlap=200):
        """
        STAGE 1: INDEX
        Load, chunk, embed, and store documents
        """
        print("Starting indexing process...")

        # Load documents
        documents = []
        for path in file_paths:
            # loader = TextLoader(path)
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
        print(f"Loaded {len(documents)} documents")

        # Chunk documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        chunks = text_splitter.split_documents(documents)
        print(f"Created {len(chunks)} chunks")

        # Delete any existing Chroma store from previous runs
        import os
        import shutil

        persist_directory = "./rag_db"

        if os.path.exists(persist_directory):
            shutil.rmtree(persist_directory)
            print(f"Deleted existing Chroma vector store: {persist_directory}")

        # Create vector store
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=persist_directory
        )
        # self.vectorstore.persist()
        print("Indexing complete!")

    def retrieve(self, query, k=3):
        """
        STAGE 2: RETRIEVE
        Find relevant chunks for the query
        """
        if self.vectorstore is None:
            raise ValueError("No documents indexed. Call index_documents first.")

        results = self.vectorstore.similarity_search_with_score(query, k=k)

        retrieved_chunks = []
        for doc, score in results:
            retrieved_chunks.append({
                'content': doc.page_content,
                'score': score,
                'source': doc.metadata.get('source', 'Unknown')
            })

        return retrieved_chunks

    def generate(self, query, retrieved_chunks):
        """
        STAGE 3: GENERATE
        Create the response using LLM with retrieved context
        """
        # Build context from chunks
        context = "\n\n".join([
            f"[Source: {chunk['source']}]\n{chunk['content']}"
            for chunk in retrieved_chunks
        ])

        # Create prompt
        prompt = f"""Answer the question based on the context below. 
If the answer is not in the context, say so clearly.
Cite sources when possible.

Context: {context}

Question: {query}

Answer: 
"""

        # Generate response
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    def query(self, question, k=3, verbose=False):
        """
        Complete RAG pipeline: retrieve and generate
        """
        # Retrieve relevant chunks
        retrieved = self.retrieve(question, k=k)

        if verbose:
            print(f"\nRetrieved {len(retrieved)} chunks:")
            for i, chunk in enumerate(retrieved, 1):
                print(f"{i}. Score: {chunk['score']:.4f} | Source: {chunk['source']}")

        # Generate answer
        answer = self.generate(question, retrieved)

        return {
            'answer': answer,
            'sources': retrieved
        }

# Example usage
# rag = RAGSystem(openai_api_key="your-api-key")
rag = RAGSystem()

# Index documents
# rag.index_documents(["docs/handbook.txt", "docs/policies.txt"])
rag.index_documents(["company_handbook.pdf"])

# Query the system
result = rag.query("What are the working hours?", verbose=True)
print(f"\nQuestion: What are the working hours?")
print(f"Answer: {result['answer']}")