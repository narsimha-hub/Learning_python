# import asyncio
# async def narsi(name):
#     print(f"before timeout")
#     await asyncio.sleep(2)
#     print(f"first name:{name}")
# async def lastname(lname):
#     print (f"last name:{lname}")
#     await asyncio.sleep(1)
# async def main():
#     user1=await narsi("narsimha reddy")
#     user1=await lastname("akkala")
#     # result=[]
#     # # print(user)
#     # return result 
#     # # print(result)
# asyncio.run(main())


# import asyncio
# import time
# async def name(u_name):
#     print("program started")
#     print(f"{u_name}")
#     await asyncio.sleep(1)
# async def roll(number):
#     print (f"{number}is the roll number")
#     await asyncio.sleep(2)
# async def getsection(sname):
#     await asyncio.sleep(3)
#     print(f"{sname}")
# async def main():
#     start = time.perf_counter()
#     # user1_name=await name("narsi")
#     # user1_roll=await roll(25)
#     # user1_section=await getsection("c")
#     # since it is a asynchronous code but it takes 6 seconds to complete 
#     await asyncio.gather(
#         name("narsi"),
#         roll(25),
#         getsection("c")
#     )
#     end = time.perf_counter()

#     print(f"Total time: {end - start:.2f} seconds")
# asyncio.run(main())


# async def greet():
#     print("hello")
    
# # obj=greet()
# print(greet())


import asyncio
import time

async def s_name(name):
    print(f"started")
    await asyncio.sleep(5)
    print(name)
    return name
    
async def s_roll(roll):
    print(f"started")
    await asyncio.sleep(2)
    print(roll)
    return roll
async def s_section(section):
    print(f"started")
    await asyncio.sleep(1)
    print(section)
    return section
async def main():
    start=time.perf_counter()
    c1=asyncio.create_task(s_name("narsi"))
    # # x=c1
    c2=asyncio.create_task(s_roll(1930))
    # # y=c2
    c3=asyncio.create_task( s_section("c"))
    # # z=c3
    await c1
    await c2
    await c3
    # results=await asyncio.gather(s_name("narsi"),s_roll(1930),s_section("c"))
    # print(c1,c2,c3)
    # print(results)
    # name,roll,section=results
    # print(name)
    # print(roll)
    # print(section)
    # print(type(results))
    print(c1,c2,c3)
    end=time.perf_counter()
    print(f"total time:{end-start:.2f}")
asyncio.run(main())    
    