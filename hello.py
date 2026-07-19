# n=int(input())
# row=n
# while row>=1:
#     col=1
#     while col<row:
#         print("*",end="")
#         col+=1
#     print()
#     row-=1
# n=4
# row=1
# while row<=n:
#     col=1
#     while col<=row:
#         print("*",end="")
#         col+=1
#     print()
#     row+=1
        
        
# n=int(input())
# row=1
# while row<=n:
#     col=1
#     while col<=row:
#         print(row,end="")
#         col+=1
#     print()
#     row+=1
    
    
# n=int(input())
# row=1
# num=1
# while row<=n:
#     col=1
#     while col<=row:
#         print(num,end="")
        
#         num+=2
#         col+=1
#     print()
#     row+=1
    
# # n=int(input())
 
# from array import *
# arr=array('i',[1,2,3,4,5])
# print(type(arr.tolist()))
        

# def square(num):
#     return num*num
# def cube(num):
#     return num*num*num

# def operate(nums,operation):
#     for i in nums:
#         print( operation(i))
# nums=[5,6,7]
# operate(nums,square)
# # res=square(5)
# # print(res)
# # res=cube(5)
# # print(res)

# def great(func):
#     def wrap(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return wrap
    
        

# def sub(a,b):
#     return a-b

# def divide(a,b):
#     return a/b
# def add(a,b):
#     return a+b
# def squares(n):
#     return n*n
# sub=great(sub)
# add=great(add)
# res2=add(5,6)
# print(res2)
# res1=sub(2,4)
# print(res1)
# divide=great(divide)
# res3=divide(8,5)
# print(res3)






# def star(func):
#     def wrap(n):
        
#         func(n)
#         print(n*3)
#     return wrap
    
    
# def hash(func):
#     def wrap(n):
        
#         func(n)
#         print(n*3)
#     return wrap
    
# @star
# @hash
# def hello(n):
#    print("hello")
# ch=input()   
# hello(ch) 


# def star(func):

#     def wrapper():
#         print("*****")
#         func()
#         print("*****")

#     return wrapper


# def hash(func):

#     def wrapper():
#         print("#####")
#         func()
#         print("#####")

#     return wrapper


# @star
# @hash
# def hello():
#     print("Hello")

# hello()






# class Mobiles:
#     def __init__(self,cpu,ram,ssd):
#         self.cpu=cpu
#         self.ram=ram
#         self.ssd=ssd
        
#     def configure(self):
#         print("configure:",self.cpu,self.ram,self.ssd)
    
# android=Mobiles("snap","16GB","512")
# iphone=Mobiles("ios","16GB","1TB")
# android.configure()



# class Rank:
#     name="aryabhatta"
#     def __init__(self,behaviour,best_in,grade):
#         self.behaviour=behaviour
#         self.best_in=best_in
#         self.grade=grade       
#     def habbits(self):
#         print("habbits:",self.behaviour,self.best_in,self.grade)
#     @classmethod   
#     def clas_name(cls):
#         return cls.name
#     @staticmethod
#     def top_rank ():
#         return 1
# print(Rank.clas_name())
# s1=Rank("good","writing","reading")
# s2=Rank("bad","reading","reading")
# print(Rank.top_rank())
# s1.habbits()
# s2.habbits()


# class Teachers:
#     def __init__(self,habit,abilitys):
#         self.habit=habit
#         self.abilitys=abilitys
#     def habbits(self):
#         print("Teachers has:",self.habit)
#     def ability(self):
#         print("Teachers has:",self.abilitys)
#     @staticmethod
#     def marks(percent):
#         return percent* (100*3)/10

# class Students(Teachers):
#     def rollno(self):
#         print("roll no")
#     def name(self):
#         print("name")
        
        
# class princple(Students):
#     def __init__(self,habit,abilitys,name,height):
#         super().__init__(habit,abilitys)
#         self.name=name
#         self.height=height
    
#     def sir_height(self,weight):
#         print("height of the princple:",self.height,"weight of the sir:",weight)
#     def show_name(self):
#         print("name of the princple:",self.name)
        
        
# s1=princple("good","higher","narsimha",10)
# s1.rollno()
# print(Students.marks(1))
# s1.habbits()
# s1.sir_height(20)
# s1.show_name()




from abc import ABC,abstractmethod
# class vechile(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class bike(vechile):
    
#     def __init__(self, state):
#         self.state=state
        
