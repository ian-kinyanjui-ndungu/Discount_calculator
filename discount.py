def calculate_discount(price, discount_percent):
    """Calculates the final price and applies discout if the discount is greater than or equal to 20%"""
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

#final price
print(f"The final price after applying the discount is: {final_price}")