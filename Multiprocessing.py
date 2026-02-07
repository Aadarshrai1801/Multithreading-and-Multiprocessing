# Multiprocessing

import multiprocessing
import time

def sqaure_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Sqaure of {i} is: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube of {i} is: {i*i*i}")
      
if __name__ == "__main__":
        
    # Create two processes
    p1 = multiprocessing.Process(target=sqaure_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    f = time.time() - t
    print(f"Finishing time: {f}")