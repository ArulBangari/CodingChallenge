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
def initialize_data(n):
    producer_index = [0]
    consumer_index = [0]
    producer_lock = threading.Lock()
    consumer_lock = threading.Lock()
    source = [None]*n
    dest = [None]*n
    q = queue.Queue(maxsize=math.ceil(n/2))

    for i in range(n):
        if int(random.random() * 10) <= 4:
            source[i] = int(random.random() * 1000)
        else:
            source[i] = random.random() * 1000
    return [source, q, dest, producer_index, producer_lock, consumer_index, consumer_lock]

# Creating prod_num producer threads and cons_num consumer threads, running them, and
# checking if the entire data has been moved to the destination array
def create_and_run_threads(prod_num, cons_num, info, prod_cd=0.5, cons_cd=0.5):
    source, q, dest, producer_index, producer_lock, consumer_index, consumer_lock = info
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
    # Creating the index for each producer and consumer and the locks
    producer_index = [0]
    consumer_index = [0]
    producer_lock = threading.Lock()
    consumer_lock = threading.Lock()

    length = 20
    info = initialize_data(length)
    source, dest = info[0], info[2]

    print("Source and destination list before running producer/consumer")
    print(f"Source: {source}")
    print(f"Destination: {dest}")

    prod_num, cons_num = 2, 2
    create_and_run_threads(prod_num, cons_num, info)

    print("Source and destination list after running producer/consumer")
    print(f"Source: {source}")
    print(f"Destination: {dest}")


if __name__ == "__main__":
    main()