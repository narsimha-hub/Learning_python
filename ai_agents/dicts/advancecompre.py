messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there"},
    {"role": "user", "content": "How are you?"}
]
role_messages={msg["role"]:msg["content"] for msg in messages}
print(role_messages)

grouped_msg={}
for msg in messages:
    if msg["role"] not in grouped_msg:
        grouped_msg[msg["role"]]=[]
    grouped_msg[msg["role"]].append(msg["content"])
print(grouped_msg)



