# Create dictionary from lists
tools = ["search", "calculator", "email", "database"]
tool_status = {tool: "enabled" for tool in tools}
print(tool_status)
toolstate={tool: "diabled" for tool in tools}
print(toolstate)
fin_status={**tool_status,**toolstate}
print(fin_status)
# {'search': 'enabled', 'calculator': 'enabled', 'email': 'enabled', 'database': 'enabled'}

# Create dictionary with transformed values
models = ["gpt-4", "gpt-3.5-turbo", "claude-3"]
cost_map = {model: len(model) * 0.01 for model in models}
cost_maps={model: len(model)*0.01 for model in models}
print({**cost_map,**cost_maps})
# {'gpt-4': 0.05, 'gpt-3.5-turbo': 0.14, 'claude-3': 0.08}