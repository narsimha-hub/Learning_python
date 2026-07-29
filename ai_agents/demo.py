# # THE AGENT LOOP (Complete Implementation)
# import json 

# class AgentIteration:
#     """
#     One iteration of the agent loop.
#     This happens 1-10 times per agent run.
#     """
    
#     # STEP 1: OBSERVE
#     # What's the current situation?
#     observation = {
#         "step_number": 3,
#         "goal": "Book a flight to Paris under $500",
#         "memory_so_far": {
#             "checked_availability": True,
#             "available_flights": [...],
#             "budget_checked": True,
#             "budget": 1000
#         },
#         "previous_actions": [
#             {"tool": "search_flights", "result": "5 flights found"},
#             {"tool": "check_budget", "result": "budget: 1000"}
#         ],
#         "current_problem": "Need to filter flights under $500"
#     }
    
#     # STEP 2: BUILD CONTEXT FOR LLM
#     # Format observation into a prompt the LLM can reason about
#     context = f"""
# GOAL: {observation['goal']}

# MEMORY (what I've learned so far):
# {json.dumps(observation['memory_so_far'], indent=2)}

# AVAILABLE TOOLS:
# - search_flights(destination, max_price)
# - check_budget(user_id)
# - book_flight(flight_id)
# - get_price_history(destination)

# What should I do next?
# """
    
#     # STEP 3: REASON (Call LLM)
#     # LLM looks at context and decides next action
#     llm_response = claude.messages.create(
#         model="claude-3-5-sonnet",
#         max_tokens=1000,
#         system="You are a travel booking agent. Be helpful and efficient.",
#         messages=[{"role": "user", "content": context}]
#     )
    
#     # Example LLM response:
#     # "I see there are 5 flights. Three are under $500:
#     #  - United: $450 (8am)
#     #  - Southwest: $480 (9am)
#     #  - Spirit: $420 (10am)
#     #  
#     #  The best option is Spirit at $420. Should I book it?"
    
#     # STEP 4: PLAN (Extract tool call from LLM response)
#     # LLM's response might mention booking, so we extract that
#     decision = parse_llm_response(llm_response.content[0].text)
#     # Becomes: {"action": "book_flight", "flight_id": "spirit_420", "reason": "Cheapest option"}
    
#     # STEP 5: ACT (Execute the tool)
#     if decision["action"] == "book_flight":
#         result = book_flight(decision["flight_id"])
#         # Result: {"success": True, "booking_id": "BK-123", "confirmation_email": "sent"}
    
#     # STEP 6: UPDATE MEMORY
#     # Store what we learned
#     memory["booked_flight"] = decision["flight_id"]
#     memory["booking_confirmation"] = result["booking_id"]
#     memory["status"] = "booked"
    
#     # STEP 7: CHECK TERMINATION
#     # Is goal complete?
#     if memory["status"] == "booked":
#         return {
#             "success": True,
#             "result": f"Booked {decision['flight_id']} for ${decision['price']}",
#             "steps": step_number,
#             "memory": memory
#         }
    
#     # If goal not complete, loop continues
#     # Step counter increments
#     # Loop goes back to OBSERVE with new memory



# assignment_agent_loop.py
# Build the ENTIRE agent loop without frameworks

import asyncio
import json
from typing import Dict, List, Any
from datetime import datetime

