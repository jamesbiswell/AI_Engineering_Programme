import dotenv

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import openai

# Example: Querying LLM without company context

def query_llm_without_context(question):
    """Query LLM without providing any context"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Test with company-specific question

question = "What were TechCorp's Q3 2024 revenue figures?"
answer = query_llm_without_context(question)
print(f"Question: {question}")
print(f"Answer: {answer}")


# Example: Simple RAG implementation

# Simulated company documents (in practice, these come from a database)
company_documents = {
    "q3_report": """
    TechCorp Q3 2024 Financial Report
    Revenue: $45.2 million (up 23% from Q2)
    Net Profit: $12.8 million
    Key Products: AI Platform ($28M), Cloud Services ($17.2M)
    Customer Growth: 15,000 new customers in Q3
    """,
    "product_guide": """
    TechCorp AI Platform Features:
    - Natural Language Processing
    - Computer Vision API
    - Predictive Analytics
    - Custom Model Training
    - Enterprise Support 24/7
    """
}

def simple_retrieval(query, documents):
    """
    Simple keyword-based retrieval
    In production, this would use semantic search with embeddings
    """
    relevant_docs = []
    query_lower = query.lower()

    # Check which documents contain relevant keywords
    if "revenue" in query_lower or "q3" in query_lower or "financial" in query_lower:
        relevant_docs.append(documents["q3_report"])

    if "product" in query_lower or "features" in query_lower or "platform" in query_lower:
        relevant_docs.append(documents["product_guide"])

    return "\n\n".join(relevant_docs)

def query_with_rag(question, documents):
    """Query LLM with retrieved context"""

    # Step 1: Retrieve relevant documents
    context = simple_retrieval(question, documents)

    # Step 2: Build augmented prompt
    augmented_prompt = f"""
    Answer the question based on the following context.
    If the answer isn't in the context, say so.

    Context:
    {context}

    Question: {question}

    Answer:"""

    # Step 3: Generate response with context
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": augmented_prompt}
        ]
    )

    return response.choices[0].message.content

# Test RAG system
question = "What were TechCorp's Q3 2024 revenue figures?"
answer = query_with_rag(question, company_documents)

print(f"Question: {question}")
print(f"RAG Answer: {answer}")