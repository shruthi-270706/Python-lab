loan_amount=int(input("Enter the amount: "))
rate_of_interest=int(input("Enter the rate of interest: "))
num=int(input("Enter the number of months: "))
emi=(loan_amount*rate_of_interest*(1+rate_of_interest)**num)/((1+rate_of_interest)**num)-1
print(emi)