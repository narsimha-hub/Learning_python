agent_configure={
    "model":"gpt -5",
    "temperature":"0.7",
    "max_tokens":"50",
    "verbose":"True"
}
def validate_config(config):
    validated={}
    validated["model"]=str(config["model"])
    temp=float(config["temperature"])
    if temp<0.0 or temp>2.0:
        print(f"the output value is not hallicinated or failed to retrive")
        temp=0.7
    validated["temperature"]=temp
    tokens=int(config["max_tokens"])
    if tokens<100:
        tokens=100
    validated["max_tokens"]=tokens
    validated["verbose"]=bool(config["verbose"])
    return validated
validated_config=validate_config(agent_configure)
print(f"orginal:{agent_configure}")
print(f"validated:{validated_config}")


# user_query=input()
# if "weather" in user_query.lower():
#    # print(f"calling weather api")
# elif "calculate" in user_query.lower() or "math" in user_query.lower():
#    # print(f"calling calculator api")
# elif "country" or "capital" in user_query.lower():
#     #print("capital tool")
    
import time
import random   
attempt=1
max_attempts=5
succes=False

while attempt<max_attempts and  not succes:
    if random.random()<0.1:
        print(f"in the {attempt}attempt is succes")
        succes=True
        
    else:
        print(f"failure there is not at all attempt in {attempt}succes is reached")
        time.sleep(attempt)
        attempt+=1
if not succes:
    
    print(f"in all retries there is no sucees")
