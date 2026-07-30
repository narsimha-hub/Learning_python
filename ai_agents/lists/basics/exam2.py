tools = ["search", "calculator", "email", "database", "search", "weather"]
if "search" in tools:
    print("yes search is avaliable")
else:
    print("no such is founded")
    
try:
    position=tools.index("calculator")
    print("if found")
except:
    print("calculator not found")
results=[]  
counter=tools.count("search")
results.append(counter)
print(results)

keyword="sea"
matching_tools=[tool for tool in tools if keyword in tool]
print(matching_tools)

requiredtools=["search","wikipedia","games"]
available=[tool for tool in requiredtools if tool in tools]
print(available)
not_available=[tool for tool in requiredtools if tool not in tools]
print(not_available)

# Agent checks tool availability before executing
def execute_agent_task(task, required_tools, available_tools):
    # Check if all required tools are available
    missing = [tool for tool in required_tools if tool not in available_tools]
    
    if missing:
        print(f"⚠️ Missing tools: {missing}")
        print(f"Available: {available_tools}")
        return False
    
    print(f"✅ All tools available. Executing task: {task}")
    # Execute the task...
    return True

# Test
available_tools = ["search", "calculator", "email", "database"]
task1 = ["search", "calculator"]  # Both available
task2 = ["search", "weather_api"] # weather_api missing

execute_agent_task("Find weather", task1, available_tools)
execute_agent_task("Find weather", task2, available_tools)


conversation = [
    "Hello", "Hi", "How are you?", "I'm fine", "What's your name?",
    "I'm AI", "Can you help me?", "Yes", "I need weather info",
    "What city?", "Tokyo", "It's sunny", "Thank you"
]

print(conversation[:-3])
print(conversation[2:5])
print(conversation[::-1])

def keep_recent(conversation,n=5):
    return conversation[-n:] if len(conversation)>=n else conversation
recent_keep=keep_recent(conversation,5)
print(recent_keep)