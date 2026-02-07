# Real world example using Multiprocessing

import multiprocessing
import math
import sys
import time

# Increase the max number of digits for integer conversion
sys.set_int_max_str_digits(100000)

def factorial(number):
    print(f"Computing factorial of {number}...")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers = [999,1233,566,875]
    
    start_time = time.time()
    
    # Create a pool of worker process
    with multiprocessing.Pool() as pool:
        results= pool.map(factorial,numbers)
        
    end_time=time.time()-start_time
    
    print(f"results: {results}")
    print(f"Time taken: {end_time} seconds")