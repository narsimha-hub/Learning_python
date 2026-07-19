from fastapi import FastAPI
from models import Student

# app=FastAPI()
# @app.get("/")
# def home():
#     return {"message":"narsi"}
# @app.get("/myhome")
# def myhome():
#     return {"feel":"i love my home"}

# app=FastAPI()
# numbers={
#     1:1,
#     2:4,
#     3:9,
#     4:16
# }
# @app.get("/numbers/{num_id}")
# def square(num_id:int):
#     return{
#         "id":num_id,
#         "sqaure":numbers.get(num_id,"sqaure not found")
#     }



app=FastAPI()
students = [
    Student(
        id=1,
        name="Narsi",
        roll=23951,
        rank=1,
        section="A"
    ),
    Student(
        id=2,
        name="Sai",
        roll=2395113,
        rank=3,
        section="C"
    ),
    Student(
        id=3,
        name="Saigani",
        roll=23951131,
        rank=2,
        section="A"
    ),
     Student(
        id=3,
        name="prathik",
        roll=23951131,
        rank=3,
        section="A"
    )
]
@app.get("/students/first")
def first_student():
    
        return students[0]
        
    
@app.get("/students/last")
def last_student():
        return students[-1]
        
    
@app.get("/students/count")
def total():
    
    return {
        "count":len(students)
    }
@app.get("/students/{student_id}")
def get_students(student_id:int):
    # for product in products:
    #     if product["id"]==id:
    #         return product
    for student in students:
        if student.id==student_id:
            return student
        
    return "student not found"
@app.get("/students/name/{student_name}")
def get_studentname(student_name:str):
    for student in students:
        if student.name==student_name:
            return student
        
    return "student not found with the name"

@app.get("/students/rank/topper")
def top_rank(topper:int):
    for student in students:
        if student.rank==topper:
            return student
        
@app.get("/students/rank/stop")
def topp_rank():
    for student in students:
        if student.rank==3:
            return student 
        
@app.get("/students/section/{section_wise}")
def get_specificsec(section_wise:str):
    res=[]
    for student in students:
        if student.section==section_wise:
            res.append(student)
       
    return res
    if not res:
        return "student not found in the section as per the required"

