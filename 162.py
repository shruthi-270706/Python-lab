def lowestmarks():
    students = {} 
    num = int(input("Enter the number of students: "))
    for i in range(num):
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        students[name] = marks 
    print(students)
    min_marks = min(students.values())
    for name, marks in students.items():
        if marks==min_marks:print(f"{name} has the lowest marks: {min_marks}")
lowestmarks()