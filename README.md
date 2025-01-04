# Discount_calculator
calculate the final price of a product after deducting the discount if the discount is greater than 20% else you pay the original price

Calculate Discount Function

This Python program calculates the final price of an item after applying a discount. The program implements a function and provides an interactive way for users to input data and view results.

Features

The program defines a function named calculate_discount to compute the final price of an item based on a given discount percentage.

Discounts are applied only if the discount percentage is 20% or higher.

Interactive user input for the original price and discount percentage.

Prints the final price after applying the discount or retains the original price if the discount is less than 20%.

Function Description

calculate_discount(price, discount_percent)

This function takes two parameters:

price (float): The original price of the item.

discount_percent (float): The percentage discount to apply.

Returns:

The final price after the discount if the discount percentage is 20% or more.

The original price if the discount percentage is less than 20%.

Example Usage:

calculate_discount(100, 20)  # Returns 80.0
calculate_discount(100, 15)  # Returns 100.0

Usage Instructions

Run the script in a Python environment.

When prompted, enter the original price of the item as a numeric value.

Enter the discount percentage as a numeric value.

The program will display the final price after applying the discount.

Example Execution

Enter the original price of the item: 200
Enter the discount percentage: 25
The final price after applying the discount is: 150.0

Error Handling

Ensure that the input values are numeric. Non-numeric inputs will raise a ValueError.

Requirements

Python 3.x

License

This code is provided as-is for educational purposes and is free to use and modify.

Author: Ndung'u Ian Kinyanjui
