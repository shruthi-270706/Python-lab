amount = int(input("Enter the amount of shopping: "))
membership_card = input("Enter y/n for membership card:")
if amount > 100:
    print("You have a discount of 15%")
    discount = 15
elif 50 <= amount <= 100:
    print("You have a discount of 10%")
    discount = 10
else:
    print("Sorry, you don't have any discount")
    discount = 0
if membership_card == 'y':
    discount += 5
total = amount - (amount * discount / 100)
print("Your total bill is:", total)