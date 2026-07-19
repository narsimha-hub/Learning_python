import asyncio
import time

# async def download():
    
#     await asyncio.sleep(2)
#     print(f"download complete")
#     return "file_zip"
# async def main():
#     start=time.perf_counter()
#     t1=asyncio.create_task(download())
#     print(f"download started")
    
#     for i in range(3):
#         print("main working")
#         await asyncio.sleep(1)
#     result=await t1
#     print(result)
#     end=time.perf_counter()
#     print(f"total time:{end-start:.2f}")
# asyncio.run(main())



import asyncio

# async def worker():
#     await asyncio.sleep(5)
#     return "done"

# async def main():
#     task = asyncio.create_task(worker())

#     print("1:", task.done())

#     await asyncio.sleep(2)

#     print("2:", task.done())

#     await asyncio.sleep(4)

#     print("3:", task.done())

#     print(await task)

# asyncio.run(main())


async def w1():
    await asyncio.sleep(1)
    return "A"

async def w2():
    await asyncio.sleep(3)
    return "B"

async def w3():
    await asyncio.sleep(5)
    return "C"
async def main():
    s=time.perf_counter()
    t1=asyncio.create_task(w1())
    t2=asyncio.create_task(w2())
    t3=asyncio.create_task(w3())
    await asyncio.sleep(2)
    print(t1.done(),
    t2.done(),
    t3.done())
    await asyncio.sleep(4)
    print(t1.done(),t2.done(),
    t3.done())
    
    results=await(t1),await(t2),await(t3)
    print(results)
    e=time.perf_counter()
    print(f"{e-s:.2f}")
asyncio.run(main())