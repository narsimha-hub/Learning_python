from typing import Annotated
def search(
    question:Annotated[str,"question"],
    max_results:int=5
    
)->list[dict]:
    pass
    # print("basic")
    return f"{question} is basic"
res=search("ai")
print(res)

def settings(**kwargs):
    print(kwargs)
settings(
    temperature=0.7,
    model="gpt-5",
    memory=True
)