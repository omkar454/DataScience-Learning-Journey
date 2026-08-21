# Multithreading  ->  Concurrency (not parallel for CPU work)
# Multiprocessing	-> Actual parallelism (multiple CPU cores)
import threading
import datetime
import time

### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.


def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
          time.sleep(1.5)
          print(f"letter: {letter}")

# Create 2 thread-:
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()
# Starting the thread-:
t1.start()
t2.start()


### Wait for the threads to complete
t1.join()
t2.join()
# t = datetime.datetime.now()
# t = time.time()
# print_numbers()
# print_letter()

finished_time = time.time() - t
# finished_time = datetime.datetime.now() - t
print(finished_time)


# Ctrl+C Behavior:
# In multithreading, Ctrl+C interrupts only the main thread; background threads continue running.
# In multiprocessing, Ctrl+C interrupts all processes because each process runs in a separate interpreter and receives signals independently.