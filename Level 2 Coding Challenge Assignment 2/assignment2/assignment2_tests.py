"""
Filename: assignment1.py
Author: Arul Bangari
Description:
    Test file for the producer and consumer class
"""

from assignment2 import create_and_run_threads, initialize_data
import random

# Testing random size and random inputs with 2 producers and 2 consumers
def random_size_and_input():
    print("Testing random size and random inputs")
    length = int(random.random()* 100) + 5
    prod_num, cons_num = 2, 2
    info = initialize_data(length)
    test_create_run(prod_num, cons_num, info, "random_size_and_input")

# Testing full queue with 5 producers, 1 consumer,
# cooldown period of 0.5 sec for producers and cooldown period of 0.75 sec for consumers
def test_full_queue():
    print("Testing full queue")
    length = 10
    prod_num, cons_num = 5, 1
    prod_cd, cons_cd = 0.5, 0.75
    info = initialize_data(length)
    test_create_run(prod_num, cons_num, info, "test_full_queue", prod_cd, cons_cd)

# Testing empty queue with 1 producer, 5 consumers,
# cooldown period of 0.75 sec for producers and cooldown period of 0.5 sec for consumers
def test_empty_queue():
    print("Testing empty queue")
    length = 10
    prod_num, cons_num = 1, 5
    prod_cd, cons_cd = 0.75, 0.5
    info = initialize_data(length)
    test_create_run(prod_num, cons_num, info, "test_empty_queue", prod_cd, cons_cd)

# Testing empty destination, source, and queue
def empty_source_dest_q():
    print("Testing dest size 0 and source size 0")
    length = 0
    prod_num, cons_num = 2, 2
    info = initialize_data(length)
    test_create_run(prod_num, cons_num, info, "empty_source_dest_q")

# Testing input of size 1 and 2 producers and consumers
def size_one_source_dest_q():
    print("Testing dest size 1 and source size 1")
    length = 1
    prod_num, cons_num = 2, 2
    info = initialize_data(length)
    test_create_run(prod_num, cons_num, info, "size_one_source_dest_q")

# Creating prod_num producer threads and cons_num consumer threads, running them, and
# checking if the entire data has been moved to the destination array
def test_create_run(prod_num, cons_num, info, test_name, prod_cd=0.5, cons_cd=0.5):
    source, dest = info[0], info[2]
    print("Source and destination list before running producer/consumer")
    print("Source container:")
    print(source)
    print("Destination container:")
    print(dest)
    
    create_and_run_threads(prod_num, cons_num, info, prod_cd, cons_cd)

    print("Source and destination list after running producer/consumer")
    print("Source container:")
    print(source)
    print("Destination container:")
    print(dest)
    print("---------------------------------------------------------")
    try:
        assert source == dest
        print(f"Test {test_name} passed!")
    except AssertionError:
        print(f"Error: Test {test_name} failed!")


def test():
    random_size_and_input()
    test_full_queue()
    test_empty_queue()
    empty_source_dest_q()
    size_one_source_dest_q()
    print("All tests passed!")

test()