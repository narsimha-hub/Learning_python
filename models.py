from pydantic import BaseModel
class Student(BaseModel):
    id:int
    name:str
    roll:int
    rank:int
    section:str