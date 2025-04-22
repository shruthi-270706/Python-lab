students=[]
while True:
    print("\n1:Add Details\n2:Display Details\n3:Search\n4:Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        name=input("Enter student name: ")
        age=int(input("Enter student age: "))
        grade=input("Enter student grade: ")
        students.append((name,age,grade))
    elif choice=="2":
        if not students:
            print("No students available.")
        else:
            for student in students:
                print(student)
    elif choice=="3":
        search_name=input("Enter the name you want to search: ")
        found=False
        for student in (students):
            if student[0]==search_name:
                print(student)
                found=True
                break
        if not found:print("Student not found ")
    elif choice=="4":break
    else: print("Invalid input")
        