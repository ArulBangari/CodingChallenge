"""
Filename: assignment1.py
Author: Arul Bangari
Description:
    This program calls the ShoppingDataAnalyzer class to analyze the given customer_shopping_data.csv file.
"""

from data_analyzer import ShoppingDataAnalyzer
import pandas as pd

pd.set_option('display.float_format', '{:,.2f}'.format)
file = open("output.txt", "w+")

def main():
    csv_location = "./CSVs/customer_shopping_data.csv"
    sda = ShoppingDataAnalyzer(csv_location)
    if sda.check_if_empty():
        file.write("Warning dataframe is empty!")
        return
    
    gender_counts = sda.count_population_by_gender()
    file.write("2. Population grouped by gender")
    file.write("Population grouped by gender:\n")
    file.write(gender_counts.to_string())
    file.write("\n")

    total_sales_by_gender = sda.total_sales_by_gender()
    file.write("3.Total sales by gender:\n")
    file.write(total_sales_by_gender.to_string())
    file.write("\n")


    most_used_payment, most_used_payment_freq =  sda.most_used_payment_method()
    file.write(f"4.Most used payment method: {most_used_payment} with {most_used_payment_freq} uses.")
    file.write("\n")

    date_with_most_sales, max_sales_count = sda.day_with_most_sales()
    file.write("5.\n")
    file.write(f"Day with most sales: {date_with_most_sales} with ${max_sales_count} in sales.")

main()