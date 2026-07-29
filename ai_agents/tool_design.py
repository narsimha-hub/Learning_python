# THE TOOL CALLING PROTOCOL
# How LLMs and tools communicate

from typing import Dict, List, Any, Callable
from pydantic import BaseModel, Field
import json

# ============================================
# STEP 1: DEFINE TOOLS (What LLM sees)
# ============================================

class Tool:
    """A tool that an LLM can call"""
    
    def __init__(self, name: str, description: str, parameters: Dict):
        self.name = name
        self.description = description
        self.parameters = parameters
        
        # Format for sending to LLM (this is what Claude/GPT-4 sees)
        self.schema = {
            "type": "function",
            "function": {
                "name": name,
                "description": description,
                "parameters": parameters
            }
        }

# Example: Define search_flights tool
search_flights_tool = Tool(
    name="search_flights",
    description="Search for flights to a destination with optional filters",
    parameters={
        "type": "object",
        "properties": {
            "destination": {
                "type": "string",
                "description": "City or airport code (e.g., 'Paris', 'CDG')"
            },
            "departure_date": {
                "type": "string",
                "description": "Date in YYYY-MM-DD format"
            },
            "max_price": {
                "type": "number",
                "description": "Maximum price in USD (optional)"
            },
            "airline": {
                "type": "string",
                "description": "Specific airline preference (optional)"
            }
        },
        "required": ["destination", "departure_date"],
        "additionalProperties": False  # No unknown fields
    }
)

# Example: Define check_budget tool
check_budget_tool = Tool(
    name="check_budget",
    description="Check user's available budget for travel",
    parameters={
        "type": "object",
        "properties": {
            "user_id": {
                "type": "string",
                "description": "User ID to check budget for"
            }
        },
        "required": ["user_id"]
    }
)

# ============================================
# STEP 2: PRESENT TOOLS TO LLM
# ============================================

def create_agent_prompt_with_tools(goal: str, tools: List[Tool]) -> str:
    """Create prompt that tells LLM about available tools"""
    
    tools_description = json.dumps(
        [tool.schema for tool in tools],
        indent=2
    )
    
    prompt = f"""
You are a helpful travel booking assistant.

Your goal: {goal}

You have access to these tools:

{tools_description}

When you need to use a tool, respond with JSON in this format:
{{
  "tool": "tool_name",
  "arguments": {{"arg1": "value1", "arg2": "value2"}}
}}

After I tell you the tool result, you can call another tool or provide final answer.

Let's start. What would you like to do?
"""
    
    return prompt

# ============================================
# STEP 3: LLM SEES TOOLS AND DECIDES
# ============================================

def simulate_llm_decision(prompt: str) -> Dict[str, Any]:
    """
    Simulate what LLM would respond.
    
    In real version: call Claude API
    Here: simulate the response
    """
    
    # In reality, you'd do:
    # response = claude.messages.create(
    #     model="claude-3-5-sonnet",
    #     max_tokens=1000,
    #     messages=[{"role": "user", "content": prompt}]
    # )
    
    # For demo, simulate LLM response:
    llm_response = """
I'll help you find a flight to Paris. Let me start by searching for available flights.

{"tool": "search_flights", "arguments": {"destination": "Paris", "departure_date": "2026-08-20", "max_price": 500}}
"""
    
    # Parse LLM's response to extract tool call
    # Look for JSON in response
    import re
    json_match = re.search(r'\{.*\}', llm_response, re.DOTALL)
    
    if json_match:
        tool_call = json.loads(json_match.group())
        return {
            "reasoning": llm_response.split("{")[0],
            "tool": tool_call["tool"],
            "arguments": tool_call["arguments"]
        }
    
    return {"error": "No tool call found"}

# ============================================
# STEP 4: VALIDATE TOOL CALL
# ============================================

def validate_tool_call(tool_name: str, arguments: Dict, available_tools: Dict[str, Tool]) -> tuple[bool, str]:
    """
    Validate that:
    1. Tool exists
    2. Arguments match schema
    3. Required arguments provided
    """
    
    # Check tool exists
    if tool_name not in available_tools:
        return False, f"Tool '{tool_name}' not found"
    
    tool = available_tools[tool_name]
    required = tool.parameters.get("required", [])
    
    # Check required arguments provided
    for req in required:
        if req not in arguments:
            return False, f"Missing required argument: '{req}'"
    
    # Check argument types (simplified)
    properties = tool.parameters.get("properties", {})
    for arg_name, arg_value in arguments.items():
        if arg_name not in properties:
            return False, f"Unknown argument: '{arg_name}'"
        
        expected_type = properties[arg_name].get("type")
        if expected_type == "string" and not isinstance(arg_value, str):
            return False, f"Argument '{arg_name}' should be string, got {type(arg_value)}"
        elif expected_type == "number" and not isinstance(arg_value, (int, float)):
            return False, f"Argument '{arg_name}' should be number, got {type(arg_value)}"
    
    return True, "Valid"

# ============================================
# STEP 5: EXECUTE TOOL
# ============================================

