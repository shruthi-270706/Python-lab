tea_price,tiffin_price,extra_charge = 0,0,0
hotel_category = input("Enter the hotel category(5, 3, or 2): ")
if hotel_category == "5":
    tea_price = 100
    tiffin_price = 250
    extra_charge = 0.10
elif hotel_category == "3":
    tea_price = 50
    tiffin_price = 125
    extra_charge = 0.05
elif hotel_category == "2":
    tea_price = 30
    tiffin_price = 120
    extra_charge = 0.05
tea_cost =tea_price*5
tiffin_cost=tiffin_price*5
subtotal =tea_cost+tiffin_cost
total_cost=subtotal+(subtotal*extra_charge)
print(f"Total bill for hotel category {hotel_category}: ₹{total_cost:.2f}")