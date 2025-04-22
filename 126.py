num=int(input("Enter the number of elements: "))
s=[]
for i in range(num):
    num=int(input("Enter the numbers: "))
    s.append(num)
s1=set(s)
while True:
    print("***************************")
    print("1:Add an element\n2:Remove an element")
    print("3:Specific element exists in the set\n4:Display")
    choice=int(input("Enter your choice: "))
    print("***************************")
    if choice==1:
        new_num=int(input("Enter the number you want to add: "))
        s.append(new_num)
        s2=set(s)
        print(s2)
    elif choice==2:
        remove_num=int(input("Enter the number you want to remove: "))
        if remove_num in s2:
            s2.remove(remove_num)
            print(s2)
        else:print("Number is not available ")
    elif choice==3:
        search=int(input("Enter the number you want to search: "))
        if search in s2:
            print("It is present")
        else:print("It is not present")
    elif choice==4:
        print(s2)
    else:break