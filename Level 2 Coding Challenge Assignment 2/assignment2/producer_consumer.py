"""
Filename: assignment1.py
Author: Arul Bangari
Description:
    This program has two classes, a Producer and Consumer.
    - Producer: read numbers from the source container into the queue
    - Consumer: dequeues from the queue and writes into the source container
"""

import threading
import time
import queue
import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Producer():
    def __init__(self, source, q, pindex, plock, cd=0.5):
        self.source = source #source list
        self.q = q #queue/buffer
        self.cd = cd #how long the producer should wait after producing or finding out queue is full
        self.pindex = pindex #holds the current index all Producers are on
        self.plock = plock #holds the lock, only matters if multiple producers
    
    def produce(self):
        # Infinite loop to keep producing items until at the end of source list
        while True:
            try:
                # Get producer lock to access the index and add to the queue
                with self.plock:
                    # Break loop when reaching end of source list
                    if self.pindex[0] >= len(self.source):
                        break
                    
                    # Adding item at index to queue, can set block=True for letting consumer know that queue is full
                    self.q.put(self.source[self.pindex[0]], block=False)
                    logging.info(f"{threading.current_thread().name} produced: {self.source[self.pindex[0]]}")
                    self.pindex[0] += 1

                # Emulating cooldown period
                time.sleep(self.cd)
            # Letting consumer know that queue is full
            except queue.Full:
                logging.info(f"{threading.current_thread().name} tried producing, buy queue is full")
                # Waiting for consumer to consume
                time.sleep(self.cd)


class Consumer():
    def __init__(self, q, dest, cindex, clock, cd=0.5):
        self.q = q #queue/buffer
        self.dest = dest #destination list
        self.cd = cd #how long the consumer should wait after producing or finding out queue is full
        self.cindex = cindex #holds the current index all the Consumers are on
        self.clock = clock #holds the lock, only matters if multiple consumers

    def consume(self):
        # Infinite loop to keep consuming items until at the end of destination list
        while True:
            try:
                # Get consumer lock to access the index and add to the queue
                with self.clock:
                    # Break loop when reaching end of destination list
                    if self.cindex[0] >= len(self.dest):
                        break
                    # Adding item to destination list at cindex after dequeuing, can set block=True for letting producer know that queue is empty
                    curr_consume = self.q.get(block=False)
                    self.dest[self.cindex[0]] = curr_consume
                    logging.info(f"{threading.current_thread().name} consumed: {self.dest[self.cindex[0]]}")
                    self.cindex[0] += 1
                
                # Emulating cooldown period
                time.sleep(self.cd)
            # Letting producer know that queue is empty
            except queue.Empty:
                logging.info(f"{threading.current_thread().name} tried consuming, but queue is empty")
                # Waiting for producer to produce
                time.sleep(self.cd)