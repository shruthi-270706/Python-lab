name=(input("enter the name "))
balance=0
acc_no=input("Enter the acc_no")
pin=input("Enter the pin")
if input("Enter you pin:")==pin:
    print("Name: ",name)
    print("Account_no:",acc_no)
    while True:
        print("\n1:deposit \n2:withdraw \n3:change pin \n4:exit")
        choice=input("Enter the choice")
        if choice=='1':
            amount=float(input("Enter the amount you want to add:"))
            balance+=amount
            print("Your balance is:",balance)
        elif choice=='2':
            amount=float(input("Enter the amount you want to withdraw:"))
            if amount<=balance:
                balance-=amount
                print("Your balance:",balance)
            else:print("Insufficient balance")
        elif choice=='3':
            pin=input("Enter new pin: ")
            print("Your pin is successfully implemented")
        elif choice=='4':
           print("Thank you for visiting our ATM ")
           break
        else:print("Invalid choice")
    else:print("Invalid pin")
    
 