###  Multiprocessing with ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def square(num):
    print(num)
    time.sleep(2)
    return f"Square: {num**2}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Multiprocessing and __name__ == "__main__":
# The target function assigned to a process runs in the child process independently.
# if __name__ == "__main__": ensures that top-level process creation code runs only in the main script, preventing child processes from recursively creating new processes.
# This is mandatory on Windows and recommended for cross-platform safety as in Wiodws each new process is assigned and executed by a new seperate Python Interpreter.

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)

    for result in results:
        print(result)

    
# Threads = lightweight → can use more max_workers (10 to 100+)
# Processes = heavy → use fewer max_workers (1–8)

# | Task type | max_workers suggestion       |
# | I/O-bound | Many threads (10–100+)       |
# | CPU-bound | Around number of cores (1–8) |