# Multithreading

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
        
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")
        
# Create two threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)
        
t = time.time() 

t1.start()
t2.start()

# Wait for the thread to complete
t1.join()
t2.join()

f = time.time() - t
print(f"Finishing time: {f}")