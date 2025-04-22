num = int(input("Enter the number of students: "))  
students = set()  
enrolled_students = set()   
subjects = []  
for i in range(num):  
    n = int(input("Enter the roll no. of student: "))  
    students.add(n)  
print("Student roll numbers:", students)  
while True:
    print("1: Enroll\n2: Remove\n3: Add\n4: View\n5: Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter the roll number: "))
        if n in students:
            if n in enrolled_students:
                print("Student is already registered")
            else:
                subject = input("Enter your subject: ")
                subjects.append((n, subject)) 
                enrolled_students.add(n)
                print(f"Student {n} is enrolled for {subject}")
        else:print("Roll no is not found")
    elif choice == 2:  
        n=int(input("Enter the rollno. you want to remove: "))
        if n in students:  
            found = False  
            for i in range(len(subjects)):  
                if subjects[i][0] == n:  
                    subjects.pop(i) 
                    enrolled_students.remove(n)  
                    print(f"Student {n} is removed from enrollment")  
                    found = True  
                    break  
            students.remove(n)  
            print(f"Student {n} is removed.")  
        else:  print(f"Student {n} not found.")  
    elif choice == 3:  
        n = int(input("Enter the new roll number: "))
        if n in students:print("Student is already there")
        else: 
            students.add(n)
            print(f"Student {n} is added")
    elif choice == 4: 
        if subjects:  
            for student, subject in subjects:  
                print(f"Student {student} is enrolled in {subject}")  
        else:print("No students enrolled in any subject.")
    elif choice == 5:break  
    else:print("Invalid choice, try again.")