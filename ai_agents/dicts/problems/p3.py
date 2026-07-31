class AgentState:
    def __init__(self):
        self.state = {
            "conversation": [],
            "tools_used": [],
            "current_step": 0,
            "metadata": {
                "start_time": None,
                "total_tokens": 0,
                "cost": 0.0
            },
            "context": {
                "user_info": {},
                "session_data": {}
            }
        }
    
    def add_message(self, role, content):
        self.state["conversation"].append({
            "role": role,
            "content": content,
            "timestamp": "2024-01-01T00:00:00"  # In reality, use datetime
        })
    
    def add_tool_usage(self, tool_name, success=True):
        self.state["tools_used"].append({
            "tool": tool_name,
            "success": success,
            "timestamp": "2024-01-01T00:00:00"
        })
        self.state["current_step"] += 1
    
    def update_metadata(self, tokens_used, cost):
        self.state["metadata"]["total_tokens"] += tokens_used
        self.state["metadata"]["cost"] += cost
    
    def get_state_summary(self):
        return {
            "steps": self.state["current_step"],
            "tokens": self.state["metadata"]["total_tokens"],
            "cost": self.state["metadata"]["cost"],
            "messages": len(self.state["conversation"]),
            "tools": self.state["tools_used"][-3:]  # Last 3 tools
        }

# Use the agent state
agent = AgentState()
agent.add_message("user", "What is AI?")
agent.add_tool_usage("search", True)
agent.add_message("assistant", "AI is artificial intelligence...")
agent.add_tool_usage("calculator", False)
agent.update_metadata(1500, 0.015)

print("Agent State Summary:")
summary = agent.get_state_summary()
for key, value in summary.items():
    print(f"  {key}: {value}")