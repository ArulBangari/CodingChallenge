"""
Filename: assignment1_tests.py
Author: Arul Bangari
Description:
    Test cases for ShoppingDataAnalyzer class.
"""

from data_analyzer import ShoppingDataAnalyzer
import pandas as pd

pd.set_option('display.float_format', '{:,.2f}'.format)

# Testing an empty dataframe
def test_empty_df():
    print("\n--- Running test_empty_df ---")
    csv_path = "./CSVs/empty.csv"
    sda = ShoppingDataAnalyzer(csv_path)

    try:
        print("Testing population grouped by gender")
        gender_counts = sda.count_population_by_gender()
        assert gender_counts is None
        print("Population grouped by gender works ✅")
    except AssertionError:
        print("Population grouped by gender failed ❌")

    try:
        print("Testing sales by gender")
        total_sales_by_gender = sda.total_sales_by_gender()
        assert total_sales_by_gender is None
        print("Sales by gender works ✅")
    except AssertionError:
        print("Sales by gender failed ❌")

    try:
        print("Testing most used payment method")
        most_used_payment_info = sda.most_used_payment_method()
        assert most_used_payment_info is None
        print("Most used payment method works ✅")
    except AssertionError:
        print("Most used payment method failed ❌")

    try:
        print("Testing day with most sales")
        date_with_most_sales_info = sda.day_with_most_sales()
        assert date_with_most_sales_info is None
        print("Day with most sales works ✅")
    except AssertionError:
        print("Day with most sales failed ❌")

# Testing a smaller csv file
def test_smaller_csv():
    print("\n--- Running test_smaller_csv ---")
    csv_path = "./CSVs/test.csv"
    sda = ShoppingDataAnalyzer(csv_path)
    
    try:
        print("Testing population grouped by gender")
        gender_counts = sda.count_population_by_gender()
        assert gender_counts["Female"] == 2
        assert gender_counts["Male"] == 2
        print("Population grouped by gender works ✅")
    except AssertionError:
        print("Population grouped by gender failed ❌")

    try:
        print("Testing sales by gender")
        total_sales_by_gender = sda.total_sales_by_gender()
        assert round(total_sales_by_gender["Female"], 2) == 22506.25
        assert round(total_sales_by_gender["Male"], 2) == 5701.61
        print("Sales by gender works ✅")
    except AssertionError:
        print("Sales by gender failed ❌")

    try:
        print("Testing most used payment method")
        most_used_payment, most_used_payment_freq = sda.most_used_payment_method()
        assert most_used_payment == ["Credit Card"]
        assert most_used_payment_freq == 2
        print("Most used payment method works ✅")
    except AssertionError:
        print("Most used payment method failed ❌")

    try:
        print("Testing day with most sales")
        date_with_most_sales, max_sales_amount = sda.day_with_most_sales()
        assert date_with_most_sales == ["16/05/2021"]
        assert round(max_sales_amount, 2) == 15004.25
        print("Day with most sales works ✅")
    except AssertionError:
        print("Day with most sales failed ❌")

# Testing where multiple payment have the same max count
def test_same_payment_method_count():
    print("\n--- Running test_same_payment_method_count ---")
    csv_path = "./CSVs/same_payment_count.csv"
    sda = ShoppingDataAnalyzer(csv_path)
    
    try:
        print("Testing population grouped by gender")
        gender_counts = sda.count_population_by_gender()
        assert gender_counts["Female"] == 5
        print("Population grouped by gender works ✅")
    except AssertionError:
        print("Population grouped by gender failed ❌")

    try:
        print("Testing sales by gender")
        total_sales_by_gender = sda.total_sales_by_gender()
        assert round(total_sales_by_gender["Female"], 2) == 17446.14
        print("Sales by gender works ✅")
    except AssertionError:
        print("Sales by gender failed ❌")

    try:
        print("Testing most used payment method")
        most_used_payment, most_used_payment_freq = sda.most_used_payment_method()
        expected = ["Cash", "Credit Card"]
        assert set(most_used_payment) == set(expected)
        assert most_used_payment_freq == 2
        print("Most used payment method works ✅")
    except AssertionError:
        print("Most used payment method failed ❌")

    try:
        print("Testing day with most sales")
        date_with_most_sales, max_sales_amount = sda.day_with_most_sales()
        assert date_with_most_sales == ["22/02/2022"]
        assert max_sales_amount == 16800
        print("Day with most sales works ✅")
    except AssertionError:
        print("Day with most sales failed ❌")

# Testing where multiple dates have the same max sales
def test_same_max_sales_date_amount():
    print("\n--- Running test_same_max_sales_date_amount ---")
    csv_path = "./CSVs/same_max_sales_date.csv"
    sda = ShoppingDataAnalyzer(csv_path)
    
    try:
        print("Testing population grouped by gender")
        gender_counts = sda.count_population_by_gender()
        assert gender_counts["Female"] == 5
        assert gender_counts["Male"] == 2
        print("Population grouped by gender works ✅")
    except AssertionError:
        print("Population grouped by gender failed ❌")

    try:
        print("Testing sales by gender")
        total_sales_by_gender = sda.total_sales_by_gender()
        assert round(total_sales_by_gender["Female"], 2) == 107559.75
        assert round(total_sales_by_gender["Male"], 2) == 55004.25
        print("Sales by gender works ✅")
    except AssertionError:
        print("Sales by gender failed ❌")

    try:
        print("Testing most used payment method")
        most_used_payment, most_used_payment_freq = sda.most_used_payment_method()
        assert most_used_payment == ["Cash"]
        assert most_used_payment_freq == 4
        print("Most used payment method works ✅")
    except AssertionError:
        print("Most used payment method failed ❌")

    try:
        print("Testing day with most sales")
        date_with_most_sales, max_sales_amount = sda.day_with_most_sales()
        expected = set(["9/5/2022", "17/10/2022", "22/01/2022"])
        assert set(date_with_most_sales) == expected
        assert max_sales_amount == 40000
        print("Day with most sales works ✅")
    except AssertionError:
        print("Day with most sales failed ❌")


def test():
    test_empty_df()
    test_smaller_csv()
    test_same_payment_method_count()
    test_same_max_sales_date_amount()

test()