# Start with empty registry
tool_registry = []

def add_tool(registry, name, description):
    """Add a new tool to the registry."""
    # Check if tool already exists
    for tool in registry:
        if tool["name"] == name:
            print(f"⚠️ Tool '{name}' already exists. Skipping.")
            return
    registry.append({
        "name": name,
        "description": description,
        "enabled": True
    })
    print(f"✅ Added tool: {name}")

def remove_tool(registry, name):
    """Remove a tool from the registry."""
    for i, tool in enumerate(registry):
        if tool["name"] == name:
            removed = registry.pop(i)
            print(f"🗑️ Removed tool: {name}")
            return removed
    print(f"❌ Tool '{name}' not found.")
    return None

def enable_tool(registry, name, enabled=True):
    """Enable or disable a tool."""
    for tool in registry:
        if tool["name"] == name:
            tool["enabled"] = enabled
            status = "enabled" if enabled else "disabled"
            print(f"🔄 Tool '{name}' {status}")
            return True
    print(f"❌ Tool '{name}' not found.")
    return False

def get_enabled_tools(registry):
    """Get list of enabled tool names."""
    return [tool["name"] for tool in registry if tool["enabled"]]

def get_tool_descriptions(registry):
    """Get descriptions of enabled tools."""
    return [f"{tool['name']}: {tool['description']}" 
            for tool in registry if tool["enabled"]]

def process_tools(registry):
    """Print all tools with their status."""
    print("\n📋 TOOL REGISTRY")
    print("-" * 30)
    for tool in registry:
        status = "✅ ENABLED" if tool["enabled"] else "❌ DISABLED"
        print(f"{tool['name']:15} {status}")
        print(f"   {tool['description']}")
    print("-" * 30)

# Test it!
print("🚀 Starting Agent Tool Registry\n")

# Add tools
add_tool(tool_registry, "search", "Search the web for information")
add_tool(tool_registry, "calculator", "Perform mathematical calculations")
add_tool(tool_registry, "email", "Send emails")
add_tool(tool_registry, "database", "Query internal database")

# Remove a tool
remove_tool(tool_registry, "email")

# Disable database
enable_tool(tool_registry, "database", enabled=False)

# Show registry
process_tools(tool_registry)

# Get enabled tools
enabled = get_enabled_tools(tool_registry)
print(f"\n✅ Enabled tools: {enabled}")

# Get descriptions
descriptions = get_tool_descriptions(tool_registry)
print(f"📝 Descriptions:\n  " + "\n  ".join(descriptions))