numbers=int(input("Enter the number of numbers you want: "))
l=[]
for i in range(numbers):
    num=int(input("Enter the number: "))
    l.append(num)
print(l)
if l:
    print("\n1:Max\n2:Min\n3:Average\n4:Ascending order\n5:Descending order")
    choice=input("Enter Your choice: ")
    if choice=='1':print(f"Maximum element is {max(l)}")
    elif choice=='2':print(f"Minimum element is {min(l)}")
    elif choice=='3':print(f"Average is {sum(l)/len(l)}")
    elif choice=='4':
        l.sort()
        print(f"Ascending order is {l}")
    elif choice=='5':
        l.sort(reverse=True)
        print(f"Descending order is {l}")
else:print("Invalid input")