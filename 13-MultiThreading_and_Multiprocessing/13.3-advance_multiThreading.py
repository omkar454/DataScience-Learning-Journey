# MultiThreading with Thread Pool Executor-:
from concurrent.futures import ThreadPoolExecutor
import time
def print_number(number):
    time.sleep(1)
    print(number)
    return f"Number: {number}"

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

t = time.time()
with ThreadPoolExecutor(max_workers=13) as executor:
    results = executor.map(print_number,numbers)
finished_time = time.time() - t

for result in results:
    print(result)
print(finished_time)

# Threads = lightweight → can use more max_workers (10 to 100+)
# Processes = heavy → use fewer max_workers (1–8)

# | Task type | max_workers suggestion       |
# | I/O-bound | Many threads (10–100+)       |
# | CPU-bound | Around number of cores (1–8) |
