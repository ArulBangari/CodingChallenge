"""
Filename: assignment1.py
Author: Arul Bangari
Description:
    This invokes the producer and consumer classes to copy a source container to a destination conatiner using a buffer(queue)
"""

from producer_consumer import Producer, Consumer
import queue
import threading
import math
import random

# Initializing container data and populating the source container
# Parameter:
#       n: integer, the size of the source array
# Returns:
#       Dictionary with elements:
#           source container, queue, destination container
def initialize_data(n):
    source = [None]*n
    dest = [None]*n
    q = queue.Queue(maxsize=math.ceil(n/2))

    # Populates the source container randomly with a double or int between 0 and 1000
    for i in range(n):
        if int(random.random() * 10) <= 4:
            source[i] = int(random.random() * 1000)
        else:
            source[i] = random.random() * 1000

    return {
        "source": source,
        "queue": q,
        "destination": dest,
        }

# Creating prod_num producer threads and cons_num consumer threads, running them, and
# checking if the entire data has been moved to the destination array
# Parameters:
#   - prod_num: number of producer threads
#   - cons_num: number of consumer threads
#   - initialized_data: dictionary with source, destination containers and queue
#   - prod_cd: cooldown period of production class
#   - cons_cd: cooldown period of consumer class
def create_and_run_threads(prod_num, cons_num, intitialized_data, prod_cd=0.5, cons_cd=0.5):
    source = intitialized_data["source"]
    q = intitialized_data["queue"]
    dest = intitialized_data["destination"]
    producer_index = [0]
    consumer_index = [0]
    producer_lock = threading.Lock()
    consumer_lock = threading.Lock()
    threads = []

    for _ in range(prod_num):
        p = Producer(source, q, producer_index, producer_lock, prod_cd)
        t = threading.Thread(target=p.produce)
        threads.append(t)
    
    for _ in range(cons_num):
        c = Consumer(q, dest, consumer_index, consumer_lock, cons_cd)
        t = threading.Thread(target=c.consume)
        threads.append(t)
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
    return

def main():
    length = 20 #length of the source array
    intitialized_data = initialize_data(length)
    source, dest = intitialized_data["source"], intitialized_data["destination"] #For printing source and destination arrays

    print("Source and destination list before running producer/consumer")
    print(f"Source: {source}\n")
    print(f"Destination: {dest}\n")

    prod_num, cons_num = 5, 5 #Initializing number of threads, sample of 5, can be changed
    create_and_run_threads(prod_num, cons_num, intitialized_data)

    print("-------------------------------------------------------------------\n")
    print("Source and destination list after running producer/consumer")
    print(f"Source: {source}\n")
    print(f"Destination: {dest}\n")

    print(f"*** Are source and destination equal? {dest == source}")


if __name__ == "__main__":
    main()