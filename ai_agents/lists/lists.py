conversation = []

def add_message(role, content):
    conversation.append({"role": role, "content": content})
    # Keep only last 10 messages (context window management)
    if len(conversation) > 10:
        conversation.pop(0)  # Remove oldest message

# Simulate a conversation
add_message("user", "What is the weather?")
add_message("assistant", "Let me check the weather for you...")
add_message("user", "I meant in Tokyo")
add_message("assistant", "Tokyo is sunny at 25°C")
add_message("user", "What is the weather?")
add_message("assistant", "Let me check the weather for you...")
add_message("user", "I meant in Tokyo")
add_message("assistant", "Tokyo is sunny at 25°C")
add_message("user", "What is the weather?")
add_message("assistant", "Let me check the weather for you...")
add_message("user", "I meant in Tokyo")


for msg in conversation:
    print(f"{msg['role']}: {msg['content']}")
    
print("---------------------------------------------------------------------")
# Tool results from various sources
results = []

# Simulate adding results from tools
results.append({"tool": "search", "data": ["result1", "result2", "result3"]})
results.append({"tool": "calculator", "data": 42})
results.append({"tool": "weather", "data": {"temp": 22, "city": "London"}})

# Process all results
for result in results:
    print(f"Tool: {result['tool']}")
    print(f"Data: {result['data']}")
    print()

# Extract all data from search results
search_data = [r["data"] for r in results if r["tool"] == "search"]
print(f"Search data: {search_data}")

print("-------------------------------------------------")
def process_batch(items, batch_size=3):
    for i in range(0, len(items), batch_size):
        batch = items[i:i+batch_size]
        print(f"Processing batch {i//batch_size + 1}: {batch}")
        # Process batch...

# Example: Processing many documents
documents = [f"doc_{i}.txt" for i in range(10)]
process_batch(documents, 3)