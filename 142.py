students_name = {}
while True:
    print("\n1:Add\n2:Update\n3:Add Marks\n4:View details\n5:Average\n6:Highest & Lowest\n7:Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:  
        name = input("Enter student name: ")
        if name in students_name:print(f"{name} is already in records")
        else:
            grade = int(input(f"Enter {name}'s Marks: "))
            students_name[name] = [grade] 
            print(f"{name} is added with marks: {grade}")
    elif choice == 2:  
        name = input("Enter student name: ")
        if name in students_name:
            grade = int(input(f"Enter {name}'s updated Marks: "))
            students_name[name] = [grade]
            print(f"{name}'s marks updated to: {grade}")
        else:print(f"{name} is not present in records")
    elif choice == 3: 
        name = input("Enter student name: ")
        if name in students_name:
            num = int(input(f"How many subject marks you want to add for {name}?: "))
            for i in range(num):
                grade = int(input(f"Enter marks {i + 1}: "))
                students_name[name].append(grade) 
            print(f"Updated marks for {name}: {students_name[name]}")
        else:print(f"{name} is not present in records")
    elif choice == 4:  
        name = input("Enter student name: ")
        if name in students_name: print(f"{name}'s marks: {students_name[name]}")
        else:print(f"{name} is not present in records")
    elif choice == 5:  
        name = input("Enter student name: ")
        if name in students_name:
            average = sum(students_name[name]) / len(students_name[name])
            print(f"{name}'s Average is {average:.2f}")  
        else:print(f"{name} is not present in records")
    elif choice == 6:  
        name = input("Enter student name: ")
        if name in students_name:
            print(f"{name}'s Highest marks: {max(students_name[name])}")
            print(f"{name}'s Lowest marks: {min(students_name[name])}")
        else:print(f"{name} is not present in records")
    elif choice == 7: 
        print("Exit")
        break
    else:print("Invalid input.")