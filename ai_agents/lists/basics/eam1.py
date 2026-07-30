tools=["search","weather"]

tools.append("email")
print(tools)


tools.insert(1,"wikipedia")
print(tools)

tools.remove("search")
print(tools)

tools.pop(-1)
print(tools)

tools.clear()
print(tools)

# Real agent scenario: Dynamic tool loading
def load_tools_for_task(task_type):
    tools = []
    
    if task_type == "research":
        tools = ["web_search", "wikipedia", "news_api"]
    elif task_type == "math":
        tools = ["calculator", "equation_solver"]
    elif task_type == "coding":
        tools = ["code_interpreter", "github_search", "documentation"]
    else:
        tools = ["general_chat"]
    
    print(f"Loaded {len(tools)} tools for {task_type}: {tools}")
    return tools

# Test
load_tools_for_task("research")
load_tools_for_task("coding")
load_tools_for_task("fighting")