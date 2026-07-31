config = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 1000
}

# Direct access (raises KeyError if missing)
model = config["model"]
print(f"Model: {model}")  # Model: gpt-4
temp=config["temperature"]
print(f"{temp}")


model=config.get("model")
print(model)
# Using .get() (returns None or default if missing)
temperature = config.get("temperature", 0.5)
print(f"Temperature: {temperature}")  # Temperature: 0.7

# Accessing missing key safely
top_p = config.get("top_p", 0.9)  # Returns 0.9 (not in dict)
print(f"Top P: {top_p}")  # Top P: 0.9

# Check if key exists
if "max_tokens" in config:
    print(f"Max tokens: {config['max_tokens']}")
    
if "temperature" in config:
    print(f"temp:{config["temperature"]}")
    
config.update({"iter":10,"name":"llm model"})
print(config)

del config["iter"]
print(config)

removed=config.pop("max_tokens")
print(f"{removed}")
print(config)
# config.clear()
# print(config)

print("keys","-"*30)
for key in config:
    print(key)
    
for value in config.values():
    print(value)
    
for key,value in config.items():
    print(f"{key}:{value}")
    
keys=list(config.keys())
values=list(config.values())
print(f"{keys}:{values}")
print(values)
