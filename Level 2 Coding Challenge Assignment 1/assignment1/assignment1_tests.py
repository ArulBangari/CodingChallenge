"""
Filename: assignment1_tests.py
Author: Arul Bangari
Description:
    Test cases for ShoppingDataAnalyzer class.
"""

from data_analyzer import ShoppingDataAnalyzer
import logging
import pandas as pd

pd.set_option('display.float_format', '{:,.2f}'.format)

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s [%(threadName)s] %(message)s"
)

def test(csv_path):
    sda = ShoppingDataAnalyzer(csv_path)
    if sda.check_if_empty():
        print("Warning dataframe is empty!")
        return
    
    gender_counts = sda.count_population_by_gender()
    print("Testing population grouped by gender")
    assert gender_counts["Female"] == 2
    assert gender_counts["Male"] == 2
    print("Population grouped by gender works")


    total_sales_by_gender = sda.total_sales_by_gender()
    print("Testing sales by gender")
    assert total_sales_by_gender["Female"] == 22506.25
    assert total_sales_by_gender["Male"] == 5701.61
    print("Sales by gender works")


    most_used_payment, most_used_payment_freq =  sda.most_used_payment_method()
    print("Testing most used payment method")
    assert most_used_payment == "Credit Card"
    assert most_used_payment_freq == 2
    print("Most used payment method works")

    date_with_most_sales, max_sales_count = sda.day_with_most_sales()
    print("Testing day with most sales")
    assert date_with_most_sales == "16/05/2021"
    assert max_sales_count == 15004.25
    print("Day with most sales works")

print("Testing on an empty dataframe")
test("./CSVs/empty.csv")
print("Testing on a small CSV file")
test("./CSVs/test.csv")