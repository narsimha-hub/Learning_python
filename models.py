from pydantic import BaseModel
class StudentCreate(BaseModel):
    name:str
    roll:int
    rank:int
    section:str
    
class Student(BaseModel):
    id:int 
    name:str
    roll:int
    rank:int
    section:str