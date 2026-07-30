def smart_trim_conversation(messages, max_messages=5):
    """
    Trim conversation to max_messages while preserving system and last user message.
    Returns a new list (doesn't modify the original).
    """
    if len(messages) <= max_messages:
        return messages.copy()
    
    # Separate system message if present
    system_msg = None
    other_messages = []
    
    for msg in messages:
        if msg["role"] == "system" and system_msg is None:
            system_msg = msg
        else:
            other_messages.append(msg)
    
    # We need to keep the last user message
    # Find the last user message
    last_user_idx = -1
    for i in range(len(other_messages) - 1, -1, -1):
        if other_messages[i]["role"] == "user":
            last_user_idx = i
            break
    
    # If we found a user message, we must keep it
    # Calculate how many messages we can keep (excluding system)
    available_slots = max_messages - (1 if system_msg else 0)
    
    # Start from the end and work backwards to keep most recent
    result = []
    if system_msg:
        result.append(system_msg)
    
    # If we have a last user, we should keep it and messages around it
    if last_user_idx != -1:
        # We want to keep the window from last_user_idx backwards
        start_idx = max(0, last_user_idx - (available_slots - 1))
        end_idx = min(len(other_messages), start_idx + available_slots)
        result.extend(other_messages[start_idx:end_idx])
    else:
        # No user message found, keep the last N messages
        result.extend(other_messages[-available_slots:])
    
    return result

# Test
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI is artificial intelligence..."},
    {"role": "user", "content": "Tell me more about machine learning"},
    {"role": "assistant", "content": "Machine learning is a subset of AI..."},
    {"role": "user", "content": "What about deep learning?"},
    {"role": "assistant", "content": "Deep learning uses neural networks..."},
    {"role": "user", "content": "Can you give me an example?"}
]

trimmed = smart_trim_conversation(conversation, max_messages=5)
for msg in trimmed:
    print(f"{msg['role']}: {msg['content'][:30]}...")