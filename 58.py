num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
while True:
    maths = int(input("1.Add,2.Subtract,3.Exit: "))
    if (maths==1):
        num3=num1+num2
    elif (maths==2):
        num3=num1-num2
    elif (maths==3):
        print("Exit")
        break 
    print("Your answer is:", num3)
    num1 = num3
    num2 = int(input("Enter the next number: "))