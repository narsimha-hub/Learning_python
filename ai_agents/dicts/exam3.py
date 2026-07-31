tool_results = {
    "search": {"status": "success", "time": 1.2},
    "calculator": {"status": "error", "time": 0.3},
    "weather": {"status": "success", "time": 2.5},
    "email": {"status": "error", "time": 3.1}
}
# tool_value={tool: if tool_results[tool]["status"]=="success" for tool in tool_results}
success_tools={
    name:details
    for name,details in tool_results.items()
    if details["status"]=="success"
        
}
print("successfull status details are returned")
for key,value in success_tools.items():
    print(key,value)