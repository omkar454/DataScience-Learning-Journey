import multiprocessing
import math
import sys
import time

# Allows Python to print extremely large numbers (huge factorials) without error.
# 1 lakh number of diigits allowed for STRING Conversion
sys.set_int_max_str_digits(100000)

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

# multiprocessing.Pool() creates a fixed number of worker processes equal to the machine’s logical CPU cores (e.g., 4 on a 2-core/4-thread CPU). These processes execute tasks in parallel and reuse the same workers for multiple inputs. The number of tasks does not increase the number of processes.

# multiprocessing.Pool() with 4 cores works just like ProcessPoolExecutor(max_workers=4) —
# fixed number of processes, unlimited number of tasks.

if __name__ == "__main__":
    numbers=[5000,6000,7000,8000]

    start_time = time.time()
    print(multiprocessing.cpu_count())

    #     multiprocessing.cpu_count() gave 4, so:
    # ✔ multiprocessing.Pool() will create exactly 4 processes
    # (and these 4 processes will handle all tasks in the list).

    # create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,numbers)

    # results = pool.map(func, numbers)-:
    # returns a list containing the outputs of func for each item in numbers, in the same order as the input list.

    #  So results is always a list.

        end_time = time.time() - start_time

        print(f"Results: {results}")
        print(f"Time taken: {end_time} seconds")