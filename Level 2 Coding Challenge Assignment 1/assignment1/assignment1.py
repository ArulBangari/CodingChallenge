"""
Filename: assignment1.py
Author: Arul Bangari
Description:
    This program calls the ShoppingDataAnalyzer class to analyze the given customer_shopping_data.csv file.
"""

from data_analyzer import ShoppingDataAnalyzer
import pandas as pd

pd.set_option('display.float_format', '{:,.2f}'.format)

def main():
    print("-----------------------------------------")
    print("1. Reading the data from the CSV file")
    csv_location = "./CSVs/customer_shopping_data.csv"
    sda = ShoppingDataAnalyzer(csv_location)

    if sda.check_if_empty():
        print("Error: Passed empty dataframe!")
        return
    
    gender_counts = sda.count_population_by_gender()
    print("2. Population grouped by gender")
    print("Population grouped by gender:\n")
    print(gender_counts.to_string())
    print("\n")

    total_sales_by_gender = sda.total_sales_by_gender()
    print("3.Total sales by gender:\n")
    print(total_sales_by_gender.to_string())
    print("\n")


    most_used_payments, most_used_payment_freq =  sda.most_used_payment_method()
    if len(most_used_payments) > 1:
        print(f"4. There are {len(most_used_payments)} payment types that are the most used, with frequency of {most_used_payment_freq}. The first 2 are shown below:")
        print(most_used_payments[0:2])
    else:
        print(f"4. There is 1 payment type that is the most used, with frequency of {most_used_payment_freq}. It is {most_used_payments[0]}.")
    print("\n")

    days_with_most_sales, max_sales_amount = sda.day_with_most_sales()
    if len(days_with_most_sales) > 1:
        print(f"5. The max sales amount is {max_sales_amount}. There are {len(days_with_most_sales)} days with the max sales. The first 2 days are shown below")
        print(days_with_most_sales[0:2])
    else:
        print(f"5. The max sales amount is {max_sales_amount}. There is 1 day with the max sales. It is {days_with_most_sales[0]}.")
        

main()