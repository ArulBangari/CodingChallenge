"""
Filename: assignment1.py
Author: Arul Bangari
Description:
    Test file for the producer and consumer class
"""

from assignment2 import create_and_run_threads, initialize_data
import random

# Testing random size and random inputs with 4 producers and 4 consumers
def test_random_size_and_input():
    print("Running test_random_size_and_input")
    length = int(random.random()* 50) + 5
    prod_num, cons_num = 4, 4
    create_run_compare(prod_num, cons_num, length, "test_random_size_and_input")

# Testing full queue with 5 producers, 1 consumer,
# cooldown period of 0.5 sec for producers and cooldown period of 0.75 sec for consumers
def test_full_queue():
    print("Running test_full_queue")
    length = 10
    prod_num, cons_num = 5, 1
    prod_cd, cons_cd = 0.5, 0.75
    create_run_compare(prod_num, cons_num, length, "test_full_queue", prod_cd, cons_cd)

# Testing empty queue with 1 producer, 5 consumers,
# cooldown period of 0.75 sec for producers and cooldown period of 0.5 sec for consumers
def test_empty_queue():
    print("Running test_empty_queue")
    length = 10
    prod_num, cons_num = 1, 5
    prod_cd, cons_cd = 0.75, 0.5
    create_run_compare(prod_num, cons_num, length, "test_empty_queue", prod_cd, cons_cd)

# Testing empty destination, source, and queue
def test_empty_source_dest_q():
    print("Running test_empty_source_dest_q")
    length = 0
    prod_num, cons_num = 2, 2
    create_run_compare(prod_num, cons_num, length, "test_empty_source_dest_q")

# Testing input of size 1 and 2 producers and consumers
def test_size_one_source_dest_q():
    print("Running test_size_one_source_dest_q")
    length = 1
    prod_num, cons_num = 2, 2
    create_run_compare(prod_num, cons_num, length, "test_size_one_source_dest_q")

# Calls initialize_data, create_and_run_threads, and compares the dest and source containers
def create_run_compare(prod_num, cons_num, length, test_name, prod_cd=0.5, cons_cd=0.5):
    intialized_data = initialize_data(length)
    source, dest = intialized_data["source"], intialized_data["destination"]
    print("Comparing source and destination list before running producer/consumer")

    try:
        assert source == dest
        print("Source and destination are the same!")
    except AssertionError:
        print("Source and destination aren't the same!")
    
    print("**********")
    create_and_run_threads(prod_num, cons_num, intialized_data, prod_cd, cons_cd)

    print("Comparing source and destination list after running producer/consumer")
    try:
        assert source == dest
        print(f"Test {test_name} passed! ✅")
    except AssertionError:
        print(f"Error: Test {test_name} failed, source container and destination container not same! ❌")
    print("---------------------------------------------------------")
    
def test():
    print("---------------------------------------------------------")
    test_random_size_and_input()
    test_full_queue()
    test_empty_queue()
    test_empty_source_dest_q()
    test_size_one_source_dest_q()

test()