# assignment_tool_system.py
# Build a complete tool system with validation and execution

from typing import Dict, Callable, Any, List
from pydantic import BaseModel, Field, ValidationError
import json
import asyncio

# Step 1: Define tool using Pydantic for validation
class SearchFlightsInput(BaseModel):
    destination: str = Field(..., description="City or airport code")
    departure_date: str = Field(..., description="Date in YYYY-MM-DD format")
    max_price: float = Field(default=float('inf'), description="Maximum price in USD")
    
    class Config:
        # This ensures Pydantic validates the schema matches
        pass
class CheckBudgetInput(BaseModel):
    user_id: str = Field(..., description="User ID")

# Step 2: Create tool registry
class ToolRegistry:
    """Central place to manage all tools"""
    
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}
    
    def register(self, name: str, description: str, input_schema: BaseModel, fn: Callable):
        """Register a tool"""
        
        self.tools[name] = {
            "name": name,
            "description": description,
            "input_schema": input_schema,
            "fn": fn,
            "openai_schema": self._to_openai_schema(input_schema)
        }
    
    def _to_openai_schema(self, pydantic_model: BaseModel) -> Dict:
        """Convert Pydantic model to OpenAI function calling schema"""
        
        schema = pydantic_model.model_json_schema()
        
        return {
            "type": "object",
            "properties": schema.get("properties", {}),
            "required": schema.get("required", [])
        }
    
    def get_tools_for_llm(self) -> List[Dict]:
        """Get tools in format LLM understands"""
        
        return [
            {
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool["description"],
                    "parameters": tool["openai_schema"]
                }
            }
            for tool in self.tools.values()
        ]
    
    async def call_tool(self, tool_name: str, arguments: Dict) -> Dict[str, Any]:
        """Call a tool safely"""
        
        if tool_name not in self.tools:
            return {"error": f"Tool {tool_name} not found"}
        
        tool = self.tools[tool_name]
        
        try:
            # Validate inputs using Pydantic
            input_model = tool["input_schema"]
            validated_input = input_model(**arguments)
            
            # Call the function
            fn = tool["fn"]
            result = await fn(**validated_input.model_dump())
            
            return {"success": True, "data": result}
        
        except ValidationError as e:
            return {"error": f"Input validation failed: {str(e)}"}
        
        except Exception as e:
            return {"error": f"Tool execution failed: {str(e)}"}

# Step 3: Define actual tool functions
async def search_flights_fn(destination: str, departure_date: str, max_price: float) -> Dict:
    """Actual flight search implementation"""
    
    # Simulate API call
    await asyncio.sleep(0.5)
    
    flights = [
        {"airline": "United", "price": 450, "departure": "08:00"},
        {"airline": "American", "price": 520, "departure": "10:30"},
        {"airline": "Spirit", "price": 380, "departure": "06:00"},
    ]
    
    filtered = [f for f in flights if f["price"] <= max_price]
    
    return {
        "destination": destination,
        "date": departure_date,
        "flights": filtered,
        "count": len(filtered)
    }

async def check_budget_fn(user_id: str) -> Dict:
    """Check user budget"""
    
    await asyncio.sleep(0.2)
    
    return {
        "user_id": user_id,
        "budget": 1000,
        "currency": "USD"
    }

# Step 4: Set up registry
async def main():
    registry = ToolRegistry()
    
    # Register tools
    registry.register(
        name="search_flights",
        description="Search for flights to a destination",
        input_schema=SearchFlightsInput,
        fn=search_flights_fn
    )
    
    registry.register(
        name="check_budget",
        description="Check user's available budget",
        input_schema=CheckBudgetInput,
        fn=check_budget_fn
    )
    
    # Show what LLM sees
    print("TOOLS AVAILABLE TO LLM:")
    print(json.dumps(registry.get_tools_for_llm(), indent=2))
    print("\n")
    
    # Test calling tools
    print("TEST 1: Valid tool call")
    result1 = await registry.call_tool("search_flights", {
        "destination": "Paris",
        "departure_date": "2026-08-20",
        "max_price": 500
    })
    print(f"Result: {json.dumps(result1, indent=2)}\n")
    
    print("TEST 2: Invalid tool call (missing required field)")
    result2 = await registry.call_tool("search_flights", {
        "destination": "Paris"
        # Missing departure_date!
    })
    print(f"Result: {json.dumps(result2, indent=2)}\n")
    
    print("TEST 3: Check budget")
    result3 = await registry.call_tool("check_budget", {
        "user_id": "user_123"
    })
    print(f"Result: {json.dumps(result3, indent=2)}\n")

# Run
asyncio.run(main())