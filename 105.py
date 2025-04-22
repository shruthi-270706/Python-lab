def menu():
    numbers=int(input("Enter the number of numbers you want: "))
    l=[]
    for i in range(numbers):
        num=int(input("Enter the number: "))
        l.append(num)
    print(l)
    while True:
        if l:
            print("\n1:Insert an Element\n2:Insert an Element desired position\n3:Update an Element")
            print("4:Delete an Element\n5:Delete Element desired position\n6:Display\n7:Exit")
            choice=int(input("Enter your choice"))
            if choice==1:
                num1=int(input("Enter the number you want to insert: "))
                l.append(num1)
                print(l)
            elif choice==2:
                position=int(input("Enter the position: "))
                num1=int(input("Enter the number you want to insert: "))
                if position>=0 and position<=len(l):
                    l.insert(position,num1)
                else:print("Invalid")
                print(l)
            elif choice==3:
                position=int(input("Enter the position: "))
                if position>=0 and position<=len(l):
                    num1=int(input("Enter the new number to update: "))
                    l[position]=num1
                else:print("Invalid")
                print(l)
            elif choice==4:
                num1=int(input("Enter the number you want to delete: "))
                if num1 in l:
                    l.remove(num1)
                else:print("Invalid")
                print(l)
            elif choice==5:
                position=int(input("Enter the position: "))
                if position>=0 and position<=len(l):
                    l.pop(position)
                else:print("Invalid")
                print(l)
            elif choice==6:
                print(l)
            elif choice==7:
                print("Exiting the program")
                break
        else:print("Invalid input")
menu()