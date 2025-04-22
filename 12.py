while True:
    num1=int(input("Enter the number1: "))
    num2=int(input("Enter the number2: "))
    maths=int(input("1.Add,2.Subtract,3.exit"))
    if(maths==1):
        num3=num1+num2
    if(maths==2):
        num3=num1-num2
    if(maths==3):
        print("Exit")
        break
print("Your answer is: ",num3)