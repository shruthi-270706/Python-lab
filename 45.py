total_cost = 0 
while True:
    quantity = int(input("Enter item quantity (or 0 to stop): "))  
    if quantity == 0:
        break  
    price = float(input("Enter item price: "))  
    total_cost += quantity * price  
print("Total cost of shopping cart:", total_cost)