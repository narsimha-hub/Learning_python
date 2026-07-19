from pydantic import BaseModel,Field

# # class User(BaseModel):
# #     u_name:str
# #     age:int
# #     email:str
    
# # user1=User("narsi","21","narsi@gmail.com")

# # print(user1)


# class Student(BaseModel):
#     name: str
#     age: int

# s = Student(name="Narsi", age=21)

# print(s)

# from pydantic import BaseModel

# class Student(BaseModel):
#     name: str
#     age: int

# s = Student(name="Narsi", age="21")
# data=s.model_dump()

# # print(data)
# # print(type(s.age))

# class student (BaseModel):
#     s_name:str=Field(min_length=5,pattern=r'^[a-z]+$')
#     age:int=Field(ge=18)
#     s_password:str=Field(min_length=8,max_length=20,patter=r'^[a-zA-Z0-9]+@')
# s=student(s_name="narsi",age=19,s_password='Nar$i@19')
# data=s.model_dump_json(indent=2)
# print(data)

import random

# class otp(BaseModel):
#     code:int=Field(default_factory=lambda:random.randint(100000,999999))
    
# c1=otp()
# c2=otp()
# print(c1)
# print(c2)





# from datetime import datetime
# # class time(BaseModel):
# #     time:datetime=Field(default_factory=datetime.now)
# #     items:list=Field(default_factory=list)
    
# # cur1=time()
# # cur1.items.append(cur1.time)
# # print(cur1)
# # cur1.items.append(10)
# # data=cur1.model_dump_json(indent=2)
# # print(data)



# class aliases(BaseModel):
#     first_name:str=Field(alias="firstname")
#     phone_number:str=Field(alias="phonenumber",pattern=r'^[6-9]\d{9}$')
    
# e1=aliases(firstname="narsi",phonenumber="9398865423")

# print(e1)



# class combine(BaseModel):
#     phone_number:str=Field(
#         validation_alias="phone",
#         serialization_alias="phonenumber"
        
#       )
# s1=combine(phone="9398865423")
# print(s1.model_dump_json(by_alias=True))




# from pydantic import BaseModel, Field

# class User(BaseModel):
#     name: str = Field( 
#         validation_alias="uname",
#         serialization_alias="username",
#         title="User Name",
#         description="Enter your full name",
#         examples=["Narsimha Reddy"]
#     )

#     age: int = Field(
#         gt=18,
#         title="Age",
#         description="Must be greater than 18",
#         examples=[21]
#     )
# u1=User(uname="narsi",age=19)
# print(u1.model_json_schema())