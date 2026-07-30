"""Problem 2: Tool Result Aggregation & Deduplication (Advanced)
Scenario: Your agent calls multiple tools that return similar data. You need to:

Collect all results from different tools.

Identify and remove duplicate entries (case-insensitive).

Rank results by relevance score.

Return the top N unique results.

Requirements:

Input: List of tool results, each with source, content, and score

Output: Top N unique results, sorted by score descending

Deduplication: Results are considered duplicates if their content is similar (use Levenshtein distance or simple text similarity threshold)"""

import re
from difflib import SequenceMatcher

def text_similarity(text1, text2):
    """Calculate similarity between two texts using SequenceMatcher."""
    # Clean texts for better comparison
    clean1 = re.sub(r'[^\w\s]', '', text1.lower())
    clean2 = re.sub(r'[^\w\s]', '', text2.lower())
    return SequenceMatcher(None, clean1, clean2).ratio()

def deduplicate_and_rank(results, similarity_threshold=0.8, top_n=3):
    """
    Deduplicate results, rank by score, return top N unique results.
    """
    if not results:
        return []
    
    # Sort by score descending first (so we keep highest score for duplicates)
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
    
    unique_results = []
    
    for result in sorted_results:
        is_duplicate = False
        
        # Check against existing unique results
        for existing in unique_results:
            similarity = text_similarity(result["content"], existing["content"])
            if similarity >= similarity_threshold:
                is_duplicate = True
                break
        
        if not is_duplicate:
            unique_results.append(result)
    
    # Return top N
    return unique_results[:top_n]

# Test
tool_results = [
    {"source": "search_google", "content": "Paris is the capital of France", "score": 0.95},
    {"source": "search_bing", "content": "Paris is the capital of France", "score": 0.92},
    {"source": "wikipedia", "content": "Paris is the capital and most populous city of France", "score": 0.98},
    {"source": "search_google", "content": "London is the capital of UK", "score": 0.85},
    {"source": "search_bing", "content": "London is the capital of the United Kingdom", "score": 0.83},
    {"source": "knowledge_base", "content": "Paris is the capital of France", "score": 0.90},
    {"source": "search_google", "content": "Berlin is the capital of Germany", "score": 0.75},
]

unique = deduplicate_and_rank(tool_results, top_n=3)
print("Top 3 unique results:")
for i, r in enumerate(unique, 1):
    print(f"{i}. [{r['score']:.2f}] {r['content'][:50]}... (from {r['source']})")