def lowestheight():
    students = {}  
    num = int(input("Enter the number of students: "))
    for i in range(num):
        name = input("Enter student name: ")
        height = int(input("Enter student height (in cm): "))
        students[name] = height  
    print("Student Data:", students)
    min_height = min(students.values())
    for name, height in students.items():
        if height==min_height:print(f"{name} has the lowest height: {min_height} cm")
lowestheight()