class ToolResult:
    """Result from executing a tool"""
    
    def __init__(self, tool_name: str, success: bool, data: Any = None, error: str = None):
        self.tool_name = tool_name
        self.success = success
        self.data = data
        self.error = error
    
    def to_dict(self) -> Dict:
        return {
            "tool": self.tool_name,
            "success": self.success,
            "data": self.data if self.success else None,
            "error": self.error if not self.success else None
        }

def execute_tool(tool_name: str, arguments: Dict) -> ToolResult:
    """Execute the actual tool"""
    
    try:
        # In real system: call actual APIs
        # Here: simulate
        
        if tool_name == "search_flights":
            # Simulate API call
            destination = arguments.get("destination")
            departure_date = arguments.get("departure_date")
            max_price = arguments.get("max_price", float('inf'))
            
            # Simulated flight data
            all_flights = [
                {"id": 1, "airline": "United", "price": 450, "departure": "08:00"},
                {"id": 2, "airline": "American", "price": 520, "departure": "10:30"},
                {"id": 3, "airline": "Spirit", "price": 380, "departure": "06:00"},
            ]
            
            filtered = [f for f in all_flights if f["price"] <= max_price]
            
            return ToolResult(
                tool_name=tool_name,
                success=True,
                data={
                    "destination": destination,
                    "date": departure_date,
                    "flights": filtered
                }
            )
        
        elif tool_name == "check_budget":
            user_id = arguments.get("user_id")
            
            # Simulated budget check
            return ToolResult(
                tool_name=tool_name,
                success=True,
                data={
                    "user_id": user_id,
                    "available_budget": 1000,
                    "currency": "USD"
                }
            )
        
        else:
            return ToolResult(
                tool_name=tool_name,
                success=False,
                error=f"Unknown tool: {tool_name}"
            )
    
    except Exception as e:
        return ToolResult(
            tool_name=tool_name,
            success=False,
            error=str(e)
        )

# ============================================
# STEP 6: RETURN RESULT TO LLM
# ============================================

def format_tool_result_for_llm(result: ToolResult) -> str:
    """Format tool result so LLM can read it"""
    
    if result.success:
        return f"""
Tool '{result.tool_name}' executed successfully.

Result:
{json.dumps(result.data, indent=2)}

What would you like to do next?
"""
    else:
        return f"""
Tool '{result.tool_name}' failed.

Error: {result.error}

Please try a different approach or ask for help.
"""

# ============================================
# STEP 7: LLM RESPONDS WITH NEXT ACTION
# ============================================

def llm_next_decision(tool_result: str) -> Dict:
    """LLM sees result and decides next action"""
    
    # In reality: Call LLM again with result
    # LLM might:
    # - Call another tool
    # - Provide final answer
    # - Ask for clarification
    
    # Simulate LLM response
    response = """
Great! I found flights under $500. Let me check the budget.

{"tool": "check_budget", "arguments": {"user_id": "user_123"}}
"""
    
    # Parse response
    import re
    json_match = re.search(r'\{.*\}', response, re.DOTALL)
    
    if json_match:
        tool_call = json.loads(json_match.group())
        return {
            "type": "tool_call",
            "tool": tool_call["tool"],
            "arguments": tool_call["arguments"]
        }
    else:
        return {
            "type": "final_answer",
            "answer": response
        }

# ============================================
# COMPLETE EXAMPLE: Full Protocol Flow
# ============================================

def complete_protocol_example():
    """Walk through entire tool calling protocol"""
    
    print("\n" + "="*60)
    print("TOOL CALLING PROTOCOL EXAMPLE")
    print("="*60 + "\n")
    
    # Define tools
    tools = {
        "search_flights": search_flights_tool,
        "check_budget": check_budget_tool
    }
    
    # Step 1: Create prompt with tools
    prompt = create_agent_prompt_with_tools(
        goal="Find a cheap flight to Paris",
        tools=list(tools.values())
    )
    print("STEP 1: Prompt sent to LLM")
    print(prompt[:200] + "...\n")
    
    # Step 2: LLM decides
    decision = simulate_llm_decision(prompt)
    print(f"STEP 2: LLM decides to call tool: {decision['tool']}")
    print(f"        Arguments: {decision['arguments']}\n")
    
    # Step 3: Validate
    is_valid, msg = validate_tool_call(decision["tool"], decision["arguments"], tools)
    print(f"STEP 3: Validate tool call: {msg}")
    if not is_valid:
        print("        ❌ Invalid! Stop here.")
        return
    print("        ✅ Valid!\n")
    
    # Step 4: Execute
    result = execute_tool(decision["tool"], decision["arguments"])
    print(f"STEP 4: Execute tool: {decision['tool']}")
    print(f"        Result: {result.to_dict()}\n")
    
    # Step 5: Format for LLM
    result_text = format_tool_result_for_llm(result)
    print(f"STEP 5: Format result for LLM")
    print(result_text[:200] + "...\n")
    
    # Step 6: LLM's next decision
    next_decision = llm_next_decision(result_text)
    print(f"STEP 6: LLM's next decision: {next_decision}")
    
    print("\n" + "="*60)
    print("This loop repeats until LLM provides final answer")
    print("="*60 + "\n")

# Run it
# complete_protocol_example()