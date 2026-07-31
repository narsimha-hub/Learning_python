# Complete tool definition in the OpenAI Agents SDK style
tool_definition = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name or coordinates"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "default": "celsius"
                }
            },
            "required": ["location"]
        }
    }
}

parameters=tool_definition["function"]["parameters"]
print(parameters)
# Access nested parameter info
parameters = tool_definition["function"]["parameters"]
properties = parameters["properties"]
required = parameters["required"]

print(f"Tool: {tool_definition['function']['name']}")
print(f"Required params: {required}")
print(f"Properties: {list(properties.keys())}")
print(f"unit:{tool_definition["function"]["parameters"]["properties"]["unit"].keys()}")