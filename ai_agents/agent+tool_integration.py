# complete_tool_agent_system.py
# Full integration of tools + agent loop + error handling

import asyncio
import json
from typing import Dict, List, Any
from pydantic import BaseModel, Field

# Tool definitions
class FlightSearchInput(BaseModel):
    destination: str
    departure_date: str
    max_price: float = 1000

class BudgetCheckInput(BaseModel):
    user_id: str

# Tool functions
async def search_flights(destination: str, departure_date: str, max_price: float) -> Dict:
    """Search for flights"""
    await asyncio.sleep(0.3)
    
    flights = [
        {"airline": "United", "price": 450, "duration": 8},
        {"airline": "American", "price": 520, "duration": 9},
        {"airline": "Spirit", "price": 380, "duration": 10},
    ]
    
    return {
        "success": True,
        "flights": [f for f in flights if f["price"] <= max_price]
    }

async def check_budget(user_id: str) -> Dict:
    """Check user budget"""
    await asyncio.sleep(0.2)
    
    return {
        "success": True,
        "budget": 1000,
        "available": 950  # Assume $50 already spent
    }

# Complete agent
class ToolCallingAgent:
    """
    Complete agent that:
    1. Reasons about what to do
    2. Calls tools safely
    3. Updates memory
    4. Repeats until goal complete
    """
    
    def __init__(self, goal: str, max_steps: int = 5):
        self.goal = goal
        self.max_steps = max_steps
        self.step = 0
        self.memory = {"goal": goal}
        self.tool_calls = []
    
    async def run(self) -> Dict[str, Any]:
        """Run agent"""
        
        print(f"\n{'='*60}")
        print(f"AGENT: {self.goal}")
        print(f"{'='*60}\n")
        
        while self.step < self.max_steps:
            print(f"[STEP {self.step + 1}]")
            
            # Decide what to do
            decision = await self._decide_action()
            
            if decision["type"] == "tool_call":
                # Call tool
                result = await self._safe_tool_call(decision)
                print(f"  Tool: {decision['tool']} → {result['status']}\n")
                
                # Update memory
                if result["status"] == "success":
                    self.memory[f"step_{self.step}"] = result["data"]
                else:
                    print(f"  Error: {result.get('error', 'Unknown')}")
            
            elif decision["type"] == "response":
                # Done
                return {
                    "success": True,
                    "response": decision["content"],
                    "steps": self.step,
                    "memory": self.memory
                }
            
            self.step += 1
        
        return {
            "success": False,
            "error": "Max steps exceeded",
            "steps": self.step
        }
    
    async def _decide_action(self) -> Dict:
        """Decide next action based on memory"""
        
        # Simple decision logic (in real version: call LLM)
        if not self.memory.get("flights_searched"):
            return {
                "type": "tool_call",
                "tool": "search_flights",
                "args": {
                    "destination": "Paris",
                    "departure_date": "2026-08-20",
                    "max_price": 500
                }
            }
        
        elif not self.memory.get("budget_checked"):
            return {
                "type": "tool_call",
                "tool": "check_budget",
                "args": {"user_id": "user_123"}
            }
        
        else:
            cheapest = min(self.memory["step_0"]["flights"], key=lambda x: x["price"])
            budget = self.memory["step_1"]["available"]
            
            if cheapest["price"] <= budget:
                return {
                    "type": "response",
                    "content": f"✅ Found flight: {cheapest['airline']} for ${cheapest['price']}"
                }
            else:
                return {
                    "type": "response",
                    "content": "❌ No flights within budget"
                }
    
    async def _safe_tool_call(self, decision: Dict) -> Dict:
        """Call tool with error handling"""
        
        tool_name = decision["tool"]
        args = decision["args"]
        
        try:
            if tool_name == "search_flights":
                result = await search_flights(**args)
            
            elif tool_name == "check_budget":
                result = await check_budget(**args)
            
            else:
                return {"status": "error", "error": f"Unknown tool: {tool_name}"}
            
            if result.get("success"):
                self.tool_calls.append({
                    "tool": tool_name,
                    "args": args,
                    "result": result,
                    "step": self.step
                })
                return {"status": "success", "data": result}
            else:
                return {"status": "error", "error": result.get("error", "Unknown error")}
        
        except asyncio.TimeoutError:
            return {"status": "error", "error": "Tool timeout"}
        
        except Exception as e:
            return {"status": "error", "error": str(e)}

# Test it
async def main():
    agent = ToolCallingAgent("Find a flight to Paris under $500")
    result = await agent.run()
    
    print(f"\n{'='*60}")
    print("RESULT:")
    print(json.dumps({
        "success": result["success"],
        "response": result.get("response"),
        "steps": result["steps"]
    }, indent=2))
    print(f"{'='*60}\n")

# Run
asyncio.run(main())