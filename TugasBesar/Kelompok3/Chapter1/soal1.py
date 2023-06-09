import threading
import time
import queue
import random

# Initialize a RLock
rlock = threading.RLock()

# Initialize inventory as a LIFO queue
inventory = queue.LifoQueue()

# Function to read inventory
def read_inventory():
    while True:
        with rlock:
            # Wait for inventory to be available
            if not inventory.empty():
                item = inventory.get()
                print("Reading inventory:", item)
        time.sleep(1)

# Function to write to inventory
def write_inventory(item):
    with rlock:
        print("Writing to inventory:", item)
        inventory.put(item)

# Create threads for reading inventory
read_thread1 = threading.Thread(target=read_inventory)
read_thread2 = threading.Thread(target=read_inventory)

# Create threads for writing to inventory
write_thread1 = threading.Thread(target=write_inventory, args=("Samsung",))
write_thread2 = threading.Thread(target=write_inventory, args=("Iphone",))
write_thread3 = threading.Thread(target=write_inventory, args=("Nokia",))

# Start the threads
read_thread1.start()
read_thread2.start()
write_thread1.start()
write_thread2.start()
write_thread3.start()

# Wait for the threads to finish
read_thread1.join()
read_thread2.join()
write_thread1.join()
write_thread2.join()
write_thread3.join()
