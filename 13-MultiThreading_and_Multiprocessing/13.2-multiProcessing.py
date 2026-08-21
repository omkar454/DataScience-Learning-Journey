import multiprocessing
import time
# Multithreading  ->  Concurrency (not parallel for CPU work)
# Multiprocessing	-> Actual parallelism (multiple CPU cores)


def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")


if __name__ == "__main__":

    ## create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()
    ## start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()
    
    finished_time = time.time() - t
    print(finished_time)

# Ctrl+C Behavior:
# In multithreading, Ctrl+C interrupts only the main thread; background threads continue running.
# In multiprocessing, Ctrl+C interrupts all processes because each process runs in a separate interpreter and receives signals independently.