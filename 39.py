credit_score=int(input("Enter the credit score: "))
annual_income=int(input("Enter the annual income: "))
if(credit_score>700):print("You are eligible for loan ")
elif(credit_score>600 and credit_score<700 and annual_income>50000):
    print("You are also eligible")
elif(credit_score>600 and credit_score<700 and annual_income<50000):
    print("You are not eligible for loan")
else : print("You are not eligible for loan")