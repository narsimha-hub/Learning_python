'''Problem 6: List Performance Optimization (Advanced)
Scenario: Your agent needs to process millions of documents. You need to optimize list operations for speed and memory.

Tasks:

Use list comprehensions instead of loops where possible.

Use set for membership tests (O(1) vs O(n)).

Use generator expressions for lazy evaluation.

Use deque for efficient append/pop from both ends.

Batch processing to avoid memory issues.'''
import time
from collections import deque
import random

# Simulating large data
def generate_data(n):
    return [f"doc_{i}_{random.randint(1,1000)}" for i in range(n)]

# 1. List Comprehension vs Loop (Faster)
data = generate_data(1000000)

start = time.time()
# Slow way (loop with append)
result1 = []
for x in data:
    if "500" in x:
        result1.append(x)
print(f"Loop: {time.time() - start:.3f}s")

start = time.time()
# Fast way (list comprehension)
result2 = [x for x in data if "500" in x]
print(f"Comprehension: {time.time() - start:.3f}s")

# 2. Set for Membership (Much faster)
tool_names = ["search", "calculator", "email", "database", "weather", "api"]

# Slow O(n)
def check_tool_slow(name):
    return name in tool_names

# Fast O(1)
tool_set = set(tool_names)
def check_tool_fast(name):
    return name in tool_set

# 3. Deque for Efficient Queue Operations
# Regular list for queue (O(n) for pop(0))
queue_list = []
for i in range(100000):
    queue_list.append(i)
# queue_list.pop(0)  # Slow!

# Deque (O(1) for appendleft/popleft)
queue_deque = deque()
for i in range(100000):
    queue_deque.append(i)
# queue_deque.popleft()  # Fast!

# 4. Generator for Memory Efficiency
def process_large_documents(documents):
    # Generator yields one at a time
    for doc in documents:
        # Process doc
        yield f"Processed: {doc}"

# 5. Batching for Memory
def process_batches(data, batch_size=1000):
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        # Process batch
        print(f"Processing batch of {len(batch)} items")
        yield [f"Processed: {item}" for item in batch]

print("\n✅ Performance optimizations ready!")