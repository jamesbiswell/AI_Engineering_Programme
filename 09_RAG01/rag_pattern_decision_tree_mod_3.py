# Decision tree for RAG pattern selection

def recommend_rag_pattern(
        num_documents,
        query_complexity,
        latency_requirement,
        document_structure):
    """
    Recommend the appropriate RAG pattern based on requirements

    Args:
        num_documents: Number of documents in knowledge base
        query_complexity: 'simple', 'medium', 'complex'
        latency_requirement: 'low', 'medium', 'high' (high = strict)
        document_structure: 'flat', 'hierarchical', 'mixed'

    Returns:
        Recommended RAG pattern and justification
    """

    # Simple cases - Basic RAG
    if query_complexity == 'simple' and num_documents < 1000:
        return {
            'pattern': 'Basic RAG',
            'justification': 'Simple queries with small corpus work well with basic RAG.'
        }

    # Strict latency - Optimise for speed
    if latency_requirement == 'high':
        return {
            'pattern': 'Basic RAG with Caching',
            'justification': 'Single retrieval minimises latency, caching reduces repeat queries.'
        }

    # Hierarchical documents - Use structure
    if document_structure == 'hierarchical' and num_documents > 100:
        return {
            'pattern': 'Hierarchical RAG',
            'justification': 'Leverage document structure for better context.'
        }

    # Complex queries - Multi-query approach
    if query_complexity == 'complex' and latency_requirement != 'high':
        return {
            'pattern': 'Multi-Query RAG',
            'justification': 'Complex queries benefit from multiple retrieval perspectives.'
        }

    # Large corpus - Hybrid search
    if num_documents > 10000:
        return {
            'pattern': 'Hybrid Search RAG',
            'justification': 'Large corpus benefits from combining semantic and keyword search.'
        }

    # Default recommendation
    return {
        'pattern': 'Basic RAG',
        'justification': 'Start simple and iterate based on performance.'
    }

# Example usage
# recommendation = recommend_rag_pattern(
#     num_documents=5000,
#     query_complexity='medium',
#     latency_requirement='medium',
#     document_structure='flat'
# )

# print(f"Recommended Pattern: {recommendation['pattern']}")
# print(f"Justification: {recommendation['justification']}")

def rag_pattern_prompt():

    while True:

        print("\n" + "=" * 21)
        print("RAG Pattern Selection")
        print("=" * 21)

        while True:
            print("Enter the number of documents. (or 'quit' to exit)")
            num_documents = input("Number of documents: ").strip()
            if num_documents.lower() == 'quit':
                return
            elif not num_documents.isdigit():
                print("Please enter a valid number.")
            else:
                num_documents = int(num_documents)
                break

        while True:
            print("Enter the complexity of the query - simple, medium, complex. (or 'quit' to exit)")
            query_complexity = input("Query complexity: ").strip().lower()
            if query_complexity == 'quit':
                return
            elif query_complexity not in ['simple', 'medium', 'complex']:
                print("Please enter simple, medium, or complex.")
            else:
                break

        while True:
            print("Enter the latency requirement - low, medium, high. (or 'quit' to exit)")
            latency_requirement = input("Latency requirement: ").strip().lower()
            if latency_requirement == 'quit':
                return
            elif latency_requirement not in ['low', 'medium', 'high']:
                print("Please enter low, medium, or high.")
            else:
                break

        while True:
            print("Enter the document structure - flat, hierarchical, mixed. (or 'quit' to exit)")
            document_structure = input("Document structure: ").strip().lower()
            if document_structure == 'quit':
                return
            elif document_structure not in ['flat', 'hierarchical', 'mixed']:
                print("Please enter flat, hierarchical, or mixed.")
            else:
                break

        recommendation = recommend_rag_pattern(
            num_documents=num_documents,
            query_complexity=query_complexity,
            latency_requirement=latency_requirement,
            document_structure=document_structure
        )

        print(f"Recommended Pattern: {recommendation['pattern']}")
        print(f"Justification: {recommendation['justification']}")

rag_pattern_prompt()