#     def start(self):
        
#         if self.state =="on":
#             print("bike starts")
#         elif self.state =="off":
#             print("bike stops")
#         else:
#             print("get the key")
            
# class car(vechile):
#     def start(self):
#         print("start the car")
# b1=bike("off")
# b1.start()
# c1=car()
# c1.start()
    
    
    
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class rectangle(shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         return self.l*self.b
# class circle(shape):
#     def __init__(self,r,pi=3.14):
#         self.r=r
#         self.pi=3.14
#     def area(self):
#         return 2*self.pi*self.r*self.r
    
    
# a1=rectangle(10,20)
# print(a1.area())
# a2=circle(5)
# print(a2.area())




# class Notification(ABC):
#     @abstractmethod
#     def send(self,message):
#         pass
    
# class E_noti(Notification):
#     def __init__(self,messagee):
#         self.messagee=messagee 
    
#     def send(self,message):
#         print(f"email notifi is {message} {self.messagee}")
# class s_noti(Notification):
#     def send(self,message):
#         print(f"it is a sms {message}")
        
# m1=E_noti("hi")
# m1.send("hello")
# m2=s_noti()
# m2.send("your mobile recharge plan has been expired")



# class Bank_account(ABC):
#     @abstractmethod
#     def deposit(self):
#         pass
#     @abstractmethod
#     def withdraw(self):
#         pass
#     @abstractmethod
#     def display_balance(self):
#         pass
    
# class Savings_account(Bank_account):
#     def __init__(self,balance=0):
#         self.balance=0
        
#     def deposit(self,money):
#         self.balance+=money
#         print(self.balance)
        
#     def withdraw(self,m1):
#         self.balance-=m1
#         return self.balance
#     def display_balance(self):
#         return self.balance
        
# m1=Savings_account()

# m1.deposit(5000)
# print(m1.withdraw(2000))
# print(m1.display_balance())     



# from abc import ABC, abstractmethod

# class BankAccount(ABC):

#     @abstractmethod
#     def deposit(self, amount):
#         pass

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

#     @abstractmethod
#     def display_balance(self):
#         pass


# class SavingsAccount(BankAccount):

#     def __init__(self, balance=0):
#         self.balance = balance
#         self.transactions=[]

#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f"deposited {amount}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             self.transactions.append(f"withdraw {amount}")
#         else:
#             print("Insufficient Balance")
#             self.transactions.append(f"failed withdraw {amount} is insufficent balance")

#     def display_balance(self):
#         return self.balance
#     def show_tran(self):
#         for tran in self.transactions:
#             print(tran)
    
# class CurrentAccount(BankAccount):
    
#     def __init__(self, balance=0):
#         self.balance = balance
#         self.transaction_history=[]

#     def deposit(self, amount):
#         self.balance += amount
#         self.transaction_history.append(f"deposited {amount}")
        
#     def withdraw(self,amount):
#         if amount<=5000:
#             self.balance-=amount
#         else:
#             print("you can withdraw upto five thousand , according to the bank policy")
            
#     def display_balance(self):
#         return self.balance
#     def show_transaction(self):
#         for trans in self.transaction_history:
#             print(trans)
    
# account = SavingsAccount()
# account1=CurrentAccount()

# account1.withdraw(5001)

# account.deposit(5000)
# print(account.display_balance())

# account.withdraw(2000)
# print(account.display_balance())

# account.withdraw(5000)
# print(account.display_balance())
# account.show_tran()





# class dog: 
#     def speak(self):
#         print("barks")
#     def sounds(self):
#         pass
#       #  sounds.append(f"")
# class cat(dog):
#     def speak(self):
#         print("meow")
# class duck:
#     def __init__(self,sound):
#         self.sound=sound
#         self.sounds=[]
#     def speak(self):
#         print(self.sound)
        
# def my_sound(obj):
#     obj.speak()


    
# d1=dog()
# my_sound(dog())
# c1=cat()
# my_sound(cat())
# du1=duck("quakes")
# my_sound(du1)



class maths:
    
    def __init__(self,value=0):
        self.value=value
    def add(self,a,b):
        self.value=a+b
    def multi(self,a,b):
        self.value= a*b
    
    def __add__(self, other):
        return self.value+other.value
    
a1=maths()
a1.add(10,20)

# print(a1.add("narsi", "arun"))
a2=maths()
a2.multi(2,5)
print(a1+a2)