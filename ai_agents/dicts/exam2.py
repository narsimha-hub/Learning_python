agent_state = {
    "metadata": {
        "name": "ResearcherBot",
        "version": "1.0",
        "created": "2024-01-01"
    },
    "config": {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 1000
    },
    "memory": {
        "conversation": [],
        "facts": []
    },
    "status": {
        "is_running": True,
        "current_step": 0,
        "error_count": 0
    }
}
for key in agent_state["metadata"].keys():
    print(key)
    
for key,value in agent_state["status"].items():
    print(f"{key}:{value}")
    
model=agent_state["config"]["model"]
print(model)

streming=agent_state["status"]["streaming"]="True"
print(agent_state["status"])

# Agent state with nested structure
agent_state = {
    "metadata": {
        "name": "ResearcherBot",
        "version": "1.0",
        "created": "2024-01-01"
    },
    "config": {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 1000
    },
    "memory": {
        "conversation": [],
        "facts": []
    },
    "status": {
        "is_running": True,
        "current_step": 0,
        "error_count": 0
    }
}

# Access nested values
model = agent_state["config"]["model"]
print(f"Model: {model}")  # Model: gpt-4

# Update nested values
agent_state["config"]["temperature"] = 0.9
agent_state["status"]["current_step"] = 1

# Safely access nested (with default)
def get_nested(dictionary, keys, default=None):
    """Safely access nested dictionary values."""
    for key in keys:
        if isinstance(dictionary, dict):
            dictionary = dictionary.get(key)
            if dictionary is None:
                return default
        else:
            return default
    return dictionary

# Usage
model = get_nested(agent_state, ["config", "model"], "gpt-3.5-turbo")
print(f"Model: {model}")  # Model: gpt-4

version = get_nested(agent_state, ["metadata", "version"], "unknown")
print(f"Version: {version}")  # Version: 1.0

non_existent = get_nested(agent_state, ["config", "top_p"], 0.9)
print(f"Top P: {non_existent}")  # Top P: 0.9