customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
units_consumed = int(input("Enter Units Consumed: "))
bill_amount = 0
if units_consumed <= 199: bill_amount = units_consumed * 1.20
elif 200 <= units_consumed < 400:bill_amount = units_consumed * 1.50
elif 400 <= units_consumed < 600:bill_amount = units_consumed * 1.80
else: bill_amount = units_consumed * 2.00
if bill_amount > 400:
    surcharge = bill_amount * 0.15
    bill_amount += surcharge
if bill_amount < 100:bill_amount = 100
print(f"Total Bill Amount: Rs. {bill_amount:.2f}")