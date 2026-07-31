tools = ["calculator", "search", "database", "weather_api", "email"]

# 1. Sort alphabetically (default)
sorted_tools = sorted(tools)  # Creates new list
print("Alphabetical:", sorted_tools)

# 2. Sort by length
sorted_by_length = sorted(tools, key=len)
print("By length:", sorted_by_length)

# 3. Sort descending
descending = sorted(tools, reverse=True)
print("Descending:", descending)

# 4. Sort numbers
scores = [95, 78, 92, 88, 99]
scores.sort()  # Modifies in place
print("Sorted scores:", scores)

# 5. Sort with custom key (dictionaries)
tool_results = [
    {"name": "search", "confidence": 0.95},
    {"name": "calculator", "confidence": 0.78},
    {"name": "weather", "confidence": 0.92},
    {"name": "email", "confidence": 0.88},
]

# Sort by confidence (highest first)
by_confidence = sorted(tool_results, key=lambda x: x["confidence"], reverse=True)
print("Sorted by confidence:")
for tool in by_confidence:
    print(f"  {tool['name']}: {tool['confidence']}")

# 6. Sort by multiple keys (confidence, then name)
by_multiple = sorted(tool_results, key=lambda x: (-x["confidence"], x["name"]))
print("By confidence (desc) then name:")
for tool in by_multiple:
    print(f"  {tool['name']}: {tool['confidence']}")
print("-"*30)

# Agent ranks results by relevance
def rank_search_results(results):
    # Sort by relevance score (higher = better)
    ranked = sorted(results, key=lambda x: x["score"], reverse=True)
    return ranked

# Example search results
search_results = [
    {"title": "Paris Travel Guide", "score": 0.85},
    {"title": "Best Restaurants in Paris", "score": 0.92},
    {"title": "Paris Weather", "score": 0.78},
    {"title": "History of Paris", "score": 0.95},
]

ranked = rank_search_results(search_results)
print("Ranked search results:")
for i, result in enumerate(ranked, 1):
    print(f"{i}. {result['title']} (score: {result['score']})")