class SimpleAgent:
    """
    Complete agent implementation from first principles.
    
    No LangGraph, no CrewAI, no frameworks.
    Just the core loop.
    """
    
    def __init__(self, goal: str, max_steps: int = 5):
        self.goal = goal
        self.max_steps = max_steps
        self.step = 0
        self.memory = {"goal": goal}
        self.history = []
        
    async def run(self) -> Dict[str, Any]:
        """Main agent loop"""
        
        print(f"\n{'='*60}")
        print(f"AGENT STARTING: {self.goal}")
        print(f"{'='*60}\n")
        
        while self.step < self.max_steps:
            print(f"\n[STEP {self.step + 1}/{self.max_steps}]")
            
            # STEP 1: OBSERVE
            observation = self._observe()
            print(f"📍 Observation: {observation}")
            
            # STEP 2: REASON (simulate LLM)
            decision = self._simulate_llm_reasoning(observation)
            print(f"🧠 Decision: {decision}")
            
            # STEP 3: ACT
            result = await self._execute_action(decision)
            print(f"🔧 Result: {result}")
            
            # STEP 4: UPDATE
            self._update_memory(result)
            
            # STEP 5: CHECK TERMINATION
            if self._is_goal_complete():
                print(f"\n✅ GOAL COMPLETE")
                return self._finalize()
            
            self.step += 1
        
        print(f"\n❌ MAX STEPS EXCEEDED")
        return self._finalize()
    
    def _observe(self) -> str:
        """What's the current situation?"""
        return f"Goal: {self.goal}, Step: {self.step}, Memory: {json.dumps(self.memory)}"
    
    def _simulate_llm_reasoning(self, observation: str) -> Dict:
        """Simulate what LLM would decide"""
        
        # In real version, call Claude/GPT-4 here
        # For now, use simple rules
        
        if "flight" and "hotel" in self.goal.lower():
            if not self.memory.get("flights_searched"):
                return {
                    "action": "search_flights",
                    "args": {"destination": "Paris", "max_price": 500}
                }
                
            elif not self.memory.get("hotels_searched"):
                            return {
                                "action":"search_hotels",
                                "args":{"destination":"Paris","max_price":100}
                            }
            
            elif not self.memory.get("budget_checked"):
                return {
                    "action": "check_budget",
                    "args": {}
                }
            else:
                return {
                    "action": "final_answer",
                    "content": "Found flights under budget. Trip is bookable."
                }
        
        return {"action": "final_answer", "content": "Completed"}
       
            
        
    
    async def _execute_action(self, decision: Dict) -> Dict:
        """Execute the decided action"""
        
        action = decision.get("action")
        
        if action == "search_flights":
            # Simulate API call
            await asyncio.sleep(0.5)
            return {
                "flights": [
                    {"price": 450, "airline": "United"},
                    {"price": 520, "airline": "American"}
                ]
            }
            
        elif action =="search_hotels":
            await asyncio.sleep(0.5)
            return {
                "hotels":[
                    {"price":90,"name":"Arun hotel"},
                    {"price":100,"name":"Narsi hotel"}
                ]
            }
        
        elif action == "check_budget":
            await asyncio.sleep(0.2)
            return {"budget": 1000}
        
        elif action == "final_answer":
            return {"answer": decision.get("content")}
        
        return {"error": f"Unknown action: {action}"}
    
    def _update_memory(self, result: Dict):
        """Store what we learned"""
        
        if "flights" in result:
            self.memory["flights_searched"] = True
            self.memory["flights"] = result["flights"]
        if "hotels" in result:
            self.memory["hotels_searched"]=True
            self.memory["hotels"]=result["hotels"]
        
        if "budget" in result:
            self.memory["budget_checked"] = True
            self.memory["budget"] = result["budget"]
        
        self.history.append({
            "step": self.step,
            "result": result
        })
    
    def _is_goal_complete(self) -> bool:
        """Is goal achieved?"""
        
        # For this example, goal is complete if we have flights + budget
        return (
            self.memory.get("flights_searched") and
            self.memory.get("hotels_searched") and
            self.memory.get("budget_checked")
        )
    
    def _finalize(self) -> Dict:
        """Return final result"""
        
        return {
            "success": self._is_goal_complete(),
            "goal": self.goal,
            "steps": self.step,
            "memory": self.memory,
            "history": self.history
        }

# Run it
async def main():
    agent = SimpleAgent("Find a flight to Paris under $500 and hotel under 100")
    result = await agent.run()
    
    print(f"\n{'='*60}")
    print("FINAL RESULT:")
    print(json.dumps(result, indent=2))
    print(f"{'='*60}")

# Run
asyncio.run(main())