def shopping(cart_total,discount_percentage):
    total_price=(cart_total-(cart_total*(discount_percentage/100)))
    print(f"Total price :{total_price }Rupees")
cart_total=int(input("Enter the Items total price: "))
discount_percentage=int(input("Enter the discount percentage: "))
shopping(cart_total,discount_percentage)