"""
Filename: data_analyzer.py
Author: Arul Bangari
Description:
    This program reads sales data from a CSV file and performs analysis such as:
    - Counting population grouped by gender
    - Finding total sales grouped by gender
    - Identifying the most used payment method
    - Finding the date with the highest total sales
    It uses pandas for data manipulation and returns the analyses.
"""

import pandas as pd

pd.set_option('display.float_format', '{:,.2f}'.format)

class ShoppingDataAnalyzer:
    def __init__(self, csv_location):
        self.df = pd.read_csv(csv_location)

    def check_if_empty(self):
        return self.df.empty


    # Counting the population grouped by gender
    # Returns a Series type which holds the count of each unique gender in the dataframe
    def count_population_by_gender(self):
        if self.check_if_empty():
            return None
        # Using value_counts() to get counts of each unique value in the column
        gender_counts = self.df["gender"].value_counts()
        return gender_counts
        

    # Total sales grouped by gender
    # Returns a series holding the sum of sales for each unique gender in the dataframe
    def total_sales_by_gender(self):
        if self.check_if_empty():
            return None
        # Creating a sales column if there isn't one
        if "sales" not in self.df.columns:
            self.df["sales"] = self.df["price"] * self.df["quantity"]

        # groupby("gender") splits the data into groups based on each unique value of gender, creating a separate group for each value
        total_sales_by_gender = self.df.groupby("gender")["sales"].sum()
        return total_sales_by_gender

    # Most used payment method
    # Returns a list holding the most used payment and the frequency of said most used payment
    def most_used_payment_method(self):
        if self.check_if_empty():
            return None
        
        # the index will be unique values in payment method and the values are the counts
        payment_counts = self.df["payment_method"].value_counts()
        # Get the max value
        most_used_payment_freq = payment_counts.max()
        # Use the max value to select all rows with max value and select the payment methods with .index
        most_used_payments = payment_counts.loc[payment_counts == most_used_payment_freq].index.tolist()
        return [most_used_payments, most_used_payment_freq]

    # Day with most sales
    # Returns a list that holds the date with the most sales and what the sales for that date was
    def day_with_most_sales(self):
        if self.check_if_empty():
            return None
        if "sales" not in self.df.columns:
            self.df["sales"] = self.df["price"] * self.df["quantity"]

        # Get the max value
        max_sales_amount = self.df["sales"].max()
        # Use the max value to select all the rows with max value
        days_with_most_sales = self.df.loc[self.df["sales"] == max_sales_amount, "invoice_date"].tolist()
        return [days_with_most_sales, max_sales_amount]