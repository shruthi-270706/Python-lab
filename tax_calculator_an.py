from finance import tax_calculator
amount = int(input("Enter the amount: "))
discount = int(input("Enter the discount: "))
final_discount = tax_calculator.calculator(amount, discount)
print(final_discount)