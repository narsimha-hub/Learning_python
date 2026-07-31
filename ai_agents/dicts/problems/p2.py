messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    },
    {
        "role": "user",
        "content": "What is the weather in Paris?"
    }
]

messages.append({
    "role":"system",
    "content":"you are a helful chatbot"
})
print(messages)

api_payload = {
    "model": "gpt-4",
    "messages": len(messages),
    "temperature": 0.7,
    "max_tokens": 500
}
print(f"Chat with {api_payload["messages"]} messages")
for msg in messages:
    print(f"  {msg['role']}: {msg['content'][:30]}...")